begin_unit
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
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'db_api'
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
op|'.'
name|'objects'
name|'import'
name|'keypair'
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
name|'import'
name|'fixtures'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyPairObjectTestCase
name|'class'
name|'KeyPairObjectTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|USES_DB_SELF
indent|'    '
name|'USES_DB_SELF'
op|'='
name|'True'
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
name|'KeyPairObjectTestCase'
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
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake-user'"
op|','
string|"'fake-project'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_api_kp
dedent|''
name|'def'
name|'_api_kp'
op|'('
name|'self'
op|','
op|'**'
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kp'
op|'='
name|'objects'
op|'.'
name|'KeyPair'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'name'
op|'='
string|"'fookey'"
op|','
nl|'\n'
name|'fingerprint'
op|'='
string|"'fp'"
op|','
nl|'\n'
name|'public_key'
op|'='
string|"'keydata'"
op|','
nl|'\n'
name|'type'
op|'='
string|"'ssh'"
op|')'
newline|'\n'
name|'kp'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'kp'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'kp'
newline|'\n'
nl|'\n'
DECL|member|_main_kp
dedent|''
name|'def'
name|'_main_kp'
op|'('
name|'self'
op|','
op|'**'
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vals'
op|'='
op|'{'
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
string|"'name'"
op|':'
string|"'fookey'"
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
string|"'fp'"
op|','
nl|'\n'
string|"'public_key'"
op|':'
string|"'keydata'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'ssh'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'vals'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'db_api'
op|'.'
name|'key_pair_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vals'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_in_api
dedent|''
name|'def'
name|'test_create_in_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kp'
op|'='
name|'self'
op|'.'
name|'_api_kp'
op|'('
op|')'
newline|'\n'
name|'keypair'
op|'.'
name|'KeyPair'
op|'.'
name|'_get_from_db'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'kp'
op|'.'
name|'user_id'
op|','
name|'kp'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeypairNotFound'
op|','
nl|'\n'
name|'db_api'
op|'.'
name|'key_pair_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'kp'
op|'.'
name|'user_id'
op|','
name|'kp'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_in_api_duplicate
dedent|''
name|'def'
name|'test_create_in_api_duplicate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeyPairExists'
op|','
name|'self'
op|'.'
name|'_api_kp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_in_api_duplicate_in_main
dedent|''
name|'def'
name|'test_create_in_api_duplicate_in_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_main_kp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeyPairExists'
op|','
name|'self'
op|'.'
name|'_api_kp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_from_api
dedent|''
name|'def'
name|'test_get_from_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'kp'
op|'='
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'get_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'apikey'"
op|','
name|'kp'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_from_main
dedent|''
name|'def'
name|'test_get_from_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'kp'
op|'='
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'get_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'mainkey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'mainkey'"
op|','
name|'kp'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_not_found
dedent|''
name|'def'
name|'test_get_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeypairNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'get_by_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
string|"'nokey'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_in_api
dedent|''
name|'def'
name|'test_destroy_in_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kp'
op|'='
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'kp'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeypairNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'get_by_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
string|"'apikey'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_by_name_in_api
dedent|''
name|'def'
name|'test_destroy_by_name_in_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'destroy_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeypairNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'get_by_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
string|"'apikey'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_in_main
dedent|''
name|'def'
name|'test_destroy_in_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'kp'
op|'='
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'get_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'mainkey'"
op|')'
newline|'\n'
name|'kp'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeypairNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'get_by_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
string|"'mainkey'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_by_name_in_main
dedent|''
name|'def'
name|'test_destroy_by_name_in_main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'objects'
op|'.'
name|'KeyPair'
op|'.'
name|'destroy_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'mainkey'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_user
dedent|''
name|'def'
name|'test_get_by_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'kpl'
op|'='
name|'objects'
op|'.'
name|'KeyPairList'
op|'.'
name|'get_by_user'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
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
number|'2'
op|','
name|'len'
op|'('
name|'kpl'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
string|"'apikey'"
op|','
string|"'mainkey'"
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
name|'x'
op|'.'
name|'name'
name|'for'
name|'x'
name|'in'
name|'kpl'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_count_by_user
dedent|''
name|'def'
name|'test_get_count_by_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_api_kp'
op|'('
name|'name'
op|'='
string|"'apikey'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_main_kp'
op|'('
name|'name'
op|'='
string|"'mainkey'"
op|')'
newline|'\n'
name|'count'
op|'='
name|'objects'
op|'.'
name|'KeyPairList'
op|'.'
name|'get_count_by_user'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
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
number|'2'
op|','
name|'count'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
