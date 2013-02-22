begin_unit
comment|'# Copyright (c) 2011-2012 OpenStack Foundation'
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
string|'"""\nLeast Cost is an algorithm for choosing which host machines to\nprovision a set of resources to. The input is a WeightedHost object which\nis decided upon by a set of objective-functions, called the \'cost-functions\'.\nThe WeightedHost contains a combined weight for each cost-function.\n\nThe cost-function and weights are tabulated, and the host with the least cost\nis then selected for provisioning.\n\nNOTE(comstud): This is deprecated. One should use the RAMWeigher and/or\ncreate other weight modules.\n"""'
newline|'\n'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
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
DECL|variable|least_cost_opts
name|'least_cost_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'least_cost_functions'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Which cost functions the LeastCostScheduler should use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'noop_cost_fn_weight'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How much weight to give the noop cost function'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'compute_fill_first_cost_fn_weight'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How much weight to give the fill-first cost function. '"
nl|'\n'
string|"'A negative value will reverse behavior: '"
nl|'\n'
string|"'e.g. spread-first'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'least_cost_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|noop_cost_fn
name|'def'
name|'noop_cost_fn'
op|'('
name|'host_state'
op|','
name|'weight_properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a pre-weight cost of 1 for each host."""'
newline|'\n'
name|'return'
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_fill_first_cost_fn
dedent|''
name|'def'
name|'compute_fill_first_cost_fn'
op|'('
name|'host_state'
op|','
name|'weight_properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Higher weights win, so we should return a lower weight\n    when there\'s more free ram available.\n\n    Note: the weight modifier for this function in default configuration\n    is -1.0. With -1.0 this function runs in reverse, so systems\n    with the most free memory will be preferred.\n    """'
newline|'\n'
name|'return'
op|'-'
name|'host_state'
op|'.'
name|'free_ram_mb'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_cost_functions
dedent|''
name|'def'
name|'_get_cost_functions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a list of tuples containing weights and cost functions to\n    use for weighing hosts\n    """'
newline|'\n'
name|'cost_fns_conf'
op|'='
name|'CONF'
op|'.'
name|'least_cost_functions'
newline|'\n'
name|'if'
name|'cost_fns_conf'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# The old default.  This will get fixed up below.'
nl|'\n'
indent|'        '
name|'fn_str'
op|'='
string|"'nova.scheduler.least_cost.compute_fill_first_cost_fn'"
newline|'\n'
name|'cost_fns_conf'
op|'='
op|'['
name|'fn_str'
op|']'
newline|'\n'
dedent|''
name|'cost_fns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'cost_fn_str'
name|'in'
name|'cost_fns_conf'
op|':'
newline|'\n'
indent|'        '
name|'short_name'
op|'='
name|'cost_fn_str'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'if'
name|'not'
op|'('
name|'short_name'
op|'.'
name|'startswith'
op|'('
string|"'compute_'"
op|')'
name|'or'
nl|'\n'
name|'short_name'
op|'.'
name|'startswith'
op|'('
string|"'noop'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
comment|'# Fix up any old paths to the new paths'
nl|'\n'
dedent|''
name|'if'
name|'cost_fn_str'
op|'.'
name|'startswith'
op|'('
string|"'nova.scheduler.least_cost.'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cost_fn_str'
op|'='
op|'('
string|"'nova.scheduler.weights.least_cost'"
op|'+'
nl|'\n'
name|'cost_fn_str'
op|'['
number|'25'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# NOTE: import_class is somewhat misnamed since'
nl|'\n'
comment|'# the weighing function can be any non-class callable'
nl|'\n'
comment|"# (i.e., no 'self')"
nl|'\n'
indent|'            '
name|'cost_fn'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'cost_fn_str'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerCostFunctionNotFound'
op|'('
nl|'\n'
name|'cost_fn_str'
op|'='
name|'cost_fn_str'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flag_name'
op|'='
string|'"%s_weight"'
op|'%'
name|'cost_fn'
op|'.'
name|'__name__'
newline|'\n'
name|'weight'
op|'='
name|'getattr'
op|'('
name|'CONF'
op|','
name|'flag_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerWeightFlagNotFound'
op|'('
nl|'\n'
name|'flag_name'
op|'='
name|'flag_name'
op|')'
newline|'\n'
comment|'# Set the original default.'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'flag_name'
op|'=='
string|"'compute_fill_first_cost_fn_weight'"
name|'and'
nl|'\n'
name|'weight'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'weight'
op|'='
op|'-'
number|'1.0'
newline|'\n'
dedent|''
name|'cost_fns'
op|'.'
name|'append'
op|'('
op|'('
name|'weight'
op|','
name|'cost_fn'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cost_fns'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_least_cost_weighers
dedent|''
name|'def'
name|'get_least_cost_weighers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'cost_functions'
op|'='
name|'_get_cost_functions'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# Unfortunately we need to import this late so we don't have an"
nl|'\n'
comment|'# import loop.'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'weights'
newline|'\n'
nl|'\n'
DECL|class|_LeastCostWeigher
name|'class'
name|'_LeastCostWeigher'
op|'('
name|'weights'
op|'.'
name|'BaseHostWeigher'
op|')'
op|':'
newline|'\n'
DECL|member|weigh_objects
indent|'        '
name|'def'
name|'weigh_objects'
op|'('
name|'self'
op|','
name|'weighted_hosts'
op|','
name|'weight_properties'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'host'
name|'in'
name|'weighted_hosts'
op|':'
newline|'\n'
indent|'                '
name|'host'
op|'.'
name|'weight'
op|'='
name|'sum'
op|'('
name|'weight'
op|'*'
name|'fn'
op|'('
name|'host'
op|'.'
name|'obj'
op|','
name|'weight_properties'
op|')'
nl|'\n'
name|'for'
name|'weight'
op|','
name|'fn'
name|'in'
name|'cost_functions'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
op|'['
name|'_LeastCostWeigher'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
