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
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'operator'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JsonFilter
name|'class'
name|'JsonFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Host Filter to allow simple JSON-based grammar for\n    selecting hosts.\n    """'
newline|'\n'
DECL|member|_op_compare
name|'def'
name|'_op_compare'
op|'('
name|'self'
op|','
name|'args'
op|','
name|'op'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns True if the specified operator can successfully\n        compare the first item in the args with all the rest. Will\n        return False if only one item is in the list.\n        """'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'<'
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'op'
name|'is'
name|'operator'
op|'.'
name|'contains'
op|':'
newline|'\n'
indent|'            '
name|'bad'
op|'='
name|'not'
name|'args'
op|'['
number|'0'
op|']'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'bad'
op|'='
op|'['
name|'arg'
name|'for'
name|'arg'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
nl|'\n'
name|'if'
name|'not'
name|'op'
op|'('
name|'args'
op|'['
number|'0'
op|']'
op|','
name|'arg'
op|')'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'not'
name|'bool'
op|'('
name|'bad'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_equals
dedent|''
name|'def'
name|'_equals'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is == all the other terms."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_op_compare'
op|'('
name|'args'
op|','
name|'operator'
op|'.'
name|'eq'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_less_than
dedent|''
name|'def'
name|'_less_than'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is < all the other terms."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_op_compare'
op|'('
name|'args'
op|','
name|'operator'
op|'.'
name|'lt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_greater_than
dedent|''
name|'def'
name|'_greater_than'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is > all the other terms."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_op_compare'
op|'('
name|'args'
op|','
name|'operator'
op|'.'
name|'gt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_in
dedent|''
name|'def'
name|'_in'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is in set of remaining terms"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_op_compare'
op|'('
name|'args'
op|','
name|'operator'
op|'.'
name|'contains'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_less_than_equal
dedent|''
name|'def'
name|'_less_than_equal'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is <= all the other terms."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_op_compare'
op|'('
name|'args'
op|','
name|'operator'
op|'.'
name|'le'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_greater_than_equal
dedent|''
name|'def'
name|'_greater_than_equal'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is >= all the other terms."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_op_compare'
op|'('
name|'args'
op|','
name|'operator'
op|'.'
name|'ge'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_not
dedent|''
name|'def'
name|'_not'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Flip each of the arguments."""'
newline|'\n'
name|'return'
op|'['
name|'not'
name|'arg'
name|'for'
name|'arg'
name|'in'
name|'args'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_or
dedent|''
name|'def'
name|'_or'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""True if any arg is True."""'
newline|'\n'
name|'return'
name|'any'
op|'('
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_and
dedent|''
name|'def'
name|'_and'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""True if all args are True."""'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|commands
dedent|''
name|'commands'
op|'='
op|'{'
nl|'\n'
string|"'='"
op|':'
name|'_equals'
op|','
nl|'\n'
string|"'<'"
op|':'
name|'_less_than'
op|','
nl|'\n'
string|"'>'"
op|':'
name|'_greater_than'
op|','
nl|'\n'
string|"'in'"
op|':'
name|'_in'
op|','
nl|'\n'
string|"'<='"
op|':'
name|'_less_than_equal'
op|','
nl|'\n'
string|"'>='"
op|':'
name|'_greater_than_equal'
op|','
nl|'\n'
string|"'not'"
op|':'
name|'_not'
op|','
nl|'\n'
string|"'or'"
op|':'
name|'_or'
op|','
nl|'\n'
string|"'and'"
op|':'
name|'_and'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_parse_string
name|'def'
name|'_parse_string'
op|'('
name|'self'
op|','
name|'string'
op|','
name|'host_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Strings prefixed with $ are capability lookups in the\n        form \'$variable\' where \'variable\' is an attribute in the\n        HostState class.  If $variable is a dictionary, you may\n        use: $variable.dictkey\n        """'
newline|'\n'
name|'if'
name|'not'
name|'string'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'string'
op|'.'
name|'startswith'
op|'('
string|'"$"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'string'
newline|'\n'
nl|'\n'
dedent|''
name|'path'
op|'='
name|'string'
op|'['
number|'1'
op|':'
op|']'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
newline|'\n'
name|'obj'
op|'='
name|'getattr'
op|'('
name|'host_state'
op|','
name|'path'
op|'['
number|'0'
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'obj'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'for'
name|'item'
name|'in'
name|'path'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'='
name|'obj'
op|'.'
name|'get'
op|'('
name|'item'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'obj'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
DECL|member|_process_filter
dedent|''
name|'def'
name|'_process_filter'
op|'('
name|'self'
op|','
name|'query'
op|','
name|'host_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Recursively parse the query structure."""'
newline|'\n'
name|'if'
name|'not'
name|'query'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'cmd'
op|'='
name|'query'
op|'['
number|'0'
op|']'
newline|'\n'
name|'method'
op|'='
name|'self'
op|'.'
name|'commands'
op|'['
name|'cmd'
op|']'
newline|'\n'
name|'cooked_args'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'arg'
name|'in'
name|'query'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'arg'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'arg'
op|'='
name|'self'
op|'.'
name|'_process_filter'
op|'('
name|'arg'
op|','
name|'host_state'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'arg'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'arg'
op|'='
name|'self'
op|'.'
name|'_parse_string'
op|'('
name|'arg'
op|','
name|'host_state'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'arg'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'cooked_args'
op|'.'
name|'append'
op|'('
name|'arg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'result'
op|'='
name|'method'
op|'('
name|'self'
op|','
name|'cooked_args'
op|')'
newline|'\n'
name|'return'
name|'result'
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
string|'"""Return a list of hosts that can fulfill the requirements\n        specified in the query.\n        """'
newline|'\n'
name|'query'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'query'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'query'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
comment|'# NOTE(comstud): Not checking capabilities or service for'
nl|'\n'
comment|'# enabled/disabled so that a provided json filter can decide'
nl|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'_process_filter'
op|'('
name|'json'
op|'.'
name|'loads'
op|'('
name|'query'
op|')'
op|','
name|'host_state'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'result'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
comment|'# If any succeeded, include the host'
nl|'\n'
indent|'            '
name|'result'
op|'='
name|'any'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'result'
op|':'
newline|'\n'
comment|'# Filter it out.'
nl|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
