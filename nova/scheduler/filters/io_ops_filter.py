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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
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
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IoOpsFilter
name|'class'
name|'IoOpsFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filter out hosts with too many concurrent I/O operations."""'
newline|'\n'
nl|'\n'
DECL|member|_get_max_io_ops_per_host
name|'def'
name|'_get_max_io_ops_per_host'
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
name|'return'
name|'CONF'
op|'.'
name|'max_io_ops_per_host'
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
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Use information about current vm and task states collected from\n        compute node statistics to decide whether to filter.\n        """'
newline|'\n'
name|'num_io_ops'
op|'='
name|'host_state'
op|'.'
name|'num_io_ops'
newline|'\n'
name|'max_io_ops'
op|'='
name|'self'
op|'.'
name|'_get_max_io_ops_per_host'
op|'('
nl|'\n'
name|'host_state'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'passes'
op|'='
name|'num_io_ops'
op|'<'
name|'max_io_ops'
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
string|'"%(host_state)s fails I/O ops check: Max IOs per host "'
nl|'\n'
string|'"is set to %(max_io_ops)s"'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'max_io_ops'"
op|':'
name|'max_io_ops'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'passes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregateIoOpsFilter
dedent|''
dedent|''
name|'class'
name|'AggregateIoOpsFilter'
op|'('
name|'IoOpsFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AggregateIoOpsFilter with per-aggregate the max io operations.\n\n    Fall back to global max_io_ops_per_host if no per-aggregate setting found.\n    """'
newline|'\n'
nl|'\n'
DECL|member|_get_max_io_ops_per_host
name|'def'
name|'_get_max_io_ops_per_host'
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
string|"'max_io_ops_per_host'"
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
name|'max_io_ops_per_host'
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
string|'"Could not decode max_io_ops_per_host: \'%s\'"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'value'
op|'='
name|'CONF'
op|'.'
name|'max_io_ops_per_host'
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
