begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# Copyright (c) 2012 VMware, Inc.'
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
string|'"""\nManagement class for Storage-related functions (attach, detach, etc).\n"""'
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
name|'log'
name|'as'
name|'logging'
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
name|'vm_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'volume_util'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
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
DECL|class|VMwareVolumeOps
name|'class'
name|'VMwareVolumeOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Management class for Volume-related tasks\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'cluster'
op|'='
name|'None'
op|','
name|'vc_support'
op|'='
name|'False'
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
name|'_cluster'
op|'='
name|'cluster'
newline|'\n'
name|'self'
op|'.'
name|'_vc_support'
op|'='
name|'vc_support'
newline|'\n'
nl|'\n'
DECL|member|attach_disk_to_vm
dedent|''
name|'def'
name|'attach_disk_to_vm'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'instance'
op|','
nl|'\n'
name|'adapter_type'
op|','
name|'disk_type'
op|','
name|'vmdk_path'
op|'='
name|'None'
op|','
nl|'\n'
name|'disk_size'
op|'='
name|'None'
op|','
name|'linked_clone'
op|'='
name|'False'
op|','
nl|'\n'
name|'controller_key'
op|'='
name|'None'
op|','
name|'unit_number'
op|'='
name|'None'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Attach disk to VM by reconfiguration.\n        """'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'client_factory'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'vmdk_attach_config_spec'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_attach_config_spec'
op|'('
nl|'\n'
name|'client_factory'
op|','
name|'adapter_type'
op|','
name|'disk_type'
op|','
nl|'\n'
name|'vmdk_path'
op|','
name|'disk_size'
op|','
name|'linked_clone'
op|','
nl|'\n'
name|'controller_key'
op|','
name|'unit_number'
op|','
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reconfiguring VM instance %(instance_name)s to attach "'
nl|'\n'
string|'"disk %(vmdk_path)s or device %(device_name)s with type "'
nl|'\n'
string|'"%(disk_type)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
string|"'vmdk_path'"
op|':'
name|'vmdk_path'
op|','
nl|'\n'
string|"'device_name'"
op|':'
name|'device_name'
op|','
string|"'disk_type'"
op|':'
name|'disk_type'
op|'}'
op|')'
newline|'\n'
name|'reconfig_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"ReconfigVM_Task"'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'spec'
op|'='
name|'vmdk_attach_config_spec'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_wait_for_task'
op|'('
name|'instance_uuid'
op|','
name|'reconfig_task'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reconfigured VM instance %(instance_name)s to attach "'
nl|'\n'
string|'"disk %(vmdk_path)s or device %(device_name)s with type "'
nl|'\n'
string|'"%(disk_type)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
string|"'vmdk_path'"
op|':'
name|'vmdk_path'
op|','
nl|'\n'
string|"'device_name'"
op|':'
name|'device_name'
op|','
string|"'disk_type'"
op|':'
name|'disk_type'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_update_volume_details
dedent|''
name|'def'
name|'_update_volume_details'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'instance'
op|','
name|'volume_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Store the uuid of the volume_device'
nl|'\n'
name|'hw_devices'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|"'get_dynamic_property'"
op|','
nl|'\n'
name|'vm_ref'
op|','
string|"'VirtualMachine'"
op|','
nl|'\n'
string|"'config.hardware.device'"
op|')'
newline|'\n'
name|'device_uuid'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_backed_disk_uuid'
op|'('
name|'hw_devices'
op|','
nl|'\n'
name|'volume_uuid'
op|')'
newline|'\n'
name|'volume_option'
op|'='
string|"'volume-%s'"
op|'%'
name|'volume_uuid'
newline|'\n'
name|'extra_opts'
op|'='
op|'{'
name|'volume_option'
op|':'
name|'device_uuid'
op|'}'
newline|'\n'
nl|'\n'
name|'client_factory'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'extra_config_specs'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_extra_config_spec'
op|'('
nl|'\n'
name|'client_factory'
op|','
name|'extra_opts'
op|')'
newline|'\n'
nl|'\n'
name|'reconfig_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"ReconfigVM_Task"'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'spec'
op|'='
name|'extra_config_specs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_wait_for_task'
op|'('
name|'instance_uuid'
op|','
name|'reconfig_task'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_volume_uuid
dedent|''
name|'def'
name|'_get_volume_uuid'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'volume_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_option'
op|'='
string|"'volume-%s'"
op|'%'
name|'volume_uuid'
newline|'\n'
name|'extra_config'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|"'get_dynamic_property'"
op|','
nl|'\n'
name|'vm_ref'
op|','
string|"'VirtualMachine'"
op|','
nl|'\n'
string|"'config.extraConfig'"
op|')'
newline|'\n'
name|'if'
name|'extra_config'
op|':'
newline|'\n'
indent|'            '
name|'options'
op|'='
name|'extra_config'
op|'.'
name|'OptionValue'
newline|'\n'
name|'for'
name|'option'
name|'in'
name|'options'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'option'
op|'.'
name|'key'
op|'=='
name|'volume_option'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'option'
op|'.'
name|'value'
newline|'\n'
nl|'\n'
DECL|member|detach_disk_from_vm
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'detach_disk_from_vm'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'instance'
op|','
name|'device'
op|','
nl|'\n'
name|'destroy_disk'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Detach disk from VM by reconfiguration.\n        """'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'client_factory'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'vmdk_detach_config_spec'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_detach_config_spec'
op|'('
nl|'\n'
name|'client_factory'
op|','
name|'device'
op|','
name|'destroy_disk'
op|')'
newline|'\n'
name|'disk_key'
op|'='
name|'device'
op|'.'
name|'key'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reconfiguring VM instance %(instance_name)s to detach "'
nl|'\n'
string|'"disk %(disk_key)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
string|"'disk_key'"
op|':'
name|'disk_key'
op|'}'
op|')'
newline|'\n'
name|'reconfig_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"ReconfigVM_Task"'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'spec'
op|'='
name|'vmdk_detach_config_spec'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_wait_for_task'
op|'('
name|'instance_uuid'
op|','
name|'reconfig_task'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reconfigured VM instance %(instance_name)s to detach "'
nl|'\n'
string|'"disk %(disk_key)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
string|"'disk_key'"
op|':'
name|'disk_key'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|discover_st
dedent|''
name|'def'
name|'discover_st'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Discover iSCSI targets."""'
newline|'\n'
name|'target_portal'
op|'='
name|'data'
op|'['
string|"'target_portal'"
op|']'
newline|'\n'
name|'target_iqn'
op|'='
name|'data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Discovering iSCSI target %(target_iqn)s from "'
nl|'\n'
string|'"%(target_portal)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
string|"'target_portal'"
op|':'
name|'target_portal'
op|'}'
op|')'
newline|'\n'
name|'device_name'
op|','
name|'uuid'
op|'='
name|'volume_util'
op|'.'
name|'find_st'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'data'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_cluster'
op|')'
newline|'\n'
name|'if'
name|'device_name'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Storage target found. No need to discover"'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'device_name'
op|','
name|'uuid'
op|')'
newline|'\n'
comment|'# Rescan iSCSI HBA'
nl|'\n'
dedent|''
name|'volume_util'
op|'.'
name|'rescan_iscsi_hba'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'self'
op|'.'
name|'_cluster'
op|')'
newline|'\n'
comment|'# Find iSCSI Target again'
nl|'\n'
name|'device_name'
op|','
name|'uuid'
op|'='
name|'volume_util'
op|'.'
name|'find_st'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'data'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_cluster'
op|')'
newline|'\n'
name|'if'
name|'device_name'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Discovered iSCSI target %(target_iqn)s from "'
nl|'\n'
string|'"%(target_portal)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
nl|'\n'
string|"'target_portal'"
op|':'
name|'target_portal'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Unable to discovered iSCSI target %(target_iqn)s "'
nl|'\n'
string|'"from %(target_portal)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
nl|'\n'
string|"'target_portal'"
op|':'
name|'target_portal'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'('
name|'device_name'
op|','
name|'uuid'
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
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vm_ref'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'vm_ref'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'iqn'
op|'='
name|'volume_util'
op|'.'
name|'get_host_iqn'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'self'
op|'.'
name|'_cluster'
op|')'
newline|'\n'
name|'connector'
op|'='
op|'{'
string|"'ip'"
op|':'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'host_ip'
op|','
nl|'\n'
string|"'initiator'"
op|':'
name|'iqn'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'host_ip'
op|'}'
newline|'\n'
name|'if'
name|'vm_ref'
op|':'
newline|'\n'
indent|'            '
name|'connector'
op|'['
string|"'instance'"
op|']'
op|'='
name|'vm_ref'
op|'.'
name|'value'
newline|'\n'
dedent|''
name|'return'
name|'connector'
newline|'\n'
nl|'\n'
DECL|member|_get_unit_number
dedent|''
name|'def'
name|'_get_unit_number'
op|'('
name|'self'
op|','
name|'mountpoint'
op|','
name|'unit_number'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a unit number for the device."""'
newline|'\n'
name|'mount_unit'
op|'='
name|'volume_util'
op|'.'
name|'mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
comment|'# Figure out the correct unit number'
nl|'\n'
name|'if'
name|'unit_number'
op|'<'
name|'mount_unit'
op|':'
newline|'\n'
indent|'            '
name|'new_unit_number'
op|'='
name|'mount_unit'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'new_unit_number'
op|'='
name|'unit_number'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'return'
name|'new_unit_number'
newline|'\n'
nl|'\n'
DECL|member|_get_volume_ref
dedent|''
name|'def'
name|'_get_volume_ref'
op|'('
name|'self'
op|','
name|'volume_ref_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the volume moref from the ref name."""'
newline|'\n'
name|'return'
name|'vim'
op|'.'
name|'get_moref'
op|'('
name|'volume_ref_name'
op|','
string|"'VirtualMachine'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vmdk_base_volume_device
dedent|''
name|'def'
name|'_get_vmdk_base_volume_device'
op|'('
name|'self'
op|','
name|'volume_ref'
op|')'
op|':'
newline|'\n'
comment|'# Get the vmdk file name that the VM is pointing to'
nl|'\n'
indent|'        '
name|'hardware_devices'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'volume_ref'
op|','
nl|'\n'
string|'"VirtualMachine"'
op|','
string|'"config.hardware.device"'
op|')'
newline|'\n'
name|'return'
name|'vm_util'
op|'.'
name|'get_vmdk_volume_disk'
op|'('
name|'hardware_devices'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume_vmdk
dedent|''
name|'def'
name|'_attach_volume_vmdk'
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
string|'"""Attach vmdk volume storage to VM instance."""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vm_ref'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|')'
newline|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Get volume details from volume ref'
nl|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'_get_volume_ref'
op|'('
name|'data'
op|'['
string|"'volume'"
op|']'
op|')'
newline|'\n'
name|'volume_device'
op|'='
name|'self'
op|'.'
name|'_get_vmdk_base_volume_device'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
name|'volume_vmdk_path'
op|'='
name|'volume_device'
op|'.'
name|'backing'
op|'.'
name|'fileName'
newline|'\n'
nl|'\n'
comment|'# Get details required for adding disk device such as'
nl|'\n'
comment|'# adapter_type, unit_number, controller_key'
nl|'\n'
name|'hw_devices'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|"'get_dynamic_property'"
op|','
nl|'\n'
name|'vm_ref'
op|','
string|"'VirtualMachine'"
op|','
nl|'\n'
string|"'config.hardware.device'"
op|')'
newline|'\n'
op|'('
name|'vmdk_file_path'
op|','
name|'controller_key'
op|','
name|'adapter_type'
op|','
name|'disk_type'
op|','
nl|'\n'
name|'unit_number'
op|')'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_path_and_adapter_type'
op|'('
name|'hw_devices'
op|')'
newline|'\n'
nl|'\n'
name|'unit_number'
op|'='
name|'self'
op|'.'
name|'_get_unit_number'
op|'('
name|'mountpoint'
op|','
name|'unit_number'
op|')'
newline|'\n'
comment|'# Attach the disk to virtual machine instance'
nl|'\n'
name|'volume_device'
op|'='
name|'self'
op|'.'
name|'attach_disk_to_vm'
op|'('
name|'vm_ref'
op|','
name|'instance'
op|','
name|'adapter_type'
op|','
nl|'\n'
name|'disk_type'
op|','
nl|'\n'
name|'vmdk_path'
op|'='
name|'volume_vmdk_path'
op|','
nl|'\n'
name|'controller_key'
op|'='
name|'controller_key'
op|','
nl|'\n'
name|'unit_number'
op|'='
name|'unit_number'
op|')'
newline|'\n'
nl|'\n'
comment|'# Store the uuid of the volume_device'
nl|'\n'
name|'self'
op|'.'
name|'_update_volume_details'
op|'('
name|'vm_ref'
op|','
name|'instance'
op|','
name|'data'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Mountpoint %(mountpoint)s attached to "'
nl|'\n'
string|'"instance %(instance_name)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|','
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume_iscsi
dedent|''
name|'def'
name|'_attach_volume_iscsi'
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
string|'"""Attach iscsi volume storage to VM instance."""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vm_ref'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|')'
newline|'\n'
comment|'# Attach Volume to VM'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attach_volume: %(connection_info)s, %(instance_name)s, "'
nl|'\n'
string|'"%(mountpoint)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
name|'connection_info'
op|','
nl|'\n'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Discover iSCSI Target'
nl|'\n'
name|'device_name'
op|','
name|'uuid'
op|'='
name|'self'
op|'.'
name|'discover_st'
op|'('
name|'data'
op|')'
newline|'\n'
name|'if'
name|'device_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'volume_util'
op|'.'
name|'StorageError'
op|'('
name|'_'
op|'('
string|'"Unable to find iSCSI Target"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the vmdk file name that the VM is pointing to'
nl|'\n'
dedent|''
name|'hardware_devices'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'vm_ref'
op|','
nl|'\n'
string|'"VirtualMachine"'
op|','
string|'"config.hardware.device"'
op|')'
newline|'\n'
name|'vmdk_file_path'
op|','
name|'controller_key'
op|','
name|'adapter_type'
op|','
name|'disk_type'
op|','
name|'unit_number'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_path_and_adapter_type'
op|'('
name|'hardware_devices'
op|')'
newline|'\n'
nl|'\n'
name|'unit_number'
op|'='
name|'self'
op|'.'
name|'_get_unit_number'
op|'('
name|'mountpoint'
op|','
name|'unit_number'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'attach_disk_to_vm'
op|'('
name|'vm_ref'
op|','
name|'instance'
op|','
nl|'\n'
name|'adapter_type'
op|','
string|"'rdmp'"
op|','
nl|'\n'
name|'controller_key'
op|'='
name|'controller_key'
op|','
nl|'\n'
name|'unit_number'
op|'='
name|'unit_number'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'device_name'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Mountpoint %(mountpoint)s attached to "'
nl|'\n'
string|'"instance %(instance_name)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|','
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
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
name|'driver_type'
op|'='
name|'connection_info'
op|'['
string|"'driver_volume_type'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Volume attach. Driver type: %s"'
op|')'
op|','
name|'driver_type'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'driver_type'
op|'=='
string|"'vmdk'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_attach_volume_vmdk'
op|'('
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'driver_type'
op|'=='
string|"'iscsi'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_attach_volume_iscsi'
op|'('
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeDriverNotFound'
op|'('
name|'driver_type'
op|'='
name|'driver_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_relocate_vmdk_volume
dedent|''
dedent|''
name|'def'
name|'_relocate_vmdk_volume'
op|'('
name|'self'
op|','
name|'volume_ref'
op|','
name|'res_pool'
op|','
name|'datastore'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Relocate the volume.\n\n        The move type will be moveAllDiskBackingsAndAllowSharing.\n        """'
newline|'\n'
name|'client_factory'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'spec'
op|'='
name|'vm_util'
op|'.'
name|'relocate_vm_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
name|'datastore'
op|'='
name|'datastore'
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'pool'
op|'='
name|'res_pool'
newline|'\n'
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"RelocateVM_Task"'
op|','
name|'volume_ref'
op|','
nl|'\n'
name|'spec'
op|'='
name|'spec'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_wait_for_task'
op|'('
name|'task'
op|'.'
name|'value'
op|','
name|'task'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_res_pool_of_vm
dedent|''
name|'def'
name|'_get_res_pool_of_vm'
op|'('
name|'self'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get resource pool to which the VM belongs."""'
newline|'\n'
comment|'# Get the host, the VM belongs to'
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|"'get_dynamic_property'"
op|','
nl|'\n'
name|'vm_ref'
op|','
string|"'VirtualMachine'"
op|','
nl|'\n'
string|"'runtime'"
op|')'
op|'.'
name|'host'
newline|'\n'
comment|'# Get the compute resource, the host belongs to'
nl|'\n'
name|'compute_res'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|"'get_dynamic_property'"
op|','
nl|'\n'
name|'host'
op|','
string|"'HostSystem'"
op|','
nl|'\n'
string|"'parent'"
op|')'
newline|'\n'
comment|'# Get resource pool from the compute resource'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|"'get_dynamic_property'"
op|','
nl|'\n'
name|'compute_res'
op|','
name|'compute_res'
op|'.'
name|'_type'
op|','
nl|'\n'
string|"'resourcePool'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_consolidate_vmdk_volume
dedent|''
name|'def'
name|'_consolidate_vmdk_volume'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vm_ref'
op|','
name|'device'
op|','
name|'volume_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Consolidate volume backing VMDK files if needed.\n\n        The volume\'s VMDK file attached to an instance can be moved by SDRS\n        if enabled on the cluster.\n        By this the VMDK files can get copied onto another datastore and the\n        copy on this new location will be the latest version of the VMDK file.\n        So at the time of detach, we need to consolidate the current backing\n        VMDK file with the VMDK file in the new location.\n\n        We need to ensure that the VMDK chain (snapshots) remains intact during\n        the consolidation. SDRS retains the chain when it copies VMDK files\n        over, so for consolidation we relocate the backing with move option\n        as moveAllDiskBackingsAndAllowSharing and then delete the older version\n        of the VMDK file attaching the new version VMDK file.\n\n        In the case of a volume boot the we need to ensure that the volume\n        is on the datastore of the instance.\n        """'
newline|'\n'
nl|'\n'
comment|'# Consolidation only supported with VC driver'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_vc_support'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'original_device'
op|'='
name|'self'
op|'.'
name|'_get_vmdk_base_volume_device'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
nl|'\n'
name|'original_device_path'
op|'='
name|'original_device'
op|'.'
name|'backing'
op|'.'
name|'fileName'
newline|'\n'
name|'current_device_path'
op|'='
name|'device'
op|'.'
name|'backing'
op|'.'
name|'fileName'
newline|'\n'
nl|'\n'
name|'if'
name|'original_device_path'
op|'=='
name|'current_device_path'
op|':'
newline|'\n'
comment|'# The volume is not moved from its original location.'
nl|'\n'
comment|'# No consolidation is required.'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"The volume has not been displaced from "'
nl|'\n'
string|'"its original location: %s. No consolidation "'
nl|'\n'
string|'"needed."'
op|')'
op|','
name|'current_device_path'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
comment|'# The volume has been moved from its original location.'
nl|'\n'
comment|'# Need to consolidate the VMDK files.'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"The volume\'s backing has been relocated to %s. Need to "'
nl|'\n'
string|'"consolidate backing disk file."'
op|')'
op|','
name|'current_device_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Pick the resource pool on which the instance resides.'
nl|'\n'
comment|'# Move the volume to the datastore where the new VMDK file is present.'
nl|'\n'
name|'res_pool'
op|'='
name|'self'
op|'.'
name|'_get_res_pool_of_vm'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'datastore'
op|'='
name|'device'
op|'.'
name|'backing'
op|'.'
name|'datastore'
newline|'\n'
name|'self'
op|'.'
name|'_relocate_vmdk_volume'
op|'('
name|'volume_ref'
op|','
name|'res_pool'
op|','
name|'datastore'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the original disk from the volume_ref'
nl|'\n'
name|'self'
op|'.'
name|'detach_disk_from_vm'
op|'('
name|'volume_ref'
op|','
name|'instance'
op|','
name|'original_device'
op|','
nl|'\n'
name|'destroy_disk'
op|'='
name|'True'
op|')'
newline|'\n'
comment|'# Attach the current disk to the volume_ref'
nl|'\n'
comment|'# Get details required for adding disk device such as'
nl|'\n'
comment|'# adapter_type, unit_number, controller_key'
nl|'\n'
name|'hw_devices'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|"'get_dynamic_property'"
op|','
nl|'\n'
name|'volume_ref'
op|','
string|"'VirtualMachine'"
op|','
nl|'\n'
string|"'config.hardware.device'"
op|')'
newline|'\n'
op|'('
name|'vmdk_file_path'
op|','
name|'controller_key'
op|','
name|'adapter_type'
op|','
name|'disk_type'
op|','
nl|'\n'
name|'unit_number'
op|')'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_path_and_adapter_type'
op|'('
name|'hw_devices'
op|')'
newline|'\n'
comment|'# Attach the current volume to the volume_ref'
nl|'\n'
name|'volume_device'
op|'='
name|'self'
op|'.'
name|'attach_disk_to_vm'
op|'('
name|'volume_ref'
op|','
name|'instance'
op|','
nl|'\n'
name|'adapter_type'
op|','
name|'disk_type'
op|','
nl|'\n'
name|'vmdk_path'
op|'='
name|'current_device_path'
op|','
nl|'\n'
name|'controller_key'
op|'='
name|'controller_key'
op|','
nl|'\n'
name|'unit_number'
op|'='
name|'unit_number'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vmdk_backed_disk_device
dedent|''
name|'def'
name|'_get_vmdk_backed_disk_device'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'connection_info_data'
op|')'
op|':'
newline|'\n'
comment|'# Get the vmdk file name that the VM is pointing to'
nl|'\n'
indent|'        '
name|'hardware_devices'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'vm_ref'
op|','
nl|'\n'
string|'"VirtualMachine"'
op|','
string|'"config.hardware.device"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get disk uuid'
nl|'\n'
name|'disk_uuid'
op|'='
name|'self'
op|'.'
name|'_get_volume_uuid'
op|'('
name|'vm_ref'
op|','
nl|'\n'
name|'connection_info_data'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
name|'device'
op|'='
name|'vm_util'
op|'.'
name|'get_vmdk_backed_disk_device'
op|'('
name|'hardware_devices'
op|','
nl|'\n'
name|'disk_uuid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'volume_util'
op|'.'
name|'StorageError'
op|'('
name|'_'
op|'('
string|'"Unable to find volume"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'device'
newline|'\n'
nl|'\n'
DECL|member|_detach_volume_vmdk
dedent|''
name|'def'
name|'_detach_volume_vmdk'
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
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vm_ref'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|')'
newline|'\n'
comment|'# Detach Volume from VM'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Detach_volume: %(instance_name)s, %(mountpoint)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|','
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
nl|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_get_vmdk_backed_disk_device'
op|'('
name|'vm_ref'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the volume ref'
nl|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'_get_volume_ref'
op|'('
name|'data'
op|'['
string|"'volume'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_consolidate_vmdk_volume'
op|'('
name|'instance'
op|','
name|'vm_ref'
op|','
name|'device'
op|','
name|'volume_ref'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'detach_disk_from_vm'
op|'('
name|'vm_ref'
op|','
name|'instance'
op|','
name|'device'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Mountpoint %(mountpoint)s detached from "'
nl|'\n'
string|'"instance %(instance_name)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|','
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_detach_volume_iscsi
dedent|''
name|'def'
name|'_detach_volume_iscsi'
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
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vm_ref'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|')'
newline|'\n'
comment|'# Detach Volume from VM'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Detach_volume: %(instance_name)s, %(mountpoint)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|','
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Discover iSCSI Target'
nl|'\n'
name|'device_name'
op|','
name|'uuid'
op|'='
name|'volume_util'
op|'.'
name|'find_st'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'data'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_cluster'
op|')'
newline|'\n'
name|'if'
name|'device_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'volume_util'
op|'.'
name|'StorageError'
op|'('
name|'_'
op|'('
string|'"Unable to find iSCSI Target"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the vmdk file name that the VM is pointing to'
nl|'\n'
dedent|''
name|'hardware_devices'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'vm_ref'
op|','
nl|'\n'
string|'"VirtualMachine"'
op|','
string|'"config.hardware.device"'
op|')'
newline|'\n'
name|'device'
op|'='
name|'vm_util'
op|'.'
name|'get_rdm_disk'
op|'('
name|'hardware_devices'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'if'
name|'device'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'volume_util'
op|'.'
name|'StorageError'
op|'('
name|'_'
op|'('
string|'"Unable to find volume"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'detach_disk_from_vm'
op|'('
name|'vm_ref'
op|','
name|'instance'
op|','
name|'device'
op|','
name|'destroy_disk'
op|'='
name|'True'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Mountpoint %(mountpoint)s detached from "'
nl|'\n'
string|'"instance %(instance_name)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|','
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
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
name|'driver_type'
op|'='
name|'connection_info'
op|'['
string|"'driver_volume_type'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Volume detach. Driver type: %s"'
op|')'
op|','
name|'driver_type'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'driver_type'
op|'=='
string|"'vmdk'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_detach_volume_vmdk'
op|'('
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'driver_type'
op|'=='
string|"'iscsi'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_detach_volume_iscsi'
op|'('
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeDriverNotFound'
op|'('
name|'driver_type'
op|'='
name|'driver_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_root_volume
dedent|''
dedent|''
name|'def'
name|'attach_root_volume'
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
name|'datastore'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach a root volume to the VM instance."""'
newline|'\n'
name|'driver_type'
op|'='
name|'connection_info'
op|'['
string|"'driver_volume_type'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Root volume attach. Driver type: %s"'
op|')'
op|','
name|'driver_type'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'driver_type'
op|'=='
string|"'vmdk'"
op|':'
newline|'\n'
indent|'            '
name|'vm_ref'
op|'='
name|'vm_util'
op|'.'
name|'get_vm_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|')'
newline|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
comment|'# Get the volume ref'
nl|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'_get_volume_ref'
op|'('
name|'data'
op|'['
string|"'volume'"
op|']'
op|')'
newline|'\n'
comment|'# Pick the resource pool on which the instance resides. Move the'
nl|'\n'
comment|'# volume to the datastore of the instance.'
nl|'\n'
name|'res_pool'
op|'='
name|'self'
op|'.'
name|'_get_res_pool_of_vm'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_relocate_vmdk_volume'
op|'('
name|'volume_ref'
op|','
name|'res_pool'
op|','
name|'datastore'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'attach_volume'
op|'('
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
