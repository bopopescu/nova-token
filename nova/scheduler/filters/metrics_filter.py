begin_unit
comment|'# Copyright (c) 2014 Intel, Inc.'
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
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
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
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'weight_setting'"
op|','
nl|'\n'
string|"'nova.scheduler.weights.metrics'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'metrics'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetricsFilter
name|'class'
name|'MetricsFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Metrics Filter\n\n    This filter is used to filter out those hosts which don\'t have the\n    corresponding metrics so these the metrics weigher won\'t fail due to\n    these hosts.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MetricsFilter'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'opts'
op|'='
name|'utils'
op|'.'
name|'parse_options'
op|'('
name|'CONF'
op|'.'
name|'metrics'
op|'.'
name|'weight_setting'
op|','
nl|'\n'
name|'sep'
op|'='
string|"'='"
op|','
nl|'\n'
name|'converter'
op|'='
name|'float'
op|','
nl|'\n'
name|'name'
op|'='
string|'"metrics.weight_setting"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'keys'
op|'='
name|'set'
op|'('
op|'['
name|'x'
op|'['
number|'0'
op|']'
name|'for'
name|'x'
name|'in'
name|'opts'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'filters'
op|'.'
name|'compat_legacy_props'
newline|'\n'
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
name|'metrics_on_host'
op|'='
name|'set'
op|'('
name|'m'
op|'.'
name|'name'
name|'for'
name|'m'
name|'in'
name|'host_state'
op|'.'
name|'metrics'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'keys'
op|'.'
name|'issubset'
op|'('
name|'metrics_on_host'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'unavail'
op|'='
name|'metrics_on_host'
op|'-'
name|'self'
op|'.'
name|'keys'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s does not have the following "'
nl|'\n'
string|'"metrics: %(metrics)s"'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'metrics'"
op|':'
string|"', '"
op|'.'
name|'join'
op|'('
name|'unavail'
op|')'
op|'}'
op|')'
newline|'\n'
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
