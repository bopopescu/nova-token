begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright 2011 Isaku Yamahata'
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
name|'MetaData'
op|','
name|'Table'
op|','
name|'Column'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'DateTime'
op|','
name|'Boolean'
op|','
name|'Integer'
op|','
name|'String'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'ForeignKey'
newline|'\n'
name|'from'
name|'nova'
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
comment|"# Upgrade operations go here. Don't create your own engine;"
nl|'\n'
comment|'# bind migrate_engine to your metadata'
nl|'\n'
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
comment|'# load tables for fk'
nl|'\n'
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
name|'volumes'
op|'='
name|'Table'
op|'('
string|"'volumes'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'snapshots'
op|'='
name|'Table'
op|'('
string|"'snapshots'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# New Tables'
nl|'\n'
comment|'#'
nl|'\n'
name|'block_device_mapping'
op|'='
name|'Table'
op|'('
string|"'block_device_mapping'"
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
name|'autoincrement'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'instance_id'"
op|','
nl|'\n'
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'instances.id'"
op|')'
op|','
nl|'\n'
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'device_name'"
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
nl|'\n'
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
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'delete_on_termination'"
op|','
nl|'\n'
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
op|','
nl|'\n'
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'virtual_name'"
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
nl|'\n'
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
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'snapshot_id'"
op|','
nl|'\n'
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'snapshots.id'"
op|')'
op|','
nl|'\n'
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'volume_id'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'ForeignKey'
op|'('
string|"'volumes.id'"
op|')'
op|','
nl|'\n'
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'volume_size'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'no_device'"
op|','
nl|'\n'
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
op|','
nl|'\n'
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'block_device_mapping'
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
name|'block_device_mapping'
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
name|'meta'
op|'.'
name|'drop_all'
op|'('
name|'tables'
op|'='
op|'['
name|'block_device_mapping'
op|']'
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
comment|'# Operations to reverse the above upgrade go here.'
nl|'\n'
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
comment|'# load tables for fk'
nl|'\n'
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
name|'volumes'
op|'='
name|'Table'
op|'('
string|"'volumes'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'snapshots'
op|'='
name|'Table'
op|'('
string|"'snapshots'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'block_device_mapping'
op|'='
name|'Table'
op|'('
string|"'block_device_mapping'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'block_device_mapping'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
