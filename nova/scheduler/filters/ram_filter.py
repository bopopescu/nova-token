begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
nl|'\n'
comment|'# Copyright (c) 2012 Cloudscaling'
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
DECL|variable|ram_allocation_ratio_opt
name|'ram_allocation_ratio_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|'"ram_allocation_ratio"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1.5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"virtual ram to physical ram allocation ratio"'
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
name|'ram_allocation_ratio_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RamFilter
name|'class'
name|'RamFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ram Filter with over subscription flag"""'
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
string|'"""Only return hosts with sufficient available RAM."""'
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
name|'requested_ram'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'free_ram_mb'
op|'='
name|'host_state'
op|'.'
name|'free_ram_mb'
newline|'\n'
name|'total_usable_ram_mb'
op|'='
name|'host_state'
op|'.'
name|'total_usable_ram_mb'
newline|'\n'
nl|'\n'
name|'oversubscribed_ram_limit_mb'
op|'='
op|'('
name|'total_usable_ram_mb'
op|'*'
nl|'\n'
name|'FLAGS'
op|'.'
name|'ram_allocation_ratio'
op|')'
newline|'\n'
name|'used_ram_mb'
op|'='
name|'total_usable_ram_mb'
op|'-'
name|'free_ram_mb'
newline|'\n'
name|'usable_ram'
op|'='
name|'oversubscribed_ram_limit_mb'
op|'-'
name|'used_ram_mb'
newline|'\n'
name|'if'
name|'not'
name|'usable_ram'
op|'>='
name|'requested_ram'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s does not have %(requested_ram)s MB "'
nl|'\n'
string|'"usable ram, it only has %(usable_ram)s MB usable ram."'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|'# save oversubscribe ram limit so the compute host can verify'
nl|'\n'
comment|'# memory availability on builds:'
nl|'\n'
dedent|''
name|'filter_properties'
op|'['
string|"'memory_mb_limit'"
op|']'
op|'='
name|'oversubscribed_ram_limit_mb'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
