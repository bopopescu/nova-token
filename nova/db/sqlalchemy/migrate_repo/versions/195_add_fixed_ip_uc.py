begin_unit
comment|'# Copyright 2013 Mirantis Inc.'
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
comment|'#'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
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
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|UC_NAME
name|'UC_NAME'
op|'='
string|"'uniq_fixed_ips0address0deleted'"
newline|'\n'
DECL|variable|COLUMNS
name|'COLUMNS'
op|'='
op|'('
string|"'address'"
op|','
string|"'deleted'"
op|')'
newline|'\n'
DECL|variable|TABLE_NAME
name|'TABLE_NAME'
op|'='
string|"'fixed_ips'"
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
name|'bind'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
name|'t'
op|'='
name|'Table'
op|'('
name|'TABLE_NAME'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'drop_old_duplicate_entries_from_table'
op|'('
name|'migrate_engine'
op|','
name|'TABLE_NAME'
op|','
nl|'\n'
name|'True'
op|','
op|'*'
name|'COLUMNS'
op|')'
newline|'\n'
name|'uc'
op|'='
name|'UniqueConstraint'
op|'('
op|'*'
name|'COLUMNS'
op|','
name|'table'
op|'='
name|'t'
op|','
name|'name'
op|'='
name|'UC_NAME'
op|')'
newline|'\n'
name|'uc'
op|'.'
name|'create'
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
name|'utils'
op|'.'
name|'drop_unique_constraint'
op|'('
name|'migrate_engine'
op|','
name|'TABLE_NAME'
op|','
name|'UC_NAME'
op|','
op|'*'
name|'COLUMNS'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
