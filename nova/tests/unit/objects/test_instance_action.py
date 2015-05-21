begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'traceback'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance_action'
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
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|NOW
name|'NOW'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
name|'microsecond'
op|'='
number|'0'
op|')'
newline|'\n'
DECL|variable|fake_action
name|'fake_action'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'action'"
op|':'
string|"'fake-action'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
string|"'fake-request'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake-user'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake-project'"
op|','
nl|'\n'
string|"'start_time'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'finish_time'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'foo'"
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|fake_event
name|'fake_event'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'event'"
op|':'
string|"'fake-event'"
op|','
nl|'\n'
string|"'action_id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'start_time'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'finish_time'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'result'"
op|':'
string|"'fake-result'"
op|','
nl|'\n'
string|"'traceback'"
op|':'
string|"'fake-tb'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceActionObject
name|'class'
name|'_TestInstanceActionObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'action_get_by_request_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_request_id
name|'def'
name|'test_get_by_request_id'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'fake_action'
newline|'\n'
name|'action'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'get_by_request_id'
op|'('
nl|'\n'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-request'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'action'
op|','
name|'fake_action'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
nl|'\n'
string|"'fake-uuid'"
op|','
string|"'fake-request'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pack_action_start
dedent|''
name|'def'
name|'test_pack_action_start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'pack_action_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'request_id'"
op|']'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'request_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'user_id'"
op|']'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'project_id'"
op|']'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'instance_uuid'"
op|']'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'action'"
op|']'
op|','
string|"'fake-action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'start_time'"
op|']'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'timestamp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pack_action_finish
dedent|''
name|'def'
name|'test_pack_action_finish'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'values'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'pack_action_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'request_id'"
op|']'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'request_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'instance_uuid'"
op|']'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'values'
op|'['
string|"'finish_time'"
op|']'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
op|','
name|'NOW'
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
name|'db'
op|','
string|"'action_start'"
op|')'
newline|'\n'
DECL|member|test_action_start
name|'def'
name|'test_action_start'
op|'('
name|'self'
op|','
name|'mock_start'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-action'"
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'return_value'
op|'='
name|'fake_action'
newline|'\n'
name|'action'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'action_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-action'"
op|','
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'action'
op|','
name|'fake_action'
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
name|'db'
op|','
string|"'action_start'"
op|')'
newline|'\n'
DECL|member|test_action_start_no_result
name|'def'
name|'test_action_start_no_result'
op|'('
name|'self'
op|','
name|'mock_start'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-action'"
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'return_value'
op|'='
name|'fake_action'
newline|'\n'
name|'action'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'action_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-action'"
op|','
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'action'
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
name|'db'
op|','
string|"'action_finish'"
op|')'
newline|'\n'
DECL|member|test_action_finish
name|'def'
name|'test_action_finish'
op|'('
name|'self'
op|','
name|'mock_finish'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_action'
newline|'\n'
name|'action'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'action_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'action'
op|','
name|'fake_action'
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
name|'db'
op|','
string|"'action_finish'"
op|')'
newline|'\n'
DECL|member|test_action_finish_no_result
name|'def'
name|'test_action_finish_no_result'
op|'('
name|'self'
op|','
name|'mock_finish'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_action'
newline|'\n'
name|'action'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'action_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'action'
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
name|'db'
op|','
string|"'action_finish'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'action_start'"
op|')'
newline|'\n'
DECL|member|test_finish
name|'def'
name|'test_finish'
op|'('
name|'self'
op|','
name|'mock_start'
op|','
name|'mock_finish'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'expected_packed_action_start'
op|'='
op|'{'
nl|'\n'
string|"'request_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'action'"
op|':'
string|"'fake-action'"
op|','
nl|'\n'
string|"'start_time'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'timestamp'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'expected_packed_action_finish'
op|'='
op|'{'
nl|'\n'
string|"'request_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'finish_time'"
op|':'
name|'NOW'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'mock_start'
op|'.'
name|'return_value'
op|'='
name|'fake_action'
newline|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_action'
newline|'\n'
name|'action'
op|'='
name|'instance_action'
op|'.'
name|'InstanceAction'
op|'.'
name|'action_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-action'"
op|')'
newline|'\n'
name|'action'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_action_start'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_action_finish'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'action'
op|','
name|'fake_action'
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
name|'db'
op|','
string|"'actions_get'"
op|')'
newline|'\n'
DECL|member|test_get_list
name|'def'
name|'test_get_list'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_actions'
op|'='
op|'['
name|'dict'
op|'('
name|'fake_action'
op|','
name|'id'
op|'='
number|'1234'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'fake_action'
op|','
name|'id'
op|'='
number|'5678'
op|')'
op|']'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'fake_actions'
newline|'\n'
name|'obj_list'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionList'
op|'.'
name|'get_by_instance_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'action'
name|'in'
name|'enumerate'
op|'('
name|'obj_list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'action'
op|','
name|'fake_actions'
op|'['
name|'index'
op|']'
op|')'
newline|'\n'
dedent|''
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceActionObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceActionObject
name|'_TestInstanceActionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteInstanceActionObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceActionObject
name|'_TestInstanceActionObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceActionEventObject
dedent|''
name|'class'
name|'_TestInstanceActionEventObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'action_event_get_by_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_id
name|'def'
name|'test_get_by_id'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'get_by_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-action-id'"
op|','
string|"'fake-event-id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'event'
op|','
name|'fake_event'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'fake-action-id'"
op|','
string|"'fake-event-id'"
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
name|'db'
op|','
string|"'action_event_start'"
op|')'
newline|'\n'
DECL|member|test_event_start
name|'def'
name|'test_event_start'
op|'('
name|'self'
op|','
name|'mock_start'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'event_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'event'
op|','
name|'fake_event'
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
name|'db'
op|','
string|"'action_event_start'"
op|')'
newline|'\n'
DECL|member|test_event_start_no_result
name|'def'
name|'test_event_start_no_result'
op|'('
name|'self'
op|','
name|'mock_start'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'event_start'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'event'
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
name|'db'
op|','
string|"'action_event_finish'"
op|')'
newline|'\n'
DECL|member|test_event_finish
name|'def'
name|'test_event_finish'
op|'('
name|'self'
op|','
name|'mock_finish'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|')'
newline|'\n'
name|'expected_packed_values'
op|'['
string|"'finish_time'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'event'
op|','
name|'fake_event'
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
name|'db'
op|','
string|"'action_event_finish'"
op|')'
newline|'\n'
DECL|member|test_event_finish_no_result
name|'def'
name|'test_event_finish_no_result'
op|'('
name|'self'
op|','
name|'mock_finish'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|')'
newline|'\n'
name|'expected_packed_values'
op|'['
string|"'finish_time'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'event'
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
name|'traceback'
op|','
string|"'format_tb'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'action_event_finish'"
op|')'
newline|'\n'
DECL|member|test_event_finish_with_failure
name|'def'
name|'test_event_finish_with_failure'
op|'('
name|'self'
op|','
name|'mock_finish'
op|','
name|'mock_tb'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
string|"'val'"
op|','
string|"'fake-tb'"
op|')'
newline|'\n'
name|'expected_packed_values'
op|'['
string|"'finish_time'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'test_class'
op|'.'
name|'event_finish_with_failure'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
string|"'val'"
op|','
string|"'fake-tb'"
op|','
nl|'\n'
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'event'
op|','
name|'fake_event'
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
name|'traceback'
op|','
string|"'format_tb'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'action_event_finish'"
op|')'
newline|'\n'
DECL|member|test_event_finish_with_failure_legacy
name|'def'
name|'test_event_finish_with_failure_legacy'
op|'('
name|'self'
op|','
name|'mock_finish'
op|','
name|'mock_tb'
op|')'
op|':'
newline|'\n'
comment|"# Tests that exc_tb is serialized when it's not a string type."
nl|'\n'
indent|'        '
name|'mock_tb'
op|'.'
name|'return_value'
op|'='
string|"'fake-tb'"
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
string|"'val'"
op|','
string|"'fake-tb'"
op|')'
newline|'\n'
name|'expected_packed_values'
op|'['
string|"'finish_time'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'fake_tb'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'fake_tb'
newline|'\n'
name|'event'
op|'='
name|'test_class'
op|'.'
name|'event_finish_with_failure'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
name|'exc_val'
op|'='
string|"'val'"
op|','
nl|'\n'
name|'exc_tb'
op|'='
name|'fake_tb'
op|','
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'event'
op|','
name|'fake_event'
op|')'
newline|'\n'
name|'mock_tb'
op|'.'
name|'assert_called_once_with'
op|'('
name|'fake_tb'
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
name|'db'
op|','
string|"'action_event_finish'"
op|')'
newline|'\n'
DECL|member|test_event_finish_with_failure_legacy_unicode
name|'def'
name|'test_event_finish_with_failure_legacy_unicode'
op|'('
name|'self'
op|','
name|'mock_finish'
op|')'
op|':'
newline|'\n'
comment|'# Tests that traceback.format_tb is not called when exc_tb is unicode.'
nl|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
string|"'val'"
op|','
nl|'\n'
name|'six'
op|'.'
name|'text_type'
op|'('
string|"'fake-tb'"
op|')'
op|')'
newline|'\n'
name|'expected_packed_values'
op|'['
string|"'finish_time'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'test_class'
op|'.'
name|'event_finish_with_failure'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
name|'exc_val'
op|'='
string|"'val'"
op|','
nl|'\n'
name|'exc_tb'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
string|"'fake-tb'"
op|')'
op|','
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'event'
op|','
name|'fake_event'
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
name|'traceback'
op|','
string|"'format_tb'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'action_event_finish'"
op|')'
newline|'\n'
DECL|member|test_event_finish_with_failure_no_result
name|'def'
name|'test_event_finish_with_failure_no_result'
op|'('
name|'self'
op|','
name|'mock_finish'
op|','
name|'mock_tb'
op|')'
op|':'
newline|'\n'
comment|'# Tests that traceback.format_tb is not called when exc_tb is a str'
nl|'\n'
comment|'# and want_result is False, so no event should come back.'
nl|'\n'
indent|'        '
name|'mock_tb'
op|'.'
name|'return_value'
op|'='
string|"'fake-tb'"
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'NOW'
op|')'
newline|'\n'
name|'test_class'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
newline|'\n'
name|'expected_packed_values'
op|'='
name|'test_class'
op|'.'
name|'pack_action_event_finish'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
string|"'val'"
op|','
string|"'fake-tb'"
op|')'
newline|'\n'
name|'expected_packed_values'
op|'['
string|"'finish_time'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_finish'
op|'.'
name|'return_value'
op|'='
name|'fake_event'
newline|'\n'
name|'event'
op|'='
name|'test_class'
op|'.'
name|'event_finish_with_failure'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
string|"'val'"
op|','
string|"'fake-tb'"
op|','
nl|'\n'
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
name|'mock_finish'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'expected_packed_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'event'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_tb'
op|'.'
name|'called'
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
name|'db'
op|','
string|"'action_events_get'"
op|')'
newline|'\n'
DECL|member|test_get_by_action
name|'def'
name|'test_get_by_action'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_events'
op|'='
op|'['
name|'dict'
op|'('
name|'fake_event'
op|','
name|'id'
op|'='
number|'1234'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'fake_event'
op|','
name|'id'
op|'='
number|'5678'
op|')'
op|']'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'fake_events'
newline|'\n'
name|'obj_list'
op|'='
name|'instance_action'
op|'.'
name|'InstanceActionEventList'
op|'.'
name|'get_by_action'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-action-id'"
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'event'
name|'in'
name|'enumerate'
op|'('
name|'obj_list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'event'
op|','
name|'fake_events'
op|'['
name|'index'
op|']'
op|')'
newline|'\n'
dedent|''
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-action-id'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.instance_action.InstanceActionEvent.'"
nl|'\n'
string|"'pack_action_event_finish'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'traceback.format_tb'"
op|')'
newline|'\n'
DECL|member|test_event_finish_with_failure_serialized
name|'def'
name|'test_event_finish_with_failure_serialized'
op|'('
name|'self'
op|','
name|'mock_format'
op|','
nl|'\n'
name|'mock_pack'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_format'
op|'.'
name|'return_value'
op|'='
string|"'traceback'"
newline|'\n'
name|'mock_pack'
op|'.'
name|'side_effect'
op|'='
name|'test'
op|'.'
name|'TestingException'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'test'
op|'.'
name|'TestingException'
op|','
nl|'\n'
name|'instance_action'
op|'.'
name|'InstanceActionEvent'
op|'.'
name|'event_finish_with_failure'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
string|"'fake-event'"
op|','
nl|'\n'
name|'exc_val'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'exc_val'
op|','
nl|'\n'
name|'exc_tb'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'exc_tb'
op|')'
newline|'\n'
name|'mock_pack'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'fake-event'"
op|','
nl|'\n'
name|'exc_val'
op|'='
name|'str'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'exc_val'
op|')'
op|','
nl|'\n'
name|'exc_tb'
op|'='
string|"'traceback'"
op|')'
newline|'\n'
name|'mock_format'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'exc_tb'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceActionEventObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceActionEventObject
name|'_TestInstanceActionEventObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteInstanceActionEventObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceActionEventObject
name|'_TestInstanceActionEventObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
