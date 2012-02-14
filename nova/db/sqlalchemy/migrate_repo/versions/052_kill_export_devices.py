begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 University of Southern California'
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
name|'Column'
op|','
name|'DateTime'
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
name|'Table'
newline|'\n'
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
comment|'# Table definition'
nl|'\n'
DECL|variable|volumes
name|'volumes'
op|'='
name|'Table'
op|'('
string|"'volumes'"
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
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|export_devices
name|'export_devices'
op|'='
name|'Table'
op|'('
string|"'export_devices'"
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
string|"'shelf_id'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'blade_id'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'volume_id'"
op|','
nl|'\n'
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'volumes.id'"
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
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
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'export_devices'
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
name|'LOG'
op|'.'
name|'info'
op|'('
name|'repr'
op|'('
name|'export_devices'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
string|"'Exception while creating table'"
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'export_devices'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
