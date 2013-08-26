begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyPair
name|'class'
name|'KeyPair'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|variable|fields
indent|'    '
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'keypair'
op|','
name|'db_keypair'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'keypair'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'keypair'
op|'['
name|'key'
op|']'
op|'='
name|'db_keypair'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'keypair'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'keypair'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'keypair'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_name
name|'def'
name|'get_by_name'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_keypair'
op|'='
name|'db'
op|'.'
name|'key_pair_get'
op|'('
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_keypair'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|destroy_by_name
name|'def'
name|'destroy_by_name'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'key_pair_destroy'
op|'('
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'db_keypair'
op|'='
name|'db'
op|'.'
name|'key_pair_create'
op|'('
name|'context'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_keypair'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'key_pair_destroy'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyPairList
dedent|''
dedent|''
name|'class'
name|'KeyPairList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_user
name|'def'
name|'get_by_user'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_keypairs'
op|'='
name|'db'
op|'.'
name|'key_pair_get_all_by_user'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'KeyPairList'
op|'('
op|')'
op|','
name|'KeyPair'
op|','
name|'db_keypairs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_count_by_user
name|'def'
name|'get_count_by_user'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'key_pair_count_by_user'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
