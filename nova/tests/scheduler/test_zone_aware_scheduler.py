begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nTests For Zone Aware Scheduler.\n"""'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'zone_aware_scheduler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'zone_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_host_caps
name|'def'
name|'_host_caps'
op|'('
name|'multiplier'
op|')'
op|':'
newline|'\n'
comment|'# Returns host capabilities in the following way:'
nl|'\n'
comment|'# host1 = memory:free 10 (100max)'
nl|'\n'
comment|'#         disk:available 100 (1000max)'
nl|'\n'
comment|'# hostN = memory:free 10 + 10N'
nl|'\n'
comment|'#         disk:available 100 + 100N'
nl|'\n'
comment|'# in other words: hostN has more resources than host0'
nl|'\n'
comment|"# which means ... don't go above 10 hosts."
nl|'\n'
indent|'    '
name|'return'
op|'{'
string|"'host_name-description'"
op|':'
string|"'XenServer %s'"
op|'%'
name|'multiplier'
op|','
nl|'\n'
string|"'host_hostname'"
op|':'
string|"'xs-%s'"
op|'%'
name|'multiplier'
op|','
nl|'\n'
string|"'host_memory_total'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'host_memory_overhead'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'host_memory_free'"
op|':'
number|'10'
op|'+'
name|'multiplier'
op|'*'
number|'10'
op|','
nl|'\n'
string|"'host_memory_free-computed'"
op|':'
number|'10'
op|'+'
name|'multiplier'
op|'*'
number|'10'
op|','
nl|'\n'
string|"'host_other-config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'host_ip_address'"
op|':'
string|"'192.168.1.%d'"
op|'%'
op|'('
number|'100'
op|'+'
name|'multiplier'
op|')'
op|','
nl|'\n'
string|"'host_cpu_info'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'disk_available'"
op|':'
number|'100'
op|'+'
name|'multiplier'
op|'*'
number|'100'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'disk_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'host_uuid'"
op|':'
string|"'xxx-%d'"
op|'%'
name|'multiplier'
op|','
nl|'\n'
string|"'host_name-label'"
op|':'
string|"'xs-%s'"
op|'%'
name|'multiplier'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_zone_manager_service_states
dedent|''
name|'def'
name|'fake_zone_manager_service_states'
op|'('
name|'num_hosts'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'states'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'num_hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'states'
op|'['
string|"'host%02d'"
op|'%'
op|'('
name|'x'
op|'+'
number|'1'
op|')'
op|']'
op|'='
op|'{'
string|"'compute'"
op|':'
name|'_host_caps'
op|'('
name|'x'
op|')'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'states'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeZoneAwareScheduler
dedent|''
name|'class'
name|'FakeZoneAwareScheduler'
op|'('
name|'zone_aware_scheduler'
op|'.'
name|'ZoneAwareScheduler'
op|')'
op|':'
newline|'\n'
DECL|member|filter_hosts
indent|'    '
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'num'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sirp): this is returning [(hostname, services)]'
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|weigh_hosts
dedent|''
name|'def'
name|'weigh_hosts'
op|'('
name|'self'
op|','
name|'num'
op|','
name|'specs'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_weight'
op|'='
number|'99'
newline|'\n'
name|'weighted'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'hostname'
op|','
name|'caps'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'weighted'
op|'.'
name|'append'
op|'('
name|'dict'
op|'('
name|'weight'
op|'='
name|'fake_weight'
op|','
name|'name'
op|'='
name|'hostname'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'weighted'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeZoneManager
dedent|''
dedent|''
name|'class'
name|'FakeZoneManager'
op|'('
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service_states'
op|'='
op|'{'
nl|'\n'
string|"'host1'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'ram'"
op|':'
number|'1000'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'ram'"
op|':'
number|'2000'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host3'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'ram'"
op|':'
number|'3000'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeEmptyZoneManager
dedent|''
dedent|''
name|'class'
name|'FakeEmptyZoneManager'
op|'('
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service_states'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_empty_call_zone_method
dedent|''
dedent|''
name|'def'
name|'fake_empty_call_zone_method'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Hmm, I should probably be using mox for this.'
nl|'\n'
DECL|variable|was_called
dedent|''
name|'was_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_provision_resource
name|'def'
name|'fake_provision_resource'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_ask_child_zone_to_create_instance
dedent|''
name|'def'
name|'fake_ask_child_zone_to_create_instance'
op|'('
name|'context'
op|','
name|'zone_info'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_provision_resource_locally
dedent|''
name|'def'
name|'fake_provision_resource_locally'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_provision_resource_from_blob
dedent|''
name|'def'
name|'fake_provision_resource_from_blob'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_decrypt_blob_returns_local_info
dedent|''
name|'def'
name|'fake_decrypt_blob_returns_local_info'
op|'('
name|'blob'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'foo'"
op|':'
name|'True'
op|'}'
comment|"# values aren't important."
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_decrypt_blob_returns_child_info
dedent|''
name|'def'
name|'fake_decrypt_blob_returns_child_info'
op|'('
name|'blob'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'child_zone'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'child_blob'"
op|':'
name|'True'
op|'}'
comment|"# values aren't important. Keys are."
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_call_zone_method
dedent|''
name|'def'
name|'fake_call_zone_method'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
op|'('
string|"'zone1'"
op|','
op|'['
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'blob'
op|'='
string|"'AAAAAAA'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'111'
op|','
name|'blob'
op|'='
string|"'BBBBBBB'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'112'
op|','
name|'blob'
op|'='
string|"'CCCCCCC'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'113'
op|','
name|'blob'
op|'='
string|"'DDDDDDD'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'zone2'"
op|','
op|'['
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'120'
op|','
name|'blob'
op|'='
string|"'EEEEEEE'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'2'
op|','
name|'blob'
op|'='
string|"'FFFFFFF'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'122'
op|','
name|'blob'
op|'='
string|"'GGGGGGG'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'123'
op|','
name|'blob'
op|'='
string|"'HHHHHHH'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'zone3'"
op|','
op|'['
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'130'
op|','
name|'blob'
op|'='
string|"'IIIIIII'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'131'
op|','
name|'blob'
op|'='
string|"'JJJJJJJ'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'132'
op|','
name|'blob'
op|'='
string|"'KKKKKKK'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'3'
op|','
name|'blob'
op|'='
string|"'LLLLLLL'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneAwareSchedulerTestCase
dedent|''
name|'class'
name|'ZoneAwareSchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Zone Aware Scheduler."""'
newline|'\n'
nl|'\n'
DECL|member|test_zone_aware_scheduler
name|'def'
name|'test_zone_aware_scheduler'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a nested set of FakeZones, ensure that a select call returns the\n        appropriate build plan.\n        """'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_call_zone_method'"
op|','
name|'fake_call_zone_method'
op|')'
newline|'\n'
nl|'\n'
name|'zm'
op|'='
name|'FakeZoneManager'
op|'('
op|')'
newline|'\n'
name|'sched'
op|'.'
name|'set_zone_manager'
op|'('
name|'zm'
op|')'
newline|'\n'
nl|'\n'
name|'fake_context'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'build_plan'
op|'='
name|'sched'
op|'.'
name|'select'
op|'('
name|'fake_context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'15'
op|','
name|'len'
op|'('
name|'build_plan'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'hostnames'
op|'='
op|'['
name|'plan_item'
op|'['
string|"'name'"
op|']'
nl|'\n'
name|'for'
name|'plan_item'
name|'in'
name|'build_plan'
name|'if'
string|"'name'"
name|'in'
name|'plan_item'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'hostnames'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_empty_zone_aware_scheduler
dedent|''
name|'def'
name|'test_empty_zone_aware_scheduler'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure empty hosts & child_zones result in NoValidHosts exception.\n        """'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_call_zone_method'"
op|','
name|'fake_empty_call_zone_method'
op|')'
newline|'\n'
nl|'\n'
name|'zm'
op|'='
name|'FakeEmptyZoneManager'
op|'('
op|')'
newline|'\n'
name|'sched'
op|'.'
name|'set_zone_manager'
op|'('
name|'zm'
op|')'
newline|'\n'
nl|'\n'
name|'fake_context'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'driver'
op|'.'
name|'NoValidHost'
op|','
name|'sched'
op|'.'
name|'schedule_run_instance'
op|','
nl|'\n'
name|'fake_context'
op|','
number|'1'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host_filter'
op|'='
name|'None'
op|','
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_schedule_do_not_schedule_with_hint
dedent|''
name|'def'
name|'test_schedule_do_not_schedule_with_hint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check the local/child zone routing in the run_instance() call.\n        If the zone_blob hint was passed in, don\'t re-schedule.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_provision_resource'"
op|','
name|'fake_provision_resource'
op|')'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'filter_driver'"
op|':'
string|"'nova.scheduler.host_filter.AllHostsFilter'"
op|','
nl|'\n'
string|"'blob'"
op|':'
string|'"Non-None blob data"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'sched'
op|'.'
name|'schedule_run_instance'
op|'('
name|'None'
op|','
number|'1'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'None'
op|','
name|'result'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_local
dedent|''
name|'def'
name|'test_provision_resource_local'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provision a resource locally or remotely."""'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_provision_resource_locally'"
op|','
nl|'\n'
name|'fake_provision_resource_locally'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'hostname'"
op|':'
string|'"foo"'
op|'}'
newline|'\n'
name|'sched'
op|'.'
name|'_provision_resource'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
number|'1'
op|','
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_remote
dedent|''
name|'def'
name|'test_provision_resource_remote'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provision a resource locally or remotely."""'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_provision_resource_from_blob'"
op|','
nl|'\n'
name|'fake_provision_resource_from_blob'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sched'
op|'.'
name|'_provision_resource'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
number|'1'
op|','
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_empty
dedent|''
name|'def'
name|'test_provision_resource_from_blob_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provision a resource locally or remotely given no hints."""'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'zone_aware_scheduler'
op|'.'
name|'InvalidBlob'
op|','
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|','
nl|'\n'
name|'None'
op|','
op|'{'
op|'}'
op|','
number|'1'
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_with_local_blob
dedent|''
name|'def'
name|'test_provision_resource_from_blob_with_local_blob'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Provision a resource locally or remotely when blob hint passed in.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_decrypt_blob'"
op|','
nl|'\n'
name|'fake_decrypt_blob_returns_local_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_provision_resource_locally'"
op|','
nl|'\n'
name|'fake_provision_resource_locally'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'blob'"
op|':'
string|'"Non-None blob data"'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
number|'1'
op|','
nl|'\n'
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_with_child_blob
dedent|''
name|'def'
name|'test_provision_resource_from_blob_with_child_blob'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Provision a resource locally or remotely when child blob hint\n        passed in.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_decrypt_blob'"
op|','
nl|'\n'
name|'fake_decrypt_blob_returns_child_info'
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_ask_child_zone_to_create_instance'"
op|','
nl|'\n'
name|'fake_ask_child_zone_to_create_instance'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'blob'"
op|':'
string|'"Non-None blob data"'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
number|'1'
op|','
nl|'\n'
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_with_immediate_child_blob
dedent|''
name|'def'
name|'test_provision_resource_from_blob_with_immediate_child_blob'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Provision a resource locally or remotely when blob hint passed in\n        from an immediate child.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeZoneAwareScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_ask_child_zone_to_create_instance'"
op|','
nl|'\n'
name|'fake_ask_child_zone_to_create_instance'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'child_blob'"
op|':'
name|'True'
op|','
string|"'child_zone'"
op|':'
name|'True'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
number|'1'
op|','
nl|'\n'
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
