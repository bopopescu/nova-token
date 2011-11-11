begin_unit
comment|'#   Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|INSTANCE
name|'INSTANCE'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"fake"'
op|','
nl|'\n'
string|'"display_name"'
op|':'
string|'"test_server"'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"abcd"'
op|','
nl|'\n'
string|'"user_id"'
op|':'
string|"'fake_user_id'"
op|','
nl|'\n'
string|'"tenant_id"'
op|':'
string|"'fake_tenant_id'"
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"security_groups"'
op|':'
op|'['
op|'{'
string|'"id"'
op|':'
number|'1'
op|','
string|'"name"'
op|':'
string|'"test"'
op|'}'
op|']'
op|','
nl|'\n'
string|'"progress"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"image_ref"'
op|':'
string|"'http://foo.com/123'"
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"instance_type"'
op|':'
op|'{'
string|'"flavorid"'
op|':'
string|"'124'"
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api
name|'def'
name|'fake_compute_api'
op|'('
name|'cls'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api_get
dedent|''
name|'def'
name|'fake_compute_api_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'uuid'"
op|':'
name|'instance_id'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminActionsTest
dedent|''
name|'class'
name|'AdminActionsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_actions
indent|'    '
name|'_actions'
op|'='
op|'('
string|"'pause'"
op|','
string|"'unpause'"
op|','
string|"'suspend'"
op|','
string|"'resume'"
op|','
string|"'migrate'"
op|','
nl|'\n'
string|"'resetNetwork'"
op|','
string|"'injectNetworkInfo'"
op|','
string|"'lock'"
op|','
string|"'unlock'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_methods
name|'_methods'
op|'='
op|'('
string|"'pause'"
op|','
string|"'unpause'"
op|','
string|"'suspend'"
op|','
string|"'resume'"
op|','
string|"'resize'"
op|','
nl|'\n'
string|"'reset_network'"
op|','
string|"'inject_network_info'"
op|','
string|"'lock'"
op|','
string|"'unlock'"
op|')'
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
name|'AdminActionsTest'
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
name|'allow_admin_api'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_api_get'
op|')'
newline|'\n'
name|'for'
name|'_method'
name|'in'
name|'self'
op|'.'
name|'_methods'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'API'
op|','
name|'_method'
op|','
name|'fake_compute_api'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_admin_api_enabled
dedent|''
dedent|''
name|'def'
name|'test_admin_api_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
newline|'\n'
name|'for'
name|'_action'
name|'in'
name|'self'
op|'.'
name|'_actions'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/abcd/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
name|'_action'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
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
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_admin_api_disabled
dedent|''
dedent|''
name|'def'
name|'test_admin_api_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|'='
name|'False'
newline|'\n'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
newline|'\n'
name|'for'
name|'_action'
name|'in'
name|'self'
op|'.'
name|'_actions'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/abcd/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
name|'_action'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
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
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
