begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
name|'import'
name|'flags'
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
DECL|variable|ipv6_backend_opt
name|'ipv6_backend_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ipv6_backend'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'rfc2462'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Backend to use for IPv6 generation'"
op|')'
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
name|'register_opt'
op|'('
name|'ipv6_backend_opt'
op|')'
newline|'\n'
DECL|variable|IMPL
name|'IMPL'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset_backend
name|'def'
name|'reset_backend'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'IMPL'
newline|'\n'
name|'IMPL'
op|'='
name|'utils'
op|'.'
name|'LazyPluggable'
op|'('
string|"'ipv6_backend'"
op|','
nl|'\n'
name|'rfc2462'
op|'='
string|"'nova.ipv6.rfc2462'"
op|','
nl|'\n'
name|'account_identifier'
op|'='
string|"'nova.ipv6.account_identifier'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|to_global
dedent|''
name|'def'
name|'to_global'
op|'('
name|'prefix'
op|','
name|'mac'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'to_global'
op|'('
name|'prefix'
op|','
name|'mac'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|to_mac
dedent|''
name|'def'
name|'to_mac'
op|'('
name|'ipv6_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'to_mac'
op|'('
name|'ipv6_address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'reset_backend'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
