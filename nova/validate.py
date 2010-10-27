begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""Decorators for argument validation, courtesy of\nhttp://rmi.net/~lutz/rangetest.html"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rangetest
name|'def'
name|'rangetest'
op|'('
op|'**'
name|'argchecks'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validate ranges for both + defaults"""'
newline|'\n'
nl|'\n'
DECL|function|onDecorator
name|'def'
name|'onDecorator'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""onCall remembers func and argchecks"""'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'code'
op|'='
name|'func'
op|'.'
name|'__code__'
name|'if'
name|'sys'
op|'.'
name|'version_info'
op|'['
number|'0'
op|']'
op|'=='
number|'3'
name|'else'
name|'func'
op|'.'
name|'func_code'
newline|'\n'
name|'allargs'
op|'='
name|'code'
op|'.'
name|'co_varnames'
op|'['
op|':'
name|'code'
op|'.'
name|'co_argcount'
op|']'
newline|'\n'
name|'funcname'
op|'='
name|'func'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
DECL|function|onCall
name|'def'
name|'onCall'
op|'('
op|'*'
name|'pargs'
op|','
op|'**'
name|'kargs'
op|')'
op|':'
newline|'\n'
comment|'# all pargs match first N args by position'
nl|'\n'
comment|'# the rest must be in kargs or omitted defaults'
nl|'\n'
indent|'            '
name|'positionals'
op|'='
name|'list'
op|'('
name|'allargs'
op|')'
newline|'\n'
name|'positionals'
op|'='
name|'positionals'
op|'['
op|':'
name|'len'
op|'('
name|'pargs'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'argname'
op|','
op|'('
name|'low'
op|','
name|'high'
op|')'
op|')'
name|'in'
name|'argchecks'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# for all args to be checked'
nl|'\n'
indent|'                '
name|'if'
name|'argname'
name|'in'
name|'kargs'
op|':'
newline|'\n'
comment|'# was passed by name'
nl|'\n'
indent|'                    '
name|'if'
name|'float'
op|'('
name|'kargs'
op|'['
name|'argname'
op|']'
op|')'
op|'<'
name|'low'
name|'or'
name|'float'
op|'('
name|'kargs'
op|'['
name|'argname'
op|']'
op|')'
op|'>'
name|'high'
op|':'
newline|'\n'
indent|'                        '
name|'errmsg'
op|'='
string|'\'{0} argument "{1}" not in {2}..{3}\''
newline|'\n'
name|'errmsg'
op|'='
name|'errmsg'
op|'.'
name|'format'
op|'('
name|'funcname'
op|','
name|'argname'
op|','
name|'low'
op|','
name|'high'
op|')'
newline|'\n'
name|'raise'
name|'TypeError'
op|'('
name|'errmsg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'elif'
name|'argname'
name|'in'
name|'positionals'
op|':'
newline|'\n'
comment|'# was passed by position'
nl|'\n'
indent|'                    '
name|'position'
op|'='
name|'positionals'
op|'.'
name|'index'
op|'('
name|'argname'
op|')'
newline|'\n'
name|'if'
name|'float'
op|'('
name|'pargs'
op|'['
name|'position'
op|']'
op|')'
op|'<'
name|'low'
name|'or'
name|'float'
op|'('
name|'pargs'
op|'['
name|'position'
op|']'
op|')'
op|'>'
name|'high'
op|':'
newline|'\n'
indent|'                        '
name|'errmsg'
op|'='
string|'\'{0} argument "{1}" with value of {4} \''
string|"'not in {2}..{3}'"
newline|'\n'
name|'errmsg'
op|'='
name|'errmsg'
op|'.'
name|'format'
op|'('
name|'funcname'
op|','
name|'argname'
op|','
name|'low'
op|','
name|'high'
op|','
nl|'\n'
name|'pargs'
op|'['
name|'position'
op|']'
op|')'
newline|'\n'
name|'raise'
name|'TypeError'
op|'('
name|'errmsg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'func'
op|'('
op|'*'
name|'pargs'
op|','
op|'**'
name|'kargs'
op|')'
comment|'# okay: run original call'
newline|'\n'
dedent|''
name|'return'
name|'onCall'
newline|'\n'
dedent|''
name|'return'
name|'onDecorator'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|typetest
dedent|''
name|'def'
name|'typetest'
op|'('
op|'**'
name|'argchecks'
op|')'
op|':'
newline|'\n'
DECL|function|onDecorator
indent|'    '
name|'def'
name|'onDecorator'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'import'
name|'sys'
newline|'\n'
name|'code'
op|'='
name|'func'
op|'.'
name|'__code__'
name|'if'
name|'sys'
op|'.'
name|'version_info'
op|'['
number|'0'
op|']'
op|'=='
number|'3'
name|'else'
name|'func'
op|'.'
name|'func_code'
newline|'\n'
name|'allargs'
op|'='
name|'code'
op|'.'
name|'co_varnames'
op|'['
op|':'
name|'code'
op|'.'
name|'co_argcount'
op|']'
newline|'\n'
name|'funcname'
op|'='
name|'func'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
DECL|function|onCall
name|'def'
name|'onCall'
op|'('
op|'*'
name|'pargs'
op|','
op|'**'
name|'kargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'positionals'
op|'='
name|'list'
op|'('
name|'allargs'
op|')'
op|'['
op|':'
name|'len'
op|'('
name|'pargs'
op|')'
op|']'
newline|'\n'
name|'for'
op|'('
name|'argname'
op|','
name|'typeof'
op|')'
name|'in'
name|'argchecks'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'argname'
name|'in'
name|'kargs'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'kargs'
op|'['
name|'argname'
op|']'
op|','
name|'typeof'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'errmsg'
op|'='
string|'\'{0} argument "{1}" not of type {2}\''
newline|'\n'
name|'errmsg'
op|'='
name|'errmsg'
op|'.'
name|'format'
op|'('
name|'funcname'
op|','
name|'argname'
op|','
name|'typeof'
op|')'
newline|'\n'
name|'raise'
name|'TypeError'
op|'('
name|'errmsg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'argname'
name|'in'
name|'positionals'
op|':'
newline|'\n'
indent|'                    '
name|'position'
op|'='
name|'positionals'
op|'.'
name|'index'
op|'('
name|'argname'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'pargs'
op|'['
name|'position'
op|']'
op|','
name|'typeof'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'errmsg'
op|'='
string|'\'{0} argument "{1}" with value of {2} \''
string|"'not of type {3}'"
newline|'\n'
name|'errmsg'
op|'='
name|'errmsg'
op|'.'
name|'format'
op|'('
name|'funcname'
op|','
name|'argname'
op|','
nl|'\n'
name|'pargs'
op|'['
name|'position'
op|']'
op|','
name|'typeof'
op|')'
newline|'\n'
name|'raise'
name|'TypeError'
op|'('
name|'errmsg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'func'
op|'('
op|'*'
name|'pargs'
op|','
op|'**'
name|'kargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'onCall'
newline|'\n'
dedent|''
name|'return'
name|'onDecorator'
newline|'\n'
dedent|''
endmarker|''
end_unit
