begin_unit
comment|'# Copyright 2012 OpenStack LLC.'
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
name|'sqlalchemy'
name|'import'
name|'String'
op|','
name|'Column'
op|','
name|'MetaData'
op|','
name|'Table'
op|','
name|'delete'
op|','
name|'select'
newline|'\n'
name|'from'
name|'migrate'
op|'.'
name|'changeset'
name|'import'
name|'UniqueConstraint'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
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
name|'dialect'
op|'='
name|'migrate_engine'
op|'.'
name|'url'
op|'.'
name|'get_dialect'
op|'('
op|')'
op|'.'
name|'name'
newline|'\n'
nl|'\n'
name|'aggregates'
op|'='
name|'Table'
op|'('
string|"'aggregates'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'aggregate_metadata'
op|'='
name|'Table'
op|'('
string|"'aggregate_metadata'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'record_list'
op|'='
name|'list'
op|'('
name|'aggregates'
op|'.'
name|'select'
op|'('
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'rec'
name|'in'
name|'record_list'
op|':'
newline|'\n'
indent|'        '
name|'row'
op|'='
name|'aggregate_metadata'
op|'.'
name|'insert'
op|'('
op|')'
newline|'\n'
name|'row'
op|'.'
name|'execute'
op|'('
op|'{'
string|"'created_at'"
op|':'
name|'rec'
op|'['
string|"'created_at'"
op|']'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'rec'
op|'['
string|"'updated_at'"
op|']'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'rec'
op|'['
string|"'deleted_at'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'rec'
op|'['
string|"'deleted'"
op|']'
op|','
nl|'\n'
string|"'key'"
op|':'
string|"'operational_state'"
op|','
nl|'\n'
string|"'value'"
op|':'
name|'rec'
op|'['
string|"'operational_state'"
op|']'
op|','
nl|'\n'
string|"'aggregate_id'"
op|':'
name|'rec'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'aggregates'
op|'.'
name|'drop_column'
op|'('
string|"'operational_state'"
op|')'
newline|'\n'
nl|'\n'
name|'aggregate_hosts'
op|'='
name|'Table'
op|'('
string|"'aggregate_hosts'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'dialect'
op|'.'
name|'startswith'
op|'('
string|"'sqlite'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_hosts'
op|'.'
name|'c'
op|'.'
name|'host'
op|'.'
name|'alter'
op|'('
name|'unique'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'dialect'
op|'.'
name|'startswith'
op|'('
string|"'postgres'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ucon'
op|'='
name|'UniqueConstraint'
op|'('
string|"'host'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'aggregate_hosts_host_key'"
op|','
nl|'\n'
name|'table'
op|'='
name|'aggregate_hosts'
op|')'
newline|'\n'
name|'ucon'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'col'
op|'='
name|'aggregate_hosts'
op|'.'
name|'c'
op|'.'
name|'host'
newline|'\n'
name|'UniqueConstraint'
op|'('
name|'col'
op|','
name|'name'
op|'='
string|"'host'"
op|')'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
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
name|'aggregates'
op|'='
name|'Table'
op|'('
string|"'aggregates'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'aggregate_metadata'
op|'='
name|'Table'
op|'('
string|"'aggregate_metadata'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'operational_state'
op|'='
name|'Column'
op|'('
string|"'operational_state'"
op|','
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
name|'aggregates'
op|'.'
name|'create_column'
op|'('
name|'operational_state'
op|')'
newline|'\n'
name|'aggregates'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'values'
op|'('
name|'operational_state'
op|'='
name|'select'
op|'('
nl|'\n'
op|'['
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'value'
op|']'
op|')'
op|'.'
name|'where'
op|'('
name|'aggregates'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
nl|'\n'
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'aggregate_id'
name|'and'
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'key'
op|'=='
nl|'\n'
string|"'operational_state'"
op|')'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
name|'delete'
op|'('
name|'aggregate_metadata'
op|','
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'key'
op|'=='
string|"'operational_state'"
op|')'
newline|'\n'
name|'aggregates'
op|'.'
name|'c'
op|'.'
name|'operational_state'
op|'.'
name|'alter'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
newline|'\n'
name|'aggregate_hosts'
op|'='
name|'Table'
op|'('
string|"'aggregate_hosts'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'aggregate_hosts'
op|'.'
name|'c'
op|'.'
name|'host'
op|'.'
name|'alter'
op|'('
name|'unique'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
