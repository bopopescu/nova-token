begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nFakes For Cells tests.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'manager'
name|'as'
name|'cells_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'messaging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'state'
name|'as'
name|'cells_state'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'name'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Fake Cell Hierarchy'
nl|'\n'
DECL|variable|FAKE_TOP_LEVEL_CELL_NAME
name|'FAKE_TOP_LEVEL_CELL_NAME'
op|'='
string|"'api-cell'"
newline|'\n'
DECL|variable|FAKE_CELL_LAYOUT
name|'FAKE_CELL_LAYOUT'
op|'='
op|'['
op|'{'
string|"'child-cell1'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'child-cell2'"
op|':'
op|'['
op|'{'
string|"'grandchild-cell1'"
op|':'
op|'['
op|']'
op|'}'
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'child-cell3'"
op|':'
op|'['
op|'{'
string|"'grandchild-cell2'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'grandchild-cell3'"
op|':'
op|'['
op|']'
op|'}'
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'child-cell4'"
op|':'
op|'['
op|']'
op|'}'
op|']'
newline|'\n'
nl|'\n'
comment|'# build_cell_stub_infos() below will take the above layout and create'
nl|'\n'
comment|'# a fake view of the DB from the perspective of each of the cells.'
nl|'\n'
comment|'# For each cell, a CellStubInfo will be created with this info.'
nl|'\n'
DECL|variable|CELL_NAME_TO_STUB_INFO
name|'CELL_NAME_TO_STUB_INFO'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeDBApi
name|'class'
name|'FakeDBApi'
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
op|','
name|'cell_db_entries'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cell_db_entries'
op|'='
name|'cell_db_entries'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cell_get_all
dedent|''
name|'def'
name|'cell_get_all'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'cell_db_entries'
newline|'\n'
nl|'\n'
DECL|member|compute_node_get_all
dedent|''
name|'def'
name|'compute_node_get_all'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCellsDriver
dedent|''
dedent|''
name|'class'
name|'FakeCellsDriver'
op|'('
name|'driver'
op|'.'
name|'BaseCellsDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCellState
dedent|''
name|'class'
name|'FakeCellState'
op|'('
name|'cells_state'
op|'.'
name|'CellState'
op|')'
op|':'
newline|'\n'
DECL|member|send_message
indent|'    '
name|'def'
name|'send_message'
op|'('
name|'self'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'message_runner'
op|'='
name|'get_message_runner'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'orig_ctxt'
op|'='
name|'message'
op|'.'
name|'ctxt'
newline|'\n'
name|'json_message'
op|'='
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
newline|'\n'
name|'message'
op|'='
name|'message_runner'
op|'.'
name|'message_from_json'
op|'('
name|'json_message'
op|')'
newline|'\n'
comment|'# Restore this so we can use mox and verify same context'
nl|'\n'
name|'message'
op|'.'
name|'ctxt'
op|'='
name|'orig_ctxt'
newline|'\n'
name|'message'
op|'.'
name|'process'
op|'('
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
name|'cells_state'
op|'.'
name|'CellStateManager'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeCellStateManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
nl|'\n'
name|'cell_state_cls'
op|'='
name|'FakeCellState'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCellsManager
dedent|''
dedent|''
name|'class'
name|'FakeCellsManager'
op|'('
name|'cells_manager'
op|'.'
name|'CellsManager'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeCellsManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
nl|'\n'
name|'cell_state_manager'
op|'='
name|'FakeCellStateManager'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellStubInfo
dedent|''
dedent|''
name|'class'
name|'CellStubInfo'
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
op|','
name|'test_case'
op|','
name|'cell_name'
op|','
name|'db_entries'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_case'
op|'='
name|'test_case'
newline|'\n'
name|'self'
op|'.'
name|'cell_name'
op|'='
name|'cell_name'
newline|'\n'
name|'self'
op|'.'
name|'db_entries'
op|'='
name|'db_entries'
newline|'\n'
nl|'\n'
DECL|function|fake_base_init
name|'def'
name|'fake_base_init'
op|'('
name|'_self'
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
name|'_self'
op|'.'
name|'db'
op|'='
name|'FakeDBApi'
op|'('
name|'db_entries'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'test_case'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'base'
op|'.'
name|'Base'
op|','
string|"'__init__'"
op|','
name|'fake_base_init'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cells_manager'
op|'='
name|'FakeCellsManager'
op|'('
op|')'
newline|'\n'
comment|'# Fix the cell name, as it normally uses CONF.cells.name'
nl|'\n'
name|'msg_runner'
op|'='
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'msg_runner'
newline|'\n'
name|'msg_runner'
op|'.'
name|'our_name'
op|'='
name|'self'
op|'.'
name|'cell_name'
newline|'\n'
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'state_manager'
op|'.'
name|'my_cell_state'
op|'.'
name|'name'
op|'='
name|'self'
op|'.'
name|'cell_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_cell_stub_info
dedent|''
dedent|''
name|'def'
name|'_build_cell_stub_info'
op|'('
name|'test_case'
op|','
name|'our_name'
op|','
name|'parent_path'
op|','
name|'children'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'cell_db_entries'
op|'='
op|'['
op|']'
newline|'\n'
name|'cur_db_id'
op|'='
number|'1'
newline|'\n'
name|'sep_char'
op|'='
name|'messaging'
op|'.'
name|'_PATH_CELL_SEP'
newline|'\n'
name|'if'
name|'parent_path'
op|':'
newline|'\n'
indent|'        '
name|'cell_db_entries'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
name|'cur_db_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'parent_path'
op|'.'
name|'split'
op|'('
name|'sep_char'
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|','
nl|'\n'
name|'is_parent'
op|'='
name|'True'
op|','
nl|'\n'
name|'username'
op|'='
string|"'username%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'password'
op|'='
string|"'password%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'rpc_host'
op|'='
string|"'rpc_host%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'rpc_port'
op|'='
string|"'rpc_port%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'rpc_virtual_host'
op|'='
string|"'rpc_vhost%s'"
op|'%'
name|'cur_db_id'
op|')'
op|')'
newline|'\n'
name|'cur_db_id'
op|'+='
number|'1'
newline|'\n'
name|'our_path'
op|'='
name|'parent_path'
op|'+'
name|'sep_char'
op|'+'
name|'our_name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'our_path'
op|'='
name|'our_name'
newline|'\n'
dedent|''
name|'for'
name|'child'
name|'in'
name|'children'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'child_name'
op|','
name|'grandchildren'
name|'in'
name|'child'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_build_cell_stub_info'
op|'('
name|'test_case'
op|','
name|'child_name'
op|','
name|'our_path'
op|','
nl|'\n'
name|'grandchildren'
op|')'
newline|'\n'
name|'cell_entry'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'cur_db_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'child_name'
op|','
nl|'\n'
name|'username'
op|'='
string|"'username%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'password'
op|'='
string|"'password%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'rpc_host'
op|'='
string|"'rpc_host%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'rpc_port'
op|'='
string|"'rpc_port%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'rpc_virtual_host'
op|'='
string|"'rpc_vhost%s'"
op|'%'
name|'cur_db_id'
op|','
nl|'\n'
name|'is_parent'
op|'='
name|'False'
op|')'
newline|'\n'
name|'cell_db_entries'
op|'.'
name|'append'
op|'('
name|'cell_entry'
op|')'
newline|'\n'
name|'cur_db_id'
op|'+='
number|'1'
newline|'\n'
dedent|''
dedent|''
name|'stub_info'
op|'='
name|'CellStubInfo'
op|'('
name|'test_case'
op|','
name|'our_name'
op|','
name|'cell_db_entries'
op|')'
newline|'\n'
name|'CELL_NAME_TO_STUB_INFO'
op|'['
name|'our_name'
op|']'
op|'='
name|'stub_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_cell_stub_infos
dedent|''
name|'def'
name|'_build_cell_stub_infos'
op|'('
name|'test_case'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_build_cell_stub_info'
op|'('
name|'test_case'
op|','
name|'FAKE_TOP_LEVEL_CELL_NAME'
op|','
string|"''"
op|','
nl|'\n'
name|'FAKE_CELL_LAYOUT'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init
dedent|''
name|'def'
name|'init'
op|'('
name|'test_case'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'CELL_NAME_TO_STUB_INFO'
newline|'\n'
name|'test_case'
op|'.'
name|'flags'
op|'('
name|'driver'
op|'='
string|"'nova.tests.cells.fakes.FakeCellsDriver'"
op|','
nl|'\n'
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'CELL_NAME_TO_STUB_INFO'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'_build_cell_stub_infos'
op|'('
name|'test_case'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_cell_stub_info
dedent|''
name|'def'
name|'_get_cell_stub_info'
op|'('
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'CELL_NAME_TO_STUB_INFO'
op|'['
name|'cell_name'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_state_manager
dedent|''
name|'def'
name|'get_state_manager'
op|'('
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_cell_stub_info'
op|'('
name|'cell_name'
op|')'
op|'.'
name|'cells_manager'
op|'.'
name|'state_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_cell_state
dedent|''
name|'def'
name|'get_cell_state'
op|'('
name|'cur_cell_name'
op|','
name|'tgt_cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'state_manager'
op|'='
name|'get_state_manager'
op|'('
name|'cur_cell_name'
op|')'
newline|'\n'
name|'cell'
op|'='
name|'state_manager'
op|'.'
name|'child_cells'
op|'.'
name|'get'
op|'('
name|'tgt_cell_name'
op|')'
newline|'\n'
name|'if'
name|'cell'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'cell'
op|'='
name|'state_manager'
op|'.'
name|'parent_cells'
op|'.'
name|'get'
op|'('
name|'tgt_cell_name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cell'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_cells_manager
dedent|''
name|'def'
name|'get_cells_manager'
op|'('
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_cell_stub_info'
op|'('
name|'cell_name'
op|')'
op|'.'
name|'cells_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_message_runner
dedent|''
name|'def'
name|'get_message_runner'
op|'('
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_cell_stub_info'
op|'('
name|'cell_name'
op|')'
op|'.'
name|'cells_manager'
op|'.'
name|'msg_runner'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_tgt_method
dedent|''
name|'def'
name|'stub_tgt_method'
op|'('
name|'test_case'
op|','
name|'cell_name'
op|','
name|'method_name'
op|','
name|'method'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'msg_runner'
op|'='
name|'get_message_runner'
op|'('
name|'cell_name'
op|')'
newline|'\n'
name|'tgt_msg_methods'
op|'='
name|'msg_runner'
op|'.'
name|'methods_by_type'
op|'['
string|"'targeted'"
op|']'
newline|'\n'
name|'setattr'
op|'('
name|'tgt_msg_methods'
op|','
name|'method_name'
op|','
name|'method'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_bcast_method
dedent|''
name|'def'
name|'stub_bcast_method'
op|'('
name|'test_case'
op|','
name|'cell_name'
op|','
name|'method_name'
op|','
name|'method'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'msg_runner'
op|'='
name|'get_message_runner'
op|'('
name|'cell_name'
op|')'
newline|'\n'
name|'tgt_msg_methods'
op|'='
name|'msg_runner'
op|'.'
name|'methods_by_type'
op|'['
string|"'broadcast'"
op|']'
newline|'\n'
name|'setattr'
op|'('
name|'tgt_msg_methods'
op|','
name|'method_name'
op|','
name|'method'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_bcast_methods
dedent|''
name|'def'
name|'stub_bcast_methods'
op|'('
name|'test_case'
op|','
name|'method_name'
op|','
name|'method'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'cell_name'
name|'in'
name|'CELL_NAME_TO_STUB_INFO'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stub_bcast_method'
op|'('
name|'test_case'
op|','
name|'cell_name'
op|','
name|'method_name'
op|','
name|'method'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
