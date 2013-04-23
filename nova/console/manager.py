begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack Foundation'
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
string|'"""Console Proxy Service."""'
newline|'\n'
nl|'\n'
name|'import'
name|'socket'
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
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'importutils'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|console_manager_opts
name|'console_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.console.xvp.XVPConsoleProxy'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for the console proxy'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'stub_compute'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Stub calls to compute worker for tests'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_public_hostname'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Publicly visible name for this console host'"
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
name|'console_manager_opts'
op|')'
newline|'\n'
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
DECL|class|ConsoleProxyManager
name|'class'
name|'ConsoleProxyManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sets up and tears down any console proxy connections.\n\n    Needed for accessing instance consoles securely.\n\n    """'
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
name|'console_driver'
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
name|'if'
name|'not'
name|'console_driver'
op|':'
newline|'\n'
indent|'            '
name|'console_driver'
op|'='
name|'CONF'
op|'.'
name|'console_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'console_driver'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ConsoleProxyManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'service_name'
op|'='
string|"'console'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'='
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_console
dedent|''
name|'def'
name|'add_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'password'
op|'='
name|'None'
op|','
nl|'\n'
name|'port'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'pool'
op|'='
name|'self'
op|'.'
name|'get_pool_for_instance_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'console'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_get_by_pool_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'pool'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Adding console'"
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'password'
op|':'
newline|'\n'
indent|'                '
name|'password'
op|'='
name|'utils'
op|'.'
name|'generate_password'
op|'('
number|'8'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'port'
op|':'
newline|'\n'
indent|'                '
name|'port'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_port'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'console_data'
op|'='
op|'{'
string|"'instance_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'password'
op|','
nl|'\n'
string|"'pool_id'"
op|':'
name|'pool'
op|'['
string|"'id'"
op|']'
op|'}'
newline|'\n'
name|'if'
name|'port'
op|':'
newline|'\n'
indent|'                '
name|'console_data'
op|'['
string|"'port'"
op|']'
op|'='
name|'port'
newline|'\n'
dedent|''
name|'console'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_create'
op|'('
name|'context'
op|','
name|'console_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'setup_console'
op|'('
name|'context'
op|','
name|'console'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'console'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|remove_console
dedent|''
name|'def'
name|'remove_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'console_id'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'console'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_get'
op|'('
name|'context'
op|','
name|'console_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Tried to remove non-existent console '"
nl|'\n'
string|"'%(console_id)s.'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'console_id'"
op|':'
name|'console_id'
op|'}'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_delete'
op|'('
name|'context'
op|','
name|'console_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'teardown_console'
op|'('
name|'context'
op|','
name|'console'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_pool_for_instance_host
dedent|''
name|'def'
name|'get_pool_for_instance_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'console_type'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'console_type'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_pool_get_by_host_type'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'console_type'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
comment|'#NOTE(mdragon): Right now, the only place this info exists is the'
nl|'\n'
comment|"#               compute worker's flagfile, at least for"
nl|'\n'
comment|'#               xenserver. Thus we ned to ask.'
nl|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'stub_compute'
op|':'
newline|'\n'
indent|'                '
name|'pool_info'
op|'='
op|'{'
string|"'address'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'username'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'1234pass'"
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'pool_info'
op|'='
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'get_console_pool_info'
op|'('
name|'context'
op|','
nl|'\n'
name|'console_type'
op|','
name|'instance_host'
op|')'
newline|'\n'
dedent|''
name|'pool_info'
op|'['
string|"'password'"
op|']'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'fix_pool_password'
op|'('
nl|'\n'
name|'pool_info'
op|'['
string|"'password'"
op|']'
op|')'
newline|'\n'
name|'pool_info'
op|'['
string|"'host'"
op|']'
op|'='
name|'self'
op|'.'
name|'host'
newline|'\n'
name|'pool_info'
op|'['
string|"'public_hostname'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'console_public_hostname'
newline|'\n'
name|'pool_info'
op|'['
string|"'console_type'"
op|']'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'console_type'
newline|'\n'
name|'pool_info'
op|'['
string|"'compute_host'"
op|']'
op|'='
name|'instance_host'
newline|'\n'
name|'pool'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_pool_create'
op|'('
name|'context'
op|','
name|'pool_info'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'pool'
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
