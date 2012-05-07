begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
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
DECL|class|TestNoAuthMiddleware
name|'class'
name|'TestNoAuthMiddleware'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestNoAuthMiddleware'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'context'
op|','
string|"'RequestContext'"
op|','
name|'fakes'
op|'.'
name|'FakeRequestContext'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'clear_fakes'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_user
dedent|''
name|'def'
name|'test_authorize_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Project-Id'"
op|']'
op|'='
string|"'user1_project'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'use_no_auth'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Server-Management-Url'"
op|']'
op|','
nl|'\n'
string|'"http://localhost/v2/user1_project"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_user_trailing_slash
dedent|''
name|'def'
name|'test_authorize_user_trailing_slash'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'#make sure it works with trailing slash on the request'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Project-Id'"
op|']'
op|'='
string|"'user1_project'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'use_no_auth'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Server-Management-Url'"
op|']'
op|','
nl|'\n'
string|'"http://localhost/v2/user1_project"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_auth_token_no_empty_headers
dedent|''
name|'def'
name|'test_auth_token_no_empty_headers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Project-Id'"
op|']'
op|'='
string|"'user1_project'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'use_no_auth'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'X-CDN-Management-Url'"
name|'in'
name|'result'
op|'.'
name|'headers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'X-Storage-Url'"
name|'in'
name|'result'
op|'.'
name|'headers'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
