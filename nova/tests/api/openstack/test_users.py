begin_unit
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
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'users'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
name|'import'
name|'User'
op|','
name|'Project'
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
DECL|function|fake_init
name|'def'
name|'fake_init'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'manager'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_admin_check
dedent|''
name|'def'
name|'fake_admin_check'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UsersTest
dedent|''
name|'class'
name|'UsersTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'UsersTest'
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
name|'set_flags_verbosity'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'users'
op|'.'
name|'Controller'
op|','
string|"'__init__'"
op|','
nl|'\n'
name|'fake_init'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'users'
op|'.'
name|'Controller'
op|','
string|"'_check_admin'"
op|','
nl|'\n'
name|'fake_admin_check'
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
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'='
name|'dict'
op|'('
name|'testacct'
op|'='
name|'Project'
op|'('
string|"'testacct'"
op|','
nl|'\n'
string|"'testacct'"
op|','
nl|'\n'
string|"'id1'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
op|'['
op|']'
op|')'
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
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
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
name|'stub_out_auth'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'fakemgr'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'fakemgr'
op|'.'
name|'add_user'
op|'('
name|'User'
op|'('
string|"'id1'"
op|','
string|"'guy1'"
op|','
string|"'acc1'"
op|','
string|"'secret1'"
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'fakemgr'
op|'.'
name|'add_user'
op|'('
name|'User'
op|'('
string|"'id2'"
op|','
string|"'guy2'"
op|','
string|"'acc2'"
op|','
string|"'secret2'"
op|','
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_user_list
dedent|''
name|'def'
name|'test_get_user_list'
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
string|"'/v1.0/users'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'users'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_user_by_id
dedent|''
name|'def'
name|'test_get_user_by_id'
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
string|"'/v1.0/users/id2'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'id2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'guy2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'secret'"
op|']'
op|','
string|"'secret2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'admin'"
op|']'
op|','
name|'True'
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_delete
dedent|''
name|'def'
name|'test_user_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Check the user exists'
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
string|"'/v1.0/users/id1'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'id1'"
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the user'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/users/id1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'id1'"
name|'not'
name|'in'
op|'['
name|'u'
op|'.'
name|'id'
name|'for'
name|'u'
name|'in'
nl|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|']'
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check the user is not returned (and returns 404)'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/users/id1'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
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
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_create
dedent|''
name|'def'
name|'test_user_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'secret'
op|'='
name|'utils'
op|'.'
name|'generate_password'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'user'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'test_guy'"
op|','
nl|'\n'
name|'access'
op|'='
string|"'acc3'"
op|','
nl|'\n'
name|'secret'
op|'='
name|'secret'
op|','
nl|'\n'
name|'admin'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/users'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"Content-Type"'
op|']'
op|'='
string|'"application/json"'
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
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(justinsb): This is a questionable assertion in general'
nl|'\n'
comment|'# fake sets id=name, but others might not...'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'test_guy'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'test_guy'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'access'"
op|']'
op|','
string|"'acc3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'secret'"
op|']'
op|','
name|'secret'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'admin'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'test_guy'"
name|'in'
op|'['
name|'u'
op|'.'
name|'id'
name|'for'
name|'u'
name|'in'
nl|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_update
dedent|''
name|'def'
name|'test_user_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'new_secret'
op|'='
name|'utils'
op|'.'
name|'generate_password'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'user'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'guy2'"
op|','
nl|'\n'
name|'access'
op|'='
string|"'acc2'"
op|','
nl|'\n'
name|'secret'
op|'='
name|'new_secret'
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/users/id2'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"Content-Type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'id2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'guy2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'access'"
op|']'
op|','
string|"'acc2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'secret'"
op|']'
op|','
name|'new_secret'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'user'"
op|']'
op|'['
string|"'admin'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
