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
name|'migrate'
op|'.'
name|'changeset'
op|'.'
name|'constraint'
name|'import'
name|'ForeignKeyConstraint'
newline|'\n'
name|'from'
name|'migrate'
name|'import'
name|'UniqueConstraint'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Boolean'
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
name|'Float'
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
name|'flavors'
op|'='
name|'Table'
op|'('
string|"'flavors'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'name'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'memory_mb'"
op|','
name|'Integer'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'vcpus'"
op|','
name|'Integer'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'swap'"
op|','
name|'Integer'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'vcpu_weight'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'flavorid'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'rxtx_factor'"
op|','
name|'Float'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'root_gb'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'ephemeral_gb'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'disabled'"
op|','
name|'Boolean'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'is_public'"
op|','
name|'Boolean'
op|')'
op|','
nl|'\n'
name|'UniqueConstraint'
op|'('
string|'"flavorid"'
op|','
name|'name'
op|'='
string|'"uniq_flavors0flavorid"'
op|')'
op|','
nl|'\n'
name|'UniqueConstraint'
op|'('
string|'"name"'
op|','
name|'name'
op|'='
string|'"uniq_flavors0name"'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
name|'mysql_charset'
op|'='
string|"'utf8'"
nl|'\n'
op|')'
newline|'\n'
name|'flavors'
op|'.'
name|'create'
op|'('
name|'checkfirst'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'flavor_extra_specs'
op|'='
name|'Table'
op|'('
string|"'flavor_extra_specs'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'flavor_id'"
op|','
name|'Integer'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'key'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'value'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'UniqueConstraint'
op|'('
string|"'flavor_id'"
op|','
string|"'key'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'uniq_flavor_extra_specs0flavor_id0key'"
op|')'
op|','
nl|'\n'
name|'ForeignKeyConstraint'
op|'('
name|'columns'
op|'='
op|'['
string|"'flavor_id'"
op|']'
op|','
name|'refcolumns'
op|'='
op|'['
name|'flavors'
op|'.'
name|'c'
op|'.'
name|'id'
op|']'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
name|'mysql_charset'
op|'='
string|"'utf8'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(mriedem): DB2 creates an index when a unique constraint is created'
nl|'\n'
comment|'# so trying to add a second index on the flavor_id/key column will fail'
nl|'\n'
comment|'# with error SQL0605W, so omit the index in the case of DB2.'
nl|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
op|'!='
string|"'ibm_db_sa'"
op|':'
newline|'\n'
indent|'        '
name|'Index'
op|'('
string|"'flavor_extra_specs_flavor_id_key_idx'"
op|','
nl|'\n'
name|'flavor_extra_specs'
op|'.'
name|'c'
op|'.'
name|'flavor_id'
op|','
nl|'\n'
name|'flavor_extra_specs'
op|'.'
name|'c'
op|'.'
name|'key'
op|')'
newline|'\n'
dedent|''
name|'flavor_extra_specs'
op|'.'
name|'create'
op|'('
name|'checkfirst'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'flavor_projects'
op|'='
name|'Table'
op|'('
string|"'flavor_projects'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'flavor_id'"
op|','
name|'Integer'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'project_id'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'UniqueConstraint'
op|'('
string|"'flavor_id'"
op|','
string|"'project_id'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'uniq_flavor_projects0flavor_id0project_id'"
op|')'
op|','
nl|'\n'
name|'ForeignKeyConstraint'
op|'('
name|'columns'
op|'='
op|'['
string|"'flavor_id'"
op|']'
op|','
nl|'\n'
name|'refcolumns'
op|'='
op|'['
name|'flavors'
op|'.'
name|'c'
op|'.'
name|'id'
op|']'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
name|'mysql_charset'
op|'='
string|"'utf8'"
nl|'\n'
op|')'
newline|'\n'
name|'flavor_projects'
op|'.'
name|'create'
op|'('
name|'checkfirst'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
