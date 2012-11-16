begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Pedro Navarro Perez'
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
string|'"""\nManagement class for Storage-related functions (attach, detach, etc).\n"""'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
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
name|'hyperv'
name|'import'
name|'baseops'
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
name|'volumeutils'
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
DECL|variable|hyper_volumeops_opts
name|'hyper_volumeops_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'hyperv_attaching_volume_retry_count'"
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
string|"'The number of times we retry on attaching volume '"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'hyperv_wait_between_attach_retry'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The seconds to wait between an volume attachment attempt'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'hyper_volumeops_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeOps
name|'class'
name|'VolumeOps'
op|'('
name|'baseops'
op|'.'
name|'BaseOps'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VolumeOps'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'vmutils'
op|'.'
name|'VMUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_driver'
op|'='
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'_block_device'
op|'='
name|'block_device'
newline|'\n'
name|'self'
op|'.'
name|'_time'
op|'='
name|'time'
newline|'\n'
name|'self'
op|'.'
name|'_initiator'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_default_root_device'
op|'='
string|"'vda'"
newline|'\n'
name|'self'
op|'.'
name|'_attaching_volume_retry_count'
op|'='
name|'CONF'
op|'.'
name|'hyperv_attaching_volume_retry_count'
newline|'\n'
name|'self'
op|'.'
name|'_wait_between_attach_retry'
op|'='
name|'CONF'
op|'.'
name|'hyperv_wait_between_attach_retry'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'='
name|'volumeutils'
op|'.'
name|'VolumeUtils'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_boot_volume
dedent|''
name|'def'
name|'attach_boot_volume'
op|'('
name|'self'
op|','
name|'block_device_info'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach the boot volume to the IDE controller"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"block device info: %s"'
op|')'
op|','
name|'block_device_info'
op|')'
newline|'\n'
name|'ebs_root'
op|'='
name|'self'
op|'.'
name|'_driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'connection_info'
op|'='
name|'ebs_root'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'target_lun'
op|'='
name|'data'
op|'['
string|"'target_lun'"
op|']'
newline|'\n'
name|'target_iqn'
op|'='
name|'data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'target_portal'
op|'='
name|'data'
op|'['
string|"'target_portal'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'login_storage_target'
op|'('
name|'target_lun'
op|','
name|'target_iqn'
op|','
nl|'\n'
name|'target_portal'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'#Getting the mounted disk'
nl|'\n'
indent|'            '
name|'mounted_disk'
op|'='
name|'self'
op|'.'
name|'_get_mounted_disk_from_lun'
op|'('
name|'target_iqn'
op|','
nl|'\n'
name|'target_lun'
op|')'
newline|'\n'
comment|'#Attach to IDE controller'
nl|'\n'
comment|'#Find the IDE controller for the vm.'
nl|'\n'
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'MSVM_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'vm_name'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vmsettings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
newline|'\n'
name|'rasds'
op|'='
name|'vmsettings'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'MSVM_ResourceAllocationSettingData'"
op|')'
newline|'\n'
name|'ctrller'
op|'='
op|'['
name|'r'
name|'for'
name|'r'
name|'in'
name|'rasds'
nl|'\n'
name|'if'
name|'r'
op|'.'
name|'ResourceSubType'
op|'=='
string|"'Microsoft Emulated IDE Controller'"
nl|'\n'
name|'and'
name|'r'
op|'.'
name|'Address'
op|'=='
string|'"0"'
op|']'
newline|'\n'
comment|'#Attaching to the same slot as the VHD disk file'
nl|'\n'
name|'self'
op|'.'
name|'_attach_volume_to_controller'
op|'('
name|'ctrller'
op|','
number|'0'
op|','
name|'mounted_disk'
op|','
name|'vm'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exn'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Attach boot from volume failed: %s'"
op|')'
op|','
name|'exn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'logout_storage_target'
op|'('
name|'self'
op|'.'
name|'_conn_wmi'
op|','
name|'target_iqn'
op|')'
newline|'\n'
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Unable to attach boot volume to instance %s'"
op|')'
nl|'\n'
op|'%'
name|'vm_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|volume_in_mapping
dedent|''
dedent|''
name|'def'
name|'volume_in_mapping'
op|'('
name|'self'
op|','
name|'mount_device'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'volume_in_mapping'
op|'('
name|'mount_device'
op|','
nl|'\n'
name|'block_device_info'
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
string|'"""Attach a volume to the SCSI controller"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attach_volume: %(connection_info)s, %(instance_name)s,"'
nl|'\n'
string|'" %(mountpoint)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'target_lun'
op|'='
name|'data'
op|'['
string|"'target_lun'"
op|']'
newline|'\n'
name|'target_iqn'
op|'='
name|'data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'target_portal'
op|'='
name|'data'
op|'['
string|"'target_portal'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'login_storage_target'
op|'('
name|'target_lun'
op|','
name|'target_iqn'
op|','
nl|'\n'
name|'target_portal'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'#Getting the mounted disk'
nl|'\n'
indent|'            '
name|'mounted_disk'
op|'='
name|'self'
op|'.'
name|'_get_mounted_disk_from_lun'
op|'('
name|'target_iqn'
op|','
nl|'\n'
name|'target_lun'
op|')'
newline|'\n'
comment|'#Find the SCSI controller for the vm'
nl|'\n'
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'MSVM_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'instance_name'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vmsettings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
newline|'\n'
name|'rasds'
op|'='
name|'vmsettings'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'MSVM_ResourceAllocationSettingData'"
op|')'
newline|'\n'
name|'ctrller'
op|'='
op|'['
name|'r'
name|'for'
name|'r'
name|'in'
name|'rasds'
nl|'\n'
name|'if'
name|'r'
op|'.'
name|'ResourceSubType'
op|'=='
string|"'Microsoft Synthetic SCSI Controller'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_attach_volume_to_controller'
op|'('
nl|'\n'
name|'ctrller'
op|','
name|'self'
op|'.'
name|'_get_free_controller_slot'
op|'('
name|'ctrller'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
name|'mounted_disk'
op|','
name|'vm'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exn'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Attach volume failed: %s'"
op|')'
op|','
name|'exn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'logout_storage_target'
op|'('
name|'self'
op|'.'
name|'_conn_wmi'
op|','
name|'target_iqn'
op|')'
newline|'\n'
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Unable to attach volume to instance %s'"
op|')'
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume_to_controller
dedent|''
dedent|''
name|'def'
name|'_attach_volume_to_controller'
op|'('
name|'self'
op|','
name|'controller'
op|','
name|'address'
op|','
name|'mounted_disk'
op|','
nl|'\n'
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach a volume to a controller """'
newline|'\n'
comment|'#Find the default disk drive object for the vm and clone it.'
nl|'\n'
name|'diskdflt'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM Msvm_ResourceAllocationSettingData \\\n                WHERE ResourceSubType LIKE \'Microsoft Physical Disk Drive\'\\\n                AND InstanceID LIKE \'%Default%\'"'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'diskdrive'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'clone_wmi_obj'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
nl|'\n'
string|"'Msvm_ResourceAllocationSettingData'"
op|','
name|'diskdflt'
op|')'
newline|'\n'
name|'diskdrive'
op|'.'
name|'Address'
op|'='
name|'address'
newline|'\n'
name|'diskdrive'
op|'.'
name|'Parent'
op|'='
name|'controller'
op|'['
number|'0'
op|']'
op|'.'
name|'path_'
op|'('
op|')'
newline|'\n'
name|'diskdrive'
op|'.'
name|'HostResource'
op|'='
op|'['
name|'mounted_disk'
op|'['
number|'0'
op|']'
op|'.'
name|'path_'
op|'('
op|')'
op|']'
newline|'\n'
name|'new_resources'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'add_virt_resource'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
name|'diskdrive'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'new_resources'
name|'is'
name|'None'
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
string|"'Failed to add volume to VM %s'"
op|')'
op|'%'
nl|'\n'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_free_controller_slot
dedent|''
dedent|''
name|'def'
name|'_get_free_controller_slot'
op|'('
name|'self'
op|','
name|'scsi_controller'
op|')'
op|':'
newline|'\n'
comment|'#Getting volumes mounted in the SCSI controller'
nl|'\n'
indent|'        '
name|'volumes'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM Msvm_ResourceAllocationSettingData \\\n                WHERE ResourceSubType LIKE \'Microsoft Physical Disk Drive\'\\\n                AND Parent = \'"'
op|'+'
name|'scsi_controller'
op|'.'
name|'path_'
op|'('
op|')'
op|'+'
string|'"\'"'
op|')'
newline|'\n'
comment|'#Slots starts from 0, so the lenght of the disks gives us the free slot'
nl|'\n'
name|'return'
name|'len'
op|'('
name|'volumes'
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
string|'"""Dettach a volume to the SCSI controller"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Detach_volume: %(connection_info)s, %(instance_name)s,"'
nl|'\n'
string|'" %(mountpoint)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'target_lun'
op|'='
name|'data'
op|'['
string|"'target_lun'"
op|']'
newline|'\n'
name|'target_iqn'
op|'='
name|'data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
comment|'#Getting the mounted disk'
nl|'\n'
name|'mounted_disk'
op|'='
name|'self'
op|'.'
name|'_get_mounted_disk_from_lun'
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|')'
newline|'\n'
name|'physical_list'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM Msvm_ResourceAllocationSettingData \\\n                WHERE ResourceSubType LIKE \'Microsoft Physical Disk Drive\'"'
op|')'
newline|'\n'
name|'physical_disk'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'phydisk'
name|'in'
name|'physical_list'
op|':'
newline|'\n'
indent|'            '
name|'host_resource_list'
op|'='
name|'phydisk'
op|'.'
name|'HostResource'
newline|'\n'
name|'if'
name|'host_resource_list'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'host_resource'
op|'='
name|'str'
op|'('
name|'host_resource_list'
op|'['
number|'0'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
newline|'\n'
name|'mounted_disk_path'
op|'='
name|'str'
op|'('
name|'mounted_disk'
op|'['
number|'0'
op|']'
op|'.'
name|'path_'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Mounted disk to detach is: %s"'
op|')'
op|','
name|'mounted_disk_path'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"host_resource disk detached is: %s"'
op|')'
op|','
name|'host_resource'
op|')'
newline|'\n'
name|'if'
name|'host_resource'
op|'=='
name|'mounted_disk_path'
op|':'
newline|'\n'
indent|'                '
name|'physical_disk'
op|'='
name|'phydisk'
newline|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Physical disk detached is: %s"'
op|')'
op|','
name|'physical_disk'
op|')'
newline|'\n'
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'MSVM_ComputerSystem'
op|'('
name|'ElementName'
op|'='
name|'instance_name'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
name|'remove_result'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'remove_virt_resource'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
nl|'\n'
name|'physical_disk'
op|','
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'remove_result'
name|'is'
name|'False'
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
string|"'Failed to remove volume from VM %s'"
op|')'
op|'%'
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
comment|'#Sending logout'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'logout_storage_target'
op|'('
name|'self'
op|'.'
name|'_conn_wmi'
op|','
name|'target_iqn'
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
name|'if'
name|'not'
name|'self'
op|'.'
name|'_initiator'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_initiator'
op|'='
name|'self'
op|'.'
name|'_get_iscsi_initiator'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_initiator'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Could not determine iscsi initiator name'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
nl|'\n'
string|"'ip'"
op|':'
name|'CONF'
op|'.'
name|'my_ip'
op|','
nl|'\n'
string|"'initiator'"
op|':'
name|'self'
op|'.'
name|'_initiator'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_iscsi_initiator
dedent|''
name|'def'
name|'_get_iscsi_initiator'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_iscsi_initiator'
op|'('
name|'self'
op|'.'
name|'_conn_cimv2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_mounted_disk_from_lun
dedent|''
name|'def'
name|'_get_mounted_disk_from_lun'
op|'('
name|'self'
op|','
name|'target_iqn'
op|','
name|'target_lun'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'initiator_session'
op|'='
name|'self'
op|'.'
name|'_conn_wmi'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM MSiSCSIInitiator_SessionClass \\\n                WHERE TargetName=\'"'
op|'+'
name|'target_iqn'
op|'+'
string|'"\'"'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'devices'
op|'='
name|'initiator_session'
op|'.'
name|'Devices'
newline|'\n'
name|'device_number'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'device'
name|'in'
name|'devices'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.InitiatorName: %s"'
op|')'
op|','
name|'device'
op|'.'
name|'InitiatorName'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.TargetName: %s"'
op|')'
op|','
name|'device'
op|'.'
name|'TargetName'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.ScsiPortNumber: %s"'
op|')'
op|','
name|'device'
op|'.'
name|'ScsiPortNumber'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.ScsiPathId: %s"'
op|')'
op|','
name|'device'
op|'.'
name|'ScsiPathId'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.ScsiTargetId): %s"'
op|')'
op|','
name|'device'
op|'.'
name|'ScsiTargetId'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.ScsiLun: %s"'
op|')'
op|','
name|'device'
op|'.'
name|'ScsiLun'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.DeviceInterfaceGuid :%s"'
op|')'
op|','
nl|'\n'
name|'device'
op|'.'
name|'DeviceInterfaceGuid'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.DeviceInterfaceName: %s"'
op|')'
op|','
nl|'\n'
name|'device'
op|'.'
name|'DeviceInterfaceName'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.LegacyName: %s"'
op|')'
op|','
name|'device'
op|'.'
name|'LegacyName'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.DeviceType: %s"'
op|')'
op|','
name|'device'
op|'.'
name|'DeviceType'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.DeviceNumber %s"'
op|')'
op|','
name|'device'
op|'.'
name|'DeviceNumber'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"device.PartitionNumber :%s"'
op|')'
op|','
name|'device'
op|'.'
name|'PartitionNumber'
op|')'
newline|'\n'
name|'scsi_lun'
op|'='
name|'device'
op|'.'
name|'ScsiLun'
newline|'\n'
name|'if'
name|'scsi_lun'
op|'=='
name|'target_lun'
op|':'
newline|'\n'
indent|'                '
name|'device_number'
op|'='
name|'device'
op|'.'
name|'DeviceNumber'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'device_number'
name|'is'
name|'None'
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
string|"'Unable to find a mounted disk for'"
nl|'\n'
string|"' target_iqn: %s'"
op|')'
op|'%'
name|'target_iqn'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Device number : %s"'
op|')'
op|','
name|'device_number'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Target lun : %s"'
op|')'
op|','
name|'target_lun'
op|')'
newline|'\n'
comment|'#Finding Mounted disk drive'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'_attaching_volume_retry_count'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mounted_disk'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM Msvm_DiskDrive WHERE DriveNumber="'
op|'+'
nl|'\n'
name|'str'
op|'('
name|'device_number'
op|')'
op|'+'
string|'""'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Mounted disk is: %s"'
op|')'
op|','
name|'mounted_disk'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'mounted_disk'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_time'
op|'.'
name|'sleep'
op|'('
name|'self'
op|'.'
name|'_wait_between_attach_retry'
op|')'
newline|'\n'
dedent|''
name|'mounted_disk'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM Msvm_DiskDrive WHERE DriveNumber="'
op|'+'
nl|'\n'
name|'str'
op|'('
name|'device_number'
op|')'
op|'+'
string|'""'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Mounted disk is: %s"'
op|')'
op|','
name|'mounted_disk'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'mounted_disk'
op|')'
op|'=='
number|'0'
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
string|"'Unable to find a mounted disk for'"
nl|'\n'
string|"' target_iqn: %s'"
op|')'
op|'%'
name|'target_iqn'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'mounted_disk'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volume
dedent|''
name|'def'
name|'disconnect_volume'
op|'('
name|'self'
op|','
name|'physical_drive_path'
op|')'
op|':'
newline|'\n'
comment|'#Get the session_id of the ISCSI connection'
nl|'\n'
indent|'        '
name|'session_id'
op|'='
name|'self'
op|'.'
name|'_get_session_id_from_mounted_disk'
op|'('
nl|'\n'
name|'physical_drive_path'
op|')'
newline|'\n'
comment|'#Logging out the target'
nl|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute_log_out'
op|'('
name|'session_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_session_id_from_mounted_disk
dedent|''
name|'def'
name|'_get_session_id_from_mounted_disk'
op|'('
name|'self'
op|','
name|'physical_drive_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'drive_number'
op|'='
name|'self'
op|'.'
name|'_get_drive_number_from_disk_path'
op|'('
nl|'\n'
name|'physical_drive_path'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Drive number to disconnect is: %s"'
op|')'
op|','
name|'drive_number'
op|')'
newline|'\n'
name|'initiator_sessions'
op|'='
name|'self'
op|'.'
name|'_conn_wmi'
op|'.'
name|'query'
op|'('
nl|'\n'
string|'"SELECT * FROM MSiSCSIInitiator_SessionClass"'
op|')'
newline|'\n'
name|'for'
name|'initiator_session'
name|'in'
name|'initiator_sessions'
op|':'
newline|'\n'
indent|'            '
name|'devices'
op|'='
name|'initiator_session'
op|'.'
name|'Devices'
newline|'\n'
name|'for'
name|'device'
name|'in'
name|'devices'
op|':'
newline|'\n'
indent|'                '
name|'deviceNumber'
op|'='
name|'str'
op|'('
name|'device'
op|'.'
name|'DeviceNumber'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"DeviceNumber : %s"'
op|')'
op|','
name|'deviceNumber'
op|')'
newline|'\n'
name|'if'
name|'deviceNumber'
op|'=='
name|'drive_number'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'initiator_session'
op|'.'
name|'SessionId'
newline|'\n'
nl|'\n'
DECL|member|_get_drive_number_from_disk_path
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_drive_number_from_disk_path'
op|'('
name|'self'
op|','
name|'disk_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Disk path to parse: %s"'
op|')'
op|','
name|'disk_path'
op|')'
newline|'\n'
name|'start_device_id'
op|'='
name|'disk_path'
op|'.'
name|'find'
op|'('
string|'\'"\''
op|','
name|'disk_path'
op|'.'
name|'find'
op|'('
string|"'DeviceID'"
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"start_device_id: %s"'
op|')'
op|','
name|'start_device_id'
op|')'
newline|'\n'
name|'end_device_id'
op|'='
name|'disk_path'
op|'.'
name|'find'
op|'('
string|'\'"\''
op|','
name|'start_device_id'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"end_device_id: %s"'
op|')'
op|','
name|'end_device_id'
op|')'
newline|'\n'
name|'deviceID'
op|'='
name|'disk_path'
op|'['
name|'start_device_id'
op|'+'
number|'1'
op|':'
name|'end_device_id'
op|']'
newline|'\n'
name|'return'
name|'deviceID'
op|'['
name|'deviceID'
op|'.'
name|'find'
op|'('
string|'"\\\\"'
op|')'
op|'+'
number|'2'
op|':'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_default_root_device
dedent|''
name|'def'
name|'get_default_root_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_default_root_device'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
