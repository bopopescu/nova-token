begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
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
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'_'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# The read_only parameter is ignored.'
nl|'\n'
indent|'    '
name|'return'
name|'FakeConnection'
op|'.'
name|'instance'
op|'('
op|')'
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
nl|'\n'
DECL|class|FakeConnection
dedent|''
dedent|''
name|'class'
name|'FakeConnection'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fake hypervisor driver"""'
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
name|'self'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'host_status'
op|'='
op|'{'
nl|'\n'
string|"'host_name-description'"
op|':'
string|"'Fake Host'"
op|','
nl|'\n'
string|"'host_hostname'"
op|':'
string|"'fake-mini'"
op|','
nl|'\n'
string|"'host_memory_total'"
op|':'
number|'8000000000'
op|','
nl|'\n'
string|"'host_memory_overhead'"
op|':'
number|'10000000'
op|','
nl|'\n'
string|"'host_memory_free'"
op|':'
number|'7900000000'
op|','
nl|'\n'
string|"'host_memory_free_computed'"
op|':'
number|'7900000000'
op|','
nl|'\n'
string|"'host_other_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'host_ip_address'"
op|':'
string|"'192.168.1.109'"
op|','
nl|'\n'
string|"'host_cpu_info'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'disk_available'"
op|':'
number|'500000000000'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'600000000000'
op|','
nl|'\n'
string|"'disk_used'"
op|':'
number|'100000000000'
op|','
nl|'\n'
string|"'host_uuid'"
op|':'
string|"'cedb9b39-9388-41df-8891-c5c9a0c0fe5f'"
op|','
nl|'\n'
string|"'host_name_label'"
op|':'
string|"'fake-mini'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_mounts'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'cls'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
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
DECL|member|_map_to_instance_info
dedent|''
name|'def'
name|'_map_to_instance_info'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'utils'
op|'.'
name|'check_isinstance'
op|'('
name|'instance'
op|','
name|'FakeInstance'
op|')'
newline|'\n'
name|'info'
op|'='
name|'driver'
op|'.'
name|'InstanceInfo'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
name|'instance'
op|'.'
name|'state'
op|')'
newline|'\n'
name|'return'
name|'info'
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
name|'info_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'info_list'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_map_to_instance_info'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'info_list'
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
name|'name'
op|'='
name|'instance'
op|'.'
name|'name'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'instance'
op|'['
string|"'name'"
op|']'
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
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
name|'pass'
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
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'instance_type'
op|','
name|'network_info'
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
name|'instance'
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
string|'"Key \'%s\' not in instances \'%s\'"'
op|'%'
nl|'\n'
op|'('
name|'key'
op|','
name|'self'
op|'.'
name|'instances'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
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
name|'if'
name|'not'
name|'instance_name'
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
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach the disk attached to the instance"""'
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
name|'instance_name'
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
string|"'FAKE_DIAGNOSTICS'"
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
name|'bwusage'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'bwusage'
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
name|'return'
op|'['
string|"'A_DISK'"
op|']'
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
name|'return'
op|'['
string|"'A_VIF'"
op|']'
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
string|'"""Updates compute manager resource info on ComputeNode table.\n\n           Since we don\'t have a real hypervisor, pretend we have lots of\n           disk and ram.\n        """'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'ctxt'
op|','
name|'host'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
nl|'\n'
comment|'# Updating host information'
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
number|'4096'
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
string|"'service_id'"
op|':'
name|'service_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
string|"'?'"
op|'}'
newline|'\n'
nl|'\n'
name|'compute_node_ref'
op|'='
name|'service_ref'
op|'['
string|"'compute_node'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'compute_node_ref'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Compute_service record created for %s '"
op|')'
op|'%'
name|'host'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_create'
op|'('
name|'ctxt'
op|','
name|'dic'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Compute_service record updated for %s '"
op|')'
op|'%'
name|'host'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_update'
op|'('
name|'ctxt'
op|','
name|'compute_node_ref'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|','
name|'dic'
op|')'
newline|'\n'
nl|'\n'
DECL|member|compare_cpu
dedent|''
dedent|''
name|'def'
name|'compare_cpu'
op|'('
name|'self'
op|','
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only by libvirt.'"
op|')'
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
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only by libvirt.'"
op|')'
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
string|'"""This method is supported only by libvirt."""'
newline|'\n'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
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
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
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
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only by libvirt.'"
op|')'
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
string|'""" Removes the named VM, as if it crashed. For testing"""'
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
string|'"""Return fake Host Status of ram, disk, network."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'host_status'
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
name|'return'
name|'self'
op|'.'
name|'host_status'
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
name|'pass'
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
string|'""" """'
newline|'\n'
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
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
