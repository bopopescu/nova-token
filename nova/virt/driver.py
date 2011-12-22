begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nDriver base-classes:\n\n    (Beginning of) the contract that compute drivers must follow, and shared\n    types that support that contract\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceInfo
name|'class'
name|'InstanceInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'assert'
name|'state'
name|'in'
name|'power_state'
op|'.'
name|'valid_states'
op|'('
op|')'
op|','
string|'"Bad state: %s"'
op|'%'
name|'state'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'state'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|block_device_info_get_root
dedent|''
dedent|''
name|'def'
name|'block_device_info_get_root'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'block_device_info'
op|'='
name|'block_device_info'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'return'
name|'block_device_info'
op|'.'
name|'get'
op|'('
string|"'root_device_name'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|block_device_info_get_swap
dedent|''
name|'def'
name|'block_device_info_get_swap'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'block_device_info'
op|'='
name|'block_device_info'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'return'
name|'block_device_info'
op|'.'
name|'get'
op|'('
string|"'swap'"
op|')'
name|'or'
op|'{'
string|"'device_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|swap_is_usable
dedent|''
name|'def'
name|'swap_is_usable'
op|'('
name|'swap'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'swap'
name|'and'
name|'swap'
op|'['
string|"'device_name'"
op|']'
name|'and'
name|'swap'
op|'['
string|"'swap_size'"
op|']'
op|'>'
number|'0'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|block_device_info_get_ephemerals
dedent|''
name|'def'
name|'block_device_info_get_ephemerals'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'block_device_info'
op|'='
name|'block_device_info'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'ephemerals'
op|'='
name|'block_device_info'
op|'.'
name|'get'
op|'('
string|"'ephemerals'"
op|')'
name|'or'
op|'['
op|']'
newline|'\n'
name|'return'
name|'ephemerals'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|block_device_info_get_mapping
dedent|''
name|'def'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'block_device_info'
op|'='
name|'block_device_info'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'block_device_mapping'
op|'='
name|'block_device_info'
op|'.'
name|'get'
op|'('
string|"'block_device_mapping'"
op|')'
name|'or'
op|'['
op|']'
newline|'\n'
name|'return'
name|'block_device_mapping'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeDriver
dedent|''
name|'class'
name|'ComputeDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for compute drivers.\n\n    The interface to this class talks in terms of \'instances\' (Amazon EC2 and\n    internal Nova terminology), by which we mean \'running virtual machine\'\n    (XenAPI terminology) or domain (Xen or libvirt terminology).\n\n    An instance has an ID, which is the identifier chosen by Nova to represent\n    the instance further up the stack.  This is unfortunately also called a\n    \'name\' elsewhere.  As far as this layer is concerned, \'instance ID\' and\n    \'instance name\' are synonyms.\n\n    Note that the instance ID or name is not human-readable or\n    customer-controlled -- it\'s an internal ID chosen by Nova.  At the\n    nova.virt layer, instances do not have human-readable names at all -- such\n    things are only known higher up the stack.\n\n    Most virtualization platforms will also have their own identity schemes,\n    to uniquely identify a VM or domain.  These IDs must stay internal to the\n    platform-specific layer, and never escape the connection interface.  The\n    platform-specific layer is responsible for keeping track of which instance\n    ID maps to which platform-specific ID, and vice versa.\n\n    In contrast, the list_disks and list_interfaces calls may return\n    platform-specific IDs.  These identify a specific virtual disk or specific\n    virtual network interface, and these IDs are opaque to the rest of Nova.\n\n    Some methods here take an instance of nova.compute.service.Instance.  This\n    is the data structure used by nova.compute to store details regarding an\n    instance, and pass them into this layer.  This layer is responsible for\n    translating that generic data structure into terms that are specific to the\n    virtualization platform.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|init_host
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the current status of an instance, by name (not ID!)\n\n        Returns a dict containing:\n\n        :state:           the running state, one of the power_state codes\n        :max_mem:         (int) the maximum memory in KBytes allowed\n        :mem:             (int) the memory in KBytes used by the domain\n        :num_cpu:         (int) the number of virtual CPUs for the domain\n        :cpu_time:        (int) the CPU time used in nanoseconds\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""\n        Return the names of all the instances known to the virtualization\n        layer, as a list.\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_instances_detail
dedent|''
name|'def'
name|'list_instances_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of InstanceInfo for all registered VMs"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
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
string|'"""\n        Create a new instance/VM/domain on the virtualization platform.\n\n        Once this successfully completes, the instance should be\n        running (power_state.RUNNING).\n\n        If this fails, any partial instance should be completely\n        cleaned up, and the virtualization platform should be in the state\n        that it was before this call began.\n\n        :param context: security context\n        :param instance: Instance object as returned by DB layer.\n                         This function should use the data there to guide\n                         the creation of the new instance.\n        :param image_meta: image object returned by nova.image.glance that\n                           defines the image from which to boot this instance\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param block_device_info: Information about block devices to be\n                                  attached to the instance.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Destroy (shutdown and delete) the specified instance.\n\n        If the instance is not found (for example if networking failed), this\n        function should still succeed.  It\'s probably a good idea to log a\n        warning in that case.\n\n        :param instance: Instance object as returned by DB layer.\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param block_device_info: Information about block devices that should\n                                  be detached from the instance.\n\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot the specified instance.\n\n        :param instance: Instance object as returned by DB layer.\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param reboot_type: Either a HARD or SOFT reboot\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|snapshot_instance
dedent|''
name|'def'
name|'snapshot_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vnc_console
dedent|''
name|'def'
name|'get_vnc_console'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Return data about VM diagnostics"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_bw_usage
dedent|''
name|'def'
name|'get_all_bw_usage'
op|'('
name|'self'
op|','
name|'start_time'
op|','
name|'stop_time'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return bandwidth usage info for each interface on each\n           running VM"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach the disk to the instance at mountpoint using info"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach the disk attached to the instance"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|compare_cpu
dedent|''
name|'def'
name|'compare_cpu'
op|'('
name|'self'
op|','
name|'cpu_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Compares given cpu info against host\n\n        Before attempting to migrate a VM to this host,\n        compare_cpu is called to ensure that the VM will\n        actually run here.\n\n        :param cpu_info: (str) JSON structure describing the source CPU.\n        :returns: None if migration is acceptable\n        :raises: :py:class:`~nova.exception.InvalidCPUInfo` if migration\n                 is not acceptable.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_disk_and_power_off
dedent|''
name|'def'
name|'migrate_disk_and_power_off'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Transfers the disk of a running instance in multiple phases, turning\n        off the instance before the end.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Snapshots the specified instance.\n\n        :param context: security context\n        :param instance: Instance object as returned by DB layer.\n        :param image_id: Reference to a pre-created image that will\n                         hold the snapshot.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_migration
dedent|''
name|'def'
name|'finish_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration'
op|','
name|'instance'
op|','
name|'disk_info'
op|','
nl|'\n'
name|'network_info'
op|','
name|'image_meta'
op|','
name|'resize_instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Completes a resize, turning on the migrated instance\n\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param image_meta: image object returned by nova.image.glance that\n                           defines the image from which this instance\n                           was created\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|confirm_migration
dedent|''
name|'def'
name|'confirm_migration'
op|'('
name|'self'
op|','
name|'migration'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Confirms a resize, destroying the source VM"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_revert_migration
dedent|''
name|'def'
name|'finish_revert_migration'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Finish reverting a resize, powering back on the instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Pause the specified instance."""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Unpause paused VM instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""suspend the specified instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""resume the specified instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|rescue
dedent|''
name|'def'
name|'rescue'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rescue the specified instance"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unrescue
dedent|''
name|'def'
name|'unrescue'
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
string|'"""Unrescue the specified instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
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
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_available_resource
dedent|''
name|'def'
name|'update_available_resource'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates compute manager resource info on ComputeNode table.\n\n        This method is called when nova-compute launches, and\n        whenever admin executes "nova-manage service update_resource".\n\n        :param ctxt: security context\n        :param host: hostname that compute manager is currently running\n\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migration
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
nl|'\n'
name|'post_method'
op|','
name|'recover_method'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Spawning live_migration operation for distributing high-load.\n\n        :param ctxt: security context\n        :param instance_ref:\n            nova.db.sqlalchemy.models.Instance object\n            instance object that is migrated.\n        :param dest: destination host\n        :param post_method:\n            post operation method.\n            expected nova.compute.manager.post_live_migration.\n        :param recover_method:\n            recovery method when any exception occurs.\n            expected nova.compute.manager.recover_live_migration.\n\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_rules
dedent|''
name|'def'
name|'refresh_security_group_rules'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called after a change to security groups.\n\n        All security groups and their associated rules live in the datastore,\n        and calling this method should apply the updated rules to instances\n        running the specified security group.\n\n        An error should be raised if the operation cannot complete.\n\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_members
dedent|''
name|'def'
name|'refresh_security_group_members'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called when a security group is added to an instance.\n\n        This message is sent to the virtualization drivers on hosts that are\n        running an instance that belongs to a security group that has a rule\n        that references the security group identified by `security_group_id`.\n        It is the responsibility of this method to make sure any rules\n        that authorize traffic flow with members of the security group are\n        updated and any new members can communicate, and any removed members\n        cannot.\n\n        Scenario:\n            * we are running on host \'H0\' and we have an instance \'i-0\'.\n            * instance \'i-0\' is a member of security group \'speaks-b\'\n            * group \'speaks-b\' has an ingress rule that authorizes group \'b\'\n            * another host \'H1\' runs an instance \'i-1\'\n            * instance \'i-1\' is a member of security group \'b\'\n\n            When \'i-1\' launches or terminates we will recieve the message\n            to update members of group \'b\', at which time we will make\n            any changes needed to the rules for instance \'i-0\' to allow\n            or deny traffic coming from \'i-1\', depending on if it is being\n            added or removed from the group.\n\n        In this scenario, \'i-1\' could just as easily have been running on our\n        host \'H0\' and this method would still have been called.  The point was\n        that this method isn\'t called on the host where instances of that\n        group are running (as is the case with\n        :method:`refresh_security_group_rules`) but is called where references\n        are made to authorizing those instances.\n\n        An error should be raised if the operation cannot complete.\n\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_provider_fw_rules
dedent|''
name|'def'
name|'refresh_provider_fw_rules'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This triggers a firewall update based on database changes.\n\n        When this is called, rules have either been added or removed from the\n        datastore.  You can retrieve rules with\n        :method:`nova.db.provider_fw_rule_get_all`.\n\n        Provider rules take precedence over security group rules.  If an IP\n        would be allowed by a security group ingress rule, but blocked by\n        a provider rule, then packets from the IP are dropped.  This includes\n        intra-project traffic in the case of the allow_project_net_traffic\n        flag for the libvirt-derived classes.\n\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset_network
dedent|''
name|'def'
name|'reset_network'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""reset networking for specified instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|ensure_filtering_rules_for_instance
dedent|''
name|'def'
name|'ensure_filtering_rules_for_instance'
op|'('
name|'self'
op|','
name|'instance_ref'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setting up filtering rules and waiting for its completion.\n\n        To migrate an instance, filtering rules to hypervisors\n        and firewalls are inevitable on destination host.\n        ( Waiting only for filtering rules to hypervisor,\n        since filtering rules to firewall rules can be set faster).\n\n        Concretely, the below method must be called.\n        - setup_basic_filtering (for nova-basic, etc.)\n        - prepare_instance_filter(for nova-instance-instance-xxx, etc.)\n\n        to_xml may have to be called since it defines PROJNET, PROJMASK.\n        but libvirt migrates those value through migrateToURI(),\n        so , no need to be called.\n\n        Don\'t use thread for this method since migration should\n        not be started when setting-up filtering rules operations\n        are not completed.\n\n        :params instance_ref: nova.db.sqlalchemy.models.Instance object\n\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
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
string|'"""Stop filtering instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_admin_password
dedent|''
name|'def'
name|'set_admin_password'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'new_pass'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Set the root password on the specified instance.\n\n        The first parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name. The second\n        parameter is the value of the new password.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|inject_file
dedent|''
name|'def'
name|'inject_file'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'b64_path'
op|','
name|'b64_contents'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Writes a file on the specified instance.\n\n        The first parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name. The second\n        parameter is the base64-encoded path to which the file is to be\n        written on the instance; the third is the contents of the file, also\n        base64-encoded.\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|agent_update
dedent|''
name|'def'
name|'agent_update'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'url'
op|','
name|'md5hash'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Update agent on the specified instance.\n\n        The first parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name. The second\n        parameter is the URL of the agent to be fetched and updated on the\n        instance; the third is the md5 hash of the file for verification\n        purposes.\n        """'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
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
name|'nw_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""inject network info for specified instance"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|poll_rebooting_instances
dedent|''
name|'def'
name|'poll_rebooting_instances'
op|'('
name|'self'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll for rebooting instances"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|poll_rescued_instances
dedent|''
name|'def'
name|'poll_rescued_instances'
op|'('
name|'self'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll for rescued instances"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|poll_unconfirmed_resizes
dedent|''
name|'def'
name|'poll_unconfirmed_resizes'
op|'('
name|'self'
op|','
name|'resize_confirm_window'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll for unconfirmed resizes"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
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
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_host_enabled
dedent|''
name|'def'
name|'set_host_enabled'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'enabled'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the specified host\'s ability to accept new instances."""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_host_status
dedent|''
name|'def'
name|'update_host_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Refresh host stats"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
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
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_disks
dedent|''
name|'def'
name|'list_disks'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the IDs of all the virtual disks attached to the specified\n        instance, as a list.  These IDs are opaque to the caller (they are\n        only useful for giving back to this layer as a parameter to\n        disk_stats).  These IDs only need to be unique for a given instance.\n\n        Note that this function takes an instance ID.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""\n        Return the IDs of all the virtual network interfaces attached to the\n        specified instance, as a list.  These IDs are opaque to the caller\n        (they are only useful for giving back to this layer as a parameter to\n        interface_stats).  These IDs only need to be unique for a given\n        instance.\n\n        Note that this function takes an instance ID.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|resize
dedent|''
name|'def'
name|'resize'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Resizes/Migrates the specified instance.\n\n        The flavor parameter determines whether or not the instance RAM and\n        disk space are modified, and if so, to what size.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_stats
dedent|''
name|'def'
name|'block_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'disk_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return performance counters associated with the given disk_id on the\n        given instance_name.  These are returned as [rd_req, rd_bytes, wr_req,\n        wr_bytes, errs], where rd indicates read, wr indicates write, req is\n        the total number of I/O requests made, bytes is the total number of\n        bytes transferred, and errs is the number of requests held up due to a\n        full pipeline.\n\n        All counters are long integers.\n\n        This method is optional.  On some platforms (e.g. XenAPI) performance\n        statistics can be retrieved directly in aggregate form, without Nova\n        having to do the aggregation.  On those platforms, this method is\n        unused.\n\n        Note that this function takes an instance ID.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|interface_stats
dedent|''
name|'def'
name|'interface_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return performance counters associated with the given iface_id on the\n        given instance_id.  These are returned as [rx_bytes, rx_packets,\n        rx_errs, rx_drop, tx_bytes, tx_packets, tx_errs, tx_drop], where rx\n        indicates receive, tx indicates transmit, bytes and packets indicate\n        the total number of bytes or packets transferred, and errs and dropped\n        is the total number of packets failed / dropped.\n\n        All counters are long integers.\n\n        This method is optional.  On some platforms (e.g. XenAPI) performance\n        statistics can be retrieved directly in aggregate form, without Nova\n        having to do the aggregation.  On those platforms, this method is\n        unused.\n\n        Note that this function takes an instance ID.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
