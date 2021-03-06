begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
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
nl|'\n'
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tarfile'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenio'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VdiThroughDevStore
name|'class'
name|'VdiThroughDevStore'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deal with virtual disks by attaching them to the OS domU.\n\n    At the moment it supports upload to Glance, and the upload format is a raw\n    disk inside a tgz.\n    """'
newline|'\n'
nl|'\n'
DECL|member|upload_image
name|'def'
name|'upload_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image_id'
op|','
name|'vdi_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'command'
op|'='
name|'UploadToGlanceAsRawTgz'
op|'('
nl|'\n'
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image_id'
op|','
name|'vdi_uuids'
op|')'
newline|'\n'
name|'return'
name|'command'
op|'.'
name|'upload_image'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|download_image
dedent|''
name|'def'
name|'download_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
comment|'# TODO(matelakat) Move through-dev image download functionality to this'
nl|'\n'
comment|'# method.'
nl|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UploadToGlanceAsRawTgz
dedent|''
dedent|''
name|'class'
name|'UploadToGlanceAsRawTgz'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image_id'
op|','
name|'vdi_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'image_id'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'vdi_uuids'
op|'='
name|'vdi_uuids'
newline|'\n'
nl|'\n'
DECL|member|_get_virtual_size
dedent|''
name|'def'
name|'_get_virtual_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
nl|'\n'
string|"'VDI.get_virtual_size'"
op|','
name|'self'
op|'.'
name|'_get_vdi_ref'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vdi_ref
dedent|''
name|'def'
name|'_get_vdi_ref'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VDI.get_by_uuid'"
op|','
name|'self'
op|'.'
name|'vdi_uuids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_perform_upload
dedent|''
name|'def'
name|'_perform_upload'
op|'('
name|'self'
op|','
name|'devpath'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'readfile'
op|','
name|'writefile'
op|'='
name|'self'
op|'.'
name|'_create_pipe'
op|'('
op|')'
newline|'\n'
name|'size'
op|'='
name|'self'
op|'.'
name|'_get_virtual_size'
op|'('
op|')'
newline|'\n'
name|'producer'
op|'='
name|'TarGzProducer'
op|'('
name|'devpath'
op|','
name|'writefile'
op|','
name|'size'
op|','
string|"'disk.raw'"
op|')'
newline|'\n'
name|'consumer'
op|'='
name|'glance'
op|'.'
name|'UpdateGlanceImage'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'image_id'
op|','
name|'producer'
op|'.'
name|'get_metadata'
op|'('
op|')'
op|','
name|'readfile'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'eventlet'
op|'.'
name|'GreenPool'
op|'('
op|')'
newline|'\n'
name|'pool'
op|'.'
name|'spawn'
op|'('
name|'producer'
op|'.'
name|'start'
op|')'
newline|'\n'
name|'pool'
op|'.'
name|'spawn'
op|'('
name|'consumer'
op|'.'
name|'start'
op|')'
newline|'\n'
name|'pool'
op|'.'
name|'waitall'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_pipe
dedent|''
name|'def'
name|'_create_pipe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpipe'
op|','
name|'wpipe'
op|'='
name|'os'
op|'.'
name|'pipe'
op|'('
op|')'
newline|'\n'
name|'rfile'
op|'='
name|'greenio'
op|'.'
name|'GreenPipe'
op|'('
name|'rpipe'
op|','
string|"'rb'"
op|','
number|'0'
op|')'
newline|'\n'
name|'wfile'
op|'='
name|'greenio'
op|'.'
name|'GreenPipe'
op|'('
name|'wpipe'
op|','
string|"'wb'"
op|','
number|'0'
op|')'
newline|'\n'
name|'return'
name|'rfile'
op|','
name|'wfile'
newline|'\n'
nl|'\n'
DECL|member|upload_image
dedent|''
name|'def'
name|'upload_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vdi_ref'
op|'='
name|'self'
op|'.'
name|'_get_vdi_ref'
op|'('
op|')'
newline|'\n'
name|'with'
name|'vm_utils'
op|'.'
name|'vdi_attached_here'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'vdi_ref'
op|','
nl|'\n'
name|'read_only'
op|'='
name|'True'
op|')'
name|'as'
name|'dev'
op|':'
newline|'\n'
indent|'            '
name|'devpath'
op|'='
name|'utils'
op|'.'
name|'make_dev_path'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'temporary_chown'
op|'('
name|'devpath'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_perform_upload'
op|'('
name|'devpath'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TarGzProducer
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'TarGzProducer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'devpath'
op|','
name|'writefile'
op|','
name|'size'
op|','
name|'fname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fpath'
op|'='
name|'devpath'
newline|'\n'
name|'self'
op|'.'
name|'output'
op|'='
name|'writefile'
newline|'\n'
name|'self'
op|'.'
name|'size'
op|'='
name|'size'
newline|'\n'
name|'self'
op|'.'
name|'fname'
op|'='
name|'fname'
newline|'\n'
nl|'\n'
DECL|member|get_metadata
dedent|''
name|'def'
name|'get_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'disk_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'tgz'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'contextlib'
op|'.'
name|'closing'
op|'('
name|'self'
op|'.'
name|'output'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'tinfo'
op|'='
name|'tarfile'
op|'.'
name|'TarInfo'
op|'('
name|'name'
op|'='
name|'self'
op|'.'
name|'fname'
op|')'
newline|'\n'
name|'tinfo'
op|'.'
name|'size'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'size'
op|')'
newline|'\n'
name|'with'
name|'tarfile'
op|'.'
name|'open'
op|'('
name|'fileobj'
op|'='
name|'self'
op|'.'
name|'output'
op|','
name|'mode'
op|'='
string|"'w|gz'"
op|')'
name|'as'
name|'tfile'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'self'
op|'.'
name|'_open_file'
op|'('
name|'self'
op|'.'
name|'fpath'
op|','
string|"'rb'"
op|')'
name|'as'
name|'input_file'
op|':'
newline|'\n'
indent|'                    '
name|'tfile'
op|'.'
name|'addfile'
op|'('
name|'tinfo'
op|','
name|'fileobj'
op|'='
name|'input_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_open_file
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_open_file'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'open'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
