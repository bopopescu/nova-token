begin_unit
comment|'# Copyright (c) 2013 Rackspace Hosting'
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
string|'"""\nTests For Scheduler Utils\n"""'
newline|'\n'
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'mox3'
name|'import'
name|'mox'
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
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
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
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'utils'
name|'as'
name|'scheduler_utils'
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
name|'fake_instance'
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
DECL|class|SchedulerUtilsTestCase
name|'class'
name|'SchedulerUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for scheduler utils methods."""'
newline|'\n'
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
name|'SchedulerUtilsTestCase'
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
name|'context'
op|'='
string|"'fake-context'"
newline|'\n'
nl|'\n'
DECL|member|test_build_request_spec_without_image
dedent|''
name|'def'
name|'test_build_request_spec_without_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'None'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid'"
op|'}'
newline|'\n'
name|'instance_type'
op|'='
op|'{'
string|"'flavorid'"
op|':'
string|"'fake-id'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'flavors'
op|','
string|"'extract_flavor'"
op|')'
newline|'\n'
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance_type'
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
name|'request_spec'
op|'='
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image'
op|','
nl|'\n'
op|'['
name|'instance'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'request_spec'
op|'['
string|"'image'"
op|']'
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
name|'flavors'
op|','
string|"'extract_flavor'"
op|')'
newline|'\n'
DECL|member|test_build_request_spec_with_object
name|'def'
name|'test_build_request_spec_with_object'
op|'('
name|'self'
op|','
name|'extract_flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
op|'{'
string|"'flavorid'"
op|':'
string|"'fake-id'"
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'extract_flavor'
op|'.'
name|'return_value'
op|'='
name|'instance_type'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'None'
op|','
nl|'\n'
op|'['
name|'instance'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|','
name|'dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_set_vm_state_and_notify
dedent|''
name|'def'
name|'_test_set_vm_state_and_notify'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'expected_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'dict'
op|'('
name|'vm_state'
op|'='
string|"'fake-vm-state'"
op|')'
newline|'\n'
name|'service'
op|'='
string|"'fake-service'"
newline|'\n'
name|'method'
op|'='
string|"'fake-method'"
newline|'\n'
name|'exc_info'
op|'='
string|"'exc_info'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_utils'
op|','
nl|'\n'
string|"'add_instance_fault_from_exc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'notifications'
op|','
string|"'send_update'"
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
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpc'
op|','
string|"'get_notifier'"
op|')'
newline|'\n'
name|'notifier'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
name|'service'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'notifier'
op|')'
newline|'\n'
nl|'\n'
name|'old_ref'
op|'='
string|"'old_ref'"
newline|'\n'
name|'new_ref'
op|'='
string|"'new_ref'"
newline|'\n'
name|'inst_obj'
op|'='
string|"'inst_obj'"
newline|'\n'
nl|'\n'
name|'for'
name|'_uuid'
name|'in'
name|'expected_uuids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'_uuid'
op|','
name|'updates'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'system_metadata'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'('
name|'old_ref'
op|','
name|'new_ref'
op|')'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'old_ref'
op|','
name|'inst_obj'
op|','
nl|'\n'
name|'service'
op|'='
name|'service'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'add_instance_fault_from_exc'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'new_ref'
op|','
name|'exc_info'
op|','
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'tuple'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'payload'
op|'='
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'instance_properties'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
nl|'\n'
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'_uuid'
op|','
nl|'\n'
name|'state'
op|'='
string|"'fake-vm-state'"
op|','
nl|'\n'
name|'method'
op|'='
name|'method'
op|','
nl|'\n'
name|'reason'
op|'='
name|'exc_info'
op|')'
newline|'\n'
name|'event_type'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'service'
op|','
name|'method'
op|')'
newline|'\n'
name|'notifier'
op|'.'
name|'error'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'event_type'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'Instance'
op|','
string|"'_from_db_object'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'inst_obj'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'scheduler_utils'
op|'.'
name|'set_vm_state_and_notify'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'service'
op|','
nl|'\n'
name|'method'
op|','
nl|'\n'
name|'updates'
op|','
nl|'\n'
name|'exc_info'
op|','
nl|'\n'
name|'request_spec'
op|','
nl|'\n'
name|'db'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_vm_state_and_notify_rs_uuids
dedent|''
dedent|''
name|'def'
name|'test_set_vm_state_and_notify_rs_uuids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_uuids'
op|'='
op|'['
string|"'1'"
op|','
string|"'2'"
op|','
string|"'3'"
op|']'
newline|'\n'
name|'request_spec'
op|'='
name|'dict'
op|'('
name|'instance_uuids'
op|'='
name|'expected_uuids'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_set_vm_state_and_notify'
op|'('
name|'request_spec'
op|','
name|'expected_uuids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_vm_state_and_notify_uuid_from_instance_props
dedent|''
name|'def'
name|'test_set_vm_state_and_notify_uuid_from_instance_props'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_uuids'
op|'='
op|'['
string|"'fake-uuid'"
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
name|'uuid'
op|'='
string|"'fake-uuid'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_set_vm_state_and_notify'
op|'('
name|'request_spec'
op|','
name|'expected_uuids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_populate_filter_props
dedent|''
name|'def'
name|'_test_populate_filter_props'
op|'('
name|'self'
op|','
name|'host_state_obj'
op|'='
name|'True'
op|','
nl|'\n'
name|'with_retry'
op|'='
name|'True'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'force_hosts'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'force_hosts'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
name|'force_nodes'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'force_nodes'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
name|'with_retry'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'force_hosts'
name|'and'
name|'not'
name|'force_nodes'
op|':'
newline|'\n'
indent|'                '
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'retry'
op|'='
name|'dict'
op|'('
name|'hosts'
op|'='
op|'['
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'force_hosts'
op|'='
name|'force_hosts'
op|','
nl|'\n'
name|'force_nodes'
op|'='
name|'force_nodes'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'filter_properties'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'host_state_obj'
op|':'
newline|'\n'
DECL|class|host_state
indent|'            '
name|'class'
name|'host_state'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|host
indent|'                '
name|'host'
op|'='
string|"'fake-host'"
newline|'\n'
DECL|variable|nodename
name|'nodename'
op|'='
string|"'fake-node'"
newline|'\n'
DECL|variable|limits
name|'limits'
op|'='
string|"'fake-limits'"
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'host_state'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'fake-host'"
op|','
nl|'\n'
DECL|variable|nodename
name|'nodename'
op|'='
string|"'fake-node'"
op|','
nl|'\n'
DECL|variable|limits
name|'limits'
op|'='
string|"'fake-limits'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'scheduler_utils'
op|'.'
name|'populate_filter_properties'
op|'('
name|'filter_properties'
op|','
nl|'\n'
name|'host_state'
op|')'
newline|'\n'
name|'if'
name|'with_retry'
name|'and'
name|'not'
name|'force_hosts'
name|'and'
name|'not'
name|'force_nodes'
op|':'
newline|'\n'
comment|'# So we can check for 2 hosts'
nl|'\n'
indent|'            '
name|'scheduler_utils'
op|'.'
name|'populate_filter_properties'
op|'('
name|'filter_properties'
op|','
nl|'\n'
name|'host_state'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'force_hosts'
op|':'
newline|'\n'
indent|'            '
name|'expected_limits'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'expected_limits'
op|'='
string|"'fake-limits'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_limits'
op|','
nl|'\n'
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'limits'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'with_retry'
name|'and'
name|'not'
name|'force_hosts'
name|'and'
name|'not'
name|'force_nodes'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'['
string|"'fake-host'"
op|','
string|"'fake-node'"
op|']'
op|','
nl|'\n'
op|'['
string|"'fake-host'"
op|','
string|"'fake-node'"
op|']'
op|']'
op|','
nl|'\n'
name|'filter_properties'
op|'['
string|"'retry'"
op|']'
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'retry'"
op|','
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_populate_filter_props
dedent|''
dedent|''
name|'def'
name|'test_populate_filter_props'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_populate_filter_props'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_populate_filter_props_host_dict
dedent|''
name|'def'
name|'test_populate_filter_props_host_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_populate_filter_props'
op|'('
name|'host_state_obj'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_populate_filter_props_no_retry
dedent|''
name|'def'
name|'test_populate_filter_props_no_retry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_populate_filter_props'
op|'('
name|'with_retry'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_populate_filter_props_force_hosts_no_retry
dedent|''
name|'def'
name|'test_populate_filter_props_force_hosts_no_retry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_populate_filter_props'
op|'('
name|'force_hosts'
op|'='
op|'['
string|"'force-host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_populate_filter_props_force_nodes_no_retry
dedent|''
name|'def'
name|'test_populate_filter_props_force_nodes_no_retry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_populate_filter_props'
op|'('
name|'force_nodes'
op|'='
op|'['
string|"'force-node'"
op|']'
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
name|'scheduler_utils'
op|','
string|"'_max_attempts'"
op|')'
newline|'\n'
DECL|member|test_populate_retry_exception_at_max_attempts
name|'def'
name|'test_populate_retry_exception_at_max_attempts'
op|'('
name|'self'
op|','
name|'_max_attempts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_max_attempts'
op|'.'
name|'return_value'
op|'='
number|'2'
newline|'\n'
name|'msg'
op|'='
string|"'The exception text was preserved!'"
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'retry'
op|'='
name|'dict'
op|'('
name|'num_attempts'
op|'='
number|'2'
op|','
name|'hosts'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'exc'
op|'='
op|'['
name|'msg'
op|']'
op|')'
op|')'
newline|'\n'
name|'nvh'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'populate_retry'
op|','
nl|'\n'
name|'filter_properties'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
comment|"# make sure 'msg' is a substring of the complete exception text"
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'msg'
op|','
name|'nvh'
op|'.'
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_parse_options
dedent|''
name|'def'
name|'_check_parse_options'
op|'('
name|'self'
op|','
name|'opts'
op|','
name|'sep'
op|','
name|'converter'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'good'
op|'='
name|'scheduler_utils'
op|'.'
name|'parse_options'
op|'('
name|'opts'
op|','
nl|'\n'
name|'sep'
op|'='
name|'sep'
op|','
nl|'\n'
name|'converter'
op|'='
name|'converter'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'expected'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'item'
op|','
name|'good'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parse_options
dedent|''
dedent|''
name|'def'
name|'test_parse_options'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# check normal'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_parse_options'
op|'('
op|'['
string|"'foo=1'"
op|','
string|"'bar=-2.1'"
op|']'
op|','
nl|'\n'
string|"'='"
op|','
nl|'\n'
name|'float'
op|','
nl|'\n'
op|'['
op|'('
string|"'foo'"
op|','
number|'1.0'
op|')'
op|','
op|'('
string|"'bar'"
op|','
op|'-'
number|'2.1'
op|')'
op|']'
op|')'
newline|'\n'
comment|'# check convert error'
nl|'\n'
name|'self'
op|'.'
name|'_check_parse_options'
op|'('
op|'['
string|"'foo=a1'"
op|','
string|"'bar=-2.1'"
op|']'
op|','
nl|'\n'
string|"'='"
op|','
nl|'\n'
name|'float'
op|','
nl|'\n'
op|'['
op|'('
string|"'bar'"
op|','
op|'-'
number|'2.1'
op|')'
op|']'
op|')'
newline|'\n'
comment|'# check separator missing'
nl|'\n'
name|'self'
op|'.'
name|'_check_parse_options'
op|'('
op|'['
string|"'foo'"
op|','
string|"'bar=-2.1'"
op|']'
op|','
nl|'\n'
string|"'='"
op|','
nl|'\n'
name|'float'
op|','
nl|'\n'
op|'['
op|'('
string|"'bar'"
op|','
op|'-'
number|'2.1'
op|')'
op|']'
op|')'
newline|'\n'
comment|'# check key missing'
nl|'\n'
name|'self'
op|'.'
name|'_check_parse_options'
op|'('
op|'['
string|"'=5'"
op|','
string|"'bar=-2.1'"
op|']'
op|','
nl|'\n'
string|"'='"
op|','
nl|'\n'
name|'float'
op|','
nl|'\n'
op|'['
op|'('
string|"'bar'"
op|','
op|'-'
number|'2.1'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_filters_configured
dedent|''
name|'def'
name|'test_validate_filters_configured'
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
string|"'FakeFilter1,FakeFilter2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'scheduler_utils'
op|'.'
name|'validate_filter'
op|'('
string|"'FakeFilter1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'scheduler_utils'
op|'.'
name|'validate_filter'
op|'('
string|"'FakeFilter2'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'scheduler_utils'
op|'.'
name|'validate_filter'
op|'('
string|"'FakeFilter3'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_server_group
dedent|''
name|'def'
name|'_create_server_group'
op|'('
name|'self'
op|','
name|'policy'
op|'='
string|"'anti-affinity'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'params'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'hostA'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'group'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'name'
op|'='
string|"'pele'"
newline|'\n'
name|'group'
op|'.'
name|'uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'group'
op|'.'
name|'members'
op|'='
op|'['
name|'instance'
op|'.'
name|'uuid'
op|']'
newline|'\n'
name|'group'
op|'.'
name|'policies'
op|'='
op|'['
name|'policy'
op|']'
newline|'\n'
name|'return'
name|'group'
newline|'\n'
nl|'\n'
DECL|member|_get_group_details
dedent|''
name|'def'
name|'_get_group_details'
op|'('
name|'self'
op|','
name|'group'
op|','
name|'policy'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group_hosts'
op|'='
op|'['
string|"'hostB'"
op|']'
newline|'\n'
nl|'\n'
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
name|'objects'
op|'.'
name|'InstanceGroup'
op|','
string|"'get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'group'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'InstanceGroup'
op|','
string|"'get_hosts'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'['
string|"'hostA'"
op|']'
op|')'
op|','
nl|'\n'
op|')'
name|'as'
op|'('
name|'get_group'
op|','
name|'get_hosts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_ANTI_AFFINITY'
op|'='
name|'None'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_AFFINITY'
op|'='
name|'None'
newline|'\n'
name|'group_info'
op|'='
name|'scheduler_utils'
op|'.'
name|'_get_group_details'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake_uuid'"
op|']'
op|','
name|'group_hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
op|'('
name|'set'
op|'('
op|'['
string|"'hostA'"
op|','
string|"'hostB'"
op|']'
op|')'
op|','
op|'['
name|'policy'
op|']'
op|')'
op|','
nl|'\n'
name|'group_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_group_details
dedent|''
dedent|''
name|'def'
name|'test_get_group_details'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'policy'
name|'in'
op|'['
string|"'affinity'"
op|','
string|"'anti-affinity'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'='
name|'self'
op|'.'
name|'_create_server_group'
op|'('
name|'policy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_get_group_details'
op|'('
name|'group'
op|','
name|'policy'
op|'='
name|'policy'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_group_details_with_no_affinity_filters
dedent|''
dedent|''
name|'def'
name|'test_get_group_details_with_no_affinity_filters'
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
string|"'fake'"
op|']'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_ANTI_AFFINITY'
op|'='
name|'None'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_AFFINITY'
op|'='
name|'None'
newline|'\n'
name|'group_info'
op|'='
name|'scheduler_utils'
op|'.'
name|'_get_group_details'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'['
string|"'fake-uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'group_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_group_details_with_no_instance_uuids
dedent|''
name|'def'
name|'test_get_group_details_with_no_instance_uuids'
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
string|"'fake'"
op|']'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_ANTI_AFFINITY'
op|'='
name|'None'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_AFFINITY'
op|'='
name|'None'
newline|'\n'
name|'group_info'
op|'='
name|'scheduler_utils'
op|'.'
name|'_get_group_details'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'group_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_group_details_with_filter_not_configured
dedent|''
name|'def'
name|'_get_group_details_with_filter_not_configured'
op|'('
name|'self'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'wrong_filter'
op|'='
op|'{'
nl|'\n'
string|"'affinity'"
op|':'
string|"'ServerGroupAntiAffinityFilter'"
op|','
nl|'\n'
string|"'anti-affinity'"
op|':'
string|"'ServerGroupAffinityFilter'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_default_filters'
op|'='
op|'['
name|'wrong_filter'
op|'['
name|'policy'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'params'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'hostA'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'group'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'group'
op|'.'
name|'members'
op|'='
op|'['
name|'instance'
op|'.'
name|'uuid'
op|']'
newline|'\n'
name|'group'
op|'.'
name|'policies'
op|'='
op|'['
name|'policy'
op|']'
newline|'\n'
nl|'\n'
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
name|'objects'
op|'.'
name|'InstanceGroup'
op|','
string|"'get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'group'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'InstanceGroup'
op|','
string|"'get_hosts'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'['
string|"'hostA'"
op|']'
op|')'
op|','
nl|'\n'
op|')'
name|'as'
op|'('
name|'get_group'
op|','
name|'get_hosts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_ANTI_AFFINITY'
op|'='
name|'None'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'_SUPPORTS_AFFINITY'
op|'='
name|'None'
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
name|'scheduler_utils'
op|'.'
name|'_get_group_details'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_group_details_with_filter_not_configured
dedent|''
dedent|''
name|'def'
name|'test_get_group_details_with_filter_not_configured'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'policies'
op|'='
op|'['
string|"'anti-affinity'"
op|','
string|"'affinity'"
op|']'
newline|'\n'
name|'for'
name|'policy'
name|'in'
name|'policies'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_get_group_details_with_filter_not_configured'
op|'('
name|'policy'
op|')'
newline|'\n'
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
name|'scheduler_utils'
op|','
string|"'_get_group_details'"
op|')'
newline|'\n'
DECL|member|test_setup_instance_group_in_filter_properties
name|'def'
name|'test_setup_instance_group_in_filter_properties'
op|'('
name|'self'
op|','
name|'mock_ggd'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_ggd'
op|'.'
name|'return_value'
op|'='
name|'scheduler_utils'
op|'.'
name|'GroupDetails'
op|'('
nl|'\n'
name|'hosts'
op|'='
name|'set'
op|'('
op|'['
string|"'hostA'"
op|','
string|"'hostB'"
op|']'
op|')'
op|','
name|'policies'
op|'='
op|'['
string|"'policy'"
op|']'
op|')'
newline|'\n'
name|'spec'
op|'='
op|'{'
string|"'instance_uuids'"
op|':'
op|'['
string|"'fake-uuid'"
op|']'
op|'}'
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'group_hosts'"
op|':'
op|'['
string|"'hostC'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'setup_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec'
op|','
name|'filter_props'
op|')'
newline|'\n'
nl|'\n'
name|'mock_ggd'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
op|','
nl|'\n'
op|'['
string|"'hostC'"
op|']'
op|')'
newline|'\n'
name|'expected_filter_props'
op|'='
op|'{'
string|"'group_updated'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'group_hosts'"
op|':'
name|'set'
op|'('
op|'['
string|"'hostA'"
op|','
string|"'hostB'"
op|']'
op|')'
op|','
nl|'\n'
string|"'group_policies'"
op|':'
op|'['
string|"'policy'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_filter_props'
op|','
name|'filter_props'
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
name|'scheduler_utils'
op|','
string|"'_get_group_details'"
op|')'
newline|'\n'
DECL|member|test_setup_instance_group_with_no_group
name|'def'
name|'test_setup_instance_group_with_no_group'
op|'('
name|'self'
op|','
name|'mock_ggd'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_ggd'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
name|'spec'
op|'='
op|'{'
string|"'instance_uuids'"
op|':'
op|'['
string|"'fake-uuid'"
op|']'
op|'}'
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'group_hosts'"
op|':'
op|'['
string|"'hostC'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'setup_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec'
op|','
name|'filter_props'
op|')'
newline|'\n'
nl|'\n'
name|'mock_ggd'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
op|','
nl|'\n'
op|'['
string|"'hostC'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'group_updated'"
op|','
name|'filter_props'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'group_policies'"
op|','
name|'filter_props'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'hostC'"
op|']'
op|','
name|'filter_props'
op|'['
string|"'group_hosts'"
op|']'
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
name|'scheduler_utils'
op|','
string|"'_get_group_details'"
op|')'
newline|'\n'
DECL|member|test_setup_instance_group_with_filter_not_configured
name|'def'
name|'test_setup_instance_group_with_filter_not_configured'
op|'('
name|'self'
op|','
name|'mock_ggd'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_ggd'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|"'whatever'"
op|')'
newline|'\n'
name|'spec'
op|'='
op|'{'
string|"'instance_uuids'"
op|':'
op|'['
string|"'fake-uuid'"
op|']'
op|'}'
newline|'\n'
name|'filter_props'
op|'='
op|'{'
string|"'group_hosts'"
op|':'
op|'['
string|"'hostC'"
op|']'
op|'}'
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
name|'scheduler_utils'
op|'.'
name|'setup_instance_group'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'spec'
op|','
name|'filter_props'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
