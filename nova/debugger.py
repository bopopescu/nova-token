begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
comment|'# NOTE(markmc): this is imported before monkey patching in nova.cmd'
nl|'\n'
comment|'# so we avoid extra imports here'
nl|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|enabled
name|'def'
name|'enabled'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
string|"'--remote_debug-host'"
name|'in'
name|'sys'
op|'.'
name|'argv'
name|'and'
nl|'\n'
string|"'--remote_debug-port'"
name|'in'
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_cli_opts
dedent|''
name|'def'
name|'register_cli_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'cli_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'host'"
op|','
nl|'\n'
name|'help'
op|'='
string|"'Debug host (IP or name) to connect. Note '"
nl|'\n'
string|"'that using the remote debug option changes how '"
nl|'\n'
string|"'Nova uses the eventlet library to support async IO. '"
nl|'\n'
string|"'This could result in failures that do not occur '"
nl|'\n'
string|"'under normal operation. Use at your own risk.'"
op|')'
op|','
nl|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'port'"
op|','
nl|'\n'
name|'help'
op|'='
string|"'Debug port to connect. Note '"
nl|'\n'
string|"'that using the remote debug option changes how '"
nl|'\n'
string|"'Nova uses the eventlet library to support async IO. '"
nl|'\n'
string|"'This could result in failures that do not occur '"
nl|'\n'
string|"'under normal operation. Use at your own risk.'"
op|')'
nl|'\n'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'register_cli_opts'
op|'('
name|'cli_opts'
op|','
string|"'remote_debug'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init
dedent|''
name|'def'
name|'init'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
comment|'# NOTE(markmc): gracefully handle the CLI options not being registered'
nl|'\n'
name|'if'
string|"'remote_debug'"
name|'not'
name|'in'
name|'CONF'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
op|'('
name|'CONF'
op|'.'
name|'remote_debug'
op|'.'
name|'host'
name|'and'
name|'CONF'
op|'.'
name|'remote_debug'
op|'.'
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
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
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Listening on %(host)s:%(port)s for debug connection'"
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'remote_debug'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'CONF'
op|'.'
name|'remote_debug'
op|'.'
name|'port'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'pydev'
name|'import'
name|'pydevd'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'        '
name|'import'
name|'pydevd'
newline|'\n'
dedent|''
name|'pydevd'
op|'.'
name|'settrace'
op|'('
name|'host'
op|'='
name|'CONF'
op|'.'
name|'remote_debug'
op|'.'
name|'host'
op|','
nl|'\n'
name|'port'
op|'='
name|'CONF'
op|'.'
name|'remote_debug'
op|'.'
name|'port'
op|','
nl|'\n'
name|'stdoutToServer'
op|'='
name|'False'
op|','
nl|'\n'
name|'stderrToServer'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'WARNING: Using the remote debug option changes how '"
nl|'\n'
string|"'Nova uses the eventlet library to support async IO. This '"
nl|'\n'
string|"'could result in failures that do not occur under normal '"
nl|'\n'
string|"'operation. Use at your own risk.'"
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
