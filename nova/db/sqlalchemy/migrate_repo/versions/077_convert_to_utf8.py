begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack LLC.'
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
name|'MetaData'
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
comment|'# NOTE (ironcamel): The only table we are not converting to utf8 here is'
nl|'\n'
comment|'# dns_domains. This table has a primary key that is 512 characters wide.'
nl|'\n'
comment|'# When the mysql engine attempts to convert it to utf8, it complains about'
nl|'\n'
comment|'# not supporting key columns larger than 1000.'
nl|'\n'
nl|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
op|'=='
string|'"mysql"'
op|':'
newline|'\n'
indent|'        '
name|'tables'
op|'='
op|'['
nl|'\n'
comment|'# tables that are FK parents, must be converted early'
nl|'\n'
string|'"aggregates"'
op|','
string|'"console_pools"'
op|','
string|'"instance_types"'
op|','
string|'"instances"'
op|','
nl|'\n'
string|'"projects"'
op|','
string|'"security_groups"'
op|','
string|'"sm_backend_config"'
op|','
string|'"sm_flavors"'
op|','
nl|'\n'
string|'"snapshots"'
op|','
string|'"user_project_association"'
op|','
string|'"users"'
op|','
string|'"volume_types"'
op|','
nl|'\n'
string|'"volumes"'
op|','
nl|'\n'
comment|'# those that are children and others later'
nl|'\n'
string|'"agent_builds"'
op|','
string|'"aggregate_hosts"'
op|','
string|'"aggregate_metadata"'
op|','
nl|'\n'
string|'"auth_tokens"'
op|','
string|'"block_device_mapping"'
op|','
string|'"bw_usage_cache"'
op|','
nl|'\n'
string|'"certificates"'
op|','
string|'"compute_nodes"'
op|','
string|'"consoles"'
op|','
string|'"fixed_ips"'
op|','
nl|'\n'
string|'"floating_ips"'
op|','
string|'"instance_actions"'
op|','
string|'"instance_faults"'
op|','
nl|'\n'
string|'"instance_info_caches"'
op|','
string|'"instance_metadata"'
op|','
nl|'\n'
string|'"instance_type_extra_specs"'
op|','
string|'"iscsi_targets"'
op|','
string|'"key_pairs"'
op|','
nl|'\n'
string|'"migrate_version"'
op|','
string|'"migrations"'
op|','
string|'"networks"'
op|','
string|'"provider_fw_rules"'
op|','
nl|'\n'
string|'"quotas"'
op|','
string|'"s3_images"'
op|','
string|'"security_group_instance_association"'
op|','
nl|'\n'
string|'"security_group_rules"'
op|','
string|'"services"'
op|','
string|'"sm_volume"'
op|','
nl|'\n'
string|'"user_project_role_association"'
op|','
string|'"user_role_association"'
op|','
nl|'\n'
string|'"virtual_interfaces"'
op|','
string|'"virtual_storage_arrays"'
op|','
string|'"volume_metadata"'
op|','
nl|'\n'
string|'"volume_type_extra_specs"'
op|','
string|'"zones"'
op|']'
newline|'\n'
name|'sql'
op|'='
string|'"SET foreign_key_checks = 0;"'
newline|'\n'
name|'for'
name|'table'
name|'in'
name|'tables'
op|':'
newline|'\n'
indent|'            '
name|'sql'
op|'+='
string|'"ALTER TABLE %s CONVERT TO CHARACTER SET utf8;"'
op|'%'
name|'table'
newline|'\n'
dedent|''
name|'sql'
op|'+='
string|'"SET foreign_key_checks = 1;"'
newline|'\n'
name|'sql'
op|'+='
string|'"ALTER DATABASE %s DEFAULT CHARACTER SET utf8;"'
op|'%'
name|'migrate_engine'
op|'.'
name|'url'
op|'.'
name|'database'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'sql'
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
comment|'# utf8 tables should be backwards compatible, so lets leave it alone'
nl|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
