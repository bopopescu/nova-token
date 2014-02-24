begin_unit
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
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the host iSCSI IQN."""'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
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
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the iSCSI Target given a volume info."""'
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
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
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
name|'prop_dict'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_properties"'
op|','
nl|'\n'
name|'host_mor'
op|','
string|'"HostSystem"'
op|','
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
name|'if'
name|'prop_dict'
op|':'
newline|'\n'
indent|'        '
name|'hbas_ret'
op|'='
name|'prop_dict'
op|'.'
name|'get'
op|'('
string|"'config.storageDevice.hostBusAdapter'"
op|')'
newline|'\n'
name|'scsi_topology'
op|'='
name|'prop_dict'
op|'.'
name|'get'
op|'('
string|"'config.storageDevice.scsiTopology'"
op|')'
newline|'\n'
name|'scsi_lun_ret'
op|'='
name|'prop_dict'
op|'.'
name|'get'
op|'('
string|"'config.storageDevice.scsiLun'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Meaning there are no host bus adapters on the host'
nl|'\n'
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
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Rescan the iSCSI HBA to discover iSCSI targets."""'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'storage_system_mor'
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
string|'"configManager.storageSystem"'
op|')'
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
dedent|''
endmarker|''
end_unit
