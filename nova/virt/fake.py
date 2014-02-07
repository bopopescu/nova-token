begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nA fake (in-memory) hypervisor+api.\n\nAllows nova testing w/o a hypervisor.  This module also documents the\nsemantics of real hypervisor connections.\n\n"""'
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
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
name|'import'
name|'virtapi'
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
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
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
nl|'\n'
DECL|variable|_FAKE_NODES
name|'_FAKE_NODES'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_nodes
name|'def'
name|'set_nodes'
op|'('
name|'nodes'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sets FakeDriver\'s node.list.\n\n    It has effect on the following methods:\n        get_available_nodes()\n        get_available_resource\n        get_host_stats()\n\n    To restore the change, call restore_nodes()\n    """'
newline|'\n'
name|'global'
name|'_FAKE_NODES'
newline|'\n'
name|'_FAKE_NODES'
op|'='
name|'nodes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|restore_nodes
dedent|''
name|'def'
name|'restore_nodes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Resets FakeDriver\'s node list modified by set_nodes().\n\n    Usually called from tearDown().\n    """'
newline|'\n'
name|'global'
name|'_FAKE_NODES'
newline|'\n'
name|'_FAKE_NODES'
op|'='
op|'['
name|'CONF'
op|'.'
name|'host'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeInstance
dedent|''
name|'class'
name|'FakeInstance'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'self'
op|'.'
name|'state'
op|'='
name|'state'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeDriver
dedent|''
dedent|''
name|'class'
name|'FakeDriver'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
DECL|variable|capabilities
indent|'    '
name|'capabilities'
op|'='
op|'{'
nl|'\n'
string|'"has_imagecache"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"supports_recreate"'
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
string|'"""Fake hypervisor driver."""'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'host_status_base'
op|'='
op|'{'
nl|'\n'
string|"'vcpus'"
op|':'
number|'100000'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'8000000000'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'600000000000'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
number|'100000000000'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'utils'
op|'.'
name|'convert_version_to_int'
op|'('
string|"'1.0'"
op|')'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'disk_available_least'"
op|':'
number|'500000000000'
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
op|'['
op|'('
name|'None'
op|','
string|"'fake'"
op|','
name|'None'
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mounts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_interfaces'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'_FAKE_NODES'
op|':'
newline|'\n'
indent|'            '
name|'set_nodes'
op|'('
op|'['
name|'CONF'
op|'.'
name|'host'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
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
name|'return'
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
name|'instances'
op|'.'
name|'keys'
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
name|'pass'
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
name|'name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'state'
op|'='
name|'power_state'
op|'.'
name|'RUNNING'
newline|'\n'
name|'fake_instance'
op|'='
name|'FakeInstance'
op|'('
name|'name'
op|','
name|'state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'['
name|'name'
op|']'
op|'='
name|'fake_instance'
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
name|'if'
name|'instance'
op|'['
string|"'name'"
op|']'
name|'not'
name|'in'
name|'self'
op|'.'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotRunning'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'update_task_state'
op|'('
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_UPLOADING'
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
name|'context'
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
op|','
name|'bad_volumes_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_host_ip_addr
name|'def'
name|'get_host_ip_addr'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'192.168.0.1'"
newline|'\n'
nl|'\n'
DECL|member|set_admin_password
dedent|''
name|'def'
name|'set_admin_password'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'new_pass'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|resume_state_on_host_boot
dedent|''
name|'def'
name|'resume_state_on_host_boot'
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
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
op|','
nl|'\n'
name|'rescue_password'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
name|'flavor'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|finish_revert_migration
dedent|''
name|'def'
name|'finish_revert_migration'
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
name|'block_device_info'
op|'='
name|'None'
op|','
name|'power_on'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|post_live_migration_at_destination
dedent|''
name|'def'
name|'post_live_migration_at_destination'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|power_on
dedent|''
name|'def'
name|'power_on'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|soft_delete
dedent|''
name|'def'
name|'soft_delete'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|restore
dedent|''
name|'def'
name|'restore'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'context'
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
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
name|'key'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'.'
name|'instances'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Key \'%(key)s\' not in instances \'%(inst)s\'"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
nl|'\n'
string|"'inst'"
op|':'
name|'self'
op|'.'
name|'instances'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cleanup
dedent|''
dedent|''
name|'def'
name|'cleanup'
op|'('
name|'self'
op|','
name|'context'
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
name|'pass'
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
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|','
nl|'\n'
name|'encryption'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach the disk to the instance at mountpoint using info."""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'if'
name|'instance_name'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_mounts'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_mounts'
op|'['
name|'instance_name'
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_mounts'
op|'['
name|'instance_name'
op|']'
op|'['
name|'mountpoint'
op|']'
op|'='
name|'connection_info'
newline|'\n'
name|'return'
name|'True'
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
op|','
nl|'\n'
name|'encryption'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach the disk attached to the instance."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'.'
name|'_mounts'
op|'['
name|'instance'
op|'['
string|"'name'"
op|']'
op|']'
op|'['
name|'mountpoint'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|swap_volume
dedent|''
name|'def'
name|'swap_volume'
op|'('
name|'self'
op|','
name|'old_connection_info'
op|','
name|'new_connection_info'
op|','
nl|'\n'
name|'instance'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replace the disk attached to the instance."""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'if'
name|'instance_name'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_mounts'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_mounts'
op|'['
name|'instance_name'
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_mounts'
op|'['
name|'instance_name'
op|']'
op|'['
name|'mountpoint'
op|']'
op|'='
name|'new_connection_info'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|attach_interface
dedent|''
name|'def'
name|'attach_interface'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'image_meta'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'vif'
op|'['
string|"'id'"
op|']'
name|'in'
name|'self'
op|'.'
name|'_interfaces'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InterfaceAttachFailed'
op|'('
string|"'duplicate'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_interfaces'
op|'['
name|'vif'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'vif'
newline|'\n'
nl|'\n'
DECL|member|detach_interface
dedent|''
name|'def'
name|'detach_interface'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'.'
name|'_interfaces'
op|'['
name|'vif'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InterfaceDetachFailed'
op|'('
string|"'not attached'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
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
name|'if'
name|'instance'
op|'['
string|"'name'"
op|']'
name|'not'
name|'in'
name|'self'
op|'.'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'i'
op|'='
name|'self'
op|'.'
name|'instances'
op|'['
name|'instance'
op|'['
string|"'name'"
op|']'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'i'
op|'.'
name|'state'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'cpu0_time'"
op|':'
number|'17300000000'
op|','
nl|'\n'
string|"'memory'"
op|':'
number|'524288'
op|','
nl|'\n'
string|"'vda_errors'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|"'vda_read'"
op|':'
number|'262144'
op|','
nl|'\n'
string|"'vda_read_req'"
op|':'
number|'112'
op|','
nl|'\n'
string|"'vda_write'"
op|':'
number|'5778432'
op|','
nl|'\n'
string|"'vda_write_req'"
op|':'
number|'488'
op|','
nl|'\n'
string|"'vnet1_rx'"
op|':'
number|'2070139'
op|','
nl|'\n'
string|"'vnet1_rx_drop'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'vnet1_rx_errors'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'vnet1_rx_packets'"
op|':'
number|'26701'
op|','
nl|'\n'
string|"'vnet1_tx'"
op|':'
number|'140208'
op|','
nl|'\n'
string|"'vnet1_tx_drop'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'vnet1_tx_errors'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'vnet1_tx_packets'"
op|':'
number|'662'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_all_bw_counters
dedent|''
name|'def'
name|'get_all_bw_counters'
op|'('
name|'self'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return bandwidth usage counters for each interface on each\n           running VM.\n        """'
newline|'\n'
name|'bw'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'bw'
newline|'\n'
nl|'\n'
DECL|member|get_all_volume_usage
dedent|''
name|'def'
name|'get_all_volume_usage'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'compute_host_bdms'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return usage info for volumes attached to vms on\n           a given host.\n        """'
newline|'\n'
name|'volusage'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'volusage'
newline|'\n'
nl|'\n'
DECL|member|get_host_cpu_stats
dedent|''
name|'def'
name|'get_host_cpu_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stats'
op|'='
op|'{'
string|"'kernel'"
op|':'
number|'5664160000000L'
op|','
nl|'\n'
string|"'idle'"
op|':'
number|'1592705190000000L'
op|','
nl|'\n'
string|"'user'"
op|':'
number|'26728850000000L'
op|','
nl|'\n'
string|"'iowait'"
op|':'
number|'6121490000000L'
op|'}'
newline|'\n'
name|'stats'
op|'['
string|"'frequency'"
op|']'
op|'='
number|'800'
newline|'\n'
name|'return'
name|'stats'
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
name|'return'
op|'['
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
name|'None'
op|']'
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
name|'return'
op|'['
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'FAKE CONSOLE OUTPUT\\nANOTHER\\nLAST LINE'"
newline|'\n'
nl|'\n'
DECL|member|get_vnc_console
dedent|''
name|'def'
name|'get_vnc_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'internal_access_path'"
op|':'
string|"'FAKE'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fakevncconsole.com'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'6969'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_spice_console
dedent|''
name|'def'
name|'get_spice_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'internal_access_path'"
op|':'
string|"'FAKE'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fakespiceconsole.com'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'6969'
op|','
nl|'\n'
string|"'tlsPort'"
op|':'
number|'6970'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_rdp_console
dedent|''
name|'def'
name|'get_rdp_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'internal_access_path'"
op|':'
string|"'FAKE'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fakerdpconsole.com'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'6969'
op|'}'
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
name|'return'
op|'{'
string|"'address'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'username'"
op|':'
string|"'fakeuser'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'fakepassword'"
op|'}'
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
name|'return'
name|'True'
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
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|refresh_instance_security_rules
dedent|''
name|'def'
name|'refresh_instance_security_rules'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|refresh_provider_fw_rules
dedent|''
name|'def'
name|'refresh_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
string|'"""Updates compute manager resource info on ComputeNode table.\n\n           Since we don\'t have a real hypervisor, pretend we have lots of\n           disk and ram.\n        """'
newline|'\n'
name|'if'
name|'nodename'
name|'not'
name|'in'
name|'_FAKE_NODES'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'dic'
op|'='
op|'{'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'8192'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'1028'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
string|"'1.0'"
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'nodename'
op|','
nl|'\n'
string|"'disk_available_least'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
string|"'?'"
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'['
op|'('
name|'None'
op|','
string|"'fake'"
op|','
name|'None'
op|')'
op|']'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'dic'
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
name|'return'
newline|'\n'
nl|'\n'
DECL|member|get_instance_disk_info
dedent|''
name|'def'
name|'get_instance_disk_info'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
DECL|member|live_migration
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
nl|'\n'
name|'post_method'
op|','
name|'recover_method'
op|','
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'migrate_data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'post_method'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
name|'block_migration'
op|','
nl|'\n'
name|'migrate_data'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_destination_cleanup
dedent|''
name|'def'
name|'check_can_live_migrate_destination_cleanup'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_destination
dedent|''
name|'def'
name|'check_can_live_migrate_destination'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'src_compute_info'
op|','
name|'dst_compute_info'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_source
dedent|''
name|'def'
name|'check_can_live_migrate_source'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
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
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
name|'power_on'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
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
name|'return'
newline|'\n'
nl|'\n'
DECL|member|pre_live_migration
dedent|''
name|'def'
name|'pre_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'network_info'
op|','
name|'disk'
op|','
name|'migrate_data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
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
name|'return'
newline|'\n'
nl|'\n'
DECL|member|test_remove_vm
dedent|''
name|'def'
name|'test_remove_vm'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes the named VM, as if it crashed. For testing."""'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'pop'
op|'('
name|'instance_name'
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
string|'"""Return fake Host Status of ram, disk, network."""'
newline|'\n'
name|'stats'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'nodename'
name|'in'
name|'_FAKE_NODES'
op|':'
newline|'\n'
indent|'            '
name|'host_status'
op|'='
name|'self'
op|'.'
name|'host_status_base'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'host_status'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
name|'nodename'
newline|'\n'
name|'host_status'
op|'['
string|"'host_hostname'"
op|']'
op|'='
name|'nodename'
newline|'\n'
name|'host_status'
op|'['
string|"'host_name_label'"
op|']'
op|'='
name|'nodename'
newline|'\n'
name|'stats'
op|'.'
name|'append'
op|'('
name|'host_status'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'stats'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
string|'"FakeDriver has no node"'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'stats'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'stats'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'stats'
newline|'\n'
nl|'\n'
DECL|member|host_power_action
dedent|''
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
name|'return'
name|'action'
newline|'\n'
nl|'\n'
DECL|member|host_maintenance_mode
dedent|''
name|'def'
name|'host_maintenance_mode'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start/Stop host maintenance window. On start, it triggers\n        guest VMs evacuation.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'mode'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'off_maintenance'"
newline|'\n'
dedent|''
name|'return'
string|"'on_maintenance'"
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
name|'if'
name|'enabled'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'enabled'"
newline|'\n'
dedent|''
name|'return'
string|"'disabled'"
newline|'\n'
nl|'\n'
DECL|member|get_disk_available_least
dedent|''
name|'def'
name|'get_disk_available_least'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
name|'return'
op|'{'
string|"'ip'"
op|':'
string|"'127.0.0.1'"
op|','
string|"'initiator'"
op|':'
string|"'fake'"
op|','
string|"'host'"
op|':'
string|"'fakehost'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_available_nodes
dedent|''
name|'def'
name|'get_available_nodes'
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
name|'return'
name|'_FAKE_NODES'
newline|'\n'
nl|'\n'
DECL|member|instance_on_disk
dedent|''
name|'def'
name|'instance_on_disk'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|list_instance_uuids
dedent|''
name|'def'
name|'list_instance_uuids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeVirtAPI
dedent|''
dedent|''
name|'class'
name|'FakeVirtAPI'
op|'('
name|'virtapi'
op|'.'
name|'VirtAPI'
op|')'
op|':'
newline|'\n'
DECL|member|instance_update
indent|'    '
name|'def'
name|'instance_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|provider_fw_rule_get_all
dedent|''
name|'def'
name|'provider_fw_rule_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'provider_fw_rule_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|agent_build_get_by_triple
dedent|''
name|'def'
name|'agent_build_get_by_triple'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'hypervisor'
op|','
name|'os'
op|','
name|'architecture'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'agent_build_get_by_triple'
op|'('
name|'context'
op|','
nl|'\n'
name|'hypervisor'
op|','
name|'os'
op|','
name|'architecture'
op|')'
newline|'\n'
nl|'\n'
DECL|member|flavor_get
dedent|''
name|'def'
name|'flavor_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'flavor_get'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_get_all_by_instance
dedent|''
name|'def'
name|'block_device_mapping_get_all_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'legacy'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdms'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'bdms'
op|'='
name|'block_device'
op|'.'
name|'legacy_mapping'
op|'('
name|'bdms'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'bdms'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
