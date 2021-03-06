begin_unit
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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'network_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkUtilsTestCase
name|'class'
name|'NetworkUtilsTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
op|')'
op|':'
newline|'\n'
DECL|member|test_find_network_with_name_label_works
indent|'    '
name|'def'
name|'test_find_network_with_name_label_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_by_name_label'
op|'.'
name|'return_value'
op|'='
op|'['
string|'"net"'
op|']'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'network_utils'
op|'.'
name|'find_network_with_name_label'
op|'('
name|'session'
op|','
string|'"label"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"net"'
op|','
name|'result'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_by_name_label'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"label"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_network_with_name_returns_none
dedent|''
name|'def'
name|'test_find_network_with_name_returns_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_by_name_label'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'network_utils'
op|'.'
name|'find_network_with_name_label'
op|'('
name|'session'
op|','
string|'"label"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_network_with_name_label_raises
dedent|''
name|'def'
name|'test_find_network_with_name_label_raises'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_by_name_label'
op|'.'
name|'return_value'
op|'='
op|'['
string|'"net"'
op|','
string|'"net2"'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'network_utils'
op|'.'
name|'find_network_with_name_label'
op|','
nl|'\n'
name|'session'
op|','
string|'"label"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_network_with_bridge_works
dedent|''
name|'def'
name|'test_find_network_with_bridge_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_all_records_where'
op|'.'
name|'return_value'
op|'='
op|'{'
string|'"net"'
op|':'
string|'"asdf"'
op|'}'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'network_utils'
op|'.'
name|'find_network_with_bridge'
op|'('
name|'session'
op|','
string|'"bridge"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"net"'
op|')'
newline|'\n'
name|'expr'
op|'='
string|'\'field "name__label" = "bridge" or field "bridge" = "bridge"\''
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_all_records_where'
op|'.'
name|'assert_called_once_with'
op|'('
name|'expr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_network_with_bridge_raises_too_many
dedent|''
name|'def'
name|'test_find_network_with_bridge_raises_too_many'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_all_records_where'
op|'.'
name|'return_value'
op|'='
op|'{'
nl|'\n'
string|'"net"'
op|':'
string|'"asdf"'
op|','
nl|'\n'
string|'"net2"'
op|':'
string|'"asdf2"'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'network_utils'
op|'.'
name|'find_network_with_bridge'
op|','
nl|'\n'
name|'session'
op|','
string|'"bridge"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_network_with_bridge_raises_no_networks
dedent|''
name|'def'
name|'test_find_network_with_bridge_raises_no_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_all_records_where'
op|'.'
name|'return_value'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'network_utils'
op|'.'
name|'find_network_with_bridge'
op|','
nl|'\n'
name|'session'
op|','
string|'"bridge"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
