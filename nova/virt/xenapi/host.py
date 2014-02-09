begin_unit
comment|'# Copyright (c) 2012 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""\nManagement class for host-related functions (start, reboot, etc).\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
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
name|'from'
name|'nova'
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'aggregate'
name|'as'
name|'aggregate_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
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
op|'.'
name|'pci'
name|'import'
name|'pci_whitelist'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'pool_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
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
DECL|class|Host
name|'class'
name|'Host'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements host related operations."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'_virtapi'
op|'='
name|'virtapi'
newline|'\n'
name|'self'
op|'.'
name|'_conductor_api'
op|'='
name|'conductor'
op|'.'
name|'API'
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
name|'_host'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboots or shuts down the host."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|'"action"'
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'action'
op|')'
op|'}'
newline|'\n'
name|'methods'
op|'='
op|'{'
string|'"reboot"'
op|':'
string|'"host_reboot"'
op|','
string|'"shutdown"'
op|':'
string|'"host_shutdown"'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'call_xenhost'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'methods'
op|'['
name|'action'
op|']'
op|','
name|'args'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'get'
op|'('
string|'"power_action"'
op|','
name|'response'
op|')'
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
name|'host_list'
op|'='
op|'['
name|'host_ref'
name|'for'
name|'host_ref'
name|'in'
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'host'
op|'.'
name|'get_all'
op|'('
op|')'
nl|'\n'
name|'if'
name|'host_ref'
op|'!='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'host_ref'
op|']'
newline|'\n'
name|'migrations_counter'
op|'='
name|'vm_counter'
op|'='
number|'0'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'vm_ref'
op|','
name|'vm_rec'
name|'in'
name|'vm_utils'
op|'.'
name|'list_vms'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'host_ref'
name|'in'
name|'host_list'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
comment|'# Ensure only guest instances are migrated'
nl|'\n'
indent|'                    '
name|'uuid'
op|'='
name|'vm_rec'
op|'['
string|"'other_config'"
op|']'
op|'.'
name|'get'
op|'('
string|"'nova_uuid'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'uuid'
op|':'
newline|'\n'
indent|'                        '
name|'name'
op|'='
name|'vm_rec'
op|'['
string|"'name_label'"
op|']'
newline|'\n'
name|'uuid'
op|'='
name|'_uuid_find'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'uuid'
op|':'
newline|'\n'
indent|'                            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Instance %(name)s running on %(host)s'"
nl|'\n'
string|"' could not be found in the database:'"
nl|'\n'
string|"' assuming it is a worker VM and skip'"
nl|'\n'
string|"' ping migration to a new host'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
dedent|''
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'vm_counter'
op|'='
name|'vm_counter'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
name|'aggregate'
op|'='
name|'aggregate_obj'
op|'.'
name|'AggregateList'
op|'.'
name|'get_by_host'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'host'
op|','
name|'key'
op|'='
name|'pool_states'
op|'.'
name|'POOL_FLAG'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'aggregate'
op|':'
newline|'\n'
indent|'                        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Aggregate for host %(host)s count not be'"
nl|'\n'
string|"' found.'"
op|')'
op|'%'
name|'dict'
op|'('
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'dest'
op|'='
name|'_host_find'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'_session'
op|','
name|'aggregate'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'host_ref'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'host'
op|'='
name|'dest'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'MIGRATING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VM'
op|'.'
name|'pool_migrate'
op|'('
name|'vm_ref'
op|','
name|'host_ref'
op|','
nl|'\n'
op|'{'
string|'"live"'
op|':'
string|'"true"'
op|'}'
op|')'
newline|'\n'
name|'migrations_counter'
op|'='
name|'migrations_counter'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
name|'instance'
op|'.'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Unable to migrate VM %(vm_ref)s '"
nl|'\n'
string|"'from %(host)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'vm_ref'"
op|':'
name|'vm_ref'
op|','
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'instance'
op|'.'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'vm_counter'
op|'=='
name|'migrations_counter'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'on_maintenance'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|"'Unable to find suitable '"
nl|'\n'
string|"'host for VMs evacuation'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_host_enabled
dedent|''
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
comment|'# Since capabilities are gone, use service table to disable a node'
nl|'\n'
comment|'# in scheduler'
nl|'\n'
name|'status'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'not'
name|'enabled'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'set by xenapi host_state'"
nl|'\n'
op|'}'
newline|'\n'
name|'cntxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'_conductor_api'
op|'.'
name|'service_get_by_args'
op|'('
nl|'\n'
name|'cntxt'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
string|"'nova-compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conductor_api'
op|'.'
name|'service_update'
op|'('
nl|'\n'
name|'cntxt'
op|','
nl|'\n'
name|'service'
op|','
nl|'\n'
name|'status'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
string|'"enabled"'
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'enabled'
op|')'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'call_xenhost'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|'"set_host_enabled"'
op|','
name|'args'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'get'
op|'('
string|'"status"'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_uptime
dedent|''
name|'def'
name|'get_host_uptime'
op|'('
name|'self'
op|','
name|'_host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the result of calling "uptime" on the target host."""'
newline|'\n'
name|'response'
op|'='
name|'call_xenhost'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|'"host_uptime"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'get'
op|'('
string|'"uptime"'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostState
dedent|''
dedent|''
name|'class'
name|'HostState'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages information about the XenServer host this compute\n    node is running on.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'HostState'
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
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'_stats'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_pci_device_filter'
op|'='
name|'pci_whitelist'
op|'.'
name|'get_pci_devices_filter'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'update_status'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_passthrough_devices
dedent|''
name|'def'
name|'_get_passthrough_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list pci devices that are available for pci passthtough.\n\n        We use a plugin to get the output of the lspci command runs on dom0.\n        From this list we will extract pci devices that are using the pciback\n        kernel driver. Then we compare this list to the pci whitelist to get\n        a new list of pci devices that can be used for pci passthrough.\n\n        :returns: a list of pci devices available for pci passthrough.\n        """'
newline|'\n'
DECL|function|_compile_hex
name|'def'
name|'_compile_hex'
op|'('
name|'pattern'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Return a compiled regular expression pattern into which we have\n            replaced occurrences of hex by [\\da-fA-F].\n            """'
newline|'\n'
name|'return'
name|'re'
op|'.'
name|'compile'
op|'('
name|'pattern'
op|'.'
name|'replace'
op|'('
string|'"hex"'
op|','
string|'r"[\\da-fA-F]"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_parse_pci_device_string
dedent|''
name|'def'
name|'_parse_pci_device_string'
op|'('
name|'dev_string'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Exctract information from the device string about the slot, the\n            vendor and the product ID. The string is as follow:\n                "Slot:\\tBDF\\nClass:\\txxxx\\nVendor:\\txxxx\\nDevice:\\txxxx\\n..."\n            Return a dictionary with informations about the device.\n            """'
newline|'\n'
name|'slot_regex'
op|'='
name|'_compile_hex'
op|'('
string|'r"Slot:\\t"'
nl|'\n'
string|'r"((?:hex{4}:)?"'
comment|'# Domain: (optional)'
nl|'\n'
string|'r"hex{2}:"'
comment|'# Bus:'
nl|'\n'
string|'r"hex{2}\\."'
comment|'# Device.'
nl|'\n'
string|'r"hex{1})"'
op|')'
comment|'# Function'
newline|'\n'
name|'vendor_regex'
op|'='
name|'_compile_hex'
op|'('
string|'r"\\nVendor:\\t(hex+)"'
op|')'
newline|'\n'
name|'product_regex'
op|'='
name|'_compile_hex'
op|'('
string|'r"\\nDevice:\\t(hex+)"'
op|')'
newline|'\n'
nl|'\n'
name|'slot_id'
op|'='
name|'slot_regex'
op|'.'
name|'findall'
op|'('
name|'dev_string'
op|')'
newline|'\n'
name|'vendor_id'
op|'='
name|'vendor_regex'
op|'.'
name|'findall'
op|'('
name|'dev_string'
op|')'
newline|'\n'
name|'product_id'
op|'='
name|'product_regex'
op|'.'
name|'findall'
op|'('
name|'dev_string'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'slot_id'
name|'or'
name|'not'
name|'vendor_id'
name|'or'
name|'not'
name|'product_id'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Failed to parse information about"'
nl|'\n'
string|'" a pci device for passthrough"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'type_pci'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_plugin_serialized'
op|'('
nl|'\n'
string|"'xenhost'"
op|','
string|"'get_pci_type'"
op|','
name|'slot_id'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'label'"
op|':'
string|"'_'"
op|'.'
name|'join'
op|'('
op|'['
string|"'label'"
op|','
nl|'\n'
name|'vendor_id'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'product_id'
op|'['
number|'0'
op|']'
op|']'
op|')'
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
name|'vendor_id'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'product_id'"
op|':'
name|'product_id'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'slot_id'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'dev_id'"
op|':'
string|"'_'"
op|'.'
name|'join'
op|'('
op|'['
string|"'pci'"
op|','
name|'slot_id'
op|'['
number|'0'
op|']'
op|']'
op|')'
op|','
nl|'\n'
string|"'dev_type'"
op|':'
name|'type_pci'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
nl|'\n'
comment|'# Devices are separated by a blank line. That is why we'
nl|'\n'
comment|'# use "\\n\\n" as separator.'
nl|'\n'
dedent|''
name|'lspci_out'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_plugin_serialized'
op|'('
nl|'\n'
string|"'xenhost'"
op|','
string|"'get_pci_device_details'"
op|')'
newline|'\n'
name|'pci_list'
op|'='
name|'lspci_out'
op|'.'
name|'split'
op|'('
string|'"\\n\\n"'
op|')'
newline|'\n'
nl|'\n'
comment|'# For each device of the list, check if it uses the pciback'
nl|'\n'
comment|'# kernel driver and if it does, get informations and add it'
nl|'\n'
comment|'# to the list of passthrough_devices. Ignore it if the driver'
nl|'\n'
comment|'# is not pciback.'
nl|'\n'
name|'passthrough_devices'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'dev_string_info'
name|'in'
name|'pci_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|'"Driver:\\tpciback"'
name|'in'
name|'dev_string_info'
op|':'
newline|'\n'
indent|'                '
name|'new_dev'
op|'='
name|'_parse_pci_device_string'
op|'('
name|'dev_string_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_pci_device_filter'
op|'.'
name|'device_assignable'
op|'('
name|'new_dev'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'passthrough_devices'
op|'.'
name|'append'
op|'('
name|'new_dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'passthrough_devices'
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
string|'"""Return the current state of the host. If \'refresh\' is\n        True, run the update first.\n        """'
newline|'\n'
name|'if'
name|'refresh'
name|'or'
name|'not'
name|'self'
op|'.'
name|'_stats'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'update_status'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_stats'
newline|'\n'
nl|'\n'
DECL|member|update_status
dedent|''
name|'def'
name|'update_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Since under Xenserver, a compute node runs on a given host,\n        we can get host status information using xenapi.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Updating host stats"'
op|')'
op|')'
newline|'\n'
name|'data'
op|'='
name|'call_xenhost'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|'"host_data"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'sr_ref'
op|'='
name|'vm_utils'
op|'.'
name|'scan_default_sr'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
name|'sr_rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'SR'
op|'.'
name|'get_record'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
name|'total'
op|'='
name|'int'
op|'('
name|'sr_rec'
op|'['
string|'"physical_size"'
op|']'
op|')'
newline|'\n'
name|'used'
op|'='
name|'int'
op|'('
name|'sr_rec'
op|'['
string|'"physical_utilisation"'
op|']'
op|')'
newline|'\n'
name|'data'
op|'['
string|'"disk_total"'
op|']'
op|'='
name|'total'
newline|'\n'
name|'data'
op|'['
string|'"disk_used"'
op|']'
op|'='
name|'used'
newline|'\n'
name|'data'
op|'['
string|'"disk_available"'
op|']'
op|'='
name|'total'
op|'-'
name|'used'
newline|'\n'
name|'data'
op|'['
string|'"supported_instances"'
op|']'
op|'='
name|'to_supported_instances'
op|'('
nl|'\n'
name|'data'
op|'.'
name|'get'
op|'('
string|'"host_capabilities"'
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'host_memory'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'host_memory'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'host_memory'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'['
string|'"host_memory_total"'
op|']'
op|'='
name|'host_memory'
op|'.'
name|'get'
op|'('
string|"'total'"
op|','
number|'0'
op|')'
newline|'\n'
name|'data'
op|'['
string|'"host_memory_overhead"'
op|']'
op|'='
name|'host_memory'
op|'.'
name|'get'
op|'('
string|"'overhead'"
op|','
number|'0'
op|')'
newline|'\n'
name|'data'
op|'['
string|'"host_memory_free"'
op|']'
op|'='
name|'host_memory'
op|'.'
name|'get'
op|'('
string|"'free'"
op|','
number|'0'
op|')'
newline|'\n'
name|'data'
op|'['
string|'"host_memory_free_computed"'
op|']'
op|'='
name|'host_memory'
op|'.'
name|'get'
op|'('
nl|'\n'
string|"'free-computed'"
op|','
number|'0'
op|')'
newline|'\n'
name|'del'
name|'data'
op|'['
string|"'host_memory'"
op|']'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'data'
op|'['
string|"'host_hostname'"
op|']'
op|'!='
nl|'\n'
name|'self'
op|'.'
name|'_stats'
op|'.'
name|'get'
op|'('
string|"'host_hostname'"
op|','
name|'data'
op|'['
string|"'host_hostname'"
op|']'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Hostname has changed from %(old)s '"
nl|'\n'
string|"'to %(new)s. A restart is required to take effect.'"
nl|'\n'
op|')'
op|'%'
op|'{'
string|"'old'"
op|':'
name|'self'
op|'.'
name|'_stats'
op|'['
string|"'host_hostname'"
op|']'
op|','
nl|'\n'
string|"'new'"
op|':'
name|'data'
op|'['
string|"'host_hostname'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'data'
op|'['
string|"'host_hostname'"
op|']'
op|'='
name|'self'
op|'.'
name|'_stats'
op|'['
string|"'host_hostname'"
op|']'
newline|'\n'
dedent|''
name|'data'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
name|'data'
op|'['
string|"'host_hostname'"
op|']'
newline|'\n'
name|'vcpus_used'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'vm_ref'
op|','
name|'vm_rec'
name|'in'
name|'vm_utils'
op|'.'
name|'list_vms'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'vcpus_used'
op|'='
name|'vcpus_used'
op|'+'
name|'int'
op|'('
name|'vm_rec'
op|'['
string|"'VCPUs_max'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'data'
op|'['
string|"'vcpus_used'"
op|']'
op|'='
name|'vcpus_used'
newline|'\n'
name|'data'
op|'['
string|"'pci_passthrough_devices'"
op|']'
op|'='
name|'self'
op|'.'
name|'_get_passthrough_devices'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_stats'
op|'='
name|'data'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|to_supported_instances
dedent|''
dedent|''
dedent|''
name|'def'
name|'to_supported_instances'
op|'('
name|'host_capabilities'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'host_capabilities'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'capability'
name|'in'
name|'host_capabilities'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ostype'
op|','
name|'_version'
op|','
name|'arch'
op|'='
name|'capability'
op|'.'
name|'split'
op|'('
string|'"-"'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'append'
op|'('
op|'('
name|'arch'
op|','
string|"'xapi'"
op|','
name|'ostype'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Failed to extract instance support from %s"'
op|')'
op|','
name|'capability'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|call_xenhost
dedent|''
name|'def'
name|'call_xenhost'
op|'('
name|'session'
op|','
name|'method'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""There will be several methods that will need this general\n    handling for interacting with the xenhost plugin, so this abstracts\n    out that behavior.\n    """'
newline|'\n'
comment|"# Create a task ID as something that won't match any instance ID"
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'session'
op|'.'
name|'call_plugin'
op|'('
string|"'xenhost'"
op|','
name|'method'
op|','
name|'args'
op|'='
name|'arg_dict'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"''"
newline|'\n'
dedent|''
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Unable to get updated status"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"The call to %(method)s returned "'
nl|'\n'
string|'"an error: %(e)s."'
op|')'
op|','
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'e'
op|'.'
name|'details'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_uuid_find
dedent|''
dedent|''
name|'def'
name|'_uuid_find'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'name_label'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return instance uuid by name_label."""'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'instance_obj'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'i'
op|'.'
name|'name'
op|'=='
name|'name_label'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'i'
op|'.'
name|'uuid'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_host_find
dedent|''
name|'def'
name|'_host_find'
op|'('
name|'context'
op|','
name|'session'
op|','
name|'src_aggregate'
op|','
name|'host_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the host from the xenapi host reference.\n\n    :param src_aggregate: the aggregate that the compute host being put in\n                          maintenance (source of VMs) belongs to\n    :param host_ref: the hypervisor host reference (destination of VMs)\n\n    :return: the compute host that manages host_ref\n    """'
newline|'\n'
comment|'# NOTE: this would be a lot simpler if nova-compute stored'
nl|'\n'
comment|"# CONF.host in the XenServer host's other-config map."
nl|'\n'
comment|'# TODO(armando-migliaccio): improve according the note above'
nl|'\n'
name|'uuid'
op|'='
name|'session'
op|'.'
name|'host'
op|'.'
name|'get_uuid'
op|'('
name|'host_ref'
op|')'
newline|'\n'
name|'for'
name|'compute_host'
op|','
name|'host_uuid'
name|'in'
name|'src_aggregate'
op|'.'
name|'metadetails'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'host_uuid'
op|'=='
name|'uuid'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'compute_host'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|"'Host %(host_uuid)s could not be found '"
nl|'\n'
string|"'from aggregate metadata: %(metadata)s.'"
op|'%'
nl|'\n'
op|'{'
string|"'host_uuid'"
op|':'
name|'uuid'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'src_aggregate'
op|'.'
name|'metadetails'
op|'}'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
