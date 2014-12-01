begin_unit
comment|'# Copyright 2012 Pedro Navarro Perez'
nl|'\n'
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
string|'"""\nManagement class for Storage-related functions (attach, detach, etc).\n"""'
newline|'\n'
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'excutils'
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
op|','
name|'_LE'
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
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'utilsfactory'
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
string|"'volume_attach_retry_count'"
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
string|"'The number of times to retry to attach a volume'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'volume_attach_retry_interval'"
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
string|"'Interval between volume attachment attempts, in seconds'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'mounted_disk_query_retry_count'"
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
string|"'The number of times to retry checking for a disk mounted '"
nl|'\n'
string|"'via iSCSI.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'mounted_disk_query_retry_interval'"
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
string|"'Interval between checks for a mounted iSCSI '"
nl|'\n'
string|"'disk, in seconds.'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'hyper_volumeops_opts'
op|','
string|"'hyperv'"
op|')'
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
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'my_ip'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeOps
name|'class'
name|'VolumeOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Management class for Volume-related tasks\n    """'
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
name|'_hostutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_hostutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_volumeutils'
op|'('
op|')'
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
nl|'\n'
DECL|member|ebs_root_in_block_devices
dedent|''
name|'def'
name|'ebs_root_in_block_devices'
op|'('
name|'self'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'block_device_info'
op|':'
newline|'\n'
indent|'            '
name|'root_device'
op|'='
name|'block_device_info'
op|'.'
name|'get'
op|'('
string|"'root_device_name'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'root_device'
op|':'
newline|'\n'
indent|'                '
name|'root_device'
op|'='
name|'self'
op|'.'
name|'_default_root_device'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'volume_in_mapping'
op|'('
name|'root_device'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volumes
dedent|''
dedent|''
name|'def'
name|'attach_volumes'
op|'('
name|'self'
op|','
name|'block_device_info'
op|','
name|'instance_name'
op|','
name|'ebs_root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'ebs_root'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'attach_volume'
op|'('
name|'mapping'
op|'['
number|'0'
op|']'
op|'['
string|"'connection_info'"
op|']'
op|','
nl|'\n'
name|'instance_name'
op|','
name|'True'
op|')'
newline|'\n'
name|'mapping'
op|'='
name|'mapping'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'for'
name|'vol'
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'attach_volume'
op|'('
name|'vol'
op|'['
string|"'connection_info'"
op|']'
op|','
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|login_storage_targets
dedent|''
dedent|''
name|'def'
name|'login_storage_targets'
op|'('
name|'self'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_login_storage_target'
op|'('
name|'vol'
op|'['
string|"'connection_info'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_login_storage_target
dedent|''
dedent|''
name|'def'
name|'_login_storage_target'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'auth_method'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'auth_method'"
op|')'
newline|'\n'
name|'auth_username'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'auth_username'"
op|')'
newline|'\n'
name|'auth_password'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'auth_password'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'auth_method'
name|'and'
name|'auth_method'
op|'.'
name|'upper'
op|'('
op|')'
op|'!='
string|"'CHAP'"
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
string|'"Cannot log in target %(target_iqn)s. Unsupported iSCSI "'
nl|'\n'
string|'"authentication method: %(auth_method)s."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
nl|'\n'
string|"'auth_method'"
op|':'
name|'auth_method'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if we already logged in'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_device_number_for_target'
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Already logged in on storage target. No need to "'
nl|'\n'
string|'"login. Portal: %(target_portal)s, "'
nl|'\n'
string|'"IQN: %(target_iqn)s, LUN: %(target_lun)s"'
op|','
nl|'\n'
op|'{'
string|"'target_portal'"
op|':'
name|'target_portal'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
string|"'target_lun'"
op|':'
name|'target_lun'
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
string|'"Logging in on storage target. Portal: "'
nl|'\n'
string|'"%(target_portal)s, IQN: %(target_iqn)s, "'
nl|'\n'
string|'"LUN: %(target_lun)s"'
op|','
nl|'\n'
op|'{'
string|"'target_portal'"
op|':'
name|'target_portal'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
string|"'target_lun'"
op|':'
name|'target_lun'
op|'}'
op|')'
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
op|','
name|'auth_username'
op|','
nl|'\n'
name|'auth_password'
op|')'
newline|'\n'
comment|'# Wait for the target to be mounted'
nl|'\n'
name|'self'
op|'.'
name|'_get_mounted_disk_from_lun'
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|','
name|'True'
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
name|'ebs_root'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach a volume to the SCSI controller or to the IDE controller if\n        ebs_root is True\n        """'
newline|'\n'
name|'target_iqn'
op|'='
name|'None'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Attach_volume: %(connection_info)s to %(instance_name)s"'
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
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_login_storage_target'
op|'('
name|'connection_info'
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
nl|'\n'
comment|'# Getting the mounted disk'
nl|'\n'
name|'mounted_disk_path'
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
nl|'\n'
name|'if'
name|'ebs_root'
op|':'
newline|'\n'
comment|'# Find the IDE controller for the vm.'
nl|'\n'
indent|'                '
name|'ctrller_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_ide_controller'
op|'('
nl|'\n'
name|'instance_name'
op|','
number|'0'
op|')'
newline|'\n'
comment|'# Attaching to the first slot'
nl|'\n'
name|'slot'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Find the SCSI controller for the vm'
nl|'\n'
indent|'                '
name|'ctrller_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_scsi_controller'
op|'('
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'slot'
op|'='
name|'self'
op|'.'
name|'_get_free_controller_slot'
op|'('
name|'ctrller_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'attach_volume_to_controller'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'ctrller_path'
op|','
nl|'\n'
name|'slot'
op|','
nl|'\n'
name|'mounted_disk_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'Unable to attach volume to instance %s'"
op|')'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'target_iqn'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_free_controller_slot
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_free_controller_slot'
op|'('
name|'self'
op|','
name|'scsi_controller_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attached_disks'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_attached_disks'
op|'('
name|'scsi_controller_path'
op|')'
newline|'\n'
name|'used_slots'
op|'='
op|'['
name|'int'
op|'('
name|'disk'
op|'.'
name|'AddressOnParent'
op|')'
name|'for'
name|'disk'
name|'in'
name|'attached_disks'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'slot'
name|'in'
name|'xrange'
op|'('
name|'constants'
op|'.'
name|'SCSI_CONTROLLER_SLOTS_NUMBER'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'slot'
name|'not'
name|'in'
name|'used_slots'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'slot'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
string|'"Exceeded the maximum number of slots"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volumes
dedent|''
name|'def'
name|'detach_volumes'
op|'('
name|'self'
op|','
name|'block_device_info'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'detach_volume'
op|'('
name|'vol'
op|'['
string|"'connection_info'"
op|']'
op|','
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|logout_storage_target
dedent|''
dedent|''
name|'def'
name|'logout_storage_target'
op|'('
name|'self'
op|','
name|'target_iqn'
op|','
name|'disconnected_luns_count'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'total_available_luns'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_target_lun_count'
op|'('
nl|'\n'
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'total_available_luns'
op|'=='
name|'disconnected_luns_count'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Logging off storage target %s"'
op|','
name|'target_iqn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
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
string|'"Skipping disconnecting target %s as there "'
nl|'\n'
string|'"are LUNs still being used."'
op|','
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach a volume to the SCSI controller."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Detach_volume: %(connection_info)s "'
nl|'\n'
string|'"from %(instance_name)s"'
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
nl|'\n'
comment|'# Getting the mounted disk'
nl|'\n'
name|'mounted_disk_path'
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
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Detaching physical disk from instance: %s"'
op|','
nl|'\n'
name|'mounted_disk_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'detach_vm_disk'
op|'('
name|'instance_name'
op|','
name|'mounted_disk_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'logout_storage_target'
op|'('
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
name|'_volutils'
op|'.'
name|'get_iscsi_initiator'
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
name|'my_block_storage_ip'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
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
op|','
nl|'\n'
name|'wait_for_device'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# The WMI query in get_device_number_for_target can incorrectly'
nl|'\n'
comment|'# return no data when the system is under load.  This issue can'
nl|'\n'
comment|'# be avoided by adding a retry.'
nl|'\n'
indent|'        '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'mounted_disk_query_retry_count'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'device_number'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_device_number_for_target'
op|'('
nl|'\n'
name|'target_iqn'
op|','
name|'target_lun'
op|')'
newline|'\n'
name|'if'
name|'device_number'
name|'in'
op|'('
name|'None'
op|','
op|'-'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'attempt'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Attempt %d to get device_number '"
nl|'\n'
string|"'from get_device_number_for_target failed. '"
nl|'\n'
string|"'Retrying...'"
op|','
name|'attempt'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'mounted_disk_query_retry_interval'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'device_number'
name|'in'
op|'('
name|'None'
op|','
op|'-'
number|'1'
op|')'
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
string|"'Unable to find a mounted disk for '"
nl|'\n'
string|"'target_iqn: %s'"
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
string|"'Device number: %(device_number)s, '"
nl|'\n'
string|"'target lun: %(target_lun)s'"
op|','
nl|'\n'
op|'{'
string|"'device_number'"
op|':'
name|'device_number'
op|','
string|"'target_lun'"
op|':'
name|'target_lun'
op|'}'
op|')'
newline|'\n'
comment|'# Finding Mounted disk drive'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'volume_attach_retry_count'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mounted_disk_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_mounted_disk_by_drive_number'
op|'('
nl|'\n'
name|'device_number'
op|')'
newline|'\n'
name|'if'
name|'mounted_disk_path'
name|'or'
name|'not'
name|'wait_for_device'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'volume_attach_retry_interval'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'mounted_disk_path'
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
string|"'Unable to find a mounted disk '"
nl|'\n'
string|"'for target_iqn: %s'"
op|')'
op|'%'
name|'target_iqn'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'mounted_disk_path'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volumes
dedent|''
name|'def'
name|'disconnect_volumes'
op|'('
name|'self'
op|','
name|'volume_drives'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'targets'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'int'
op|')'
newline|'\n'
name|'for'
name|'volume_drive'
name|'in'
name|'volume_drives'
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
nl|'\n'
name|'volume_drive'
op|')'
newline|'\n'
name|'if'
name|'target'
op|':'
newline|'\n'
indent|'                '
name|'target_iqn'
op|'='
name|'target'
op|'['
number|'0'
op|']'
newline|'\n'
name|'targets'
op|'['
name|'target_iqn'
op|']'
op|'+='
number|'1'
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
string|'"Could not retrieve iSCSI target from disk path: "'
op|','
nl|'\n'
name|'volume_drive'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'target_iqn'
name|'in'
name|'targets'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
op|','
name|'targets'
op|'['
name|'target_iqn'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_target_from_disk_path
dedent|''
dedent|''
name|'def'
name|'get_target_from_disk_path'
op|'('
name|'self'
op|','
name|'physical_drive_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_target_from_disk_path'
op|'('
name|'physical_drive_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fix_instance_volume_disk_paths
dedent|''
name|'def'
name|'fix_instance_volume_disk_paths'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'ebs_root_in_block_devices'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mapping'
op|'='
name|'mapping'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'disk_address'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
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
nl|'\n'
name|'mounted_disk_path'
op|'='
name|'self'
op|'.'
name|'_get_mounted_disk_from_lun'
op|'('
nl|'\n'
name|'target_iqn'
op|','
name|'target_lun'
op|','
name|'True'
op|')'
newline|'\n'
name|'ctrller_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_scsi_controller'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'set_disk_host_resource'
op|'('
nl|'\n'
name|'instance_name'
op|','
name|'ctrller_path'
op|','
name|'disk_address'
op|','
name|'mounted_disk_path'
op|')'
newline|'\n'
name|'disk_address'
op|'+='
number|'1'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
