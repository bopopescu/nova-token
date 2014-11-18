begin_unit
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
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
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
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'hardware'
newline|'\n'
nl|'\n'
DECL|variable|fake_numa_topology
name|'fake_numa_topology'
op|'='
name|'hardware'
op|'.'
name|'VirtNUMAInstanceTopology'
op|'('
nl|'\n'
DECL|variable|cells
name|'cells'
op|'='
op|'['
name|'hardware'
op|'.'
name|'VirtNUMATopologyCellInstance'
op|'('
nl|'\n'
number|'0'
op|','
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
number|'512'
op|','
number|'2048'
op|')'
op|','
nl|'\n'
name|'hardware'
op|'.'
name|'VirtNUMATopologyCellInstance'
op|'('
nl|'\n'
number|'1'
op|','
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
number|'512'
op|','
number|'2048'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|fake_db_topology
name|'fake_db_topology'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'fake_numa_topology'
op|'.'
name|'to_json'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceNUMATopology
name|'class'
name|'_TestInstanceNUMATopology'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_update_by_uuid'"
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'mock_update'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'topo_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'.'
name|'obj_from_topology'
op|'('
nl|'\n'
name|'fake_numa_topology'
op|')'
newline|'\n'
name|'topo_obj'
op|'.'
name|'instance_uuid'
op|'='
name|'fake_db_topology'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
name|'topo_obj'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'mock_update'
op|'.'
name|'call_args_list'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid
name|'def'
name|'test_get_by_instance_uuid'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'fake_db_topology'
newline|'\n'
name|'numa_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'.'
name|'get_by_instance_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'fake_db_topology'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_db_topology'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
name|'numa_topology'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'for'
name|'obj_cell'
op|','
name|'topo_cell'
name|'in'
name|'zip'
op|'('
nl|'\n'
name|'numa_topology'
op|'.'
name|'cells'
op|','
name|'fake_numa_topology'
op|'.'
name|'cells'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'obj_cell'
op|','
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'topo_cell'
op|'.'
name|'cpuset'
op|','
name|'obj_cell'
op|'.'
name|'cpuset'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'topo_cell'
op|'.'
name|'memory'
op|','
name|'obj_cell'
op|'.'
name|'memory'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'topo_cell'
op|'.'
name|'pagesize'
op|','
name|'obj_cell'
op|'.'
name|'pagesize'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid_missing
name|'def'
name|'test_get_by_instance_uuid_missing'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NumaTopologyNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'.'
name|'get_by_instance_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake_uuid'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceNUMATopology'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceNUMATopology
name|'_TestInstanceNUMATopology'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestInstanceNUMATopologyRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestInstanceNUMATopologyRemote
name|'_TestInstanceNUMATopology'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
