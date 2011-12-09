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
comment|'# Copyright 2011 Red Hat, Inc.'
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
string|'"""Command-line flag library.\n\nEmulates gflags by wrapping cfg.ConfigOpts.\n\nThe idea is to move fully to cfg eventually, and this wrapper is a\nstepping stone.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'gflags'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlagValues
name|'class'
name|'FlagValues'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|class|Flag
indent|'    '
name|'class'
name|'Flag'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'update_default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'value'
op|'='
name|'value'
newline|'\n'
name|'self'
op|'.'
name|'_update_default'
op|'='
name|'update_default'
newline|'\n'
nl|'\n'
DECL|member|SetDefault
dedent|''
name|'def'
name|'SetDefault'
op|'('
name|'self'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_update_default'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_update_default'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
DECL|class|ErrorCatcher
dedent|''
dedent|''
dedent|''
name|'class'
name|'ErrorCatcher'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'orig_error'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'orig_error'
op|'='
name|'orig_error'
newline|'\n'
name|'self'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset
dedent|''
name|'def'
name|'reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error_msg'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|catch
dedent|''
name|'def'
name|'catch'
op|'('
name|'self'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|'": --"'
name|'in'
name|'msg'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_error_msg'
op|'='
name|'msg'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'orig_error'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_unknown_arg
dedent|''
dedent|''
name|'def'
name|'get_unknown_arg'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_error_msg'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
comment|'# Error message is e.g. "no such option: --runtime_answer"'
nl|'\n'
dedent|''
name|'a'
op|'='
name|'self'
op|'.'
name|'_error_msg'
op|'['
name|'self'
op|'.'
name|'_error_msg'
op|'.'
name|'rindex'
op|'('
string|'": --"'
op|')'
op|'+'
number|'2'
op|':'
op|']'
newline|'\n'
name|'return'
name|'filter'
op|'('
name|'lambda'
name|'i'
op|':'
name|'i'
op|'=='
name|'a'
name|'or'
name|'i'
op|'.'
name|'startswith'
op|'('
name|'a'
op|'+'
string|'"="'
op|')'
op|','
name|'args'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
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
name|'_conf'
op|'='
name|'cfg'
op|'.'
name|'ConfigOpts'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'_oparser'
op|'.'
name|'disable_interspersed_args'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_opts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'Reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parse
dedent|''
name|'def'
name|'_parse'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_extra'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
name|'gflags'
op|'.'
name|'FlagValues'
op|'('
op|')'
op|'.'
name|'ReadFlagsFromFiles'
op|'('
name|'self'
op|'.'
name|'_args'
op|')'
newline|'\n'
nl|'\n'
name|'extra'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# This horrendous hack allows us to stop optparse'
nl|'\n'
comment|'# exiting when it encounters an unknown option'
nl|'\n'
comment|'#'
nl|'\n'
name|'error_catcher'
op|'='
name|'self'
op|'.'
name|'ErrorCatcher'
op|'('
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'_oparser'
op|'.'
name|'error'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'_oparser'
op|'.'
name|'error'
op|'='
name|'error_catcher'
op|'.'
name|'catch'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'error_catcher'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'extra'
op|'='
name|'self'
op|'.'
name|'_conf'
op|'('
name|'args'
op|')'
newline|'\n'
nl|'\n'
name|'unknown'
op|'='
name|'error_catcher'
op|'.'
name|'get_unknown_arg'
op|'('
name|'args'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'unknown'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'.'
name|'remove'
op|'('
name|'unknown'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'_oparser'
op|'.'
name|'error'
op|'='
name|'error_catcher'
op|'.'
name|'orig_error'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_extra'
op|'='
name|'extra'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'argv'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'Reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_args'
op|'='
name|'argv'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_parse'
op|'('
op|')'
newline|'\n'
name|'return'
op|'['
name|'argv'
op|'['
number|'0'
op|']'
op|']'
op|'+'
name|'self'
op|'.'
name|'_extra'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_parse'
op|'('
op|')'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_conf'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'name'
op|')'
newline|'\n'
name|'if'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
comment|'# value might be \'0\' or ""'
newline|'\n'
indent|'            '
name|'return'
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'default'
newline|'\n'
nl|'\n'
DECL|member|__contains__
dedent|''
dedent|''
name|'def'
name|'__contains__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_parse'
op|'('
op|')'
newline|'\n'
name|'return'
name|'hasattr'
op|'('
name|'self'
op|'.'
name|'_conf'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_update_default
dedent|''
name|'def'
name|'_update_default'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'set_default'
op|'('
name|'name'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'FlagValuesDict'
op|'('
op|')'
op|'.'
name|'iterkeys'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_parse'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'__contains__'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'Flag'
op|'('
name|'name'
op|','
name|'getattr'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|','
name|'self'
op|'.'
name|'_update_default'
op|')'
newline|'\n'
nl|'\n'
DECL|member|Reset
dedent|''
name|'def'
name|'Reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_args'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_extra'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|ParseNewFlags
dedent|''
name|'def'
name|'ParseNewFlags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|FlagValuesDict
dedent|''
name|'def'
name|'FlagValuesDict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_parse'
op|'('
op|')'
newline|'\n'
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'opt'
name|'in'
name|'self'
op|'.'
name|'_opts'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'['
name|'opt'
op|'.'
name|'dest'
op|']'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'opt'
op|'.'
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|_add_option
dedent|''
name|'def'
name|'_add_option'
op|'('
name|'self'
op|','
name|'opt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'opt'
op|'.'
name|'dest'
name|'in'
name|'self'
op|'.'
name|'_opts'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_opts'
op|'['
name|'opt'
op|'.'
name|'dest'
op|']'
op|'='
name|'opt'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'register_cli_opts'
op|'('
name|'self'
op|'.'
name|'_opts'
op|'.'
name|'values'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cfg'
op|'.'
name|'ArgsAlreadyParsedError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conf'
op|'.'
name|'register_cli_opts'
op|'('
name|'self'
op|'.'
name|'_opts'
op|'.'
name|'values'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extra'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|define_string
dedent|''
dedent|''
name|'def'
name|'define_string'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_add_option'
op|'('
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
name|'name'
op|','
name|'default'
op|'='
name|'default'
op|','
name|'help'
op|'='
name|'help'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|define_integer
dedent|''
name|'def'
name|'define_integer'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_add_option'
op|'('
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
name|'name'
op|','
name|'default'
op|'='
name|'default'
op|','
name|'help'
op|'='
name|'help'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|define_float
dedent|''
name|'def'
name|'define_float'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_add_option'
op|'('
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
name|'name'
op|','
name|'default'
op|'='
name|'default'
op|','
name|'help'
op|'='
name|'help'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|define_bool
dedent|''
name|'def'
name|'define_bool'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_add_option'
op|'('
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
name|'name'
op|','
name|'default'
op|'='
name|'default'
op|','
name|'help'
op|'='
name|'help'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|define_list
dedent|''
name|'def'
name|'define_list'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_add_option'
op|'('
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
name|'name'
op|','
name|'default'
op|'='
name|'default'
op|','
name|'help'
op|'='
name|'help'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|define_multistring
dedent|''
name|'def'
name|'define_multistring'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_add_option'
op|'('
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
name|'name'
op|','
name|'default'
op|'='
name|'default'
op|','
name|'help'
op|'='
name|'help'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
dedent|''
dedent|''
name|'FLAGS'
op|'='
name|'FlagValues'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_string
name|'def'
name|'DEFINE_string'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flag_values'
op|'.'
name|'define_string'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_integer
dedent|''
name|'def'
name|'DEFINE_integer'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'lower_bound'
op|'='
name|'None'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
comment|'# FIXME(markmc): ignoring lower_bound'
nl|'\n'
indent|'    '
name|'flag_values'
op|'.'
name|'define_integer'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_bool
dedent|''
name|'def'
name|'DEFINE_bool'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flag_values'
op|'.'
name|'define_bool'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_boolean
dedent|''
name|'def'
name|'DEFINE_boolean'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'DEFINE_bool'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'flag_values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_list
dedent|''
name|'def'
name|'DEFINE_list'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flag_values'
op|'.'
name|'define_list'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_float
dedent|''
name|'def'
name|'DEFINE_float'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flag_values'
op|'.'
name|'define_float'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_multistring
dedent|''
name|'def'
name|'DEFINE_multistring'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flag_values'
op|'.'
name|'define_multistring'
op|'('
name|'name'
op|','
name|'default'
op|','
name|'help'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnrecognizedFlag
dedent|''
name|'class'
name|'UnrecognizedFlag'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DECLARE
dedent|''
name|'def'
name|'DECLARE'
op|'('
name|'name'
op|','
name|'module_string'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'module_string'
name|'not'
name|'in'
name|'sys'
op|'.'
name|'modules'
op|':'
newline|'\n'
indent|'        '
name|'__import__'
op|'('
name|'module_string'
op|','
name|'globals'
op|'('
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'name'
name|'not'
name|'in'
name|'flag_values'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'UnrecognizedFlag'
op|'('
string|"'%s not defined by %s'"
op|'%'
op|'('
name|'name'
op|','
name|'module_string'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DEFINE_flag
dedent|''
dedent|''
name|'def'
name|'DEFINE_flag'
op|'('
name|'flag'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HelpFlag
dedent|''
name|'class'
name|'HelpFlag'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HelpshortFlag
dedent|''
name|'class'
name|'HelpshortFlag'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HelpXMLFlag
dedent|''
name|'class'
name|'HelpXMLFlag'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_my_ip
dedent|''
name|'def'
name|'_get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the actual ip of the local machine."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'csock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_DGRAM'
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'connect'
op|'('
op|'('
string|"'8.8.8.8'"
op|','
number|'80'
op|')'
op|')'
newline|'\n'
op|'('
name|'addr'
op|','
name|'port'
op|')'
op|'='
name|'csock'
op|'.'
name|'getsockname'
op|'('
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'addr'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"127.0.0.1"'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# __GLOBAL FLAGS ONLY__'
nl|'\n'
comment|'# Define any app-specific flags in their own files, docs at:'
nl|'\n'
comment|'# http://code.google.com/p/python-gflags/source/browse/trunk/gflags.py#a9'
nl|'\n'
dedent|''
dedent|''
name|'DEFINE_string'
op|'('
string|"'my_ip'"
op|','
name|'_get_my_ip'
op|'('
op|')'
op|','
string|"'host ip address'"
op|')'
newline|'\n'
name|'DEFINE_list'
op|'('
string|"'region_list'"
op|','
nl|'\n'
op|'['
op|']'
op|','
nl|'\n'
string|"'list of region=fqdn pairs separated by commas'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'connection_type'"
op|','
string|"'libvirt'"
op|','
string|"'libvirt, xenapi or fake'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'aws_access_key_id'"
op|','
string|"'admin'"
op|','
string|"'AWS Access ID'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'aws_secret_access_key'"
op|','
string|"'admin'"
op|','
string|"'AWS Access Key'"
op|')'
newline|'\n'
comment|"# NOTE(sirp): my_ip interpolation doesn't work within nested structures"
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'glance_host'"
op|','
name|'_get_my_ip'
op|'('
op|')'
op|','
string|"'default glance host'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'glance_port'"
op|','
number|'9292'
op|','
string|"'default glance port'"
op|')'
newline|'\n'
name|'DEFINE_list'
op|'('
string|"'glance_api_servers'"
op|','
nl|'\n'
op|'['
string|"'%s:%d'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'glance_host'
op|','
name|'FLAGS'
op|'.'
name|'glance_port'
op|')'
op|']'
op|','
nl|'\n'
string|"'list of glance api servers available to nova (host:port)'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'glance_num_retries'"
op|','
number|'0'
op|','
nl|'\n'
string|"'The number of times to retry downloading an image from glance'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'s3_port'"
op|','
number|'3333'
op|','
string|"'s3 port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'s3_host'"
op|','
string|"'$my_ip'"
op|','
string|"'s3 host (for infrastructure)'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'s3_dmz'"
op|','
string|"'$my_ip'"
op|','
string|"'s3 dmz ip (for instances)'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'compute_topic'"
op|','
string|"'compute'"
op|','
string|"'the topic compute nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'console_topic'"
op|','
string|"'console'"
op|','
nl|'\n'
string|"'the topic console proxy nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'scheduler_topic'"
op|','
string|"'scheduler'"
op|','
nl|'\n'
string|"'the topic scheduler nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'volume_topic'"
op|','
string|"'volume'"
op|','
string|"'the topic volume nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'network_topic'"
op|','
string|"'network'"
op|','
string|"'the topic network nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ajax_console_proxy_topic'"
op|','
string|"'ajax_proxy'"
op|','
nl|'\n'
string|"'the topic ajax proxy nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ajax_console_proxy_url'"
op|','
nl|'\n'
string|"'http://127.0.0.1:8000'"
op|','
nl|'\n'
string|'\'location of ajax console proxy, \\\n               in the form "http://127.0.0.1:8000"\''
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'ajax_console_proxy_port'"
op|','
nl|'\n'
number|'8000'
op|','
string|"'port that ajax_console_proxy binds'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'vsa_topic'"
op|','
string|"'vsa'"
op|','
string|"'the topic that nova-vsa service listens on'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'verbose'"
op|','
name|'False'
op|','
string|"'show debug output'"
op|')'
newline|'\n'
name|'DEFINE_boolean'
op|'('
string|"'fake_rabbit'"
op|','
name|'False'
op|','
string|"'use a fake rabbit'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'fake_network'"
op|','
name|'False'
op|','
nl|'\n'
string|"'should we use fake network devices and addresses'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_host'"
op|','
string|"'localhost'"
op|','
string|"'rabbit host'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_port'"
op|','
number|'5672'
op|','
string|"'rabbit port'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'rabbit_use_ssl'"
op|','
name|'False'
op|','
string|"'connect over SSL'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_userid'"
op|','
string|"'guest'"
op|','
string|"'rabbit userid'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_password'"
op|','
string|"'guest'"
op|','
string|"'rabbit password'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_virtual_host'"
op|','
string|"'/'"
op|','
string|"'rabbit virtual host'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_retry_interval'"
op|','
number|'1'
op|','
nl|'\n'
string|"'rabbit connection retry interval to start'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_retry_backoff'"
op|','
number|'2'
op|','
nl|'\n'
string|"'rabbit connection retry backoff in seconds'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_max_retries'"
op|','
number|'0'
op|','
nl|'\n'
string|"'maximum rabbit connection attempts (0=try forever)'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'control_exchange'"
op|','
string|"'nova'"
op|','
string|"'the main exchange to connect to'"
op|')'
newline|'\n'
name|'DEFINE_boolean'
op|'('
string|"'rabbit_durable_queues'"
op|','
name|'False'
op|','
string|"'use durable queues'"
op|')'
newline|'\n'
name|'DEFINE_list'
op|'('
string|"'enabled_apis'"
op|','
op|'['
string|"'ec2'"
op|','
string|"'osapi'"
op|','
string|"'metadata'"
op|']'
op|','
nl|'\n'
string|"'list of APIs to enable by default'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_host'"
op|','
string|"'$my_ip'"
op|','
string|"'ip of api server'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_dmz_host'"
op|','
string|"'$my_ip'"
op|','
string|"'internal ip of api server'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'ec2_port'"
op|','
number|'8773'
op|','
string|"'cloud controller port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_scheme'"
op|','
string|"'http'"
op|','
string|"'prefix for ec2'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_path'"
op|','
string|"'/services/Cloud'"
op|','
string|"'suffix for ec2'"
op|')'
newline|'\n'
name|'DEFINE_multistring'
op|'('
string|"'osapi_extension'"
op|','
nl|'\n'
op|'['
string|"'nova.api.openstack.v2.contrib.standard_extensions'"
op|']'
op|','
nl|'\n'
string|"'osapi extension to load'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'osapi_host'"
op|','
string|"'$my_ip'"
op|','
string|"'ip of api server'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'osapi_scheme'"
op|','
string|"'http'"
op|','
string|"'prefix for openstack'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'osapi_port'"
op|','
number|'8774'
op|','
string|"'OpenStack API port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'osapi_path'"
op|','
string|"'/v1.1/'"
op|','
string|"'suffix for openstack'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'osapi_max_limit'"
op|','
number|'1000'
op|','
nl|'\n'
string|"'max number of items returned in a collection response'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'metadata_host'"
op|','
string|"'$my_ip'"
op|','
string|"'ip of metadata server'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'metadata_port'"
op|','
number|'8775'
op|','
string|"'Metadata API port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_project'"
op|','
string|"'openstack'"
op|','
string|"'default project for openstack'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_image'"
op|','
string|"'ami-11111'"
op|','
nl|'\n'
string|"'default image to use, testing only'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_instance_type'"
op|','
string|"'m1.small'"
op|','
nl|'\n'
string|"'default instance type to use, testing only'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'null_kernel'"
op|','
string|"'nokernel'"
op|','
nl|'\n'
string|"'kernel image that indicates not to use a kernel,'"
nl|'\n'
string|"' but to use a raw disk image instead'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'vpn_image_id'"
op|','
string|"'0'"
op|','
string|"'image id for cloudpipe vpn server'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'vpn_key_suffix'"
op|','
nl|'\n'
string|"'-vpn'"
op|','
nl|'\n'
string|"'Suffix to add to project name for vpn key and secgroups'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_integer'
op|'('
string|"'auth_token_ttl'"
op|','
number|'3600'
op|','
string|"'Seconds for auth tokens to linger'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'state_path'"
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'../'"
op|')'
op|','
nl|'\n'
string|'"Top-level directory for maintaining nova\'s state"'
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'lock_path'"
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'../'"
op|')'
op|','
nl|'\n'
string|"'Directory for lock files'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'logdir'"
op|','
name|'None'
op|','
string|"'output to a per-service log file in named '"
nl|'\n'
string|"'directory'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'logfile_mode'"
op|','
string|"'0644'"
op|','
string|"'Default file mode of the logs.'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'sqlite_db'"
op|','
string|"'nova.sqlite'"
op|','
string|"'file name for sqlite'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'sqlite_synchronous'"
op|','
name|'True'
op|','
string|"'Synchronous mode for sqlite'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'sql_connection'"
op|','
nl|'\n'
string|"'sqlite:///$state_path/$sqlite_db'"
op|','
nl|'\n'
string|"'connection string for sql database'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'sql_idle_timeout'"
op|','
nl|'\n'
number|'3600'
op|','
nl|'\n'
string|"'timeout for idle sql database connections'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'sql_max_retries'"
op|','
number|'12'
op|','
string|"'sql connection attempts'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'sql_retry_interval'"
op|','
number|'10'
op|','
string|"'sql connection retry interval'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'compute_manager'"
op|','
string|"'nova.compute.manager.ComputeManager'"
op|','
nl|'\n'
string|"'Manager for compute'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'console_manager'"
op|','
string|"'nova.console.manager.ConsoleProxyManager'"
op|','
nl|'\n'
string|"'Manager for console proxy'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'instance_dns_manager'"
op|','
nl|'\n'
string|"'nova.network.instance_dns_driver.InstanceDNSManagerDriver'"
op|','
nl|'\n'
string|"'DNS Manager for instance IPs'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'instance_dns_zone'"
op|','
string|"''"
op|','
nl|'\n'
string|"'DNS Zone for instance IPs'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'network_manager'"
op|','
string|"'nova.network.manager.VlanManager'"
op|','
nl|'\n'
string|"'Manager for network'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'volume_manager'"
op|','
string|"'nova.volume.manager.VolumeManager'"
op|','
nl|'\n'
string|"'Manager for volume'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'scheduler_manager'"
op|','
string|"'nova.scheduler.manager.SchedulerManager'"
op|','
nl|'\n'
string|"'Manager for scheduler'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'vsa_manager'"
op|','
string|"'nova.vsa.manager.VsaManager'"
op|','
nl|'\n'
string|"'Manager for vsa'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'vc_image_name'"
op|','
string|"'vc_image'"
op|','
nl|'\n'
string|"'the VC image ID (for a VC image that exists in DB Glance)'"
op|')'
newline|'\n'
comment|'# VSA constants and enums'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'default_vsa_instance_type'"
op|','
string|"'m1.small'"
op|','
nl|'\n'
string|"'default instance type for VSA instances'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'max_vcs_in_vsa'"
op|','
number|'32'
op|','
nl|'\n'
string|"'maxinum VCs in a VSA'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'vsa_part_size_gb'"
op|','
number|'100'
op|','
nl|'\n'
string|"'default partition size for shared capacity'"
op|')'
newline|'\n'
nl|'\n'
comment|'# The service to use for image search and retrieval'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'image_service'"
op|','
string|"'nova.image.glance.GlanceImageService'"
op|','
nl|'\n'
string|"'The service to use for retrieving and searching for images.'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'host'"
op|','
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
string|"'Name of this node.  This can be an opaque identifier.  It is '"
nl|'\n'
string|"'not necessarily a hostname, FQDN, or IP address.'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'node_availability_zone'"
op|','
string|"'nova'"
op|','
nl|'\n'
string|"'availability zone of this node'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'notification_driver'"
op|','
nl|'\n'
string|"'nova.notifier.no_op_notifier'"
op|','
nl|'\n'
string|"'Default driver for sending notifications'"
op|')'
newline|'\n'
name|'DEFINE_list'
op|'('
string|"'memcached_servers'"
op|','
name|'None'
op|','
nl|'\n'
string|"'Memcached servers or None for in process cache.'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'zone_name'"
op|','
string|"'nova'"
op|','
string|"'name of this zone'"
op|')'
newline|'\n'
name|'DEFINE_list'
op|'('
string|"'zone_capabilities'"
op|','
nl|'\n'
op|'['
string|"'hypervisor=xenserver;kvm'"
op|','
string|"'os=linux;windows'"
op|']'
op|','
nl|'\n'
string|"'Key/Multi-value list representng capabilities of this zone'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'build_plan_encryption_key'"
op|','
name|'None'
op|','
nl|'\n'
string|"'128bit (hex) encryption key for scheduler build plans.'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'instance_usage_audit_period'"
op|','
string|"'month'"
op|','
nl|'\n'
string|"'time period to generate instance usages for.'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'bandwith_poll_interval'"
op|','
number|'600'
op|','
nl|'\n'
string|"'interval to pull bandwidth usage info'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_bool'
op|'('
string|"'start_guests_on_host_boot'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Whether to restart guests when the host reboots'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'resume_guests_state_on_host_boot'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Whether to start guests, that was running before the host reboot'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'root_helper'"
op|','
string|"'sudo'"
op|','
nl|'\n'
string|"'Command prefix to use for running commands as root'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'network_driver'"
op|','
string|"'nova.network.linux_net'"
op|','
nl|'\n'
string|"'Driver to use for network creation'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_bool'
op|'('
string|"'use_ipv6'"
op|','
name|'False'
op|','
string|"'use ipv6'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_integer'
op|'('
string|"'password_length'"
op|','
number|'12'
op|','
nl|'\n'
string|"'Length of generated instance admin passwords'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_bool'
op|'('
string|"'monkey_patch'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Whether to log monkey patching'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_list'
op|'('
string|"'monkey_patch_modules'"
op|','
nl|'\n'
op|'['
string|"'nova.api.ec2.cloud:nova.notifier.api.notify_decorator'"
op|','
nl|'\n'
string|"'nova.compute.api:nova.notifier.api.notify_decorator'"
op|']'
op|','
nl|'\n'
string|"'Module list representing monkey '"
nl|'\n'
string|"'patched module and decorator'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_bool'
op|'('
string|"'allow_resize_to_same_host'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Allow destination machine to match source for resize. Useful'"
nl|'\n'
string|"' when testing in environments with only one host machine.'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'stub_network'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Stub network related code'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_integer'
op|'('
string|"'reclaim_instance_interval'"
op|','
number|'0'
op|','
nl|'\n'
string|"'Interval in seconds for reclaiming deleted instances'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_integer'
op|'('
string|"'zombie_instance_updated_at_window'"
op|','
number|'172800'
op|','
nl|'\n'
string|"'Limit in seconds that a zombie instance can exist before '"
nl|'\n'
string|"'being cleaned up.'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_boolean'
op|'('
string|"'allow_ec2_admin_api'"
op|','
name|'False'
op|','
string|"'Enable/Disable EC2 Admin API'"
op|')'
newline|'\n'
endmarker|''
end_unit
