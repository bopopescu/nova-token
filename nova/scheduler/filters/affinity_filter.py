begin_unit
comment|'# Copyright 2012, Piston Cloud Computing, Inc.'
nl|'\n'
comment|'# Copyright 2012, OpenStack Foundation'
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
name|'netaddr'
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
nl|'\n'
DECL|class|DifferentHostFilter
name|'class'
name|'DifferentHostFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Schedule the instance on a different host from a set of instances.'''"
newline|'\n'
nl|'\n'
comment|"# The hosts the instances are running on doesn't change within a request"
nl|'\n'
DECL|variable|run_filter_once_per_request
name|'run_filter_once_per_request'
op|'='
name|'True'
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
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'affinity_uuids'
op|'='
name|'spec_obj'
op|'.'
name|'get_scheduler_hint'
op|'('
string|"'different_host'"
op|')'
newline|'\n'
name|'if'
name|'affinity_uuids'
op|':'
newline|'\n'
indent|'            '
name|'overlap'
op|'='
name|'utils'
op|'.'
name|'instance_uuids_overlap'
op|'('
name|'host_state'
op|','
name|'affinity_uuids'
op|')'
newline|'\n'
name|'return'
name|'not'
name|'overlap'
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
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Schedule the instance on the same host as another instance in a set of\n    instances.\n    '''"
newline|'\n'
nl|'\n'
comment|"# The hosts the instances are running on doesn't change within a request"
nl|'\n'
DECL|variable|run_filter_once_per_request
name|'run_filter_once_per_request'
op|'='
name|'True'
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
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'affinity_uuids'
op|'='
name|'spec_obj'
op|'.'
name|'get_scheduler_hint'
op|'('
string|"'same_host'"
op|')'
newline|'\n'
name|'if'
name|'affinity_uuids'
name|'and'
name|'host_state'
op|'.'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'overlap'
op|'='
name|'utils'
op|'.'
name|'instance_uuids_overlap'
op|'('
name|'host_state'
op|','
name|'affinity_uuids'
op|')'
newline|'\n'
name|'return'
name|'overlap'
newline|'\n'
comment|'# With no same_host key or no instances'
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
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Schedule the instance on a host with a particular cidr\n    '''"
newline|'\n'
nl|'\n'
comment|"# The address of a host doesn't change within a request"
nl|'\n'
DECL|variable|run_filter_once_per_request
name|'run_filter_once_per_request'
op|'='
name|'True'
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
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'affinity_cidr'
op|'='
name|'spec_obj'
op|'.'
name|'get_scheduler_hint'
op|'('
string|"'cidr'"
op|','
string|"'/24'"
op|')'
newline|'\n'
name|'affinity_host_addr'
op|'='
name|'spec_obj'
op|'.'
name|'get_scheduler_hint'
op|'('
string|"'build_near_host_ip'"
op|')'
newline|'\n'
name|'host_ip'
op|'='
name|'host_state'
op|'.'
name|'host_ip'
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
nl|'\n'
name|'return'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'host_ip'
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
nl|'\n'
nl|'\n'
DECL|class|_GroupAntiAffinityFilter
dedent|''
dedent|''
name|'class'
name|'_GroupAntiAffinityFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Schedule the instance on a different host from a set of group\n    hosts.\n    """'
newline|'\n'
DECL|member|host_passes
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'spec_obj'
op|')'
op|':'
newline|'\n'
comment|"# Only invoke the filter is 'anti-affinity' is configured"
nl|'\n'
indent|'        '
name|'policies'
op|'='
op|'('
name|'spec_obj'
op|'.'
name|'instance_group'
op|'.'
name|'policies'
nl|'\n'
name|'if'
name|'spec_obj'
op|'.'
name|'instance_group'
name|'else'
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'policy_name'
name|'not'
name|'in'
name|'policies'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'group_hosts'
op|'='
op|'('
name|'spec_obj'
op|'.'
name|'instance_group'
op|'.'
name|'hosts'
nl|'\n'
name|'if'
name|'spec_obj'
op|'.'
name|'instance_group'
name|'else'
op|'['
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Group anti affinity: check if %(host)s not "'
nl|'\n'
string|'"in %(configured)s"'
op|','
op|'{'
string|"'host'"
op|':'
name|'host_state'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'configured'"
op|':'
name|'group_hosts'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'group_hosts'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'host_state'
op|'.'
name|'host'
name|'not'
name|'in'
name|'group_hosts'
newline|'\n'
nl|'\n'
comment|'# No groups configured'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupAntiAffinityFilter
dedent|''
dedent|''
name|'class'
name|'ServerGroupAntiAffinityFilter'
op|'('
name|'_GroupAntiAffinityFilter'
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
name|'policy_name'
op|'='
string|"'anti-affinity'"
newline|'\n'
name|'super'
op|'('
name|'ServerGroupAntiAffinityFilter'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_GroupAffinityFilter
dedent|''
dedent|''
name|'class'
name|'_GroupAffinityFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Schedule the instance on to host from a set of group hosts.\n    """'
newline|'\n'
DECL|member|host_passes
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'spec_obj'
op|')'
op|':'
newline|'\n'
comment|"# Only invoke the filter is 'affinity' is configured"
nl|'\n'
indent|'        '
name|'policies'
op|'='
op|'('
name|'spec_obj'
op|'.'
name|'instance_group'
op|'.'
name|'policies'
nl|'\n'
name|'if'
name|'spec_obj'
op|'.'
name|'instance_group'
name|'else'
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'policy_name'
name|'not'
name|'in'
name|'policies'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'group_hosts'
op|'='
op|'('
name|'spec_obj'
op|'.'
name|'instance_group'
op|'.'
name|'hosts'
nl|'\n'
name|'if'
name|'spec_obj'
op|'.'
name|'instance_group'
name|'else'
op|'['
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Group affinity: check if %(host)s in "'
nl|'\n'
string|'"%(configured)s"'
op|','
op|'{'
string|"'host'"
op|':'
name|'host_state'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'configured'"
op|':'
name|'group_hosts'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'group_hosts'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'host_state'
op|'.'
name|'host'
name|'in'
name|'group_hosts'
newline|'\n'
nl|'\n'
comment|'# No groups configured'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupAffinityFilter
dedent|''
dedent|''
name|'class'
name|'ServerGroupAffinityFilter'
op|'('
name|'_GroupAffinityFilter'
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
name|'policy_name'
op|'='
string|"'affinity'"
newline|'\n'
name|'super'
op|'('
name|'ServerGroupAffinityFilter'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
