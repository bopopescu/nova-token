begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 OpenStack, LLC.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""Auth Components for Consoles."""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
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
op|'.'
name|'common'
name|'import'
name|'memorycache'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
DECL|variable|consoleauth_opts
name|'consoleauth_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'console_token_ttl'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How many seconds before deleting tokens'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'consoleauth_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.consoleauth.manager.ConsoleAuthManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Manager for console auth'"
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
name|'consoleauth_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAuthManager
name|'class'
name|'ConsoleAuthManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages token based authentication."""'
newline|'\n'
nl|'\n'
DECL|variable|RPC_API_VERSION
name|'RPC_API_VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'scheduler_driver'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConsoleAuthManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc'
op|'='
name|'memorycache'
op|'.'
name|'get_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|authorize_console
dedent|''
name|'def'
name|'authorize_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'token'
op|','
name|'console_type'
op|','
name|'host'
op|','
name|'port'
op|','
nl|'\n'
name|'internal_access_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'token_dict'
op|'='
op|'{'
string|"'token'"
op|':'
name|'token'
op|','
nl|'\n'
string|"'console_type'"
op|':'
name|'console_type'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'port'
op|','
nl|'\n'
string|"'internal_access_path'"
op|':'
name|'internal_access_path'
op|','
nl|'\n'
string|"'last_activity_at'"
op|':'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'token_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'token'
op|'.'
name|'encode'
op|'('
string|"'UTF-8'"
op|')'
op|','
name|'data'
op|','
name|'CONF'
op|'.'
name|'console_token_ttl'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Received Token: %(token)s, %(token_dict)s)"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_token
dedent|''
name|'def'
name|'check_token'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'token_str'
op|'='
name|'self'
op|'.'
name|'mc'
op|'.'
name|'get'
op|'('
name|'token'
op|'.'
name|'encode'
op|'('
string|"'UTF-8'"
op|')'
op|')'
newline|'\n'
name|'token_valid'
op|'='
op|'('
name|'token_str'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Checking Token: %(token)s, %(token_valid)s)"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'token_valid'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'token_str'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_backdoor_port
dedent|''
dedent|''
name|'def'
name|'get_backdoor_port'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'backdoor_port'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
