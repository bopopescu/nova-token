begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
name|'import'
name|'webob'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'vsa'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
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
name|'import'
name|'nova'
op|'.'
name|'wsgi'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
op|'.'
name|'virtual_storage_arrays'
name|'import'
name|'_vsa_view'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.api.openstack.vsa'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|last_param
name|'last_param'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_default_vsa_param
name|'def'
name|'_get_default_vsa_param'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'display_name'"
op|':'
string|"'Test_VSA_name'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'Test_VSA_description'"
op|','
nl|'\n'
string|"'vc_count'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
string|"'m1.small'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'image_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'storage'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'shared'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_vsa_create
dedent|''
name|'def'
name|'stub_vsa_create'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'param'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'last_param'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_create: param=%s"'
op|')'
op|','
name|'param'
op|')'
newline|'\n'
name|'param'
op|'['
string|"'id'"
op|']'
op|'='
number|'123'
newline|'\n'
name|'param'
op|'['
string|"'name'"
op|']'
op|'='
string|"'Test name'"
newline|'\n'
name|'param'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
number|'5'
newline|'\n'
name|'last_param'
op|'='
name|'param'
newline|'\n'
name|'return'
name|'param'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_vsa_delete
dedent|''
name|'def'
name|'stub_vsa_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'last_param'
newline|'\n'
name|'last_param'
op|'='
name|'dict'
op|'('
name|'vsa_id'
op|'='
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_delete: %s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'vsa_id'
op|'!='
string|"'123'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_vsa_get
dedent|''
dedent|''
name|'def'
name|'stub_vsa_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'last_param'
newline|'\n'
name|'last_param'
op|'='
name|'dict'
op|'('
name|'vsa_id'
op|'='
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_get: %s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'vsa_id'
op|'!='
string|"'123'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'param'
op|'='
name|'_get_default_vsa_param'
op|'('
op|')'
newline|'\n'
name|'param'
op|'['
string|"'id'"
op|']'
op|'='
name|'vsa_id'
newline|'\n'
name|'return'
name|'param'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_vsa_get_all
dedent|''
name|'def'
name|'stub_vsa_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_get_all: %s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'param'
op|'='
name|'_get_default_vsa_param'
op|'('
op|')'
newline|'\n'
name|'param'
op|'['
string|"'id'"
op|']'
op|'='
number|'123'
newline|'\n'
name|'return'
op|'['
name|'param'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VSAApiTest
dedent|''
name|'class'
name|'VSAApiTest'
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
name|'VSAApiTest'
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
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'reset_fake_data'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vsa'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"create"'
op|','
name|'stub_vsa_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vsa'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"delete"'
op|','
name|'stub_vsa_delete'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vsa'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'stub_vsa_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vsa'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get_all"'
op|','
name|'stub_vsa_get_all'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VSAApiTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create
dedent|''
name|'def'
name|'test_vsa_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_param'
newline|'\n'
name|'last_param'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'vsa'
op|'='
op|'{'
string|'"displayName"'
op|':'
string|'"VSA Test Name"'
op|','
nl|'\n'
string|'"displayDescription"'
op|':'
string|'"VSA Test Desc"'
op|'}'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'vsa'
op|'='
name|'vsa'
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
string|"'/v1.1/777/zadr-vsa'"
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
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
comment|'# Compare if parameters were correctly passed to stub'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_param'
op|'['
string|"'display_name'"
op|']'
op|','
string|'"VSA Test Name"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_param'
op|'['
string|"'display_description'"
op|']'
op|','
string|'"VSA Test Desc"'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'vsa'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'vsa'"
op|']'
op|'['
string|"'displayName'"
op|']'
op|','
name|'vsa'
op|'['
string|"'displayName'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'vsa'"
op|']'
op|'['
string|"'displayDescription'"
op|']'
op|','
nl|'\n'
name|'vsa'
op|'['
string|"'displayDescription'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_no_body
dedent|''
name|'def'
name|'test_vsa_create_no_body'
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
string|"'/v1.1/777/zadr-vsa'"
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
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'422'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_delete
dedent|''
name|'def'
name|'test_vsa_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_param'
newline|'\n'
name|'last_param'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
number|'123'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/%d'"
op|'%'
name|'vsa_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
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
name|'str'
op|'('
name|'last_param'
op|'['
string|"'vsa_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_delete_invalid_id
dedent|''
name|'def'
name|'test_vsa_delete_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_param'
newline|'\n'
name|'last_param'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
number|'234'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/%d'"
op|'%'
name|'vsa_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'last_param'
op|'['
string|"'vsa_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_show
dedent|''
name|'def'
name|'test_vsa_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_param'
newline|'\n'
name|'last_param'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
number|'123'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/%d'"
op|'%'
name|'vsa_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
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
name|'str'
op|'('
name|'last_param'
op|'['
string|"'vsa_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'vsa'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'vsa'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_show_invalid_id
dedent|''
name|'def'
name|'test_vsa_show_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_param'
newline|'\n'
name|'last_param'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
number|'234'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/%d'"
op|'%'
name|'vsa_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'last_param'
op|'['
string|"'vsa_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_index
dedent|''
name|'def'
name|'test_vsa_index'
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
string|"'/v1.1/777/zadr-vsa'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'vsaSet'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'resp_vsas'
op|'='
name|'resp_dict'
op|'['
string|"'vsaSet'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'resp_vsas'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'resp_vsa'
op|'='
name|'resp_vsas'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_vsa'
op|'['
string|"'id'"
op|']'
op|','
number|'123'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_detail
dedent|''
name|'def'
name|'test_vsa_detail'
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
string|"'/v1.1/777/zadr-vsa/detail'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'vsaSet'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'resp_vsas'
op|'='
name|'resp_dict'
op|'['
string|"'vsaSet'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'resp_vsas'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'resp_vsa'
op|'='
name|'resp_vsas'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_vsa'
op|'['
string|"'id'"
op|']'
op|','
number|'123'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_default_volume_param
dedent|''
dedent|''
name|'def'
name|'_get_default_volume_param'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'attach_status'"
op|':'
string|"'detached'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'vol name'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'Default vol name'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'Default vol description'"
op|','
nl|'\n'
string|"'volume_type_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'volume_metadata'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_get_vsa_volume_type
dedent|''
name|'def'
name|'stub_get_vsa_volume_type'
op|'('
name|'self'
op|','
name|'context'
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
nl|'\n'
string|"'name'"
op|':'
string|"'VSA volume type'"
op|','
nl|'\n'
string|"'extra_specs'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'vsa_volume'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_volume_create
dedent|''
name|'def'
name|'stub_volume_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'size'
op|','
name|'snapshot_id'
op|','
name|'name'
op|','
name|'description'
op|','
nl|'\n'
op|'**'
name|'param'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_create: param=%s"'
op|')'
op|','
name|'size'
op|')'
newline|'\n'
name|'vol'
op|'='
name|'_get_default_volume_param'
op|'('
op|')'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'vol'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'name'
newline|'\n'
name|'vol'
op|'['
string|"'display_description'"
op|']'
op|'='
name|'description'
newline|'\n'
name|'return'
name|'vol'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_volume_update
dedent|''
name|'def'
name|'stub_volume_update'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'param'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_volume_update: param=%s"'
op|')'
op|','
name|'param'
op|')'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_volume_delete
dedent|''
name|'def'
name|'stub_volume_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'param'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_volume_delete: param=%s"'
op|')'
op|','
name|'param'
op|')'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_volume_get
dedent|''
name|'def'
name|'stub_volume_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_volume_get: volume_id=%s"'
op|')'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'vol'
op|'='
name|'_get_default_volume_param'
op|'('
op|')'
newline|'\n'
name|'vol'
op|'['
string|"'id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'meta'
op|'='
op|'{'
string|"'key'"
op|':'
string|"'from_vsa_id'"
op|','
string|"'value'"
op|':'
string|"'123'"
op|'}'
newline|'\n'
name|'if'
name|'volume_id'
op|'=='
string|"'345'"
op|':'
newline|'\n'
indent|'        '
name|'meta'
op|'='
op|'{'
string|"'key'"
op|':'
string|"'to_vsa_id'"
op|','
string|"'value'"
op|':'
string|"'123'"
op|'}'
newline|'\n'
dedent|''
name|'vol'
op|'['
string|"'volume_metadata'"
op|']'
op|'.'
name|'append'
op|'('
name|'meta'
op|')'
newline|'\n'
name|'return'
name|'vol'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_volume_get_notfound
dedent|''
name|'def'
name|'stub_volume_get_notfound'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_volume_get_all
dedent|''
name|'def'
name|'stub_volume_get_all'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'search_opts'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vol'
op|'='
name|'stub_volume_get'
op|'('
name|'self'
op|','
name|'context'
op|','
string|"'123'"
op|')'
newline|'\n'
name|'vol'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'search_opts'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
name|'return'
op|'['
name|'vol'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_vsa
dedent|''
name|'def'
name|'return_vsa'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'vsa_id'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VSAVolumeApiTest
dedent|''
name|'class'
name|'VSAVolumeApiTest'
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
op|','
name|'test_obj'
op|'='
name|'None'
op|','
name|'test_objs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VSAVolumeApiTest'
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
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'reset_fake_data'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'vsa_get'"
op|','
name|'return_vsa'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vsa'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get_vsa_volume_type"'
op|','
nl|'\n'
name|'stub_get_vsa_volume_type'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"update"'
op|','
name|'stub_volume_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"delete"'
op|','
name|'stub_volume_delete'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'stub_volume_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get_all"'
op|','
name|'stub_volume_get_all'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_obj'
op|'='
name|'test_obj'
name|'if'
name|'test_obj'
name|'else'
string|'"volume"'
newline|'\n'
name|'self'
op|'.'
name|'test_objs'
op|'='
name|'test_objs'
name|'if'
name|'test_objs'
name|'else'
string|'"volumes"'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VSAVolumeApiTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_create
dedent|''
name|'def'
name|'test_vsa_volume_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"create"'
op|','
name|'stub_volume_create'
op|')'
newline|'\n'
nl|'\n'
name|'vol'
op|'='
op|'{'
string|'"size"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"displayName"'
op|':'
string|'"VSA Volume Test Name"'
op|','
nl|'\n'
string|'"displayDescription"'
op|':'
string|'"VSA Volume Test Desc"'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
name|'self'
op|'.'
name|'test_obj'
op|':'
name|'vol'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/123/%s'"
op|'%'
name|'self'
op|'.'
name|'test_objs'
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
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'resp'
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
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'test_obj'
op|'=='
string|'"volume"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'test_obj'
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
name|'self'
op|'.'
name|'test_obj'
op|']'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
name|'self'
op|'.'
name|'test_obj'
op|']'
op|'['
string|"'displayName'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'displayName'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
name|'self'
op|'.'
name|'test_obj'
op|']'
op|'['
string|"'displayDescription'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'displayDescription'"
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_create_no_body
dedent|''
dedent|''
name|'def'
name|'test_vsa_volume_create_no_body'
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
string|"'/v1.1/777/zadr-vsa/123/%s'"
op|'%'
name|'self'
op|'.'
name|'test_objs'
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
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'if'
name|'self'
op|'.'
name|'test_obj'
op|'=='
string|'"volume"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'422'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_index
dedent|''
dedent|''
name|'def'
name|'test_vsa_volume_index'
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
string|"'/v1.1/777/zadr-vsa/123/%s'"
op|'%'
name|'self'
op|'.'
name|'test_objs'
op|')'
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_detail
dedent|''
name|'def'
name|'test_vsa_volume_detail'
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
string|"'/v1.1/777/zadr-vsa/123/%s/detail'"
op|'%'
name|'self'
op|'.'
name|'test_objs'
op|')'
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_show
dedent|''
name|'def'
name|'test_vsa_volume_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj_num'
op|'='
number|'234'
name|'if'
name|'self'
op|'.'
name|'test_objs'
op|'=='
string|'"volumes"'
name|'else'
number|'345'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/123/%s/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'test_objs'
op|','
name|'obj_num'
op|')'
op|')'
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_show_no_vsa_assignment
dedent|''
name|'def'
name|'test_vsa_volume_show_no_vsa_assignment'
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
string|"'/v1.1/777/zadr-vsa/4/%s/333'"
op|'%'
op|'('
name|'self'
op|'.'
name|'test_objs'
op|')'
op|')'
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_show_no_volume
dedent|''
name|'def'
name|'test_vsa_volume_show_no_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'stub_volume_get_notfound'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/123/%s/333'"
op|'%'
op|'('
name|'self'
op|'.'
name|'test_objs'
op|')'
op|')'
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_update
dedent|''
name|'def'
name|'test_vsa_volume_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj_num'
op|'='
number|'234'
name|'if'
name|'self'
op|'.'
name|'test_objs'
op|'=='
string|'"volumes"'
name|'else'
number|'345'
newline|'\n'
name|'update'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"available"'
op|','
nl|'\n'
string|'"displayName"'
op|':'
string|'"Test Display name"'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
name|'self'
op|'.'
name|'test_obj'
op|':'
name|'update'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/123/%s/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'test_objs'
op|','
name|'obj_num'
op|')'
op|')'
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
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'if'
name|'self'
op|'.'
name|'test_obj'
op|'=='
string|'"volume"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_delete
dedent|''
dedent|''
name|'def'
name|'test_vsa_volume_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj_num'
op|'='
number|'234'
name|'if'
name|'self'
op|'.'
name|'test_objs'
op|'=='
string|'"volumes"'
name|'else'
number|'345'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/123/%s/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'test_objs'
op|','
name|'obj_num'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'resp'
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
name|'if'
name|'self'
op|'.'
name|'test_obj'
op|'=='
string|'"volume"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_delete_no_vsa_assignment
dedent|''
dedent|''
name|'def'
name|'test_vsa_volume_delete_no_vsa_assignment'
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
string|"'/v1.1/777/zadr-vsa/4/%s/333'"
op|'%'
op|'('
name|'self'
op|'.'
name|'test_objs'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'resp'
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
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_delete_no_volume
dedent|''
name|'def'
name|'test_vsa_volume_delete_no_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'stub_volume_get_notfound'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/777/zadr-vsa/123/%s/333'"
op|'%'
op|'('
name|'self'
op|'.'
name|'test_objs'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'resp'
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
name|'if'
name|'self'
op|'.'
name|'test_obj'
op|'=='
string|'"volume"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VSADriveApiTest
dedent|''
dedent|''
dedent|''
name|'class'
name|'VSADriveApiTest'
op|'('
name|'VSAVolumeApiTest'
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
name|'VSADriveApiTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
name|'test_obj'
op|'='
string|'"drive"'
op|','
nl|'\n'
name|'test_objs'
op|'='
string|'"drives"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VSADriveApiTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
