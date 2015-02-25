begin_unit
comment|'# Copyright 2011 Eldar Nugaev'
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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'compute'
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
name|'server_diagnostics'
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
DECL|variable|UUID
name|'UUID'
op|'='
string|"'abc'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_diagnostics
name|'def'
name|'fake_get_diagnostics'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'data'"
op|':'
string|"'Some diagnostic info'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get
dedent|''
name|'def'
name|'fake_instance_get'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance_uuid'
op|','
name|'want_objects'
op|'='
name|'False'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'instance_uuid'
op|'!='
name|'UUID'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"Invalid UUID"'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerDiagnosticsTestV21
dedent|''
name|'class'
name|'ServerDiagnosticsTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_setup_router
indent|'    '
name|'def'
name|'_setup_router'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'router'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
nl|'\n'
string|"'os-server-diagnostics'"
op|')'
op|')'
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
nl|'\n'
string|"'/fake/servers/%s/diagnostics'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ServerDiagnosticsTestV21'
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
name|'_setup_router'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_diagnostics'"
op|','
nl|'\n'
name|'fake_get_diagnostics'
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
string|"'get'"
op|','
nl|'\n'
name|'fake_instance_get'
op|')'
newline|'\n'
DECL|member|test_get_diagnostics
name|'def'
name|'test_get_diagnostics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'output'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
op|'{'
string|"'data'"
op|':'
string|"'Some diagnostic info'"
op|'}'
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
string|"'get_diagnostics'"
op|','
nl|'\n'
name|'fake_get_diagnostics'
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
string|"'get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'UUID'
op|')'
op|')'
newline|'\n'
DECL|member|test_get_diagnostics_with_non_existed_instance
name|'def'
name|'test_get_diagnostics_with_non_existed_instance'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
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
string|"'get_diagnostics'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
string|"'fake message'"
op|')'
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
string|"'get'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
DECL|member|test_get_diagnostics_raise_conflict_on_invalid_state
name|'def'
name|'test_get_diagnostics_raise_conflict_on_invalid_state'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_get_diagnostics'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'409'
op|','
name|'res'
op|'.'
name|'status_int'
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
string|"'get_diagnostics'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'NotImplementedError'
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
string|"'get'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
DECL|member|test_get_diagnostics_raise_no_notimplementederror
name|'def'
name|'test_get_diagnostics_raise_no_notimplementederror'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_get_diagnostics'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'501'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerDiagnosticsTestV2
dedent|''
dedent|''
name|'class'
name|'ServerDiagnosticsTestV2'
op|'('
name|'ServerDiagnosticsTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_setup_router
indent|'    '
name|'def'
name|'_setup_router'
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
name|'verbose'
op|'='
name|'True'
op|','
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Server_diagnostics'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'router'
op|'='
name|'compute'
op|'.'
name|'APIRouter'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
string|"'diagnostics'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerDiagnosticsEnforcementV21
dedent|''
dedent|''
name|'class'
name|'ServerDiagnosticsEnforcementV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
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
name|'ServerDiagnosticsEnforcementV21'
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
name|'controller'
op|'='
name|'server_diagnostics'
op|'.'
name|'ServerDiagnosticsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
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
DECL|member|test_get_diagnostics_policy_failed
dedent|''
name|'def'
name|'test_get_diagnostics_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"compute_extension:v3:os-server-diagnostics"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
