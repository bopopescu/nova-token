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
name|'import'
name|'glanceclient'
op|'.'
name|'exc'
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
op|','
name|'version'
op|'='
name|'None'
op|','
name|'endpoint'
op|'='
name|'None'
op|','
op|'**'
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'auth_token'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'token'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'identity_headers'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'identity_headers'"
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'identity_headers'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'identity_headers'
op|'.'
name|'get'
op|'('
string|"'X-Auth-Token'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'auth_token'
op|'='
op|'('
name|'self'
op|'.'
name|'identity_headers'
op|'.'
name|'get'
op|'('
string|"'X-Auth_Token'"
op|')'
name|'or'
nl|'\n'
name|'self'
op|'.'
name|'auth_token'
op|')'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'identity_headers'
op|'['
string|"'X-Auth-Token'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_images'
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
name|'create'
op|'('
op|'**'
name|'image'
op|')'
op|','
name|'_images'
op|')'
newline|'\n'
nl|'\n'
comment|'#NOTE(bcwaldon): HACK to get client.images.* to work'
nl|'\n'
name|'self'
op|'.'
name|'images'
op|'='
name|'lambda'
op|':'
name|'None'
newline|'\n'
name|'for'
name|'fn'
name|'in'
op|'('
string|"'list'"
op|','
string|"'get'"
op|','
string|"'data'"
op|','
string|"'create'"
op|','
string|"'update'"
op|','
string|"'delete'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|'.'
name|'images'
op|','
name|'fn'
op|','
name|'getattr'
op|'('
name|'self'
op|','
name|'fn'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): implement filters'
nl|'\n'
DECL|member|list
dedent|''
dedent|''
name|'def'
name|'list'
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
number|'30'
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
name|'_images'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'image'
op|'.'
name|'id'
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
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'BadRequest'
op|'('
string|"'Marker not found'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_images'
op|'['
name|'index'
op|':'
name|'index'
op|'+'
name|'limit'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
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
name|'_images'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image'
op|'.'
name|'id'
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
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'NotFound'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|data
dedent|''
name|'def'
name|'data'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'get'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
op|'**'
name|'metadata'
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
name|'_images'
op|'.'
name|'append'
op|'('
name|'FakeImage'
op|'('
name|'metadata'
op|')'
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
name|'_images'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_images'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'id'
op|'='
name|'image_id'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_images'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'image_id'
op|','
op|'**'
name|'metadata'
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
name|'_images'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image'
op|'.'
name|'id'
op|'=='
name|'str'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
comment|'# If you try to update a non-authorized image, it raises'
nl|'\n'
comment|'# HTTPForbidden'
nl|'\n'
indent|'                '
name|'if'
name|'image'
op|'.'
name|'owner'
op|'=='
string|"'authorized_fake'"
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'metadata'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'setattr'
op|'('
name|'self'
op|'.'
name|'_images'
op|'['
name|'i'
op|']'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_images'
op|'['
name|'i'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'NotFound'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
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
name|'_images'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image'
op|'.'
name|'id'
op|'=='
name|'image_id'
op|':'
newline|'\n'
comment|'# When you delete an image from glance, it sets the status to'
nl|'\n'
comment|'# DELETED. If you try to delete a DELETED image, it raises'
nl|'\n'
comment|'# HTTPForbidden.'
nl|'\n'
indent|'                '
name|'image_data'
op|'='
name|'self'
op|'.'
name|'_images'
op|'['
name|'i'
op|']'
newline|'\n'
name|'if'
name|'image_data'
op|'.'
name|'deleted'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
dedent|''
name|'image_data'
op|'.'
name|'deleted'
op|'='
name|'True'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'glanceclient'
op|'.'
name|'exc'
op|'.'
name|'NotFound'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeImage
dedent|''
dedent|''
name|'class'
name|'FakeImage'
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
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'IMAGE_ATTRIBUTES'
op|'='
op|'['
string|"'size'"
op|','
string|"'disk_format'"
op|','
string|"'owner'"
op|','
nl|'\n'
string|"'container_format'"
op|','
string|"'checksum'"
op|','
string|"'id'"
op|','
nl|'\n'
string|"'name'"
op|','
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
nl|'\n'
string|"'deleted'"
op|','
string|"'status'"
op|','
nl|'\n'
string|"'min_disk'"
op|','
string|"'min_ram'"
op|','
string|"'is_public'"
op|']'
newline|'\n'
name|'raw'
op|'='
name|'dict'
op|'.'
name|'fromkeys'
op|'('
name|'IMAGE_ATTRIBUTES'
op|')'
newline|'\n'
name|'raw'
op|'.'
name|'update'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'raw'"
op|']'
op|'='
name|'raw'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'raw'"
op|']'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AttributeError'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setattr__
dedent|''
dedent|''
name|'def'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'raw'"
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AttributeError'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
