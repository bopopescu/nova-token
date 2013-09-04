begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
string|'"""\nClient side of the consoleauth RPC API.\n"""'
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
name|'rpcclient'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'consoleauth'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to consoleauth services'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|"'upgrade_levels'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAuthAPI
name|'class'
name|'ConsoleAuthAPI'
op|'('
name|'rpcclient'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the consoleauth rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Added get_backdoor_port()\n        1.2 - Added instance_uuid to authorize_console, and\n              delete_tokens_for_instance\n\n        ... Grizzly supports message version 1.2.  So, any changes to existing\n        methods in 2.x after that point should be done such that they can\n        handle the version_cap being set to 1.2.\n    '''"
newline|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# NOTE(russellb): This is the default minimum version that the server'
nl|'\n'
comment|'# (manager) side must implement unless otherwise specified using a version'
nl|'\n'
comment|'# argument to self.call()/cast()/etc. here.  It should be left as X.0 where'
nl|'\n'
comment|'# X is the current major API version (1.0, 2.0, ...).  For more information'
nl|'\n'
comment|'# about rpc API versioning, see the docs in'
nl|'\n'
comment|'# openstack/common/rpc/dispatcher.py.'
nl|'\n'
comment|'#'
nl|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'1.2'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version_cap'
op|'='
name|'self'
op|'.'
name|'VERSION_ALIASES'
op|'.'
name|'get'
op|'('
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'consoleauth'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'consoleauth'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ConsoleAuthAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
nl|'\n'
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'consoleauth_topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'version_cap'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'self'
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
name|'ctxt'
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
op|','
name|'instance_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|"# The remote side doesn't return anything, but we want to block"
nl|'\n'
comment|'# until it completes.'
nl|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'authorize_console'"
op|','
nl|'\n'
name|'token'
op|'='
name|'token'
op|','
name|'console_type'
op|'='
name|'console_type'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'port'
op|'='
name|'port'
op|','
nl|'\n'
name|'internal_access_path'
op|'='
name|'internal_access_path'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
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
name|'ctxt'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'client'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'check_token'"
op|','
name|'token'
op|'='
name|'token'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_tokens_for_instance
dedent|''
name|'def'
name|'delete_tokens_for_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'delete_tokens_for_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
