begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
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
name|'from'
name|'glance'
op|'.'
name|'common'
name|'import'
name|'exception'
name|'as'
name|'glance_exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|NOW_GLANCE_FORMAT
name|'NOW_GLANCE_FORMAT'
op|'='
string|'"2010-10-11T10:30:22"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StubGlanceClient
name|'class'
name|'StubGlanceClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'images'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'images'
op|'='
op|'['
op|']'
newline|'\n'
name|'_images'
op|'='
name|'images'
name|'or'
op|'['
op|']'
newline|'\n'
name|'map'
op|'('
name|'lambda'
name|'image'
op|':'
name|'self'
op|'.'
name|'add_image'
op|'('
name|'image'
op|','
name|'None'
op|')'
op|','
name|'_images'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_auth_token
dedent|''
name|'def'
name|'set_auth_token'
op|'('
name|'self'
op|','
name|'auth_tok'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_image_meta
dedent|''
name|'def'
name|'get_image_meta'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'image'
name|'in'
name|'self'
op|'.'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image'
op|'['
string|"'id'"
op|']'
op|'=='
name|'str'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'image'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'glance_exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): implement filters'
nl|'\n'
DECL|member|get_images_detailed
dedent|''
name|'def'
name|'get_images_detailed'
op|'('
name|'self'
op|','
name|'filters'
op|'='
name|'None'
op|','
name|'marker'
op|'='
name|'None'
op|','
name|'limit'
op|'='
number|'3'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'marker'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'index'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'index'
op|','
name|'image'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'images'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'image'
op|'['
string|"'id'"
op|']'
op|'=='
name|'str'
op|'('
name|'marker'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'index'
op|'+='
number|'1'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'glance_exception'
op|'.'
name|'Invalid'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
name|'index'
op|':'
name|'index'
op|'+'
name|'limit'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_image
dedent|''
name|'def'
name|'get_image'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'get_image_meta'
op|'('
name|'image_id'
op|')'
op|','
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|add_image
dedent|''
name|'def'
name|'add_image'
op|'('
name|'self'
op|','
name|'metadata'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'NOW_GLANCE_FORMAT'
newline|'\n'
name|'metadata'
op|'['
string|"'updated_at'"
op|']'
op|'='
name|'NOW_GLANCE_FORMAT'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'images'
op|'.'
name|'append'
op|'('
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_id'
op|'='
name|'str'
op|'('
name|'metadata'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|"# auto-generate an id if one wasn't provided"
nl|'\n'
indent|'            '
name|'image_id'
op|'='
name|'str'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'images'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'images'
op|'['
op|'-'
number|'1'
op|']'
op|'['
string|"'id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
DECL|member|update_image
dedent|''
name|'def'
name|'update_image'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'metadata'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'i'
op|','
name|'image'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'images'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image'
op|'['
string|"'id'"
op|']'
op|'=='
name|'str'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
string|"'id'"
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'                    '
name|'metadata'
op|'['
string|"'id'"
op|']'
op|'='
name|'str'
op|'('
name|'metadata'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'images'
op|'['
name|'i'
op|']'
op|'.'
name|'update'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
name|'i'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'glance_exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_image
dedent|''
name|'def'
name|'delete_image'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'i'
op|','
name|'image'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'images'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image'
op|'['
string|"'id'"
op|']'
op|'=='
name|'image_id'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'self'
op|'.'
name|'images'
op|'['
name|'i'
op|']'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'glance_exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
