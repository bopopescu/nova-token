begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
nl|'\n'
comment|'#    Copyright 2011 Ilya Alekseyev'
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
name|'imp'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'db'
name|'import'
name|'fakes'
name|'as'
name|'db_fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TOPDIR
name|'TOPDIR'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|')'
op|')'
newline|'\n'
DECL|variable|NOVA_MANAGE_PATH
name|'NOVA_MANAGE_PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'TOPDIR'
op|','
string|"'bin'"
op|','
string|"'nova-manage'"
op|')'
newline|'\n'
nl|'\n'
name|'sys'
op|'.'
name|'dont_write_bytecode'
op|'='
name|'True'
newline|'\n'
DECL|variable|nova_manage
name|'nova_manage'
op|'='
name|'imp'
op|'.'
name|'load_source'
op|'('
string|"'nova_manage'"
op|','
name|'NOVA_MANAGE_PATH'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'dont_write_bytecode'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIpCommandsTestCase
name|'class'
name|'FixedIpCommandsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'FixedIpCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'db_fakes'
op|'.'
name|'stub_out_db_network_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'='
name|'nova_manage'
op|'.'
name|'FixedIpCommands'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reserve
dedent|''
name|'def'
name|'test_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'commands'
op|'.'
name|'reserve'
op|'('
string|"'192.168.0.100'"
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|"'192.168.0.100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|'['
string|"'reserved'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reserve_nonexistent_address
dedent|''
name|'def'
name|'test_reserve_nonexistent_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'SystemExit'
op|','
nl|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'reserve'
op|','
nl|'\n'
string|"'55.55.55.55'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unreserve
dedent|''
name|'def'
name|'test_unreserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'commands'
op|'.'
name|'unreserve'
op|'('
string|"'192.168.0.100'"
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|"'192.168.0.100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|'['
string|"'reserved'"
op|']'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unreserve_nonexistent_address
dedent|''
name|'def'
name|'test_unreserve_nonexistent_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'SystemExit'
op|','
nl|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'unreserve'
op|','
nl|'\n'
string|"'55.55.55.55'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpCommandsTestCase
dedent|''
dedent|''
name|'class'
name|'FloatingIpCommandsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'FloatingIpCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'db_fakes'
op|'.'
name|'stub_out_db_network_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'='
name|'nova_manage'
op|'.'
name|'FloatingIpCommands'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_address_to_hosts
dedent|''
name|'def'
name|'test_address_to_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|assert_loop
indent|'        '
name|'def'
name|'assert_loop'
op|'('
name|'result'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ip'
name|'in'
name|'result'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'str'
op|'('
name|'ip'
op|')'
name|'in'
name|'expected'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'address_to_hosts'
op|'='
name|'self'
op|'.'
name|'commands'
op|'.'
name|'address_to_hosts'
newline|'\n'
comment|'# /32 and /31'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
name|'address_to_hosts'
op|','
nl|'\n'
string|"'192.168.100.1/32'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
name|'address_to_hosts'
op|','
nl|'\n'
string|"'192.168.100.1/31'"
op|')'
newline|'\n'
comment|'# /30'
nl|'\n'
name|'expected'
op|'='
op|'['
string|'"192.168.100.%s"'
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'1'
op|','
number|'3'
op|')'
op|']'
newline|'\n'
name|'result'
op|'='
name|'address_to_hosts'
op|'('
string|"'192.168.100.0/30'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'result'
op|')'
op|')'
op|'=='
number|'2'
op|')'
newline|'\n'
name|'assert_loop'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
comment|'# /29'
nl|'\n'
name|'expected'
op|'='
op|'['
string|'"192.168.100.%s"'
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'1'
op|','
number|'7'
op|')'
op|']'
newline|'\n'
name|'result'
op|'='
name|'address_to_hosts'
op|'('
string|"'192.168.100.0/29'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'result'
op|')'
op|')'
op|'=='
number|'6'
op|')'
newline|'\n'
name|'assert_loop'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
comment|'# /28'
nl|'\n'
name|'expected'
op|'='
op|'['
string|'"192.168.100.%s"'
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'1'
op|','
number|'15'
op|')'
op|']'
newline|'\n'
name|'result'
op|'='
name|'address_to_hosts'
op|'('
string|"'192.168.100.0/28'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'list'
op|'('
name|'result'
op|')'
op|')'
op|'=='
number|'14'
op|')'
newline|'\n'
name|'assert_loop'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkCommandsTestCase
dedent|''
dedent|''
name|'class'
name|'NetworkCommandsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'NetworkCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'='
name|'nova_manage'
op|'.'
name|'NetworkCommands'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'net'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.0.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'dead:beef::/64'"
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'dead:beef::1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'fa0'"
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'fake_fa0'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'8.8.8.8'"
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'8.8.4.4'"
op|','
nl|'\n'
string|"'vlan'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'vpn_public_address'"
op|':'
string|"'10.0.0.2'"
op|','
nl|'\n'
string|"'vpn_public_port'"
op|':'
string|"'2222'"
op|','
nl|'\n'
string|"'vpn_private_address'"
op|':'
string|"'192.168.0.2'"
op|','
nl|'\n'
string|"'dhcp_start'"
op|':'
string|"'192.168.0.3'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_by_cidr
name|'def'
name|'fake_network_get_by_cidr'
op|'('
name|'context'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'['
string|"'is_admin'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cidr'
op|','
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'db_fakes'
op|'.'
name|'FakeModel'
op|'('
name|'self'
op|'.'
name|'fake_net'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_by_uuid
dedent|''
name|'def'
name|'fake_network_get_by_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'['
string|"'is_admin'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'uuid'
op|','
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'db_fakes'
op|'.'
name|'FakeModel'
op|'('
name|'self'
op|'.'
name|'fake_net'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_update
dedent|''
name|'def'
name|'fake_network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'['
string|"'is_admin'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network_id'
op|','
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|','
name|'self'
op|'.'
name|'fake_update_value'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'fake_network_get_by_cidr'
op|'='
name|'fake_network_get_by_cidr'
newline|'\n'
name|'self'
op|'.'
name|'fake_network_get_by_uuid'
op|'='
name|'fake_network_get_by_uuid'
newline|'\n'
name|'self'
op|'.'
name|'fake_network_update'
op|'='
name|'fake_network_update'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_create_networks
indent|'        '
name|'def'
name|'fake_create_networks'
op|'('
name|'obj'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'['
string|"'is_admin'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'label'"
op|']'
op|','
string|"'Test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'cidr'"
op|']'
op|','
string|"'10.2.0.0/24'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'multi_host'"
op|']'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'num_networks'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'network_size'"
op|']'
op|','
number|'256'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'vlan_start'"
op|']'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'vpn_start'"
op|']'
op|','
number|'2000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'cidr_v6'"
op|']'
op|','
string|"'fd00:2::/120'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'gateway'"
op|']'
op|','
string|"'10.2.0.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'gateway_v6'"
op|']'
op|','
string|"'fd00:2::22'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'br200'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'bridge_interface'"
op|']'
op|','
string|"'eth0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'dns1'"
op|']'
op|','
string|"'8.8.8.8'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'dns2'"
op|']'
op|','
string|"'8.8.4.4'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'flags'
op|'('
name|'network_manager'
op|'='
string|"'nova.network.manager.VlanManager'"
op|')'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
name|'as'
name|'net_manager'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'net_manager'
op|'.'
name|'VlanManager'
op|','
string|"'create_networks'"
op|','
nl|'\n'
name|'fake_create_networks'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'create'
op|'('
nl|'\n'
name|'label'
op|'='
string|"'Test'"
op|','
nl|'\n'
name|'fixed_range_v4'
op|'='
string|"'10.2.0.0/24'"
op|','
nl|'\n'
name|'num_networks'
op|'='
number|'1'
op|','
nl|'\n'
name|'network_size'
op|'='
number|'256'
op|','
nl|'\n'
name|'multi_host'
op|'='
string|"'F'"
op|','
nl|'\n'
name|'vlan_start'
op|'='
number|'200'
op|','
nl|'\n'
name|'vpn_start'
op|'='
number|'2000'
op|','
nl|'\n'
name|'fixed_range_v6'
op|'='
string|"'fd00:2::/120'"
op|','
nl|'\n'
name|'gateway'
op|'='
string|"'10.2.0.1'"
op|','
nl|'\n'
name|'gateway_v6'
op|'='
string|"'fd00:2::22'"
op|','
nl|'\n'
name|'bridge'
op|'='
string|"'br200'"
op|','
nl|'\n'
name|'bridge_interface'
op|'='
string|"'eth0'"
op|','
nl|'\n'
name|'dns1'
op|'='
string|"'8.8.8.8'"
op|','
nl|'\n'
name|'dns2'
op|'='
string|"'8.8.4.4'"
op|','
nl|'\n'
name|'uuid'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list
dedent|''
name|'def'
name|'test_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_all
indent|'        '
name|'def'
name|'fake_network_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'db_fakes'
op|'.'
name|'FakeModel'
op|'('
name|'self'
op|'.'
name|'net'
op|')'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_all'"
op|','
name|'fake_network_get_all'
op|')'
newline|'\n'
name|'output'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'output'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'list'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'sys'
op|'.'
name|'__stdout__'
newline|'\n'
name|'result'
op|'='
name|'output'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
name|'_fmt'
op|'='
string|'"\\t"'
op|'.'
name|'join'
op|'('
op|'['
string|'"%(id)-5s"'
op|','
string|'"%(cidr)-18s"'
op|','
string|'"%(cidr_v6)-15s"'
op|','
nl|'\n'
string|'"%(dhcp_start)-15s"'
op|','
string|'"%(dns1)-15s"'
op|','
string|'"%(dns2)-15s"'
op|','
nl|'\n'
string|'"%(vlan)-15s"'
op|','
string|'"%(project_id)-15s"'
op|','
string|'"%(uuid)-15s"'
op|']'
op|')'
newline|'\n'
name|'head'
op|'='
name|'_fmt'
op|'%'
op|'{'
string|"'id'"
op|':'
name|'_'
op|'('
string|"'id'"
op|')'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'_'
op|'('
string|"'IPv4'"
op|')'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'_'
op|'('
string|"'IPv6'"
op|')'
op|','
nl|'\n'
string|"'dhcp_start'"
op|':'
name|'_'
op|'('
string|"'start address'"
op|')'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'_'
op|'('
string|"'DNS1'"
op|')'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'_'
op|'('
string|"'DNS2'"
op|')'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'_'
op|'('
string|"'VlanID'"
op|')'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'_'
op|'('
string|"'project'"
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'_'
op|'('
string|'"uuid"'
op|')'
op|'}'
newline|'\n'
name|'body'
op|'='
name|'_fmt'
op|'%'
op|'{'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'cidr_v6'"
op|']'
op|','
nl|'\n'
string|"'dhcp_start'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'dhcp_start'"
op|']'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'dns1'"
op|']'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'dns2'"
op|']'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'vlan'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'self'
op|'.'
name|'net'
op|'['
string|"'uuid'"
op|']'
op|'}'
newline|'\n'
name|'answer'
op|'='
string|"'%s\\n%s\\n'"
op|'%'
op|'('
name|'head'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'answer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fake_net'
op|'='
name|'self'
op|'.'
name|'net'
newline|'\n'
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'host'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_by_uuid'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_network_get_by_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_delete_safe
name|'def'
name|'fake_network_delete_safe'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'['
string|"'is_admin'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network_id'
op|','
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_delete_safe'"
op|','
name|'fake_network_delete_safe'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'delete'
op|'('
name|'uuid'
op|'='
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_by_cidr
dedent|''
name|'def'
name|'test_delete_by_cidr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fake_net'
op|'='
name|'self'
op|'.'
name|'net'
newline|'\n'
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'host'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_by_cidr'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_network_get_by_cidr'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_delete_safe
name|'def'
name|'fake_network_delete_safe'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'['
string|"'is_admin'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network_id'
op|','
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_delete_safe'"
op|','
name|'fake_network_delete_safe'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'delete'
op|'('
name|'fixed_range'
op|'='
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_modify_base
dedent|''
name|'def'
name|'_test_modify_base'
op|'('
name|'self'
op|','
name|'update_value'
op|','
name|'project'
op|','
name|'host'
op|','
name|'dis_project'
op|'='
name|'None'
op|','
nl|'\n'
name|'dis_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fake_net'
op|'='
name|'self'
op|'.'
name|'net'
newline|'\n'
name|'self'
op|'.'
name|'fake_update_value'
op|'='
name|'update_value'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_by_cidr'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_network_get_by_cidr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_update'"
op|','
name|'self'
op|'.'
name|'fake_network_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'modify'
op|'('
name|'self'
op|'.'
name|'fake_net'
op|'['
string|"'cidr'"
op|']'
op|','
name|'project'
op|'='
name|'project'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'dis_project'
op|'='
name|'dis_project'
op|','
name|'dis_host'
op|'='
name|'dis_host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_modify_associate
dedent|''
name|'def'
name|'test_modify_associate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_modify_base'
op|'('
name|'update_value'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'test_project'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'test_host'"
op|'}'
op|','
nl|'\n'
name|'project'
op|'='
string|"'test_project'"
op|','
name|'host'
op|'='
string|"'test_host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_modify_unchanged
dedent|''
name|'def'
name|'test_modify_unchanged'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_modify_base'
op|'('
name|'update_value'
op|'='
op|'{'
op|'}'
op|','
name|'project'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_modify_disassociate
dedent|''
name|'def'
name|'test_modify_disassociate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_modify_base'
op|'('
name|'update_value'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'None'
op|','
string|"'host'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
name|'project'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'dis_project'
op|'='
name|'True'
op|','
nl|'\n'
name|'dis_host'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTypeCommandsTestCase
dedent|''
dedent|''
name|'class'
name|'InstanceTypeCommandsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'InstanceTypeCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'values'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test.small"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'220'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'root_gb'
op|'='
number|'16'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'32'
op|','
nl|'\n'
name|'flavorid'
op|'='
number|'105'
op|')'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'instance_type_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_type_name'
op|'='
name|'ref'
op|'['
string|'"name"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|'='
name|'ref'
op|'['
string|'"id"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'instance_type_flavorid'
op|'='
name|'ref'
op|'['
string|'"flavorid"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'set_key'
op|'='
name|'nova_manage'
op|'.'
name|'InstanceTypeCommands'
op|'('
op|')'
op|'.'
name|'set_key'
newline|'\n'
name|'self'
op|'.'
name|'unset_key'
op|'='
name|'nova_manage'
op|'.'
name|'InstanceTypeCommands'
op|'('
op|')'
op|'.'
name|'unset_key'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'instance_type_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|'"test.small"'
op|')'
newline|'\n'
name|'super'
op|'('
name|'InstanceTypeCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_extra_specs_empty
dedent|''
name|'def'
name|'_test_extra_specs_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'empty_specs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'empty_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_set_unset
dedent|''
name|'def'
name|'test_extra_specs_set_unset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
op|'{'
string|"'k1'"
op|':'
string|"'v1'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_test_extra_specs_empty'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'set_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k1"'
op|','
string|'"v1"'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'unset_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_extra_specs_empty'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_update
dedent|''
name|'def'
name|'test_extra_specs_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_specs'
op|'='
op|'{'
string|"'k1'"
op|':'
string|"'v1'"
op|'}'
newline|'\n'
name|'updated_specs'
op|'='
op|'{'
string|"'k1'"
op|':'
string|"'v2'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_test_extra_specs_empty'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'set_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k1"'
op|','
string|'"v1"'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'expected_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'set_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k1"'
op|','
string|'"v2"'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'updated_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'unset_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k1"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_multiple
dedent|''
name|'def'
name|'test_extra_specs_multiple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'two_items_extra_specs'
op|'='
op|'{'
string|"'k1'"
op|':'
string|"'v1'"
op|','
nl|'\n'
string|"'k3'"
op|':'
string|"'v3'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_test_extra_specs_empty'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'set_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k1"'
op|','
string|'"v1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k3"'
op|','
string|'"v3"'
op|')'
newline|'\n'
name|'actual_specs'
op|'='
name|'db'
op|'.'
name|'instance_type_extra_specs_get'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_type_flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'two_items_extra_specs'
op|','
name|'actual_specs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'unset_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'unset_key'
op|'('
name|'self'
op|'.'
name|'instance_type_name'
op|','
string|'"k3"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
