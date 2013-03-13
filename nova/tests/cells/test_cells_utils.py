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
string|'"""\nTests For Cells Utility methods\n"""'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'utils'
name|'as'
name|'cells_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsUtilsTestCase
name|'class'
name|'CellsUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Cells utility methods."""'
newline|'\n'
DECL|member|test_get_instances_to_sync
name|'def'
name|'test_get_instances_to_sync'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_context'
op|'='
string|"'fake_context'"
newline|'\n'
nl|'\n'
name|'call_info'
op|'='
op|'{'
string|"'get_all'"
op|':'
number|'0'
op|','
string|"'shuffle'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|random_shuffle
name|'def'
name|'random_shuffle'
op|'('
name|'_list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|function|instance_get_all_by_filters
dedent|''
name|'def'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
name|'filters'
op|','
nl|'\n'
name|'sort_key'
op|','
name|'sort_order'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'context'
op|','
name|'fake_context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sort_key'
op|','
string|"'deleted'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sort_order'
op|','
string|"'asc'"
op|')'
newline|'\n'
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|'='
name|'filters'
newline|'\n'
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'return'
op|'['
string|"'fake_instance1'"
op|','
string|"'fake_instance2'"
op|','
string|"'fake_instance3'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_all_by_filters'"
op|','
nl|'\n'
name|'instance_get_all_by_filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'random'
op|','
string|"'shuffle'"
op|','
name|'random_shuffle'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'cells_utils'
op|'.'
name|'get_instances_to_sync'
op|'('
name|'fake_context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'instances'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'instances'
op|']'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'cells_utils'
op|'.'
name|'get_instances_to_sync'
op|'('
name|'fake_context'
op|','
nl|'\n'
name|'shuffle'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'instances'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'instances'
op|']'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'cells_utils'
op|'.'
name|'get_instances_to_sync'
op|'('
name|'fake_context'
op|','
nl|'\n'
name|'updated_since'
op|'='
string|"'fake-updated-since'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'instances'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'instances'
op|']'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'changes-since'"
op|':'
string|"'fake-updated-since'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'cells_utils'
op|'.'
name|'get_instances_to_sync'
op|'('
name|'fake_context'
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake-project'"
op|','
nl|'\n'
name|'updated_since'
op|'='
string|"'fake-updated-since'"
op|','
name|'shuffle'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'instances'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'instances'
op|']'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'changes-since'"
op|':'
string|"'fake-updated-since'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake-project'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_split_cell_and_item
dedent|''
name|'def'
name|'test_split_cell_and_item'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
string|"'australia'"
op|','
string|"'queensland'"
op|','
string|"'gold_coast'"
newline|'\n'
name|'cell'
op|'='
name|'cells_utils'
op|'.'
name|'_PATH_CELL_SEP'
op|'.'
name|'join'
op|'('
name|'path'
op|')'
newline|'\n'
name|'item'
op|'='
string|"'host_5'"
newline|'\n'
name|'together'
op|'='
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell'
op|','
name|'item'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells_utils'
op|'.'
name|'_CELL_ITEM_SEP'
op|'.'
name|'join'
op|'('
op|'['
name|'cell'
op|','
name|'item'
op|']'
op|')'
op|','
nl|'\n'
name|'together'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test normal usage'
nl|'\n'
name|'result_cell'
op|','
name|'result_item'
op|'='
name|'cells_utils'
op|'.'
name|'split_cell_and_item'
op|'('
name|'together'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell'
op|','
name|'result_cell'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'item'
op|','
name|'result_item'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test with no cell'
nl|'\n'
name|'cell'
op|'='
name|'None'
newline|'\n'
name|'together'
op|'='
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell'
op|','
name|'item'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'item'
op|','
name|'together'
op|')'
newline|'\n'
name|'print'
name|'together'
newline|'\n'
name|'result_cell'
op|','
name|'result_item'
op|'='
name|'cells_utils'
op|'.'
name|'split_cell_and_item'
op|'('
name|'together'
op|')'
newline|'\n'
name|'print'
name|'result_cell'
op|','
name|'result_item'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell'
op|','
name|'result_cell'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'item'
op|','
name|'result_item'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
