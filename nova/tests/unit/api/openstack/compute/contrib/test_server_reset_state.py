begin_unit
comment|'#   Copyright 2015 NEC Corporation. All rights reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'uuidutils'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'admin_actions'
name|'as'
name|'admin_actions_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'admin_actions'
name|'as'
name|'admin_actions_v21'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResetStateTestsV21
name|'class'
name|'ResetStateTestsV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|admin_act
indent|'    '
name|'admin_act'
op|'='
name|'admin_actions_v21'
newline|'\n'
DECL|variable|bad_request
name|'bad_request'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'ResetStateTestsV21'
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
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'='
name|'self'
op|'.'
name|'admin_act'
op|'.'
name|'AdminActionsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'compute_api'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_request
dedent|''
name|'def'
name|'_get_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_state
dedent|''
name|'def'
name|'test_no_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'bad_request'
op|','
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_state
dedent|''
name|'def'
name|'test_bad_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'bad_request'
op|','
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"spam"'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_instance
dedent|''
name|'def'
name|'test_no_instance'
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
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'get'"
op|')'
newline|'\n'
name|'exc'
op|'='
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"'inst_ud'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exc'
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
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"active"'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_mock
dedent|''
name|'def'
name|'_setup_mock'
op|'('
name|'self'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'uuid'
newline|'\n'
name|'instance'
op|'.'
name|'vm_state'
op|'='
string|"'fake'"
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
string|"'fake'"
newline|'\n'
name|'instance'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'instance'
op|','
string|"'save'"
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
name|'compute_api'
op|','
string|"'get'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|check_state
name|'def'
name|'check_state'
op|'('
name|'admin_state_reset'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'expected'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'expected'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'v'
op|','
name|'getattr'
op|'('
name|'instance'
op|','
name|'k'
op|')'
op|','
nl|'\n'
string|'"Instance.%s doesn\'t match"'
op|'%'
name|'k'
op|')'
newline|'\n'
dedent|''
name|'instance'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'.'
name|'uuid'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
name|'admin_state_reset'
op|'='
name|'True'
op|')'
op|'.'
name|'WithSideEffects'
op|'('
name|'check_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_active
dedent|''
name|'def'
name|'test_reset_active'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_setup_mock'
op|'('
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|')'
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
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"active"'
op|'}'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|'('
name|'self'
op|'.'
name|'request'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
comment|'# NOTE: on v2.1, http status code is set as wsgi_code of API'
nl|'\n'
comment|'# method instead of status_int in a response object.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'admin_api'
op|','
nl|'\n'
name|'admin_actions_v21'
op|'.'
name|'AdminActionsController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|'.'
name|'wsgi_code'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'result'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_error
dedent|''
name|'def'
name|'test_reset_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_setup_mock'
op|'('
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|')'
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
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"error"'
op|'}'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|'('
name|'self'
op|'.'
name|'request'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
comment|'# NOTE: on v2.1, http status code is set as wsgi_code of API'
nl|'\n'
comment|'# method instead of status_int in a response object.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'admin_api'
op|','
nl|'\n'
name|'admin_actions_v21'
op|'.'
name|'AdminActionsController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|'.'
name|'wsgi_code'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'result'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResetStateTestsV2
dedent|''
dedent|''
name|'class'
name|'ResetStateTestsV2'
op|'('
name|'ResetStateTestsV21'
op|')'
op|':'
newline|'\n'
DECL|variable|admin_act
indent|'    '
name|'admin_act'
op|'='
name|'admin_actions_v2'
newline|'\n'
DECL|variable|bad_request
name|'bad_request'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
dedent|''
endmarker|''
end_unit
