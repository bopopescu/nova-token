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
name|'StringIO'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_glance_client
name|'def'
name|'stubout_glance_client'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_glance_client
indent|'    '
name|'def'
name|'fake_get_glance_client'
op|'('
name|'image_href'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'int'
op|'('
name|'str'
op|'('
name|'image_href'
op|')'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'return'
op|'('
name|'FakeGlance'
op|'('
string|"'foo'"
op|')'
op|','
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|','
string|"'get_glance_client'"
op|','
name|'fake_get_glance_client'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeGlance
dedent|''
name|'class'
name|'FakeGlance'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|IMAGE_MACHINE
indent|'    '
name|'IMAGE_MACHINE'
op|'='
number|'1'
newline|'\n'
DECL|variable|IMAGE_KERNEL
name|'IMAGE_KERNEL'
op|'='
number|'2'
newline|'\n'
DECL|variable|IMAGE_RAMDISK
name|'IMAGE_RAMDISK'
op|'='
number|'3'
newline|'\n'
DECL|variable|IMAGE_RAW
name|'IMAGE_RAW'
op|'='
number|'4'
newline|'\n'
DECL|variable|IMAGE_VHD
name|'IMAGE_VHD'
op|'='
number|'5'
newline|'\n'
DECL|variable|IMAGE_ISO
name|'IMAGE_ISO'
op|'='
number|'6'
newline|'\n'
nl|'\n'
DECL|variable|IMAGE_FIXTURES
name|'IMAGE_FIXTURES'
op|'='
op|'{'
nl|'\n'
name|'IMAGE_MACHINE'
op|':'
op|'{'
nl|'\n'
string|"'image_meta'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'fakemachine'"
op|','
string|"'size'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ami'"
op|'}'
op|','
nl|'\n'
string|"'image_data'"
op|':'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|"''"
op|')'
op|'}'
op|','
nl|'\n'
name|'IMAGE_KERNEL'
op|':'
op|'{'
nl|'\n'
string|"'image_meta'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'fakekernel'"
op|','
string|"'size'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'aki'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'aki'"
op|'}'
op|','
nl|'\n'
string|"'image_data'"
op|':'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|"''"
op|')'
op|'}'
op|','
nl|'\n'
name|'IMAGE_RAMDISK'
op|':'
op|'{'
nl|'\n'
string|"'image_meta'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'fakeramdisk'"
op|','
string|"'size'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'ari'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ari'"
op|'}'
op|','
nl|'\n'
string|"'image_data'"
op|':'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|"''"
op|')'
op|'}'
op|','
nl|'\n'
name|'IMAGE_RAW'
op|':'
op|'{'
nl|'\n'
string|"'image_meta'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'fakeraw'"
op|','
string|"'size'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'bare'"
op|'}'
op|','
nl|'\n'
string|"'image_data'"
op|':'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|"''"
op|')'
op|'}'
op|','
nl|'\n'
name|'IMAGE_VHD'
op|':'
op|'{'
nl|'\n'
string|"'image_meta'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'fakevhd'"
op|','
string|"'size'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vhd'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ovf'"
op|'}'
op|','
nl|'\n'
string|"'image_data'"
op|':'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|"''"
op|')'
op|'}'
op|','
nl|'\n'
name|'IMAGE_ISO'
op|':'
op|'{'
nl|'\n'
string|"'image_meta'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'fakeiso'"
op|','
string|"'size'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'iso'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'bare'"
op|'}'
op|','
nl|'\n'
string|"'image_data'"
op|':'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|"''"
op|')'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|'='
name|'None'
op|','
name|'use_ssl'
op|'='
name|'False'
op|','
name|'auth_tok'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
name|'return'
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|'['
name|'int'
op|'('
name|'image_id'
op|')'
op|']'
op|'['
string|"'image_meta'"
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
name|'image'
op|'='
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|'['
name|'int'
op|'('
name|'image_id'
op|')'
op|']'
newline|'\n'
name|'return'
name|'image'
op|'['
string|"'image_meta'"
op|']'
op|','
name|'image'
op|'['
string|"'image_data'"
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
