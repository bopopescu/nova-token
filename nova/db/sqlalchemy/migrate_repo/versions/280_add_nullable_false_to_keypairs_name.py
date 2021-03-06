begin_unit
comment|'# Copyright 2015 Intel Corporation'
nl|'\n'
comment|'# All Rights Reserved'
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
name|'migrate'
op|'.'
name|'changeset'
name|'import'
name|'UniqueConstraint'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Table'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Function enforces non-null value for keypairs name field."""'
newline|'\n'
name|'meta'
op|'='
name|'MetaData'
op|'('
name|'bind'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
name|'key_pairs'
op|'='
name|'Table'
op|'('
string|"'key_pairs'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note: Since we are altering name field, this constraint on name needs to'
nl|'\n'
comment|'# first be dropped before we can alter name. We then re-create the same'
nl|'\n'
comment|'# constraint. It was first added in 216_havana.py so no need to remove'
nl|'\n'
comment|'# constraint on downgrade.'
nl|'\n'
name|'UniqueConstraint'
op|'('
string|"'user_id'"
op|','
string|"'name'"
op|','
string|"'deleted'"
op|','
name|'table'
op|'='
name|'key_pairs'
op|','
nl|'\n'
name|'name'
op|'='
string|"'uniq_key_pairs0user_id0name0deleted'"
op|')'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'key_pairs'
op|'.'
name|'c'
op|'.'
name|'name'
op|'.'
name|'alter'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'UniqueConstraint'
op|'('
string|"'user_id'"
op|','
string|"'name'"
op|','
string|"'deleted'"
op|','
name|'table'
op|'='
name|'key_pairs'
op|','
nl|'\n'
name|'name'
op|'='
string|"'uniq_key_pairs0user_id0name0deleted'"
op|')'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
