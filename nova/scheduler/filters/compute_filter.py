begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'abstract_filter'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
string|"'nova.scheduler.filter.compute_filter'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeFilter
name|'class'
name|'ComputeFilter'
op|'('
name|'abstract_filter'
op|'.'
name|'AbstractHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""HostFilter hard-coded to work with InstanceType records."""'
newline|'\n'
nl|'\n'
DECL|member|_satisfies_extra_specs
name|'def'
name|'_satisfies_extra_specs'
op|'('
name|'self'
op|','
name|'capabilities'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check that the capabilities provided by the compute service\n        satisfy the extra specs associated with the instance type"""'
newline|'\n'
name|'if'
string|"'extra_specs'"
name|'not'
name|'in'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
comment|'# NOTE(lorinh): For now, we are just checking exact matching on the'
nl|'\n'
comment|'# values. Later on, we want to handle numerical'
nl|'\n'
comment|'# values so we can represent things like number of GPU cards'
nl|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'capabilities'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'None'
op|')'
op|'!='
name|'value'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
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
string|'"""Return a list of hosts that can create instance_type."""'
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
dedent|''
name|'capabilities'
op|'='
name|'host_state'
op|'.'
name|'capabilities'
newline|'\n'
name|'service'
op|'='
name|'host_state'
op|'.'
name|'service'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
name|'or'
name|'service'
op|'['
string|"'disabled'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'capabilities'
op|'.'
name|'get'
op|'('
string|'"enabled"'
op|','
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_satisfies_extra_specs'
op|'('
name|'capabilities'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
