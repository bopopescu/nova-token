begin_unit
comment|'# Copyright (c) 2014 Rackspace Hosting'
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
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
name|'import'
name|'range'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'caching_scheduler'
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
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'scheduler'
name|'import'
name|'test_scheduler'
newline|'\n'
nl|'\n'
DECL|variable|ENABLE_PROFILER
name|'ENABLE_PROFILER'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CachingSchedulerTestCase
name|'class'
name|'CachingSchedulerTestCase'
op|'('
name|'test_scheduler'
op|'.'
name|'SchedulerTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Caching Scheduler."""'
newline|'\n'
nl|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'caching_scheduler'
op|'.'
name|'CachingScheduler'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'caching_scheduler'
op|'.'
name|'CachingScheduler'
op|','
nl|'\n'
string|'"_get_up_hosts"'
op|')'
newline|'\n'
DECL|member|test_run_periodic_tasks_loads_hosts
name|'def'
name|'test_run_periodic_tasks_loads_hosts'
op|'('
name|'self'
op|','
name|'mock_up_hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_up_hosts'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'run_periodic_tasks'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_up_hosts'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'self'
op|'.'
name|'driver'
op|'.'
name|'all_host_states'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'elevated'
op|'.'
name|'assert_called_with'
op|'('
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
name|'caching_scheduler'
op|'.'
name|'CachingScheduler'
op|','
nl|'\n'
string|'"_get_up_hosts"'
op|')'
newline|'\n'
DECL|member|test_get_all_host_states_returns_cached_value
name|'def'
name|'test_get_all_host_states_returns_cached_value'
op|'('
name|'self'
op|','
name|'mock_up_hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'all_host_states'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_get_all_host_states'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_up_hosts'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'self'
op|'.'
name|'driver'
op|'.'
name|'all_host_states'
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
name|'caching_scheduler'
op|'.'
name|'CachingScheduler'
op|','
nl|'\n'
string|'"_get_up_hosts"'
op|')'
newline|'\n'
DECL|member|test_get_all_host_states_loads_hosts
name|'def'
name|'test_get_all_host_states_loads_hosts'
op|'('
name|'self'
op|','
name|'mock_up_hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_up_hosts'
op|'.'
name|'return_value'
op|'='
op|'['
string|'"asdf"'
op|']'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_get_all_host_states'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_up_hosts'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|'"asdf"'
op|']'
op|','
name|'self'
op|'.'
name|'driver'
op|'.'
name|'all_host_states'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|'"asdf"'
op|']'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_up_hosts
dedent|''
name|'def'
name|'test_get_up_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
nl|'\n'
string|'"get_all_host_states"'
op|')'
name|'as'
name|'mock_get_hosts'
op|':'
newline|'\n'
indent|'            '
name|'mock_get_hosts'
op|'.'
name|'return_value'
op|'='
op|'['
string|'"asdf"'
op|']'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_get_up_hosts'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_get_hosts'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_get_hosts'
op|'.'
name|'return_value'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_select_destination_raises_with_no_hosts
dedent|''
dedent|''
name|'def'
name|'test_select_destination_raises_with_no_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'spec_obj'
op|'='
name|'self'
op|'.'
name|'_get_fake_request_spec'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'all_host_states'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
DECL|member|test_select_destination_works
name|'def'
name|'test_select_destination_works'
op|'('
name|'self'
op|','
name|'mock_get_extra'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'spec_obj'
op|'='
name|'self'
op|'.'
name|'_get_fake_request_spec'
op|'('
op|')'
newline|'\n'
name|'fake_host'
op|'='
name|'self'
op|'.'
name|'_get_fake_host_state'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'all_host_states'
op|'='
op|'['
name|'fake_host'
op|']'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_test_select_destinations'
op|'('
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
number|'0'
op|']'
op|'['
string|'"host"'
op|']'
op|','
name|'fake_host'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_select_destinations
dedent|''
name|'def'
name|'_test_select_destinations'
op|'('
name|'self'
op|','
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_fake_request_spec
dedent|''
name|'def'
name|'_get_fake_request_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): Prevent to stub the Flavor.get_by_id call just by'
nl|'\n'
comment|'# directly providing a Flavor object'
nl|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
nl|'\n'
name|'flavorid'
op|'='
string|'"small"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'root_gb'
op|'='
number|'1'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'1'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'swap'
op|'='
number|'0'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'instance_properties'
op|'='
op|'{'
nl|'\n'
string|'"os_type"'
op|':'
string|'"linux"'
op|','
nl|'\n'
string|'"project_id"'
op|':'
string|'"1234"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'request_spec'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'flavor'
op|'='
name|'flavor'
op|','
nl|'\n'
name|'num_instances'
op|'='
number|'1'
op|','
nl|'\n'
name|'ignore_hosts'
op|'='
name|'None'
op|','
nl|'\n'
name|'force_hosts'
op|'='
name|'None'
op|','
nl|'\n'
name|'force_nodes'
op|'='
name|'None'
op|','
nl|'\n'
name|'retry'
op|'='
name|'None'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'None'
op|','
nl|'\n'
name|'image'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_group'
op|'='
name|'None'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|','
nl|'\n'
op|'**'
name|'instance_properties'
nl|'\n'
op|')'
newline|'\n'
name|'return'
name|'request_spec'
newline|'\n'
nl|'\n'
DECL|member|_get_fake_host_state
dedent|''
name|'def'
name|'_get_fake_host_state'
op|'('
name|'self'
op|','
name|'index'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_state'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
nl|'\n'
string|"'host_%s'"
op|'%'
name|'index'
op|','
nl|'\n'
string|"'node_%s'"
op|'%'
name|'index'
op|')'
newline|'\n'
name|'host_state'
op|'.'
name|'free_ram_mb'
op|'='
number|'50000'
newline|'\n'
name|'host_state'
op|'.'
name|'total_usable_ram_mb'
op|'='
number|'50000'
newline|'\n'
name|'host_state'
op|'.'
name|'free_disk_mb'
op|'='
number|'4096'
newline|'\n'
name|'host_state'
op|'.'
name|'service'
op|'='
op|'{'
nl|'\n'
string|'"disabled"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'host_state'
op|'.'
name|'cpu_allocation_ratio'
op|'='
number|'16.0'
newline|'\n'
name|'host_state'
op|'.'
name|'ram_allocation_ratio'
op|'='
number|'1.5'
newline|'\n'
name|'host_state'
op|'.'
name|'disk_allocation_ratio'
op|'='
number|'1.0'
newline|'\n'
name|'host_state'
op|'.'
name|'metrics'
op|'='
name|'objects'
op|'.'
name|'MonitorMetricList'
op|'('
name|'objects'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'return'
name|'host_state'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
DECL|member|test_performance_check_select_destination
name|'def'
name|'test_performance_check_select_destination'
op|'('
name|'self'
op|','
name|'mock_get_extra'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hosts'
op|'='
number|'2'
newline|'\n'
name|'requests'
op|'='
number|'1'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'service_down_time'
op|'='
number|'240'
op|')'
newline|'\n'
nl|'\n'
name|'spec_obj'
op|'='
name|'self'
op|'.'
name|'_get_fake_request_spec'
op|'('
op|')'
newline|'\n'
name|'host_states'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'host_state'
op|'='
name|'self'
op|'.'
name|'_get_fake_host_state'
op|'('
name|'x'
op|')'
newline|'\n'
name|'host_states'
op|'.'
name|'append'
op|'('
name|'host_state'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'.'
name|'all_host_states'
op|'='
name|'host_states'
newline|'\n'
nl|'\n'
DECL|function|run_test
name|'def'
name|'run_test'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'a'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'requests'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'b'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'c'
op|'='
name|'b'
op|'-'
name|'a'
newline|'\n'
nl|'\n'
name|'seconds'
op|'='
op|'('
name|'c'
op|'.'
name|'days'
op|'*'
number|'24'
op|'*'
number|'60'
op|'*'
number|'60'
op|'+'
name|'c'
op|'.'
name|'seconds'
op|')'
newline|'\n'
name|'microseconds'
op|'='
name|'seconds'
op|'*'
number|'1000'
op|'+'
name|'c'
op|'.'
name|'microseconds'
op|'/'
number|'1000.0'
newline|'\n'
name|'per_request_ms'
op|'='
name|'microseconds'
op|'/'
name|'requests'
newline|'\n'
name|'return'
name|'per_request_ms'
newline|'\n'
nl|'\n'
dedent|''
name|'per_request_ms'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'ENABLE_PROFILER'
op|':'
newline|'\n'
indent|'            '
name|'import'
name|'pycallgraph'
newline|'\n'
name|'from'
name|'pycallgraph'
name|'import'
name|'output'
newline|'\n'
name|'config'
op|'='
name|'pycallgraph'
op|'.'
name|'Config'
op|'('
name|'max_depth'
op|'='
number|'10'
op|')'
newline|'\n'
name|'config'
op|'.'
name|'trace_filter'
op|'='
name|'pycallgraph'
op|'.'
name|'GlobbingFilter'
op|'('
name|'exclude'
op|'='
op|'['
nl|'\n'
string|"'pycallgraph.*'"
op|','
nl|'\n'
string|"'unittest.*'"
op|','
nl|'\n'
string|"'testtools.*'"
op|','
nl|'\n'
string|"'nova.tests.unit.*'"
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'graphviz'
op|'='
name|'output'
op|'.'
name|'GraphvizOutput'
op|'('
name|'output_file'
op|'='
string|"'scheduler.png'"
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'pycallgraph'
op|'.'
name|'PyCallGraph'
op|'('
name|'output'
op|'='
name|'graphviz'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'per_request_ms'
op|'='
name|'run_test'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'per_request_ms'
op|'='
name|'run_test'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# This has proved to be around 1 ms on a random dev box'
nl|'\n'
comment|'# But this is here so you can do simply performance testing easily.'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'per_request_ms'
op|'<'
number|'1000'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
comment|'# A handy tool to help profile the schedulers performance'
nl|'\n'
DECL|variable|ENABLE_PROFILER
indent|'    '
name|'ENABLE_PROFILER'
op|'='
name|'True'
newline|'\n'
name|'import'
name|'testtools'
newline|'\n'
DECL|variable|suite
name|'suite'
op|'='
name|'testtools'
op|'.'
name|'ConcurrentTestSuite'
op|'('
op|')'
newline|'\n'
DECL|variable|test
name|'test'
op|'='
string|'"test_performance_check_select_destination"'
newline|'\n'
DECL|variable|test_case
name|'test_case'
op|'='
name|'CachingSchedulerTestCase'
op|'('
name|'test'
op|')'
newline|'\n'
name|'suite'
op|'.'
name|'addTest'
op|'('
name|'test_case'
op|')'
newline|'\n'
DECL|variable|runner
name|'runner'
op|'='
name|'testtools'
op|'.'
name|'TextTestResult'
op|'.'
name|'TextTestRunner'
op|'('
op|')'
newline|'\n'
name|'runner'
op|'.'
name|'run'
op|'('
name|'suite'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
