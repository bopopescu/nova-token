begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nHelper methods for operations related to the management of volumes,\nand storage repositories\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'XenAPI'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'process'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
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
string|'""" To raise errors related to SR, VDI, PBD, and VBD commands """'
newline|'\n'
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
DECL|class|VolumeHelper
dedent|''
dedent|''
name|'class'
name|'VolumeHelper'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The class that wraps the helper methods together.\n    """'
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
name|'return'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|create_iscsi_storage
name|'def'
name|'create_iscsi_storage'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'info'
op|','
name|'label'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create an iSCSI storage repository that will be used to mount\n        the volume for the specified instance\n        """'
newline|'\n'
name|'return'
name|'VolumeHelper'
op|'.'
name|'create_iscsi_storage_blocking'
op|'('
name|'session'
op|','
name|'info'
op|','
nl|'\n'
name|'label'
op|','
nl|'\n'
name|'description'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_iscsi_storage_blocking
name|'def'
name|'create_iscsi_storage_blocking'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'info'
op|','
name|'label'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Synchronous create_iscsi_storage """'
newline|'\n'
name|'sr_ref'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'SR'
op|'.'
name|'get_by_name_label'
op|'('
name|'label'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'sr_ref'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Introducing %s...'"
op|','
name|'label'
op|')'
newline|'\n'
name|'record'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'chapuser'"
name|'in'
name|'info'
name|'and'
string|"'chappassword'"
name|'in'
name|'info'
op|':'
newline|'\n'
indent|'                '
name|'record'
op|'='
op|'{'
string|"'target'"
op|':'
name|'info'
op|'['
string|"'targetHost'"
op|']'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'info'
op|'['
string|"'targetPort'"
op|']'
op|','
nl|'\n'
string|"'targetIQN'"
op|':'
name|'info'
op|'['
string|"'targeIQN'"
op|']'
op|','
nl|'\n'
string|"'chapuser'"
op|':'
name|'info'
op|'['
string|"'chapuser'"
op|']'
op|','
nl|'\n'
string|"'chappassword'"
op|':'
name|'info'
op|'['
string|"'chappassword'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'record'
op|'='
op|'{'
string|"'target'"
op|':'
name|'info'
op|'['
string|"'targetHost'"
op|']'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'info'
op|'['
string|"'targetPort'"
op|']'
op|','
nl|'\n'
string|"'targetIQN'"
op|':'
name|'info'
op|'['
string|"'targeIQN'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'sr_ref'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'SR'
op|'.'
name|'create'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'get_xenapi_host'
op|'('
op|')'
op|','
nl|'\n'
name|'record'
op|','
nl|'\n'
string|"'0'"
op|','
name|'label'
op|','
name|'description'
op|','
string|"'iscsi'"
op|','
string|"''"
op|','
name|'False'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Introduced %s as %s.'"
op|','
name|'label'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'return'
name|'sr_ref'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'StorageError'
op|'('
string|"'Unable to create Storage Repository'"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'sr_ref'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|find_sr_from_vbd
name|'def'
name|'find_sr_from_vbd'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vbd_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Find the SR reference from the VBD reference """'
newline|'\n'
name|'vdi_ref'
op|'='
name|'yield'
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VBD'
op|'.'
name|'get_VDI'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'yield'
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_SR'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|destroy_iscsi_storage
name|'def'
name|'destroy_iscsi_storage'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Forget the SR whilst preserving the state of the disk """'
newline|'\n'
name|'VolumeHelper'
op|'.'
name|'destroy_iscsi_storage_blocking'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|destroy_iscsi_storage_blocking
name|'def'
name|'destroy_iscsi_storage_blocking'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Synchronous destroy_iscsi_storage """'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Forgetting SR %s ... "'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'pbds'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pbds'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'SR'
op|'.'
name|'get_PBDs'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|"'Ignoring exception %s when getting PBDs for %s'"
op|','
nl|'\n'
name|'exc'
op|','
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'pbd'
name|'in'
name|'pbds'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'PBD'
op|'.'
name|'unplug'
op|'('
name|'pbd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'warn'
op|'('
string|"'Ignoring exception %s when unplugging PBD %s'"
op|','
nl|'\n'
name|'exc'
op|','
name|'pbd'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'SR'
op|'.'
name|'forget'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Forgetting SR %s done."'
op|','
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|"'Ignoring exception %s when forgetting SR %s'"
op|','
nl|'\n'
name|'exc'
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|introduce_vdi
name|'def'
name|'introduce_vdi'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Introduce VDI in the host """'
newline|'\n'
name|'return'
name|'VolumeHelper'
op|'.'
name|'introduce_vdi_blocking'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|introduce_vdi_blocking
name|'def'
name|'introduce_vdi_blocking'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Synchronous introduce_vdi """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vdis'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'SR'
op|'.'
name|'get_VDIs'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'StorageError'
op|'('
string|"'Unable to introduce VDI on SR %s'"
op|'%'
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'vdis'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'StorageError'
op|'('
string|"'Unable to get record of VDI %s on'"
op|'%'
name|'vdis'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'introduce'
op|'('
nl|'\n'
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'name_label'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'name_description'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'SR'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'type'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'sharable'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'read_only'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'other_config'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'location'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'xenstore_data'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'sm_config'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|parse_volume_info
name|'def'
name|'parse_volume_info'
op|'('
name|'cls'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Parse device_path and mountpoint as they can be used by XenAPI.\n        In particular, the mountpoint (e.g. /dev/sdc) must be translated\n        into a numeric literal.\n        FIXME(armando):\n        As for device_path, currently cannot be used as it is,\n        because it does not contain target information. As for interim\n        solution, target details are passed either via Flags or obtained\n        by iscsiadm. Long-term solution is to add a few more fields to the\n        db in the iscsi_target table with the necessary info and modify\n        the iscsi driver to set them.\n        """'
newline|'\n'
name|'device_number'
op|'='
name|'VolumeHelper'
op|'.'
name|'mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
name|'volume_id'
op|'='
name|'_get_volume_id'
op|'('
name|'device_path'
op|')'
newline|'\n'
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
op|'='
name|'yield'
name|'_get_target'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'target_host'
op|'='
name|'_get_target_host'
op|'('
name|'iscsi_portal'
op|')'
newline|'\n'
name|'target_port'
op|'='
name|'_get_target_port'
op|'('
name|'iscsi_portal'
op|')'
newline|'\n'
name|'target_iqn'
op|'='
name|'_get_iqn'
op|'('
name|'iscsi_name'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'(vol_id,number,host,port,iqn): (%s,%s,%s,%s)'"
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
name|'target_host'
op|','
nl|'\n'
name|'target_port'
op|','
nl|'\n'
name|'target_iqn'
op|')'
newline|'\n'
name|'if'
op|'('
name|'device_number'
op|'<'
number|'0'
op|')'
name|'or'
op|'('
name|'volume_id'
name|'is'
name|'None'
op|')'
name|'or'
op|'('
name|'target_host'
name|'is'
name|'None'
op|')'
name|'or'
op|'('
name|'target_iqn'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'StorageError'
op|'('
string|"'Unable to obtain target information %s, %s'"
op|'%'
nl|'\n'
op|'('
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|')'
newline|'\n'
dedent|''
name|'volume_info'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'volume_info'
op|'['
string|"'deviceNumber'"
op|']'
op|'='
name|'device_number'
newline|'\n'
name|'volume_info'
op|'['
string|"'volumeId'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'volume_info'
op|'['
string|"'targetHost'"
op|']'
op|'='
name|'target_host'
newline|'\n'
name|'volume_info'
op|'['
string|"'targetPort'"
op|']'
op|'='
name|'target_port'
newline|'\n'
name|'volume_info'
op|'['
string|"'targeIQN'"
op|']'
op|'='
name|'target_iqn'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'volume_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|mountpoint_to_number
name|'def'
name|'mountpoint_to_number'
op|'('
name|'cls'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Translate a mountpoint like /dev/sdc into a numberic """'
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
indent|'            '
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
string|"'^[hs]d[a-p]$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'            '
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
string|"'^vd[a-p]$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'            '
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
indent|'            '
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
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|"'Mountpoint cannot be translated: %s'"
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'return'
op|'-'
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_volume_id
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_volume_id'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Retrieve the volume id from device_path """'
newline|'\n'
comment|'# n must contain at least the volume_id'
nl|'\n'
comment|'# /vol- is for remote volumes'
nl|'\n'
comment|'# -vol- is for local volumes'
nl|'\n'
comment|'# see compute/manager->setup_compute_volume'
nl|'\n'
name|'volume_id'
op|'='
name|'path'
op|'['
name|'path'
op|'.'
name|'find'
op|'('
string|"'/vol-'"
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
name|'if'
name|'volume_id'
op|'=='
name|'path'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'path'
op|'['
name|'path'
op|'.'
name|'find'
op|'('
string|"'-vol-'"
op|')'
op|'+'
number|'1'
op|':'
op|']'
op|'.'
name|'replace'
op|'('
string|"'--'"
op|','
string|"'-'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'volume_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_target_host
dedent|''
name|'def'
name|'_get_target_host'
op|'('
name|'iscsi_string'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Retrieve target host """'
newline|'\n'
name|'if'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iscsi_string'
op|'['
number|'0'
op|':'
name|'iscsi_string'
op|'.'
name|'find'
op|'('
string|"':'"
op|')'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'iscsi_string'
name|'is'
name|'None'
name|'or'
name|'FLAGS'
op|'.'
name|'target_host'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'target_host'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_target_port
dedent|''
dedent|''
name|'def'
name|'_get_target_port'
op|'('
name|'iscsi_string'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Retrieve target port """'
newline|'\n'
name|'if'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iscsi_string'
op|'['
name|'iscsi_string'
op|'.'
name|'find'
op|'('
string|"':'"
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'iscsi_string'
name|'is'
name|'None'
name|'or'
name|'FLAGS'
op|'.'
name|'target_port'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'target_port'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_iqn
dedent|''
dedent|''
name|'def'
name|'_get_iqn'
op|'('
name|'iscsi_string'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Retrieve target IQN """'
newline|'\n'
name|'if'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iscsi_string'
newline|'\n'
dedent|''
name|'elif'
name|'iscsi_string'
name|'is'
name|'None'
name|'or'
name|'FLAGS'
op|'.'
name|'iqn_prefix'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'_get_volume_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'return'
string|"'%s:%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'iqn_prefix'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|function|_get_target
name|'def'
name|'_get_target'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Gets iscsi name and portal from volume name and host.\n    For this method to work the following are needed:\n    1) volume_ref[\'host\'] must resolve to something rather than loopback\n    2) ietd must bind only to the address as resolved above\n    If any of the two conditions are not met, fall back on Flags.\n    """'
newline|'\n'
name|'volume_ref'
op|'='
name|'db'
op|'.'
name|'volume_get_by_ec2_id'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'r'
op|','
name|'_e'
op|')'
op|'='
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo iscsiadm -m discovery -t "'
nl|'\n'
string|'"sendtargets -p %s"'
op|'%'
nl|'\n'
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'_e'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'target'
name|'in'
name|'r'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume_id'
name|'in'
name|'target'
op|':'
newline|'\n'
indent|'                '
op|'('
name|'location'
op|','
name|'_sep'
op|','
name|'iscsi_name'
op|')'
op|'='
name|'target'
op|'.'
name|'partition'
op|'('
string|'" "'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'iscsi_portal'
op|'='
name|'location'
op|'.'
name|'split'
op|'('
string|'","'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'defer'
op|'.'
name|'returnValue'
op|'('
op|'('
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
