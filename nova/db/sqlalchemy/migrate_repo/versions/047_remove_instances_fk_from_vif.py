begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'Column'
op|','
name|'Integer'
op|','
name|'MetaData'
op|','
name|'Table'
newline|'\n'
name|'from'
name|'migrate'
name|'import'
name|'ForeignKeyConstraint'
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
DECL|variable|instances
name|'instances'
op|'='
name|'Table'
op|'('
string|"'instances'"
op|','
name|'meta'
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|vifs
name|'vifs'
op|'='
name|'Table'
op|'('
string|"'virtual_interfaces'"
op|','
name|'meta'
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
string|"'instance_id'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
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
comment|"# Upgrade operations go here. Don't create your own engine;"
nl|'\n'
comment|'# bind migrate_engine to your metadata'
nl|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
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
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ForeignKeyConstraint'
op|'('
name|'columns'
op|'='
op|'['
name|'vifs'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|']'
op|','
nl|'\n'
name|'refcolumns'
op|'='
op|'['
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|']'
op|')'
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
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE migrations DROP "'
string|'"FOREIGN KEY "'
string|'"`virtual_interfaces_ibfk_2`;"'
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
name|'error'
op|'('
name|'_'
op|'('
string|'"foreign key constraint couldn\'t be removed"'
op|')'
op|')'
newline|'\n'
name|'raise'
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
comment|'# Operations to reverse the above upgrade go here.'
nl|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
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
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ForeignKeyConstraint'
op|'('
name|'columns'
op|'='
op|'['
name|'vifs'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|']'
op|','
nl|'\n'
name|'refcolumns'
op|'='
op|'['
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|']'
op|')'
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
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"foreign key constraint couldn\'t be added"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
