begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""Tests for baremetal volume driver."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'volume_driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'volume'
name|'as'
name|'libvirt_volume'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
name|'SHOW_OUTPUT'
op|'='
string|'"""Target 1: iqn.2010-10.org.openstack:volume-00000001\n    System information:\n        Driver: iscsi\n        State: ready\n    I_T nexus information:\n        I_T nexus: 8\n            Initiator: iqn.1993-08.org.debian:01:7780c6a16b4\n            Connection: 0\n                IP Address: 172.17.12.10\n    LUN information:\n        LUN: 0\n            Type: controller\n            SCSI ID: IET     00010000\n            SCSI SN: beaf10\n            Size: 0 MB, Block size: 1\n            Online: Yes\n            Removable media: No\n            Readonly: No\n            Backing store type: null\n            Backing store path: None\n            Backing store flags:\n        LUN: 1\n            Type: disk\n            SCSI ID: IET     00010001\n            SCSI SN: beaf11\n            Size: 1074 MB, Block size: 512\n            Online: Yes\n            Removable media: No\n            Readonly: No\n            Backing store type: rdwr\n            Backing store path: /dev/nova-volumes/volume-00000001\n            Backing store flags:\n    Account information:\n    ACL information:\n        ALL\nTarget 2: iqn.2010-10.org.openstack:volume-00000002\n    System information:\n        Driver: iscsi\n        State: ready\n    I_T nexus information:\n    LUN information:\n        LUN: 0\n            Type: controller\n            SCSI ID: IET     00020000\n            SCSI SN: beaf20\n            Size: 0 MB, Block size: 1\n            Online: Yes\n            Removable media: No\n            Readonly: No\n            Backing store type: null\n            Backing store path: None\n            Backing store flags:\n        LUN: 1\n            Type: disk\n            SCSI ID: IET     00020001\n            SCSI SN: beaf21\n            Size: 2147 MB, Block size: 512\n            Online: Yes\n            Removable media: No\n            Readonly: No\n            Backing store type: rdwr\n            Backing store path: /dev/nova-volumes/volume-00000002\n            Backing store flags:\n    Account information:\n    ACL information:\n        ALL\nTarget 1000001: iqn.2010-10.org.openstack.baremetal:1000001-dev.vdc\n    System information:\n        Driver: iscsi\n        State: ready\n    I_T nexus information:\n    LUN information:\n        LUN: 0\n            Type: controller\n            SCSI ID: IET     f42410000\n            SCSI SN: beaf10000010\n            Size: 0 MB, Block size: 1\n            Online: Yes\n            Removable media: No\n            Readonly: No\n            Backing store type: null\n            Backing store path: None\n            Backing store flags:\n        LUN: 1\n            Type: disk\n            SCSI ID: IET     f42410001\n            SCSI SN: beaf10000011\n            Size: 1074 MB, Block size: 512\n            Online: Yes\n            Removable media: No\n            Readonly: No\n            Backing store type: rdwr\n            Backing store path: /dev/disk/by-path/ip-172.17.12.10:3260-iscsi-\\\niqn.2010-10.org.openstack:volume-00000001-lun-1\n            Backing store flags:\n    Account information:\n    ACL information:\n        ALL\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_show_tgtadm
name|'def'
name|'fake_show_tgtadm'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'SHOW_OUTPUT'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalVolumeTestCase
dedent|''
name|'class'
name|'BareMetalVolumeTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
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
name|'BareMetalVolumeTestCase'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_driver'
op|','
string|"'_show_tgtadm'"
op|','
name|'fake_show_tgtadm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_backingstore_path
dedent|''
name|'def'
name|'test_list_backingstore_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'l'
op|'='
name|'volume_driver'
op|'.'
name|'_list_backingstore_path'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'l'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'/dev/nova-volumes/volume-00000001'"
op|','
name|'l'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'/dev/nova-volumes/volume-00000002'"
op|','
name|'l'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'/dev/disk/by-path/ip-172.17.12.10:3260-iscsi-'"
nl|'\n'
string|"'iqn.2010-10.org.openstack:volume-00000001-lun-1'"
op|','
name|'l'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_next_tid
dedent|''
name|'def'
name|'test_get_next_tid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tid'
op|'='
name|'volume_driver'
op|'.'
name|'_get_next_tid'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1000002'
op|','
name|'tid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_tid_found
dedent|''
name|'def'
name|'test_find_tid_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tid'
op|'='
name|'volume_driver'
op|'.'
name|'_find_tid'
op|'('
nl|'\n'
string|"'iqn.2010-10.org.openstack.baremetal:1000001-dev.vdc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1000001'
op|','
name|'tid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_tid_not_found
dedent|''
name|'def'
name|'test_find_tid_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tid'
op|'='
name|'volume_driver'
op|'.'
name|'_find_tid'
op|'('
nl|'\n'
string|"'iqn.2010-10.org.openstack.baremetal:1000002-dev.vdc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'tid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_iqn
dedent|''
name|'def'
name|'test_get_iqn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'iscsi_iqn_prefix'
op|'='
string|"'iqn.2012-12.a.b'"
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'iqn'
op|'='
name|'volume_driver'
op|'.'
name|'_get_iqn'
op|'('
string|"'instname'"
op|','
string|"'/dev/vdx'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'iqn.2012-12.a.b:instname-dev-vdx'"
op|','
name|'iqn'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalLibVirtVolumeDriverTestCase
dedent|''
dedent|''
name|'class'
name|'BareMetalLibVirtVolumeDriverTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
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
name|'BareMetalLibVirtVolumeDriverTestCase'
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
name|'flags'
op|'('
name|'volume_drivers'
op|'='
op|'['
nl|'\n'
string|"'fake=nova.virt.libvirt.volume.LibvirtFakeVolumeDriver'"
op|','
nl|'\n'
string|"'fake2=nova.virt.libvirt.volume.LibvirtFakeVolumeDriver'"
op|','
nl|'\n'
op|']'
op|','
name|'group'
op|'='
string|"'libvirt'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'volume_driver'
op|'.'
name|'LibvirtVolumeDriver'
op|'('
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'disk_info'
op|'='
op|'{'
nl|'\n'
string|"'dev'"
op|':'
string|"'vdc'"
op|','
nl|'\n'
string|"'bus'"
op|':'
string|"'baremetal'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'baremetal'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'connection_info'
op|'='
op|'{'
string|"'driver_volume_type'"
op|':'
string|"'fake'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_init_loads_volume_drivers
dedent|''
name|'def'
name|'test_init_loads_volume_drivers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'type'
op|'('
name|'self'
op|'.'
name|'driver'
op|'.'
name|'volume_drivers'
op|'['
string|"'fake'"
op|']'
op|')'
op|','
nl|'\n'
name|'libvirt_volume'
op|'.'
name|'LibvirtFakeVolumeDriver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'type'
op|'('
name|'self'
op|'.'
name|'driver'
op|'.'
name|'volume_drivers'
op|'['
string|"'fake2'"
op|']'
op|')'
op|','
nl|'\n'
name|'libvirt_volume'
op|'.'
name|'LibvirtFakeVolumeDriver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'driver'
op|'.'
name|'volume_drivers'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fake_connect_volume
dedent|''
name|'def'
name|'test_fake_connect_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check connect_volume returns without exceptions."""'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_volume_driver_method'
op|'('
string|"'connect_volume'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'connection_info'
op|','
nl|'\n'
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
