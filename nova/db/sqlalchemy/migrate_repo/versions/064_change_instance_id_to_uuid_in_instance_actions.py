begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'from'
name|'sqlalchemy'
name|'import'
name|'select'
op|','
name|'Column'
op|','
name|'ForeignKey'
op|','
name|'Integer'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'String'
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
name|'instance_actions'
op|'='
name|'Table'
op|'('
string|"'instance_actions'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instances'
op|'='
name|'Table'
op|'('
string|"'instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'uuid_column'
op|'='
name|'Column'
op|'('
string|"'instance_uuid'"
op|','
name|'String'
op|'('
number|'36'
op|')'
op|')'
newline|'\n'
name|'uuid_column'
op|'.'
name|'create'
op|'('
name|'instance_actions'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'instance_actions'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'values'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'select'
op|'('
nl|'\n'
op|'['
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|']'
op|','
nl|'\n'
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
name|'instance_actions'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|')'
nl|'\n'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'uuid_column'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'dialect'
op|'.'
name|'startswith'
op|'('
string|"'sqlite'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fkeys'
op|'='
name|'list'
op|'('
name|'instance_actions'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|'.'
name|'foreign_keys'
op|')'
newline|'\n'
name|'if'
name|'fkeys'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'fkey_name'
op|'='
name|'fkeys'
op|'['
number|'0'
op|']'
op|'.'
name|'constraint'
op|'.'
name|'name'
newline|'\n'
name|'ForeignKeyConstraint'
op|'('
name|'columns'
op|'='
op|'['
name|'instance_actions'
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
op|','
nl|'\n'
name|'name'
op|'='
name|'fkey_name'
op|')'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
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
dedent|''
dedent|''
dedent|''
name|'instance_actions'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
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
name|'instance_actions'
op|'='
name|'Table'
op|'('
string|"'instance_actions'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instances'
op|'='
name|'Table'
op|'('
string|"'instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'id_column'
op|'='
name|'Column'
op|'('
string|"'instance_id'"
op|','
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'instances.id'"
op|')'
op|')'
newline|'\n'
name|'id_column'
op|'.'
name|'create'
op|'('
name|'instance_actions'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'instance_actions'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'values'
op|'('
nl|'\n'
name|'instance_id'
op|'='
name|'select'
op|'('
nl|'\n'
op|'['
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|']'
op|','
nl|'\n'
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|'=='
name|'instance_actions'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|')'
nl|'\n'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'id_column'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_actions'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
