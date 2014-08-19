begin_unit
comment|'#    Copyright 2013 IBM Corp'
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
name|'import'
name|'objects'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeNode
name|'class'
name|'ComputeNode'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added get_by_service_id()'
nl|'\n'
comment|'# Version 1.2: String attributes updated to support unicode'
nl|'\n'
comment|'# Version 1.3: Added stats field'
nl|'\n'
comment|'# Version 1.4: Added host ip field'
nl|'\n'
comment|'# Version 1.5: Added numa_topology field'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.5'"
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
string|"'service_id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'free_ram_mb'"
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
string|"'free_disk_gb'"
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
string|"'current_workload'"
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
string|"'running_vms'"
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
string|"'cpu_info'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'disk_available_least'"
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
string|"'metrics'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'stats'"
op|':'
name|'fields'
op|'.'
name|'DictOfNullableStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'host_ip'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'fields'
op|'.'
name|'StringField'
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
DECL|member|obj_make_compatible
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'5'
op|')'
name|'and'
string|"'numa_topology'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'numa_topology'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'4'
op|')'
name|'and'
string|"'host_ip'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'host_ip'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'3'
op|')'
name|'and'
string|"'stats'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
comment|'# pre 1.3 version does not have a stats field'
nl|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'stats'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'compute'
op|','
name|'db_compute'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'fields'
op|'='
name|'set'
op|'('
name|'compute'
op|'.'
name|'fields'
op|')'
op|'-'
name|'set'
op|'('
op|'['
string|"'stats'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'compute'
op|'['
name|'key'
op|']'
op|'='
name|'db_compute'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'stats'
op|'='
name|'db_compute'
op|'['
string|"'stats'"
op|']'
newline|'\n'
name|'if'
name|'stats'
op|':'
newline|'\n'
indent|'            '
name|'compute'
op|'['
string|"'stats'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'stats'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'compute'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'compute'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'compute'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'compute_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_compute'
op|'='
name|'db'
op|'.'
name|'compute_node_get'
op|'('
name|'context'
op|','
name|'compute_id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_compute'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_service_id
name|'def'
name|'get_by_service_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_compute'
op|'='
name|'db'
op|'.'
name|'compute_node_get_by_service_id'
op|'('
name|'context'
op|','
name|'service_id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_compute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_convert_stats_to_db_format
dedent|''
name|'def'
name|'_convert_stats_to_db_format'
op|'('
name|'self'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stats'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'stats'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'stats'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'stats'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'stats'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_convert_host_ip_to_db_format
dedent|''
dedent|''
name|'def'
name|'_convert_host_ip_to_db_format'
op|'('
name|'self'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_ip'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'host_ip'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'host_ip'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'host_ip'"
op|']'
op|'='
name|'str'
op|'('
name|'host_ip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
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
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_convert_stats_to_db_format'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_convert_host_ip_to_db_format'
op|'('
name|'updates'
op|')'
newline|'\n'
nl|'\n'
name|'db_compute'
op|'='
name|'db'
op|'.'
name|'compute_node_create'
op|'('
name|'context'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_compute'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'prune_stats'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(belliott) ignore prune_stats param, no longer relevant'
nl|'\n'
nl|'\n'
indent|'        '
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_convert_stats_to_db_format'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_convert_host_ip_to_db_format'
op|'('
name|'updates'
op|')'
newline|'\n'
nl|'\n'
name|'db_compute'
op|'='
name|'db'
op|'.'
name|'compute_node_update'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_compute'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'compute_node_delete'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|service
name|'def'
name|'service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'self'
op|','
string|"'_cached_service'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_cached_service'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'service_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_cached_service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeNodeList
dedent|''
dedent|''
name|'class'
name|'ComputeNodeList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'#              ComputeNode <= version 1.2'
nl|'\n'
comment|'# Version 1.1 ComputeNode version 1.3'
nl|'\n'
comment|'# Version 1.2 Add get_by_service()'
nl|'\n'
comment|'# Version 1.3 ComputeNode version 1.4'
nl|'\n'
comment|'# Version 1.4 ComputeNode version 1.5'
nl|'\n'
comment|'# Version 1.5 Add use_slave to get_by_service'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.5'"
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'ComputeNode'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|child_versions
name|'child_versions'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
string|"'1.2'"
op|','
nl|'\n'
comment|'# NOTE(danms): ComputeNode was at 1.2 before we added this'
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.3'"
op|','
nl|'\n'
string|"'1.2'"
op|':'
string|"'1.3'"
op|','
nl|'\n'
string|"'1.3'"
op|':'
string|"'1.4'"
op|','
nl|'\n'
string|"'1.4'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'1.5'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_computes'
op|'='
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'ComputeNode'
op|','
nl|'\n'
name|'db_computes'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_hypervisor
name|'def'
name|'get_by_hypervisor'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'hypervisor_match'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_computes'
op|'='
name|'db'
op|'.'
name|'compute_node_search_by_hypervisor'
op|'('
name|'context'
op|','
nl|'\n'
name|'hypervisor_match'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'ComputeNode'
op|','
nl|'\n'
name|'db_computes'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|_get_by_service
name|'def'
name|'_get_by_service'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service_id'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|','
name|'service_id'
op|','
nl|'\n'
name|'with_compute_node'
op|'='
name|'True'
op|','
nl|'\n'
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'ComputeNode'
op|','
nl|'\n'
name|'db_service'
op|'['
string|"'compute_node'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_by_service
name|'def'
name|'get_by_service'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'_get_by_service'
op|'('
name|'context'
op|','
name|'service'
op|'.'
name|'id'
op|','
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
