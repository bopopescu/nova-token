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
name|'MetaData'
op|','
name|'Table'
newline|'\n'
nl|'\n'
DECL|variable|meta
name|'meta'
op|'='
name|'MetaData'
op|'('
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
op|'=='
string|'"mysql"'
op|':'
newline|'\n'
indent|'        '
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE auth_tokens Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE certificates Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE compute_nodes Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE console_pools Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE consoles Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE export_devices Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE fixed_ips Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE floating_ips Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE instance_actions Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE instance_metadata Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE instance_types Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE instances Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE iscsi_targets Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE key_pairs Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE migrate_version Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE migrations Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE networks Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE projects Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE quotas Engine=InnoDB"'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|'"ALTER TABLE security_group_instance_association Engine=InnoDB"'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|'"ALTER TABLE security_group_rules Engine=InnoDB"'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE security_groups Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE services Engine=InnoDB"'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|'"ALTER TABLE user_project_association Engine=InnoDB"'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|'"ALTER TABLE user_project_role_association Engine=InnoDB"'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|'"ALTER TABLE user_role_association Engine=InnoDB"'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE users Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE volumes Engine=InnoDB"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
string|'"ALTER TABLE zones Engine=InnoDB"'
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
dedent|''
endmarker|''
end_unit
