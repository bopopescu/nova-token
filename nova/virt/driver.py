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
DECL|class|ComputeDriver
dedent|''
dedent|''
name|'class'
name|'ComputeDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for compute drivers.\n\n    Lots of documentation is currently on fake.py.\n    """'
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
string|'"""Adopt existing VM\'s running here"""'
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
string|'"""Get the current status of an instance, by name (not ID!)\n\n        Returns a dict containing:\n        :state:           the running state, one of the power_state codes\n        :max_mem:         (int) the maximum memory in KBytes allowed\n        :mem:             (int) the memory in KBytes used by the domain\n        :num_cpu:         (int) the number of virtual CPUs for the domain\n        :cpu_time:        (int) the CPU time used in nanoseconds\n        """'
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
indent|'        '
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
name|'network_info'
op|','
nl|'\n'
name|'block_device_mapping'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Launch a VM for the specified instance"""'
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
name|'cleanup'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy (shutdown and delete) the specified instance.\n\n        The given parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name.\n\n        The work will be done asynchronously.  This function returns a\n        task that allows the caller to detect when it is complete.\n\n        If the instance is not found (for example if networking failed), this\n        function should still succeed.  It\'s probably a good idea to log a\n        warning in that case.\n\n        """'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot specified VM"""'
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
DECL|member|get_host_ip_addr
dedent|''
name|'def'
name|'get_host_ip_addr'
op|'('
name|'self'
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
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'volume_id'
op|','
name|'mountpoint'
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
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'volume_id'
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
DECL|member|compare_cpu
dedent|''
name|'def'
name|'compare_cpu'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cpu_info'
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
DECL|member|migrate_disk_and_power_off
dedent|''
name|'def'
name|'migrate_disk_and_power_off'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Transfers the VHD of a running instance to another host, then shuts\n        off the instance copies over the COW disk"""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
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
string|'"""Create snapshot from a running VM instance."""'
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
name|'instance'
op|','
name|'disk_info'
op|','
name|'network_info'
op|','
nl|'\n'
name|'resize_instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Completes a resize, turning on the migrated instance"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|revert_migration
dedent|''
name|'def'
name|'revert_migration'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reverts a resize, powering back on the instance"""'
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
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pause VM instance"""'
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
op|','
name|'callback'
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
op|','
name|'callback'
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
op|','
name|'callback'
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
name|'callback'
op|','
name|'network_info'
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
name|'callback'
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
string|'"""Spawning live_migration operation for distributing high-load.\n\n        :params ctxt: security context\n        :params instance_ref:\n            nova.db.sqlalchemy.models.Instance object\n            instance object that is migrated.\n        :params dest: destination host\n        :params post_method:\n            post operation method.\n            expected nova.compute.manager.post_live_migration.\n        :params recover_method:\n            recovery method when any exception occurs.\n            expected nova.compute.manager.recover_live_migration.\n\n        """'
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
indent|'        '
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
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
indent|'        '
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
string|'"""See: nova/virt/fake.py for docs."""'
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
string|'"""Set the root/admin password for an instance on this server."""'
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
string|'"""Create a file on the VM instance. The file path and contents\n        should be base64-encoded.\n        """'
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
string|'"""Update agent on the VM instance."""'
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
DECL|member|set_host_powerstate
dedent|''
name|'def'
name|'set_host_powerstate'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboots or shuts down the host."""'
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
DECL|member|set_power_state
dedent|''
name|'def'
name|'set_power_state'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'power_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboots, shuts down or starts up the host."""'
newline|'\n'
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
string|'"""Plugs in VIFs to networks."""'
newline|'\n'
comment|'# TODO(Vek): Need to pass context in for access to auth_token'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
