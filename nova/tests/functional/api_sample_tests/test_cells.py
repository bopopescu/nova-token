begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
name|'import'
name|'range'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'state'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
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
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsSampleJsonTest
name|'class'
name|'CellsSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-cells"'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'CellsSampleJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.cells.Cells'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.cell_capacities.Cell_capacities'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# db_check_interval < 0 makes cells manager always hit the DB'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable'
op|'='
name|'True'
op|','
name|'db_check_interval'
op|'='
op|'-'
number|'1'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'super'
op|'('
name|'CellsSampleJsonTest'
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
name|'cells'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'cells'"
op|','
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_stub_cells'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_cells
dedent|''
name|'def'
name|'_stub_cells'
op|'('
name|'self'
op|','
name|'num_cells'
op|'='
number|'5'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cell_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'cells_next_id'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|function|_fake_cell_get_all
name|'def'
name|'_fake_cell_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'cell_list'
newline|'\n'
nl|'\n'
DECL|function|_fake_cell_get
dedent|''
name|'def'
name|'_fake_cell_get'
op|'('
name|'inst'
op|','
name|'context'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'cell_list'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'cell'
op|'['
string|"'name'"
op|']'
op|'=='
name|'cell_name'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'cell'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'CellNotFound'
op|'('
name|'cell_name'
op|'='
name|'cell_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'num_cells'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'='
name|'models'
op|'.'
name|'Cell'
op|'('
op|')'
newline|'\n'
name|'our_id'
op|'='
name|'self'
op|'.'
name|'cells_next_id'
newline|'\n'
name|'self'
op|'.'
name|'cells_next_id'
op|'+='
number|'1'
newline|'\n'
name|'cell'
op|'.'
name|'update'
op|'('
op|'{'
string|"'id'"
op|':'
name|'our_id'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'cell%s'"
op|'%'
name|'our_id'
op|','
nl|'\n'
string|"'transport_url'"
op|':'
string|"'rabbit://username%s@/'"
op|'%'
name|'our_id'
op|','
nl|'\n'
string|"'is_parent'"
op|':'
name|'our_id'
op|'%'
number|'2'
op|'=='
number|'0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cell_list'
op|'.'
name|'append'
op|'('
name|'cell'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.cell_get_all'"
op|','
name|'_fake_cell_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.cells.rpcapi.CellsAPI.cell_get'"
op|','
name|'_fake_cell_get'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cells_empty_list
dedent|''
name|'def'
name|'test_cells_empty_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Override this'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stub_cells'
op|'('
name|'num_cells'
op|'='
number|'0'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-cells'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'cells-list-empty-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cells_list
dedent|''
name|'def'
name|'test_cells_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-cells'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'cells-list-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cells_get
dedent|''
name|'def'
name|'test_cells_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-cells/cell3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'cells-get-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cell_capacity
dedent|''
name|'def'
name|'test_get_cell_capacity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_cell_capacity'
op|'('
op|')'
newline|'\n'
name|'state_manager'
op|'='
name|'state'
op|'.'
name|'CellStateManager'
op|'('
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
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-cells/%s/capacities'"
op|'%'
nl|'\n'
name|'my_state'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'cells-capacities-resp'"
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_cells_capacity
dedent|''
name|'def'
name|'test_get_all_cells_capacity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_cell_capacity'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-cells/capacities'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'cells-capacities-resp'"
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_mock_cell_capacity
dedent|''
name|'def'
name|'_mock_cell_capacity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
op|'{'
string|'"ram_free"'
op|':'
nl|'\n'
op|'{'
string|'"units_by_mb"'
op|':'
op|'{'
string|'"8192"'
op|':'
number|'0'
op|','
string|'"512"'
op|':'
number|'13'
op|','
nl|'\n'
string|'"4096"'
op|':'
number|'1'
op|','
string|'"2048"'
op|':'
number|'3'
op|','
string|'"16384"'
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
string|'"total_mb"'
op|':'
number|'7680'
op|'}'
op|','
nl|'\n'
string|'"disk_free"'
op|':'
nl|'\n'
op|'{'
string|'"units_by_mb"'
op|':'
op|'{'
string|'"81920"'
op|':'
number|'11'
op|','
string|'"20480"'
op|':'
number|'46'
op|','
nl|'\n'
string|'"40960"'
op|':'
number|'23'
op|','
string|'"163840"'
op|':'
number|'5'
op|','
string|'"0"'
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
string|'"total_mb"'
op|':'
number|'1052672'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'goc_mock'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'goc_mock'
op|'.'
name|'return_value'
op|'='
name|'response'
newline|'\n'
name|'self'
op|'.'
name|'cells'
op|'.'
name|'manager'
op|'.'
name|'state_manager'
op|'.'
name|'get_our_capacities'
op|'='
name|'goc_mock'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
