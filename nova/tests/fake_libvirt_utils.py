begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright (c) 2011 OpenStack LLC'
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
name|'StringIO'
newline|'\n'
nl|'\n'
DECL|variable|files
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
DECL|variable|disk_sizes
name|'disk_sizes'
op|'='
op|'{'
op|'}'
newline|'\n'
DECL|variable|disk_backing_files
name|'disk_backing_files'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_image
name|'def'
name|'create_image'
op|'('
name|'disk_format'
op|','
name|'path'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_cow_image
dedent|''
name|'def'
name|'create_cow_image'
op|'('
name|'backing_file'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_size
dedent|''
name|'def'
name|'get_disk_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'disk_sizes'
op|'.'
name|'get'
op|'('
name|'path'
op|','
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'20'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_backing_file
dedent|''
name|'def'
name|'get_disk_backing_file'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'disk_backing_files'
op|'.'
name|'get'
op|'('
name|'path'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|copy_image
dedent|''
name|'def'
name|'copy_image'
op|'('
name|'src'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkfs
dedent|''
name|'def'
name|'mkfs'
op|'('
name|'fs'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_tree
dedent|''
name|'def'
name|'ensure_tree'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_to_file
dedent|''
name|'def'
name|'write_to_file'
op|'('
name|'path'
op|','
name|'contents'
op|','
name|'umask'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|chown
dedent|''
name|'def'
name|'chown'
op|'('
name|'path'
op|','
name|'owner'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extract_snapshot
dedent|''
name|'def'
name|'extract_snapshot'
op|'('
name|'disk_path'
op|','
name|'source_fmt'
op|','
name|'snapshot_name'
op|','
name|'out_path'
op|','
name|'dest_fmt'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'files'
op|'['
name|'out_path'
op|']'
op|'='
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|File
dedent|''
name|'class'
name|'File'
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
name|'path'
op|','
name|'mode'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fp'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
name|'files'
op|'['
name|'path'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'fp'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
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
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_open
dedent|''
dedent|''
name|'def'
name|'file_open'
op|'('
name|'path'
op|','
name|'mode'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'File'
op|'('
name|'path'
op|','
name|'mode'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_file
dedent|''
name|'def'
name|'load_file'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_delete
dedent|''
name|'def'
name|'file_delete'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_open_port
dedent|''
name|'def'
name|'get_open_port'
op|'('
name|'start_port'
op|','
name|'end_port'
op|')'
op|':'
newline|'\n'
comment|'# Return the port in the middle'
nl|'\n'
indent|'    '
name|'return'
name|'int'
op|'('
op|'('
name|'start_port'
op|'+'
name|'end_port'
op|')'
op|'/'
number|'2'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|run_ajaxterm
dedent|''
name|'def'
name|'run_ajaxterm'
op|'('
name|'cmd'
op|','
name|'token'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fs_info
dedent|''
name|'def'
name|'get_fs_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'total'"
op|':'
number|'128'
op|'*'
op|'('
number|'1024'
op|'**'
number|'3'
op|')'
op|','
nl|'\n'
string|"'used'"
op|':'
number|'44'
op|'*'
op|'('
number|'1024'
op|'**'
number|'3'
op|')'
op|','
nl|'\n'
string|"'free'"
op|':'
number|'84'
op|'*'
op|'('
number|'1024'
op|'**'
number|'3'
op|')'
op|'}'
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
name|'target'
op|','
name|'image_id'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
