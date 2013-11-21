begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'import'
name|'paramiko'
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
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
DECL|variable|CONNECTION_TIMEOUT
name|'CONNECTION_TIMEOUT'
op|'='
number|'60'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConnectionFailed
name|'class'
name|'ConnectionFailed'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'        '
name|'msg_fmt'
op|'='
name|'_'
op|'('
string|"'Connection failed'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Connection
dedent|''
name|'class'
name|'Connection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'username'
op|','
name|'password'
op|','
name|'port'
op|'='
number|'22'
op|','
name|'keyfile'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'username'
op|'='
name|'username'
newline|'\n'
name|'self'
op|'.'
name|'password'
op|'='
name|'password'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'port'
newline|'\n'
name|'self'
op|'.'
name|'keyfile'
op|'='
name|'keyfile'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ssh_connect
dedent|''
dedent|''
name|'def'
name|'ssh_connect'
op|'('
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Method to connect to remote system using ssh protocol.\n\n    :param connection: a Connection object.\n    :returns: paramiko.SSHClient -- an active ssh connection.\n    :raises: ConnectionFailed\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ssh'
op|'='
name|'paramiko'
op|'.'
name|'SSHClient'
op|'('
op|')'
newline|'\n'
name|'ssh'
op|'.'
name|'set_missing_host_key_policy'
op|'('
name|'paramiko'
op|'.'
name|'AutoAddPolicy'
op|'('
op|')'
op|')'
newline|'\n'
name|'ssh'
op|'.'
name|'connect'
op|'('
name|'connection'
op|'.'
name|'host'
op|','
nl|'\n'
name|'username'
op|'='
name|'connection'
op|'.'
name|'username'
op|','
nl|'\n'
name|'password'
op|'='
name|'connection'
op|'.'
name|'password'
op|','
nl|'\n'
name|'port'
op|'='
name|'connection'
op|'.'
name|'port'
op|','
nl|'\n'
name|'key_filename'
op|'='
name|'connection'
op|'.'
name|'keyfile'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'CONNECTION_TIMEOUT'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"SSH connection with %s established successfully."'
op|'%'
nl|'\n'
name|'connection'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
comment|'# send TCP keepalive packets every 20 seconds'
nl|'\n'
name|'ssh'
op|'.'
name|'get_transport'
op|'('
op|')'
op|'.'
name|'set_keepalive'
op|'('
number|'20'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'ssh'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Connection error'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'ConnectionFailed'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
