begin_unit
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'fixtures'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'mox3'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'import'
name|'fake_instance'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'utils'
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
name|'vmwareapi'
name|'import'
name|'fake'
name|'as'
name|'vmwareapi_fake'
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
name|'vmwareapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'uuidsentinel'
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
name|'vmwareapi'
name|'import'
name|'driver'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vmops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfigDriveTestCase
name|'class'
name|'ConfigDriveTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|REQUIRES_LOCKING
indent|'    '
name|'REQUIRES_LOCKING'
op|'='
name|'True'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'driver'
op|'.'
name|'VMwareVCDriver'
op|','
string|"'_register_openstack_extension'"
op|')'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|','
name|'mock_register'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConfigDriveTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'vm_util'
op|'.'
name|'vm_refs_cache_reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'is_admin'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'cluster_name'
op|'='
string|"'test_cluster'"
op|','
nl|'\n'
name|'host_ip'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'host_username'
op|'='
string|"'test_username'"
op|','
nl|'\n'
name|'host_password'
op|'='
string|"'test_pass'"
op|','
nl|'\n'
name|'use_linked_clone'
op|'='
name|'False'
op|','
name|'group'
op|'='
string|"'vmware'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enabled'
op|'='
name|'False'
op|','
name|'group'
op|'='
string|"'vnc'"
op|')'
newline|'\n'
name|'vmwareapi_fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'set_stubs'
op|'('
name|'self'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'driver'
op|'.'
name|'VMwareVCDriver'
op|'('
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_info'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'node_name'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'_nodename'
newline|'\n'
name|'image_ref'
op|'='
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'instance_values'
op|'='
op|'{'
nl|'\n'
string|"'vm_state'"
op|':'
string|"'building'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'mac_addresses'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
string|"'de:ad:be:ef:be:ef'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'8192'
op|','
nl|'\n'
string|"'flavor'"
op|':'
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'vcpus'
op|'='
number|'4'
op|','
name|'extra_specs'
op|'='
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'80'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_ref'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
op|','
nl|'\n'
string|"'task_state'"
op|':'
string|"'scheduling'"
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
string|"'r-3t8muvr0'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'uuidsentinel'
op|'.'
name|'foo'
op|','
nl|'\n'
string|"'node'"
op|':'
name|'self'
op|'.'
name|'node_name'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'expected_attrs'"
op|':'
op|'['
string|"'system_metadata'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'test_instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'**'
name|'instance_values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_instance'
op|'.'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'vcpus'
op|'='
number|'4'
op|','
name|'memory_mb'
op|'='
number|'8192'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'swap'
op|'='
number|'0'
op|','
nl|'\n'
name|'extra_specs'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
nl|'\n'
name|'image_ref'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image'
op|'='
name|'objects'
op|'.'
name|'ImageMeta'
op|'.'
name|'from_dict'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'image_ref'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'size'"
op|':'
name|'int'
op|'('
name|'metadata'
op|'['
string|"'size'"
op|']'
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeInstanceMetadata
name|'class'
name|'FakeInstanceMetadata'
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
op|','
name|'instance'
op|','
name|'content'
op|'='
name|'None'
op|','
name|'extra_md'
op|'='
name|'None'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|metadata_for_config_drive
dedent|''
name|'def'
name|'metadata_for_config_drive'
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
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.api.metadata.base.InstanceMetadata'"
op|','
nl|'\n'
name|'FakeInstanceMetadata'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_make_drive
name|'def'
name|'fake_make_drive'
op|'('
name|'_self'
op|','
name|'_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
comment|"# We can't actually make a config drive v2 because ensure_tree has"
nl|'\n'
comment|'# been faked out'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.virt.configdrive.ConfigDriveBuilder.make_drive'"
op|','
nl|'\n'
name|'fake_make_drive'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_upload_iso_to_datastore
name|'def'
name|'fake_upload_iso_to_datastore'
op|'('
name|'iso_path'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.virt.vmwareapi.images.upload_iso_to_datastore'"
op|','
nl|'\n'
name|'fake_upload_iso_to_datastore'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConfigDriveTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'vmwareapi_fake'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService_reset'
op|'('
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
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|','
string|"'_get_instance_metadata'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_metadata'"
op|')'
newline|'\n'
DECL|member|_spawn_vm
name|'def'
name|'_spawn_vm'
op|'('
name|'self'
op|','
name|'fake_get_instance_meta'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'injected_files'
op|'='
name|'injected_files'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'test_instance'
op|','
name|'self'
op|'.'
name|'image'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'self'
op|'.'
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vm_with_config_drive_verify_method_invocation
dedent|''
name|'def'
name|'test_create_vm_with_config_drive_verify_method_invocation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_instance'
op|'.'
name|'config_drive'
op|'='
string|"'True'"
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|','
string|"'_create_config_drive'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|','
string|"'_attach_cdrom_to_vm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'_vmops'
op|'.'
name|'_create_config_drive'
op|'('
name|'self'
op|'.'
name|'test_instance'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'[ds1] fake.iso'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'_vmops'
op|'.'
name|'_attach_cdrom_to_vm'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
comment|'# if spawn does not call the _create_config_drive or'
nl|'\n'
comment|'# _attach_cdrom_to_vm call with the correct set of parameters'
nl|'\n'
comment|"# then mox's VerifyAll will throw a Expected methods never called"
nl|'\n'
comment|'# Exception'
nl|'\n'
name|'self'
op|'.'
name|'_spawn_vm'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vm_without_config_drive
dedent|''
name|'def'
name|'test_create_vm_without_config_drive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_instance'
op|'.'
name|'config_drive'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|','
string|"'_create_config_drive'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|','
string|"'_attach_cdrom_to_vm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
comment|'# if spawn ends up calling _create_config_drive or'
nl|'\n'
comment|'# _attach_cdrom_to_vm then mox will log a Unexpected method call'
nl|'\n'
comment|'# exception'
nl|'\n'
name|'self'
op|'.'
name|'_spawn_vm'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vm_with_config_drive
dedent|''
name|'def'
name|'test_create_vm_with_config_drive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_instance'
op|'.'
name|'config_drive'
op|'='
string|"'True'"
newline|'\n'
name|'self'
op|'.'
name|'_spawn_vm'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
