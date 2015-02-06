begin_unit
comment|'#'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
comment|'#'
nl|'\n'
nl|'\n'
string|'"""\nBase RPC client and server common to all services.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'baseapi'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to the base api in any '"
nl|'\n'
string|"'service'"
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
DECL|variable|_NAMESPACE
name|'_NAMESPACE'
op|'='
string|"'baseapi'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseAPI
name|'class'
name|'BaseAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Client side of the base rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Add get_backdoor_port\n    """'
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
comment|'# baseapi was added in havana'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'BaseAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'namespace'
op|'='
name|'_NAMESPACE'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.0'"
op|')'
newline|'\n'
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
name|'baseapi'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'baseapi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'target'
op|','
name|'version_cap'
op|'='
name|'version_cap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ping
dedent|''
name|'def'
name|'ping'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'arg'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'arg_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'arg'
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'timeout'
op|'='
name|'timeout'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'ping'"
op|','
name|'arg'
op|'='
name|'arg_p'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_backdoor_port
dedent|''
name|'def'
name|'get_backdoor_port'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
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
name|'server'
op|'='
name|'host'
op|','
name|'version'
op|'='
string|"'1.1'"
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'get_backdoor_port'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseRPCAPI
dedent|''
dedent|''
name|'class'
name|'BaseRPCAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server side of the base RPC API."""'
newline|'\n'
nl|'\n'
DECL|variable|target
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'namespace'
op|'='
name|'_NAMESPACE'
op|','
name|'version'
op|'='
string|"'1.1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'service_name'
op|','
name|'backdoor_port'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service_name'
op|'='
name|'service_name'
newline|'\n'
name|'self'
op|'.'
name|'backdoor_port'
op|'='
name|'backdoor_port'
newline|'\n'
nl|'\n'
DECL|member|ping
dedent|''
name|'def'
name|'ping'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'arg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
op|'{'
string|"'service'"
op|':'
name|'self'
op|'.'
name|'service_name'
op|','
string|"'arg'"
op|':'
name|'arg'
op|'}'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'resp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_backdoor_port
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
