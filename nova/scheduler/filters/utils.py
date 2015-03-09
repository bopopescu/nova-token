begin_unit
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
string|'"""Bench of utility methods used by filters."""'
newline|'\n'
nl|'\n'
name|'import'
name|'collections'
newline|'\n'
nl|'\n'
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
name|'i18n'
name|'import'
name|'_LI'
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
DECL|function|aggregate_values_from_key
name|'def'
name|'aggregate_values_from_key'
op|'('
name|'host_state'
op|','
name|'key_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a set of values based on a metadata key for a specific host."""'
newline|'\n'
name|'aggrlist'
op|'='
name|'host_state'
op|'.'
name|'aggregates'
newline|'\n'
name|'aggregate_vals'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'aggr'
name|'in'
name|'aggrlist'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key_name'
name|'in'
name|'aggr'
op|'.'
name|'metadata'
op|':'
newline|'\n'
indent|'            '
name|'aggregate_vals'
op|'.'
name|'add'
op|'('
name|'aggr'
op|'.'
name|'metadata'
op|'['
name|'key_name'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'aggregate_vals'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|aggregate_metadata_get_by_host
dedent|''
name|'def'
name|'aggregate_metadata_get_by_host'
op|'('
name|'host_state'
op|','
name|'key'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a dict of all metadata for a specific host."""'
newline|'\n'
name|'aggrlist'
op|'='
name|'host_state'
op|'.'
name|'aggregates'
newline|'\n'
name|'metadata'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'set'
op|')'
newline|'\n'
name|'for'
name|'aggr'
name|'in'
name|'aggrlist'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'is'
name|'not'
name|'None'
name|'and'
name|'key'
name|'not'
name|'in'
name|'aggr'
op|'.'
name|'metadata'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'aggr'
op|'.'
name|'metadata'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'v'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
name|'for'
name|'value'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'                '
name|'metadata'
op|'['
name|'k'
op|']'
op|'.'
name|'add'
op|'('
name|'value'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_num_values
dedent|''
name|'def'
name|'validate_num_values'
op|'('
name|'vals'
op|','
name|'default'
op|'='
name|'None'
op|','
name|'cast_to'
op|'='
name|'int'
op|','
name|'based_on'
op|'='
name|'min'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a correctly casted value based on a set of values.\n\n    This method is useful to work with per-aggregate filters, It takes\n    a set of values then return the \'based_on\'{min/max} converted to\n    \'cast_to\' of the set or the default value.\n\n    Note: The cast implies a possible ValueError\n    """'
newline|'\n'
name|'num_values'
op|'='
name|'len'
op|'('
name|'vals'
op|')'
newline|'\n'
name|'if'
name|'num_values'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'default'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'num_values'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"%(num_values)d values found, "'
nl|'\n'
string|'"of which the minimum value will be used."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'num_values'"
op|':'
name|'num_values'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cast_to'
op|'('
name|'based_on'
op|'('
name|'vals'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
