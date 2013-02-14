begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2010 OpenStack LLC'
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
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'blockinfo'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtBlockInfoTest
name|'class'
name|'LibvirtBlockInfoTest'
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
name|'LibvirtBlockInfoTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_instance'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
string|"'32dfcb37-5af1-552b-357c-be8c3aa38310'"
op|','
nl|'\n'
string|"'memory_kb'"
op|':'
string|"'1024000'"
op|','
nl|'\n'
string|"'basepath'"
op|':'
string|"'/some/path'"
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
string|"'br100'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'br101'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
string|"'5'"
op|'}'
comment|'# m1.small'
newline|'\n'
nl|'\n'
DECL|member|test_volume_in_mapping
dedent|''
name|'def'
name|'test_volume_in_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'swap'
op|'='
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'1'
op|'}'
newline|'\n'
name|'ephemerals'
op|'='
op|'['
op|'{'
string|"'num'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc1'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'num'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral2'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdd'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|']'
newline|'\n'
name|'block_device_mapping'
op|'='
op|'['
op|'{'
string|"'mount_device'"
op|':'
string|"'/dev/sde'"
op|','
nl|'\n'
string|"'device_path'"
op|':'
string|"'fake_device'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'mount_device'"
op|':'
string|"'/dev/sdf'"
op|','
nl|'\n'
string|"'device_path'"
op|':'
string|"'fake_device'"
op|'}'
op|']'
newline|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda'"
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'swap'
op|','
nl|'\n'
string|"'ephemerals'"
op|':'
name|'ephemerals'
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
name|'block_device_mapping'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_assert_volume_in_mapping
name|'def'
name|'_assert_volume_in_mapping'
op|'('
name|'device_name'
op|','
name|'true_or_false'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'block_device'
op|'.'
name|'volume_in_mapping'
op|'('
name|'device_name'
op|','
nl|'\n'
name|'block_device_info'
op|')'
op|','
nl|'\n'
name|'true_or_false'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_assert_volume_in_mapping'
op|'('
string|"'sda'"
op|','
name|'False'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdb'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdc1'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdd'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sde'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdf'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdg'"
op|','
name|'False'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdh1'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_disk_dev
dedent|''
name|'def'
name|'test_find_disk_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
op|'{'
nl|'\n'
string|'"disk.local"'
op|':'
op|'{'
nl|'\n'
string|"'dev'"
op|':'
string|"'sda'"
op|','
nl|'\n'
string|"'bus'"
op|':'
string|"'scsi'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'disk'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"disk.swap"'
op|':'
op|'{'
nl|'\n'
string|"'dev'"
op|':'
string|"'sdc'"
op|','
nl|'\n'
string|"'bus'"
op|':'
string|"'scsi'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'disk'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'dev'
op|'='
name|'blockinfo'
op|'.'
name|'find_disk_dev_for_disk_bus'
op|'('
name|'mapping'
op|','
string|"'scsi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dev'
op|','
string|"'sdb'"
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'='
name|'blockinfo'
op|'.'
name|'find_disk_dev_for_disk_bus'
op|'('
name|'mapping'
op|','
string|"'scsi'"
op|','
nl|'\n'
name|'last_device'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dev'
op|','
string|"'sdz'"
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'='
name|'blockinfo'
op|'.'
name|'find_disk_dev_for_disk_bus'
op|'('
name|'mapping'
op|','
string|"'virtio'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dev'
op|','
string|"'vda'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_next_disk_dev
dedent|''
name|'def'
name|'test_get_next_disk_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'mapping'
op|'['
string|"'disk.local'"
op|']'
op|'='
name|'blockinfo'
op|'.'
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
string|"'virtio'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|'['
string|"'disk.local'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mapping'
op|'['
string|"'disk.swap'"
op|']'
op|'='
name|'blockinfo'
op|'.'
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
string|"'virtio'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|'['
string|"'disk.swap'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mapping'
op|'['
string|"'disk.config'"
op|']'
op|'='
name|'blockinfo'
op|'.'
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
string|"'ide'"
op|','
nl|'\n'
string|"'cdrom'"
op|','
nl|'\n'
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|'['
string|"'disk.config'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'dev'"
op|':'
string|"'hdd'"
op|','
string|"'bus'"
op|':'
string|"'ide'"
op|','
string|"'type'"
op|':'
string|"'cdrom'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_simple
dedent|''
name|'def'
name|'test_get_disk_mapping_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# The simplest possible disk mapping setup, all defaults'
nl|'\n'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.local'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_simple_rootdev
dedent|''
name|'def'
name|'test_get_disk_mapping_simple_rootdev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A simple disk mapping setup, but with custom root device name'
nl|'\n'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'scsi'"
op|','
string|"'dev'"
op|':'
string|"'sda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.local'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'scsi'"
op|','
string|"'dev'"
op|':'
string|"'sda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_rescue
dedent|''
name|'def'
name|'test_get_disk_mapping_rescue'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A simple disk mapping setup, but in rescue mode'
nl|'\n'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'rescue'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk.rescue'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_simple_iso
dedent|''
name|'def'
name|'test_get_disk_mapping_simple_iso'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A simple disk mapping setup, but with a ISO for root device'
nl|'\n'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
name|'image_meta'
op|'='
op|'{'
string|"'disk_format'"
op|':'
string|"'iso'"
op|'}'
newline|'\n'
nl|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'ide'"
op|','
string|"'dev'"
op|':'
string|"'hda'"
op|','
string|"'type'"
op|':'
string|"'cdrom'"
op|'}'
op|','
nl|'\n'
string|"'disk.local'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'ide'"
op|','
string|"'dev'"
op|':'
string|"'hda'"
op|','
string|"'type'"
op|':'
string|"'cdrom'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_simple_swap
dedent|''
name|'def'
name|'test_get_disk_mapping_simple_swap'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A simple disk mapping setup, but with a swap device added'
nl|'\n'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
name|'instance_ref'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'swap'"
op|']'
op|'='
number|'5'
newline|'\n'
nl|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.local'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.swap'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdc'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_simple_configdrive
dedent|''
name|'def'
name|'test_get_disk_mapping_simple_configdrive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A simple disk mapping setup, but with configdrive added'
nl|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'force_config_drive'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.local'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.config'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdz'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_ephemeral
dedent|''
name|'def'
name|'test_get_disk_mapping_ephemeral'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A disk mapping with ephemeral devices'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
name|'instance_ref'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'swap'"
op|']'
op|'='
number|'5'
newline|'\n'
nl|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'ephemerals'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'num'"
op|':'
number|'0'
op|','
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdb'"
op|','
string|"'size'"
op|':'
number|'10'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'num'"
op|':'
number|'1'
op|','
string|"'virtual_name'"
op|':'
string|"'ephemeral1'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdc'"
op|','
string|"'size'"
op|':'
number|'10'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'num'"
op|':'
number|'2'
op|','
string|"'virtual_name'"
op|':'
string|"'ephemeral2'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdd'"
op|','
string|"'size'"
op|':'
number|'10'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.eph0'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.eph1'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdc'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.eph2'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdd'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.swap'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vde'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_custom_swap
dedent|''
name|'def'
name|'test_get_disk_mapping_custom_swap'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A disk mapping with a swap device at position vdb. This'
nl|'\n'
comment|'# should cause disk.local to be removed'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'swap'"
op|':'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/vdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'10'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.swap'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_blockdev_root
dedent|''
name|'def'
name|'test_get_disk_mapping_blockdev_root'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A disk mapping with a blockdev replacing the default root'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'block_device_mapping'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
string|'"fake"'
op|','
nl|'\n'
string|"'mount_device'"
op|':'
string|'"/dev/vda"'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'/dev/vda'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.local'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_blockdev_eph
dedent|''
name|'def'
name|'test_get_disk_mapping_blockdev_eph'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A disk mapping with a blockdev replacing the ephemeral device'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'block_device_mapping'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
string|'"fake"'
op|','
nl|'\n'
string|"'mount_device'"
op|':'
string|'"/dev/vdb"'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'/dev/vdb'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_blockdev_many
dedent|''
name|'def'
name|'test_get_disk_mapping_blockdev_many'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# A disk mapping with a blockdev replacing all devices'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'block_device_mapping'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
string|'"fake"'
op|','
nl|'\n'
string|"'mount_device'"
op|':'
string|'"/dev/vda"'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
string|'"fake"'
op|','
nl|'\n'
string|"'mount_device'"
op|':'
string|'"/dev/vdb"'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
string|'"fake"'
op|','
nl|'\n'
string|"'mount_device'"
op|':'
string|'"/dev/vdc"'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'/dev/vda'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'/dev/vdb'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'/dev/vdc'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdc'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_mapping_complex
dedent|''
name|'def'
name|'test_get_disk_mapping_complex'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# The strangest possible disk mapping setup'
nl|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'user_context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|')'
newline|'\n'
nl|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/vdf'"
op|','
nl|'\n'
string|"'swap'"
op|':'
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/vdy'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'10'
op|'}'
op|','
nl|'\n'
string|"'ephemerals'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'num'"
op|':'
number|'0'
op|','
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdb'"
op|','
string|"'size'"
op|':'
number|'10'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'num'"
op|':'
number|'1'
op|','
string|"'virtual_name'"
op|':'
string|"'ephemeral1'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdc'"
op|','
string|"'size'"
op|':'
number|'10'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
string|'"fake"'
op|','
nl|'\n'
string|"'mount_device'"
op|':'
string|'"/dev/vda"'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'mapping'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_mapping'
op|'('
string|'"kvm"'
op|','
name|'instance_ref'
op|','
nl|'\n'
string|'"virtio"'
op|','
string|'"ide"'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'expect'
op|'='
op|'{'
nl|'\n'
string|"'disk'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdf'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'/dev/vda'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vda'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.eph0'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdb'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.eph1'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdc'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'disk.swap'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdy'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
op|','
nl|'\n'
string|"'root'"
op|':'
op|'{'
string|"'bus'"
op|':'
string|"'virtio'"
op|','
string|"'dev'"
op|':'
string|"'vdf'"
op|','
string|"'type'"
op|':'
string|"'disk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mapping'
op|','
name|'expect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_disk_bus
dedent|''
name|'def'
name|'test_get_disk_bus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bus'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_bus_for_device_type'
op|'('
string|"'kvm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bus'
op|','
string|"'virtio'"
op|')'
newline|'\n'
nl|'\n'
name|'bus'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_bus_for_device_type'
op|'('
string|"'kvm'"
op|','
nl|'\n'
name|'device_type'
op|'='
string|"'cdrom'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bus'
op|','
string|"'ide'"
op|')'
newline|'\n'
nl|'\n'
name|'image_meta'
op|'='
op|'{'
string|"'properties'"
op|':'
op|'{'
string|"'disk_bus'"
op|':'
string|"'scsi'"
op|'}'
op|'}'
newline|'\n'
name|'bus'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_bus_for_device_type'
op|'('
string|"'kvm'"
op|','
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bus'
op|','
string|"'scsi'"
op|')'
newline|'\n'
nl|'\n'
name|'image_meta'
op|'='
op|'{'
string|"'properties'"
op|':'
op|'{'
string|"'disk_bus'"
op|':'
string|"'usb'"
op|','
nl|'\n'
string|"'cdrom_bus'"
op|':'
string|"'scsi'"
op|'}'
op|'}'
newline|'\n'
name|'bus'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_bus_for_device_type'
op|'('
string|"'kvm'"
op|','
nl|'\n'
name|'image_meta'
op|','
nl|'\n'
name|'device_type'
op|'='
string|"'cdrom'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bus'
op|','
string|"'scsi'"
op|')'
newline|'\n'
nl|'\n'
name|'bus'
op|'='
name|'blockinfo'
op|'.'
name|'get_disk_bus_for_device_type'
op|'('
string|"'kvm'"
op|','
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bus'
op|','
string|"'usb'"
op|')'
newline|'\n'
nl|'\n'
name|'image_meta'
op|'='
op|'{'
string|"'properties'"
op|':'
op|'{'
string|"'disk_bus'"
op|':'
string|"'xen'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'UnsupportedHardware'
op|','
nl|'\n'
name|'blockinfo'
op|'.'
name|'get_disk_bus_for_device_type'
op|','
nl|'\n'
string|"'kvm'"
op|','
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
