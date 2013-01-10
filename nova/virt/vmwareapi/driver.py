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
string|'"""\nA connection to the VMware ESX platform.\n\n**Related Flags**\n\n:vmwareapi_host_ip:        IPAddress of VMware ESX server.\n:vmwareapi_host_username:  Username for connection to VMware ESX Server.\n:vmwareapi_host_password:  Password for connection to VMware ESX Server.\n:vmwareapi_task_poll_interval:  The interval (seconds) used for polling of\n                             remote tasks\n                             (default: 1.0).\n:vmwareapi_api_retry_count:  The API retry count in case of failure such as\n                             network failures (socket errors etc.)\n                             (default: 10).\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vmops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'volumeops'
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
DECL|variable|vmwareapi_opts
name|'vmwareapi_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vmwareapi_host_ip'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'URL for connection to VMware ESX host. Required if '"
nl|'\n'
string|"'compute_driver is vmwareapi.VMwareESXDriver.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vmwareapi_host_username'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Username for connection to VMware ESX host. '"
nl|'\n'
string|"'Used only if compute_driver is '"
nl|'\n'
string|"'vmwareapi.VMwareESXDriver.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vmwareapi_host_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Password for connection to VMware ESX host. '"
nl|'\n'
string|"'Used only if compute_driver is '"
nl|'\n'
string|"'vmwareapi.VMwareESXDriver.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'vmwareapi_task_poll_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The interval used for polling of remote tasks. '"
nl|'\n'
string|"'Used only if compute_driver is '"
nl|'\n'
string|"'vmwareapi.VMwareESXDriver.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'vmwareapi_api_retry_count'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The number of times we retry on failures, e.g., '"
nl|'\n'
string|"'socket error, etc. '"
nl|'\n'
string|"'Used only if compute_driver is '"
nl|'\n'
string|"'vmwareapi.VMwareESXDriver.'"
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
name|'vmwareapi_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|TIME_BETWEEN_API_CALL_RETRIES
name|'TIME_BETWEEN_API_CALL_RETRIES'
op|'='
number|'2.0'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Failure
name|'class'
name|'Failure'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Exception class for handling task failures."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'details'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'details'
op|'='
name|'details'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'details'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareESXDriver
dedent|''
dedent|''
name|'class'
name|'VMwareESXDriver'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The ESX host connection object."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'virtapi'
op|','
name|'read_only'
op|'='
name|'False'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VMwareESXDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
nl|'\n'
name|'host_ip'
op|'='
name|'CONF'
op|'.'
name|'vmwareapi_host_ip'
newline|'\n'
name|'host_username'
op|'='
name|'CONF'
op|'.'
name|'vmwareapi_host_username'
newline|'\n'
name|'host_password'
op|'='
name|'CONF'
op|'.'
name|'vmwareapi_host_password'
newline|'\n'
name|'api_retry_count'
op|'='
name|'CONF'
op|'.'
name|'vmwareapi_api_retry_count'
newline|'\n'
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
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Must specify vmwareapi_host_ip,"'
nl|'\n'
string|'"vmwareapi_host_username "'
nl|'\n'
string|'"and vmwareapi_host_password to use"'
nl|'\n'
string|'"compute_driver=vmwareapi.VMwareESXDriver"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_session'
op|'='
name|'VMwareAPISession'
op|'('
name|'host_ip'
op|','
name|'host_username'
op|','
name|'host_password'
op|','
nl|'\n'
name|'api_retry_count'
op|','
name|'scheme'
op|'='
name|'scheme'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'volumeops'
op|'.'
name|'VMwareVolumeOps'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Do the initialization that needs to be done."""'
newline|'\n'
comment|'# FIXME(sateesh): implement this'
nl|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|legacy_nwinfo
dedent|''
name|'def'
name|'legacy_nwinfo'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List VM instances."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'network_info'
op|'='
name|'None'
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create VM instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'spawn'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'name'
op|','
name|'update_task_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create snapshot from a running VM instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'snapshot'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'name'
op|','
name|'update_task_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'reboot_type'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot VM instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'reboot'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'destroy_disks'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy VM instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|','
name|'network_info'
op|','
name|'destroy_disks'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pause VM instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'pause'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unpause paused VM instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'unpause'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Suspend the specified instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'suspend'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|resume
dedent|''
name|'def'
name|'resume'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Resume the suspended VM instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'resume'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return info about the VM instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Return data about VM diagnostics."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Return snapshot of console."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_console_output'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_volume_connector
dedent|''
name|'def'
name|'get_volume_connector'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return volume connector information."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'get_volume_connector'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volume storage to VM instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'attach_volume'
op|'('
name|'connection_info'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach volume storage to VM instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'detach_volume'
op|'('
name|'connection_info'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Get info about the host on which the VM resides."""'
newline|'\n'
name|'return'
op|'{'
string|"'address'"
op|':'
name|'CONF'
op|'.'
name|'vmwareapi_host_ip'
op|','
nl|'\n'
string|"'username'"
op|':'
name|'CONF'
op|'.'
name|'vmwareapi_host_username'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'CONF'
op|'.'
name|'vmwareapi_host_password'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_available_resource
dedent|''
name|'def'
name|'get_available_resource'
op|'('
name|'self'
op|','
name|'nodename'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|inject_network_info
dedent|''
name|'def'
name|'inject_network_info'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""inject network info for specified instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'inject_network_info'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug_vifs
dedent|''
name|'def'
name|'plug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Plug VIFs into networks."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'plug_vifs'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug_vifs
dedent|''
name|'def'
name|'unplug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unplug VIFs from networks."""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'unplug_vifs'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_interfaces
dedent|''
name|'def'
name|'list_interfaces'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the IDs of all the virtual network interfaces attached to the\n        specified instance, as a list.  These IDs are opaque to the caller\n        (they are only useful for giving back to this layer as a parameter to\n        interface_stats).  These IDs only need to be unique for a given\n        instance.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'list_interfaces'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareAPISession
dedent|''
dedent|''
name|'class'
name|'VMwareAPISession'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Sets up a session with the ESX host and handles all\n    the calls made to the host.\n    """'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'api_retry_count'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_host_ip'
op|'='
name|'host_ip'
newline|'\n'
name|'self'
op|'.'
name|'_host_username'
op|'='
name|'host_username'
newline|'\n'
name|'self'
op|'.'
name|'_host_password'
op|'='
name|'host_password'
newline|'\n'
name|'self'
op|'.'
name|'api_retry_count'
op|'='
name|'api_retry_count'
newline|'\n'
name|'self'
op|'.'
name|'_scheme'
op|'='
name|'scheme'
newline|'\n'
name|'self'
op|'.'
name|'_session_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'vim'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_create_session'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vim_object
dedent|''
name|'def'
name|'_get_vim_object'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the VIM Object instance."""'
newline|'\n'
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
newline|'\n'
nl|'\n'
DECL|member|_create_session
dedent|''
name|'def'
name|'_create_session'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a session with the ESX host."""'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'# Login and setup the session with the ESX host for making'
nl|'\n'
comment|'# API calls'
nl|'\n'
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
newline|'\n'
name|'session'
op|'='
name|'self'
op|'.'
name|'vim'
op|'.'
name|'Login'
op|'('
nl|'\n'
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
nl|'\n'
name|'userName'
op|'='
name|'self'
op|'.'
name|'_host_username'
op|','
nl|'\n'
name|'password'
op|'='
name|'self'
op|'.'
name|'_host_password'
op|')'
newline|'\n'
comment|'# Terminate the earlier session, if possible ( For the sake of'
nl|'\n'
comment|'# preserving sessions as there is a limit to the number of'
nl|'\n'
comment|'# sessions we can have )'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_session_id'
op|':'
newline|'\n'
indent|'                    '
name|'try'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'vim'
op|'.'
name|'TerminateSession'
op|'('
nl|'\n'
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
nl|'\n'
name|'sessionId'
op|'='
op|'['
name|'self'
op|'.'
name|'_session_id'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\n'
comment|'# This exception is something we can live with. It is'
nl|'\n'
comment|'# just an extra caution on our side. The session may'
nl|'\n'
comment|'# have been cleared. We could have made a call to'
nl|'\n'
comment|'# SessionIsActive, but that is an overhead because we'
nl|'\n'
comment|'# anyway would have to call TerminateSession.'
nl|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'excep'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_session_id'
op|'='
name|'session'
op|'.'
name|'key'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'critical'
op|'('
name|'_'
op|'('
string|'"In vmwareapi:_create_session, "'
nl|'\n'
string|'"got this exception: %s"'
op|')'
op|'%'
name|'excep'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'excep'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Logs-out the session."""'
newline|'\n'
comment|'# Logout to avoid un-necessary increase in session count at the'
nl|'\n'
comment|'# ESX host'
nl|'\n'
name|'try'
op|':'
newline|'\n'
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
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\n'
comment|'# It is just cautionary on our part to do a logout in del just'
nl|'\n'
comment|'# to ensure that the session is not left active.'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'excep'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Check if the module is a VIM Object instance."""'
newline|'\n'
name|'return'
name|'isinstance'
op|'('
name|'module'
op|','
name|'vim'
op|'.'
name|'Vim'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""\n        Calls a method within the module specified with\n        args provided.\n        """'
newline|'\n'
name|'args'
op|'='
name|'list'
op|'('
name|'args'
op|')'
newline|'\n'
name|'retry_count'
op|'='
number|'0'
newline|'\n'
name|'exc'
op|'='
name|'None'
newline|'\n'
name|'last_fault_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
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
newline|'\n'
comment|'# If it is not the first try, then get the latest'
nl|'\n'
comment|'# vim object'
nl|'\n'
indent|'                    '
name|'if'
name|'retry_count'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                        '
name|'args'
op|'='
name|'args'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
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
newline|'\n'
dedent|''
name|'retry_count'
op|'+='
number|'1'
newline|'\n'
name|'temp_module'
op|'='
name|'module'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'                    '
name|'temp_module'
op|'='
name|'getattr'
op|'('
name|'temp_module'
op|','
name|'method_elem'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'temp_module'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'VimFaultException'
op|','
name|'excep'
op|':'
newline|'\n'
comment|'# If it is a Session Fault Exception, it may point'
nl|'\n'
comment|'# to a session gone bad. So we try re-creating a session'
nl|'\n'
comment|'# and then proceeding ahead with the call.'
nl|'\n'
indent|'                '
name|'exc'
op|'='
name|'excep'
newline|'\n'
name|'if'
name|'error_util'
op|'.'
name|'FAULT_NOT_AUTHENTICATED'
name|'in'
name|'excep'
op|'.'
name|'fault_list'
op|':'
newline|'\n'
comment|'# Because of the idle session returning an empty'
nl|'\n'
comment|'# RetrievePropertiesResponse and also the same is returned'
nl|'\n'
comment|'# when there is say empty answer to the query for'
nl|'\n'
comment|'# VMs on the host ( as in no VMs on the host), we have no'
nl|'\n'
comment|'# way to differentiate.'
nl|'\n'
comment|'# So if the previous response was also am empty response'
nl|'\n'
comment|'# and after creating a new session, we get the same empty'
nl|'\n'
comment|'# response, then we are sure of the response being supposed'
nl|'\n'
comment|'# to be empty.'
nl|'\n'
indent|'                    '
name|'if'
name|'error_util'
op|'.'
name|'FAULT_NOT_AUTHENTICATED'
name|'in'
name|'last_fault_list'
op|':'
newline|'\n'
indent|'                        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'last_fault_list'
op|'='
name|'excep'
op|'.'
name|'fault_list'
newline|'\n'
name|'self'
op|'.'
name|'_create_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# No re-trying for errors for API call has gone through'
nl|'\n'
comment|"# and is the caller's fault. Caller should handle these"
nl|'\n'
comment|'# errors. e.g, InvalidArgument fault.'
nl|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|','
name|'excep'
op|':'
newline|'\n'
comment|'# For exceptions which may come because of session overload,'
nl|'\n'
comment|'# we retry'
nl|'\n'
indent|'                '
name|'exc'
op|'='
name|'excep'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\n'
comment|'# If it is a proper exception, say not having furnished'
nl|'\n'
comment|'# proper data in the SOAP call or the retry limit having'
nl|'\n'
comment|'# exceeded, we raise the exception'
nl|'\n'
indent|'                '
name|'exc'
op|'='
name|'excep'
newline|'\n'
name|'break'
newline|'\n'
comment|'# If retry count has been reached then break and'
nl|'\n'
comment|'# raise the exception'
nl|'\n'
dedent|''
name|'if'
name|'retry_count'
op|'>'
name|'self'
op|'.'
name|'api_retry_count'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
name|'TIME_BETWEEN_API_CALL_RETRIES'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'critical'
op|'('
name|'_'
op|'('
string|'"In vmwareapi:_call_method, "'
nl|'\n'
string|'"got this exception: %s"'
op|')'
op|'%'
name|'exc'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|_get_vim
dedent|''
name|'def'
name|'_get_vim'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets the VIM object reference."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'vim'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_create_session'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'vim'
newline|'\n'
nl|'\n'
DECL|member|_wait_for_task
dedent|''
name|'def'
name|'_wait_for_task'
op|'('
name|'self'
op|','
name|'instance_uuid'
op|','
name|'task_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a Deferred that will give the result of the given task.\n        The task is polled until it completes.\n        """'
newline|'\n'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
name|'loop'
op|'='
name|'utils'
op|'.'
name|'FixedIntervalLoopingCall'
op|'('
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'task_ref'
op|','
name|'done'
op|')'
newline|'\n'
name|'loop'
op|'.'
name|'start'
op|'('
name|'CONF'
op|'.'
name|'vmwareapi_task_poll_interval'
op|')'
newline|'\n'
name|'ret_val'
op|'='
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'loop'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'return'
name|'ret_val'
newline|'\n'
nl|'\n'
DECL|member|_poll_task
dedent|''
name|'def'
name|'_poll_task'
op|'('
name|'self'
op|','
name|'instance_uuid'
op|','
name|'task_ref'
op|','
name|'done'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Poll the given task, and fires the given Deferred if we\n        get a result.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
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
nl|'\n'
name|'task_ref'
op|','
string|'"Task"'
op|','
string|'"info"'
op|')'
newline|'\n'
name|'task_name'
op|'='
name|'task_info'
op|'.'
name|'name'
newline|'\n'
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
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'elif'
name|'task_info'
op|'.'
name|'state'
op|'=='
string|"'success'"
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Task [%(task_name)s] %(task_ref)s "'
nl|'\n'
string|'"status: success"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send'
op|'('
string|'"success"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
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
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Task [%(task_name)s] %(task_ref)s "'
nl|'\n'
string|'"status: error %(error_info)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'error_info'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\n'
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
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'excep'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
