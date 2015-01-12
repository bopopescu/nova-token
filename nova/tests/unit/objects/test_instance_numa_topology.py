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
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
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
nl|'\n'
DECL|variable|fake_instance_uuid
name|'fake_instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|fake_obj_numa_topology
name|'fake_obj_numa_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
DECL|variable|instance_uuid
name|'instance_uuid'
op|'='
name|'fake_instance_uuid'
op|','
nl|'\n'
DECL|variable|cells
name|'cells'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'0'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
name|'pagesize'
op|'='
number|'2048'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
name|'pagesize'
op|'='
number|'2048'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|fake_numa_topology
name|'fake_numa_topology'
op|'='
name|'fake_obj_numa_topology'
op|'.'
name|'_to_dict'
op|'('
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
name|'fake_instance_uuid'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'fake_obj_numa_topology'
op|'.'
name|'_to_json'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|fake_old_db_topology
name|'fake_old_db_topology'
op|'='
name|'dict'
op|'('
name|'fake_db_topology'
op|')'
comment|'# copy'
newline|'\n'
name|'fake_old_db_topology'
op|'['
string|"'numa_topology'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'fake_numa_topology'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fake_obj_numa_topology
name|'def'
name|'get_fake_obj_numa_topology'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fake_obj_numa_topology_cpy'
op|'='
name|'fake_obj_numa_topology'
op|'.'
name|'obj_clone'
op|'('
op|')'
newline|'\n'
name|'fake_obj_numa_topology_cpy'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'return'
name|'fake_obj_numa_topology_cpy'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceNUMATopology
dedent|''
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
name|'get_fake_obj_numa_topology'
op|'('
name|'self'
op|'.'
name|'context'
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
string|"'nova.db.instance_extra_update_by_uuid'"
op|')'
newline|'\n'
DECL|member|test_save
name|'def'
name|'test_save'
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
name|'get_fake_obj_numa_topology'
op|'('
name|'self'
op|'.'
name|'context'
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
name|'_save'
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
DECL|member|_test_get_by_instance_uuid
dedent|''
name|'def'
name|'_test_get_by_instance_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'fake_obj_numa_topology'
op|'['
string|"'cells'"
op|']'
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
name|'id'
op|','
name|'obj_cell'
op|'.'
name|'id'
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
name|'self'
op|'.'
name|'_test_get_by_instance_uuid'
op|'('
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
DECL|member|test_get_by_instance_uuid_old
name|'def'
name|'test_get_by_instance_uuid_old'
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
name|'fake_old_db_topology'
newline|'\n'
name|'self'
op|'.'
name|'_test_get_by_instance_uuid'
op|'('
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
DECL|member|test_siblings
dedent|''
name|'def'
name|'test_siblings'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'topo'
op|'='
name|'objects'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'sockets'
op|'='
number|'1'
op|','
name|'cores'
op|'='
number|'3'
op|','
name|'threads'
op|'='
number|'0'
op|')'
newline|'\n'
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'topology'
op|'='
name|'topo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'inst_cell'
op|'.'
name|'siblings'
op|')'
newline|'\n'
nl|'\n'
comment|'# One thread actually means no threads'
nl|'\n'
name|'topo'
op|'='
name|'objects'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'sockets'
op|'='
number|'1'
op|','
name|'cores'
op|'='
number|'3'
op|','
name|'threads'
op|'='
number|'1'
op|')'
newline|'\n'
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'cpu_topology'
op|'='
name|'topo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'inst_cell'
op|'.'
name|'siblings'
op|')'
newline|'\n'
nl|'\n'
name|'topo'
op|'='
name|'objects'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'sockets'
op|'='
number|'1'
op|','
name|'cores'
op|'='
number|'2'
op|','
name|'threads'
op|'='
number|'2'
op|')'
newline|'\n'
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|')'
op|','
name|'cpu_topology'
op|'='
name|'topo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|']'
op|')'
op|','
name|'set'
op|'('
op|'['
number|'2'
op|','
number|'3'
op|']'
op|')'
op|']'
op|','
name|'inst_cell'
op|'.'
name|'siblings'
op|')'
newline|'\n'
nl|'\n'
name|'topo'
op|'='
name|'objects'
op|'.'
name|'VirtCPUTopology'
op|'('
name|'sockets'
op|'='
number|'1'
op|','
name|'cores'
op|'='
number|'1'
op|','
name|'threads'
op|'='
number|'4'
op|')'
newline|'\n'
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|')'
op|','
name|'cpu_topology'
op|'='
name|'topo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|')'
op|']'
op|','
name|'inst_cell'
op|'.'
name|'siblings'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pin
dedent|''
name|'def'
name|'test_pin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|')'
op|','
nl|'\n'
name|'cpu_pinning'
op|'='
name|'None'
op|')'
newline|'\n'
name|'inst_cell'
op|'.'
name|'pin'
op|'('
number|'0'
op|','
number|'14'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
number|'0'
op|':'
number|'14'
op|'}'
op|','
name|'inst_cell'
op|'.'
name|'cpu_pinning'
op|')'
newline|'\n'
name|'inst_cell'
op|'.'
name|'pin'
op|'('
number|'12'
op|','
number|'14'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
number|'0'
op|':'
number|'14'
op|'}'
op|','
name|'inst_cell'
op|'.'
name|'cpu_pinning'
op|')'
newline|'\n'
name|'inst_cell'
op|'.'
name|'pin'
op|'('
number|'1'
op|','
number|'16'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
number|'0'
op|':'
number|'14'
op|','
number|'1'
op|':'
number|'16'
op|'}'
op|','
name|'inst_cell'
op|'.'
name|'cpu_pinning'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pin_vcpus
dedent|''
name|'def'
name|'test_pin_vcpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|')'
op|','
nl|'\n'
name|'cpu_pinning'
op|'='
name|'None'
op|')'
newline|'\n'
name|'inst_cell'
op|'.'
name|'pin_vcpus'
op|'('
op|'('
number|'0'
op|','
number|'14'
op|')'
op|','
op|'('
number|'1'
op|','
number|'15'
op|')'
op|','
op|'('
number|'2'
op|','
number|'16'
op|')'
op|','
op|'('
number|'3'
op|','
number|'17'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
number|'0'
op|':'
number|'14'
op|','
number|'1'
op|':'
number|'15'
op|','
number|'2'
op|':'
number|'16'
op|','
number|'3'
op|':'
number|'17'
op|'}'
op|','
name|'inst_cell'
op|'.'
name|'cpu_pinning'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_behavior
dedent|''
name|'def'
name|'test_default_behavior'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'inst_cell'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
op|')'
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
