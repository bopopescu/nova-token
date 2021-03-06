begin_unit
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Index'
op|','
name|'MetaData'
op|','
name|'Table'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
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
DECL|function|_get_deleted_expire_index
name|'def'
name|'_get_deleted_expire_index'
op|'('
name|'table'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'members'
op|'='
name|'sorted'
op|'('
op|'['
string|"'deleted'"
op|','
string|"'expire'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'idx'
name|'in'
name|'table'
op|'.'
name|'indexes'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'sorted'
op|'('
name|'idx'
op|'.'
name|'columns'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'=='
name|'members'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'idx'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
dedent|''
dedent|''
dedent|''
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
name|'reservations'
op|'='
name|'Table'
op|'('
string|"'reservations'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'_get_deleted_expire_index'
op|'('
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Skipped adding reservations_deleted_expire_idx '"
nl|'\n'
string|"'because an equivalent index already exists.'"
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
comment|'# Based on expire_reservations query'
nl|'\n'
comment|'# from: nova/db/sqlalchemy/api.py'
nl|'\n'
dedent|''
name|'index'
op|'='
name|'Index'
op|'('
string|"'reservations_deleted_expire_idx'"
op|','
nl|'\n'
name|'reservations'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|','
name|'reservations'
op|'.'
name|'c'
op|'.'
name|'expire'
op|')'
newline|'\n'
nl|'\n'
name|'index'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
