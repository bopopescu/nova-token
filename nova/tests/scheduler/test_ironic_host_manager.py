begin_unit
comment|'# Copyright (c) 2014 OpenStack Foundation'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
string|'"""\nTests For IronicHostManager\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'host_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'ironic_host_manager'
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
name|'scheduler'
name|'import'
name|'ironic_fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeFilterClass1
name|'class'
name|'FakeFilterClass1'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
DECL|member|host_passes
indent|'    '
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeFilterClass2
dedent|''
dedent|''
name|'class'
name|'FakeFilterClass2'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
DECL|member|host_passes
indent|'    '
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IronicHostManagerTestCase
dedent|''
dedent|''
name|'class'
name|'IronicHostManagerTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for IronicHostManager class."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'IronicHostManagerTestCase'
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
name|'host_manager'
op|'='
name|'ironic_host_manager'
op|'.'
name|'IronicHostManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_manager_public_api_signatures
dedent|''
name|'def'
name|'test_manager_public_api_signatures'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertPublicAPISignatures'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_state_public_api_signatures
dedent|''
name|'def'
name|'test_state_public_api_signatures'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertPublicAPISignatures'
op|'('
nl|'\n'
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|'"dummy"'
op|','
nl|'\n'
string|'"dummy"'
op|')'
op|','
nl|'\n'
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|'('
string|'"dummy"'
op|','
nl|'\n'
string|'"dummy"'
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_host_states
dedent|''
name|'def'
name|'test_get_all_host_states'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure .service is set and we have the values we expect to.'
nl|'\n'
indent|'        '
name|'context'
op|'='
string|"'fake_context'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'compute_node_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ironic_fakes'
op|'.'
name|'COMPUTE_NODES'
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
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'context'
op|')'
newline|'\n'
name|'host_states_map'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_state_map'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'host_states_map'
op|')'
op|','
number|'4'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'4'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'compute_node'
op|'='
name|'ironic_fakes'
op|'.'
name|'COMPUTE_NODES'
op|'['
name|'i'
op|']'
newline|'\n'
name|'host'
op|'='
name|'compute_node'
op|'['
string|"'service'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'node'
op|'='
name|'compute_node'
op|'['
string|"'hypervisor_hostname'"
op|']'
newline|'\n'
name|'state_key'
op|'='
op|'('
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'compute_node'
op|'['
string|"'service'"
op|']'
op|','
nl|'\n'
name|'host_states_map'
op|'['
name|'state_key'
op|']'
op|'.'
name|'service'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'compute_node'
op|'['
string|"'stats'"
op|']'
op|')'
op|','
nl|'\n'
name|'host_states_map'
op|'['
name|'state_key'
op|']'
op|'.'
name|'stats'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'compute_node'
op|'['
string|"'free_ram_mb'"
op|']'
op|','
nl|'\n'
name|'host_states_map'
op|'['
name|'state_key'
op|']'
op|'.'
name|'free_ram_mb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'compute_node'
op|'['
string|"'free_disk_gb'"
op|']'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'host_states_map'
op|'['
name|'state_key'
op|']'
op|'.'
name|'free_disk_mb'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IronicHostManagerChangedNodesTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'IronicHostManagerChangedNodesTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for IronicHostManager class."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'IronicHostManagerChangedNodesTestCase'
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
name|'host_manager'
op|'='
name|'ironic_host_manager'
op|'.'
name|'IronicHostManager'
op|'('
op|')'
newline|'\n'
name|'ironic_driver'
op|'='
string|'"nova.virt.ironic.driver.IronicDriver"'
newline|'\n'
name|'supported_instances'
op|'='
string|'\'[["i386", "baremetal", "baremetal"]]\''
newline|'\n'
name|'self'
op|'.'
name|'compute_node'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'10'
op|','
name|'memory_mb'
op|'='
number|'1024'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'0'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'memory_mb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
string|"'baremetal cpu'"
op|','
nl|'\n'
name|'stats'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'dict'
op|'('
nl|'\n'
name|'ironic_driver'
op|'='
name|'ironic_driver'
op|','
nl|'\n'
name|'cpu_arch'
op|'='
string|"'i386'"
op|')'
op|')'
op|','
nl|'\n'
name|'supported_instances'
op|'='
name|'supported_instances'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'10'
op|','
name|'free_ram_mb'
op|'='
number|'1024'
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
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|','
string|"'__init__'"
op|')'
newline|'\n'
DECL|member|test_create_ironic_node_state
name|'def'
name|'test_create_ironic_node_state'
op|'('
name|'self'
op|','
name|'init_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'init_mock'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
name|'compute'
op|'='
op|'{'
string|"'cpu_info'"
op|':'
string|"'baremetal cpu'"
op|'}'
newline|'\n'
name|'host_state'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_state_cls'
op|'('
string|"'fake-host'"
op|','
string|"'fake-node'"
op|','
nl|'\n'
name|'compute'
op|'='
name|'compute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIs'
op|'('
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|','
name|'type'
op|'('
name|'host_state'
op|')'
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
name|'host_manager'
op|'.'
name|'HostState'
op|','
string|"'__init__'"
op|')'
newline|'\n'
DECL|member|test_create_non_ironic_host_state
name|'def'
name|'test_create_non_ironic_host_state'
op|'('
name|'self'
op|','
name|'init_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'init_mock'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
name|'compute'
op|'='
op|'{'
string|"'cpu_info'"
op|':'
string|"'other cpu'"
op|'}'
newline|'\n'
name|'host_state'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_state_cls'
op|'('
string|"'fake-host'"
op|','
string|"'fake-node'"
op|','
nl|'\n'
name|'compute'
op|'='
name|'compute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIs'
op|'('
name|'host_manager'
op|'.'
name|'HostState'
op|','
name|'type'
op|'('
name|'host_state'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_host_states_after_delete_one
dedent|''
name|'def'
name|'test_get_all_host_states_after_delete_one'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
string|"'fake_context'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'compute_node_get_all'"
op|')'
newline|'\n'
comment|'# all nodes active for first call'
nl|'\n'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ironic_fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
comment|'# remove node4 for second call'
nl|'\n'
name|'running_nodes'
op|'='
op|'['
name|'n'
name|'for'
name|'n'
name|'in'
name|'ironic_fakes'
op|'.'
name|'COMPUTE_NODES'
nl|'\n'
name|'if'
name|'n'
op|'.'
name|'get'
op|'('
string|"'hypervisor_hostname'"
op|')'
op|'!='
string|"'node4uuid'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'running_nodes'
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
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'context'
op|')'
newline|'\n'
name|'host_states_map'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_state_map'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'host_states_map'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_host_states_after_delete_all
dedent|''
name|'def'
name|'test_get_all_host_states_after_delete_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
string|"'fake_context'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'compute_node_get_all'"
op|')'
newline|'\n'
comment|'# all nodes active for first call'
nl|'\n'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ironic_fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
comment|'# remove all nodes for second call'
nl|'\n'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
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
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'context'
op|')'
newline|'\n'
name|'host_states_map'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_state_map'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'host_states_map'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_from_compute_node
dedent|''
name|'def'
name|'test_update_from_compute_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|'('
string|'"fakehost"'
op|','
string|'"fakenode"'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'update_from_compute_node'
op|'('
name|'self'
op|'.'
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1024'
op|','
name|'host'
op|'.'
name|'free_ram_mb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1024'
op|','
name|'host'
op|'.'
name|'total_usable_ram_mb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'10240'
op|','
name|'host'
op|'.'
name|'free_disk_mb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'host'
op|'.'
name|'vcpus_total'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'host'
op|'.'
name|'vcpus_used'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'self'
op|'.'
name|'compute_node'
op|'['
string|"'stats'"
op|']'
op|')'
op|','
nl|'\n'
name|'host'
op|'.'
name|'stats'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_consume_identical_instance_from_compute
dedent|''
name|'def'
name|'test_consume_identical_instance_from_compute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|'('
string|'"fakehost"'
op|','
string|'"fakenode"'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'update_from_compute_node'
op|'('
name|'self'
op|'.'
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'10'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'1024'
op|','
name|'vcpus'
op|'='
number|'1'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'consume_from_instance'
op|'('
string|"'fake-context'"
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'host'
op|'.'
name|'vcpus_used'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'host'
op|'.'
name|'free_ram_mb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'host'
op|'.'
name|'free_disk_mb'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_consume_larger_instance_from_compute
dedent|''
name|'def'
name|'test_consume_larger_instance_from_compute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|'('
string|'"fakehost"'
op|','
string|'"fakenode"'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'update_from_compute_node'
op|'('
name|'self'
op|'.'
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'20'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'2'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'consume_from_instance'
op|'('
string|"'fake-context'"
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'host'
op|'.'
name|'vcpus_used'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'host'
op|'.'
name|'free_ram_mb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'host'
op|'.'
name|'free_disk_mb'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_consume_smaller_instance_from_compute
dedent|''
name|'def'
name|'test_consume_smaller_instance_from_compute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|'('
string|'"fakehost"'
op|','
string|'"fakenode"'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'update_from_compute_node'
op|'('
name|'self'
op|'.'
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'5'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'consume_from_instance'
op|'('
string|"'fake-context'"
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'host'
op|'.'
name|'vcpus_used'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'host'
op|'.'
name|'free_ram_mb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'host'
op|'.'
name|'free_disk_mb'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IronicHostManagerTestFilters
dedent|''
dedent|''
name|'class'
name|'IronicHostManagerTestFilters'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test filters work for IronicHostManager."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'IronicHostManagerTestFilters'
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
name|'host_manager'
op|'='
name|'ironic_host_manager'
op|'.'
name|'IronicHostManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_hosts'
op|'='
op|'['
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|'('
nl|'\n'
string|"'fake_host%s'"
op|'%'
name|'x'
op|','
string|"'fake-node'"
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'1'
op|','
number|'5'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'fake_hosts'
op|'+='
op|'['
name|'ironic_host_manager'
op|'.'
name|'IronicNodeState'
op|'('
nl|'\n'
string|"'fake_multihost'"
op|','
string|"'fake-node%s'"
op|'%'
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'1'
op|','
number|'5'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_choose_host_filters_not_found
dedent|''
name|'def'
name|'test_choose_host_filters_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_default_filters'
op|'='
string|"'FakeFilterClass3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'filter_classes'
op|'='
op|'['
name|'FakeFilterClass1'
op|','
nl|'\n'
name|'FakeFilterClass2'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'SchedulerHostFilterNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'_choose_host_filters'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_choose_host_filters
dedent|''
name|'def'
name|'test_choose_host_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_default_filters'
op|'='
op|'['
string|"'FakeFilterClass2'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'filter_classes'
op|'='
op|'['
name|'FakeFilterClass1'
op|','
nl|'\n'
name|'FakeFilterClass2'
op|']'
newline|'\n'
nl|'\n'
comment|'# Test we returns 1 correct function'
nl|'\n'
name|'filter_classes'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'_choose_host_filters'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'filter_classes'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'FakeFilterClass2'"
op|','
name|'filter_classes'
op|'['
number|'0'
op|']'
op|'.'
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_mock_get_filtered_hosts
dedent|''
name|'def'
name|'_mock_get_filtered_hosts'
op|'('
name|'self'
op|','
name|'info'
op|','
name|'specified_filters'
op|'='
name|'None'
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
name|'self'
op|'.'
name|'host_manager'
op|','
string|"'_choose_host_filters'"
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'got_objs'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'info'
op|'['
string|"'got_fprops'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_filter_one
name|'def'
name|'fake_filter_one'
op|'('
name|'_self'
op|','
name|'obj'
op|','
name|'filter_props'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'['
string|"'got_objs'"
op|']'
op|'.'
name|'append'
op|'('
name|'obj'
op|')'
newline|'\n'
name|'info'
op|'['
string|"'got_fprops'"
op|']'
op|'.'
name|'append'
op|'('
name|'filter_props'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'FakeFilterClass1'
op|','
string|"'_filter_one'"
op|','
name|'fake_filter_one'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'_choose_host_filters'
op|'('
name|'specified_filters'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
name|'FakeFilterClass1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_result
dedent|''
name|'def'
name|'_verify_result'
op|'('
name|'self'
op|','
name|'info'
op|','
name|'result'
op|','
name|'filters'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'info'
op|'['
string|"'got_fprops'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'x'
op|','
name|'info'
op|'['
string|"'expected_fprops'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'filters'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'info'
op|'['
string|"'expected_objs'"
op|']'
op|')'
op|','
name|'set'
op|'('
name|'info'
op|'['
string|"'got_objs'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'info'
op|'['
string|"'expected_objs'"
op|']'
op|')'
op|','
name|'set'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts
dedent|''
name|'def'
name|'test_get_filtered_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'moo'"
op|':'
number|'1'
op|','
string|"'cow'"
op|':'
number|'2'
op|'}'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_specified_filters
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_specified_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'moo'"
op|':'
number|'1'
op|','
string|"'cow'"
op|':'
number|'2'
op|'}'
newline|'\n'
nl|'\n'
name|'specified_filters'
op|'='
op|'['
string|"'FakeFilterClass1'"
op|','
string|"'FakeFilterClass2'"
op|']'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
op|','
name|'specified_filters'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|','
name|'filter_class_names'
op|'='
name|'specified_filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_ignore
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_ignore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'ignore_hosts'"
op|':'
op|'['
string|"'fake_host1'"
op|','
string|"'fake_host3'"
op|','
nl|'\n'
string|"'fake_host5'"
op|','
string|"'fake_multihost'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
comment|'# [1] and [3] are host2 and host4'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'1'
op|']'
op|','
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'3'
op|']'
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_force_hosts
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_force_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_hosts'"
op|':'
op|'['
string|"'fake_host1'"
op|','
string|"'fake_host3'"
op|','
nl|'\n'
string|"'fake_host5'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
comment|'# [0] and [2] are host1 and host3'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'0'
op|']'
op|','
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'2'
op|']'
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_no_matching_force_hosts
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_no_matching_force_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_hosts'"
op|':'
op|'['
string|"'fake_host5'"
op|','
string|"'fake_host6'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_ignore_and_force_hosts
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_ignore_and_force_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure ignore_hosts processed before force_hosts in host filters.'
nl|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_hosts'"
op|':'
op|'['
string|"'fake_host3'"
op|','
string|"'fake_host1'"
op|']'
op|','
nl|'\n'
string|"'ignore_hosts'"
op|':'
op|'['
string|"'fake_host1'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
comment|'# only fake_host3 should be left.'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'2'
op|']'
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_force_host_and_many_nodes
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_force_host_and_many_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure all nodes returned for a host with many nodes'
nl|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_hosts'"
op|':'
op|'['
string|"'fake_multihost'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'4'
op|']'
op|','
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'5'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'6'
op|']'
op|','
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'7'
op|']'
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_force_nodes
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_force_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_nodes'"
op|':'
op|'['
string|"'fake-node2'"
op|','
string|"'fake-node4'"
op|','
nl|'\n'
string|"'fake-node9'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
comment|'# [5] is fake-node2, [7] is fake-node4'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'5'
op|']'
op|','
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'7'
op|']'
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_force_hosts_and_nodes
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_force_hosts_and_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure only overlapping results if both force host and node'
nl|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_hosts'"
op|':'
op|'['
string|"'fake_host1'"
op|','
string|"'fake_multihost'"
op|']'
op|','
nl|'\n'
string|"'force_nodes'"
op|':'
op|'['
string|"'fake-node2'"
op|','
string|"'fake-node9'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
comment|'# [5] is fake-node2'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'5'
op|']'
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_force_hosts_and_wrong_nodes
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_force_hosts_and_wrong_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure non-overlapping force_node and force_host yield no result'
nl|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_hosts'"
op|':'
op|'['
string|"'fake_multihost'"
op|']'
op|','
nl|'\n'
string|"'force_nodes'"
op|':'
op|'['
string|"'fake-node'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_ignore_hosts_and_force_nodes
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_ignore_hosts_and_force_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure ignore_hosts can coexist with force_nodes'
nl|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_nodes'"
op|':'
op|'['
string|"'fake-node4'"
op|','
string|"'fake-node2'"
op|']'
op|','
nl|'\n'
string|"'ignore_hosts'"
op|':'
op|'['
string|"'fake_host1'"
op|','
string|"'fake_host2'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'5'
op|']'
op|','
name|'self'
op|'.'
name|'fake_hosts'
op|'['
number|'7'
op|']'
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_hosts_with_ignore_hosts_and_force_same_nodes
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_ignore_hosts_and_force_same_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure ignore_hosts is processed before force_nodes'
nl|'\n'
indent|'        '
name|'fake_properties'
op|'='
op|'{'
string|"'force_nodes'"
op|':'
op|'['
string|"'fake_node4'"
op|','
string|"'fake_node2'"
op|']'
op|','
nl|'\n'
string|"'ignore_hosts'"
op|':'
op|'['
string|"'fake_multihost'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'expected_objs'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'expected_fprops'"
op|':'
name|'fake_properties'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mock_get_filtered_hosts'
op|'('
name|'info'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'self'
op|'.'
name|'fake_hosts'
op|','
nl|'\n'
name|'fake_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_result'
op|'('
name|'info'
op|','
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
