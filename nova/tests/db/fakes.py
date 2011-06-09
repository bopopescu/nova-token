begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack, LLC'
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
string|'"""Stubouts, mocks and fixtures for the test suite"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeModel
name|'class'
name|'FakeModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out for model."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'values'
op|'='
name|'values'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'<FakeModel: %s>'"
op|'%'
name|'self'
op|'.'
name|'values'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out
dedent|''
dedent|''
name|'def'
name|'stub_out'
op|'('
name|'stubs'
op|','
name|'funcs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Set the stubs in mapping in the db api\n    """'
newline|'\n'
name|'for'
name|'func'
name|'in'
name|'funcs'
op|':'
newline|'\n'
indent|'        '
name|'func_name'
op|'='
string|"'_'"
op|'.'
name|'join'
op|'('
name|'func'
op|'.'
name|'__name__'
op|'.'
name|'split'
op|'('
string|"'_'"
op|')'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
name|'func_name'
op|','
name|'func'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_db_network_api
dedent|''
dedent|''
name|'def'
name|'stub_out_db_network_api'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_fields'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.0.0/24'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'dead:beef::/64'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.0.1'"
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
string|"'broadcast'"
op|':'
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'dead:beef::1'"
op|','
nl|'\n'
string|"'dns'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vpn_public_address'"
op|':'
string|"'192.168.0.2'"
op|'}'
newline|'\n'
nl|'\n'
name|'fixed_ip_fields'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.0.100'"
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'allocated'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'mac_address_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'flavor_fields'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'rxtx_cap'"
op|':'
number|'3'
op|'}'
newline|'\n'
nl|'\n'
name|'floating_ip_fields'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.1.100'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'auto_assigned'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
name|'mac_address_fields'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'FakeModel'
op|'('
name|'network_fields'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'fixed_ips'
op|'='
op|'['
name|'fixed_ip_fields'
op|']'
newline|'\n'
name|'floating_ips'
op|'='
op|'['
name|'floating_ip_fields'
op|']'
newline|'\n'
name|'mac_addresses'
op|'='
op|'['
name|'mac_address_fields'
op|']'
newline|'\n'
name|'networks'
op|'='
op|'['
name|'network_fields'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_floating_ip_allocate_address
name|'def'
name|'fake_floating_ip_allocate_address'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'fixed_ip_id'"
op|']'
op|'=='
name|'None'
name|'and'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'None'
op|','
nl|'\n'
name|'floating_ips'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'db'
op|'.'
name|'NoMoreAddresses'
op|'('
op|')'
newline|'\n'
dedent|''
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
name|'return'
name|'FakeModel'
op|'('
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_floating_ip_deallocate
dedent|''
name|'def'
name|'fake_floating_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'floating_ips'
op|')'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'auto_assigned'"
op|']'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|fake_floating_ip_disassociate
dedent|''
dedent|''
name|'def'
name|'fake_floating_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'floating_ips'
op|')'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip_address'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'fixed_ip_address'
op|'='
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'return'
name|'fixed_ip_address'
newline|'\n'
nl|'\n'
DECL|function|fake_floating_ip_fixed_ip_associate
dedent|''
dedent|''
name|'def'
name|'fake_floating_ip_fixed_ip_associate'
op|'('
name|'context'
op|','
name|'floating_address'
op|','
nl|'\n'
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'float'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'floating_address'
op|','
nl|'\n'
name|'floating_ips'
op|')'
newline|'\n'
name|'fixed'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'fixed_address'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'if'
name|'float'
name|'and'
name|'fixed'
op|':'
newline|'\n'
indent|'            '
name|'float'
op|'['
number|'0'
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'fixed'
op|'['
number|'0'
op|']'
newline|'\n'
name|'float'
op|'['
number|'0'
op|']'
op|'['
string|"'fixed_ip_id'"
op|']'
op|'='
name|'fixed'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_floating_ip_get_all_by_host
dedent|''
dedent|''
name|'def'
name|'fake_floating_ip_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
comment|'# TODO(jkoelker): Once we get the patches that remove host from'
nl|'\n'
comment|"#                 the floating_ip table, we'll need to stub"
nl|'\n'
comment|'#                 this out'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_floating_ip_get_by_address
dedent|''
name|'def'
name|'fake_floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'floating_ips'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FloatingIpNotFound'
op|'('
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'FakeModel'
op|'('
name|'ips'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_floating_ip_set_auto_assigned
dedent|''
name|'def'
name|'fake_floating_ip_set_auto_assigned'
op|'('
name|'contex'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'floating_ips'
op|')'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'auto_assigned'"
op|']'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_associate
dedent|''
dedent|''
name|'def'
name|'fake_fixed_ip_associate'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'db'
op|'.'
name|'NoMoreAddresses'
op|'('
op|')'
newline|'\n'
dedent|''
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'instance'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance_id'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_associate_pool
dedent|''
name|'def'
name|'fake_fixed_ip_associate_pool'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
op|'('
name|'i'
op|'['
string|"'network_id'"
op|']'
op|'=='
name|'network_id'
name|'or'
name|'i'
op|'['
string|"'network_id'"
op|']'
name|'is'
name|'None'
op|')'
name|'and'
name|'not'
name|'i'
op|'['
string|"'instance'"
op|']'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'db'
op|'.'
name|'NoMoreAddresses'
op|'('
op|')'
newline|'\n'
dedent|''
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'instance'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance_id'
newline|'\n'
name|'return'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_create
dedent|''
name|'def'
name|'fake_fixed_ip_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip'
op|'='
name|'dict'
op|'('
name|'fixed_ip_fields'
op|')'
newline|'\n'
name|'ip'
op|'['
string|"'id'"
op|']'
op|'='
name|'max'
op|'('
op|'['
name|'i'
op|'['
string|"'id'"
op|']'
name|'for'
name|'i'
name|'in'
name|'fixed_ips'
op|']'
name|'or'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|'+'
number|'1'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'['
name|'key'
op|']'
op|'='
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'ip'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_disassociate
dedent|''
name|'def'
name|'fake_fixed_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'instance'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'mac_address_id'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_disassociate_all_by_timeout
dedent|''
dedent|''
name|'def'
name|'fake_fixed_ip_disassociate_all_by_timeout'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'time'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_all_by_instance
dedent|''
name|'def'
name|'fake_fixed_ip_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'instance_id'"
op|']'
op|'=='
name|'instance_id'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'ips'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_by_address
dedent|''
name|'def'
name|'fake_fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FakeModel'
op|'('
name|'ips'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_network
dedent|''
dedent|''
name|'def'
name|'fake_fixed_ip_get_network'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'nets'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'n'
op|':'
name|'n'
op|'['
string|"'id'"
op|']'
op|'=='
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'network_id'"
op|']'
op|','
nl|'\n'
name|'networks'
op|')'
newline|'\n'
name|'if'
name|'nets'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'FakeModel'
op|'('
name|'nets'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_update
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|','
nl|'\n'
name|'fixed_ips'
op|')'
newline|'\n'
name|'if'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'                '
name|'ips'
op|'['
number|'0'
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
name|'if'
name|'key'
op|'=='
string|"'mac_address_id'"
op|':'
newline|'\n'
indent|'                    '
name|'mac'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'x'
op|':'
name|'x'
op|'['
string|"'id'"
op|']'
op|'=='
name|'values'
op|'['
name|'key'
op|']'
op|','
nl|'\n'
name|'mac_addresses'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'mac'
op|':'
newline|'\n'
indent|'                        '
name|'continue'
newline|'\n'
dedent|''
name|'fixed_ip_fields'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'FakeModel'
op|'('
name|'mac'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_by_id
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_instance_type_get_by_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'flavor_fields'
op|'['
string|"'id'"
op|']'
op|'=='
name|'id'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FakeModel'
op|'('
name|'flavor_fields'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_mac_address_create
dedent|''
dedent|''
name|'def'
name|'fake_mac_address_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mac'
op|'='
name|'dict'
op|'('
name|'mac_address_fields'
op|')'
newline|'\n'
name|'mac'
op|'['
string|"'id'"
op|']'
op|'='
name|'max'
op|'('
op|'['
name|'m'
op|'['
string|"'id'"
op|']'
name|'for'
name|'m'
name|'in'
name|'mac_addresses'
op|']'
name|'or'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|'+'
number|'1'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'mac'
op|'['
name|'key'
op|']'
op|'='
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'FakeModel'
op|'('
name|'mac'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_mac_address_delete_by_instance
dedent|''
name|'def'
name|'fake_mac_address_delete_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'addresses'
op|'='
op|'['
name|'m'
name|'for'
name|'m'
name|'in'
name|'mac_addresses'
name|'if'
name|'m'
op|'['
string|"'instance_id'"
op|']'
op|'=='
name|'instance_id'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'address'
name|'in'
name|'addresses'
op|':'
newline|'\n'
indent|'                '
name|'mac_addresses'
op|'.'
name|'remove'
op|'('
name|'address'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_mac_address_get_all_by_instance
dedent|''
dedent|''
name|'def'
name|'fake_mac_address_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'m'
op|')'
name|'for'
name|'m'
name|'in'
name|'mac_addresses'
name|'if'
name|'m'
op|'['
string|"'instance_id'"
op|']'
op|'=='
name|'instance_id'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_mac_address_get_by_instance_and_network
dedent|''
name|'def'
name|'fake_mac_address_get_by_instance_and_network'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mac'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'m'
op|':'
name|'m'
op|'['
string|"'instance_id'"
op|']'
op|'=='
name|'instance_id'
name|'and'
name|'m'
op|'['
string|"'network_id'"
op|']'
op|'=='
name|'network_id'
op|','
nl|'\n'
name|'mac_addresses'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'mac'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'FakeModel'
op|'('
name|'mac'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_create_safe
dedent|''
name|'def'
name|'fake_network_create_safe'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'net'
op|'='
name|'dict'
op|'('
name|'network_fields'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'id'"
op|']'
op|'='
name|'max'
op|'('
op|'['
name|'n'
op|'['
string|"'id'"
op|']'
name|'for'
name|'n'
name|'in'
name|'networks'
op|']'
name|'or'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|'+'
number|'1'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|'['
name|'key'
op|']'
op|'='
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'FakeModel'
op|'('
name|'net'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get
dedent|''
name|'def'
name|'fake_network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'net'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'n'
op|':'
name|'n'
op|'['
string|"'id'"
op|']'
op|'=='
name|'network_id'
op|','
name|'networks'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'net'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'FakeModel'
op|'('
name|'net'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_all
dedent|''
name|'def'
name|'fake_network_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'n'
op|')'
name|'for'
name|'n'
name|'in'
name|'networks'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_all_by_host
dedent|''
name|'def'
name|'fake_network_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nets'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'n'
op|':'
name|'n'
op|'['
string|"'host'"
op|']'
op|'=='
name|'host'
op|','
name|'networks'
op|')'
newline|'\n'
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'n'
op|')'
name|'for'
name|'n'
name|'in'
name|'nets'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_all_by_instance
dedent|''
name|'def'
name|'fake_network_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nets'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'n'
op|':'
name|'n'
op|'['
string|"'instance_id'"
op|']'
op|'=='
name|'instance_id'
op|','
name|'networks'
op|')'
newline|'\n'
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'n'
op|')'
name|'for'
name|'n'
name|'in'
name|'nets'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_network_set_host
dedent|''
name|'def'
name|'fake_network_set_host'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'host_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nets'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'n'
op|':'
name|'n'
op|'['
string|"'id'"
op|']'
op|'=='
name|'network_id'
op|','
name|'networks'
op|')'
newline|'\n'
name|'for'
name|'net'
name|'in'
name|'nets'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|'['
string|"'host'"
op|']'
op|'='
name|'host_id'
newline|'\n'
dedent|''
name|'return'
name|'host_id'
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
indent|'        '
name|'nets'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'n'
op|':'
name|'n'
op|'['
string|"'id'"
op|']'
op|'=='
name|'network_id'
op|','
name|'networks'
op|')'
newline|'\n'
name|'for'
name|'net'
name|'in'
name|'nets'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'                '
name|'net'
op|'['
name|'key'
op|']'
op|'='
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_project_get_networks
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_project_get_networks'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'n'
op|')'
name|'for'
name|'n'
name|'in'
name|'networks'
name|'if'
name|'n'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_queue_get_for
dedent|''
name|'def'
name|'fake_queue_get_for'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s.%s"'
op|'%'
op|'('
name|'topic'
op|','
name|'node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'funcs'
op|'='
op|'['
name|'fake_floating_ip_allocate_address'
op|','
nl|'\n'
name|'fake_floating_ip_deallocate'
op|','
nl|'\n'
name|'fake_floating_ip_disassociate'
op|','
nl|'\n'
name|'fake_floating_ip_fixed_ip_associate'
op|','
nl|'\n'
name|'fake_floating_ip_get_all_by_host'
op|','
nl|'\n'
name|'fake_floating_ip_get_by_address'
op|','
nl|'\n'
name|'fake_floating_ip_set_auto_assigned'
op|','
nl|'\n'
name|'fake_fixed_ip_associate'
op|','
nl|'\n'
name|'fake_fixed_ip_associate_pool'
op|','
nl|'\n'
name|'fake_fixed_ip_create'
op|','
nl|'\n'
name|'fake_fixed_ip_disassociate'
op|','
nl|'\n'
name|'fake_fixed_ip_disassociate_all_by_timeout'
op|','
nl|'\n'
name|'fake_fixed_ip_get_all_by_instance'
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_address'
op|','
nl|'\n'
name|'fake_fixed_ip_get_network'
op|','
nl|'\n'
name|'fake_fixed_ip_update'
op|','
nl|'\n'
name|'fake_instance_type_get_by_id'
op|','
nl|'\n'
name|'fake_mac_address_create'
op|','
nl|'\n'
name|'fake_mac_address_delete_by_instance'
op|','
nl|'\n'
name|'fake_mac_address_get_all_by_instance'
op|','
nl|'\n'
name|'fake_mac_address_get_by_instance_and_network'
op|','
nl|'\n'
name|'fake_network_create_safe'
op|','
nl|'\n'
name|'fake_network_get'
op|','
nl|'\n'
name|'fake_network_get_all'
op|','
nl|'\n'
name|'fake_network_get_all_by_host'
op|','
nl|'\n'
name|'fake_network_get_all_by_instance'
op|','
nl|'\n'
name|'fake_network_set_host'
op|','
nl|'\n'
name|'fake_network_update'
op|','
nl|'\n'
name|'fake_project_get_networks'
op|','
nl|'\n'
name|'fake_queue_get_for'
op|']'
newline|'\n'
nl|'\n'
name|'stub_out'
op|'('
name|'stubs'
op|','
name|'funcs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_db_instance_api
dedent|''
name|'def'
name|'stub_out_db_instance_api'
op|'('
name|'stubs'
op|','
name|'injected'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out the db API for creating Instances."""'
newline|'\n'
nl|'\n'
name|'INSTANCE_TYPES'
op|'='
op|'{'
nl|'\n'
string|"'m1.tiny'"
op|':'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'flavorid'
op|'='
number|'1'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'m1.small'"
op|':'
name|'dict'
op|'('
name|'id'
op|'='
number|'5'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2048'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'20'
op|','
nl|'\n'
name|'flavorid'
op|'='
number|'2'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'2'
op|')'
op|','
nl|'\n'
string|"'m1.medium'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'4096'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'2'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'40'
op|','
nl|'\n'
name|'flavorid'
op|'='
number|'3'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'3'
op|')'
op|','
nl|'\n'
string|"'m1.large'"
op|':'
name|'dict'
op|'('
name|'id'
op|'='
number|'3'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'8192'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'80'
op|','
nl|'\n'
name|'flavorid'
op|'='
number|'4'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'4'
op|')'
op|','
nl|'\n'
string|"'m1.xlarge'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'4'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'16384'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'8'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'160'
op|','
nl|'\n'
name|'flavorid'
op|'='
number|'5'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'5'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'flat_network_fields'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake_flat'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'xenbr0'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'fake_flat_network'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'fe80::a00:0/120'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'120'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'fe80::a00:1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'10.0.0.255'"
op|','
nl|'\n'
string|"'dns'"
op|':'
string|"'10.0.0.2'"
op|','
nl|'\n'
string|"'ra_server'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'injected'
op|'}'
newline|'\n'
nl|'\n'
name|'vlan_network_fields'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake_vlan'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'br111'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'fake_vlan_network'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'fe80::a00:0/120'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'120'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'fe80::a00:1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'10.0.0.255'"
op|','
nl|'\n'
string|"'dns'"
op|':'
string|"'10.0.0.2'"
op|','
nl|'\n'
string|"'ra_server'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vlan'"
op|':'
number|'111'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
name|'fixed_ip_fields'
op|'='
op|'{'
string|"'address'"
op|':'
string|"'10.0.0.3'"
op|','
nl|'\n'
string|"'address_v6'"
op|':'
string|"'fe80::a00:3'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
string|"'fake_flat'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_all
name|'def'
name|'fake_instance_type_get_all'
op|'('
name|'context'
op|','
name|'inactive'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_by_name
dedent|''
name|'def'
name|'fake_instance_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_by_id
dedent|''
name|'def'
name|'fake_instance_type_get_by_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'name'
op|','
name|'inst_type'
name|'in'
name|'INSTANCE_TYPES'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'str'
op|'('
name|'inst_type'
op|'['
string|"'id'"
op|']'
op|')'
op|'=='
name|'str'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'inst_type'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_by_instance
dedent|''
name|'def'
name|'fake_network_get_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
comment|'# Even instance numbers are on vlan networks'
nl|'\n'
indent|'        '
name|'if'
name|'instance_id'
op|'%'
number|'2'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FakeModel'
op|'('
name|'vlan_network_fields'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FakeModel'
op|'('
name|'flat_network_fields'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_network_get_all_by_instance
dedent|''
dedent|''
name|'def'
name|'fake_network_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
comment|'# Even instance numbers are on vlan networks'
nl|'\n'
indent|'        '
name|'if'
name|'instance_id'
op|'%'
number|'2'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'vlan_network_fields'
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'flat_network_fields'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_fixed_addresses
dedent|''
dedent|''
name|'def'
name|'fake_instance_get_fixed_addresses'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'fixed_ip_fields'
op|')'
op|'.'
name|'address'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_fixed_addresses_v6
dedent|''
name|'def'
name|'fake_instance_get_fixed_addresses_v6'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'fixed_ip_fields'
op|')'
op|'.'
name|'address'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_by_instance
dedent|''
name|'def'
name|'fake_fixed_ip_get_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'fixed_ip_fields'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'funcs'
op|'='
op|'['
name|'fake_network_get_by_instance'
op|','
nl|'\n'
name|'fake_network_get_all_by_instance'
op|','
nl|'\n'
name|'fake_instance_type_get_all'
op|','
nl|'\n'
name|'fake_instance_type_get_by_name'
op|','
nl|'\n'
name|'fake_instance_type_get_by_id'
op|','
nl|'\n'
name|'fake_instance_get_fixed_addresses'
op|','
nl|'\n'
name|'fake_instance_get_fixed_addresses_v6'
op|','
nl|'\n'
name|'fake_network_get_all_by_instance'
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_instance'
op|']'
newline|'\n'
name|'stub_out'
op|'('
name|'stubs'
op|','
name|'funcs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
