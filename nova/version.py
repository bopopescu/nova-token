begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
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
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'nova'
op|'.'
name|'vcsversion'
name|'import'
name|'version_info'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|version_info
indent|'    '
name|'version_info'
op|'='
op|'{'
string|"'branch_nick'"
op|':'
string|"u'LOCALBRANCH'"
op|','
nl|'\n'
string|"'revision_id'"
op|':'
string|"'LOCALREVISION'"
op|','
nl|'\n'
string|"'revno'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|NOVA_VERSION
dedent|''
name|'NOVA_VERSION'
op|'='
op|'['
string|"'2011'"
op|','
string|"'1'"
op|']'
newline|'\n'
name|'YEAR'
op|','
name|'COUNT'
op|'='
name|'NOVA_VERSION'
newline|'\n'
nl|'\n'
DECL|variable|FINAL
name|'FINAL'
op|'='
name|'False'
comment|'# This becomes true at Release Candidate time'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|canonical_version_string
name|'def'
name|'canonical_version_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"''"
newline|'\n'
name|'return'
string|"'.'"
op|'.'
name|'join'
op|'('
op|'['
name|'YEAR'
op|','
name|'COUNT'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|version_string
dedent|''
name|'def'
name|'version_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"''"
newline|'\n'
name|'if'
name|'FINAL'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'canonical_version_string'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'%s-dev'"
op|'%'
op|'('
name|'canonical_version_string'
op|'('
op|')'
op|','
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vcs_version_string
dedent|''
dedent|''
name|'def'
name|'vcs_version_string'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"''"
newline|'\n'
name|'return'
string|'"%s:%s"'
op|'%'
op|'('
name|'version_info'
op|'['
string|"'branch_nick'"
op|']'
op|','
name|'version_info'
op|'['
string|"'revision_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|version_string_with_vcs
dedent|''
name|'def'
name|'version_string_with_vcs'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"''"
newline|'\n'
name|'return'
string|'"%s-%s"'
op|'%'
op|'('
name|'canonical_version_string'
op|'('
op|')'
op|','
name|'vcs_version_string'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
