begin_unit
comment|'# Copyright (c) 2013 Rackspace Hosting'
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
string|'"""\nTests For CellStateManager\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_COMPUTES
name|'FAKE_COMPUTES'
op|'='
op|'['
nl|'\n'
op|'('
string|"'host1'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
number|'1024'
op|','
number|'100'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'host3'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'1024'
op|','
number|'100'
op|')'
op|','
nl|'\n'
op|'('
string|"'host4'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'300'
op|','
number|'30'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_COMPUTES_N_TO_ONE
name|'FAKE_COMPUTES_N_TO_ONE'
op|'='
op|'['
nl|'\n'
op|'('
string|"'host1'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
string|"'host1'"
op|','
number|'1024'
op|','
number|'100'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'1024'
op|','
number|'100'
op|')'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'300'
op|','
number|'30'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_SERVICES
name|'FAKE_SERVICES'
op|'='
op|'['
nl|'\n'
op|'('
string|"'host1'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
string|"'host3'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
string|"'host4'"
op|','
number|'3600'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(alaski): It's important to have multiple types that end up having the"
nl|'\n'
comment|'# same memory and disk requirements.  So two types need the same first value,'
nl|'\n'
comment|'# and two need the second and third values to add up to the same thing.'
nl|'\n'
DECL|variable|FAKE_ITYPES
name|'FAKE_ITYPES'
op|'='
op|'['
nl|'\n'
op|'('
number|'0'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
number|'50'
op|','
number|'12'
op|','
number|'13'
op|')'
op|','
nl|'\n'
op|'('
number|'50'
op|','
number|'2'
op|','
number|'4'
op|')'
op|','
nl|'\n'
op|'('
number|'10'
op|','
number|'20'
op|','
number|'5'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_fake_node
name|'def'
name|'_create_fake_node'
op|'('
name|'host'
op|','
name|'total_mem'
op|','
name|'total_disk'
op|','
name|'free_mem'
op|','
name|'free_disk'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'memory_mb'
op|'='
name|'total_mem'
op|','
nl|'\n'
name|'local_gb'
op|'='
name|'total_disk'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
name|'free_mem'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
name|'free_disk'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|_fake_service_get_all_by_binary
name|'def'
name|'_fake_service_get_all_by_binary'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
DECL|function|_node
indent|'    '
name|'def'
name|'_node'
op|'('
name|'host'
op|','
name|'total_mem'
op|','
name|'total_disk'
op|','
name|'free_mem'
op|','
name|'free_disk'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'return'
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
name|'forced_down'
op|'='
name|'False'
op|','
nl|'\n'
name|'last_seen_up'
op|'='
name|'now'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'_node'
op|'('
op|'*'
name|'fake'
op|')'
name|'for'
name|'fake'
name|'in'
name|'FAKE_COMPUTES'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|_fake_service_get_all_by_binary_nodedown
name|'def'
name|'_fake_service_get_all_by_binary_nodedown'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
DECL|function|_service
indent|'    '
name|'def'
name|'_service'
op|'('
name|'host'
op|','
name|'noupdate_sec'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'last_seen'
op|'='
name|'now'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'noupdate_sec'
op|')'
newline|'\n'
name|'return'
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
name|'forced_down'
op|'='
name|'False'
op|','
nl|'\n'
name|'last_seen_up'
op|'='
name|'last_seen'
op|','
nl|'\n'
name|'binary'
op|'='
name|'binary'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'_service'
op|'('
op|'*'
name|'fake'
op|')'
name|'for'
name|'fake'
name|'in'
name|'FAKE_SERVICES'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|_fake_compute_node_get_all
name|'def'
name|'_fake_compute_node_get_all'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'_create_fake_node'
op|'('
op|'*'
name|'fake'
op|')'
name|'for'
name|'fake'
name|'in'
name|'FAKE_COMPUTES'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|_fake_compute_node_n_to_one_get_all
name|'def'
name|'_fake_compute_node_n_to_one_get_all'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'_create_fake_node'
op|'('
op|'*'
name|'fake'
op|')'
name|'for'
name|'fake'
name|'in'
name|'FAKE_COMPUTES_N_TO_ONE'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_cell_get_all
dedent|''
name|'def'
name|'_fake_cell_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_instance_type_all
dedent|''
name|'def'
name|'_fake_instance_type_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
DECL|function|_type
indent|'    '
name|'def'
name|'_type'
op|'('
name|'mem'
op|','
name|'root'
op|','
name|'eph'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'root_gb'"
op|':'
name|'root'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'eph'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'mem'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'_type'
op|'('
op|'*'
name|'fake'
op|')'
name|'for'
name|'fake'
name|'in'
name|'FAKE_ITYPES'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCellsStateManager
dedent|''
name|'class'
name|'TestCellsStateManager'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestCellsStateManager'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'objects'
op|'.'
name|'ComputeNodeList'
op|','
string|"'get_all'"
op|','
nl|'\n'
name|'_fake_compute_node_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'objects'
op|'.'
name|'ServiceList'
op|','
string|"'get_by_binary'"
op|','
nl|'\n'
name|'_fake_service_get_all_by_binary'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.flavor_get_all'"
op|','
name|'_fake_instance_type_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.cell_get_all'"
op|','
name|'_fake_cell_get_all'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cells_config_not_found
dedent|''
name|'def'
name|'test_cells_config_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'cells_config'
op|'='
string|"'no_such_file_exists.conf'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'e'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'cfg'
op|'.'
name|'ConfigFilesNotFoundError'
op|','
nl|'\n'
name|'state'
op|'.'
name|'CellStateManager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'no_such_file_exists.conf'"
op|']'
op|','
name|'e'
op|'.'
name|'config_files'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'cfg'
op|'.'
name|'ConfigOpts'
op|','
string|"'find_file'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'read_cached_file'"
op|')'
newline|'\n'
DECL|member|test_filemanager_returned
name|'def'
name|'test_filemanager_returned'
op|'('
name|'self'
op|','
name|'mock_read_cached_file'
op|','
name|'mock_find_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_find_file'
op|'.'
name|'return_value'
op|'='
string|'"/etc/nova/cells.json"'
newline|'\n'
name|'mock_read_cached_file'
op|'.'
name|'return_value'
op|'='
op|'('
name|'False'
op|','
name|'six'
op|'.'
name|'StringIO'
op|'('
string|"'{}'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'cells_config'
op|'='
string|"'cells.json'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'manager'
op|'='
name|'state'
op|'.'
name|'CellStateManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'manager'
op|','
nl|'\n'
name|'state'
op|'.'
name|'CellStateManagerFile'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CellsUpdateUnsupported'
op|','
nl|'\n'
name|'manager'
op|'.'
name|'cell_create'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CellsUpdateUnsupported'
op|','
nl|'\n'
name|'manager'
op|'.'
name|'cell_update'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CellsUpdateUnsupported'
op|','
nl|'\n'
name|'manager'
op|'.'
name|'cell_delete'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dbmanager_returned
dedent|''
name|'def'
name|'test_dbmanager_returned'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'state'
op|'.'
name|'CellStateManager'
op|'('
op|')'
op|','
nl|'\n'
name|'state'
op|'.'
name|'CellStateManagerDB'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_no_reserve
dedent|''
name|'def'
name|'test_capacity_no_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# utilize entire cell'
nl|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'0.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'3'
op|']'
op|')'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_disk'
op|'='
number|'1024'
op|'*'
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'4'
op|']'
op|')'
nl|'\n'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'units'
op|'='
name|'cell_free_ram'
op|'//'
number|'50'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'50'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'sz'
op|'='
number|'25'
op|'*'
number|'1024'
newline|'\n'
name|'units'
op|'='
number|'5'
comment|'# 4 on host 3, 1 on host4'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
name|'str'
op|'('
name|'sz'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_full_reserve
dedent|''
name|'def'
name|'test_capacity_full_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# reserve the entire cell. (utilize zero percent)'
nl|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'100.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'3'
op|']'
op|')'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_disk'
op|'='
number|'1024'
op|'*'
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'4'
op|']'
op|')'
nl|'\n'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'50'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'sz'
op|'='
number|'25'
op|'*'
number|'1024'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
name|'str'
op|'('
name|'sz'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_part_reserve
dedent|''
name|'def'
name|'test_capacity_part_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# utilize half the cell's free capacity"
nl|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'50.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'3'
op|']'
op|')'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_disk'
op|'='
number|'1024'
op|'*'
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'4'
op|']'
op|')'
nl|'\n'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'units'
op|'='
number|'10'
comment|'# 10 from host 3'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'50'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'sz'
op|'='
number|'25'
op|'*'
number|'1024'
newline|'\n'
name|'units'
op|'='
number|'2'
comment|'# 2 on host 3'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
name|'str'
op|'('
name|'sz'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_state_manager
dedent|''
name|'def'
name|'_get_state_manager'
op|'('
name|'self'
op|','
name|'reserve_percent'
op|'='
number|'0.0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'reserve_percent'
op|'='
name|'reserve_percent'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'return'
name|'state'
op|'.'
name|'CellStateManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_capacity
dedent|''
name|'def'
name|'_capacity'
op|'('
name|'self'
op|','
name|'reserve_percent'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'state_manager'
op|'='
name|'self'
op|'.'
name|'_get_state_manager'
op|'('
name|'reserve_percent'
op|')'
newline|'\n'
name|'my_state'
op|'='
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
name|'return'
name|'my_state'
op|'.'
name|'capacities'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCellsStateManagerNToOne
dedent|''
dedent|''
name|'class'
name|'TestCellsStateManagerNToOne'
op|'('
name|'TestCellsStateManager'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestCellsStateManagerNToOne'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'objects'
op|'.'
name|'ComputeNodeList'
op|','
string|"'get_all'"
op|','
nl|'\n'
name|'_fake_compute_node_n_to_one_get_all'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_part_reserve
dedent|''
name|'def'
name|'test_capacity_part_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# utilize half the cell's free capacity"
nl|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'50.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'3'
op|']'
op|')'
nl|'\n'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES_N_TO_ONE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_disk'
op|'='
op|'('
number|'1024'
op|'*'
nl|'\n'
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'4'
op|']'
op|')'
nl|'\n'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES_N_TO_ONE'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'units'
op|'='
number|'6'
comment|'# 6 from host 2'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'50'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'sz'
op|'='
number|'25'
op|'*'
number|'1024'
newline|'\n'
name|'units'
op|'='
number|'1'
comment|'# 1 on host 2'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
name|'str'
op|'('
name|'sz'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCellsStateManagerNodeDown
dedent|''
dedent|''
name|'class'
name|'TestCellsStateManagerNodeDown'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestCellsStateManagerNodeDown'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|','
nl|'\n'
name|'_fake_compute_node_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.objects.ServiceList.get_by_binary'"
op|','
nl|'\n'
name|'_fake_service_get_all_by_binary_nodedown'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.flavor_get_all'"
op|','
name|'_fake_instance_type_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.cell_get_all'"
op|','
name|'_fake_cell_get_all'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_no_reserve_nodedown
dedent|''
name|'def'
name|'test_capacity_no_reserve_nodedown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'0.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'3'
op|']'
op|')'
nl|'\n'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'free_disk'
op|'='
name|'sum'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'compute'
op|'['
number|'4'
op|']'
op|')'
nl|'\n'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'cell_free_disk'
op|'='
number|'1024'
op|'*'
name|'free_disk'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_state_manager
dedent|''
name|'def'
name|'_get_state_manager'
op|'('
name|'self'
op|','
name|'reserve_percent'
op|'='
number|'0.0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'reserve_percent'
op|'='
name|'reserve_percent'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'return'
name|'state'
op|'.'
name|'CellStateManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_capacity
dedent|''
name|'def'
name|'_capacity'
op|'('
name|'self'
op|','
name|'reserve_percent'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'state_manager'
op|'='
name|'self'
op|'.'
name|'_get_state_manager'
op|'('
name|'reserve_percent'
op|')'
newline|'\n'
name|'my_state'
op|'='
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
name|'return'
name|'my_state'
op|'.'
name|'capacities'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCellStateManagerException
dedent|''
dedent|''
name|'class'
name|'TestCellStateManagerException'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'time'
op|','
string|"'sleep'"
op|')'
newline|'\n'
DECL|member|test_init_db_error
name|'def'
name|'test_init_db_error'
op|'('
name|'self'
op|','
name|'mock_sleep'
op|')'
op|':'
newline|'\n'
DECL|class|TestCellStateManagerDB
indent|'        '
name|'class'
name|'TestCellStateManagerDB'
op|'('
name|'state'
op|'.'
name|'CellStateManagerDB'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_cell_data_sync'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_cell_data_sync'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'db_exc'
op|'.'
name|'DBError'
op|'('
op|')'
op|','
op|'['
op|']'
op|']'
newline|'\n'
name|'super'
op|'('
name|'TestCellStateManagerDB'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'test'
op|'='
name|'TestCellStateManagerDB'
op|'('
op|')'
newline|'\n'
name|'mock_sleep'
op|'.'
name|'assert_called_once_with'
op|'('
number|'30'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'test'
op|'.'
name|'_cell_data_sync'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCellsGetCapacity
dedent|''
dedent|''
name|'class'
name|'TestCellsGetCapacity'
op|'('
name|'TestCellsStateManager'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestCellsGetCapacity'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'capacities'
op|'='
op|'{'
string|'"ram_free"'
op|':'
number|'1234'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'state_manager'
op|'='
name|'self'
op|'.'
name|'_get_state_manager'
op|'('
op|')'
newline|'\n'
name|'cell'
op|'='
name|'models'
op|'.'
name|'Cell'
op|'('
name|'name'
op|'='
string|'"cell_name"'
op|')'
newline|'\n'
name|'other_cell'
op|'='
name|'models'
op|'.'
name|'Cell'
op|'('
name|'name'
op|'='
string|'"other_cell_name"'
op|')'
newline|'\n'
name|'cell'
op|'.'
name|'capacities'
op|'='
name|'self'
op|'.'
name|'capacities'
newline|'\n'
name|'other_cell'
op|'.'
name|'capacities'
op|'='
name|'self'
op|'.'
name|'capacities'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'state_manager'
op|','
string|"'child_cells'"
op|','
nl|'\n'
op|'{'
string|'"cell_name"'
op|':'
name|'cell'
op|','
nl|'\n'
string|'"other_cell_name"'
op|':'
name|'other_cell'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cell_capacity_for_all_cells
dedent|''
name|'def'
name|'test_get_cell_capacity_for_all_cells'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'my_cell_state'
op|','
string|"'capacities'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'capacities'
op|')'
newline|'\n'
name|'capacities'
op|'='
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_capacities'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|'"ram_free"'
op|':'
number|'3702'
op|'}'
op|','
name|'capacities'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cell_capacity_for_the_parent_cell
dedent|''
name|'def'
name|'test_get_cell_capacity_for_the_parent_cell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'my_cell_state'
op|','
string|"'capacities'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'capacities'
op|')'
newline|'\n'
name|'capacities'
op|'='
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_capacities'
op|'('
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'my_cell_state'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|'"ram_free"'
op|':'
number|'3702'
op|'}'
op|','
name|'capacities'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cell_capacity_for_a_cell
dedent|''
name|'def'
name|'test_get_cell_capacity_for_a_cell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'capacities'
op|','
nl|'\n'
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_capacities'
op|'('
name|'cell_name'
op|'='
string|'"cell_name"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cell_capacity_for_non_existing_cell
dedent|''
name|'def'
name|'test_get_cell_capacity_for_non_existing_cell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CellNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_capacities'
op|','
nl|'\n'
name|'cell_name'
op|'='
string|'"invalid_cell_name"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCellStateManager
dedent|''
dedent|''
name|'class'
name|'FakeCellStateManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'called'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_cell_data_sync
dedent|''
name|'def'
name|'_cell_data_sync'
op|'('
name|'self'
op|','
name|'force'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'called'
op|'.'
name|'append'
op|'('
op|'('
string|"'_cell_data_sync'"
op|','
name|'force'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSyncDecorators
dedent|''
dedent|''
name|'class'
name|'TestSyncDecorators'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_sync_before
indent|'    '
name|'def'
name|'test_sync_before'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'FakeCellStateManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|test
name|'def'
name|'test'
op|'('
name|'inst'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'manager'
op|','
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
op|','
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dict'
op|'('
name|'a'
op|'='
number|'4'
op|','
name|'b'
op|'='
number|'5'
op|','
name|'c'
op|'='
number|'6'
op|')'
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
string|"'result'"
newline|'\n'
dedent|''
name|'wrapper'
op|'='
name|'state'
op|'.'
name|'sync_before'
op|'('
name|'test'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'wrapper'
op|'('
name|'manager'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
name|'a'
op|'='
number|'4'
op|','
name|'b'
op|'='
number|'5'
op|','
name|'c'
op|'='
number|'6'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'result'"
op|','
name|'result'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'('
string|"'_cell_data_sync'"
op|','
name|'False'
op|')'
op|']'
op|','
name|'manager'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_sync_after
dedent|''
name|'def'
name|'test_sync_after'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'FakeCellStateManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|test
name|'def'
name|'test'
op|'('
name|'inst'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'manager'
op|','
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
op|','
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dict'
op|'('
name|'a'
op|'='
number|'4'
op|','
name|'b'
op|'='
number|'5'
op|','
name|'c'
op|'='
number|'6'
op|')'
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
string|"'result'"
newline|'\n'
dedent|''
name|'wrapper'
op|'='
name|'state'
op|'.'
name|'sync_after'
op|'('
name|'test'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'wrapper'
op|'('
name|'manager'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
name|'a'
op|'='
number|'4'
op|','
name|'b'
op|'='
number|'5'
op|','
name|'c'
op|'='
number|'6'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'result'"
op|','
name|'result'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'('
string|"'_cell_data_sync'"
op|','
name|'True'
op|')'
op|']'
op|','
name|'manager'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
