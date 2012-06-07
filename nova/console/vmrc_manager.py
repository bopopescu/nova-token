begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""VMRC Console Manager."""'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'cfg'
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
name|'virt'
name|'import'
name|'vmwareapi_conn'
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
DECL|variable|vmrc_manager_opts
name|'vmrc_manager_opts'
op|'='
op|'['
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
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Publicly visible name for this console host'"
op|')'
op|','
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
string|"'nova.console.vmrc.VMRCConsole'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for the console'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'vmrc_manager_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleVMRCManager
name|'class'
name|'ConsoleVMRCManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manager to handle VMRC connections for accessing instance consoles."""'
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
name|'self'
op|'.'
name|'driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'console_driver'
op|')'
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
name|'super'
op|'('
name|'ConsoleVMRCManager'
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
name|'sessions'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vim_session
dedent|''
name|'def'
name|'_get_vim_session'
op|'('
name|'self'
op|','
name|'pool'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get VIM session for the pool specified."""'
newline|'\n'
name|'vim_session'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'pool'
op|'['
string|"'id'"
op|']'
name|'not'
name|'in'
name|'self'
op|'.'
name|'sessions'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vim_session'
op|'='
name|'vmwareapi_conn'
op|'.'
name|'VMWareAPISession'
op|'('
nl|'\n'
name|'pool'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
name|'pool'
op|'['
string|"'username'"
op|']'
op|','
nl|'\n'
name|'pool'
op|'['
string|"'password'"
op|']'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'console_vmrc_error_retries'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sessions'
op|'['
name|'pool'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'vim_session'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'sessions'
op|'['
name|'pool'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_generate_console
dedent|''
name|'def'
name|'_generate_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'pool'
op|','
name|'name'
op|','
name|'instance_id'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up console for the instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Adding console'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'password'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'generate_password'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_vim_session'
op|'('
name|'pool'
op|')'
op|','
nl|'\n'
name|'pool'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'console_data'
op|'='
op|'{'
string|"'instance_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'instance_id'
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
name|'console_data'
op|'['
string|"'port'"
op|']'
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
name|'return'
name|'console'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
DECL|member|add_console
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
string|'"""Adds a console for the instance.\n\n        If it is one time password, then we generate new console credentials.\n\n        """'
newline|'\n'
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
name|'if'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'is_otp'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'console'
op|'='
name|'self'
op|'.'
name|'_generate_console'
op|'('
name|'context'
op|','
nl|'\n'
name|'pool'
op|','
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'console'
op|'='
name|'self'
op|'.'
name|'_generate_console'
op|'('
name|'context'
op|','
nl|'\n'
name|'pool'
op|','
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'console'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
DECL|member|remove_console
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
string|'"""Removes a console entry."""'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Removing console '"
nl|'\n'
string|"'%(console_id)s.'"
op|')'
op|'%'
op|'{'
string|"'console_id'"
op|':'
name|'console_id'
op|'}'
op|')'
newline|'\n'
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
string|'"""Gets console pool info for the instance."""'
newline|'\n'
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
indent|'            '
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
comment|'# ESX Address or Proxy Address'
nl|'\n'
name|'public_host_name'
op|'='
name|'pool_info'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'console_public_hostname'
op|':'
newline|'\n'
indent|'                '
name|'public_host_name'
op|'='
name|'FLAGS'
op|'.'
name|'console_public_hostname'
newline|'\n'
dedent|''
name|'pool_info'
op|'['
string|"'public_hostname'"
op|']'
op|'='
name|'public_host_name'
newline|'\n'
name|'pool_info'
op|'['
string|"'console_type'"
op|']'
op|'='
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
dedent|''
dedent|''
endmarker|''
end_unit
