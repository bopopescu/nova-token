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
nl|'\n'
name|'import'
name|'datetime'
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
name|'timeutils'
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
op|'.'
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeFilterClass1
name|'class'
name|'ComputeFilterClass1'
op|'('
name|'object'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeFilterClass2
dedent|''
dedent|''
name|'class'
name|'ComputeFilterClass2'
op|'('
name|'object'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
string|'"""Test case for HostManager class"""'
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
string|"'ComputeFilterClass3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'filter_classes'
op|'='
op|'['
name|'ComputeFilterClass1'
op|','
nl|'\n'
name|'ComputeFilterClass2'
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
string|"'ComputeFilterClass2'"
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
name|'ComputeFilterClass1'
op|','
nl|'\n'
name|'ComputeFilterClass2'
op|']'
newline|'\n'
nl|'\n'
comment|"# Test 'compute' returns 1 correct function"
nl|'\n'
name|'filter_fns'
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
name|'filter_fns'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'filter_fns'
op|'['
number|'0'
op|']'
op|'.'
name|'__func__'
op|','
nl|'\n'
name|'ComputeFilterClass2'
op|'.'
name|'host_passes'
op|'.'
name|'__func__'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_hosts
dedent|''
name|'def'
name|'test_filter_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'topic'
op|'='
string|"'fake_topic'"
newline|'\n'
nl|'\n'
name|'filters'
op|'='
op|'['
string|"'fake-filter1'"
op|','
string|"'fake-filter2'"
op|']'
newline|'\n'
name|'fake_host1'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host1'"
op|','
name|'topic'
op|')'
newline|'\n'
name|'fake_host2'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host2'"
op|','
name|'topic'
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
name|'fake_host1'
op|','
name|'fake_host2'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
string|"'fake_properties'"
newline|'\n'
nl|'\n'
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
nl|'\n'
string|"'_choose_host_filters'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'fake_host1'
op|','
string|"'passes_filters'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'fake_host2'
op|','
string|"'passes_filters'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'_choose_host_filters'
op|'('
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'filters'
op|')'
newline|'\n'
name|'fake_host1'
op|'.'
name|'passes_filters'
op|'('
name|'filters'
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'False'
op|')'
newline|'\n'
name|'fake_host2'
op|'.'
name|'passes_filters'
op|'('
name|'filters'
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'True'
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
name|'filtered_hosts'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'filter_hosts'
op|'('
name|'hosts'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'filters'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'filtered_hosts'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'filtered_hosts'
op|'['
number|'0'
op|']'
op|','
name|'fake_host2'
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
name|'assertDictMatch'
op|'('
name|'service_states'
op|','
op|'{'
op|'}'
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
number|'31338'
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
op|')'
newline|'\n'
name|'host1_volume_capabs'
op|'='
name|'dict'
op|'('
name|'free_disk'
op|'='
number|'4321'
op|','
name|'timestamp'
op|'='
number|'1'
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
string|"'volume'"
op|','
string|"'host1'"
op|','
nl|'\n'
name|'host1_volume_capabs'
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
comment|"# Make sure dictionary isn't re-assigned"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'service_states'
op|','
name|'service_states'
op|')'
newline|'\n'
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
name|'host1_volume_capabs'
op|'['
string|"'timestamp'"
op|']'
op|'='
number|'31338'
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
string|"'host1'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host1_compute_capabs'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'host1_volume_capabs'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host2_compute_capabs'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'service_states'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_service_caps_stale
dedent|''
name|'def'
name|'test_host_service_caps_stale'
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
name|'periodic_interval'
op|'='
number|'5'
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
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3000'
op|')'
op|')'
newline|'\n'
name|'host1_volume_capabs'
op|'='
name|'dict'
op|'('
name|'free_disk'
op|'='
number|'4321'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3005'
op|')'
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
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3010'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'service_states'
op|'='
op|'{'
string|"'host1'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host1_compute_capabs'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'host1_volume_capabs'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host2_compute_capabs'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'service_states'
op|'='
name|'service_states'
newline|'\n'
nl|'\n'
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
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3020'
op|')'
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
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3020'
op|')'
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
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3020'
op|')'
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
name|'res1'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_service_caps_stale'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'res2'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_service_caps_stale'
op|'('
string|"'host1'"
op|','
string|"'volume'"
op|')'
newline|'\n'
name|'res3'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'host_service_caps_stale'
op|'('
string|"'host2'"
op|','
string|"'compute'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res1'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res2'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res3'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_expired_host_services
dedent|''
name|'def'
name|'test_delete_expired_host_services'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3000'
op|')'
op|')'
newline|'\n'
name|'host1_volume_capabs'
op|'='
name|'dict'
op|'('
name|'free_disk'
op|'='
number|'4321'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3005'
op|')'
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
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3010'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'service_states'
op|'='
op|'{'
string|"'host1'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host1_compute_capabs'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'host1_volume_capabs'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host2_compute_capabs'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'service_states'
op|'='
name|'service_states'
newline|'\n'
nl|'\n'
name|'to_delete'
op|'='
op|'{'
string|"'host1'"
op|':'
op|'{'
string|"'volume'"
op|':'
name|'host1_volume_capabs'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host2_compute_capabs'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'delete_expired_host_services'
op|'('
name|'to_delete'
op|')'
newline|'\n'
comment|"# Make sure dictionary isn't re-assigned"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'service_states'
op|','
name|'service_states'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'host1'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host1_compute_capabs'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'service_states'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_service_capabilities
dedent|''
name|'def'
name|'test_get_service_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host1_compute_capabs'
op|'='
name|'dict'
op|'('
name|'free_memory'
op|'='
number|'1000'
op|','
name|'host_memory'
op|'='
number|'5678'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3000'
op|')'
op|')'
newline|'\n'
name|'host1_volume_capabs'
op|'='
name|'dict'
op|'('
name|'free_disk'
op|'='
number|'4321'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3005'
op|')'
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
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3010'
op|')'
op|')'
newline|'\n'
name|'host2_volume_capabs'
op|'='
name|'dict'
op|'('
name|'free_disk'
op|'='
number|'8756'
op|','
nl|'\n'
name|'enabled'
op|'='
name|'False'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3010'
op|')'
op|')'
newline|'\n'
name|'host3_compute_capabs'
op|'='
name|'dict'
op|'('
name|'free_memory'
op|'='
number|'1234'
op|','
name|'host_memory'
op|'='
number|'4000'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3010'
op|')'
op|')'
newline|'\n'
name|'host3_volume_capabs'
op|'='
name|'dict'
op|'('
name|'free_disk'
op|'='
number|'2000'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'fromtimestamp'
op|'('
number|'3010'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'service_states'
op|'='
op|'{'
string|"'host1'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host1_compute_capabs'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'host1_volume_capabs'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host2_compute_capabs'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'host2_volume_capabs'
op|'}'
op|','
nl|'\n'
string|"'host3'"
op|':'
op|'{'
string|"'compute'"
op|':'
name|'host3_compute_capabs'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'host3_volume_capabs'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'service_states'
op|'='
name|'service_states'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'called'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
comment|'# This tests with 1 volume disabled (host2), and 1 volume node'
nl|'\n'
comment|'# as stale (host1)'
nl|'\n'
DECL|function|_fake_host_service_caps_stale
name|'def'
name|'_fake_host_service_caps_stale'
op|'('
name|'host'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'['
string|"'called'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'if'
name|'host'
op|'=='
string|"'host1'"
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'service'
op|'=='
string|"'compute'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'elif'
name|'service'
op|'=='
string|"'volume'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'host'
op|'=='
string|"'host2'"
op|':'
newline|'\n'
comment|"# Shouldn't get here for 'volume' because the service"
nl|'\n'
comment|'# is disabled'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'service'
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host'
op|','
string|"'host3'"
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'host_manager'
op|','
string|"'host_service_caps_stale'"
op|','
nl|'\n'
name|'_fake_host_service_caps_stale'
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
string|"'delete_expired_host_services'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'delete_expired_host_services'
op|'('
op|'{'
string|"'host1'"
op|':'
op|'['
string|"'volume'"
op|']'
op|'}'
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
name|'get_service_capabilities'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'5'
op|')'
newline|'\n'
nl|'\n'
comment|"# only 1 volume node active == 'host3', so min/max is 2000"
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'volume_free_disk'"
op|':'
op|'('
number|'2000'
op|','
number|'2000'
op|')'
op|','
nl|'\n'
string|"'compute_host_memory'"
op|':'
op|'('
number|'4000'
op|','
number|'5678'
op|')'
op|','
nl|'\n'
string|"'compute_free_memory'"
op|':'
op|'('
number|'1000'
op|','
number|'8756'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'result'
op|','
name|'expected'
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
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'reserved_host_memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'reserved_host_disk_mb'
op|'='
number|'1024'
op|')'
newline|'\n'
nl|'\n'
name|'context'
op|'='
string|"'fake_context'"
newline|'\n'
name|'topic'
op|'='
string|"'compute'"
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_all'"
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
name|'db'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'instance_type'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fakes'
op|'.'
name|'INSTANCES'
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
name|'host_states'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'context'
op|','
name|'topic'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'host_states'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
name|'host'
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
name|'host_states'
op|'['
string|"'host1'"
op|']'
op|'.'
name|'free_ram_mb'
op|','
number|'0'
op|')'
newline|'\n'
comment|'# 511GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
string|"'host1'"
op|']'
op|'.'
name|'free_disk_mb'
op|','
number|'523264'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
string|"'host2'"
op|']'
op|'.'
name|'free_ram_mb'
op|','
number|'512'
op|')'
newline|'\n'
comment|'# 1023GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
string|"'host2'"
op|']'
op|'.'
name|'free_disk_mb'
op|','
number|'1047552'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
string|"'host3'"
op|']'
op|'.'
name|'free_ram_mb'
op|','
number|'2560'
op|')'
newline|'\n'
comment|'# 3071GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
string|"'host3'"
op|']'
op|'.'
name|'free_disk_mb'
op|','
number|'3144704'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
string|"'host4'"
op|']'
op|'.'
name|'free_ram_mb'
op|','
number|'7680'
op|')'
newline|'\n'
comment|'# 8191GB'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host_states'
op|'['
string|"'host4'"
op|']'
op|'.'
name|'free_disk_mb'
op|','
number|'8387584'
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
string|'"""Test case for HostState class"""'
newline|'\n'
nl|'\n'
comment|'# update_from_compute_node() and consume_from_instance() are tested'
nl|'\n'
comment|'# in HostManagerTestCase.test_get_all_host_states()'
nl|'\n'
nl|'\n'
DECL|member|test_host_state_passes_filters_passes
name|'def'
name|'test_host_state_passes_filters_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_host'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'cls1'
op|'='
name|'ComputeFilterClass1'
op|'('
op|')'
newline|'\n'
name|'cls2'
op|'='
name|'ComputeFilterClass2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls1'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls2'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'filter_fns'
op|'='
op|'['
name|'cls1'
op|'.'
name|'host_passes'
op|','
name|'cls2'
op|'.'
name|'host_passes'
op|']'
newline|'\n'
nl|'\n'
name|'cls1'
op|'.'
name|'host_passes'
op|'('
name|'fake_host'
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'cls2'
op|'.'
name|'host_passes'
op|'('
name|'fake_host'
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'fake_host'
op|'.'
name|'passes_filters'
op|'('
name|'filter_fns'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_state_passes_filters_passes_with_ignore
dedent|''
name|'def'
name|'test_host_state_passes_filters_passes_with_ignore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_host'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'ignore_hosts'"
op|':'
op|'['
string|"'host2'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'cls1'
op|'='
name|'ComputeFilterClass1'
op|'('
op|')'
newline|'\n'
name|'cls2'
op|'='
name|'ComputeFilterClass2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls1'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls2'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'filter_fns'
op|'='
op|'['
name|'cls1'
op|'.'
name|'host_passes'
op|','
name|'cls2'
op|'.'
name|'host_passes'
op|']'
newline|'\n'
nl|'\n'
name|'cls1'
op|'.'
name|'host_passes'
op|'('
name|'fake_host'
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'cls2'
op|'.'
name|'host_passes'
op|'('
name|'fake_host'
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'fake_host'
op|'.'
name|'passes_filters'
op|'('
name|'filter_fns'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_state_passes_filters_fails
dedent|''
name|'def'
name|'test_host_state_passes_filters_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_host'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'cls1'
op|'='
name|'ComputeFilterClass1'
op|'('
op|')'
newline|'\n'
name|'cls2'
op|'='
name|'ComputeFilterClass2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls1'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls2'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'filter_fns'
op|'='
op|'['
name|'cls1'
op|'.'
name|'host_passes'
op|','
name|'cls2'
op|'.'
name|'host_passes'
op|']'
newline|'\n'
nl|'\n'
name|'cls1'
op|'.'
name|'host_passes'
op|'('
name|'fake_host'
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
comment|'# cls2.host_passes() not called because of short circuit'
nl|'\n'
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
name|'fake_host'
op|'.'
name|'passes_filters'
op|'('
name|'filter_fns'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_state_passes_filters_fails_from_ignore
dedent|''
name|'def'
name|'test_host_state_passes_filters_fails_from_ignore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_host'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'ignore_hosts'"
op|':'
op|'['
string|"'host1'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'cls1'
op|'='
name|'ComputeFilterClass1'
op|'('
op|')'
newline|'\n'
name|'cls2'
op|'='
name|'ComputeFilterClass2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls1'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls2'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'filter_fns'
op|'='
op|'['
name|'cls1'
op|'.'
name|'host_passes'
op|','
name|'cls2'
op|'.'
name|'host_passes'
op|']'
newline|'\n'
nl|'\n'
comment|'# cls[12].host_passes() not called because of short circuit'
nl|'\n'
comment|'# with matching host to ignore'
nl|'\n'
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
name|'fake_host'
op|'.'
name|'passes_filters'
op|'('
name|'filter_fns'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_state_passes_filters_skipped_from_force
dedent|''
name|'def'
name|'test_host_state_passes_filters_skipped_from_force'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_host'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'force_hosts'"
op|':'
op|'['
string|"'host1'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'cls1'
op|'='
name|'ComputeFilterClass1'
op|'('
op|')'
newline|'\n'
name|'cls2'
op|'='
name|'ComputeFilterClass2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls1'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cls2'
op|','
string|"'host_passes'"
op|')'
newline|'\n'
name|'filter_fns'
op|'='
op|'['
name|'cls1'
op|'.'
name|'host_passes'
op|','
name|'cls2'
op|'.'
name|'host_passes'
op|']'
newline|'\n'
nl|'\n'
comment|'# cls[12].host_passes() not called because of short circuit'
nl|'\n'
comment|'# with matching host to force'
nl|'\n'
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
name|'fake_host'
op|'.'
name|'passes_filters'
op|'('
name|'filter_fns'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
