begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_view_builder
name|'def'
name|'get_view_builder'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''\n    A factory method that returns the correct builder based on the version of\n    the api requested.\n    '''"
newline|'\n'
name|'version'
op|'='
name|'common'
op|'.'
name|'get_api_version'
op|'('
name|'req'
op|')'
newline|'\n'
name|'base_url'
op|'='
name|'req'
op|'.'
name|'application_url'
newline|'\n'
name|'if'
name|'version'
op|'=='
string|"'1.1'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ViewBuilder_1_1'
op|'('
name|'base_url'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ViewBuilder_1_0'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
dedent|''
dedent|''
name|'class'
name|'ViewBuilder'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|build
dedent|''
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'flavor_obj'
op|','
name|'is_detail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'is_detail'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'='
name|'self'
op|'.'
name|'_build_detail'
op|'('
name|'flavor_obj'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'='
name|'self'
op|'.'
name|'_build_simple'
op|'('
name|'flavor_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'full_flavor'
op|'='
name|'self'
op|'.'
name|'_build_extra'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'full_flavor'
newline|'\n'
nl|'\n'
DECL|member|_build_simple
dedent|''
name|'def'
name|'_build_simple'
op|'('
name|'self'
op|','
name|'flavor_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'flavor_obj'
op|'['
string|'"flavorid"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'flavor_obj'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_build_detail
dedent|''
name|'def'
name|'_build_detail'
op|'('
name|'self'
op|','
name|'flavor_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'simple'
op|'='
name|'self'
op|'.'
name|'_build_simple'
op|'('
name|'flavor_obj'
op|')'
newline|'\n'
nl|'\n'
name|'detail'
op|'='
op|'{'
nl|'\n'
string|'"ram"'
op|':'
name|'flavor_obj'
op|'['
string|'"memory_mb"'
op|']'
op|','
nl|'\n'
string|'"disk"'
op|':'
name|'flavor_obj'
op|'['
string|'"local_gb"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'detail'
op|'.'
name|'update'
op|'('
name|'simple'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'detail'
newline|'\n'
nl|'\n'
DECL|member|_build_extra
dedent|''
name|'def'
name|'_build_extra'
op|'('
name|'self'
op|','
name|'flavor_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'flavor_obj'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder_1_1
dedent|''
dedent|''
name|'class'
name|'ViewBuilder_1_1'
op|'('
name|'ViewBuilder'
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
name|'base_url'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'base_url'
op|'='
name|'base_url'
newline|'\n'
nl|'\n'
DECL|member|_build_extra
dedent|''
name|'def'
name|'_build_extra'
op|'('
name|'self'
op|','
name|'flavor_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor_obj'
op|'['
string|'"links"'
op|']'
op|'='
name|'self'
op|'.'
name|'_build_links'
op|'('
name|'flavor_obj'
op|')'
newline|'\n'
name|'return'
name|'flavor_obj'
newline|'\n'
nl|'\n'
DECL|member|_build_links
dedent|''
name|'def'
name|'_build_links'
op|'('
name|'self'
op|','
name|'flavor_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'links'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'generate_href'
op|'('
name|'flavor_obj'
op|'['
string|'"id"'
op|']'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'return'
name|'links'
newline|'\n'
nl|'\n'
DECL|member|generate_href
dedent|''
name|'def'
name|'generate_href'
op|'('
name|'self'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s/flavors/%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'base_url'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder_1_0
dedent|''
dedent|''
name|'class'
name|'ViewBuilder_1_0'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
