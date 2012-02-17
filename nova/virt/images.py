begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nHandling of VM disk images.\n"""'
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
name|'import'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
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
DECL|variable|image_opts
name|'image_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'force_raw_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Force backing images to raw format'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'image_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch
name|'def'
name|'fetch'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path'
op|','
name|'_user_id'
op|','
name|'_project_id'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): Improve context handling and add owner and auth data'
nl|'\n'
comment|'#             when it is added to glance.  Right now there is no'
nl|'\n'
comment|'#             auth checking in glance, so we assume that access was'
nl|'\n'
comment|'#             checked before we got here.'
nl|'\n'
indent|'    '
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'nova'
op|'.'
name|'image'
op|'.'
name|'get_image_service'
op|'('
name|'context'
op|','
nl|'\n'
name|'image_href'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|'"wb"'
op|')'
name|'as'
name|'image_file'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'image_service'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image_file'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_to_raw
dedent|''
name|'def'
name|'fetch_to_raw'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'path_tmp'
op|'='
string|'"%s.part"'
op|'%'
name|'path'
newline|'\n'
name|'metadata'
op|'='
name|'fetch'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path_tmp'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_qemu_img_info
name|'def'
name|'_qemu_img_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
comment|"# output of qemu-img is 'field: value'"
nl|'\n'
comment|"# the fields of interest are 'file format' and 'backing file'"
nl|'\n'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'out'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'field'
op|','
name|'val'
op|')'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'val'
op|'['
number|'0'
op|']'
op|'=='
string|'" "'
op|':'
newline|'\n'
indent|'                '
name|'val'
op|'='
name|'val'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'data'
op|'['
name|'field'
op|']'
op|'='
name|'val'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
name|'_qemu_img_info'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
nl|'\n'
name|'fmt'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|'"file format"'
op|')'
newline|'\n'
name|'if'
name|'fmt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"\'qemu-img info\' parsing failed."'
op|')'
op|','
name|'image_id'
op|'='
name|'image_href'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|'"backing file"'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'        '
name|'backing_file'
op|'='
name|'data'
op|'['
string|"'backing file'"
op|']'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'image_href'
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"fmt=%(fmt)s backed by: %(backing_file)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'fmt'
op|'!='
string|'"raw"'
name|'and'
name|'FLAGS'
op|'.'
name|'force_raw_images'
op|':'
newline|'\n'
indent|'        '
name|'staged'
op|'='
string|'"%s.converted"'
op|'%'
name|'path'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%s was %s, converting to raw"'
op|'%'
op|'('
name|'image_href'
op|','
name|'fmt'
op|')'
op|')'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'qemu-img'"
op|','
string|"'convert'"
op|','
string|"'-O'"
op|','
string|"'raw'"
op|','
nl|'\n'
name|'path_tmp'
op|','
name|'staged'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'_qemu_img_info'
op|'('
name|'staged'
op|')'
newline|'\n'
name|'if'
name|'data'
op|'.'
name|'get'
op|'('
string|"'file format'"
op|','
name|'None'
op|')'
op|'!='
string|'"raw"'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'staged'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'image_href'
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Converted to raw, but format is now %s"'
op|')'
op|'%'
nl|'\n'
name|'data'
op|'.'
name|'get'
op|'('
string|"'file format'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'rename'
op|'('
name|'staged'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'rename'
op|'('
name|'path_tmp'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
dedent|''
endmarker|''
end_unit
