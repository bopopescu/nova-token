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
name|'import'
name|'os'
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
name|'base_url'
op|'='
name|'req'
op|'.'
name|'application_url'
newline|'\n'
name|'return'
name|'ViewBuilder'
op|'('
name|'base_url'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
dedent|''
name|'class'
name|'ViewBuilder'
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
name|'base_url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        :param base_url: url of the root wsgi application\n        """'
newline|'\n'
name|'self'
op|'.'
name|'base_url'
op|'='
name|'base_url'
newline|'\n'
nl|'\n'
DECL|member|build_choices
dedent|''
name|'def'
name|'build_choices'
op|'('
name|'self'
op|','
name|'VERSIONS'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version_objs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'version'
name|'in'
name|'VERSIONS'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'VERSIONS'
op|'['
name|'version'
op|']'
newline|'\n'
name|'version_objs'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'version'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'version'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
string|'"links"'
op|':'
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
name|'version'
op|'['
string|"'id'"
op|']'
op|','
name|'req'
op|'.'
name|'path'
op|')'
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
name|'version'
op|'['
string|"'media-types'"
op|']'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'choices'
op|'='
name|'version_objs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_versions
dedent|''
name|'def'
name|'build_versions'
op|'('
name|'self'
op|','
name|'versions'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version_objs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'version'
name|'in'
name|'versions'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'versions'
op|'['
name|'version'
op|']'
newline|'\n'
name|'version_objs'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'version'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'version'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
string|'"updated"'
op|':'
name|'version'
op|'['
string|"'updated'"
op|']'
op|','
nl|'\n'
string|'"links"'
op|':'
name|'self'
op|'.'
name|'_build_links'
op|'('
name|'version'
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'versions'
op|'='
name|'version_objs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_version
dedent|''
name|'def'
name|'build_version'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'link'
name|'in'
name|'version'
op|'['
string|"'links'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'link'
op|'['
string|"'rel'"
op|']'
op|'=='
string|"'self'"
op|':'
newline|'\n'
indent|'                '
name|'link'
op|'['
string|"'href'"
op|']'
op|'='
name|'self'
op|'.'
name|'base_url'
op|'.'
name|'rstrip'
op|'('
string|"'/'"
op|')'
op|'+'
string|"'/'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'dict'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_links
dedent|''
name|'def'
name|'_build_links'
op|'('
name|'self'
op|','
name|'version_data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generate a container of links that refer to the provided version."""'
newline|'\n'
name|'href'
op|'='
name|'self'
op|'.'
name|'generate_href'
op|'('
name|'version_data'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
nl|'\n'
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
name|'href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
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
name|'version_number'
op|','
name|'path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an url that refers to a specific version_number."""'
newline|'\n'
name|'version_number'
op|'='
name|'version_number'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'if'
name|'path'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'path'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'base_url'
op|','
name|'version_number'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'base_url'
op|','
name|'version_number'
op|')'
op|'+'
string|"'/'"
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
