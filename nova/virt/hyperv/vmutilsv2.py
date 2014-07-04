begin_unit
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
string|'"""\nUtility class for VM related operations.\nBased on the "root/virtualization/v2" namespace available starting with\nHyper-V Server / Windows Server 2012.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'wmi'
newline|'\n'
nl|'\n'
dedent|''
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
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
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
DECL|class|VMUtilsV2
name|'class'
name|'VMUtilsV2'
op|'('
name|'vmutils'
op|'.'
name|'VMUtils'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_PHYS_DISK_RES_SUB_TYPE
indent|'    '
name|'_PHYS_DISK_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Physical Disk Drive'"
newline|'\n'
DECL|variable|_DISK_DRIVE_RES_SUB_TYPE
name|'_DISK_DRIVE_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Synthetic Disk Drive'"
newline|'\n'
DECL|variable|_DVD_DRIVE_RES_SUB_TYPE
name|'_DVD_DRIVE_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Synthetic DVD Drive'"
newline|'\n'
DECL|variable|_SCSI_RES_SUBTYPE
name|'_SCSI_RES_SUBTYPE'
op|'='
string|"'Microsoft:Hyper-V:Synthetic SCSI Controller'"
newline|'\n'
DECL|variable|_HARD_DISK_RES_SUB_TYPE
name|'_HARD_DISK_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Virtual Hard Disk'"
newline|'\n'
DECL|variable|_DVD_DISK_RES_SUB_TYPE
name|'_DVD_DISK_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Virtual CD/DVD Disk'"
newline|'\n'
DECL|variable|_IDE_CTRL_RES_SUB_TYPE
name|'_IDE_CTRL_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Emulated IDE Controller'"
newline|'\n'
DECL|variable|_SCSI_CTRL_RES_SUB_TYPE
name|'_SCSI_CTRL_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Synthetic SCSI Controller'"
newline|'\n'
DECL|variable|_SERIAL_PORT_RES_SUB_TYPE
name|'_SERIAL_PORT_RES_SUB_TYPE'
op|'='
string|"'Microsoft:Hyper-V:Serial Port'"
newline|'\n'
nl|'\n'
DECL|variable|_VIRTUAL_SYSTEM_TYPE_REALIZED
name|'_VIRTUAL_SYSTEM_TYPE_REALIZED'
op|'='
string|"'Microsoft:Hyper-V:System:Realized'"
newline|'\n'
nl|'\n'
DECL|variable|_SNAPSHOT_FULL
name|'_SNAPSHOT_FULL'
op|'='
number|'2'
newline|'\n'
nl|'\n'
DECL|variable|_METRIC_AGGR_CPU_AVG
name|'_METRIC_AGGR_CPU_AVG'
op|'='
string|"'Aggregated Average CPU Utilization'"
newline|'\n'
DECL|variable|_METRIC_ENABLED
name|'_METRIC_ENABLED'
op|'='
number|'2'
newline|'\n'
nl|'\n'
DECL|variable|_STORAGE_ALLOC_SETTING_DATA_CLASS
name|'_STORAGE_ALLOC_SETTING_DATA_CLASS'
op|'='
string|"'Msvm_StorageAllocationSettingData'"
newline|'\n'
name|'_ETHERNET_PORT_ALLOCATION_SETTING_DATA_CLASS'
op|'='
DECL|variable|_ETHERNET_PORT_ALLOCATION_SETTING_DATA_CLASS
string|"'Msvm_EthernetPortAllocationSettingData'"
newline|'\n'
nl|'\n'
DECL|variable|_AUTOMATIC_STARTUP_ACTION_NONE
name|'_AUTOMATIC_STARTUP_ACTION_NONE'
op|'='
number|'2'
newline|'\n'
nl|'\n'
DECL|variable|_vm_power_states_map
name|'_vm_power_states_map'
op|'='
op|'{'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
op|':'
number|'2'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_DISABLED'
op|':'
number|'3'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_SHUTTING_DOWN'
op|':'
number|'4'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_REBOOT'
op|':'
number|'11'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_PAUSED'
op|':'
number|'9'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_SUSPENDED'
op|':'
number|'6'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|'='
string|"'.'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VMUtilsV2'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_init_hyperv_wmi_conn
dedent|''
name|'def'
name|'_init_hyperv_wmi_conn'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_conn'
op|'='
name|'wmi'
op|'.'
name|'WMI'
op|'('
name|'moniker'
op|'='
string|"'//%s/root/virtualization/v2'"
op|'%'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_instance_notes
dedent|''
name|'def'
name|'list_instance_notes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_notes'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'vs'
name|'in'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'('
nl|'\n'
op|'['
string|"'ElementName'"
op|','
string|"'Notes'"
op|']'
op|','
nl|'\n'
name|'VirtualSystemType'
op|'='
name|'self'
op|'.'
name|'_VIRTUAL_SYSTEM_TYPE_REALIZED'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_notes'
op|'.'
name|'append'
op|'('
op|'('
name|'vs'
op|'.'
name|'ElementName'
op|','
op|'['
name|'v'
name|'for'
name|'v'
name|'in'
name|'vs'
op|'.'
name|'Notes'
name|'if'
name|'v'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'instance_notes'
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
string|'"""Return the names of all the instances known to Hyper-V."""'
newline|'\n'
name|'return'
op|'['
name|'v'
op|'.'
name|'ElementName'
name|'for'
name|'v'
name|'in'
nl|'\n'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'('
nl|'\n'
op|'['
string|"'ElementName'"
op|']'
op|','
nl|'\n'
name|'VirtualSystemType'
op|'='
name|'self'
op|'.'
name|'_VIRTUAL_SYSTEM_TYPE_REALIZED'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_vm_obj
dedent|''
name|'def'
name|'_create_vm_obj'
op|'('
name|'self'
op|','
name|'vs_man_svc'
op|','
name|'vm_name'
op|','
name|'notes'
op|','
name|'dynamic_memory_ratio'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vs_data'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
name|'vs_data'
op|'.'
name|'ElementName'
op|'='
name|'vm_name'
newline|'\n'
name|'vs_data'
op|'.'
name|'Notes'
op|'='
name|'notes'
newline|'\n'
comment|"# Don't start automatically on host boot"
nl|'\n'
name|'vs_data'
op|'.'
name|'AutomaticStartupAction'
op|'='
name|'self'
op|'.'
name|'_AUTOMATIC_STARTUP_ACTION_NONE'
newline|'\n'
nl|'\n'
comment|'# vNUMA and dynamic memory are mutually exclusive'
nl|'\n'
name|'if'
name|'dynamic_memory_ratio'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'vs_data'
op|'.'
name|'VirtualNumaEnabled'
op|'='
name|'False'
newline|'\n'
nl|'\n'
dedent|''
op|'('
name|'job_path'
op|','
nl|'\n'
name|'vm_path'
op|','
nl|'\n'
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'DefineSystem'
op|'('
name|'ResourceSettings'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'ReferenceConfiguration'
op|'='
name|'None'
op|','
nl|'\n'
name|'SystemSettings'
op|'='
name|'vs_data'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'job'
op|'='
name|'self'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'vm_path'
name|'and'
name|'job'
op|':'
newline|'\n'
indent|'            '
name|'vm_path'
op|'='
name|'job'
op|'.'
name|'associators'
op|'('
name|'self'
op|'.'
name|'_AFFECTED_JOB_ELEMENT_CLASS'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_get_wmi_obj'
op|'('
name|'vm_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vm_setting_data
dedent|''
name|'def'
name|'_get_vm_setting_data'
op|'('
name|'self'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmsettings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
name|'self'
op|'.'
name|'_VIRTUAL_SYSTEM_SETTING_DATA_CLASS'
op|')'
newline|'\n'
comment|'# Avoid snapshots'
nl|'\n'
name|'return'
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'vmsettings'
name|'if'
nl|'\n'
name|'s'
op|'.'
name|'VirtualSystemType'
op|'=='
name|'self'
op|'.'
name|'_VIRTUAL_SYSTEM_TYPE_REALIZED'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_attach_drive
dedent|''
name|'def'
name|'_attach_drive'
op|'('
name|'self'
op|','
name|'vm'
op|','
name|'path'
op|','
name|'ctrller_path'
op|','
name|'drive_addr'
op|','
name|'drive_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a drive and attach it to the vm."""'
newline|'\n'
nl|'\n'
name|'if'
name|'drive_type'
op|'=='
name|'constants'
op|'.'
name|'DISK'
op|':'
newline|'\n'
indent|'            '
name|'res_sub_type'
op|'='
name|'self'
op|'.'
name|'_DISK_DRIVE_RES_SUB_TYPE'
newline|'\n'
dedent|''
name|'elif'
name|'drive_type'
op|'=='
name|'constants'
op|'.'
name|'DVD'
op|':'
newline|'\n'
indent|'            '
name|'res_sub_type'
op|'='
name|'self'
op|'.'
name|'_DVD_DRIVE_RES_SUB_TYPE'
newline|'\n'
nl|'\n'
dedent|''
name|'drive'
op|'='
name|'self'
op|'.'
name|'_get_new_resource_setting_data'
op|'('
name|'res_sub_type'
op|')'
newline|'\n'
nl|'\n'
comment|'# Set the ctrller as parent.'
nl|'\n'
name|'drive'
op|'.'
name|'Parent'
op|'='
name|'ctrller_path'
newline|'\n'
name|'drive'
op|'.'
name|'Address'
op|'='
name|'drive_addr'
newline|'\n'
name|'drive'
op|'.'
name|'AddressOnParent'
op|'='
name|'drive_addr'
newline|'\n'
comment|'# Add the cloned disk drive object to the vm.'
nl|'\n'
name|'new_resources'
op|'='
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'drive'
op|','
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
name|'drive_path'
op|'='
name|'new_resources'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'drive_type'
op|'=='
name|'constants'
op|'.'
name|'DISK'
op|':'
newline|'\n'
indent|'            '
name|'res_sub_type'
op|'='
name|'self'
op|'.'
name|'_HARD_DISK_RES_SUB_TYPE'
newline|'\n'
dedent|''
name|'elif'
name|'drive_type'
op|'=='
name|'constants'
op|'.'
name|'DVD'
op|':'
newline|'\n'
indent|'            '
name|'res_sub_type'
op|'='
name|'self'
op|'.'
name|'_DVD_DISK_RES_SUB_TYPE'
newline|'\n'
nl|'\n'
dedent|''
name|'res'
op|'='
name|'self'
op|'.'
name|'_get_new_resource_setting_data'
op|'('
nl|'\n'
name|'res_sub_type'
op|','
name|'self'
op|'.'
name|'_STORAGE_ALLOC_SETTING_DATA_CLASS'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'.'
name|'Parent'
op|'='
name|'drive_path'
newline|'\n'
name|'res'
op|'.'
name|'HostResource'
op|'='
op|'['
name|'path'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'res'
op|','
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume_to_controller
dedent|''
name|'def'
name|'attach_volume_to_controller'
op|'('
name|'self'
op|','
name|'vm_name'
op|','
name|'controller_path'
op|','
name|'address'
op|','
nl|'\n'
name|'mounted_disk_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach a volume to a controller."""'
newline|'\n'
nl|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm_check'
op|'('
name|'vm_name'
op|')'
newline|'\n'
nl|'\n'
name|'diskdrive'
op|'='
name|'self'
op|'.'
name|'_get_new_resource_setting_data'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_PHYS_DISK_RES_SUB_TYPE'
op|')'
newline|'\n'
nl|'\n'
name|'diskdrive'
op|'.'
name|'AddressOnParent'
op|'='
name|'address'
newline|'\n'
name|'diskdrive'
op|'.'
name|'Parent'
op|'='
name|'controller_path'
newline|'\n'
name|'diskdrive'
op|'.'
name|'HostResource'
op|'='
op|'['
name|'mounted_disk_path'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'diskdrive'
op|','
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_disk_resource_address
dedent|''
name|'def'
name|'_get_disk_resource_address'
op|'('
name|'self'
op|','
name|'disk_resource'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'disk_resource'
op|'.'
name|'AddressOnParent'
newline|'\n'
nl|'\n'
DECL|member|create_scsi_controller
dedent|''
name|'def'
name|'create_scsi_controller'
op|'('
name|'self'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an iscsi controller ready to mount volumes."""'
newline|'\n'
name|'scsicontrl'
op|'='
name|'self'
op|'.'
name|'_get_new_resource_setting_data'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_SCSI_RES_SUBTYPE'
op|')'
newline|'\n'
nl|'\n'
name|'scsicontrl'
op|'.'
name|'VirtualSystemIdentifiers'
op|'='
op|'['
string|"'{'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|'+'
string|"'}'"
op|']'
newline|'\n'
nl|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm_check'
op|'('
name|'vm_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'scsicontrl'
op|','
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_disk_resource_disk_path
dedent|''
name|'def'
name|'_get_disk_resource_disk_path'
op|'('
name|'self'
op|','
name|'disk_resource'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'disk_resource'
op|'.'
name|'HostResource'
newline|'\n'
nl|'\n'
DECL|member|destroy_vm
dedent|''
name|'def'
name|'destroy_vm'
op|'('
name|'self'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm_check'
op|'('
name|'vm_name'
op|')'
newline|'\n'
nl|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'# Remove the VM. It does not destroy any associated virtual disk.'
nl|'\n'
op|'('
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'DestroySystem'
op|'('
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_virt_resource
dedent|''
name|'def'
name|'_add_virt_resource'
op|'('
name|'self'
op|','
name|'res_setting_data'
op|','
name|'vm_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds a new resource to the VM."""'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'res_xml'
op|'='
op|'['
name|'res_setting_data'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|']'
newline|'\n'
op|'('
name|'job_path'
op|','
nl|'\n'
name|'new_resources'
op|','
nl|'\n'
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'AddResourceSettings'
op|'('
name|'vm_path'
op|','
name|'res_xml'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
name|'return'
name|'new_resources'
newline|'\n'
nl|'\n'
DECL|member|_modify_virt_resource
dedent|''
name|'def'
name|'_modify_virt_resource'
op|'('
name|'self'
op|','
name|'res_setting_data'
op|','
name|'vm_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates a VM resource."""'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
op|'('
name|'job_path'
op|','
nl|'\n'
name|'out_res_setting_data'
op|','
nl|'\n'
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'ModifyResourceSettings'
op|'('
nl|'\n'
name|'ResourceSettings'
op|'='
op|'['
name|'res_setting_data'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_remove_virt_resource
dedent|''
name|'def'
name|'_remove_virt_resource'
op|'('
name|'self'
op|','
name|'res_setting_data'
op|','
name|'vm_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a VM resource."""'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'res_path'
op|'='
op|'['
name|'res_setting_data'
op|'.'
name|'path_'
op|'('
op|')'
op|']'
newline|'\n'
op|'('
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'RemoveResourceSettings'
op|'('
name|'res_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vm_state
dedent|''
name|'def'
name|'get_vm_state'
op|'('
name|'self'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'settings'
op|'='
name|'self'
op|'.'
name|'get_vm_summary_info'
op|'('
name|'vm_name'
op|')'
newline|'\n'
name|'return'
name|'settings'
op|'['
string|"'EnabledState'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|take_vm_snapshot
dedent|''
name|'def'
name|'take_vm_snapshot'
op|'('
name|'self'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm_check'
op|'('
name|'vm_name'
op|')'
newline|'\n'
name|'vs_snap_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSnapshotService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
op|'('
name|'job_path'
op|','
name|'snp_setting_data'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_snap_svc'
op|'.'
name|'CreateSnapshot'
op|'('
nl|'\n'
name|'AffectedSystem'
op|'='
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|','
nl|'\n'
name|'SnapshotType'
op|'='
name|'self'
op|'.'
name|'_SNAPSHOT_FULL'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
name|'job_wmi_path'
op|'='
name|'job_path'
op|'.'
name|'replace'
op|'('
string|"'\\\\'"
op|','
string|"'/'"
op|')'
newline|'\n'
name|'job'
op|'='
name|'wmi'
op|'.'
name|'WMI'
op|'('
name|'moniker'
op|'='
name|'job_wmi_path'
op|')'
newline|'\n'
name|'snp_setting_data'
op|'='
name|'job'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
name|'self'
op|'.'
name|'_VIRTUAL_SYSTEM_SETTING_DATA_CLASS'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'snp_setting_data'
op|'.'
name|'path_'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_vm_snapshot
dedent|''
name|'def'
name|'remove_vm_snapshot'
op|'('
name|'self'
op|','
name|'snapshot_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vs_snap_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSnapshotService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
op|'('
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'vs_snap_svc'
op|'.'
name|'DestroySnapshot'
op|'('
name|'snapshot_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_nic_connection
dedent|''
name|'def'
name|'set_nic_connection'
op|'('
name|'self'
op|','
name|'vm_name'
op|','
name|'nic_name'
op|','
name|'vswitch_conn_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nic_data'
op|'='
name|'self'
op|'.'
name|'_get_nic_data_by_name'
op|'('
name|'nic_name'
op|')'
newline|'\n'
nl|'\n'
name|'eth_port_data'
op|'='
name|'self'
op|'.'
name|'_get_new_setting_data'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_ETHERNET_PORT_ALLOCATION_SETTING_DATA_CLASS'
op|')'
newline|'\n'
nl|'\n'
name|'eth_port_data'
op|'.'
name|'HostResource'
op|'='
op|'['
name|'vswitch_conn_data'
op|']'
newline|'\n'
name|'eth_port_data'
op|'.'
name|'Parent'
op|'='
name|'nic_data'
op|'.'
name|'path_'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm_check'
op|'('
name|'vm_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_virt_resource'
op|'('
name|'eth_port_data'
op|','
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|enable_vm_metrics_collection
dedent|''
name|'def'
name|'enable_vm_metrics_collection'
op|'('
name|'self'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metric_names'
op|'='
op|'['
name|'self'
op|'.'
name|'_METRIC_AGGR_CPU_AVG'
op|']'
newline|'\n'
nl|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm_check'
op|'('
name|'vm_name'
op|')'
newline|'\n'
name|'metric_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_MetricService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
op|'('
name|'disks'
op|','
name|'volumes'
op|')'
op|'='
name|'self'
op|'.'
name|'_get_vm_disks'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'filtered_disks'
op|'='
op|'['
name|'d'
name|'for'
name|'d'
name|'in'
name|'disks'
name|'if'
nl|'\n'
name|'d'
op|'.'
name|'ResourceSubType'
name|'is'
name|'not'
name|'self'
op|'.'
name|'_DVD_DISK_RES_SUB_TYPE'
op|']'
newline|'\n'
nl|'\n'
comment|'# enable metrics for disk.'
nl|'\n'
name|'for'
name|'disk'
name|'in'
name|'filtered_disks'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_enable_metrics'
op|'('
name|'metric_svc'
op|','
name|'disk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'metric_name'
name|'in'
name|'metric_names'
op|':'
newline|'\n'
indent|'            '
name|'metric_def'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'CIM_BaseMetricDefinition'
op|'('
name|'Name'
op|'='
name|'metric_name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'metric_def'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Metric not found: %s"'
op|','
name|'metric_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_enable_metrics'
op|'('
name|'metric_svc'
op|','
name|'vm'
op|','
name|'metric_def'
op|'['
number|'0'
op|']'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_enable_metrics
dedent|''
dedent|''
dedent|''
name|'def'
name|'_enable_metrics'
op|'('
name|'self'
op|','
name|'metric_svc'
op|','
name|'element'
op|','
name|'definition_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metric_svc'
op|'.'
name|'ControlMetrics'
op|'('
nl|'\n'
name|'Subject'
op|'='
name|'element'
op|'.'
name|'path_'
op|'('
op|')'
op|','
nl|'\n'
name|'Definition'
op|'='
name|'definition_path'
op|','
nl|'\n'
name|'MetricCollectionEnabled'
op|'='
name|'self'
op|'.'
name|'_METRIC_ENABLED'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
