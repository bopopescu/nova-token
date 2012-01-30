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
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
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
name|'keypairs'
newline|'\n'
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
DECL|function|fake_keypair
name|'def'
name|'fake_keypair'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'public_key'"
op|':'
string|"'FAKE_KEY'"
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
string|"'FAKE_FINGERPRINT'"
op|','
nl|'\n'
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_key_pair_get_all_by_user
dedent|''
name|'def'
name|'db_key_pair_get_all_by_user'
op|'('
name|'self'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'fake_keypair'
op|'('
string|"'FAKE'"
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_key_pair_create
dedent|''
name|'def'
name|'db_key_pair_create'
op|'('
name|'self'
op|','
name|'keypair'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_key_pair_destroy
dedent|''
name|'def'
name|'db_key_pair_destroy'
op|'('
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
op|'('
name|'user_id'
name|'and'
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeypairsTest
dedent|''
dedent|''
name|'class'
name|'KeypairsTest'
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
name|'KeypairsTest'
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
name|'keypairs'
op|'.'
name|'KeypairController'
op|'('
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
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
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
name|'db'
op|','
string|'"key_pair_get_all_by_user"'
op|','
nl|'\n'
name|'db_key_pair_get_all_by_user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_create"'
op|','
nl|'\n'
name|'db_key_pair_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_destroy"'
op|','
nl|'\n'
name|'db_key_pair_destroy'
op|')'
newline|'\n'
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
DECL|member|test_keypair_list
dedent|''
name|'def'
name|'test_keypair_list'
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
string|"'/v2/fake/os-keypairs'"
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
name|'response'
op|'='
op|'{'
string|"'keypairs'"
op|':'
op|'['
op|'{'
string|"'keypair'"
op|':'
name|'fake_keypair'
op|'('
string|"'FAKE'"
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypair_create
dedent|''
name|'def'
name|'test_keypair_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'keypair'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'create_test'"
op|'}'
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
string|"'/v2/fake/os-keypairs'"
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
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
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'keypair'"
op|']'
op|'['
string|"'fingerprint'"
op|']'
op|')'
op|'>'
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'keypair'"
op|']'
op|'['
string|"'private_key'"
op|']'
op|')'
op|'>'
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypair_create_with_empty_name
dedent|''
name|'def'
name|'test_keypair_create_with_empty_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'keypair'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"''"
op|'}'
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
string|"'/v2/fake/os-keypairs'"
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypair_create_with_invalid_name
dedent|''
name|'def'
name|'test_keypair_create_with_invalid_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'keypair'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'a'"
op|'*'
number|'256'
nl|'\n'
op|'}'
nl|'\n'
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
string|"'/v2/fake/os-keypairs'"
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypair_import
dedent|''
name|'def'
name|'test_keypair_import'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'keypair'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'create_test'"
op|','
nl|'\n'
string|"'public_key'"
op|':'
string|"'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBYIznA'"
nl|'\n'
string|"'x9D7118Q1VKGpXy2HDiKyUTM8XcUuhQpo0srqb9rboUp4'"
nl|'\n'
string|"'a9NmCwpWpeElDLuva707GOUnfaBAvHBwsRXyxHJjRaI6Y'"
nl|'\n'
string|"'Qj2oLJwqvaSaWUbyT1vtryRqy6J3TecN0WINY71f4uymi'"
nl|'\n'
string|"'MZP0wby4bKBcYnac8KiCIlvkEl0ETjkOGUq8OyWRmn7lj'"
nl|'\n'
string|"'j5SESEUdBP0JnuTFKddWTU/wD6wydeJaUhBTqOlHn0kX1'"
nl|'\n'
string|"'GyqoNTE1UEhcM5ZRWgfUZfTjVyDF2kGj3vJLCJtJ8LoGc'"
nl|'\n'
string|"'j7YaN4uPg1rBle+izwE/tLonRrds+cev8p6krSSrxWOwB'"
nl|'\n'
string|"'bHkXa6OciiJDvkRzJXzf'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
string|"'/v2/fake/os-keypairs'"
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
comment|'# FIXME(ja): sholud we check that public_key was sent to create?'
nl|'\n'
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
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'keypair'"
op|']'
op|'['
string|"'fingerprint'"
op|']'
op|')'
op|'>'
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'private_key'"
name|'in'
name|'res_dict'
op|'['
string|"'keypair'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypair_import_bad_key
dedent|''
name|'def'
name|'test_keypair_import_bad_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'keypair'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'create_test'"
op|','
nl|'\n'
string|"'public_key'"
op|':'
string|"'ssh-what negative'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
string|"'/v2/fake/os-keypairs'"
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypair_delete
dedent|''
name|'def'
name|'test_keypair_delete'
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
string|"'/v2/fake/os-keypairs/FAKE'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
DECL|member|test_keypair_delete_not_found
dedent|''
name|'def'
name|'test_keypair_delete_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|db_key_pair_get_not_found
indent|'        '
name|'def'
name|'db_key_pair_get_not_found'
op|'('
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'KeyPairNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_get"'
op|','
nl|'\n'
name|'db_key_pair_get_not_found'
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
string|"'/v2/fake/os-keypairs/WHAT'"
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
name|'print'
name|'res'
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
nl|'\n'
DECL|class|KeypairsXMLSerializerTest
dedent|''
dedent|''
name|'class'
name|'KeypairsXMLSerializerTest'
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
name|'KeypairsXMLSerializerTest'
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
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_serializer
dedent|''
name|'def'
name|'test_default_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'keypair'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'public_key'
op|'='
string|"'fake_public_key'"
op|','
nl|'\n'
name|'private_key'
op|'='
string|"'fake_private_key'"
op|','
nl|'\n'
name|'fingerprint'
op|'='
string|"'fake_fingerprint'"
op|','
nl|'\n'
name|'user_id'
op|'='
string|"'fake_user_id'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'fake_key_name'"
op|')'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'keypairs'
op|'.'
name|'KeypairTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'keypair'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'child'
op|'.'
name|'tag'
name|'in'
name|'exemplar'
op|'['
string|"'keypair'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'child'
op|'.'
name|'text'
op|','
name|'exemplar'
op|'['
string|"'keypair'"
op|']'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_serializer
dedent|''
dedent|''
name|'def'
name|'test_index_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'keypairs'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'keypair'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'key1_name'"
op|','
nl|'\n'
name|'public_key'
op|'='
string|"'key1_key'"
op|','
nl|'\n'
name|'fingerprint'
op|'='
string|"'key1_fingerprint'"
op|')'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'keypair'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'key2_name'"
op|','
nl|'\n'
name|'public_key'
op|'='
string|"'key2_key'"
op|','
nl|'\n'
name|'fingerprint'
op|'='
string|"'key2_fingerprint'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'keypairs'
op|'.'
name|'KeypairsTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'keypairs'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'exemplar'
op|'['
string|"'keypairs'"
op|']'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'idx'
op|','
name|'keypair'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'keypair'"
op|','
name|'keypair'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'kp_data'
op|'='
name|'exemplar'
op|'['
string|"'keypairs'"
op|']'
op|'['
name|'idx'
op|']'
op|'['
string|"'keypair'"
op|']'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'keypair'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'child'
op|'.'
name|'tag'
name|'in'
name|'kp_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'child'
op|'.'
name|'text'
op|','
name|'kp_data'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserializer
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'keypair'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'key_name'"
op|','
nl|'\n'
name|'public_key'
op|'='
string|"'public_key'"
op|')'
op|')'
newline|'\n'
name|'intext'
op|'='
op|'('
string|'"<?xml version=\'1.0\' encoding=\'UTF-8\'?>\\n"'
nl|'\n'
string|"'<keypair><name>key_name</name>'"
nl|'\n'
string|"'<public_key>public_key</public_key></keypair>'"
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'intext'
op|')'
op|'['
string|"'body'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'exemplar'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
