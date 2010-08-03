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
string|'"""\nTwisted daemon helpers, specifically to parse out gFlags from twisted flags,\nmanage pid files and support syslogging.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'scripts'
name|'import'
name|'twistd'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'reflect'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'runtime'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'usage'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
nl|'\n'
name|'if'
name|'runtime'
op|'.'
name|'platformType'
op|'=='
string|'"win32"'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'scripts'
op|'.'
name|'_twistw'
name|'import'
name|'ServerOptions'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'scripts'
op|'.'
name|'_twistd_unix'
name|'import'
name|'ServerOptions'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
dedent|''
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TwistdServerOptions
name|'class'
name|'TwistdServerOptions'
op|'('
name|'ServerOptions'
op|')'
op|':'
newline|'\n'
DECL|member|parseArgs
indent|'    '
name|'def'
name|'parseArgs'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|WrapTwistedOptions
dedent|''
dedent|''
name|'def'
name|'WrapTwistedOptions'
op|'('
name|'wrapped'
op|')'
op|':'
newline|'\n'
DECL|class|TwistedOptionsToFlags
indent|'    '
name|'class'
name|'TwistedOptionsToFlags'
op|'('
name|'wrapped'
op|')'
op|':'
newline|'\n'
DECL|variable|subCommands
indent|'        '
name|'subCommands'
op|'='
name|'None'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(termie): _data exists because Twisted stuff expects'
nl|'\n'
comment|'#               to be able to set arbitrary things that are'
nl|'\n'
comment|'#               not actual flags'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_flagHandlers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_paramHandlers'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Absorb the twistd flags into our FLAGS'
nl|'\n'
name|'self'
op|'.'
name|'_absorbFlags'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_absorbParameters'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_absorbHandlers'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'TwistedOptionsToFlags'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_absorbFlags
dedent|''
name|'def'
name|'_absorbFlags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'twistd_flags'
op|'='
op|'['
op|']'
newline|'\n'
name|'reflect'
op|'.'
name|'accumulateClassList'
op|'('
name|'self'
op|'.'
name|'__class__'
op|','
string|"'optFlags'"
op|','
name|'twistd_flags'
op|')'
newline|'\n'
name|'for'
name|'flag'
name|'in'
name|'twistd_flags'
op|':'
newline|'\n'
indent|'                '
name|'key'
op|'='
name|'flag'
op|'['
number|'0'
op|']'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
name|'key'
op|','
name|'None'
op|','
name|'str'
op|'('
name|'flag'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_absorbParameters
dedent|''
dedent|''
name|'def'
name|'_absorbParameters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'twistd_params'
op|'='
op|'['
op|']'
newline|'\n'
name|'reflect'
op|'.'
name|'accumulateClassList'
op|'('
name|'self'
op|'.'
name|'__class__'
op|','
string|"'optParameters'"
op|','
name|'twistd_params'
op|')'
newline|'\n'
name|'for'
name|'param'
name|'in'
name|'twistd_params'
op|':'
newline|'\n'
indent|'                '
name|'key'
op|'='
name|'param'
op|'['
number|'0'
op|']'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
name|'key'
op|','
name|'param'
op|'['
number|'2'
op|']'
op|','
name|'str'
op|'('
name|'param'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_absorbHandlers
dedent|''
dedent|''
name|'def'
name|'_absorbHandlers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'twistd_handlers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'reflect'
op|'.'
name|'addMethodNamesToDict'
op|'('
name|'self'
op|'.'
name|'__class__'
op|','
name|'twistd_handlers'
op|','
string|'"opt_"'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(termie): Much of the following is derived/copied from'
nl|'\n'
comment|'#               twisted.python.usage with the express purpose of'
nl|'\n'
comment|'#               providing compatibility'
nl|'\n'
name|'for'
name|'name'
name|'in'
name|'twistd_handlers'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|"'opt_'"
op|'+'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'takesArg'
op|'='
name|'not'
name|'usage'
op|'.'
name|'flagFunction'
op|'('
name|'method'
op|','
name|'name'
op|')'
newline|'\n'
name|'doc'
op|'='
name|'getattr'
op|'('
name|'method'
op|','
string|"'__doc__'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'doc'
op|':'
newline|'\n'
indent|'                    '
name|'doc'
op|'='
string|"'undocumented'"
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'takesArg'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'name'
name|'not'
name|'in'
name|'FLAGS'
op|':'
newline|'\n'
indent|'                        '
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
name|'name'
op|','
name|'None'
op|','
name|'doc'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_flagHandlers'
op|'['
name|'name'
op|']'
op|'='
name|'method'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'name'
name|'not'
name|'in'
name|'FLAGS'
op|':'
newline|'\n'
indent|'                        '
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
name|'name'
op|','
name|'None'
op|','
name|'doc'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_paramHandlers'
op|'['
name|'name'
op|']'
op|'='
name|'method'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_doHandlers
dedent|''
dedent|''
dedent|''
name|'def'
name|'_doHandlers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'flag'
op|','
name|'handler'
name|'in'
name|'self'
op|'.'
name|'_flagHandlers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'self'
op|'['
name|'flag'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'handler'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'param'
op|','
name|'handler'
name|'in'
name|'self'
op|'.'
name|'_paramHandlers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'self'
op|'['
name|'param'
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'handler'
op|'('
name|'self'
op|'['
name|'param'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
dedent|''
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'FLAGS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|parseOptions
dedent|''
name|'def'
name|'parseOptions'
op|'('
name|'self'
op|','
name|'options'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'options'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'options'
op|'='
name|'sys'
op|'.'
name|'argv'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'options'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
name|'FLAGS'
op|'('
name|'options'
op|')'
newline|'\n'
name|'argv'
op|'='
name|'args'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
comment|'# ignore subcommands'
nl|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'parseArgs'
op|'('
op|'*'
name|'argv'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'usage'
op|'.'
name|'UsageError'
op|'('
string|'"Wrong number of arguments."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'postOptions'
op|'('
op|')'
newline|'\n'
name|'return'
name|'args'
newline|'\n'
nl|'\n'
DECL|member|parseArgs
dedent|''
name|'def'
name|'parseArgs'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): figure out a decent way of dealing with args'
nl|'\n'
comment|'#return'
nl|'\n'
indent|'            '
name|'super'
op|'('
name|'TwistedOptionsToFlags'
op|','
name|'self'
op|')'
op|'.'
name|'parseArgs'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|postOptions
dedent|''
name|'def'
name|'postOptions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_doHandlers'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'TwistedOptionsToFlags'
op|','
name|'self'
op|')'
op|'.'
name|'postOptions'
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
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
name|'key'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'getattr'
op|'('
name|'FLAGS'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'AttributeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
name|'key'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'setattr'
op|'('
name|'FLAGS'
op|','
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'AttributeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_data'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
name|'key'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'getattr'
op|'('
name|'FLAGS'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'AttributeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'TwistedOptionsToFlags'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Stop the daemon\n    """'
newline|'\n'
comment|'# Get the pid from the pidfile'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'pf'
op|'='
name|'file'
op|'('
name|'pidfile'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'pid'
op|'='
name|'int'
op|'('
name|'pf'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
name|'pf'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'        '
name|'pid'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'pid'
op|':'
newline|'\n'
indent|'        '
name|'message'
op|'='
string|'"pidfile %s does not exist. Daemon not running?\\n"'
newline|'\n'
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
name|'message'
op|'%'
name|'pidfile'
op|')'
newline|'\n'
name|'return'
comment|'# not an error in a restart'
newline|'\n'
nl|'\n'
comment|'# Try killing the daemon process'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'while'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGKILL'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.1'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'OSError'
op|','
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'err'
op|'='
name|'str'
op|'('
name|'err'
op|')'
newline|'\n'
name|'if'
name|'err'
op|'.'
name|'find'
op|'('
string|'"No such process"'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'remove'
op|'('
name|'pidfile'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'str'
op|'('
name|'err'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serve
dedent|''
dedent|''
dedent|''
name|'def'
name|'serve'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Serving %s"'
op|'%'
name|'filename'
op|')'
newline|'\n'
name|'name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'filename'
op|')'
newline|'\n'
name|'OptionsClass'
op|'='
name|'WrapTwistedOptions'
op|'('
name|'TwistdServerOptions'
op|')'
newline|'\n'
name|'options'
op|'='
name|'OptionsClass'
op|'('
op|')'
newline|'\n'
name|'argv'
op|'='
name|'options'
op|'.'
name|'parseOptions'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'amqplib'"
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'WARN'
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'python'
op|'='
name|'filename'
newline|'\n'
name|'FLAGS'
op|'.'
name|'no_save'
op|'='
name|'True'
newline|'\n'
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'pidfile'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'pidfile'
op|'='
string|"'%s.pid'"
op|'%'
name|'name'
newline|'\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'pidfile'
op|'.'
name|'endswith'
op|'('
string|"'twistd.pid'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'pidfile'
op|'='
name|'FLAGS'
op|'.'
name|'pidfile'
op|'.'
name|'replace'
op|'('
string|"'twistd.pid'"
op|','
string|"'%s.pid'"
op|'%'
name|'name'
op|')'
newline|'\n'
comment|"# NOTE(vish): if we're running nodaemon, redirect the log to stdout"
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'nodaemon'
name|'and'
name|'not'
name|'FLAGS'
op|'.'
name|'logfile'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'logfile'
op|'='
string|'"-"'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'logfile'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'logfile'
op|'='
string|"'%s.log'"
op|'%'
name|'name'
newline|'\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'logfile'
op|'.'
name|'endswith'
op|'('
string|"'twistd.log'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'logfile'
op|'='
name|'FLAGS'
op|'.'
name|'logfile'
op|'.'
name|'replace'
op|'('
string|"'twistd.log'"
op|','
string|"'%s.log'"
op|'%'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'prefix'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'prefix'
op|'='
name|'name'
newline|'\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'prefix'
op|'.'
name|'endswith'
op|'('
string|"'twisted'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'prefix'
op|'='
name|'FLAGS'
op|'.'
name|'prefix'
op|'.'
name|'replace'
op|'('
string|"'twisted'"
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'action'
op|'='
string|"'start'"
newline|'\n'
name|'if'
name|'len'
op|'('
name|'argv'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
name|'argv'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'action'
op|'=='
string|"'stop'"
op|':'
newline|'\n'
indent|'        '
name|'stop'
op|'('
name|'FLAGS'
op|'.'
name|'pidfile'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'action'
op|'=='
string|"'restart'"
op|':'
newline|'\n'
indent|'        '
name|'stop'
op|'('
name|'FLAGS'
op|'.'
name|'pidfile'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'action'
op|'=='
string|"'start'"
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|"'usage: %s [options] [start|stop|restart]'"
op|'%'
name|'argv'
op|'['
number|'0'
op|']'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|class|NoNewlineFormatter
dedent|''
name|'class'
name|'NoNewlineFormatter'
op|'('
name|'logging'
op|'.'
name|'Formatter'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Strips newlines from default formatter"""'
newline|'\n'
DECL|member|format
name|'def'
name|'format'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Grabs default formatter\'s output and strips newlines"""'
newline|'\n'
name|'data'
op|'='
name|'logging'
op|'.'
name|'Formatter'
op|'.'
name|'format'
op|'('
name|'self'
op|','
name|'record'
op|')'
newline|'\n'
name|'return'
name|'data'
op|'.'
name|'replace'
op|'('
string|'"\\n"'
op|','
string|'"--"'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(vish): syslog-ng doesn't handle newlines from trackbacks very well"
nl|'\n'
dedent|''
dedent|''
name|'formatter'
op|'='
name|'NoNewlineFormatter'
op|'('
nl|'\n'
string|"'(%(name)s): %(levelname)s %(message)s'"
op|')'
newline|'\n'
name|'handler'
op|'='
name|'logging'
op|'.'
name|'StreamHandler'
op|'('
name|'log'
op|'.'
name|'StdioOnnaStick'
op|'('
op|')'
op|')'
newline|'\n'
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'formatter'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'addHandler'
op|'('
name|'handler'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'WARNING'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Full set of FLAGS:"'
op|')'
newline|'\n'
name|'for'
name|'flag'
name|'in'
name|'FLAGS'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"%s : %s"'
op|'%'
op|'('
name|'flag'
op|','
name|'FLAGS'
op|'.'
name|'get'
op|'('
name|'flag'
op|','
name|'None'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'twistd'
op|'.'
name|'runApp'
op|'('
name|'options'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
