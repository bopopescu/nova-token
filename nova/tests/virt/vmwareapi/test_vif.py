begin_unit
comment|'# Copyright 2013 Canonical Corp.'
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
name|'contextlib'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
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
name|'import'
name|'matchers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'test_vm_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'network_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vif'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vm_util'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareVifTestCase
name|'class'
name|'VMwareVifTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'VMwareVifTestCase'
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
name|'flags'
op|'('
name|'vlan_interface'
op|'='
string|"'vmnet0'"
op|','
name|'group'
op|'='
string|"'vmware'"
op|')'
newline|'\n'
name|'network'
op|'='
name|'network_model'
op|'.'
name|'Network'
op|'('
name|'id'
op|'='
number|'0'
op|','
nl|'\n'
name|'bridge'
op|'='
string|"'fa0'"
op|','
nl|'\n'
name|'label'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'vlan'
op|'='
number|'3'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
string|"'eth0'"
op|','
nl|'\n'
name|'injected'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
nl|'\n'
name|'network_model'
op|'.'
name|'VIF'
op|'('
name|'id'
op|'='
name|'None'
op|','
nl|'\n'
name|'address'
op|'='
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\n'
name|'network'
op|'='
name|'network'
op|','
nl|'\n'
name|'type'
op|'='
name|'None'
op|','
nl|'\n'
name|'devname'
op|'='
name|'None'
op|','
nl|'\n'
name|'ovs_interfaceid'
op|'='
name|'None'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'3'
op|')'
nl|'\n'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'test_vm_util'
op|'.'
name|'fake_session'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cluster'
op|'='
name|'None'
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
name|'super'
op|'('
name|'VMwareVifTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ensure_vlan_bridge
dedent|''
name|'def'
name|'test_ensure_vlan_bridge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'get_network_with_the_name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'get_vswitch_for_vlan_interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'check_if_vlan_interface_exists'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'create_port_group'"
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'get_vswitch_for_vlan_interface'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'vmnet0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'vmnet0'"
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'check_if_vlan_interface_exists'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'vmnet0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'create_port_group'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
string|"'vmnet0'"
op|','
number|'3'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'create_vlan'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|"# FlatDHCP network mode without vlan - network doesn't exist with the host"
nl|'\n'
DECL|member|test_ensure_vlan_bridge_without_vlan
dedent|''
name|'def'
name|'test_ensure_vlan_bridge_without_vlan'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'get_network_with_the_name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'get_vswitch_for_vlan_interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'check_if_vlan_interface_exists'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'create_port_group'"
op|')'
newline|'\n'
nl|'\n'
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'get_vswitch_for_vlan_interface'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'vmnet0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'vmnet0'"
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'check_if_vlan_interface_exists'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'vmnet0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'create_port_group'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
string|"'vmnet0'"
op|','
number|'0'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'create_vlan'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# FlatDHCP network mode without vlan - network exists with the host'
nl|'\n'
comment|'# Get vswitch and check vlan interface should not be called'
nl|'\n'
DECL|member|test_ensure_vlan_bridge_with_network
dedent|''
name|'def'
name|'test_ensure_vlan_bridge_with_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'get_network_with_the_name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'get_vswitch_for_vlan_interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'check_if_vlan_interface_exists'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'create_port_group'"
op|')'
newline|'\n'
name|'vm_network'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'VM Network'"
op|','
string|"'type'"
op|':'
string|"'Network'"
op|'}'
newline|'\n'
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vm_network'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'create_vlan'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# Flat network mode with DVS'
nl|'\n'
DECL|member|test_ensure_vlan_bridge_with_existing_dvs
dedent|''
name|'def'
name|'test_ensure_vlan_bridge_with_existing_dvs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_ref'
op|'='
op|'{'
string|"'dvpg'"
op|':'
string|"'dvportgroup-2062'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'DistributedVirtualPortgroup'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'get_network_with_the_name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'get_vswitch_for_vlan_interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
nl|'\n'
string|"'check_if_vlan_interface_exists'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'create_port_group'"
op|')'
newline|'\n'
nl|'\n'
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'network_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'ref'
op|'='
name|'vif'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|','
nl|'\n'
name|'create_vlan'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'ref'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'network_ref'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_neutron
dedent|''
name|'def'
name|'test_get_network_ref_neutron'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vif'
op|','
string|"'get_neutron_network'"
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'get_neutron_network'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'fa0'"
op|','
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'vif'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'get_network_ref'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_flat_dhcp
dedent|''
name|'def'
name|'test_get_network_ref_flat_dhcp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vif'
op|','
string|"'ensure_vlan_bridge'"
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'cluster'
op|'='
name|'self'
op|'.'
name|'cluster'
op|','
nl|'\n'
name|'create_vlan'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'get_network_ref'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_bridge
dedent|''
name|'def'
name|'test_get_network_ref_bridge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vif'
op|','
string|"'ensure_vlan_bridge'"
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'cluster'
op|'='
name|'self'
op|'.'
name|'cluster'
op|','
nl|'\n'
name|'create_vlan'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'network'
op|'='
name|'network_model'
op|'.'
name|'Network'
op|'('
name|'id'
op|'='
number|'0'
op|','
nl|'\n'
name|'bridge'
op|'='
string|"'fa0'"
op|','
nl|'\n'
name|'label'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'vlan'
op|'='
number|'3'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
string|"'eth0'"
op|','
nl|'\n'
name|'injected'
op|'='
name|'True'
op|','
nl|'\n'
name|'should_create_vlan'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vif'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
nl|'\n'
name|'network_model'
op|'.'
name|'VIF'
op|'('
name|'id'
op|'='
name|'None'
op|','
nl|'\n'
name|'address'
op|'='
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\n'
name|'network'
op|'='
name|'network'
op|','
nl|'\n'
name|'type'
op|'='
name|'None'
op|','
nl|'\n'
name|'devname'
op|'='
name|'None'
op|','
nl|'\n'
name|'ovs_interfaceid'
op|'='
name|'None'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'3'
op|')'
nl|'\n'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vif'
op|'.'
name|'get_network_ref'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'vif'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_bridge
dedent|''
name|'def'
name|'test_get_network_ref_bridge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'opaque_networks'
op|'='
op|'['
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'bridge_id'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'vif'
op|'.'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque_networks'
op|','
nl|'\n'
string|"'integration_bridge'"
op|','
string|"'bridge_id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'bridge_id'"
op|','
name|'network_ref'
op|'['
string|"'network-id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_bridges
dedent|''
name|'def'
name|'test_get_network_ref_bridges'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'opaque_networks'
op|'='
op|'['
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'bridge_id1'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name1'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'bridge_id2'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name2'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'vif'
op|'.'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque_networks'
op|','
nl|'\n'
string|"'integration_bridge'"
op|','
string|"'bridge_id2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'bridge_id2'"
op|','
name|'network_ref'
op|'['
string|"'network-id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_integration
dedent|''
name|'def'
name|'test_get_network_ref_integration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'opaque_networks'
op|'='
op|'['
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'integration_bridge'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'vif'
op|'.'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque_networks'
op|','
nl|'\n'
string|"'integration_bridge'"
op|','
string|"'bridge_id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'integration_bridge'"
op|','
name|'network_ref'
op|'['
string|"'network-id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_bridge_none
dedent|''
name|'def'
name|'test_get_network_ref_bridge_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'opaque_networks'
op|'='
op|'['
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'bridge_id1'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name1'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'bridge_id2'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name2'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'vif'
op|'.'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque_networks'
op|','
nl|'\n'
string|"'integration_bridge'"
op|','
string|"'bridge_id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'network_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_network_ref_integration_multiple
dedent|''
name|'def'
name|'test_get_network_ref_integration_multiple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'opaque_networks'
op|'='
op|'['
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'bridge_id1'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name1'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'opaqueNetworkId'"
op|':'
string|"'integration_bridge'"
op|','
nl|'\n'
string|"'opaqueNetworkName'"
op|':'
string|"'name2'"
op|','
nl|'\n'
string|"'opaqueNetworkType'"
op|':'
string|"'OpaqueNetwork'"
op|'}'
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'vif'
op|'.'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque_networks'
op|','
nl|'\n'
string|"'integration_bridge'"
op|','
string|"'bridge_id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'network_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_neutron_network
dedent|''
name|'def'
name|'test_get_neutron_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_util'
op|','
string|"'get_host_ref'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vif'
op|','
string|"'_get_network_ref_from_opaque'"
op|')'
newline|'\n'
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake-host'"
op|')'
newline|'\n'
name|'opaque'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'opaque'
op|'.'
name|'HostOpaqueNetworkInfo'
op|'='
op|'['
string|"'fake-network-info'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_property"'
op|','
nl|'\n'
string|"'fake-host'"
op|','
string|"'HostSystem'"
op|','
nl|'\n'
string|"'config.network.opaqueNetwork'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'opaque'
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque'
op|'.'
name|'HostOpaqueNetworkInfo'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'integration_bridge'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake-network-ref'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'vif'
op|'.'
name|'get_neutron_network'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network_ref'
op|','
string|"'fake-network-ref'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_neutron_network_opaque_network_not_found
dedent|''
name|'def'
name|'test_get_neutron_network_opaque_network_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_util'
op|','
string|"'get_host_ref'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vif'
op|','
string|"'_get_network_ref_from_opaque'"
op|')'
newline|'\n'
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake-host'"
op|')'
newline|'\n'
name|'opaque'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'opaque'
op|'.'
name|'HostOpaqueNetworkInfo'
op|'='
op|'['
string|"'fake-network-info'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_property"'
op|','
nl|'\n'
string|"'fake-host'"
op|','
string|"'HostSystem'"
op|','
nl|'\n'
string|"'config.network.opaqueNetwork'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'opaque'
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque'
op|'.'
name|'HostOpaqueNetworkInfo'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'integration_bridge'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NetworkNotFoundForBridge'
op|','
nl|'\n'
name|'vif'
op|'.'
name|'get_neutron_network'
op|','
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'vif'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_neutron_network_bridge_network_not_found
dedent|''
name|'def'
name|'test_get_neutron_network_bridge_network_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_util'
op|','
string|"'get_host_ref'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'network_util'
op|','
string|"'get_network_with_the_name'"
op|')'
newline|'\n'
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake-host'"
op|')'
newline|'\n'
name|'opaque'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'opaque'
op|'.'
name|'HostOpaqueNetworkInfo'
op|'='
op|'['
string|"'fake-network-info'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_property"'
op|','
nl|'\n'
string|"'fake-host'"
op|','
string|"'HostSystem'"
op|','
nl|'\n'
string|"'config.network.opaqueNetwork'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'self'
op|'.'
name|'session'
op|','
number|'0'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cluster'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NetworkNotFoundForBridge'
op|','
nl|'\n'
name|'vif'
op|'.'
name|'get_neutron_network'
op|','
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'vif'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_port_group_already_exists
dedent|''
name|'def'
name|'test_create_port_group_already_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'method'
op|'=='
string|"'AddPortGroup'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'error_util'
op|'.'
name|'AlreadyExistsException'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_add_vswitch_port_group_spec'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_host_ref'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_add_vswitch'
op|','
name|'_get_host'
op|','
name|'_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_util'
op|'.'
name|'create_port_group'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'pg_name'"
op|','
nl|'\n'
string|"'vswitch_name'"
op|','
name|'vlan_id'
op|'='
number|'0'
op|','
nl|'\n'
name|'cluster'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_port_group_exception
dedent|''
dedent|''
name|'def'
name|'test_create_port_group_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'method'
op|'=='
string|"'AddPortGroup'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'error_util'
op|'.'
name|'VMwareDriverException'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_add_vswitch_port_group_spec'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_host_ref'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_add_vswitch'
op|','
name|'_get_host'
op|','
name|'_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'error_util'
op|'.'
name|'VMwareDriverException'
op|','
nl|'\n'
name|'network_util'
op|'.'
name|'create_port_group'
op|','
nl|'\n'
name|'self'
op|'.'
name|'session'
op|','
string|"'pg_name'"
op|','
nl|'\n'
string|"'vswitch_name'"
op|','
name|'vlan_id'
op|'='
number|'0'
op|','
nl|'\n'
name|'cluster'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_neutron_network_invalid_property
dedent|''
dedent|''
name|'def'
name|'test_get_neutron_network_invalid_property'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'method'
op|'=='
string|"'get_dynamic_property'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'error_util'
op|'.'
name|'InvalidPropertyException'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_host_ref'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'network_util'
op|','
string|"'get_network_with_the_name'"
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_get_host'
op|','
name|'_call_method'
op|','
name|'_get_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vif'
op|'.'
name|'get_neutron_network'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'network_name'"
op|','
nl|'\n'
string|"'cluster'"
op|','
string|"'vif'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vif_info_none
dedent|''
dedent|''
name|'def'
name|'test_get_vif_info_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif_info'
op|'='
name|'vif'
op|'.'
name|'get_vif_info'
op|'('
string|"'fake_session'"
op|','
string|"'fake_cluster'"
op|','
nl|'\n'
string|"'is_neutron'"
op|','
string|"'fake_model'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'vif_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vif'
op|','
string|"'get_network_ref'"
op|','
name|'return_value'
op|'='
string|"'fake_ref'"
op|')'
newline|'\n'
DECL|member|test_get_vif_info
name|'def'
name|'test_get_vif_info'
op|'('
name|'self'
op|','
name|'mock_get_network_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_info'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
newline|'\n'
name|'vif_info'
op|'='
name|'vif'
op|'.'
name|'get_vif_info'
op|'('
string|"'fake_session'"
op|','
string|"'fake_cluster'"
op|','
nl|'\n'
string|"'is_neutron'"
op|','
string|"'fake_model'"
op|','
name|'network_info'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
op|'{'
string|"'iface_id'"
op|':'
string|"'vif-xxx-yyy-zzz'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'network_name'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'network_ref'"
op|':'
string|"'fake_ref'"
op|','
nl|'\n'
string|"'vif_model'"
op|':'
string|"'fake_model'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'vif_info'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
