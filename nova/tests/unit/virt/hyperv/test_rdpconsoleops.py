begin_unit
comment|'# Copyright 2015 Cloudbase Solutions SRL'
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
string|'"""\nUnit tests for the Hyper-V RDPConsoleOps.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'test_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'rdpconsoleops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RDPConsoleOpsTestCase
name|'class'
name|'RDPConsoleOpsTestCase'
op|'('
name|'test_base'
op|'.'
name|'HyperVBaseTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'RDPConsoleOpsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'rdpconsoleops'
op|'='
name|'rdpconsoleops'
op|'.'
name|'RDPConsoleOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rdpconsoleops'
op|'.'
name|'_hostops'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rdpconsoleops'
op|'.'
name|'_vmutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rdpconsoleops'
op|'.'
name|'_rdpconsoleutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_rdp_console
dedent|''
name|'def'
name|'test_get_rdp_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_host_ip'
op|'='
name|'self'
op|'.'
name|'rdpconsoleops'
op|'.'
name|'_hostops'
op|'.'
name|'get_host_ip_addr'
newline|'\n'
name|'mock_get_rdp_port'
op|'='
op|'('
nl|'\n'
name|'self'
op|'.'
name|'rdpconsoleops'
op|'.'
name|'_rdpconsoleutils'
op|'.'
name|'get_rdp_console_port'
op|')'
newline|'\n'
name|'mock_get_vm_id'
op|'='
name|'self'
op|'.'
name|'rdpconsoleops'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_id'
newline|'\n'
nl|'\n'
name|'connect_info'
op|'='
name|'self'
op|'.'
name|'rdpconsoleops'
op|'.'
name|'get_rdp_console'
op|'('
name|'mock'
op|'.'
name|'DEFAULT'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_get_host_ip'
op|'.'
name|'return_value'
op|','
name|'connect_info'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_get_rdp_port'
op|'.'
name|'return_value'
op|','
name|'connect_info'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_get_vm_id'
op|'.'
name|'return_value'
op|','
nl|'\n'
name|'connect_info'
op|'.'
name|'internal_access_path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
