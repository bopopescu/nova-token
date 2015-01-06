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
name|'as'
name|'obj_fields'
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
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
name|'class'
name|'InstanceNUMACell'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|InstanceNUMACell
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Add pagesize field'
nl|'\n'
comment|'# Version 1.2: Add cpu_pinning_raw and topology fields'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'obj_fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'cpuset'"
op|':'
name|'obj_fields'
op|'.'
name|'SetOfIntegersField'
op|'('
op|')'
op|','
nl|'\n'
string|"'memory'"
op|':'
name|'obj_fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'pagesize'"
op|':'
name|'obj_fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'cpu_topology'"
op|':'
name|'obj_fields'
op|'.'
name|'ObjectField'
op|'('
string|"'VirtCPUTopology'"
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'cpu_pinning_raw'"
op|':'
name|'obj_fields'
op|'.'
name|'DictOfIntegersField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'cpu_topology'"
op|':'
op|'['
op|'('
string|"'1.2'"
op|','
string|"'1.0'"
op|')'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|cpu_pinning
name|'cpu_pinning'
op|'='
name|'obj_fields'
op|'.'
name|'DictProxyField'
op|'('
string|"'cpu_pinning_raw'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'InstanceNUMACell'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
string|"'pagesize'"
name|'not'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'pagesize'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'pagesize'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'cpu_topology'"
name|'not'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cpu_topology'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'cpu_topology'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'cpu_pinning'"
name|'not'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cpu_pinning'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'cpu_pinning_raw'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__len__
dedent|''
dedent|''
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'cpuset'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_to_dict
dedent|''
name|'def'
name|'_to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sahid): Used as legacy, could be renamed in'
nl|'\n'
comment|'# _legacy_to_dict_ to the future to avoid confusing.'
nl|'\n'
indent|'        '
name|'return'
op|'{'
string|"'cpus'"
op|':'
name|'hardware'
op|'.'
name|'format_cpu_spec'
op|'('
name|'self'
op|'.'
name|'cpuset'
op|','
nl|'\n'
name|'allow_ranges'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'mem'"
op|':'
op|'{'
string|"'total'"
op|':'
name|'self'
op|'.'
name|'memory'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'pagesize'"
op|':'
name|'self'
op|'.'
name|'pagesize'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_from_dict
name|'def'
name|'_from_dict'
op|'('
name|'cls'
op|','
name|'data_dict'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sahid): Used as legacy, could be renamed in'
nl|'\n'
comment|'# _legacy_from_dict_ to the future to avoid confusing.'
nl|'\n'
indent|'        '
name|'cpuset'
op|'='
name|'hardware'
op|'.'
name|'parse_cpu_spec'
op|'('
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'cpus'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'memory'
op|'='
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'mem'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'total'"
op|','
number|'0'
op|')'
newline|'\n'
name|'cell_id'
op|'='
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'pagesize'
op|'='
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'pagesize'"
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'id'
op|'='
name|'cell_id'
op|','
name|'cpuset'
op|'='
name|'cpuset'
op|','
nl|'\n'
name|'memory'
op|'='
name|'memory'
op|','
name|'pagesize'
op|'='
name|'pagesize'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|siblings
name|'def'
name|'siblings'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cpu_list'
op|'='
name|'sorted'
op|'('
name|'list'
op|'('
name|'self'
op|'.'
name|'cpuset'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'threads'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'cpu_topology'
op|':'
newline|'\n'
indent|'            '
name|'threads'
op|'='
name|'self'
op|'.'
name|'cpu_topology'
op|'.'
name|'threads'
newline|'\n'
dedent|''
name|'if'
name|'threads'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'threads'
op|'='
number|'0'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'map'
op|'('
name|'set'
op|','
name|'zip'
op|'('
op|'*'
op|'['
name|'iter'
op|'('
name|'cpu_list'
op|')'
op|']'
op|'*'
name|'threads'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pin
dedent|''
name|'def'
name|'pin'
op|'('
name|'self'
op|','
name|'vcpu'
op|','
name|'pcpu'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'vcpu'
name|'not'
name|'in'
name|'self'
op|'.'
name|'cpuset'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'pinning_dict'
op|'='
name|'self'
op|'.'
name|'cpu_pinning'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'pinning_dict'
op|'['
name|'vcpu'
op|']'
op|'='
name|'pcpu'
newline|'\n'
name|'self'
op|'.'
name|'cpu_pinning'
op|'='
name|'pinning_dict'
newline|'\n'
nl|'\n'
DECL|member|pin_vcpus
dedent|''
name|'def'
name|'pin_vcpus'
op|'('
name|'self'
op|','
op|'*'
name|'cpu_pairs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'vcpu'
op|','
name|'pcpu'
name|'in'
name|'cpu_pairs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'pin'
op|'('
name|'vcpu'
op|','
name|'pcpu'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'class'
name|'InstanceNUMATopology'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|InstanceNUMATopology
name|'base'
op|'.'
name|'NovaObjectDictCompat'
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
name|'obj_fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'obj_fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'cells'"
op|':'
name|'obj_fields'
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
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'cells'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_from_primitive
name|'def'
name|'obj_from_primitive'
op|'('
name|'cls'
op|','
name|'primitive'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'nova_object.name'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'obj_topology'
op|'='
name|'super'
op|'('
name|'InstanceNUMATopology'
op|','
name|'cls'
op|')'
op|'.'
name|'obj_from_primitive'
op|'('
nl|'\n'
name|'primitive'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(sahid): This compatibility code needs to stay until we can'
nl|'\n'
comment|'# guarantee that there are no cases of the old format stored in'
nl|'\n'
comment|'# the database (or forever, if we can never guarantee that).'
nl|'\n'
indent|'            '
name|'obj_topology'
op|'='
name|'InstanceNUMATopology'
op|'.'
name|'_from_dict'
op|'('
name|'primitive'
op|')'
newline|'\n'
name|'obj_topology'
op|'.'
name|'id'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'return'
name|'obj_topology'
newline|'\n'
nl|'\n'
dedent|''
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
name|'primitive'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'db_obj'
op|')'
newline|'\n'
name|'obj_topology'
op|'='
name|'cls'
op|'.'
name|'obj_from_primitive'
op|'('
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'nova_object.name'"
name|'not'
name|'in'
name|'db_obj'
op|':'
newline|'\n'
indent|'            '
name|'obj_topology'
op|'.'
name|'instance_uuid'
op|'='
name|'instance_uuid'
newline|'\n'
comment|'# No benefit to store a list of changed fields'
nl|'\n'
name|'obj_topology'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'obj_topology'
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
name|'self'
op|'.'
name|'_save'
op|'('
name|'context'
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
name|'values'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'self'
op|'.'
name|'_to_json'
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
nl|'\n'
DECL|member|_to_json
dedent|''
name|'def'
name|'_to_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'self'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__len__
dedent|''
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Defined so that boolean testing works the same as for lists."""'
newline|'\n'
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'cells'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_to_dict
dedent|''
name|'def'
name|'_to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sahid): Used as legacy, could be renamed in _legacy_to_dict_'
nl|'\n'
comment|'# in the future to avoid confusing.'
nl|'\n'
indent|'        '
name|'return'
op|'{'
string|"'cells'"
op|':'
op|'['
name|'cell'
op|'.'
name|'_to_dict'
op|'('
op|')'
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'cells'
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_from_dict
name|'def'
name|'_from_dict'
op|'('
name|'cls'
op|','
name|'data_dict'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sahid): Used as legacy, could be renamed in _legacy_from_dict_'
nl|'\n'
comment|'# in the future to avoid confusing.'
nl|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
name|'cells'
op|'='
op|'['
nl|'\n'
name|'InstanceNUMACell'
op|'.'
name|'_from_dict'
op|'('
name|'cell_dict'
op|')'
nl|'\n'
name|'for'
name|'cell_dict'
name|'in'
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'cells'"
op|','
op|'['
op|']'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
