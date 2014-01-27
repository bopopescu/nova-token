begin_unit
comment|'# Copyright (c) 2012 VMware, Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
string|'"""\nUtility functions for Image transfer.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'io_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'read_write_util'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|QUEUE_BUFFER_SIZE
name|'QUEUE_BUFFER_SIZE'
op|'='
number|'10'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|start_transfer
name|'def'
name|'start_transfer'
op|'('
name|'context'
op|','
name|'read_file_handle'
op|','
name|'data_size'
op|','
nl|'\n'
name|'write_file_handle'
op|'='
name|'None'
op|','
name|'image_service'
op|'='
name|'None'
op|','
name|'image_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Start the data transfer from the reader to the writer.\n    Reader writes to the pipe and the writer reads from the pipe. This means\n    that the total transfer time boils down to the slower of the read/write\n    and not the addition of the two times.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image_meta'
op|':'
newline|'\n'
indent|'        '
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# The pipe that acts as an intermediate store of data for reader to write'
nl|'\n'
comment|'# to and writer to grab from.'
nl|'\n'
dedent|''
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
newline|'\n'
comment|'# The read thread. In case of glance it is the instance of the'
nl|'\n'
comment|'# GlanceFileRead class. The glance client read returns an iterator'
nl|'\n'
comment|'# and this class wraps that iterator to provide datachunks in calls'
nl|'\n'
comment|'# to read.'
nl|'\n'
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
newline|'\n'
nl|'\n'
comment|'# In case of Glance - VMware transfer, we just need a handle to the'
nl|'\n'
comment|'# HTTP Connection that is to send transfer data to the VMware datastore.'
nl|'\n'
name|'if'
name|'write_file_handle'
op|':'
newline|'\n'
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
newline|'\n'
comment|'# In case of VMware - Glance transfer, we relinquish VMware HTTP file read'
nl|'\n'
comment|'# handle to Glance Client instance, but to be sure of the transfer we need'
nl|'\n'
comment|'# to be sure of the status of the image on glance changing to active.'
nl|'\n'
comment|'# The GlanceWriteThread handles the same for us.'
nl|'\n'
dedent|''
name|'elif'
name|'image_service'
name|'and'
name|'image_id'
op|':'
newline|'\n'
indent|'        '
name|'write_thread'
op|'='
name|'io_util'
op|'.'
name|'GlanceWriteThread'
op|'('
name|'context'
op|','
name|'thread_safe_pipe'
op|','
nl|'\n'
name|'image_service'
op|','
name|'image_id'
op|','
name|'image_meta'
op|')'
newline|'\n'
comment|'# Start the read and write threads.'
nl|'\n'
dedent|''
name|'read_event'
op|'='
name|'read_thread'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'write_event'
op|'='
name|'write_thread'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Wait on the read and write events to signal their end'
nl|'\n'
indent|'        '
name|'read_event'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'write_event'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# In case of any of the reads or writes raising an exception,'
nl|'\n'
comment|"# stop the threads so that we un-necessarily don't keep the other one"
nl|'\n'
comment|'# waiting.'
nl|'\n'
indent|'        '
name|'read_thread'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'write_thread'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Log and raise the exception.'
nl|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# No matter what, try closing the read and write handles, if it so'
nl|'\n'
comment|'# applies.'
nl|'\n'
indent|'        '
name|'read_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'write_file_handle'
op|':'
newline|'\n'
indent|'            '
name|'write_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upload_iso_to_datastore
dedent|''
dedent|''
dedent|''
name|'def'
name|'upload_iso_to_datastore'
op|'('
name|'iso_path'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Uploading iso %s to datastore"'
op|')'
op|'%'
name|'iso_path'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'iso_path'
op|','
string|"'r'"
op|')'
name|'as'
name|'iso_file'
op|':'
newline|'\n'
indent|'        '
name|'write_file_handle'
op|'='
name|'read_write_util'
op|'.'
name|'VMwareHTTPWriteFile'
op|'('
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"data_center_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"datastore_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cookies"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"file_path"'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'fstat'
op|'('
name|'iso_file'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
op|'.'
name|'st_size'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Uploading iso of size : %s "'
op|')'
op|'%'
nl|'\n'
name|'os'
op|'.'
name|'fstat'
op|'('
name|'iso_file'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
op|'.'
name|'st_size'
op|')'
newline|'\n'
name|'block_size'
op|'='
number|'0x10000'
newline|'\n'
name|'data'
op|'='
name|'iso_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
name|'while'
name|'len'
op|'('
name|'data'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'write_file_handle'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'data'
op|'='
name|'iso_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
dedent|''
name|'write_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Uploaded iso %s to datastore"'
op|')'
op|'%'
name|'iso_path'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_image
dedent|''
name|'def'
name|'fetch_image'
op|'('
name|'context'
op|','
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Download image from the glance image server."""'
newline|'\n'
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
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
name|'image'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'file_size'
op|'='
name|'int'
op|'('
name|'metadata'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
name|'read_iter'
op|'='
name|'image_service'
op|'.'
name|'download'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'read_file_handle'
op|'='
name|'read_write_util'
op|'.'
name|'GlanceFileRead'
op|'('
name|'read_iter'
op|')'
newline|'\n'
name|'write_file_handle'
op|'='
name|'read_write_util'
op|'.'
name|'VMwareHTTPWriteFile'
op|'('
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"data_center_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"datastore_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cookies"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"file_path"'
op|')'
op|','
nl|'\n'
name|'file_size'
op|')'
newline|'\n'
name|'start_transfer'
op|'('
name|'context'
op|','
name|'read_file_handle'
op|','
name|'file_size'
op|','
nl|'\n'
name|'write_file_handle'
op|'='
name|'write_file_handle'
op|')'
newline|'\n'
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
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upload_image
dedent|''
name|'def'
name|'upload_image'
op|'('
name|'context'
op|','
name|'image'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Upload the snapshotted vm disk file to Glance image server."""'
newline|'\n'
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
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'read_file_handle'
op|'='
name|'read_write_util'
op|'.'
name|'VMwareHTTPReadFile'
op|'('
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"data_center_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"datastore_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cookies"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"file_path"'
op|')'
op|')'
newline|'\n'
name|'file_size'
op|'='
name|'read_file_handle'
op|'.'
name|'get_size'
op|'('
op|')'
newline|'\n'
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
name|'image'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# The properties and other fields that we need to set for the image.'
nl|'\n'
name|'image_metadata'
op|'='
op|'{'
string|'"disk_format"'
op|':'
string|'"vmdk"'
op|','
nl|'\n'
string|'"is_public"'
op|':'
string|'"false"'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'metadata'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"active"'
op|','
nl|'\n'
string|'"container_format"'
op|':'
string|'"bare"'
op|','
nl|'\n'
string|'"size"'
op|':'
name|'file_size'
op|','
nl|'\n'
string|'"properties"'
op|':'
op|'{'
string|'"vmware_adaptertype"'
op|':'
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"adapter_type"'
op|')'
op|','
nl|'\n'
string|'"vmware_disktype"'
op|':'
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"disk_type"'
op|')'
op|','
nl|'\n'
string|'"vmware_ostype"'
op|':'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"os_type"'
op|')'
op|','
nl|'\n'
string|'"vmware_image_version"'
op|':'
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"image_version"'
op|')'
op|','
nl|'\n'
string|'"owner_id"'
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|'}'
op|'}'
newline|'\n'
name|'start_transfer'
op|'('
name|'context'
op|','
name|'read_file_handle'
op|','
name|'file_size'
op|','
nl|'\n'
name|'image_service'
op|'='
name|'image_service'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_id'
op|','
name|'image_meta'
op|'='
name|'image_metadata'
op|')'
newline|'\n'
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
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vmdk_size_and_properties
dedent|''
name|'def'
name|'get_vmdk_size_and_properties'
op|'('
name|'context'
op|','
name|'image'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Get size of the vmdk file that is to be downloaded for attach in spawn.\n    Need this to create the dummy virtual disk for the meta-data file. The\n    geometry of the disk created depends on the size.\n    """'
newline|'\n'
nl|'\n'
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
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
name|'image'
op|')'
newline|'\n'
name|'meta_data'
op|'='
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
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
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got image size of %(size)s for the image %(image)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'size'"
op|':'
name|'size'
op|','
string|"'image'"
op|':'
name|'image'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'size'
op|','
name|'properties'
newline|'\n'
dedent|''
endmarker|''
end_unit
