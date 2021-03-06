begin_unit
comment|'# Copyright 2014 Red Hat, Inc.'
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
nl|'\n'
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
string|'"""Remove the instance_group_metadata table."""'
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
nl|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'has_table'
op|'('
string|"'instance_group_metadata'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group_metadata'
op|'='
name|'Table'
op|'('
string|"'instance_group_metadata'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'group_metadata'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'migrate_engine'
op|'.'
name|'has_table'
op|'('
string|"'shadow_instance_group_metadata'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'shadow_group_metadata'
op|'='
name|'Table'
op|'('
string|"'shadow_instance_group_metadata'"
op|','
name|'meta'
op|','
nl|'\n'
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'shadow_group_metadata'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
