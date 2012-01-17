begin_unit
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
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
name|'Boolean'
op|','
name|'String'
op|','
name|'DateTime'
op|','
name|'Integer'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Column'
op|','
name|'ForeignKey'
op|','
name|'Table'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|meta
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|aggregates
name|'aggregates'
op|'='
name|'Table'
op|'('
string|"'aggregates'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|'('
name|'create_constraint'
op|'='
name|'True'
op|','
name|'name'
op|'='
name|'None'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|','
name|'autoincrement'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'name'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
DECL|variable|unique
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'operational_state'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'availability_zone'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|hosts
name|'hosts'
op|'='
name|'Table'
op|'('
string|"'aggregate_hosts'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|'('
name|'create_constraint'
op|'='
name|'True'
op|','
name|'name'
op|'='
name|'None'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
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
string|"'host'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
DECL|variable|unique
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'aggregate_id'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'ForeignKey'
op|'('
string|"'aggregates.id'"
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|metadata
name|'metadata'
op|'='
name|'Table'
op|'('
string|"'aggregate_metadata'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|'('
name|'create_constraint'
op|'='
name|'True'
op|','
name|'name'
op|'='
name|'None'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
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
string|"'aggregate_id'"
op|','
nl|'\n'
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'aggregates.id'"
op|')'
op|','
nl|'\n'
DECL|variable|nullable
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
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
DECL|variable|nullable
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
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|tables
name|'tables'
op|'='
op|'('
name|'aggregates'
op|','
name|'hosts'
op|','
name|'metadata'
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'for'
name|'table'
name|'in'
name|'tables'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
name|'repr'
op|'('
name|'table'
op|')'
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'for'
name|'table'
name|'in'
name|'tables'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
name|'repr'
op|'('
name|'table'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
