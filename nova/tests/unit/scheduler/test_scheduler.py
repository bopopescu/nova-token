begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nTests For Scheduler\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
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
name|'objects'
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
name|'manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'servicegroup'
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
name|'unit'
name|'import'
name|'fake_server_actions'
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
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerManagerTestCase
name|'class'
name|'SchedulerManagerTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for scheduler manager."""'
newline|'\n'
nl|'\n'
DECL|variable|manager_cls
name|'manager_cls'
op|'='
name|'manager'
op|'.'
name|'SchedulerManager'
newline|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'fakes'
op|'.'
name|'FakeScheduler'
newline|'\n'
DECL|variable|driver_cls_name
name|'driver_cls_name'
op|'='
string|"'nova.tests.unit.scheduler.fakes.FakeScheduler'"
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|','
string|"'_init_instance_info'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|','
string|"'_init_aggregates'"
op|')'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|','
name|'mock_init_agg'
op|','
name|'mock_init_inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'SchedulerManagerTestCase'
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
name|'scheduler_driver'
op|'='
name|'self'
op|'.'
name|'driver_cls_name'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|','
string|"'_init_aggregates'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'='
name|'self'
op|'.'
name|'manager_cls'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
string|"'fake_topic'"
newline|'\n'
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'fake_kwargs'
op|'='
op|'{'
string|"'cat'"
op|':'
string|"'meow'"
op|','
string|"'dog'"
op|':'
string|"'woof'"
op|'}'
newline|'\n'
name|'fake_server_actions'
op|'.'
name|'stub_out_action_events'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_1_correct_init
dedent|''
name|'def'
name|'test_1_correct_init'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Correct scheduler driver'
nl|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'manager'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'manager'
op|'.'
name|'driver'
op|','
name|'self'
op|'.'
name|'driver_cls'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_select_destination
dedent|''
name|'def'
name|'test_select_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_spec'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'driver'
op|','
string|"'select_destinations'"
nl|'\n'
op|')'
name|'as'
name|'select_destinations'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'select_destinations'
op|'('
name|'None'
op|','
name|'spec_obj'
op|'='
name|'fake_spec'
op|')'
newline|'\n'
name|'select_destinations'
op|'.'
name|'assert_called_once_with'
op|'('
name|'None'
op|','
name|'fake_spec'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(sbauza): Remove that test once the API v4 is removed'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'RequestSpec'
op|','
string|"'from_primitives'"
op|')'
newline|'\n'
DECL|member|test_select_destination_with_old_client
name|'def'
name|'test_select_destination_with_old_client'
op|'('
name|'self'
op|','
name|'from_primitives'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_spec'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
op|')'
newline|'\n'
name|'from_primitives'
op|'.'
name|'return_value'
op|'='
name|'fake_spec'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'driver'
op|','
string|"'select_destinations'"
nl|'\n'
op|')'
name|'as'
name|'select_destinations'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'select_destinations'
op|'('
name|'None'
op|','
name|'request_spec'
op|'='
string|"'fake_spec'"
op|','
nl|'\n'
name|'filter_properties'
op|'='
string|"'fake_props'"
op|')'
newline|'\n'
name|'select_destinations'
op|'.'
name|'assert_called_once_with'
op|'('
name|'None'
op|','
name|'fake_spec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_aggregates
dedent|''
dedent|''
name|'def'
name|'test_update_aggregates'
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
name|'manager'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
nl|'\n'
string|"'update_aggregates'"
nl|'\n'
op|')'
name|'as'
name|'update_aggregates'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'update_aggregates'
op|'('
name|'None'
op|','
name|'aggregates'
op|'='
string|"'agg'"
op|')'
newline|'\n'
name|'update_aggregates'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'agg'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_aggregate
dedent|''
dedent|''
name|'def'
name|'test_delete_aggregate'
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
name|'manager'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
nl|'\n'
string|"'delete_aggregate'"
nl|'\n'
op|')'
name|'as'
name|'delete_aggregate'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_aggregate'
op|'('
name|'None'
op|','
name|'aggregate'
op|'='
string|"'agg'"
op|')'
newline|'\n'
name|'delete_aggregate'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'agg'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_instance_info
dedent|''
dedent|''
name|'def'
name|'test_update_instance_info'
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
name|'manager'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
nl|'\n'
string|"'update_instance_info'"
op|')'
name|'as'
name|'mock_update'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'update_instance_info'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'host_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_info'
op|')'
newline|'\n'
name|'mock_update'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'host_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_instance_info
dedent|''
dedent|''
name|'def'
name|'test_delete_instance_info'
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
name|'manager'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
nl|'\n'
string|"'delete_instance_info'"
op|')'
name|'as'
name|'mock_delete'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_instance_info'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'host_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'mock_delete'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'host_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_sync_instance_info
dedent|''
dedent|''
name|'def'
name|'test_sync_instance_info'
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
name|'manager'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
nl|'\n'
string|"'sync_instance_info'"
op|')'
name|'as'
name|'mock_sync'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'sync_instance_info'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'host_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuids'
op|')'
newline|'\n'
name|'mock_sync'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'host_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuids'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'SchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for base scheduler driver class."""'
newline|'\n'
nl|'\n'
comment|'# So we can subclass this test and re-use tests if we need.'
nl|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'fakes'
op|'.'
name|'FakeScheduler'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|','
string|"'_init_instance_info'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|','
string|"'_init_aggregates'"
op|')'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|','
name|'mock_init_agg'
op|','
name|'mock_init_inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'SchedulerTestCase'
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
name|'driver'
op|'='
name|'self'
op|'.'
name|'driver_cls'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
string|"'fake_topic'"
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hosts_up
dedent|''
name|'def'
name|'test_hosts_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service1'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
string|"'host1'"
op|')'
newline|'\n'
name|'service2'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
string|"'host2'"
op|')'
newline|'\n'
name|'services'
op|'='
name|'objects'
op|'.'
name|'ServiceList'
op|'('
name|'objects'
op|'='
op|'['
name|'service1'
op|','
name|'service2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'objects'
op|'.'
name|'ServiceList'
op|','
string|"'get_by_topic'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'servicegroup'
op|'.'
name|'API'
op|','
string|"'service_is_up'"
op|')'
newline|'\n'
nl|'\n'
name|'objects'
op|'.'
name|'ServiceList'
op|'.'
name|'get_by_topic'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service1'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service2'
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'topic'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
op|'['
string|"'host2'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
