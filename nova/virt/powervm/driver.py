begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM'
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
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
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
nl|'\n'
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
name|'powervm'
name|'import'
name|'operator'
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
DECL|variable|powervm_opts
name|'powervm_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'ivm'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PowerVM manager type (ivm, hmc)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr'"
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
string|"'PowerVM manager host or ip'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr_user'"
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
string|"'PowerVM manager user name'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr_passwd'"
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
string|"'PowerVM manager user password'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_img_remote_path'"
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
string|"'PowerVM image remote path'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_img_local_path'"
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
string|"'Local directory to download glance images to'"
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
name|'powervm_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMDriver
name|'class'
name|'PowerVMDriver'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""PowerVM Implementation of Compute Driver."""'
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
name|'super'
op|'('
name|'PowerVMDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'='
name|'operator'
op|'.'
name|'PowerVMOperator'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|host_state
name|'def'
name|'host_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
string|'"""Initialize anything that is necessary for the driver to function,\n        including catching up with currently running VM\'s on the given host."""'
newline|'\n'
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'powervm_instances'
op|'='
name|'self'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
comment|"# Looks for db instances that don't exist on the host side"
nl|'\n'
comment|'# and cleanup the inconsistencies.'
nl|'\n'
name|'for'
name|'db_instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'task_state'
op|'='
name|'db_instance'
op|'['
string|"'task_state'"
op|']'
newline|'\n'
name|'if'
name|'db_instance'
op|'['
string|"'name'"
op|']'
name|'in'
name|'powervm_instances'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'task_state'
name|'in'
op|'['
name|'task_states'
op|'.'
name|'DELETING'
op|','
name|'task_states'
op|'.'
name|'SPAWNING'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'db_instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'DELETED'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'db_instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
dedent|''
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
string|'"""Get the current status of an instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_num_instances
dedent|''
name|'def'
name|'get_num_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'list_instances'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_exists
dedent|''
name|'def'
name|'instance_exists'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'instance_exists'
op|'('
name|'instance_name'
op|')'
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
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_stats
dedent|''
name|'def'
name|'get_host_stats'
op|'('
name|'self'
op|','
name|'refresh'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return currently known host stats"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'get_host_stats'
op|'('
name|'refresh'
op|'='
name|'refresh'
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
name|'pass'
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
nl|'\n'
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
string|'"""\n        Create a new instance/VM/domain on powerVM.\n\n        :param context: security context\n        :param instance: Instance object as returned by DB layer.\n                         This function should use the data there to guide\n                         the creation of the new instance.\n        :param image_meta: image object returned by nova.image.glance that\n                           defines the image from which to boot this instance\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param block_device_info: Information about block devices to be\n                                  attached to the instance.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'spawn'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|'['
string|"'id'"
op|']'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy (shutdown and delete) the specified instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
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
string|'"""Reboot the specified instance.\n\n        :param instance: Instance object as returned by DB layer.\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param reboot_type: Either a HARD or SOFT reboot\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_host_ip_addr
dedent|''
name|'def'
name|'get_host_ip_addr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Retrieves the IP address of the dom0\n        """'
newline|'\n'
name|'pass'
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
string|'"""Pause the specified instance."""'
newline|'\n'
name|'pass'
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
string|'"""Unpause paused VM instance"""'
newline|'\n'
name|'pass'
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
string|'"""suspend the specified instance"""'
newline|'\n'
name|'pass'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""resume the specified instance"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|power_off
dedent|''
name|'def'
name|'power_off'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Power off the specified instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_on
dedent|''
name|'def'
name|'power_on'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Power on the specified instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'power_on'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_available_resource
dedent|''
name|'def'
name|'get_available_resource'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve resource info."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'get_available_resource'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_power_action
dedent|''
name|'def'
name|'host_power_action'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboots, shuts down or powers up the host."""'
newline|'\n'
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
string|'"""\n        Indicate if the driver requires the legacy network_info format.\n        """'
newline|'\n'
comment|'# TODO(tr3buchet): update all subclasses and remove this'
nl|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|manage_image_cache
dedent|''
name|'def'
name|'manage_image_cache'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Manage the driver\'s local image cache.\n\n        Some drivers chose to cache images for instances on disk. This method\n        is an opportunity to do management of that cache which isn\'t directly\n        related to other calls into the driver. The prime example is to clean\n        the cache and remove images which are no longer of interest.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
