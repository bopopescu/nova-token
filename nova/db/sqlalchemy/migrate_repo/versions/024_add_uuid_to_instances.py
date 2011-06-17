begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'String'
op|','
name|'Table'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|instances
name|'instances'
op|'='
name|'Table'
op|'('
string|'"instances"'
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|'"id"'
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
op|')'
newline|'\n'
DECL|variable|uuid_column
name|'uuid_column'
op|'='
name|'Column'
op|'('
string|'"uuid"'
op|','
name|'String'
op|'('
number|'36'
op|')'
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
name|'instances'
op|'.'
name|'create_column'
op|'('
name|'uuid_column'
op|')'
newline|'\n'
nl|'\n'
name|'rows'
op|'='
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'instances'
op|'.'
name|'select'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'row'
name|'in'
name|'rows'
op|':'
newline|'\n'
indent|'        '
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'utils'
op|'.'
name|'gen_uuid'
op|'('
op|')'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'instances'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'where'
op|'('
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
name|'row'
op|'['
number|'0'
op|']'
op|')'
op|'.'
name|'values'
op|'('
name|'uuid'
op|'='
name|'instance_uuid'
op|')'
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'instances'
op|'.'
name|'drop_column'
op|'('
name|'uuid_column'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
