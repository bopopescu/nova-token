begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
string|'"""\nTests For Chance Scheduler.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'chance'
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
name|'tests'
op|'.'
name|'scheduler'
name|'import'
name|'test_scheduler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ChanceSchedulerTestCase
name|'class'
name|'ChanceSchedulerTestCase'
op|'('
name|'test_scheduler'
op|'.'
name|'SchedulerTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Chance Scheduler."""'
newline|'\n'
nl|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'chance'
op|'.'
name|'ChanceScheduler'
newline|'\n'
nl|'\n'
DECL|member|test_filter_hosts_avoid
name|'def'
name|'test_filter_hosts_avoid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test to make sure _filter_hosts() filters original hosts if\n        avoid_original_host is True."""'
newline|'\n'
nl|'\n'
name|'hosts'
op|'='
op|'['
string|"'host1'"
op|','
string|"'host2'"
op|','
string|"'host3'"
op|']'
newline|'\n'
name|'request_spec'
op|'='
name|'dict'
op|'('
name|'instance_properties'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host2'"
op|')'
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
name|'filtered'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_filter_hosts'
op|'('
name|'request_spec'
op|','
name|'hosts'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'filtered'
op|','
op|'['
string|"'host1'"
op|','
string|"'host3'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_hosts_no_avoid
dedent|''
name|'def'
name|'test_filter_hosts_no_avoid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test to make sure _filter_hosts() does not filter original\n        hosts if avoid_original_host is False."""'
newline|'\n'
nl|'\n'
name|'hosts'
op|'='
op|'['
string|"'host1'"
op|','
string|"'host2'"
op|','
string|"'host3'"
op|']'
newline|'\n'
name|'request_spec'
op|'='
name|'dict'
op|'('
name|'instance_properties'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host2'"
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'ignore_hosts'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'filtered'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_filter_hosts'
op|'('
name|'request_spec'
op|','
name|'hosts'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'filtered'
op|','
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_basic_schedule_run_instance
dedent|''
name|'def'
name|'test_basic_schedule_run_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'False'
op|')'
newline|'\n'
name|'ctxt_elevated'
op|'='
string|"'fake-context-elevated'"
newline|'\n'
name|'fake_args'
op|'='
op|'('
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
name|'instance_opts'
op|'='
op|'{'
string|"'fake_opt1'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'num_instances'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
name|'instance_opts'
op|'}'
newline|'\n'
name|'instance1'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid1'"
op|'}'
newline|'\n'
name|'instance2'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid2'"
op|'}'
newline|'\n'
name|'instance1_encoded'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid1'"
op|','
string|"'_is_precooked'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'instance2_encoded'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid2'"
op|','
string|"'_is_precooked'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'reservations'
op|'='
op|'['
string|"'resv1'"
op|','
string|"'resv2'"
op|']'
newline|'\n'
nl|'\n'
comment|"# create_instance_db_entry() usually does this, but we're"
nl|'\n'
comment|'# stubbing it.'
nl|'\n'
DECL|function|_add_uuid1
name|'def'
name|'_add_uuid1'
op|'('
name|'ctxt'
op|','
name|'request_spec'
op|','
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid1'"
newline|'\n'
nl|'\n'
DECL|function|_add_uuid2
dedent|''
name|'def'
name|'_add_uuid2'
op|'('
name|'ctxt'
op|','
name|'request_spec'
op|','
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid2'"
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ctxt'
op|','
string|"'elevated'"
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
name|'driver'
op|','
string|"'hosts_up'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'random'
op|','
string|"'random'"
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
name|'driver'
op|','
string|"'create_instance_db_entry'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'driver'
op|','
string|"'encode_instance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'driver'
op|','
string|"'instance_update_db'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|','
string|"'run_instance'"
op|')'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'.'
name|'elevated'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ctxt_elevated'
op|')'
newline|'\n'
comment|'# instance 1'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'ctxt_elevated'
op|','
string|"'compute'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|"'host1'"
op|','
string|"'host2'"
op|','
string|"'host3'"
op|','
string|"'host4'"
op|']'
op|')'
newline|'\n'
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'.5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_instance_db_entry'
op|'('
name|'ctxt'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'reservations'
op|')'
op|'.'
name|'WithSideEffects'
op|'('
name|'_add_uuid1'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'instance1'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'instance_update_db'
op|'('
name|'ctxt'
op|','
name|'instance1'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'host3'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance1'
op|')'
newline|'\n'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'run_instance'
op|'('
name|'ctxt'
op|','
name|'host'
op|'='
string|"'host3'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance1'
op|','
name|'requested_networks'
op|'='
name|'None'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
name|'is_first_time'
op|'='
name|'None'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'filter_properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance1'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance1_encoded'
op|')'
newline|'\n'
comment|'# instance 2'
nl|'\n'
name|'ctxt'
op|'.'
name|'elevated'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ctxt_elevated'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'ctxt_elevated'
op|','
string|"'compute'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|"'host1'"
op|','
string|"'host2'"
op|','
string|"'host3'"
op|','
string|"'host4'"
op|']'
op|')'
newline|'\n'
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'.2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_instance_db_entry'
op|'('
name|'ctxt'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'reservations'
op|')'
op|'.'
name|'WithSideEffects'
op|'('
name|'_add_uuid2'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'instance2'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'instance_update_db'
op|'('
name|'ctxt'
op|','
name|'instance2'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'host1'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance2'
op|')'
newline|'\n'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'run_instance'
op|'('
name|'ctxt'
op|','
name|'host'
op|'='
string|"'host1'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance2'
op|','
name|'requested_networks'
op|'='
name|'None'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
name|'is_first_time'
op|'='
name|'None'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'filter_properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance2'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance2_encoded'
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
name|'driver'
op|'.'
name|'schedule_run_instance'
op|'('
name|'ctxt'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
op|'{'
op|'}'
op|','
name|'reservations'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'instance1_encoded'
op|','
name|'instance2_encoded'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_scheduler_includes_launch_index
dedent|''
name|'def'
name|'test_scheduler_includes_launch_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'False'
op|')'
newline|'\n'
name|'instance_opts'
op|'='
op|'{'
string|"'fake_opt1'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'num_instances'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
name|'instance_opts'
op|'}'
newline|'\n'
name|'instance1'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid1'"
op|'}'
newline|'\n'
name|'instance2'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid2'"
op|'}'
newline|'\n'
nl|'\n'
comment|"# create_instance_db_entry() usually does this, but we're"
nl|'\n'
comment|'# stubbing it.'
nl|'\n'
DECL|function|_add_uuid
name|'def'
name|'_add_uuid'
op|'('
name|'num'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Return a function that adds the provided uuid number."""'
newline|'\n'
DECL|function|_add_uuid_num
name|'def'
name|'_add_uuid_num'
op|'('
name|'_'
op|','
name|'spec'
op|','
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid%d'"
op|'%'
name|'num'
newline|'\n'
dedent|''
name|'return'
name|'_add_uuid_num'
newline|'\n'
nl|'\n'
DECL|function|_has_launch_index
dedent|''
name|'def'
name|'_has_launch_index'
op|'('
name|'expected_index'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Return a function that verifies the expected index."""'
newline|'\n'
DECL|function|_check_launch_index
name|'def'
name|'_check_launch_index'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
string|"'instance_properties'"
name|'in'
name|'value'
op|':'
newline|'\n'
indent|'                    '
name|'if'
string|"'launch_index'"
name|'in'
name|'value'
op|'['
string|"'instance_properties'"
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'index'
op|'='
name|'value'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'launch_index'"
op|']'
newline|'\n'
name|'if'
name|'index'
op|'=='
name|'expected_index'
op|':'
newline|'\n'
indent|'                            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'_check_launch_index'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'driver'
op|','
string|"'_schedule'"
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
name|'driver'
op|','
string|"'create_instance_db_entry'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'driver'
op|','
string|"'encode_instance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'driver'
op|','
string|"'instance_update_db'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|','
string|"'run_instance'"
op|')'
newline|'\n'
nl|'\n'
comment|'# instance 1'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_schedule'
op|'('
name|'ctxt'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
nl|'\n'
op|'{'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_instance_db_entry'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'mox'
op|'.'
name|'Func'
op|'('
name|'_has_launch_index'
op|'('
number|'0'
op|')'
op|')'
op|','
name|'None'
nl|'\n'
op|')'
op|'.'
name|'WithSideEffects'
op|'('
name|'_add_uuid'
op|'('
number|'1'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance1'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'instance_update_db'
op|'('
name|'ctxt'
op|','
name|'instance1'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance1'
op|')'
newline|'\n'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'run_instance'
op|'('
name|'ctxt'
op|','
name|'host'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance1'
op|','
name|'requested_networks'
op|'='
name|'None'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
name|'is_first_time'
op|'='
name|'None'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'filter_properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance1'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance1'
op|')'
newline|'\n'
comment|'# instance 2'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_schedule'
op|'('
name|'ctxt'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
nl|'\n'
op|'{'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_instance_db_entry'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'mox'
op|'.'
name|'Func'
op|'('
name|'_has_launch_index'
op|'('
number|'1'
op|')'
op|')'
op|','
name|'None'
nl|'\n'
op|')'
op|'.'
name|'WithSideEffects'
op|'('
name|'_add_uuid'
op|'('
number|'2'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance2'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'instance_update_db'
op|'('
name|'ctxt'
op|','
name|'instance2'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance2'
op|')'
newline|'\n'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'run_instance'
op|'('
name|'ctxt'
op|','
name|'host'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance2'
op|','
name|'requested_networks'
op|'='
name|'None'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
name|'is_first_time'
op|'='
name|'None'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'filter_properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance2'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance2'
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
name|'driver'
op|'.'
name|'schedule_run_instance'
op|'('
name|'ctxt'
op|','
name|'request_spec'
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
op|'{'
op|'}'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_basic_schedule_run_instance_no_hosts
dedent|''
name|'def'
name|'test_basic_schedule_run_instance_no_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'False'
op|')'
newline|'\n'
name|'ctxt_elevated'
op|'='
string|"'fake-context-elevated'"
newline|'\n'
name|'fake_args'
op|'='
op|'('
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
name|'instance_opts'
op|'='
string|"'fake_instance_opts'"
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'num_instances'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
name|'instance_opts'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ctxt'
op|','
string|"'elevated'"
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
name|'driver'
op|','
string|"'hosts_up'"
op|')'
newline|'\n'
nl|'\n'
comment|'# instance 1'
nl|'\n'
name|'ctxt'
op|'.'
name|'elevated'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ctxt_elevated'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'ctxt_elevated'
op|','
string|"'compute'"
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
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
name|'schedule_run_instance'
op|','
name|'ctxt'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
op|'{'
op|'}'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_basic_schedule_fallback
dedent|''
name|'def'
name|'test_basic_schedule_fallback'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'False'
op|')'
newline|'\n'
name|'ctxt_elevated'
op|'='
string|"'fake-context-elevated'"
newline|'\n'
name|'topic'
op|'='
string|"'fake_topic'"
newline|'\n'
name|'method'
op|'='
string|"'fake_method'"
newline|'\n'
name|'fake_args'
op|'='
op|'('
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
name|'fake_kwargs'
op|'='
op|'{'
string|"'fake_kwarg1'"
op|':'
string|"'fake_value1'"
op|','
nl|'\n'
string|"'fake_kwarg2'"
op|':'
string|"'fake_value2'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ctxt'
op|','
string|"'elevated'"
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
name|'driver'
op|','
string|"'hosts_up'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'random'
op|','
string|"'random'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'driver'
op|','
string|"'cast_to_host'"
op|')'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'.'
name|'elevated'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ctxt_elevated'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'ctxt_elevated'
op|','
name|'topic'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|"'host1'"
op|','
string|"'host2'"
op|','
string|"'host3'"
op|','
string|"'host4'"
op|']'
op|')'
newline|'\n'
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'.5'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'cast_to_host'
op|'('
name|'ctxt'
op|','
name|'topic'
op|','
string|"'host3'"
op|','
name|'method'
op|','
op|'**'
name|'fake_kwargs'
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
name|'driver'
op|'.'
name|'schedule'
op|'('
name|'ctxt'
op|','
name|'topic'
op|','
name|'method'
op|','
op|'*'
name|'fake_args'
op|','
op|'**'
name|'fake_kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_basic_schedule_fallback_no_hosts
dedent|''
name|'def'
name|'test_basic_schedule_fallback_no_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'False'
op|')'
newline|'\n'
name|'ctxt_elevated'
op|'='
string|"'fake-context-elevated'"
newline|'\n'
name|'topic'
op|'='
string|"'fake_topic'"
newline|'\n'
name|'method'
op|'='
string|"'fake_method'"
newline|'\n'
name|'fake_args'
op|'='
op|'('
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
name|'fake_kwargs'
op|'='
op|'{'
string|"'fake_kwarg1'"
op|':'
string|"'fake_value1'"
op|','
nl|'\n'
string|"'fake_kwarg2'"
op|':'
string|"'fake_value2'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ctxt'
op|','
string|"'elevated'"
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
name|'driver'
op|','
string|"'hosts_up'"
op|')'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'.'
name|'elevated'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'ctxt_elevated'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'ctxt_elevated'
op|','
name|'topic'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
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
name|'schedule'
op|','
name|'ctxt'
op|','
name|'topic'
op|','
name|'method'
op|','
nl|'\n'
op|'*'
name|'fake_args'
op|','
op|'**'
name|'fake_kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
