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
name|'oslo_config'
name|'import'
name|'cfg'
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
DECL|member|_get_max_instances_per_host
name|'def'
name|'_get_max_instances_per_host'
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
name|'max_instances_per_host'
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
name|'num_instances'
op|'='
name|'host_state'
op|'.'
name|'num_instances'
newline|'\n'
name|'max_instances'
op|'='
name|'self'
op|'.'
name|'_get_max_instances_per_host'
op|'('
nl|'\n'
name|'host_state'
op|','
name|'filter_properties'
op|')'
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
string|'"%(host_state)s fails num_instances check: Max "'
nl|'\n'
string|'"instances per host is set to %(max_instances)s"'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'max_instances'"
op|':'
name|'max_instances'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'passes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregateNumInstancesFilter
dedent|''
dedent|''
name|'class'
name|'AggregateNumInstancesFilter'
op|'('
name|'NumInstancesFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AggregateNumInstancesFilter with per-aggregate the max num instances.\n\n    Fall back to global max_num_instances_per_host if no per-aggregate setting\n    found.\n    """'
newline|'\n'
nl|'\n'
DECL|member|_get_max_instances_per_host
name|'def'
name|'_get_max_instances_per_host'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
comment|'# TODO(uni): DB query in filter is a performance hit, especially for'
nl|'\n'
comment|'# system with lots of hosts. Will need a general solutnumn here to fix'
nl|'\n'
comment|'# all filters with aggregate DB call things.'
nl|'\n'
indent|'        '
name|'aggregate_vals'
op|'='
name|'utils'
op|'.'
name|'aggregate_values_from_db'
op|'('
nl|'\n'
name|'filter_properties'
op|'['
string|"'context'"
op|']'
op|','
nl|'\n'
name|'host_state'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'max_instances_per_host'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'value'
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
name|'max_instances_per_host'
op|','
name|'cast_to'
op|'='
name|'int'
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
string|'"Could not decode max_instances_per_host: \'%s\'"'
op|')'
op|','
nl|'\n'
name|'e'
op|')'
newline|'\n'
name|'value'
op|'='
name|'CONF'
op|'.'
name|'max_instances_per_host'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
