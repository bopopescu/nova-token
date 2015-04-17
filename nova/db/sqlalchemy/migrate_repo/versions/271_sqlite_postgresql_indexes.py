begin_unit
comment|'# Copyright 2014 Rackspace Hosting'
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
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|INDEXES
name|'INDEXES'
op|'='
op|'['
nl|'\n'
op|'('
string|"'block_device_mapping'"
op|','
string|"'snapshot_id'"
op|','
op|'['
string|"'snapshot_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'block_device_mapping'"
op|','
string|"'volume_id'"
op|','
op|'['
string|"'volume_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'dns_domains'"
op|','
string|"'dns_domains_project_id_idx'"
op|','
op|'['
string|"'project_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'fixed_ips'"
op|','
string|"'network_id'"
op|','
op|'['
string|"'network_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'fixed_ips'"
op|','
string|"'fixed_ips_instance_uuid_fkey'"
op|','
op|'['
string|"'instance_uuid'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'fixed_ips'"
op|','
string|"'fixed_ips_virtual_interface_id_fkey'"
op|','
nl|'\n'
op|'['
string|"'virtual_interface_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'floating_ips'"
op|','
string|"'fixed_ip_id'"
op|','
op|'['
string|"'fixed_ip_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsi_targets'"
op|','
string|"'iscsi_targets_volume_id_fkey'"
op|','
op|'['
string|"'volume_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'virtual_interfaces'"
op|','
string|"'virtual_interfaces_network_id_idx'"
op|','
nl|'\n'
op|'['
string|"'network_id'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'virtual_interfaces'"
op|','
string|"'virtual_interfaces_instance_uuid_fkey'"
op|','
nl|'\n'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_index_exists
name|'def'
name|'ensure_index_exists'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'index_name'
op|','
name|'column_names'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'utils'
op|'.'
name|'index_exists'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'index_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'add_index'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'index_name'
op|','
name|'column_names'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_index_removed
dedent|''
dedent|''
name|'def'
name|'ensure_index_removed'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'index_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'utils'
op|'.'
name|'index_exists'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'index_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'drop_index'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'index_name'
op|')'
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
string|'"""Add indexes missing on SQLite and PostgreSQL."""'
newline|'\n'
nl|'\n'
comment|'# PostgreSQL and SQLite namespace indexes at the database level, whereas'
nl|'\n'
comment|'# MySQL namespaces indexes at the table level. Unfortunately, some of'
nl|'\n'
comment|'# the missing indexes in PostgreSQL and SQLite have conflicting names'
nl|'\n'
comment|'# that MySQL allowed.'
nl|'\n'
nl|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
name|'in'
op|'('
string|"'sqlite'"
op|','
string|"'postgresql'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'table_name'
op|','
name|'index_name'
op|','
name|'column_names'
name|'in'
name|'INDEXES'
op|':'
newline|'\n'
indent|'            '
name|'ensure_index_exists'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'index_name'
op|','
nl|'\n'
name|'column_names'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'migrate_engine'
op|'.'
name|'name'
op|'=='
string|"'mysql'"
op|':'
newline|'\n'
comment|'# Rename some indexes with conflicting names'
nl|'\n'
indent|'        '
name|'ensure_index_removed'
op|'('
name|'migrate_engine'
op|','
string|"'dns_domains'"
op|','
string|"'project_id'"
op|')'
newline|'\n'
name|'ensure_index_exists'
op|'('
name|'migrate_engine'
op|','
string|"'dns_domains'"
op|','
nl|'\n'
string|"'dns_domains_project_id_idx'"
op|','
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'ensure_index_removed'
op|'('
name|'migrate_engine'
op|','
string|"'virtual_interfaces'"
op|','
nl|'\n'
string|"'network_id'"
op|')'
newline|'\n'
name|'ensure_index_exists'
op|'('
name|'migrate_engine'
op|','
string|"'virtual_interfaces'"
op|','
nl|'\n'
string|"'virtual_interfaces_network_id_idx'"
op|','
nl|'\n'
op|'['
string|"'network_id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
