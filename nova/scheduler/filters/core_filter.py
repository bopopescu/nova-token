begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright (c) 2012 Justin Santa Barbara'
nl|'\n'
comment|'#'
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
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
comment|'# TODO(sbauza): Remove the import once all compute nodes are reporting the'
nl|'\n'
comment|'# allocation ratio to the HostState'
nl|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'cpu_allocation_ratio'"
op|','
string|"'nova.compute.resource_tracker'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseCoreFilter
name|'class'
name|'BaseCoreFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_get_cpu_allocation_ratio
indent|'    '
name|'def'
name|'_get_cpu_allocation_ratio'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|host_passes
dedent|''
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if host has sufficient CPU cores."""'
newline|'\n'
name|'instance_type'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'host_state'
op|'.'
name|'vcpus_total'
op|':'
newline|'\n'
comment|'# Fail safe'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"VCPUs not set; assuming CPU collection broken"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_vcpus'
op|'='
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'cpu_allocation_ratio'
op|'='
name|'self'
op|'.'
name|'_get_cpu_allocation_ratio'
op|'('
name|'host_state'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'vcpus_total'
op|'='
name|'host_state'
op|'.'
name|'vcpus_total'
op|'*'
name|'cpu_allocation_ratio'
newline|'\n'
nl|'\n'
comment|'# Only provide a VCPU limit to compute if the virt driver is reporting'
nl|'\n'
comment|'# an accurate count of installed VCPUs. (XenServer driver does not)'
nl|'\n'
name|'if'
name|'vcpus_total'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'host_state'
op|'.'
name|'limits'
op|'['
string|"'vcpu'"
op|']'
op|'='
name|'vcpus_total'
newline|'\n'
nl|'\n'
comment|'# Do not allow an instance to overcommit against itself, only'
nl|'\n'
comment|'# against other instances.'
nl|'\n'
name|'if'
name|'instance_vcpus'
op|'>'
name|'host_state'
op|'.'
name|'vcpus_total'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s does not have %(instance_vcpus)d "'
nl|'\n'
string|'"total cpus before overcommit, it only has %(cpus)d"'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'instance_vcpus'"
op|':'
name|'instance_vcpus'
op|','
nl|'\n'
string|"'cpus'"
op|':'
name|'host_state'
op|'.'
name|'vcpus_total'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'free_vcpus'
op|'='
name|'vcpus_total'
op|'-'
name|'host_state'
op|'.'
name|'vcpus_used'
newline|'\n'
name|'if'
name|'free_vcpus'
op|'<'
name|'instance_vcpus'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s does not have %(instance_vcpus)d "'
nl|'\n'
string|'"usable vcpus, it only has %(free_vcpus)d usable "'
nl|'\n'
string|'"vcpus"'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'instance_vcpus'"
op|':'
name|'instance_vcpus'
op|','
nl|'\n'
string|"'free_vcpus'"
op|':'
name|'free_vcpus'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CoreFilter
dedent|''
dedent|''
name|'class'
name|'CoreFilter'
op|'('
name|'BaseCoreFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""CoreFilter filters based on CPU core utilization."""'
newline|'\n'
nl|'\n'
DECL|member|_get_cpu_allocation_ratio
name|'def'
name|'_get_cpu_allocation_ratio'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'CONF'
op|'.'
name|'cpu_allocation_ratio'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregateCoreFilter
dedent|''
dedent|''
name|'class'
name|'AggregateCoreFilter'
op|'('
name|'BaseCoreFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AggregateCoreFilter with per-aggregate CPU subscription flag.\n\n    Fall back to global cpu_allocation_ratio if no per-aggregate setting found.\n    """'
newline|'\n'
nl|'\n'
DECL|member|_get_cpu_allocation_ratio
name|'def'
name|'_get_cpu_allocation_ratio'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_vals'
op|'='
name|'utils'
op|'.'
name|'aggregate_values_from_key'
op|'('
nl|'\n'
name|'host_state'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ratio'
op|'='
name|'utils'
op|'.'
name|'validate_num_values'
op|'('
nl|'\n'
name|'aggregate_vals'
op|','
name|'CONF'
op|'.'
name|'cpu_allocation_ratio'
op|','
name|'cast_to'
op|'='
name|'float'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Could not decode cpu_allocation_ratio: \'%s\'"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'ratio'
op|'='
name|'CONF'
op|'.'
name|'cpu_allocation_ratio'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'ratio'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
