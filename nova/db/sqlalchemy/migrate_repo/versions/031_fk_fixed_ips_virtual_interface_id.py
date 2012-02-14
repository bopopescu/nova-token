begin_unit
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
op|'*'
newline|'\n'
name|'from'
name|'migrate'
name|'import'
op|'*'
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
DECL|variable|meta
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
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
nl|'\n'
comment|'# grab tables'
nl|'\n'
name|'fixed_ips'
op|'='
name|'Table'
op|'('
string|"'fixed_ips'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'virtual_interfaces'
op|'='
name|'Table'
op|'('
string|"'virtual_interfaces'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# add foreignkey if not sqlite'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
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
indent|'            '
name|'ForeignKeyConstraint'
op|'('
name|'columns'
op|'='
op|'['
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'virtual_interface_id'
op|']'
op|','
nl|'\n'
name|'refcolumns'
op|'='
op|'['
name|'virtual_interfaces'
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
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
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
nl|'\n'
comment|'# drop foreignkey if not sqlite'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
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
indent|'            '
name|'ForeignKeyConstraint'
op|'('
name|'columns'
op|'='
op|'['
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'virtual_interface_id'
op|']'
op|','
nl|'\n'
name|'refcolumns'
op|'='
op|'['
name|'virtual_interfaces'
op|'.'
name|'c'
op|'.'
name|'id'
op|']'
op|')'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"foreign key constraint couldn\'t be dropped"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
