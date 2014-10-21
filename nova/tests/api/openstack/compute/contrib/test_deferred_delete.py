begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'contrib'
name|'import'
name|'deferred_delete'
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
name|'deferred_delete'
name|'as'
name|'dd_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
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
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'environ'
op|'='
op|'{'
string|"'nova.context'"
op|':'
name|'context'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DeferredDeleteExtensionTestV21
dedent|''
dedent|''
name|'class'
name|'DeferredDeleteExtensionTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|ext_ver
indent|'    '
name|'ext_ver'
op|'='
name|'dd_v21'
op|'.'
name|'DeferredDeleteController'
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
name|'DeferredDeleteExtensionTestV21'
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
name|'fake_input_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'fake_uuid'
op|'='
string|"'fake_uuid'"
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'extension'
op|'='
name|'self'
op|'.'
name|'ext_ver'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_force_delete
dedent|''
name|'def'
name|'test_force_delete'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'force_delete'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
string|"'fake_instance'"
newline|'\n'
nl|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
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
name|'fake_instance'
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'force_delete'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'fake_instance'
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
name|'res'
op|'='
name|'self'
op|'.'
name|'extension'
op|'.'
name|'_force_delete'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_input_dict'
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
name|'extension'
op|','
name|'dd_v21'
op|'.'
name|'DeferredDeleteController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'extension'
op|'.'
name|'_force_delete'
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
name|'res'
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
DECL|member|test_force_delete_instance_not_found
dedent|''
name|'def'
name|'test_force_delete_instance_not_found'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
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
nl|'\n'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"'instance-0000'"
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
name|'extension'
op|'.'
name|'_force_delete'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_input_dict'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'force_delete'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake_uuid'"
op|')'
op|')'
newline|'\n'
DECL|member|test_force_delete_instance_locked
name|'def'
name|'test_force_delete_instance_locked'
op|'('
name|'self'
op|','
name|'mock_force_delete'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/fake_uuid/action'"
op|')'
newline|'\n'
name|'ex'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'extension'
op|'.'
name|'_force_delete'
op|','
nl|'\n'
name|'req'
op|','
string|"'fake_uuid'"
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'Instance fake_uuid is locked'"
op|','
name|'ex'
op|'.'
name|'explanation'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_restore
dedent|''
name|'def'
name|'test_restore'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'restore'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
string|"'fake_instance'"
newline|'\n'
nl|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
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
name|'fake_instance'
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'restore'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'fake_instance'
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
name|'res'
op|'='
name|'self'
op|'.'
name|'extension'
op|'.'
name|'_restore'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_input_dict'
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
name|'extension'
op|','
name|'dd_v21'
op|'.'
name|'DeferredDeleteController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'extension'
op|'.'
name|'_restore'
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
name|'res'
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
DECL|member|test_restore_instance_not_found
dedent|''
name|'def'
name|'test_restore_instance_not_found'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|','
name|'want_objects'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"'instance-0000'"
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
name|'self'
op|'.'
name|'extension'
op|'.'
name|'_restore'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_input_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_restore_raises_conflict_on_invalid_state
dedent|''
name|'def'
name|'test_restore_raises_conflict_on_invalid_state'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'restore'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
string|"'fake_instance'"
newline|'\n'
name|'exc'
op|'='
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
name|'attr'
op|'='
string|"'fake_attr'"
op|','
nl|'\n'
name|'state'
op|'='
string|"'fake_state'"
op|','
name|'method'
op|'='
string|"'fake_method'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
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
name|'fake_instance'
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'restore'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'fake_instance'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'exc'
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
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'extension'
op|'.'
name|'_restore'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
name|'self'
op|'.'
name|'fake_input_dict'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DeferredDeleteExtensionTestV2
dedent|''
dedent|''
name|'class'
name|'DeferredDeleteExtensionTestV2'
op|'('
name|'DeferredDeleteExtensionTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ext_ver
indent|'    '
name|'ext_ver'
op|'='
name|'deferred_delete'
op|'.'
name|'DeferredDeleteController'
newline|'\n'
dedent|''
endmarker|''
end_unit
