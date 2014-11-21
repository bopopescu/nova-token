begin_unit
comment|'#    Copyright 2014 Red Hat Inc.'
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
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'hardware'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNUMACell
name|'class'
name|'InstanceNUMACell'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Add pagesize field'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'cpuset'"
op|':'
name|'fields'
op|'.'
name|'SetOfIntegersField'
op|'('
op|')'
op|','
nl|'\n'
string|"'memory'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'pagesize'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNUMATopology
dedent|''
name|'class'
name|'InstanceNUMATopology'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Takes into account pagesize'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
comment|"# NOTE(danms): The 'id' field is no longer used and should be"
nl|'\n'
comment|'# removed in the future when convenient'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'cells'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'InstanceNUMACell'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_from_db_obj
name|'def'
name|'obj_from_db_obj'
op|'('
name|'cls'
op|','
name|'instance_uuid'
op|','
name|'db_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'topo'
op|'='
name|'hardware'
op|'.'
name|'VirtNUMAInstanceTopology'
op|'.'
name|'from_json'
op|'('
name|'db_obj'
op|')'
newline|'\n'
name|'obj_topology'
op|'='
name|'cls'
op|'.'
name|'obj_from_topology'
op|'('
name|'topo'
op|')'
newline|'\n'
name|'obj_topology'
op|'.'
name|'instance_uuid'
op|'='
name|'instance_uuid'
newline|'\n'
comment|'# NOTE (ndipanov) not really needed as we never save, but left for'
nl|'\n'
comment|'# consistency'
nl|'\n'
name|'obj_topology'
op|'.'
name|'id'
op|'='
number|'0'
newline|'\n'
name|'obj_topology'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'obj_topology'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_from_topology
name|'def'
name|'obj_from_topology'
op|'('
name|'cls'
op|','
name|'topology'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'topology'
op|','
name|'hardware'
op|'.'
name|'VirtNUMAInstanceTopology'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'obj_from_topology'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'invalid topology class'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'topology'
op|':'
newline|'\n'
indent|'            '
name|'cells'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'topocell'
name|'in'
name|'topology'
op|'.'
name|'cells'
op|':'
newline|'\n'
indent|'                '
name|'cell'
op|'='
name|'InstanceNUMACell'
op|'('
name|'id'
op|'='
name|'topocell'
op|'.'
name|'id'
op|','
name|'cpuset'
op|'='
name|'topocell'
op|'.'
name|'cpuset'
op|','
nl|'\n'
name|'memory'
op|'='
name|'topocell'
op|'.'
name|'memory'
op|','
nl|'\n'
name|'pagesize'
op|'='
name|'topocell'
op|'.'
name|'pagesize'
op|')'
newline|'\n'
name|'cells'
op|'.'
name|'append'
op|'('
name|'cell'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'('
name|'cells'
op|'='
name|'cells'
op|')'
newline|'\n'
nl|'\n'
DECL|member|topology_from_obj
dedent|''
dedent|''
name|'def'
name|'topology_from_obj'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'objcell'
name|'in'
name|'self'
op|'.'
name|'cells'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'='
name|'hardware'
op|'.'
name|'VirtNUMATopologyCellInstance'
op|'('
nl|'\n'
name|'objcell'
op|'.'
name|'id'
op|','
name|'objcell'
op|'.'
name|'cpuset'
op|','
name|'objcell'
op|'.'
name|'memory'
op|','
name|'objcell'
op|'.'
name|'pagesize'
op|')'
newline|'\n'
name|'cells'
op|'.'
name|'append'
op|'('
name|'cell'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'hardware'
op|'.'
name|'VirtNUMAInstanceTopology'
op|'('
name|'cells'
op|'='
name|'cells'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(ndipanov) Remove this method on the major version bump to 2.0'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'topology'
op|'='
name|'self'
op|'.'
name|'topology_from_obj'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'topology'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'values'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'topology'
op|'.'
name|'to_json'
op|'('
op|')'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_extra_update_by_uuid'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(ndipanov): We can't rename create and want to avoid version bump"
nl|'\n'
comment|'# as this needs to be backported to stable so this is not a @remotable'
nl|'\n'
comment|"# That's OK since we only call it from inside Instance.save() which is."
nl|'\n'
DECL|member|_save
dedent|''
name|'def'
name|'_save'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'topology'
op|'='
name|'self'
op|'.'
name|'topology_from_obj'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'topology'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'values'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'topology'
op|'.'
name|'to_json'
op|'('
op|')'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_extra_update_by_uuid'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(ndipanov): We want to avoid version bump'
nl|'\n'
comment|'# as this needs to be backported to stable so this is not a @remotable'
nl|'\n'
comment|"# That's OK since we only call it from inside Instance.save() which is."
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|delete_by_instance_uuid
name|'def'
name|'delete_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_extra_update_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid
name|'def'
name|'get_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_extra'
op|'='
name|'db'
op|'.'
name|'instance_extra_get_by_instance_uuid'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuid'
op|','
name|'columns'
op|'='
op|'['
string|"'numa_topology'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'db_extra'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NumaTopologyNotFound'
op|'('
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'db_extra'
op|'['
string|"'numa_topology'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'obj_from_db_obj'
op|'('
name|'instance_uuid'
op|','
name|'db_extra'
op|'['
string|"'numa_topology'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
