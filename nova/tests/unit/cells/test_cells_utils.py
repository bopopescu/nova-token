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
name|'mock'
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
nl|'\n'
nl|'\n'
DECL|class|CellsUtilsTestCase
name|'class'
name|'CellsUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|function|instance_get_all_by_filters
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
name|'sort_dir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_context'
op|','
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'deleted'"
op|','
name|'sort_key'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'asc'"
op|','
name|'sort_dir'
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
name|'objects'
op|'.'
name|'InstanceList'
op|','
string|"'get_by_filters'"
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
name|'assertEqual'
op|'('
number|'3'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
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
name|'assertEqual'
op|'('
number|'3'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
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
name|'assertEqual'
op|'('
number|'3'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'changes-since'"
op|':'
string|"'fake-updated-since'"
op|'}'
op|','
nl|'\n'
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
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
name|'assertEqual'
op|'('
number|'3'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'call_info'
op|'['
string|"'get_all'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
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
op|','
name|'call_info'
op|'['
string|"'got_filters'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
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
name|'PATH_CELL_SEP'
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
DECL|member|test_add_cell_to_compute_node
dedent|''
name|'def'
name|'test_add_cell_to_compute_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_compute'
op|'='
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'cell_path'
op|'='
string|"'fake_path'"
newline|'\n'
nl|'\n'
name|'proxy'
op|'='
name|'cells_utils'
op|'.'
name|'add_cell_to_compute_node'
op|'('
name|'fake_compute'
op|','
name|'cell_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'proxy'
op|','
name|'cells_utils'
op|'.'
name|'ComputeNodeProxy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell_path'
op|','
number|'1'
op|')'
op|','
name|'proxy'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell_path'
op|','
string|"'fake'"
op|')'
op|','
nl|'\n'
name|'proxy'
op|'.'
name|'host'
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
name|'objects'
op|'.'
name|'Service'
op|','
string|"'obj_load_attr'"
op|')'
newline|'\n'
DECL|member|test_add_cell_to_service_no_compute_node
name|'def'
name|'test_add_cell_to_service_no_compute_node'
op|'('
name|'self'
op|','
name|'mock_get_by_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_service'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'mock_get_by_id'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ServiceNotFound'
op|'('
name|'service_id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'cell_path'
op|'='
string|"'fake_path'"
newline|'\n'
nl|'\n'
name|'proxy'
op|'='
name|'cells_utils'
op|'.'
name|'add_cell_to_service'
op|'('
name|'fake_service'
op|','
name|'cell_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'proxy'
op|','
name|'cells_utils'
op|'.'
name|'ServiceProxy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell_path'
op|','
number|'1'
op|')'
op|','
name|'proxy'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell_path'
op|','
string|"'fake'"
op|')'
op|','
nl|'\n'
name|'proxy'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AttributeError'
op|','
nl|'\n'
name|'getattr'
op|','
name|'proxy'
op|','
string|"'compute_node'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_cell_to_service_with_compute_node
dedent|''
name|'def'
name|'test_add_cell_to_service_with_compute_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_service'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'fake_service'
op|'.'
name|'compute_node'
op|'='
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'cell_path'
op|'='
string|"'fake_path'"
newline|'\n'
nl|'\n'
name|'proxy'
op|'='
name|'cells_utils'
op|'.'
name|'add_cell_to_service'
op|'('
name|'fake_service'
op|','
name|'cell_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'proxy'
op|','
name|'cells_utils'
op|'.'
name|'ServiceProxy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell_path'
op|','
number|'1'
op|')'
op|','
name|'proxy'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
name|'cell_path'
op|','
string|"'fake'"
op|')'
op|','
nl|'\n'
name|'proxy'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AttributeError'
op|','
nl|'\n'
name|'getattr'
op|','
name|'proxy'
op|','
string|"'compute_node'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_proxy_object_serializer_to_primitive
dedent|''
name|'def'
name|'test_proxy_object_serializer_to_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'obj_proxy'
op|'='
name|'cells_utils'
op|'.'
name|'ComputeNodeProxy'
op|'('
name|'obj'
op|','
string|"'fake_path'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'cells_utils'
op|'.'
name|'ProxyObjectSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'primitive'
op|'='
name|'serializer'
op|'.'
name|'serialize_entity'
op|'('
string|"'ctx'"
op|','
name|'obj_proxy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'primitive'
op|','
name|'dict'
op|')'
newline|'\n'
name|'class_name'
op|'='
name|'primitive'
op|'.'
name|'pop'
op|'('
string|"'cell_proxy.class_name'"
op|')'
newline|'\n'
name|'cell_path'
op|'='
name|'primitive'
op|'.'
name|'pop'
op|'('
string|"'cell_proxy.cell_path'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ComputeNodeProxy'"
op|','
name|'class_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake_path'"
op|','
name|'cell_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_proxy_object_serializer_from_primitive
dedent|''
name|'def'
name|'test_proxy_object_serializer_from_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'cells_utils'
op|'.'
name|'ProxyObjectSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Recreating the primitive by hand to isolate the test for only'
nl|'\n'
comment|'# the deserializing method'
nl|'\n'
name|'primitive'
op|'='
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'primitive'
op|'['
string|"'cell_proxy.class_name'"
op|']'
op|'='
string|"'ComputeNodeProxy'"
newline|'\n'
name|'primitive'
op|'['
string|"'cell_proxy.cell_path'"
op|']'
op|'='
string|"'fake_path'"
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'serializer'
op|'.'
name|'deserialize_entity'
op|'('
string|"'ctx'"
op|','
name|'primitive'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'result'
op|','
name|'cells_utils'
op|'.'
name|'ComputeNodeProxy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
nl|'\n'
name|'result'
op|'.'
name|'_obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake_path'"
op|','
name|'result'
op|'.'
name|'_cell_path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
