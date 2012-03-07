begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""Volume drivers for libvirt."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'num_iscsi_scan_tries'"
op|','
string|"'nova.volume.driver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtVolumeDriver
name|'class'
name|'LibvirtVolumeDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for volume drivers."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
nl|'\n'
DECL|member|_pick_volume_driver
dedent|''
name|'def'
name|'_pick_volume_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hypervisor_type'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_hypervisor_type'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'return'
string|'"phy"'
name|'if'
name|'hypervisor_type'
op|'=='
string|'"xen"'
name|'else'
string|'"qemu"'
newline|'\n'
nl|'\n'
DECL|member|connect_volume
dedent|''
name|'def'
name|'connect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Connect the volume. Returns xml for libvirt."""'
newline|'\n'
name|'conf'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'source_type'
op|'='
string|'"block"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_name'
op|'='
name|'self'
op|'.'
name|'_pick_volume_driver'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'driver_format'
op|'='
string|'"raw"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_cache'
op|'='
string|'"none"'
newline|'\n'
name|'conf'
op|'.'
name|'source_path'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'mount_device'
newline|'\n'
name|'conf'
op|'.'
name|'target_bus'
op|'='
string|'"virtio"'
newline|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volume
dedent|''
name|'def'
name|'disconnect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disconnect the volume"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtFakeVolumeDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtFakeVolumeDriver'
op|'('
name|'LibvirtVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver to attach Network volumes to libvirt."""'
newline|'\n'
nl|'\n'
DECL|member|connect_volume
name|'def'
name|'connect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'source_type'
op|'='
string|'"network"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_name'
op|'='
string|'"qemu"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_format'
op|'='
string|'"raw"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_cache'
op|'='
string|'"none"'
newline|'\n'
name|'conf'
op|'.'
name|'source_protocol'
op|'='
string|'"fake"'
newline|'\n'
name|'conf'
op|'.'
name|'source_host'
op|'='
string|'"fake"'
newline|'\n'
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'mount_device'
newline|'\n'
name|'conf'
op|'.'
name|'target_bus'
op|'='
string|'"virtio"'
newline|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtNetVolumeDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtNetVolumeDriver'
op|'('
name|'LibvirtVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver to attach Network volumes to libvirt."""'
newline|'\n'
nl|'\n'
DECL|member|connect_volume
name|'def'
name|'connect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'source_type'
op|'='
string|'"network"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_name'
op|'='
name|'self'
op|'.'
name|'_pick_volume_driver'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'driver_format'
op|'='
string|'"raw"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_cache'
op|'='
string|'"none"'
newline|'\n'
name|'conf'
op|'.'
name|'source_protocol'
op|'='
name|'connection_info'
op|'['
string|"'driver_volume_type'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'source_host'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'mount_device'
newline|'\n'
name|'conf'
op|'.'
name|'target_bus'
op|'='
string|'"virtio"'
newline|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtISCSIVolumeDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtISCSIVolumeDriver'
op|'('
name|'LibvirtVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver to attach Network volumes to libvirt."""'
newline|'\n'
nl|'\n'
DECL|member|_run_iscsiadm
name|'def'
name|'_run_iscsiadm'
op|'('
name|'self'
op|','
name|'iscsi_properties'
op|','
name|'iscsi_command'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check_exit_code'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'check_exit_code'"
op|','
number|'0'
op|')'
newline|'\n'
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
nl|'\n'
name|'iscsi_properties'
op|'['
string|"'target_iqn'"
op|']'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'iscsi_properties'
op|'['
string|"'target_portal'"
op|']'
op|','
nl|'\n'
op|'*'
name|'iscsi_command'
op|','
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'check_exit_code'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"iscsiadm %s: stdout=%s stderr=%s"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_command'
op|','
name|'out'
op|','
name|'err'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'out'
op|','
name|'err'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_iscsiadm_update
dedent|''
name|'def'
name|'_iscsiadm_update'
op|'('
name|'self'
op|','
name|'iscsi_properties'
op|','
name|'property_key'
op|','
name|'property_value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'iscsi_command'
op|'='
op|'('
string|"'--op'"
op|','
string|"'update'"
op|','
string|"'-n'"
op|','
name|'property_key'
op|','
nl|'\n'
string|"'-v'"
op|','
name|'property_value'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_run_iscsiadm'
op|'('
name|'iscsi_properties'
op|','
name|'iscsi_command'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'connect_volume'"
op|')'
newline|'\n'
DECL|member|connect_volume
name|'def'
name|'connect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach the volume to instance_name"""'
newline|'\n'
name|'iscsi_properties'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
comment|'# NOTE(vish): If we are on the same host as nova volume, the'
nl|'\n'
comment|"#             discovery makes the target so we don't need to"
nl|'\n'
comment|'#             run --op new. Therefore, we check to see if the'
nl|'\n'
comment|'#             target exists, and if we get 255 (Not Found), then'
nl|'\n'
comment|'#             we run --op new. This will also happen if another'
nl|'\n'
comment|'#             volume is using the same target.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_run_iscsiadm'
op|'('
name|'iscsi_properties'
op|','
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# iscsiadm returns 21 for "No records found" after version 2.0-871'
nl|'\n'
indent|'            '
name|'if'
name|'exc'
op|'.'
name|'exit_code'
name|'in'
op|'['
number|'21'
op|','
number|'255'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_run_iscsiadm'
op|'('
name|'iscsi_properties'
op|','
op|'('
string|"'--op'"
op|','
string|"'new'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'iscsi_properties'
op|'.'
name|'get'
op|'('
string|"'auth_method'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_iscsiadm_update'
op|'('
name|'iscsi_properties'
op|','
nl|'\n'
string|'"node.session.auth.authmethod"'
op|','
nl|'\n'
name|'iscsi_properties'
op|'['
string|"'auth_method'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_iscsiadm_update'
op|'('
name|'iscsi_properties'
op|','
nl|'\n'
string|'"node.session.auth.username"'
op|','
nl|'\n'
name|'iscsi_properties'
op|'['
string|"'auth_username'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_iscsiadm_update'
op|'('
name|'iscsi_properties'
op|','
nl|'\n'
string|'"node.session.auth.password"'
op|','
nl|'\n'
name|'iscsi_properties'
op|'['
string|"'auth_password'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): If we have another lun on the same target, we may'
nl|'\n'
comment|'#             have a duplicate login'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_run_iscsiadm'
op|'('
name|'iscsi_properties'
op|','
op|'('
string|'"--login"'
op|','
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'255'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_iscsiadm_update'
op|'('
name|'iscsi_properties'
op|','
string|'"node.startup"'
op|','
string|'"automatic"'
op|')'
newline|'\n'
nl|'\n'
name|'host_device'
op|'='
op|'('
string|'"/dev/disk/by-path/ip-%s-iscsi-%s-lun-%s"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_properties'
op|'['
string|"'target_portal'"
op|']'
op|','
nl|'\n'
name|'iscsi_properties'
op|'['
string|"'target_iqn'"
op|']'
op|','
nl|'\n'
name|'iscsi_properties'
op|'.'
name|'get'
op|'('
string|"'target_lun'"
op|','
number|'0'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# The /dev/disk/by-path/... node is not always present immediately'
nl|'\n'
comment|'# TODO(justinsb): This retry-with-delay is a pattern, move to utils?'
nl|'\n'
name|'tries'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'host_device'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tries'
op|'>='
name|'FLAGS'
op|'.'
name|'num_iscsi_scan_tries'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"iSCSI device not found at %s"'
op|')'
op|'%'
nl|'\n'
op|'('
name|'host_device'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"ISCSI volume not yet found at: %(mount_device)s. "'
nl|'\n'
string|'"Will rescan & retry.  Try number: %(tries)s"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# The rescan isn't documented as being necessary(?), but it helps"
nl|'\n'
name|'self'
op|'.'
name|'_run_iscsiadm'
op|'('
name|'iscsi_properties'
op|','
op|'('
string|'"--rescan"'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'tries'
op|'='
name|'tries'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'host_device'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'time'
op|'.'
name|'sleep'
op|'('
name|'tries'
op|'**'
number|'2'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'tries'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Found iSCSI node %(mount_device)s "'
nl|'\n'
string|'"(after %(tries)s rescans)"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
op|'='
name|'host_device'
newline|'\n'
name|'sup'
op|'='
name|'super'
op|'('
name|'LibvirtISCSIVolumeDriver'
op|','
name|'self'
op|')'
newline|'\n'
name|'return'
name|'sup'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'connect_volume'"
op|')'
newline|'\n'
DECL|member|disconnect_volume
name|'def'
name|'disconnect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach the volume from instance_name"""'
newline|'\n'
name|'sup'
op|'='
name|'super'
op|'('
name|'LibvirtISCSIVolumeDriver'
op|','
name|'self'
op|')'
newline|'\n'
name|'sup'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'iscsi_properties'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
comment|'# NOTE(vish): Only disconnect from the target if no luns from the'
nl|'\n'
comment|'#             target are in use.'
nl|'\n'
name|'device_prefix'
op|'='
op|'('
string|'"/dev/disk/by-path/ip-%s-iscsi-%s-lun-"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_properties'
op|'['
string|"'target_portal'"
op|']'
op|','
nl|'\n'
name|'iscsi_properties'
op|'['
string|"'target_iqn'"
op|']'
op|')'
op|')'
newline|'\n'
name|'devices'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_all_block_devices'
op|'('
op|')'
newline|'\n'
name|'devices'
op|'='
op|'['
name|'dev'
name|'for'
name|'dev'
name|'in'
name|'devices'
name|'if'
name|'dev'
op|'.'
name|'startswith'
op|'('
name|'device_prefix'
op|')'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'devices'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_iscsiadm_update'
op|'('
name|'iscsi_properties'
op|','
string|'"node.startup"'
op|','
string|'"manual"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_run_iscsiadm'
op|'('
name|'iscsi_properties'
op|','
op|'('
string|'"--logout"'
op|','
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'255'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_run_iscsiadm'
op|'('
name|'iscsi_properties'
op|','
op|'('
string|"'--op'"
op|','
string|"'delete'"
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'255'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
