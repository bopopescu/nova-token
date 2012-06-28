begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
name|'nova'
name|'import'
name|'flags'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
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
DECL|variable|cpu_allocation_ratio_opt
name|'cpu_allocation_ratio_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'cpu_allocation_ratio'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'16.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Virtual CPU to Physical CPU allocation ratio'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opt'
op|'('
name|'cpu_allocation_ratio_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CoreFilter
name|'class'
name|'CoreFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""CoreFilter filters based on CPU core utilization."""'
newline|'\n'
nl|'\n'
DECL|member|host_passes
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
name|'host_state'
op|'.'
name|'topic'
op|'!='
string|"'compute'"
name|'or'
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
name|'_'
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
name|'vcpus_total'
op|'='
name|'host_state'
op|'.'
name|'vcpus_total'
op|'*'
name|'FLAGS'
op|'.'
name|'cpu_allocation_ratio'
newline|'\n'
name|'return'
op|'('
name|'vcpus_total'
op|'-'
name|'host_state'
op|'.'
name|'vcpus_used'
op|')'
op|'>='
name|'instance_vcpus'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
