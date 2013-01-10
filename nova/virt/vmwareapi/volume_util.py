begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nHelper methods for operations related to the management of volumes,\nand storage repositories\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'string'
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
name|'vim_util'
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
DECL|class|StorageError
name|'class'
name|'StorageError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""To raise errors related to Volume commands."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'StorageError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_host_iqn
dedent|''
dedent|''
name|'def'
name|'get_host_iqn'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Return the host iSCSI IQN.\n    """'
newline|'\n'
name|'host_mor'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_objects"'
op|','
nl|'\n'
string|'"HostSystem"'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'obj'
newline|'\n'
name|'hbas_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_property"'
op|','
nl|'\n'
name|'host_mor'
op|','
string|'"HostSystem"'
op|','
nl|'\n'
string|'"config.storageDevice.hostBusAdapter"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Meaning there are no host bus adapters on the host'
nl|'\n'
name|'if'
name|'not'
name|'hbas_ret'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'host_hbas'
op|'='
name|'hbas_ret'
op|'.'
name|'HostHostBusAdapter'
newline|'\n'
name|'for'
name|'hba'
name|'in'
name|'host_hbas'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hba'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|"'HostInternetScsiHba'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'hba'
op|'.'
name|'iScsiName'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_st
dedent|''
dedent|''
dedent|''
name|'def'
name|'find_st'
op|'('
name|'session'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Return the iSCSI Target given a volume info.\n    """'
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
name|'host_mor'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_objects"'
op|','
nl|'\n'
string|'"HostSystem"'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'obj'
newline|'\n'
nl|'\n'
name|'lst_properties'
op|'='
op|'['
string|'"config.storageDevice.hostBusAdapter"'
op|','
nl|'\n'
string|'"config.storageDevice.scsiTopology"'
op|','
nl|'\n'
string|'"config.storageDevice.scsiLun"'
op|']'
newline|'\n'
name|'props'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_object_properties"'
op|','
nl|'\n'
name|'None'
op|','
name|'host_mor'
op|','
string|'"HostSystem"'
op|','
nl|'\n'
name|'lst_properties'
op|')'
newline|'\n'
name|'result'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'hbas_ret'
op|'='
name|'None'
newline|'\n'
name|'scsi_topology'
op|'='
name|'None'
newline|'\n'
name|'scsi_lun_ret'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'elem'
name|'in'
name|'props'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'prop'
name|'in'
name|'elem'
op|'.'
name|'propSet'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'prop'
op|'.'
name|'name'
op|'=='
string|'"config.storageDevice.hostBusAdapter"'
op|':'
newline|'\n'
indent|'                '
name|'hbas_ret'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
dedent|''
name|'elif'
name|'prop'
op|'.'
name|'name'
op|'=='
string|'"config.storageDevice.scsiTopology"'
op|':'
newline|'\n'
indent|'                '
name|'scsi_topology'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
dedent|''
name|'elif'
name|'prop'
op|'.'
name|'name'
op|'=='
string|'"config.storageDevice.scsiLun"'
op|':'
newline|'\n'
indent|'                '
name|'scsi_lun_ret'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
nl|'\n'
comment|'# Meaning there are no host bus adapters on the host'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'hbas_ret'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'host_hbas'
op|'='
name|'hbas_ret'
op|'.'
name|'HostHostBusAdapter'
newline|'\n'
name|'if'
name|'not'
name|'host_hbas'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'for'
name|'hba'
name|'in'
name|'host_hbas'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hba'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|"'HostInternetScsiHba'"
op|':'
newline|'\n'
indent|'            '
name|'hba_key'
op|'='
name|'hba'
op|'.'
name|'key'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'scsi_topology'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'host_adapters'
op|'='
name|'scsi_topology'
op|'.'
name|'adapter'
newline|'\n'
name|'if'
name|'not'
name|'host_adapters'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'scsi_lun_key'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'adapter'
name|'in'
name|'host_adapters'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'adapter'
op|'.'
name|'adapter'
op|'=='
name|'hba_key'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'getattr'
op|'('
name|'adapter'
op|','
string|"'target'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'for'
name|'target'
name|'in'
name|'adapter'
op|'.'
name|'target'
op|':'
newline|'\n'
indent|'                '
name|'if'
op|'('
name|'getattr'
op|'('
name|'target'
op|'.'
name|'transport'
op|','
string|"'address'"
op|','
name|'None'
op|')'
name|'and'
nl|'\n'
name|'target'
op|'.'
name|'transport'
op|'.'
name|'address'
op|'['
number|'0'
op|']'
op|'=='
name|'target_portal'
name|'and'
nl|'\n'
name|'target'
op|'.'
name|'transport'
op|'.'
name|'iScsiName'
op|'=='
name|'target_iqn'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'not'
name|'target'
op|'.'
name|'lun'
op|':'
newline|'\n'
indent|'                        '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'for'
name|'lun'
name|'in'
name|'target'
op|'.'
name|'lun'
op|':'
newline|'\n'
indent|'                        '
name|'if'
string|"'host.ScsiDisk'"
name|'in'
name|'lun'
op|'.'
name|'scsiLun'
op|':'
newline|'\n'
indent|'                            '
name|'scsi_lun_key'
op|'='
name|'lun'
op|'.'
name|'scsiLun'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'scsi_lun_key'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'scsi_lun_ret'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'host_scsi_luns'
op|'='
name|'scsi_lun_ret'
op|'.'
name|'ScsiLun'
newline|'\n'
name|'if'
name|'not'
name|'host_scsi_luns'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'for'
name|'scsi_lun'
name|'in'
name|'host_scsi_luns'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'scsi_lun'
op|'.'
name|'key'
op|'=='
name|'scsi_lun_key'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'scsi_lun'
op|'.'
name|'deviceName'
op|','
name|'scsi_lun'
op|'.'
name|'uuid'
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
DECL|function|rescan_iscsi_hba
dedent|''
name|'def'
name|'rescan_iscsi_hba'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Rescan the iSCSI HBA to discover iSCSI targets.\n    """'
newline|'\n'
comment|'# There is only one default storage system in a standalone ESX host'
nl|'\n'
name|'storage_system_mor'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_objects"'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
op|'['
string|'"configManager.storageSystem"'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'propSet'
op|'['
number|'0'
op|']'
op|'.'
name|'val'
newline|'\n'
name|'hbas_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
nl|'\n'
name|'storage_system_mor'
op|','
nl|'\n'
string|'"HostStorageSystem"'
op|','
nl|'\n'
string|'"storageDeviceInfo.hostBusAdapter"'
op|')'
newline|'\n'
comment|'# Meaning there are no host bus adapters on the host'
nl|'\n'
name|'if'
name|'hbas_ret'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'host_hbas'
op|'='
name|'hbas_ret'
op|'.'
name|'HostHostBusAdapter'
newline|'\n'
name|'if'
name|'not'
name|'host_hbas'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'for'
name|'hba'
name|'in'
name|'host_hbas'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hba'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|"'HostInternetScsiHba'"
op|':'
newline|'\n'
indent|'            '
name|'hba_device'
op|'='
name|'hba'
op|'.'
name|'device'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Rescanning HBA %s"'
op|')'
op|'%'
name|'hba_device'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
string|'"RescanHba"'
op|','
name|'storage_system_mor'
op|','
nl|'\n'
name|'hbaDevice'
op|'='
name|'hba_device'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Rescanned HBA %s "'
op|')'
op|'%'
name|'hba_device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mountpoint_to_number
dedent|''
name|'def'
name|'mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Translate a mountpoint like /dev/sdc into a numeric."""'
newline|'\n'
name|'if'
name|'mountpoint'
op|'.'
name|'startswith'
op|'('
string|"'/dev/'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mountpoint'
op|'='
name|'mountpoint'
op|'['
number|'5'
op|':'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'re'
op|'.'
name|'match'
op|'('
string|"'^[hsv]d[a-p]$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'ord'
op|'('
name|'mountpoint'
op|'['
number|'2'
op|':'
number|'3'
op|']'
op|')'
op|'-'
name|'ord'
op|'('
string|"'a'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'re'
op|'.'
name|'match'
op|'('
string|"'^[0-9]+$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'string'
op|'.'
name|'atoi'
op|'('
name|'mountpoint'
op|','
number|'10'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Mountpoint cannot be translated: %s"'
op|')'
op|'%'
name|'mountpoint'
op|')'
newline|'\n'
name|'return'
op|'-'
number|'1'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
