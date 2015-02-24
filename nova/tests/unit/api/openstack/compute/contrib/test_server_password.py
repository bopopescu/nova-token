begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'password'
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
name|'contrib'
name|'import'
name|'server_password'
name|'as'
name|'server_password_v2'
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
name|'server_password'
name|'as'
name|'server_password_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_ext_list'"
op|','
string|"'nova.api.openstack.compute.contrib'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerPasswordTestV21
name|'class'
name|'ServerPasswordTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
DECL|variable|server_password
name|'server_password'
op|'='
name|'server_password_v21'
newline|'\n'
DECL|variable|delete_call
name|'delete_call'
op|'='
string|"'self.controller.clear'"
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
name|'ServerPasswordTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
nl|'\n'
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
nl|'\n'
name|'lambda'
name|'self'
op|','
name|'ctxt'
op|','
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
nl|'\n'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
nl|'\n'
name|'ctxt'
op|','
nl|'\n'
name|'system_metadata'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'system_metadata'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'password'
op|'='
string|"'fakepass'"
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'server_password'
op|'.'
name|'ServerPasswordController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_req'
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
DECL|function|fake_extract_password
name|'def'
name|'fake_extract_password'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'password'
newline|'\n'
nl|'\n'
DECL|function|fake_convert_password
dedent|''
name|'def'
name|'fake_convert_password'
op|'('
name|'context'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'password'
op|'='
name|'password'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'password'
op|','
string|"'extract_password'"
op|','
name|'fake_extract_password'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'password'
op|','
string|"'convert_password'"
op|','
name|'fake_convert_password'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_password
dedent|''
name|'def'
name|'test_get_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'['
string|"'password'"
op|']'
op|','
string|"'fakepass'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_password
dedent|''
name|'def'
name|'test_reset_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'eval'
op|'('
name|'self'
op|'.'
name|'delete_call'
op|')'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'eval'
op|'('
name|'self'
op|'.'
name|'delete_call'
op|')'
op|'.'
name|'wsgi_code'
op|','
number|'204'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'['
string|"'password'"
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerPasswordTestV2
dedent|''
dedent|''
name|'class'
name|'ServerPasswordTestV2'
op|'('
name|'ServerPasswordTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|server_password
indent|'    '
name|'server_password'
op|'='
name|'server_password_v2'
newline|'\n'
DECL|variable|delete_call
name|'delete_call'
op|'='
string|"'self.controller.delete'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerPasswordPolicyEnforcementV21
dedent|''
name|'class'
name|'ServerPasswordPolicyEnforcementV21'
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
name|'ServerPasswordPolicyEnforcementV21'
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
name|'server_password_v21'
op|'.'
name|'ServerPasswordController'
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
DECL|member|_test_policy_failed
dedent|''
name|'def'
name|'_test_policy_failed'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'rule_name'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'method'
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
nl|'\n'
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
nl|'\n'
DECL|member|test_get_password_policy_failed
dedent|''
name|'def'
name|'test_get_password_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"compute_extension:v3:os-server-password"'
newline|'\n'
name|'self'
op|'.'
name|'_test_policy_failed'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'rule_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_clear_password_policy_failed
dedent|''
name|'def'
name|'test_clear_password_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"compute_extension:v3:os-server-password"'
newline|'\n'
name|'self'
op|'.'
name|'_test_policy_failed'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'clear'
op|','
name|'rule_name'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
