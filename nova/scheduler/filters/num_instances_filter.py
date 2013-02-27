begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
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
DECL|variable|max_instances_per_host_opt
name|'max_instances_per_host_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"max_instances_per_host"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'50'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Ignore hosts that have too many instances"'
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
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'max_instances_per_host_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NumInstancesFilter
name|'class'
name|'NumInstancesFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filter out hosts with too many instances."""'
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
name|'num_instances'
op|'='
name|'host_state'
op|'.'
name|'num_instances'
newline|'\n'
name|'max_instances'
op|'='
name|'CONF'
op|'.'
name|'max_instances_per_host'
newline|'\n'
name|'passes'
op|'='
name|'num_instances'
op|'<'
name|'max_instances'
newline|'\n'
name|'if'
name|'not'
name|'passes'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s fails num_instances check: Max "'
nl|'\n'
string|'"instances per host is set to %(max_instances)s"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'passes'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
