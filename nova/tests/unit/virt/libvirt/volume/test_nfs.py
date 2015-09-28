begin_unit
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
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'test_volume'
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
name|'utils'
name|'as'
name|'libvirt_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'nfs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtNFSVolumeDriverTestCase
name|'class'
name|'LibvirtNFSVolumeDriverTestCase'
op|'('
name|'test_volume'
op|'.'
name|'LibvirtVolumeBaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests the libvirt NFS volume driver."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LibvirtNFSVolumeDriverTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'nfs_mount_point_base'
op|'='
name|'self'
op|'.'
name|'mnt_base'
op|','
name|'group'
op|'='
string|"'libvirt'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_nfs_driver
dedent|''
name|'def'
name|'test_libvirt_nfs_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'nfs'
op|'.'
name|'LibvirtNFSVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'libvirt_utils'
op|','
string|"'is_mounted'"
op|','
name|'lambda'
name|'x'
op|','
name|'d'
op|':'
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'export_string'
op|'='
string|"'192.168.1.1:/nfs/share1'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'export_string'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
op|'{'
string|"'export'"
op|':'
name|'export_string'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
op|'}'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
nl|'\n'
name|'device_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'export_mnt_base'
op|','
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
op|','
name|'device_path'
op|')'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
nl|'\n'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'export_mnt_base'
op|')'
op|','
nl|'\n'
op|'('
string|"'mount'"
op|','
string|"'-t'"
op|','
string|"'nfs'"
op|','
name|'export_string'
op|','
name|'export_mnt_base'
op|')'
op|','
nl|'\n'
op|'('
string|"'umount'"
op|','
name|'export_mnt_base'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'nfs'
op|'.'
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'nfs'
op|'.'
name|'LOG'
op|','
string|"'debug'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'nfs'
op|'.'
name|'LOG'
op|','
string|"'exception'"
op|')'
newline|'\n'
DECL|member|test_libvirt_nfs_driver_umount_error
name|'def'
name|'test_libvirt_nfs_driver_umount_error'
op|'('
name|'self'
op|','
name|'mock_LOG_exception'
op|','
nl|'\n'
name|'mock_LOG_debug'
op|','
name|'mock_utils_exe'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'export_string'
op|'='
string|"'192.168.1.1:/nfs/share1'"
newline|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
op|'{'
string|"'export'"
op|':'
name|'export_string'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
op|'}'
newline|'\n'
name|'libvirt_driver'
op|'='
name|'nfs'
op|'.'
name|'LibvirtNFSVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'mock_utils_exe'
op|'.'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
string|"'umount'"
op|','
string|"'umount: device is busy.'"
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_LOG_debug'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'mock_utils_exe'
op|'.'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
string|"'umount'"
op|','
string|"'umount: target is busy.'"
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_LOG_debug'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'mock_utils_exe'
op|'.'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
string|"'umount'"
op|','
string|"'umount: not mounted.'"
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_LOG_debug'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'mock_utils_exe'
op|'.'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
string|"'umount'"
op|','
string|"'umount: Other error.'"
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_LOG_exception'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_nfs_driver_get_config
dedent|''
name|'def'
name|'test_libvirt_nfs_driver_get_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'nfs'
op|'.'
name|'LibvirtNFSVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'export_string'
op|'='
string|"'192.168.1.1:/nfs/share1'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'export_string'
op|')'
op|')'
newline|'\n'
name|'file_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'export_mnt_base'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
op|'{'
string|"'export'"
op|':'
name|'export_string'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'device_path'"
op|':'
name|'file_path'
op|'}'
op|'}'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertFileTypeEquals'
op|'('
name|'tree'
op|','
name|'file_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'raw'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./driver'"
op|')'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_nfs_driver_already_mounted
dedent|''
name|'def'
name|'test_libvirt_nfs_driver_already_mounted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'nfs'
op|'.'
name|'LibvirtNFSVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
nl|'\n'
name|'export_string'
op|'='
string|"'192.168.1.1:/nfs/share1'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'export_string'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
op|'{'
string|"'export'"
op|':'
name|'export_string'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
op|'}'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
nl|'\n'
op|'('
string|"'findmnt'"
op|','
string|"'--target'"
op|','
name|'export_mnt_base'
op|','
string|"'--source'"
op|','
nl|'\n'
name|'export_string'
op|')'
op|','
nl|'\n'
op|'('
string|"'umount'"
op|','
name|'export_mnt_base'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_nfs_driver_with_opts
dedent|''
name|'def'
name|'test_libvirt_nfs_driver_with_opts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'nfs'
op|'.'
name|'LibvirtNFSVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'libvirt_utils'
op|','
string|"'is_mounted'"
op|','
name|'lambda'
name|'x'
op|','
name|'d'
op|':'
name|'False'
op|')'
newline|'\n'
name|'export_string'
op|'='
string|"'192.168.1.1:/nfs/share1'"
newline|'\n'
name|'options'
op|'='
string|"'-o intr,nfsvers=3'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'export_string'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
op|'{'
string|"'export'"
op|':'
name|'export_string'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'options'"
op|':'
name|'options'
op|'}'
op|'}'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
nl|'\n'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'export_mnt_base'
op|')'
op|','
nl|'\n'
op|'('
string|"'mount'"
op|','
string|"'-t'"
op|','
string|"'nfs'"
op|','
string|"'-o'"
op|','
string|"'intr,nfsvers=3'"
op|','
nl|'\n'
name|'export_string'
op|','
name|'export_mnt_base'
op|')'
op|','
nl|'\n'
op|'('
string|"'umount'"
op|','
name|'export_mnt_base'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
