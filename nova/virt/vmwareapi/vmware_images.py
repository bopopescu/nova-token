begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
string|'"""\r\nUtility functions for Image transfer.\r\n"""'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'glance'
name|'import'
name|'client'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'io_util'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'read_write_util'
newline|'\r\n'
nl|'\r\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.vmwareapi.vmware_images"'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\r\n'
nl|'\r\n'
DECL|variable|QUEUE_BUFFER_SIZE
name|'QUEUE_BUFFER_SIZE'
op|'='
number|'10'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|start_transfer
name|'def'
name|'start_transfer'
op|'('
name|'read_file_handle'
op|','
name|'data_size'
op|','
name|'write_file_handle'
op|'='
name|'None'
op|','
nl|'\r\n'
name|'glance_client'
op|'='
name|'None'
op|','
name|'image_id'
op|'='
name|'None'
op|','
name|'image_meta'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Start the data transfer from the reader to the writer.\r\n    Reader writes to the pipe and the writer reads from the pipe. This means\r\n    that the total transfer time boils down to the slower of the read/write\r\n    and not the addition of the two times."""'
newline|'\r\n'
comment|'# The pipe that acts as an intermediate store of data for reader to write'
nl|'\r\n'
comment|'# to and writer to grab from.'
nl|'\r\n'
name|'thread_safe_pipe'
op|'='
name|'io_util'
op|'.'
name|'ThreadSafePipe'
op|'('
name|'QUEUE_BUFFER_SIZE'
op|','
name|'data_size'
op|')'
newline|'\r\n'
comment|'# The read thread. In case of glance it is the instance of the'
nl|'\r\n'
comment|'# GlanceFileRead class. The glance client read returns an iterator'
nl|'\r\n'
comment|'# and this class wraps that iterator to provide datachunks in calls'
nl|'\r\n'
comment|'# to read.'
nl|'\r\n'
name|'read_thread'
op|'='
name|'io_util'
op|'.'
name|'IOThread'
op|'('
name|'read_file_handle'
op|','
name|'thread_safe_pipe'
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'# In case of Glance - VMWare transfer, we just need a handle to the'
nl|'\r\n'
comment|'# HTTP Connection that is to send transfer data to the VMWare datastore.'
nl|'\r\n'
name|'if'
name|'write_file_handle'
op|':'
newline|'\r\n'
indent|'        '
name|'write_thread'
op|'='
name|'io_util'
op|'.'
name|'IOThread'
op|'('
name|'thread_safe_pipe'
op|','
name|'write_file_handle'
op|')'
newline|'\r\n'
comment|'# In case of VMWare - Glance transfer, we relinquish VMWare HTTP file read'
nl|'\r\n'
comment|'# handle to Glance Client instance, but to be sure of the transfer we need'
nl|'\r\n'
comment|'# to be sure of the status of the image on glnace changing to active.'
nl|'\r\n'
comment|'# The GlanceWriteThread handles the same for us.'
nl|'\r\n'
dedent|''
name|'elif'
name|'glance_client'
name|'and'
name|'image_id'
op|':'
newline|'\r\n'
indent|'        '
name|'write_thread'
op|'='
name|'io_util'
op|'.'
name|'GlanceWriteThread'
op|'('
name|'thread_safe_pipe'
op|','
nl|'\r\n'
name|'glance_client'
op|','
name|'image_id'
op|','
name|'image_meta'
op|')'
newline|'\r\n'
comment|'# Start the read and write threads.'
nl|'\r\n'
dedent|''
name|'read_event'
op|'='
name|'read_thread'
op|'.'
name|'start'
op|'('
op|')'
newline|'\r\n'
name|'write_event'
op|'='
name|'write_thread'
op|'.'
name|'start'
op|'('
op|')'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
comment|'# Wait on the read and write events to signal their end'
nl|'\r\n'
indent|'        '
name|'read_event'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\r\n'
name|'write_event'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\r\n'
comment|'# In case of any of the reads or writes raising an exception,'
nl|'\r\n'
comment|"# stop the threads so that we un-necessarily don't keep the other one"
nl|'\r\n'
comment|'# waiting.'
nl|'\r\n'
indent|'        '
name|'read_thread'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'write_thread'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'# Log and raise the exception.'
nl|'\r\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\r\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'exc'
op|')'
newline|'\r\n'
dedent|''
name|'finally'
op|':'
newline|'\r\n'
comment|'# No matter what, try closing the read and write handles, if it so'
nl|'\r\n'
comment|'# applies.'
nl|'\r\n'
indent|'        '
name|'read_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\r\n'
name|'if'
name|'write_file_handle'
op|':'
newline|'\r\n'
indent|'            '
name|'write_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|fetch_image
dedent|''
dedent|''
dedent|''
name|'def'
name|'fetch_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Fetch an image for attaching to the newly created VM."""'
newline|'\r\n'
comment|'# Depending upon the image service, make appropriate image service call'
nl|'\r\n'
name|'if'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.glance.GlanceImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'func'
op|'='
name|'_get_glance_image'
newline|'\r\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.s3.S3ImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'func'
op|'='
name|'_get_s3_image'
newline|'\r\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.local.LocalImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'func'
op|'='
name|'_get_local_image'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|'"The Image Service %s is not implemented"'
op|')'
nl|'\r\n'
op|'%'
name|'FLAGS'
op|'.'
name|'image_service'
op|')'
newline|'\r\n'
dedent|''
name|'return'
name|'func'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|upload_image
dedent|''
name|'def'
name|'upload_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Upload the newly snapshotted VM disk file."""'
newline|'\r\n'
comment|'# Depending upon the image service, make appropriate image service call'
nl|'\r\n'
name|'if'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.glance.GlanceImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'func'
op|'='
name|'_put_glance_image'
newline|'\r\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.s3.S3ImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'func'
op|'='
name|'_put_s3_image'
newline|'\r\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.local.LocalImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'func'
op|'='
name|'_put_local_image'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|'"The Image Service %s is not implemented"'
op|')'
nl|'\r\n'
op|'%'
name|'FLAGS'
op|'.'
name|'image_service'
op|')'
newline|'\r\n'
dedent|''
name|'return'
name|'func'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|_get_glance_image
dedent|''
name|'def'
name|'_get_glance_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Download image from the glance image server."""'
newline|'\r\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Downloading image %s from glance image server"'
op|')'
op|'%'
name|'image'
op|')'
newline|'\r\n'
name|'glance_client'
op|'='
name|'client'
op|'.'
name|'Client'
op|'('
name|'FLAGS'
op|'.'
name|'glance_host'
op|','
name|'FLAGS'
op|'.'
name|'glance_port'
op|')'
newline|'\r\n'
name|'metadata'
op|','
name|'read_iter'
op|'='
name|'glance_client'
op|'.'
name|'get_image'
op|'('
name|'image'
op|')'
newline|'\r\n'
name|'read_file_handle'
op|'='
name|'read_write_util'
op|'.'
name|'GlanceFileRead'
op|'('
name|'read_iter'
op|')'
newline|'\r\n'
name|'file_size'
op|'='
name|'int'
op|'('
name|'metadata'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\r\n'
name|'write_file_handle'
op|'='
name|'read_write_util'
op|'.'
name|'VMWareHTTPWriteFile'
op|'('
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"data_center_name"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"datastore_name"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cookies"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"file_path"'
op|')'
op|','
nl|'\r\n'
name|'file_size'
op|')'
newline|'\r\n'
name|'start_transfer'
op|'('
name|'read_file_handle'
op|','
name|'file_size'
op|','
nl|'\r\n'
name|'write_file_handle'
op|'='
name|'write_file_handle'
op|')'
newline|'\r\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Downloaded image %s from glance image server"'
op|')'
op|'%'
name|'image'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|_get_s3_image
dedent|''
name|'def'
name|'_get_s3_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Download image from the S3 image server."""'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|_get_local_image
dedent|''
name|'def'
name|'_get_local_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Download image from the local nova compute node."""'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|_put_glance_image
dedent|''
name|'def'
name|'_put_glance_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Upload the snapshotted vm disk file to Glance image server."""'
newline|'\r\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Uploading image %s to the Glance image server"'
op|')'
op|'%'
name|'image'
op|')'
newline|'\r\n'
name|'read_file_handle'
op|'='
name|'read_write_util'
op|'.'
name|'VmWareHTTPReadFile'
op|'('
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"data_center_name"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"datastore_name"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cookies"'
op|')'
op|','
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"file_path"'
op|')'
op|')'
newline|'\r\n'
name|'file_size'
op|'='
name|'read_file_handle'
op|'.'
name|'get_size'
op|'('
op|')'
newline|'\r\n'
name|'glance_client'
op|'='
name|'client'
op|'.'
name|'Client'
op|'('
name|'FLAGS'
op|'.'
name|'glance_host'
op|','
name|'FLAGS'
op|'.'
name|'glance_port'
op|')'
newline|'\r\n'
comment|'# The properties and other fields that we need to set for the image.'
nl|'\r\n'
name|'image_metadata'
op|'='
op|'{'
string|'"is_public"'
op|':'
name|'True'
op|','
nl|'\r\n'
string|'"disk_format"'
op|':'
string|'"vmdk"'
op|','
nl|'\r\n'
string|'"container_format"'
op|':'
string|'"bare"'
op|','
nl|'\r\n'
string|'"type"'
op|':'
string|'"vmdk"'
op|','
nl|'\r\n'
string|'"properties"'
op|':'
op|'{'
string|'"vmware_adaptertype"'
op|':'
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"adapter_type"'
op|')'
op|','
nl|'\r\n'
string|'"vmware_ostype"'
op|':'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"os_type"'
op|')'
op|','
nl|'\r\n'
string|'"vmware_image_version"'
op|':'
nl|'\r\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"image_version"'
op|')'
op|'}'
op|'}'
newline|'\r\n'
name|'start_transfer'
op|'('
name|'read_file_handle'
op|','
name|'file_size'
op|','
name|'glance_client'
op|'='
name|'glance_client'
op|','
nl|'\r\n'
name|'image_id'
op|'='
name|'image'
op|','
name|'image_meta'
op|'='
name|'image_metadata'
op|')'
newline|'\r\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Uploaded image %s to the Glance image server"'
op|')'
op|'%'
name|'image'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|_put_local_image
dedent|''
name|'def'
name|'_put_local_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Upload the snapshotted vm disk file to the local nova compute node."""'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|_put_s3_image
dedent|''
name|'def'
name|'_put_s3_image'
op|'('
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Upload the snapshotted vm disk file to S3 image server."""'
newline|'\r\n'
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_vmdk_size_and_properties
dedent|''
name|'def'
name|'get_vmdk_size_and_properties'
op|'('
name|'image'
op|','
name|'instance'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Get size of the vmdk file that is to be downloaded for attach in spawn.\r\n    Need this to create the dummy virtual disk for the meta-data file. The\r\n    geometry of the disk created depends on the size.\r\n    """'
newline|'\r\n'
nl|'\r\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Getting image size for the image %s"'
op|')'
op|'%'
name|'image'
op|')'
newline|'\r\n'
name|'if'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.glance.GlanceImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'glance_client'
op|'='
name|'client'
op|'.'
name|'Client'
op|'('
name|'FLAGS'
op|'.'
name|'glance_host'
op|','
nl|'\r\n'
name|'FLAGS'
op|'.'
name|'glance_port'
op|')'
newline|'\r\n'
name|'meta_data'
op|'='
name|'glance_client'
op|'.'
name|'get_image_meta'
op|'('
name|'image'
op|')'
newline|'\r\n'
name|'size'
op|','
name|'properties'
op|'='
name|'meta_data'
op|'['
string|'"size"'
op|']'
op|','
name|'meta_data'
op|'['
string|'"properties"'
op|']'
newline|'\r\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.s3.S3ImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.local.LocalImageService"'
op|':'
newline|'\r\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
newline|'\r\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got image size of %(size)s for the image %(image)s"'
op|')'
op|'%'
nl|'\r\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\r\n'
name|'return'
name|'size'
op|','
name|'properties'
newline|'\r\n'
dedent|''
endmarker|''
end_unit
