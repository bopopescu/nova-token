begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'BigInteger'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Integer'
op|','
name|'String'
op|','
name|'Table'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
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
comment|'# add column:'
nl|'\n'
name|'bw_usage_cache'
op|'='
name|'Table'
op|'('
string|"'bw_usage_cache'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'last_ctr_in'
op|'='
name|'Column'
op|'('
string|"'last_ctr_in'"
op|','
name|'BigInteger'
op|'('
op|')'
op|')'
newline|'\n'
name|'last_ctr_out'
op|'='
name|'Column'
op|'('
string|"'last_ctr_out'"
op|','
name|'BigInteger'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'bw_usage_cache'
op|'.'
name|'create_column'
op|'('
name|'last_ctr_in'
op|')'
newline|'\n'
name|'bw_usage_cache'
op|'.'
name|'create_column'
op|'('
name|'last_ctr_out'
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
nl|'\n'
comment|'# drop column:'
nl|'\n'
name|'bw_usage_cache'
op|'='
name|'Table'
op|'('
string|"'bw_usage_cache'"
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
string|"'mac'"
op|','
name|'String'
op|'('
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'uuid'"
op|','
name|'String'
op|'('
number|'36'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'start_period'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'last_refreshed'"
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
string|"'bw_in'"
op|','
name|'BigInteger'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'bw_out'"
op|','
name|'BigInteger'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'last_ctr_in'"
op|','
name|'BigInteger'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'last_ctr_out'"
op|','
name|'BigInteger'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'extend_existing'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'bw_usage_cache'
op|'.'
name|'drop_column'
op|'('
string|"'last_ctr_in'"
op|')'
newline|'\n'
name|'bw_usage_cache'
op|'.'
name|'drop_column'
op|'('
string|"'last_ctr_out'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
