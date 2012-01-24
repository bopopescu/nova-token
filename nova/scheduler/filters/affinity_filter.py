begin_unit
comment|'# Copyright 2012, Piston Cloud Computing, Inc.'
nl|'\n'
comment|'# Copyright 2012, OpenStack LLC.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'abstract_filter'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AffinityFilter
name|'class'
name|'AffinityFilter'
op|'('
name|'abstract_filter'
op|'.'
name|'AbstractHostFilter'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_affinity_host
dedent|''
name|'def'
name|'_affinity_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|'['
string|"'host'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DifferentHostFilter
dedent|''
dedent|''
name|'class'
name|'DifferentHostFilter'
op|'('
name|'AffinityFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Schedule the instance on a different host from a set of instances.'''"
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
name|'context'
op|'='
name|'filter_properties'
op|'['
string|"'context'"
op|']'
newline|'\n'
name|'scheduler_hints'
op|'='
name|'filter_properties'
op|'['
string|"'scheduler_hints'"
op|']'
newline|'\n'
name|'me'
op|'='
name|'host_state'
op|'.'
name|'host'
newline|'\n'
nl|'\n'
name|'affinity_uuids'
op|'='
name|'scheduler_hints'
op|'.'
name|'get'
op|'('
string|"'different_host'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'affinity_uuids'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'not'
name|'any'
op|'('
op|'['
name|'i'
name|'for'
name|'i'
nl|'\n'
name|'in'
name|'affinity_uuids'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_affinity_host'
op|'('
name|'context'
op|','
name|'i'
op|')'
op|'=='
name|'me'
op|']'
op|')'
newline|'\n'
comment|'# With no different_host key'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SameHostFilter
dedent|''
dedent|''
name|'class'
name|'SameHostFilter'
op|'('
name|'AffinityFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Schedule the instance on the same host as another instance in a set of\n    of instances.\n    '''"
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
name|'context'
op|'='
name|'filter_properties'
op|'['
string|"'context'"
op|']'
newline|'\n'
name|'scheduler_hints'
op|'='
name|'filter_properties'
op|'['
string|"'scheduler_hints'"
op|']'
newline|'\n'
name|'me'
op|'='
name|'host_state'
op|'.'
name|'host'
newline|'\n'
nl|'\n'
name|'affinity_uuids'
op|'='
name|'scheduler_hints'
op|'.'
name|'get'
op|'('
string|"'same_host'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'affinity_uuids'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'any'
op|'('
op|'['
name|'i'
name|'for'
name|'i'
nl|'\n'
name|'in'
name|'affinity_uuids'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_affinity_host'
op|'('
name|'context'
op|','
name|'i'
op|')'
op|'=='
name|'me'
op|']'
op|')'
newline|'\n'
comment|'# With no same_host key'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleCIDRAffinityFilter
dedent|''
dedent|''
name|'class'
name|'SimpleCIDRAffinityFilter'
op|'('
name|'AffinityFilter'
op|')'
op|':'
newline|'\n'
DECL|member|host_passes
indent|'    '
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
name|'scheduler_hints'
op|'='
name|'filter_properties'
op|'['
string|"'scheduler_hints'"
op|']'
newline|'\n'
nl|'\n'
name|'affinity_cidr'
op|'='
name|'scheduler_hints'
op|'.'
name|'get'
op|'('
string|"'cidr'"
op|','
string|"'/24'"
op|')'
newline|'\n'
name|'affinity_host_addr'
op|'='
name|'scheduler_hints'
op|'.'
name|'get'
op|'('
string|"'build_near_host_ip'"
op|')'
newline|'\n'
name|'if'
name|'affinity_host_addr'
op|':'
newline|'\n'
indent|'            '
name|'affinity_net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'str'
op|'.'
name|'join'
op|'('
string|"''"
op|','
op|'('
name|'affinity_host_addr'
op|','
nl|'\n'
name|'affinity_cidr'
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'my_ip'
op|')'
name|'in'
name|'affinity_net'
newline|'\n'
nl|'\n'
comment|"# We don't have an affinity host address."
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
