begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation.'
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
string|'"""\nSystem-level utilities and helper functions.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'shlex'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
op|'.'
name|'green'
name|'import'
name|'subprocess'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
nl|'\n'
DECL|class|UnknownArgumentError
name|'class'
name|'UnknownArgumentError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'UnknownArgumentError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessExecutionError
dedent|''
dedent|''
name|'class'
name|'ProcessExecutionError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stdout'
op|'='
name|'None'
op|','
name|'stderr'
op|'='
name|'None'
op|','
name|'exit_code'
op|'='
name|'None'
op|','
name|'cmd'
op|'='
name|'None'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'description'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'description'
op|'='
string|'"Unexpected error while running command."'
newline|'\n'
dedent|''
name|'if'
name|'exit_code'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'exit_code'
op|'='
string|"'-'"
newline|'\n'
dedent|''
name|'message'
op|'='
op|'('
string|'"%s\\nCommand: %s\\nExit code: %s\\nStdout: %r\\nStderr: %r"'
nl|'\n'
op|'%'
op|'('
name|'description'
op|','
name|'cmd'
op|','
name|'exit_code'
op|','
name|'stdout'
op|','
name|'stderr'
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ProcessExecutionError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
dedent|''
dedent|''
name|'def'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Helper method to shell out and execute a command through subprocess with\n    optional retry.\n\n    :param cmd:             Passed to subprocess.Popen.\n    :type cmd:              string\n    :param process_input:   Send to opened process.\n    :type proces_input:     string\n    :param check_exit_code: Defaults to 0. Will raise\n                            :class:`ProcessExecutionError`\n                            if the command exits without returning this value\n                            as a returncode\n    :type check_exit_code:  int\n    :param delay_on_retry:  True | False. Defaults to True. If set to True,\n                            wait a short amount of time before retrying.\n    :type delay_on_retry:   boolean\n    :param attempts:        How many times to retry cmd.\n    :type attempts:         int\n    :param run_as_root:     True | False. Defaults to False. If set to True,\n                            the command is prefixed by the command specified\n                            in the root_helper kwarg.\n    :type run_as_root:      boolean\n    :param root_helper:     command to prefix all cmd\'s with\n    :type root_helper:      string\n    :returns:               (stdout, stderr) from process execution\n    :raises:                :class:`UnknownArgumentError` on\n                            receiving unknown arguments\n    :raises:                :class:`ProcessExecutionError`\n    """'
newline|'\n'
nl|'\n'
name|'process_input'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'process_input'"
op|','
name|'None'
op|')'
newline|'\n'
name|'check_exit_code'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'check_exit_code'"
op|','
number|'0'
op|')'
newline|'\n'
name|'delay_on_retry'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'delay_on_retry'"
op|','
name|'True'
op|')'
newline|'\n'
name|'attempts'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'attempts'"
op|','
number|'1'
op|')'
newline|'\n'
name|'run_as_root'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'run_as_root'"
op|','
name|'False'
op|')'
newline|'\n'
name|'root_helper'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'root_helper'"
op|','
string|"''"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'UnknownArgumentError'
op|'('
name|'_'
op|'('
string|"'Got unknown keyword args '"
nl|'\n'
string|"'to utils.execute: %r'"
op|')'
op|'%'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'run_as_root'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
name|'shlex'
op|'.'
name|'split'
op|'('
name|'root_helper'
op|')'
op|'+'
name|'list'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'cmd'
op|'='
name|'map'
op|'('
name|'str'
op|','
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
name|'while'
name|'attempts'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'attempts'
op|'-='
number|'1'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Running cmd (subprocess): %s'"
op|')'
op|','
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'_PIPE'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
comment|'# pylint: disable=E1101'
newline|'\n'
name|'obj'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
nl|'\n'
name|'stdin'
op|'='
name|'_PIPE'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'_PIPE'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'_PIPE'
op|','
nl|'\n'
name|'close_fds'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'process_input'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'obj'
op|'.'
name|'communicate'
op|'('
name|'process_input'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'obj'
op|'.'
name|'communicate'
op|'('
op|')'
newline|'\n'
dedent|''
name|'obj'
op|'.'
name|'stdin'
op|'.'
name|'close'
op|'('
op|')'
comment|'# pylint: disable=E1101'
newline|'\n'
name|'_returncode'
op|'='
name|'obj'
op|'.'
name|'returncode'
comment|'# pylint: disable=E1101'
newline|'\n'
name|'if'
name|'_returncode'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Result was %s'"
op|')'
op|'%'
name|'_returncode'
op|')'
newline|'\n'
name|'if'
op|'('
name|'isinstance'
op|'('
name|'check_exit_code'
op|','
name|'int'
op|')'
name|'and'
nl|'\n'
name|'not'
name|'isinstance'
op|'('
name|'check_exit_code'
op|','
name|'bool'
op|')'
name|'and'
nl|'\n'
name|'_returncode'
op|'!='
name|'check_exit_code'
op|')'
op|':'
newline|'\n'
indent|'                    '
op|'('
name|'stdout'
op|','
name|'stderr'
op|')'
op|'='
name|'result'
newline|'\n'
name|'raise'
name|'ProcessExecutionError'
op|'('
name|'exit_code'
op|'='
name|'_returncode'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'stdout'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'stderr'
op|','
nl|'\n'
name|'cmd'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'except'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'attempts'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%r failed. Retrying.'"
op|')'
op|','
name|'cmd'
op|')'
newline|'\n'
name|'if'
name|'delay_on_retry'
op|':'
newline|'\n'
indent|'                    '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'20'
op|','
number|'200'
op|')'
op|'/'
number|'100.0'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# NOTE(termie): this appears to be necessary to let the subprocess'
nl|'\n'
comment|'#               call clean something up in between calls, without'
nl|'\n'
comment|'#               it two execute calls in a row hangs the second one'
nl|'\n'
indent|'            '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
