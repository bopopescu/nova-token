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
nl|'\n'
name|'import'
name|'sys'
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'i18n'
name|'import'
name|'_'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutilsv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'volumeutilsv2'
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
DECL|class|LiveMigrationUtils
name|'class'
name|'LiveMigrationUtils'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'='
name|'volumeutilsv2'
op|'.'
name|'VolumeUtilsV2'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_conn_v2
dedent|''
name|'def'
name|'_get_conn_v2'
op|'('
name|'self'
op|','
name|'host'
op|'='
string|"'localhost'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
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
dedent|''
name|'except'
name|'wmi'
op|'.'
name|'x_wmi'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'if'
name|'ex'
op|'.'
name|'com_error'
op|'.'
name|'hresult'
op|'=='
op|'-'
number|'2147217394'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'\'Live migration is not supported on target host "%s"\''
op|')'
nl|'\n'
op|'%'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'ex'
op|'.'
name|'com_error'
op|'.'
name|'hresult'
op|'=='
op|'-'
number|'2147023174'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'\'Target live migration host "%s" is unreachable\''
op|')'
nl|'\n'
op|'%'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Live migration failed: %s'"
op|')'
op|'%'
name|'ex'
op|'.'
name|'message'
newline|'\n'
dedent|''
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_live_migration_config
dedent|''
dedent|''
name|'def'
name|'check_live_migration_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conn_v2'
op|'='
name|'self'
op|'.'
name|'_get_conn_v2'
op|'('
op|')'
newline|'\n'
name|'migration_svc'
op|'='
name|'conn_v2'
op|'.'
name|'Msvm_VirtualSystemMigrationService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vsmssds'
op|'='
name|'migration_svc'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_ElementSettingData'"
op|','
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemMigrationServiceSettingData'"
op|')'
newline|'\n'
name|'vsmssd'
op|'='
name|'vsmssds'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'vsmssd'
op|'.'
name|'EnableVirtualSystemMigration'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Live migration is not enabled on this host'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'migration_svc'
op|'.'
name|'MigrationServiceListenerIPAddressList'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Live migration networks are not configured on this host'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vm
dedent|''
dedent|''
name|'def'
name|'_get_vm'
op|'('
name|'self'
op|','
name|'conn_v2'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vms'
op|'='
name|'conn_v2'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'vm_name'
op|')'
newline|'\n'
name|'n'
op|'='
name|'len'
op|'('
name|'vms'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'n'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'VM not found: %s'"
op|')'
op|'%'
name|'vm_name'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'n'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|"'Duplicate VM name found: %s'"
op|')'
nl|'\n'
op|'%'
name|'vm_name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_destroy_planned_vm
dedent|''
name|'def'
name|'_destroy_planned_vm'
op|'('
name|'self'
op|','
name|'conn_v2_remote'
op|','
name|'planned_vm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Destroying existing remote planned VM: %s"'
op|','
nl|'\n'
name|'planned_vm'
op|'.'
name|'ElementName'
op|')'
newline|'\n'
name|'vs_man_svc'
op|'='
name|'conn_v2_remote'
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
name|'ret_val'
op|')'
op|'='
name|'vs_man_svc'
op|'.'
name|'DestroySystem'
op|'('
name|'planned_vm'
op|'.'
name|'path_'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_existing_planned_vm
dedent|''
name|'def'
name|'_check_existing_planned_vm'
op|'('
name|'self'
op|','
name|'conn_v2_remote'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
comment|"# Make sure that there's not yet a remote planned VM on the target"
nl|'\n'
comment|'# host for this VM'
nl|'\n'
indent|'        '
name|'planned_vms'
op|'='
name|'conn_v2_remote'
op|'.'
name|'Msvm_PlannedComputerSystem'
op|'('
name|'Name'
op|'='
name|'vm'
op|'.'
name|'Name'
op|')'
newline|'\n'
name|'if'
name|'planned_vms'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_destroy_planned_vm'
op|'('
name|'conn_v2_remote'
op|','
name|'planned_vms'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_remote_planned_vm
dedent|''
dedent|''
name|'def'
name|'_create_remote_planned_vm'
op|'('
name|'self'
op|','
name|'conn_v2_local'
op|','
name|'conn_v2_remote'
op|','
nl|'\n'
name|'vm'
op|','
name|'rmt_ip_addr_list'
op|','
name|'dest_host'
op|')'
op|':'
newline|'\n'
comment|'# Staged'
nl|'\n'
indent|'        '
name|'vsmsd'
op|'='
name|'conn_v2_local'
op|'.'
name|'query'
op|'('
string|'"select * from "'
nl|'\n'
string|'"Msvm_VirtualSystemMigrationSettingData "'
nl|'\n'
string|'"where MigrationType = 32770"'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vsmsd'
op|'.'
name|'DestinationIPAddressList'
op|'='
name|'rmt_ip_addr_list'
newline|'\n'
name|'migration_setting_data'
op|'='
name|'vsmsd'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating remote planned VM for VM: %s"'
op|','
nl|'\n'
name|'vm'
op|'.'
name|'ElementName'
op|')'
newline|'\n'
name|'migr_svc'
op|'='
name|'conn_v2_local'
op|'.'
name|'Msvm_VirtualSystemMigrationService'
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
name|'migr_svc'
op|'.'
name|'MigrateVirtualSystemToHost'
op|'('
nl|'\n'
name|'ComputerSystem'
op|'='
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|','
nl|'\n'
name|'DestinationHost'
op|'='
name|'dest_host'
op|','
nl|'\n'
name|'MigrationSettingData'
op|'='
name|'migration_setting_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'conn_v2_remote'
op|'.'
name|'Msvm_PlannedComputerSystem'
op|'('
name|'Name'
op|'='
name|'vm'
op|'.'
name|'Name'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_physical_disk_paths
dedent|''
name|'def'
name|'_get_physical_disk_paths'
op|'('
name|'self'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ide_ctrl_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_ide_controller'
op|'('
name|'vm_name'
op|','
number|'0'
op|')'
newline|'\n'
name|'if'
name|'ide_ctrl_path'
op|':'
newline|'\n'
indent|'            '
name|'ide_paths'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_controller_volume_paths'
op|'('
nl|'\n'
name|'ide_ctrl_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'ide_paths'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'scsi_ctrl_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_scsi_controller'
op|'('
name|'vm_name'
op|')'
newline|'\n'
name|'scsi_paths'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_controller_volume_paths'
op|'('
name|'scsi_ctrl_path'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'dict'
op|'('
name|'ide_paths'
op|'.'
name|'items'
op|'('
op|')'
op|'+'
name|'scsi_paths'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_remote_disk_data
dedent|''
name|'def'
name|'_get_remote_disk_data'
op|'('
name|'self'
op|','
name|'vmutils_remote'
op|','
name|'disk_paths'
op|','
name|'dest_host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volutils_remote'
op|'='
name|'volumeutilsv2'
op|'.'
name|'VolumeUtilsV2'
op|'('
name|'dest_host'
op|')'
newline|'\n'
nl|'\n'
name|'disk_paths_remote'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
op|'('
name|'rasd_rel_path'
op|','
name|'disk_path'
op|')'
name|'in'
name|'disk_paths'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'target'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_target_from_disk_path'
op|'('
name|'disk_path'
op|')'
newline|'\n'
name|'if'
name|'target'
op|':'
newline|'\n'
indent|'                '
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|')'
op|'='
name|'target'
newline|'\n'
nl|'\n'
name|'dev_num'
op|'='
name|'volutils_remote'
op|'.'
name|'get_device_number_for_target'
op|'('
nl|'\n'
name|'target_iqn'
op|','
name|'target_lun'
op|')'
newline|'\n'
name|'disk_path_remote'
op|'='
op|'('
nl|'\n'
name|'vmutils_remote'
op|'.'
name|'get_mounted_disk_by_drive_number'
op|'('
name|'dev_num'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'disk_paths_remote'
op|'['
name|'rasd_rel_path'
op|']'
op|'='
name|'disk_path_remote'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Could not retrieve iSCSI target "'
nl|'\n'
string|'"from disk path: %s"'
op|','
name|'disk_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'disk_paths_remote'
newline|'\n'
nl|'\n'
DECL|member|_update_planned_vm_disk_resources
dedent|''
name|'def'
name|'_update_planned_vm_disk_resources'
op|'('
name|'self'
op|','
name|'vmutils_remote'
op|','
name|'conn_v2_remote'
op|','
nl|'\n'
name|'planned_vm'
op|','
name|'vm_name'
op|','
nl|'\n'
name|'disk_paths_remote'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_settings'
op|'='
name|'planned_vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_SettingsDefineState'"
op|','
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'updated_resource_setting_data'
op|'='
op|'['
op|']'
newline|'\n'
name|'sasds'
op|'='
name|'vm_settings'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_VirtualSystemSettingDataComponent'"
op|')'
newline|'\n'
name|'for'
name|'sasd'
name|'in'
name|'sasds'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'sasd'
op|'.'
name|'ResourceType'
op|'=='
number|'17'
name|'and'
name|'sasd'
op|'.'
name|'ResourceSubType'
op|'=='
nl|'\n'
string|'"Microsoft:Hyper-V:Physical Disk Drive"'
name|'and'
nl|'\n'
name|'sasd'
op|'.'
name|'HostResource'
op|')'
op|':'
newline|'\n'
comment|'# Replace the local disk target with the correct remote one'
nl|'\n'
indent|'                '
name|'old_disk_path'
op|'='
name|'sasd'
op|'.'
name|'HostResource'
op|'['
number|'0'
op|']'
newline|'\n'
name|'new_disk_path'
op|'='
name|'disk_paths_remote'
op|'.'
name|'pop'
op|'('
name|'sasd'
op|'.'
name|'path'
op|'('
op|')'
op|'.'
name|'RelPath'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Replacing host resource "'
nl|'\n'
string|'"%(old_disk_path)s with "'
nl|'\n'
string|'"%(new_disk_path)s on planned VM %(vm_name)s"'
op|','
nl|'\n'
op|'{'
string|"'old_disk_path'"
op|':'
name|'old_disk_path'
op|','
nl|'\n'
string|"'new_disk_path'"
op|':'
name|'new_disk_path'
op|','
nl|'\n'
string|"'vm_name'"
op|':'
name|'vm_name'
op|'}'
op|')'
newline|'\n'
name|'sasd'
op|'.'
name|'HostResource'
op|'='
op|'['
name|'new_disk_path'
op|']'
newline|'\n'
name|'updated_resource_setting_data'
op|'.'
name|'append'
op|'('
name|'sasd'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Updating remote planned VM disk paths for VM: %s"'
op|','
nl|'\n'
name|'vm_name'
op|')'
newline|'\n'
name|'vsmsvc'
op|'='
name|'conn_v2_remote'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
op|'('
name|'res_settings'
op|','
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'vsmsvc'
op|'.'
name|'ModifyResourceSettings'
op|'('
nl|'\n'
name|'ResourceSettings'
op|'='
name|'updated_resource_setting_data'
op|')'
newline|'\n'
name|'vmutils_remote'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vhd_setting_data
dedent|''
name|'def'
name|'_get_vhd_setting_data'
op|'('
name|'self'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_settings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_SettingsDefineState'"
op|','
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'new_resource_setting_data'
op|'='
op|'['
op|']'
newline|'\n'
name|'sasds'
op|'='
name|'vm_settings'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_VirtualSystemSettingDataComponent'"
op|','
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_StorageAllocationSettingData'"
op|')'
newline|'\n'
name|'for'
name|'sasd'
name|'in'
name|'sasds'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'sasd'
op|'.'
name|'ResourceType'
op|'=='
number|'31'
name|'and'
name|'sasd'
op|'.'
name|'ResourceSubType'
op|'=='
nl|'\n'
string|'"Microsoft:Hyper-V:Virtual Hard Disk"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'new_resource_setting_data'
op|'.'
name|'append'
op|'('
name|'sasd'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'new_resource_setting_data'
newline|'\n'
nl|'\n'
DECL|member|_live_migrate_vm
dedent|''
name|'def'
name|'_live_migrate_vm'
op|'('
name|'self'
op|','
name|'conn_v2_local'
op|','
name|'vm'
op|','
name|'planned_vm'
op|','
name|'rmt_ip_addr_list'
op|','
nl|'\n'
name|'new_resource_setting_data'
op|','
name|'dest_host'
op|')'
op|':'
newline|'\n'
comment|'# VirtualSystemAndStorage'
nl|'\n'
indent|'        '
name|'vsmsd'
op|'='
name|'conn_v2_local'
op|'.'
name|'query'
op|'('
string|'"select * from "'
nl|'\n'
string|'"Msvm_VirtualSystemMigrationSettingData "'
nl|'\n'
string|'"where MigrationType = 32771"'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vsmsd'
op|'.'
name|'DestinationIPAddressList'
op|'='
name|'rmt_ip_addr_list'
newline|'\n'
name|'if'
name|'planned_vm'
op|':'
newline|'\n'
indent|'            '
name|'vsmsd'
op|'.'
name|'DestinationPlannedVirtualSystemId'
op|'='
name|'planned_vm'
op|'.'
name|'Name'
newline|'\n'
dedent|''
name|'migration_setting_data'
op|'='
name|'vsmsd'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'migr_svc'
op|'='
name|'conn_v2_local'
op|'.'
name|'Msvm_VirtualSystemMigrationService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Starting live migration for VM: %s"'
op|','
name|'vm'
op|'.'
name|'ElementName'
op|')'
newline|'\n'
op|'('
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'migr_svc'
op|'.'
name|'MigrateVirtualSystemToHost'
op|'('
nl|'\n'
name|'ComputerSystem'
op|'='
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|','
nl|'\n'
name|'DestinationHost'
op|'='
name|'dest_host'
op|','
nl|'\n'
name|'MigrationSettingData'
op|'='
name|'migration_setting_data'
op|','
nl|'\n'
name|'NewResourceSettingData'
op|'='
name|'new_resource_setting_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_ret_val'
op|'('
name|'ret_val'
op|','
name|'job_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_remote_ip_address_list
dedent|''
name|'def'
name|'_get_remote_ip_address_list'
op|'('
name|'self'
op|','
name|'conn_v2_remote'
op|','
name|'dest_host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Getting live migration networks for remote host: %s"'
op|','
nl|'\n'
name|'dest_host'
op|')'
newline|'\n'
name|'migr_svc_rmt'
op|'='
name|'conn_v2_remote'
op|'.'
name|'Msvm_VirtualSystemMigrationService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'migr_svc_rmt'
op|'.'
name|'MigrationServiceListenerIPAddressList'
newline|'\n'
nl|'\n'
DECL|member|live_migrate_vm
dedent|''
name|'def'
name|'live_migrate_vm'
op|'('
name|'self'
op|','
name|'vm_name'
op|','
name|'dest_host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'check_live_migration_config'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'conn_v2_local'
op|'='
name|'self'
op|'.'
name|'_get_conn_v2'
op|'('
op|')'
newline|'\n'
name|'conn_v2_remote'
op|'='
name|'self'
op|'.'
name|'_get_conn_v2'
op|'('
name|'dest_host'
op|')'
newline|'\n'
nl|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm'
op|'('
name|'conn_v2_local'
op|','
name|'vm_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_existing_planned_vm'
op|'('
name|'conn_v2_remote'
op|','
name|'vm'
op|')'
newline|'\n'
nl|'\n'
name|'rmt_ip_addr_list'
op|'='
name|'self'
op|'.'
name|'_get_remote_ip_address_list'
op|'('
name|'conn_v2_remote'
op|','
nl|'\n'
name|'dest_host'
op|')'
newline|'\n'
nl|'\n'
name|'planned_vm'
op|'='
name|'None'
newline|'\n'
name|'disk_paths'
op|'='
name|'self'
op|'.'
name|'_get_physical_disk_paths'
op|'('
name|'vm_name'
op|')'
newline|'\n'
name|'if'
name|'disk_paths'
op|':'
newline|'\n'
indent|'            '
name|'vmutils_remote'
op|'='
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|'('
name|'dest_host'
op|')'
newline|'\n'
name|'disk_paths_remote'
op|'='
name|'self'
op|'.'
name|'_get_remote_disk_data'
op|'('
name|'vmutils_remote'
op|','
nl|'\n'
name|'disk_paths'
op|','
nl|'\n'
name|'dest_host'
op|')'
newline|'\n'
nl|'\n'
name|'planned_vm'
op|'='
name|'self'
op|'.'
name|'_create_remote_planned_vm'
op|'('
name|'conn_v2_local'
op|','
nl|'\n'
name|'conn_v2_remote'
op|','
nl|'\n'
name|'vm'
op|','
name|'rmt_ip_addr_list'
op|','
nl|'\n'
name|'dest_host'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_update_planned_vm_disk_resources'
op|'('
name|'vmutils_remote'
op|','
nl|'\n'
name|'conn_v2_remote'
op|','
name|'planned_vm'
op|','
nl|'\n'
name|'vm_name'
op|','
name|'disk_paths_remote'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'new_resource_setting_data'
op|'='
name|'self'
op|'.'
name|'_get_vhd_setting_data'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_live_migrate_vm'
op|'('
name|'conn_v2_local'
op|','
name|'vm'
op|','
name|'planned_vm'
op|','
name|'rmt_ip_addr_list'
op|','
nl|'\n'
name|'new_resource_setting_data'
op|','
name|'dest_host'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
