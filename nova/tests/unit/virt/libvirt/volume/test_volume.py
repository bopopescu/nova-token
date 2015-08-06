begin_unit
comment|'#    Copyright 2010 OpenStack Foundation'
nl|'\n'
comment|'#    Copyright 2012 University Of Minho'
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
name|'mock'
newline|'\n'
name|'from'
name|'os_brick'
op|'.'
name|'initiator'
name|'import'
name|'connector'
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
name|'test'
newline|'\n'
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
name|'import'
name|'fakelibvirt'
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
name|'host'
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
name|'volume'
newline|'\n'
nl|'\n'
DECL|variable|SECRET_UUID
name|'SECRET_UUID'
op|'='
string|"'2a0a0d6c-babf-454d-b93e-9ac9957b95e0'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeSecret
name|'class'
name|'FakeSecret'
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
name|'uuid'
op|'='
name|'SECRET_UUID'
newline|'\n'
nl|'\n'
DECL|member|getUUIDString
dedent|''
name|'def'
name|'getUUIDString'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|UUIDString
dedent|''
name|'def'
name|'UUIDString'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|setValue
dedent|''
name|'def'
name|'setValue'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'value'
op|'='
name|'value'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|member|getValue
dedent|''
name|'def'
name|'getValue'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'value'
newline|'\n'
nl|'\n'
DECL|member|undefine
dedent|''
name|'def'
name|'undefine'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'value'
op|'='
name|'None'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtVolumeBaseTestCase
dedent|''
dedent|''
name|'class'
name|'LibvirtVolumeBaseTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Contains common setup and helper methods for libvirt volume tests."""'
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
name|'LibvirtVolumeBaseTestCase'
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
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_execute
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'executes'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fakelibvirt'
op|'.'
name|'FakeLibvirtFixture'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeLibvirtDriver
name|'class'
name|'FakeLibvirtDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_host'
op|'='
name|'host'
op|'.'
name|'Host'
op|'('
string|'"qemu:///system"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_all_block_devices
dedent|''
name|'def'
name|'_get_all_block_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'fake_conn'
op|'='
name|'FakeLibvirtDriver'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connr'
op|'='
op|'{'
nl|'\n'
string|"'ip'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'initiator'"
op|':'
string|"'fake_initiator'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'disk_info'
op|'='
op|'{'
nl|'\n'
string|'"bus"'
op|':'
string|'"virtio"'
op|','
nl|'\n'
string|'"dev"'
op|':'
string|'"vde"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"disk"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'self'
op|'.'
name|'location'
op|'='
string|"'10.0.2.15:3260'"
newline|'\n'
name|'self'
op|'.'
name|'iqn'
op|'='
string|"'iqn.2010-10.org.openstack:%s'"
op|'%'
name|'self'
op|'.'
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
string|"'875a8070-d0b9-4949-8b31-104d125c9a64'"
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
string|"'foo'"
newline|'\n'
nl|'\n'
DECL|member|_assertFileTypeEquals
dedent|''
name|'def'
name|'_assertFileTypeEquals'
op|'('
name|'self'
op|','
name|'tree'
op|','
name|'file_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'file'"
op|')'
op|','
name|'file_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtISCSIVolumeBaseTestCase
dedent|''
dedent|''
name|'class'
name|'LibvirtISCSIVolumeBaseTestCase'
op|'('
name|'LibvirtVolumeBaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Contains common setup and helper methods for iSCSI volume tests."""'
newline|'\n'
nl|'\n'
DECL|member|iscsi_connection
name|'def'
name|'iscsi_connection'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'location'
op|','
name|'iqn'
op|','
name|'auth'
op|'='
name|'False'
op|','
nl|'\n'
name|'transport'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_name'
op|'='
string|"'ip-%s-iscsi-%s-lun-1'"
op|'%'
op|'('
name|'location'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'if'
name|'transport'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'dev_name'
op|'='
string|"'pci-0000:00:00.0-'"
op|'+'
name|'dev_name'
newline|'\n'
dedent|''
name|'dev_path'
op|'='
string|"'/dev/disk/by-path/%s'"
op|'%'
op|'('
name|'dev_name'
op|')'
newline|'\n'
name|'ret'
op|'='
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'target_portal'"
op|':'
name|'location'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
name|'iqn'
op|','
nl|'\n'
string|"'target_lun'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'device_path'"
op|':'
name|'dev_path'
op|','
nl|'\n'
string|"'qos_specs'"
op|':'
op|'{'
nl|'\n'
string|"'total_bytes_sec'"
op|':'
string|"'102400'"
op|','
nl|'\n'
string|"'read_iops_sec'"
op|':'
string|"'200'"
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'auth'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_method'"
op|']'
op|'='
string|"'CHAP'"
newline|'\n'
name|'ret'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_username'"
op|']'
op|'='
string|"'foo'"
newline|'\n'
name|'ret'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_password'"
op|']'
op|'='
string|"'bar'"
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtVolumeTestCase
dedent|''
dedent|''
name|'class'
name|'LibvirtVolumeTestCase'
op|'('
name|'LibvirtISCSIVolumeBaseTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_assertDiskInfoEquals
indent|'    '
name|'def'
name|'_assertDiskInfoEquals'
op|'('
name|'self'
op|','
name|'tree'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'device'"
op|')'
op|','
name|'disk_info'
op|'['
string|"'type'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./target'"
op|')'
op|'.'
name|'get'
op|'('
string|"'bus'"
op|')'
op|','
nl|'\n'
name|'disk_info'
op|'['
string|"'bus'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./target'"
op|')'
op|'.'
name|'get'
op|'('
string|"'dev'"
op|')'
op|','
nl|'\n'
name|'disk_info'
op|'['
string|"'dev'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_libvirt_volume_driver_disk_info
dedent|''
name|'def'
name|'_test_libvirt_volume_driver_disk_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'device_path'"
op|':'
string|"'/foo'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'serial'"
op|':'
string|"'fake_serial'"
op|','
nl|'\n'
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
name|'_assertDiskInfoEquals'
op|'('
name|'tree'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_disk_info_type
dedent|''
name|'def'
name|'test_libvirt_volume_disk_info_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'disk_info'
op|'['
string|"'type'"
op|']'
op|'='
string|"'cdrom'"
newline|'\n'
name|'self'
op|'.'
name|'_test_libvirt_volume_driver_disk_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_disk_info_dev
dedent|''
name|'def'
name|'test_libvirt_volume_disk_info_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'disk_info'
op|'['
string|"'dev'"
op|']'
op|'='
string|"'hdc'"
newline|'\n'
name|'self'
op|'.'
name|'_test_libvirt_volume_driver_disk_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_disk_info_bus
dedent|''
name|'def'
name|'test_libvirt_volume_disk_info_bus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'disk_info'
op|'['
string|"'bus'"
op|']'
op|'='
string|"'scsi'"
newline|'\n'
name|'self'
op|'.'
name|'_test_libvirt_volume_driver_disk_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_driver_serial
dedent|''
name|'def'
name|'test_libvirt_volume_driver_serial'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'device_path'"
op|':'
string|"'/foo'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'serial'"
op|':'
string|"'fake_serial'"
op|','
nl|'\n'
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
name|'assertEqual'
op|'('
string|"'block'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake_serial'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./serial'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./blockio'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_driver_blockio
dedent|''
name|'def'
name|'test_libvirt_volume_driver_blockio'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'device_path'"
op|':'
string|"'/foo'"
op|','
nl|'\n'
string|"'logical_block_size'"
op|':'
string|"'4096'"
op|','
nl|'\n'
string|"'physical_block_size'"
op|':'
string|"'4096'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'serial'"
op|':'
string|"'fake_serial'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'disk_info'
op|'='
op|'{'
nl|'\n'
string|'"bus"'
op|':'
string|'"virtio"'
op|','
nl|'\n'
string|'"dev"'
op|':'
string|'"vde"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"disk"'
op|','
nl|'\n'
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
name|'blockio'
op|'='
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./blockio'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'4096'"
op|','
name|'blockio'
op|'.'
name|'get'
op|'('
string|"'logical_block_size'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'4096'"
op|','
name|'blockio'
op|'.'
name|'get'
op|'('
string|"'physical_block_size'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_driver_iotune
dedent|''
name|'def'
name|'test_libvirt_volume_driver_iotune'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|'"device_path"'
op|':'
string|'"/foo"'
op|','
nl|'\n'
string|"'qos_specs'"
op|':'
string|"'bar'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'disk_info'
op|'='
op|'{'
nl|'\n'
string|'"bus"'
op|':'
string|'"virtio"'
op|','
nl|'\n'
string|'"dev"'
op|':'
string|'"vde"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"disk"'
op|','
nl|'\n'
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
name|'iotune'
op|'='
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune'"
op|')'
newline|'\n'
comment|'# ensure invalid qos_specs is ignored'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'iotune'
op|')'
newline|'\n'
nl|'\n'
name|'specs'
op|'='
op|'{'
nl|'\n'
string|"'total_bytes_sec'"
op|':'
string|"'102400'"
op|','
nl|'\n'
string|"'read_bytes_sec'"
op|':'
string|"'51200'"
op|','
nl|'\n'
string|"'write_bytes_sec'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'total_iops_sec'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'read_iops_sec'"
op|':'
string|"'200'"
op|','
nl|'\n'
string|"'write_iops_sec'"
op|':'
string|"'200'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'del'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'qos_specs'"
op|']'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'.'
name|'update'
op|'('
name|'dict'
op|'('
name|'qos_specs'
op|'='
name|'specs'
op|')'
op|')'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
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
name|'assertEqual'
op|'('
string|"'102400'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/total_bytes_sec'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'51200'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/read_bytes_sec'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'0'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/write_bytes_sec'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'0'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/total_iops_sec'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'200'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/read_iops_sec'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'200'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/write_iops_sec'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_driver_readonly
dedent|''
name|'def'
name|'test_libvirt_volume_driver_readonly'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|'"device_path"'
op|':'
string|'"/foo"'
op|','
nl|'\n'
string|"'access_mode'"
op|':'
string|"'bar'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'disk_info'
op|'='
op|'{'
nl|'\n'
string|'"bus"'
op|':'
string|'"virtio"'
op|','
nl|'\n'
string|'"dev"'
op|':'
string|'"vde"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"disk"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolumeAccessMode'
op|','
nl|'\n'
name|'libvirt_driver'
op|'.'
name|'get_config'
op|','
nl|'\n'
name|'connection_info'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'access_mode'"
op|']'
op|'='
string|"'rw'"
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
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
name|'readonly'
op|'='
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./readonly'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'readonly'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'access_mode'"
op|']'
op|'='
string|"'ro'"
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
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
name|'readonly'
op|'='
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./readonly'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'readonly'
op|')'
newline|'\n'
nl|'\n'
DECL|member|iscsi_connection_discovery_chap_enable
dedent|''
name|'def'
name|'iscsi_connection_discovery_chap_enable'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'location'
op|','
name|'iqn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_name'
op|'='
string|"'ip-%s-iscsi-%s-lun-1'"
op|'%'
op|'('
name|'location'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'dev_path'
op|'='
string|"'/dev/disk/by-path/%s'"
op|'%'
op|'('
name|'dev_name'
op|')'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'target_portal'"
op|':'
name|'location'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
name|'iqn'
op|','
nl|'\n'
string|"'target_lun'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'device_path'"
op|':'
name|'dev_path'
op|','
nl|'\n'
string|"'discovery_auth_method'"
op|':'
string|"'CHAP'"
op|','
nl|'\n'
string|"'discovery_auth_username'"
op|':'
string|'"testuser"'
op|','
nl|'\n'
string|"'discovery_auth_password'"
op|':'
string|"'123456'"
op|','
nl|'\n'
string|"'qos_specs'"
op|':'
op|'{'
nl|'\n'
string|"'total_bytes_sec'"
op|':'
string|"'102400'"
op|','
nl|'\n'
string|"'read_iops_sec'"
op|':'
string|"'200'"
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|generate_device
dedent|''
name|'def'
name|'generate_device'
op|'('
name|'self'
op|','
name|'transport'
op|'='
name|'None'
op|','
name|'lun'
op|'='
number|'1'
op|','
name|'short'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_format'
op|'='
string|'"ip-%s-iscsi-%s-lun-%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'location'
op|','
name|'self'
op|'.'
name|'iqn'
op|','
name|'lun'
op|')'
newline|'\n'
name|'if'
name|'transport'
op|':'
newline|'\n'
indent|'            '
name|'dev_format'
op|'='
string|'"pci-0000:00:00.0-"'
op|'+'
name|'dev_format'
newline|'\n'
dedent|''
name|'if'
name|'short'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dev_format'
newline|'\n'
dedent|''
name|'fake_dev_path'
op|'='
string|'"/dev/disk/by-path/"'
op|'+'
name|'dev_format'
newline|'\n'
name|'return'
name|'fake_dev_path'
newline|'\n'
nl|'\n'
DECL|member|test_iscsiadm_discover_parsing
dedent|''
name|'def'
name|'test_iscsiadm_discover_parsing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure that parsing iscsiadm discover ignores cruft.'
nl|'\n'
nl|'\n'
indent|'        '
name|'targets'
op|'='
op|'['
nl|'\n'
op|'['
string|'"192.168.204.82:3260,1"'
op|','
nl|'\n'
op|'('
string|'"iqn.2010-10.org.openstack:volume-"'
nl|'\n'
string|'"f9b12623-6ce3-4dac-a71f-09ad4249bdd3"'
op|')'
op|']'
op|','
nl|'\n'
op|'['
string|'"192.168.204.82:3261,1"'
op|','
nl|'\n'
op|'('
string|'"iqn.2010-10.org.openstack:volume-"'
nl|'\n'
string|'"f9b12623-6ce3-4dac-a71f-09ad4249bdd4"'
op|')'
op|']'
op|']'
newline|'\n'
nl|'\n'
comment|'# This slight wonkiness brought to you by pep8, as the actual'
nl|'\n'
comment|'# example output runs about 97 chars wide.'
nl|'\n'
name|'sample_input'
op|'='
string|'"""Loading iscsi modules: done\nStarting iSCSI initiator service: done\nSetting up iSCSI targets: unused\n%s %s\n%s %s\n"""'
op|'%'
op|'('
name|'targets'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|','
name|'targets'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|','
name|'targets'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|','
name|'targets'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtISCSIVolumeDriver'
op|'('
string|'"none"'
op|')'
newline|'\n'
name|'out'
op|'='
name|'driver'
op|'.'
name|'connector'
op|'.'
name|'_get_target_portals_from_iscsiadm_output'
op|'('
nl|'\n'
name|'sample_input'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'out'
op|','
name|'targets'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_iscsi_driver
dedent|''
name|'def'
name|'test_libvirt_iscsi_driver'
op|'('
name|'self'
op|','
name|'transport'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtISCSIVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'libvirt_driver'
op|'.'
name|'connector'
op|','
nl|'\n'
name|'connector'
op|'.'
name|'ISCSIConnector'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_sanitize_log_run_iscsiadm
dedent|''
name|'def'
name|'test_sanitize_log_run_iscsiadm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Tests that the parameters to the os-brick connector's"
nl|'\n'
comment|'# _run_iscsiadm function are sanitized for passwords when logged.'
nl|'\n'
DECL|function|fake_debug
indent|'        '
name|'def'
name|'fake_debug'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'node.session.auth.password'"
op|','
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'scrubme'"
op|','
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_execute
dedent|''
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtISCSIVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'connector'
op|'.'
name|'set_execute'
op|'('
name|'fake_execute'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'iscsi_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|','
name|'self'
op|'.'
name|'location'
op|','
nl|'\n'
name|'self'
op|'.'
name|'iqn'
op|')'
newline|'\n'
name|'iscsi_properties'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'connector'
op|'.'
name|'LOG'
op|','
string|"'debug'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'fake_debug'
op|')'
name|'as'
name|'debug_mock'
op|':'
newline|'\n'
indent|'            '
name|'libvirt_driver'
op|'.'
name|'connector'
op|'.'
name|'_iscsiadm_update'
op|'('
nl|'\n'
name|'iscsi_properties'
op|','
string|"'node.session.auth.password'"
op|','
string|"'scrubme'"
op|')'
newline|'\n'
nl|'\n'
comment|"# we don't care what the log message is, we just want to make sure"
nl|'\n'
comment|'# our stub method is called which asserts the password is scrubbed'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'debug_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
