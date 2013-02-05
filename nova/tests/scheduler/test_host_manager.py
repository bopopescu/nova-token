begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC'
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
string|'"""\nTests For HostManager\n"""'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
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
op|'.'
name|'scheduler'
name|'import'
name|'fakes'
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
DECL|class|HostManagerTestCase
dedent|''
dedent|''
name|'class'
name|'HostManagerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for HostManager class."""'
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
name|'HostManagerTestCase'
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
name|'host_manager'
op|'.'
name|'HostManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_hosts'
op|'='
op|'['
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'fake_host%s'"
op|'%'
name|'x'
op|','
nl|'\n'
string|"'fake-node'"
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
number|'5'
op|')'
op|']'
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
name|'timeutils'
op|'.'
name|'clear_time_override'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'HostManagerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
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
name|'len'
op|'('
name|'filter_classes'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'filter_classes'
op|'['
number|'0'
op|']'
op|'.'
name|'__name__'
op|','
string|"'FakeFilterClass2'"
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
DECL|member|test_get_filtered_hosts_with_specificed_filters
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_specificed_filters'
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
DECL|member|test_get_filtered_hosts_with_ignore_and_force
dedent|''
name|'def'
name|'test_get_filtered_hosts_with_ignore_and_force'
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
DECL|member|test_update_service_capabilities
dedent|''
name|'def'
name|'test_update_service_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service_states'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'service_states'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'service_states'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'timeutils'
op|','
string|"'utcnow'"
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'31337'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'31339'
op|')'
newline|'\n'
nl|'\n'
name|'host1_compute_capabs'
op|'='
name|'dict'
op|'('
name|'free_memory'
op|'='
number|'1234'
op|','
name|'host_memory'
op|'='
number|'5678'
op|','
nl|'\n'
name|'timestamp'
op|'='
number|'1'
op|','
name|'hypervisor_hostname'
op|'='
string|"'node1'"
op|')'
newline|'\n'
name|'host2_compute_capabs'
op|'='
name|'dict'
op|'('
name|'free_memory'
op|'='
number|'8756'
op|','
name|'timestamp'
op|'='
number|'1'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|"'node2'"
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
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'update_service_capabilities'
op|'('
string|"'compute'"
op|','
string|"'host1'"
op|','
nl|'\n'
name|'host1_compute_capabs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'update_service_capabilities'
op|'('
string|"'compute'"
op|','
string|"'host2'"
op|','
nl|'\n'
name|'host2_compute_capabs'
op|')'
newline|'\n'
nl|'\n'
comment|"# Make sure original dictionary wasn't copied"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host1_compute_capabs'
op|'['
string|"'timestamp'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'host1_compute_capabs'
op|'['
string|"'timestamp'"
op|']'
op|'='
number|'31337'
newline|'\n'
name|'host2_compute_capabs'
op|'['
string|"'timestamp'"
op|']'
op|'='
number|'31339'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|')'
op|':'
name|'host1_compute_capabs'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
string|"'node2'"
op|')'
op|':'
name|'host2_compute_capabs'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'service_states'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_service_capabilities_node_key
dedent|''
name|'def'
name|'test_update_service_capabilities_node_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service_states'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'service_states'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'service_states'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'host1_cap'
op|'='
op|'{'
string|"'hypervisor_hostname'"
op|':'
string|"'host1-hvhn'"
op|'}'
newline|'\n'
name|'host2_cap'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
number|'31337'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'update_service_capabilities'
op|'('
string|"'compute'"
op|','
string|"'host1'"
op|','
nl|'\n'
name|'host1_cap'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
number|'31338'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'update_service_capabilities'
op|'('
string|"'compute'"
op|','
string|"'host2'"
op|','
nl|'\n'
name|'host2_cap'
op|')'
newline|'\n'
name|'host1_cap'
op|'['
string|"'timestamp'"
op|']'
op|'='
number|'31337'
newline|'\n'
name|'host2_cap'
op|'['
string|"'timestamp'"
op|']'
op|'='
number|'31338'
newline|'\n'
name|'expected'
op|'='
op|'{'
op|'('
string|"'host1'"
op|','
string|"'host1-hvhn'"
op|')'
op|':'
name|'host1_cap'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
name|'None'
op|')'
op|':'
name|'host2_cap'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'service_states'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected'
op|')'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'host_manager'
op|'.'
name|'LOG'
op|','
string|"'warn'"
op|')'
newline|'\n'
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
name|'fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
comment|'# Invalid service'
nl|'\n'
name|'host_manager'
op|'.'
name|'LOG'
op|'.'
name|'warn'
op|'('
string|'"No service for compute ID 5"'
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
comment|'# Check that .service is set properly'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'4'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'compute_node'
op|'='
name|'fakes'
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
name|'host_states_map'
op|'['
name|'state_key'
op|']'
op|'.'
name|'service'
op|','
nl|'\n'
name|'compute_node'
op|'['
string|"'service'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|')'
op|']'
op|'.'
name|'free_ram_mb'
op|','
nl|'\n'
number|'512'
op|')'
newline|'\n'
comment|'# 511GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|')'
op|']'
op|'.'
name|'free_disk_mb'
op|','
nl|'\n'
number|'524288'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host2'"
op|','
string|"'node2'"
op|')'
op|']'
op|'.'
name|'free_ram_mb'
op|','
nl|'\n'
number|'1024'
op|')'
newline|'\n'
comment|'# 1023GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host2'"
op|','
string|"'node2'"
op|')'
op|']'
op|'.'
name|'free_disk_mb'
op|','
nl|'\n'
number|'1048576'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host3'"
op|','
string|"'node3'"
op|')'
op|']'
op|'.'
name|'free_ram_mb'
op|','
nl|'\n'
number|'3072'
op|')'
newline|'\n'
comment|'# 3071GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host3'"
op|','
string|"'node3'"
op|')'
op|']'
op|'.'
name|'free_disk_mb'
op|','
nl|'\n'
number|'3145728'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host4'"
op|','
string|"'node4'"
op|')'
op|']'
op|'.'
name|'free_ram_mb'
op|','
nl|'\n'
number|'8192'
op|')'
newline|'\n'
comment|'# 8191GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states_map'
op|'['
op|'('
string|"'host4'"
op|','
string|"'node4'"
op|')'
op|']'
op|'.'
name|'free_disk_mb'
op|','
nl|'\n'
number|'8388608'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostStateTestCase
dedent|''
dedent|''
name|'class'
name|'HostStateTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for HostState class."""'
newline|'\n'
nl|'\n'
comment|'# update_from_compute_node() and consume_from_instance() are tested'
nl|'\n'
comment|'# in HostManagerTestCase.test_get_all_host_states()'
nl|'\n'
nl|'\n'
DECL|member|test_stat_consumption_from_compute_node
name|'def'
name|'test_stat_consumption_from_compute_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stats'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_instances'"
op|','
name|'value'
op|'='
string|"'5'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_proj_12345'"
op|','
name|'value'
op|'='
string|"'3'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_proj_23456'"
op|','
name|'value'
op|'='
string|"'1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_vm_%s'"
op|'%'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'value'
op|'='
string|"'2'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_vm_%s'"
op|'%'
name|'vm_states'
op|'.'
name|'SUSPENDED'
op|','
name|'value'
op|'='
string|"'1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_task_%s'"
op|'%'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|','
name|'value'
op|'='
string|"'1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_task_%s'"
op|'%'
name|'task_states'
op|'.'
name|'MIGRATING'
op|','
name|'value'
op|'='
string|"'2'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_os_type_linux'"
op|','
name|'value'
op|'='
string|"'4'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'num_os_type_windoze'"
op|','
name|'value'
op|'='
string|"'1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'key'
op|'='
string|"'io_workload'"
op|','
name|'value'
op|'='
string|"'42'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'compute'
op|'='
name|'dict'
op|'('
name|'stats'
op|'='
name|'stats'
op|','
name|'memory_mb'
op|'='
number|'0'
op|','
name|'free_disk_gb'
op|'='
number|'0'
op|','
name|'local_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'free_ram_mb'
op|'='
number|'0'
op|','
name|'vcpus'
op|'='
number|'0'
op|','
name|'vcpus_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
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
name|'compute'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'5'
op|','
name|'host'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'host'
op|'.'
name|'num_instances_by_project'
op|'['
string|"'12345'"
op|']'
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
name|'num_instances_by_project'
op|'['
string|"'23456'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'host'
op|'.'
name|'vm_states'
op|'['
name|'vm_states'
op|'.'
name|'BUILDING'
op|']'
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
name|'vm_states'
op|'['
name|'vm_states'
op|'.'
name|'SUSPENDED'
op|']'
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
name|'task_states'
op|'['
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'host'
op|'.'
name|'task_states'
op|'['
name|'task_states'
op|'.'
name|'MIGRATING'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'host'
op|'.'
name|'num_instances_by_os_type'
op|'['
string|"'linux'"
op|']'
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
name|'num_instances_by_os_type'
op|'['
string|"'windoze'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'42'
op|','
name|'host'
op|'.'
name|'num_io_ops'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stat_consumption_from_instance
dedent|''
name|'def'
name|'test_stat_consumption_from_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|'"fakehost"'
op|','
string|'"fakenode"'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'0'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'0'
op|','
name|'vcpus'
op|'='
number|'0'
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'12345'"
op|','
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'SCHEDULING'
op|','
name|'os_type'
op|'='
string|"'Linux'"
op|')'
newline|'\n'
name|'host'
op|'.'
name|'consume_from_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'0'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'0'
op|','
name|'vcpus'
op|'='
number|'0'
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'12345'"
op|','
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'PAUSED'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|','
name|'os_type'
op|'='
string|"'Linux'"
op|')'
newline|'\n'
name|'host'
op|'.'
name|'consume_from_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'host'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'host'
op|'.'
name|'num_instances_by_project'
op|'['
string|"'12345'"
op|']'
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
name|'vm_states'
op|'['
name|'vm_states'
op|'.'
name|'BUILDING'
op|']'
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
name|'vm_states'
op|'['
name|'vm_states'
op|'.'
name|'PAUSED'
op|']'
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
name|'task_states'
op|'['
name|'task_states'
op|'.'
name|'SCHEDULING'
op|']'
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
name|'task_states'
op|'['
name|'None'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'host'
op|'.'
name|'num_instances_by_os_type'
op|'['
string|"'Linux'"
op|']'
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
name|'num_io_ops'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
