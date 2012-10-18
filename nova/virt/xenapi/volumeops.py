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
string|'"""\nManagement class for Storage-related functions (attach, detach, etc).\n"""'
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
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'volume_utils'
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
DECL|class|VolumeOps
name|'class'
name|'VolumeOps'
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
nl|'\n'
DECL|member|create_volume_for_sm
dedent|''
name|'def'
name|'create_volume_for_sm'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'sr_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating volume for Storage Manager"'
op|')'
newline|'\n'
nl|'\n'
name|'sm_vol_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sr_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_by_uuid"'
op|','
name|'sr_uuid'
op|')'
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
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'volume_utils'
op|'.'
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to get SR using uuid'"
op|')'
op|')'
newline|'\n'
comment|'#Create VDI'
nl|'\n'
dedent|''
name|'label'
op|'='
string|"'vol-'"
op|'+'
name|'volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'desc'
op|'='
string|"'xensm volume for '"
op|'+'
name|'volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
comment|'# size presented to xenapi is in bytes, while euca api is in GB'
nl|'\n'
name|'vdi_size'
op|'='
name|'volume'
op|'['
string|"'size'"
op|']'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'vdi_ref'
op|'='
name|'vm_utils'
op|'.'
name|'create_vdi'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|','
nl|'\n'
name|'None'
op|','
name|'label'
op|','
name|'desc'
op|','
nl|'\n'
name|'vdi_size'
op|','
name|'False'
op|')'
newline|'\n'
name|'vdi_rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_record"'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'sm_vol_rec'
op|'['
string|"'vdi_uuid'"
op|']'
op|'='
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'return'
name|'sm_vol_rec'
newline|'\n'
nl|'\n'
DECL|member|delete_volume_for_sm
dedent|''
name|'def'
name|'delete_volume_for_sm'
op|'('
name|'self'
op|','
name|'vdi_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vdi_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_by_uuid"'
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
name|'if'
name|'vdi_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'Could not find VDI ref'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vm_utils'
op|'.'
name|'destroy_vdi'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_sr
dedent|''
name|'def'
name|'create_sr'
op|'('
name|'self'
op|','
name|'label'
op|','
name|'params'
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
string|'"Creating SR %s"'
op|')'
op|'%'
name|'label'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'create_sr'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'label'
op|','
name|'params'
op|')'
newline|'\n'
name|'if'
name|'sr_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'Could not create SR'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'sr_rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_record"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'if'
name|'sr_rec'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'Could not retrieve SR record'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'sr_rec'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Checks if sr has already been introduced to this host'
nl|'\n'
DECL|member|introduce_sr
dedent|''
name|'def'
name|'introduce_sr'
op|'('
name|'self'
op|','
name|'sr_uuid'
op|','
name|'label'
op|','
name|'params'
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
string|'"Introducing SR %s"'
op|')'
op|'%'
name|'label'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_sr_by_uuid'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_uuid'
op|')'
newline|'\n'
name|'if'
name|'sr_ref'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'SR found in xapi database. No need to introduce'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'sr_ref'
newline|'\n'
dedent|''
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'introduce_sr'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_uuid'
op|','
name|'label'
op|','
nl|'\n'
name|'params'
op|')'
newline|'\n'
name|'if'
name|'sr_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'Could not introduce SR'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'sr_ref'
newline|'\n'
nl|'\n'
DECL|member|is_sr_on_host
dedent|''
name|'def'
name|'is_sr_on_host'
op|'('
name|'self'
op|','
name|'sr_uuid'
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
string|"'Checking for SR %s'"
op|')'
op|'%'
name|'sr_uuid'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_sr_by_uuid'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_uuid'
op|')'
newline|'\n'
name|'if'
name|'sr_ref'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|'# Checks if sr has been introduced'
nl|'\n'
DECL|member|forget_sr
dedent|''
name|'def'
name|'forget_sr'
op|'('
name|'self'
op|','
name|'sr_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_sr_by_uuid'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_uuid'
op|')'
newline|'\n'
name|'if'
name|'sr_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'INFO'
op|'('
name|'_'
op|'('
string|"'SR %s not found in the xapi database'"
op|')'
op|'%'
name|'sr_uuid'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_utils'
op|'.'
name|'forget_sr'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'Could not forget SR'"
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
string|'"""Attach volume storage to VM instance"""'
newline|'\n'
comment|'# Before we start, check that the VM exists'
nl|'\n'
name|'vm_ref'
op|'='
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm_ref'
name|'is'
name|'None'
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
name|'instance_name'
op|')'
newline|'\n'
comment|'# NOTE: No Resource Pool concept so far'
nl|'\n'
dedent|''
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
name|'driver_type'
op|'='
name|'connection_info'
op|'['
string|"'driver_volume_type'"
op|']'
newline|'\n'
name|'if'
name|'driver_type'
name|'not'
name|'in'
op|'['
string|"'iscsi'"
op|','
string|"'xensm'"
op|']'
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
dedent|''
name|'connection_data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'if'
string|"'name_label'"
name|'not'
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'            '
name|'label'
op|'='
string|"'tempSR-%s'"
op|'%'
name|'connection_data'
op|'['
string|"'volume_id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'label'
op|'='
name|'connection_data'
op|'['
string|"'name_label'"
op|']'
newline|'\n'
name|'del'
name|'connection_data'
op|'['
string|"'name_label'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'name_description'"
name|'not'
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'            '
name|'desc'
op|'='
string|"'Disk-for:%s'"
op|'%'
name|'instance_name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'desc'
op|'='
name|'connection_data'
op|'['
string|"'name_description'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'connection_info'
op|')'
newline|'\n'
name|'sr_params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"u'sr_uuid'"
name|'not'
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'            '
name|'sr_params'
op|'='
name|'volume_utils'
op|'.'
name|'parse_volume_info'
op|'('
name|'connection_data'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
name|'uuid'
op|'='
string|'"FA15E-D15C-"'
op|'+'
name|'str'
op|'('
name|'sr_params'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'sr_params'
op|'['
string|"'sr_type'"
op|']'
op|'='
string|"'iscsi'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'uuid'
op|'='
name|'connection_data'
op|'['
string|"'sr_uuid'"
op|']'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'connection_data'
op|'['
string|"'introduce_sr_keys'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'sr_params'
op|'['
name|'k'
op|']'
op|'='
name|'connection_data'
op|'['
name|'k'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'sr_params'
op|'['
string|"'name_description'"
op|']'
op|'='
name|'desc'
newline|'\n'
nl|'\n'
comment|'# Introduce SR'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sr_ref'
op|'='
name|'self'
op|'.'
name|'introduce_sr'
op|'('
name|'uuid'
op|','
name|'label'
op|','
name|'sr_params'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Introduced %(label)s as %(sr_ref)s.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
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
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'volume_utils'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Unable to introduce Storage Repository'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vdi_uuid'
op|'='
name|'None'
newline|'\n'
name|'target_lun'
op|'='
name|'None'
newline|'\n'
name|'if'
string|"'vdi_uuid'"
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'            '
name|'vdi_uuid'
op|'='
name|'connection_data'
op|'['
string|"'vdi_uuid'"
op|']'
newline|'\n'
dedent|''
name|'elif'
string|"'target_lun'"
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'            '
name|'target_lun'
op|'='
name|'connection_data'
op|'['
string|"'target_lun'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'vdi_uuid'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# Introduce VDI  and attach VBD to VM'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vdi_ref'
op|'='
name|'volume_utils'
op|'.'
name|'introduce_vdi'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|','
nl|'\n'
name|'vdi_uuid'
op|','
name|'target_lun'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'forget_sr'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to create VDI on SR %(sr_ref)s for'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'dev_number'
op|'='
name|'volume_utils'
op|'.'
name|'mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vbd_ref'
op|'='
name|'vm_utils'
op|'.'
name|'create_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
nl|'\n'
name|'dev_number'
op|','
name|'bootable'
op|'='
name|'False'
op|')'
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
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'forget_sr'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to use SR %(sr_ref)s for'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VBD.plug"'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
comment|'# set osvol=True in other-config to indicate this is an'
nl|'\n'
comment|'# attached nova (or cinder) volume'
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VBD.add_to_other_config"'
op|','
nl|'\n'
name|'vbd_ref'
op|','
string|"'osvol'"
op|','
string|'"True"'
op|')'
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
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'forget_sr'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
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
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Mountpoint %(mountpoint)s attached to'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
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
string|'"""Detach volume storage to VM instance"""'
newline|'\n'
comment|'# Before we start, check that the VM exists'
nl|'\n'
name|'vm_ref'
op|'='
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm_ref'
name|'is'
name|'None'
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
name|'instance_name'
op|')'
newline|'\n'
comment|'# Detach VBD from VM'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Detach_volume: %(instance_name)s, %(mountpoint)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'device_number'
op|'='
name|'volume_utils'
op|'.'
name|'mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vbd_ref'
op|'='
name|'vm_utils'
op|'.'
name|'find_vbd_by_number'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'device_number'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to locate volume %s'"
op|')'
op|'%'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vm_rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VM.get_record"'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_sr_from_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
name|'if'
name|'vm_rec'
op|'['
string|"'power_state'"
op|']'
op|'!='
string|"'Halted'"
op|':'
newline|'\n'
indent|'                '
name|'vm_utils'
op|'.'
name|'unplug_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to detach volume %s'"
op|')'
op|'%'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vm_utils'
op|'.'
name|'destroy_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to destroy vbd %s'"
op|')'
op|'%'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
comment|'# Forget SR only if no other volumes on this host are using it'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_utils'
op|'.'
name|'purge_sr'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Error purging SR %s'"
op|')'
op|'%'
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Mountpoint %(mountpoint)s detached from'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
