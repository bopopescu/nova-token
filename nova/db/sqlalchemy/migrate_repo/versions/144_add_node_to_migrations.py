begin_unit
comment|'# Copyright 2012 OpenSmigrations.ck LLC.'
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
name|'and_'
op|','
name|'Index'
op|','
name|'String'
op|','
name|'Column'
op|','
name|'MetaData'
op|','
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
op|'.'
name|'expression'
name|'import'
name|'select'
op|','
name|'update'
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
name|'migrations'
op|'='
name|'Table'
op|'('
string|"'migrations'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# drop old index:'
nl|'\n'
name|'i'
op|'='
name|'_old_index'
op|'('
name|'migrations'
op|')'
newline|'\n'
name|'i'
op|'.'
name|'drop'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
comment|"# add columns.  a node is the same as a compute node's"
nl|'\n'
comment|'# hypervisor hostname:'
nl|'\n'
name|'source_node'
op|'='
name|'Column'
op|'('
string|"'source_node'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'create_column'
op|'('
name|'source_node'
op|')'
newline|'\n'
nl|'\n'
name|'dest_node'
op|'='
name|'Column'
op|'('
string|"'dest_node'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'create_column'
op|'('
name|'dest_node'
op|')'
newline|'\n'
nl|'\n'
comment|'# map compute hosts => list of compute nodes'
nl|'\n'
name|'nodemap'
op|'='
name|'_map_nodes'
op|'('
name|'meta'
op|')'
newline|'\n'
nl|'\n'
comment|'# update migration and instance records with nodes:'
nl|'\n'
name|'_update_nodes'
op|'('
name|'nodemap'
op|','
name|'instances'
op|','
name|'migrations'
op|')'
newline|'\n'
nl|'\n'
comment|'# add new index:'
nl|'\n'
name|'migrations'
op|'='
name|'Table'
op|'('
string|"'migrations'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'_add_new_index'
op|'('
name|'migrations'
op|','
name|'migrate_engine'
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
name|'migrations'
op|'='
name|'Table'
op|'('
string|"'migrations'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# drop new columns:'
nl|'\n'
name|'source_node'
op|'='
name|'Column'
op|'('
string|"'source_node'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'drop_column'
op|'('
name|'source_node'
op|')'
newline|'\n'
nl|'\n'
name|'dest_node'
op|'='
name|'Column'
op|'('
string|"'dest_node'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'drop_column'
op|'('
name|'dest_node'
op|')'
newline|'\n'
nl|'\n'
comment|'# drop new index:'
nl|'\n'
name|'_drop_new_index'
op|'('
name|'migrations'
op|','
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
comment|'# re-add old index:'
nl|'\n'
name|'i'
op|'='
name|'_old_index'
op|'('
name|'migrations'
op|')'
newline|'\n'
name|'i'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_map_nodes
dedent|''
name|'def'
name|'_map_nodes'
op|'('
name|'meta'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Map host to compute node(s) for the purpose of determining which hosts\n    are single vs multi-node.\n    """'
newline|'\n'
nl|'\n'
name|'services'
op|'='
name|'Table'
op|'('
string|"'services'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'c_nodes'
op|'='
name|'Table'
op|'('
string|"'compute_nodes'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'q'
op|'='
name|'select'
op|'('
op|'['
name|'services'
op|'.'
name|'c'
op|'.'
name|'host'
op|','
name|'c_nodes'
op|'.'
name|'c'
op|'.'
name|'hypervisor_hostname'
op|']'
op|','
nl|'\n'
nl|'\n'
name|'whereclause'
op|'='
name|'and_'
op|'('
name|'c_nodes'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|'=='
number|'0'
op|','
nl|'\n'
name|'services'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|'=='
number|'0'
op|')'
op|','
nl|'\n'
nl|'\n'
name|'from_obj'
op|'='
name|'c_nodes'
op|'.'
name|'join'
op|'('
name|'services'
op|','
nl|'\n'
name|'c_nodes'
op|'.'
name|'c'
op|'.'
name|'service_id'
op|'=='
name|'services'
op|'.'
name|'c'
op|'.'
name|'id'
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'nodemap'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'host'
op|','
name|'node'
op|')'
name|'in'
name|'q'
op|'.'
name|'execute'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nodes'
op|'='
name|'nodemap'
op|'.'
name|'setdefault'
op|'('
name|'host'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'nodes'
op|'.'
name|'append'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'nodemap'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_add_new_index
dedent|''
name|'def'
name|'_add_new_index'
op|'('
name|'migrations'
op|','
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
op|'=='
string|'"mysql"'
op|':'
newline|'\n'
comment|'# mysql-specific index by leftmost 100 chars.  (mysql gets angry if the'
nl|'\n'
comment|'# index key length is too long.)'
nl|'\n'
indent|'        '
name|'sql'
op|'='
op|'('
string|'"create index migrations_by_host_nodes_and_status_idx ON "'
nl|'\n'
string|'"migrations (deleted, source_compute(100), dest_compute(100), "'
nl|'\n'
string|'"source_node(100), dest_node(100), status)"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'sql'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'i'
op|'='
name|'Index'
op|'('
string|"'migrations_by_host_nodes_and_status_idx'"
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'source_compute'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'dest_compute'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'source_node'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'dest_node'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'status'
op|')'
newline|'\n'
name|'i'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_drop_new_index
dedent|''
dedent|''
name|'def'
name|'_drop_new_index'
op|'('
name|'migrations'
op|','
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
op|'=='
string|'"mysql"'
op|':'
newline|'\n'
indent|'        '
name|'sql'
op|'='
op|'('
string|'"drop index migrations_by_host_nodes_and_status_idx on "'
nl|'\n'
string|'"migrations"'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'sql'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'i'
op|'='
name|'Index'
op|'('
string|"'migrations_by_host_nodes_and_status_idx'"
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'source_compute'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'dest_compute'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'source_node'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'dest_node'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'status'
op|')'
newline|'\n'
name|'i'
op|'.'
name|'drop'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_old_index
dedent|''
dedent|''
name|'def'
name|'_old_index'
op|'('
name|'migrations'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'i'
op|'='
name|'Index'
op|'('
string|"'migrations_by_host_and_status_idx'"
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'source_compute'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'dest_compute'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'status'
op|')'
newline|'\n'
name|'return'
name|'i'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_update_nodes
dedent|''
name|'def'
name|'_update_nodes'
op|'('
name|'nodemap'
op|','
name|'instances'
op|','
name|'migrations'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""For each migration and matching instance record, update the node columns\n    if the referenced host is single-node.\n\n    Skip updates for multi-node hosts.  In that case, there\'s no way to\n    determine which node on a host the record should be associated with.\n    """'
newline|'\n'
name|'q'
op|'='
name|'select'
op|'('
op|'['
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'id'
op|','
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'source_compute'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'dest_compute'
op|','
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|','
name|'instances'
op|'.'
name|'c'
op|'.'
name|'host'
op|','
nl|'\n'
name|'instances'
op|'.'
name|'c'
op|'.'
name|'node'
op|']'
op|','
nl|'\n'
nl|'\n'
name|'whereclause'
op|'='
name|'and_'
op|'('
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'source_compute'
op|'!='
name|'None'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'dest_compute'
op|'!='
name|'None'
op|','
nl|'\n'
name|'instances'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|'=='
name|'False'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'status'
op|'!='
string|"'reverted'"
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'status'
op|'!='
string|"'error'"
op|')'
op|','
nl|'\n'
nl|'\n'
name|'from_obj'
op|'='
name|'migrations'
op|'.'
name|'join'
op|'('
name|'instances'
op|','
nl|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|'=='
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'q'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
name|'for'
name|'migration_id'
op|','
name|'src'
op|','
name|'dest'
op|','
name|'uuid'
op|','
name|'instance_host'
op|','
name|'instance_node'
name|'in'
name|'result'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'nodes'
op|'='
name|'nodemap'
op|'.'
name|'get'
op|'('
name|'src'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'nodes'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
comment|'# the source host is a single-node, safe to update node'
nl|'\n'
indent|'            '
name|'node'
op|'='
name|'nodes'
op|'['
number|'0'
op|']'
newline|'\n'
name|'values'
op|'['
string|"'source_node'"
op|']'
op|'='
name|'node'
newline|'\n'
nl|'\n'
name|'if'
name|'src'
op|'=='
name|'instance_host'
name|'and'
name|'node'
op|'!='
name|'instance_node'
op|':'
newline|'\n'
indent|'                '
name|'update'
op|'('
name|'instances'
op|')'
op|'.'
name|'where'
op|'('
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|'=='
name|'uuid'
op|')'
op|'.'
name|'values'
op|'('
name|'node'
op|'='
name|'node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'nodes'
op|'='
name|'nodemap'
op|'.'
name|'get'
op|'('
name|'dest'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'nodes'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
comment|'# the dest host is a single-node, safe to update node'
nl|'\n'
indent|'            '
name|'node'
op|'='
name|'nodes'
op|'['
number|'0'
op|']'
newline|'\n'
name|'values'
op|'['
string|"'dest_node'"
op|']'
op|'='
name|'node'
newline|'\n'
nl|'\n'
name|'if'
name|'dest'
op|'=='
name|'instance_host'
name|'and'
name|'node'
op|'!='
name|'instance_node'
op|':'
newline|'\n'
indent|'                '
name|'update'
op|'('
name|'instances'
op|')'
op|'.'
name|'where'
op|'('
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|'=='
name|'uuid'
op|')'
op|'.'
name|'values'
op|'('
name|'node'
op|'='
name|'node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'q'
op|'='
name|'update'
op|'('
name|'migrations'
op|','
nl|'\n'
name|'values'
op|'='
name|'values'
op|','
nl|'\n'
name|'whereclause'
op|'='
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
name|'migration_id'
op|')'
newline|'\n'
name|'q'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
