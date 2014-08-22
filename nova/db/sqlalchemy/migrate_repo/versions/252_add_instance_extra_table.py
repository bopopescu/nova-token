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
nl|'\n'
name|'from'
name|'migrate'
name|'import'
name|'ForeignKeyConstraint'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'DateTime'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Index'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Integer'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'String'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Text'
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
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'columns'
op|'='
op|'['
nl|'\n'
op|'('
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'deleted'"
op|','
name|'Integer'
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'id'"
op|','
name|'Integer'
op|')'
op|','
name|'dict'
op|'('
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'instance_uuid'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'36'
op|')'
op|')'
op|','
name|'dict'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'numa_topology'"
op|','
name|'Text'
op|')'
op|','
name|'dict'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'for'
name|'prefix'
name|'in'
op|'('
string|"''"
op|','
string|"'shadow_'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
name|'Table'
op|'('
name|'prefix'
op|'+'
string|"'instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'basename'
op|'='
name|'prefix'
op|'+'
string|"'instance_extra'"
newline|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'has_table'
op|'('
name|'basename'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'_columns'
op|'='
name|'tuple'
op|'('
op|'['
name|'Column'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
nl|'\n'
name|'for'
name|'args'
op|','
name|'kwargs'
name|'in'
name|'columns'
op|']'
op|')'
newline|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'basename'
op|','
name|'meta'
op|','
op|'*'
name|'_columns'
op|','
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
name|'mysql_charset'
op|'='
string|"'utf8'"
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Index'
nl|'\n'
name|'instance_uuid_index'
op|'='
name|'Index'
op|'('
name|'basename'
op|'+'
string|"'_idx'"
op|','
nl|'\n'
name|'table'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'instance_uuid_index'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
comment|'# Foreign key'
nl|'\n'
name|'if'
name|'not'
name|'prefix'
op|':'
newline|'\n'
indent|'            '
name|'fkey_columns'
op|'='
op|'['
name|'table'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|']'
newline|'\n'
name|'fkey_refcolumns'
op|'='
op|'['
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|']'
newline|'\n'
name|'instance_fkey'
op|'='
name|'ForeignKeyConstraint'
op|'('
nl|'\n'
name|'columns'
op|'='
name|'fkey_columns'
op|','
name|'refcolumns'
op|'='
name|'fkey_refcolumns'
op|')'
newline|'\n'
name|'instance_fkey'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
dedent|''
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'for'
name|'prefix'
name|'in'
op|'('
string|"''"
op|','
string|"'shadow_'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
name|'prefix'
op|'+'
string|"'instance_extra'"
newline|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'has_table'
op|'('
name|'table_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_extra'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance_extra'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
