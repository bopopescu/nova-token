begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
string|'"""\r\nA connection to the VMware ESX platform.\r\n\r\n**Related Flags**\r\n\r\n:vmwareapi_host_ip:        IPAddress of VMware ESX server.\r\n:vmwareapi_host_username:  Username for connection to VMware ESX Server.\r\n:vmwareapi_host_password:  Password for connection to VMware ESX Server.\r\n:vmwareapi_task_poll_interval:  The interval (seconds) used for polling of\r\n                             remote tasks\r\n                             (default: 1.0).\r\n:vmwareapi_api_retry_count:  The API retry count in case of failure such as\r\n                             network failures (socket errors etc.)\r\n                             (default: 10).\r\n"""'
newline|'\r\n'
nl|'\r\n'
name|'import'
name|'time'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'vmops'
name|'import'
name|'VMWareVMOps'
newline|'\r\n'
nl|'\r\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.vmwareapi_conn"'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\r\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vmwareapi_host_ip'"
op|','
nl|'\r\n'
name|'None'
op|','
nl|'\r\n'
string|"'URL for connection to VMWare ESX host.'"
nl|'\r\n'
string|"'Required if connection_type is vmwareapi.'"
op|')'
newline|'\r\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vmwareapi_host_username'"
op|','
nl|'\r\n'
name|'None'
op|','
nl|'\r\n'
string|"'Username for connection to VMWare ESX host.'"
nl|'\r\n'
string|"'Used only if connection_type is vmwareapi.'"
op|')'
newline|'\r\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vmwareapi_host_password'"
op|','
nl|'\r\n'
name|'None'
op|','
nl|'\r\n'
string|"'Password for connection to VMWare ESX host.'"
nl|'\r\n'
string|"'Used only if connection_type is vmwareapi.'"
op|')'
newline|'\r\n'
name|'flags'
op|'.'
name|'DEFINE_float'
op|'('
string|"'vmwareapi_task_poll_interval'"
op|','
nl|'\r\n'
number|'5.0'
op|','
nl|'\r\n'
string|"'The interval used for polling of remote tasks '"
nl|'\r\n'
string|"'Used only if connection_type is vmwareapi'"
op|')'
newline|'\r\n'
name|'flags'
op|'.'
name|'DEFINE_float'
op|'('
string|"'vmwareapi_api_retry_count'"
op|','
nl|'\r\n'
number|'10'
op|','
nl|'\r\n'
string|"'The number of times we retry on failures, '"
nl|'\r\n'
string|"'e.g., socket error, etc.'"
nl|'\r\n'
string|"'Used only if connection_type is vmwareapi'"
op|')'
newline|'\r\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vmwareapi_vlan_interface'"
op|','
nl|'\r\n'
string|"'vmnic0'"
op|','
nl|'\r\n'
string|"'Physical ethernet adapter name for vlan networking'"
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|variable|TIME_BETWEEN_API_CALL_RETRIES
name|'TIME_BETWEEN_API_CALL_RETRIES'
op|'='
number|'2.0'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|Failure
name|'class'
name|'Failure'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Base Exception class for handling task failures"""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'details'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'details'
op|'='
name|'details'
newline|'\r\n'
nl|'\r\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'details'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_connection
dedent|''
dedent|''
name|'def'
name|'get_connection'
op|'('
name|'_'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Sets up the ESX host connection."""'
newline|'\r\n'
name|'host_ip'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_host_ip'
newline|'\r\n'
name|'host_username'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_host_username'
newline|'\r\n'
name|'host_password'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_host_password'
newline|'\r\n'
name|'api_retry_count'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_api_retry_count'
newline|'\r\n'
name|'if'
name|'not'
name|'host_ip'
name|'or'
name|'host_username'
name|'is'
name|'None'
name|'or'
name|'host_password'
name|'is'
name|'None'
op|':'
newline|'\r\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Must specify vmwareapi_host_ip,"'
nl|'\r\n'
string|'"vmwareapi_host_username "'
nl|'\r\n'
string|'"and vmwareapi_host_password to use"'
nl|'\r\n'
string|'"connection_type=vmwareapi"'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'return'
name|'VMWareESXConnection'
op|'('
name|'host_ip'
op|','
name|'host_username'
op|','
name|'host_password'
op|','
nl|'\r\n'
name|'api_retry_count'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VMWareESXConnection
dedent|''
name|'class'
name|'VMWareESXConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""The ESX host connection object"""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host_ip'
op|','
name|'host_username'
op|','
name|'host_password'
op|','
nl|'\r\n'
name|'api_retry_count'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'session'
op|'='
name|'VMWareAPISession'
op|'('
name|'host_ip'
op|','
name|'host_username'
op|','
name|'host_password'
op|','
nl|'\r\n'
name|'api_retry_count'
op|','
name|'scheme'
op|'='
name|'scheme'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'VMWareVMOps'
op|'('
name|'session'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Do the initialization that needs to be done"""'
newline|'\r\n'
comment|'#FIXME(sateesh): implement this'
nl|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""List VM instances"""'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Create VM instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'spawn'
op|'('
name|'instance'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Create snapshot from a running VM instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'snapshot'
op|'('
name|'instance'
op|','
name|'name'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Reboot VM instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'reboot'
op|'('
name|'instance'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Destroy VM instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Pause VM instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'pause'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Unpause paused VM instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'unpause'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Suspend the specified instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'suspend'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|resume
dedent|''
name|'def'
name|'resume'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Resume the suspended VM instance"""'
newline|'\r\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'resume'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Return info about the VM instance"""'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance_id'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Return data about VM diagnostics"""'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Return snapshot of console"""'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_console_output'
op|'('
name|'instance'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_ajax_console
dedent|''
name|'def'
name|'get_ajax_console'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Return link to instance\'s ajax console"""'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_ajax_console'
op|'('
name|'instance'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Attach volume storage to VM instance"""'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Detach volume storage to VM instance"""'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_console_pool_info
dedent|''
name|'def'
name|'get_console_pool_info'
op|'('
name|'self'
op|','
name|'console_type'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Get info about the host on which the VM resides"""'
newline|'\r\n'
name|'return'
op|'{'
string|"'address'"
op|':'
name|'FLAGS'
op|'.'
name|'vmwareapi_host_ip'
op|','
nl|'\r\n'
string|"'username'"
op|':'
name|'FLAGS'
op|'.'
name|'vmwareapi_host_username'
op|','
nl|'\r\n'
string|"'password'"
op|':'
name|'FLAGS'
op|'.'
name|'vmwareapi_host_password'
op|'}'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VMWareAPISession
dedent|''
dedent|''
name|'class'
name|'VMWareAPISession'
op|'('
name|'object'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Sets up a session with the ESX host and handles all\r\n    the calls made to the host\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host_ip'
op|','
name|'host_username'
op|','
name|'host_password'
op|','
nl|'\r\n'
name|'api_retry_count'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_host_ip'
op|'='
name|'host_ip'
newline|'\r\n'
name|'self'
op|'.'
name|'_host_username'
op|'='
name|'host_username'
newline|'\r\n'
name|'self'
op|'.'
name|'_host_password'
op|'='
name|'host_password'
newline|'\r\n'
name|'self'
op|'.'
name|'api_retry_count'
op|'='
name|'api_retry_count'
newline|'\r\n'
name|'self'
op|'.'
name|'_scheme'
op|'='
name|'scheme'
newline|'\r\n'
name|'self'
op|'.'
name|'_session_id'
op|'='
name|'None'
newline|'\r\n'
name|'self'
op|'.'
name|'vim'
op|'='
name|'None'
newline|'\r\n'
name|'self'
op|'.'
name|'_create_session'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_get_vim_object
dedent|''
name|'def'
name|'_get_vim_object'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Create the VIM Object instance"""'
newline|'\r\n'
name|'return'
name|'vim'
op|'.'
name|'Vim'
op|'('
name|'protocol'
op|'='
name|'self'
op|'.'
name|'_scheme'
op|','
name|'host'
op|'='
name|'self'
op|'.'
name|'_host_ip'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_create_session
dedent|''
name|'def'
name|'_create_session'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Creates a session with the ESX host"""'
newline|'\r\n'
name|'while'
name|'True'
op|':'
newline|'\r\n'
indent|'            '
name|'try'
op|':'
newline|'\r\n'
comment|'# Login and setup the session with the ESX host for making'
nl|'\r\n'
comment|'# API calls'
nl|'\r\n'
indent|'                '
name|'self'
op|'.'
name|'vim'
op|'='
name|'self'
op|'.'
name|'_get_vim_object'
op|'('
op|')'
newline|'\r\n'
name|'session'
op|'='
name|'self'
op|'.'
name|'vim'
op|'.'
name|'Login'
op|'('
nl|'\r\n'
name|'self'
op|'.'
name|'vim'
op|'.'
name|'get_service_content'
op|'('
op|')'
op|'.'
name|'sessionManager'
op|','
nl|'\r\n'
name|'userName'
op|'='
name|'self'
op|'.'
name|'_host_username'
op|','
nl|'\r\n'
name|'password'
op|'='
name|'self'
op|'.'
name|'_host_password'
op|')'
newline|'\r\n'
comment|'# Terminate the earlier session, if possible ( For the sake of'
nl|'\r\n'
comment|'# preserving sessions as there is a limit to the number of'
nl|'\r\n'
comment|'# sessions we can have )'
nl|'\r\n'
name|'if'
name|'self'
op|'.'
name|'_session_id'
op|':'
newline|'\r\n'
indent|'                    '
name|'try'
op|':'
newline|'\r\n'
indent|'                        '
name|'self'
op|'.'
name|'vim'
op|'.'
name|'TerminateSession'
op|'('
nl|'\r\n'
name|'self'
op|'.'
name|'vim'
op|'.'
name|'get_service_content'
op|'('
op|')'
op|'.'
name|'sessionManager'
op|','
nl|'\r\n'
name|'sessionId'
op|'='
op|'['
name|'self'
op|'.'
name|'_session_id'
op|']'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'excep'
op|')'
newline|'\r\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_session_id'
op|'='
name|'session'
op|'.'
name|'key'
newline|'\r\n'
name|'return'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                '
name|'LOG'
op|'.'
name|'critical'
op|'('
name|'_'
op|'('
string|'"In vmwareapi:_create_session, "'
nl|'\r\n'
string|'"got this exception: %s"'
op|')'
op|'%'
name|'excep'
op|')'
newline|'\r\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'excep'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|__del__
dedent|''
dedent|''
dedent|''
name|'def'
name|'__del__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Logs-out the session."""'
newline|'\r\n'
comment|'# Logout to avoid un-necessary increase in session count at the'
nl|'\r\n'
comment|'# ESX host'
nl|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'vim'
op|'.'
name|'Logout'
op|'('
name|'self'
op|'.'
name|'vim'
op|'.'
name|'get_service_content'
op|'('
op|')'
op|'.'
name|'sessionManager'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\r\n'
indent|'            '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|_is_vim_object
dedent|''
dedent|''
name|'def'
name|'_is_vim_object'
op|'('
name|'self'
op|','
name|'module'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Check if the module is a VIM Object instance"""'
newline|'\r\n'
name|'return'
name|'isinstance'
op|'('
name|'module'
op|','
name|'vim'
op|'.'
name|'Vim'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_call_method
dedent|''
name|'def'
name|'_call_method'
op|'('
name|'self'
op|','
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Calls a method within the module specified with\r\n        args provided\r\n        """'
newline|'\r\n'
name|'args'
op|'='
name|'list'
op|'('
name|'args'
op|')'
newline|'\r\n'
name|'retry_count'
op|'='
number|'0'
newline|'\r\n'
name|'exc'
op|'='
name|'None'
newline|'\r\n'
name|'while'
name|'True'
op|':'
newline|'\r\n'
indent|'            '
name|'try'
op|':'
newline|'\r\n'
indent|'                '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_is_vim_object'
op|'('
name|'module'
op|')'
op|':'
newline|'\r\n'
comment|'#If it is not the first try, then get the latest vim object'
nl|'\r\n'
indent|'                    '
name|'if'
name|'retry_count'
op|'>'
number|'0'
op|':'
newline|'\r\n'
indent|'                        '
name|'args'
op|'='
name|'args'
op|'['
number|'1'
op|':'
op|']'
newline|'\r\n'
dedent|''
name|'args'
op|'='
op|'['
name|'self'
op|'.'
name|'vim'
op|']'
op|'+'
name|'args'
newline|'\r\n'
dedent|''
name|'retry_count'
op|'+='
number|'1'
newline|'\r\n'
name|'temp_module'
op|'='
name|'module'
newline|'\r\n'
nl|'\r\n'
name|'for'
name|'method_elem'
name|'in'
name|'method'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
op|':'
newline|'\r\n'
indent|'                    '
name|'temp_module'
op|'='
name|'getattr'
op|'('
name|'temp_module'
op|','
name|'method_elem'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'ret_val'
op|'='
name|'temp_module'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\r\n'
name|'return'
name|'ret_val'
newline|'\r\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'VimFaultException'
op|','
name|'excep'
op|':'
newline|'\r\n'
comment|'# If it is a Session Fault Exception, it may point'
nl|'\r\n'
comment|'# to a session gone bad. So we try re-creating a session'
nl|'\r\n'
comment|'# and then proceeding ahead with the call.'
nl|'\r\n'
indent|'                '
name|'exc'
op|'='
name|'excep'
newline|'\r\n'
name|'if'
name|'error_util'
op|'.'
name|'FAULT_NOT_AUTHENTICATED'
name|'in'
name|'excep'
op|'.'
name|'fault_list'
op|':'
newline|'\r\n'
indent|'                    '
name|'self'
op|'.'
name|'_create_session'
op|'('
op|')'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
comment|'#No re-trying for errors for API call has gone through'
nl|'\r\n'
comment|"#and is the caller's fault. Caller should handle these"
nl|'\r\n'
comment|'#errors. e.g, InvalidArgument fault.'
nl|'\r\n'
indent|'                    '
name|'break'
newline|'\r\n'
dedent|''
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|','
name|'excep'
op|':'
newline|'\r\n'
comment|'# For exceptions which may come because of session overload,'
nl|'\r\n'
comment|'# we retry'
nl|'\r\n'
indent|'                '
name|'exc'
op|'='
name|'excep'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\r\n'
comment|'# If it is a proper exception, say not having furnished'
nl|'\r\n'
comment|'# proper data in the SOAP call or the retry limit having'
nl|'\r\n'
comment|'# exceeded, we raise the exception'
nl|'\r\n'
indent|'                '
name|'exc'
op|'='
name|'excep'
newline|'\r\n'
name|'break'
newline|'\r\n'
comment|'# If retry count has been reached then break and'
nl|'\r\n'
comment|'# raise the exception'
nl|'\r\n'
dedent|''
name|'if'
name|'retry_count'
op|'>'
name|'self'
op|'.'
name|'api_retry_count'
op|':'
newline|'\r\n'
indent|'                '
name|'break'
newline|'\r\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
name|'TIME_BETWEEN_API_CALL_RETRIES'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'LOG'
op|'.'
name|'critical'
op|'('
name|'_'
op|'('
string|'"In vmwareapi:_call_method, "'
nl|'\r\n'
string|'"got this exception: %s"'
op|')'
op|'%'
name|'exc'
op|')'
newline|'\r\n'
name|'raise'
newline|'\r\n'
nl|'\r\n'
DECL|member|_get_vim
dedent|''
name|'def'
name|'_get_vim'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Gets the VIM object reference"""'
newline|'\r\n'
name|'if'
name|'self'
op|'.'
name|'vim'
name|'is'
name|'None'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'_create_session'
op|'('
op|')'
newline|'\r\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'vim'
newline|'\r\n'
nl|'\r\n'
DECL|member|_wait_for_task
dedent|''
name|'def'
name|'_wait_for_task'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'task_ref'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Return a Deferred that will give the result of the given task.\r\n        The task is polled until it completes.\r\n        """'
newline|'\r\n'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\r\n'
name|'loop'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'instance_id'
op|','
name|'task_ref'
op|','
nl|'\r\n'
name|'done'
op|')'
newline|'\r\n'
name|'loop'
op|'.'
name|'start'
op|'('
name|'FLAGS'
op|'.'
name|'vmwareapi_task_poll_interval'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\r\n'
name|'ret_val'
op|'='
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\r\n'
name|'loop'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'return'
name|'ret_val'
newline|'\r\n'
nl|'\r\n'
DECL|member|_poll_task
dedent|''
name|'def'
name|'_poll_task'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'task_ref'
op|','
name|'done'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Poll the given task, and fires the given Deferred if we\r\n        get a result.\r\n        """'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'task_info'
op|'='
name|'self'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_property"'
op|','
nl|'\r\n'
name|'task_ref'
op|','
string|'"Task"'
op|','
string|'"info"'
op|')'
newline|'\r\n'
name|'task_name'
op|'='
name|'task_info'
op|'.'
name|'name'
newline|'\r\n'
name|'action'
op|'='
name|'dict'
op|'('
nl|'\r\n'
name|'instance_id'
op|'='
name|'int'
op|'('
name|'instance_id'
op|')'
op|','
nl|'\r\n'
name|'action'
op|'='
name|'task_name'
op|'['
number|'0'
op|':'
number|'255'
op|']'
op|','
nl|'\r\n'
name|'error'
op|'='
name|'None'
op|')'
newline|'\r\n'
name|'if'
name|'task_info'
op|'.'
name|'state'
name|'in'
op|'['
string|"'queued'"
op|','
string|"'running'"
op|']'
op|':'
newline|'\r\n'
indent|'                '
name|'return'
newline|'\r\n'
dedent|''
name|'elif'
name|'task_info'
op|'.'
name|'state'
op|'=='
string|"'success'"
op|':'
newline|'\r\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Task [%(task_name)s] %(task_ref)s "'
nl|'\r\n'
string|'"status: success"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\r\n'
name|'done'
op|'.'
name|'send'
op|'('
string|'"success"'
op|')'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'                '
name|'error_info'
op|'='
name|'str'
op|'('
name|'task_info'
op|'.'
name|'error'
op|'.'
name|'localizedMessage'
op|')'
newline|'\r\n'
name|'action'
op|'['
string|'"error"'
op|']'
op|'='
name|'error_info'
newline|'\r\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Task [%(task_name)s] %(task_ref)s "'
nl|'\r\n'
string|'"status: error %(error_info)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\r\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'Exception'
op|'('
name|'error_info'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'db'
op|'.'
name|'instance_action_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'action'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"In vmwareapi:_poll_task, Got this error %s"'
op|')'
op|'%'
name|'excep'
op|')'
newline|'\r\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'excep'
op|')'
newline|'\r\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
