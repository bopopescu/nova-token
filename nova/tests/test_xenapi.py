begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nTest suite for XenAPI\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'xenapi_conn'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'fake'
name|'as'
name|'xenapi_fake'
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
op|'.'
name|'vmops'
name|'import'
name|'SimpleDH'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vmops'
name|'import'
name|'VMOps'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'db'
name|'import'
name|'fakes'
name|'as'
name|'db_fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'glance'
name|'import'
name|'stubs'
name|'as'
name|'glance_stubs'
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
DECL|class|XenAPIVolumeTestCase
name|'class'
name|'XenAPIVolumeTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Unit tests for Volume operations\n    """'
newline|'\n'
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
name|'XenAPIVolumeTestCase'
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
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'target_host'
op|'='
string|"'127.0.0.1'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
op|'='
string|"'test_url'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
op|'='
string|"'test_pass'"
newline|'\n'
name|'db_fakes'
op|'.'
name|'stub_out_db_instance_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stub_out_get_target'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'xenapi_fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'values'
op|'='
op|'{'
string|"'name'"
op|':'
number|'1'
op|','
string|"'id'"
op|':'
number|'1'
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
string|"'image_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
string|"'m1.large'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'aa:bb:cc:dd:ee:ff'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_create_volume
dedent|''
name|'def'
name|'_create_volume'
op|'('
name|'self'
op|','
name|'size'
op|'='
string|"'0'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a volume object."""'
newline|'\n'
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'vol'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'host'"
op|']'
op|'='
string|"'localhost'"
newline|'\n'
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
name|'vol'
op|'['
string|"'status'"
op|']'
op|'='
string|'"creating"'
newline|'\n'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'vol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_iscsi_storage
dedent|''
name|'def'
name|'test_create_iscsi_storage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" This shows how to test helper classes\' methods """'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVolumeTests'
op|')'
newline|'\n'
name|'session'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|'('
string|"'test_url'"
op|','
string|"'root'"
op|','
string|"'test_pass'"
op|')'
newline|'\n'
name|'helper'
op|'='
name|'volume_utils'
op|'.'
name|'VolumeHelper'
newline|'\n'
name|'helper'
op|'.'
name|'XenAPI'
op|'='
name|'session'
op|'.'
name|'get_imported_xenapi'
op|'('
op|')'
newline|'\n'
name|'vol'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'info'
op|'='
name|'helper'
op|'.'
name|'parse_volume_info'
op|'('
name|'vol'
op|'['
string|"'id'"
op|']'
op|','
string|"'/dev/sdc'"
op|')'
newline|'\n'
name|'label'
op|'='
string|"'SR-%s'"
op|'%'
name|'vol'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'description'
op|'='
string|"'Test-SR'"
newline|'\n'
name|'sr_ref'
op|'='
name|'helper'
op|'.'
name|'create_iscsi_storage'
op|'('
name|'session'
op|','
name|'info'
op|','
name|'label'
op|','
name|'description'
op|')'
newline|'\n'
name|'srs'
op|'='
name|'xenapi_fake'
op|'.'
name|'get_all'
op|'('
string|"'SR'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sr_ref'
op|','
name|'srs'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parse_volume_info_raise_exception
dedent|''
name|'def'
name|'test_parse_volume_info_raise_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" This shows how to test helper classes\' methods """'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVolumeTests'
op|')'
newline|'\n'
name|'session'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|'('
string|"'test_url'"
op|','
string|"'root'"
op|','
string|"'test_pass'"
op|')'
newline|'\n'
name|'helper'
op|'='
name|'volume_utils'
op|'.'
name|'VolumeHelper'
newline|'\n'
name|'helper'
op|'.'
name|'XenAPI'
op|'='
name|'session'
op|'.'
name|'get_imported_xenapi'
op|'('
op|')'
newline|'\n'
name|'vol'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
comment|'# oops, wrong mount point!'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
nl|'\n'
name|'helper'
op|'.'
name|'parse_volume_info'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'/dev/sd'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume
dedent|''
name|'def'
name|'test_attach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" This shows how to test Ops classes\' methods """'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVolumeTests'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'xenapi_conn'
op|'.'
name|'get_connection'
op|'('
name|'False'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'values'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'xenapi_fake'
op|'.'
name|'create_vm'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
string|"'Running'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'attach_volume'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
string|"'/dev/sdc'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|check
name|'def'
name|'check'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# check that the VM has a VBD attached to it'
nl|'\n'
comment|'# Get XenAPI record for VBD'
nl|'\n'
indent|'            '
name|'vbds'
op|'='
name|'xenapi_fake'
op|'.'
name|'get_all'
op|'('
string|"'VBD'"
op|')'
newline|'\n'
name|'vbd'
op|'='
name|'xenapi_fake'
op|'.'
name|'get_record'
op|'('
string|"'VBD'"
op|','
name|'vbds'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'vm_ref'
op|'='
name|'vbd'
op|'['
string|"'VM'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm_ref'
op|','
name|'vm'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'check'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_raise_exception
dedent|''
name|'def'
name|'test_attach_volume_raise_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" This shows how to test when exceptions are raised """'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
nl|'\n'
name|'stubs'
op|'.'
name|'FakeSessionForVolumeFailedTests'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'xenapi_conn'
op|'.'
name|'get_connection'
op|'('
name|'False'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'values'
op|')'
newline|'\n'
name|'xenapi_fake'
op|'.'
name|'create_vm'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
string|"'Running'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
nl|'\n'
name|'conn'
op|'.'
name|'attach_volume'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'name'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'/dev/sdc'"
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
name|'XenAPIVolumeTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset_network
dedent|''
dedent|''
name|'def'
name|'reset_network'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIVMTestCase
dedent|''
name|'class'
name|'XenAPIVMTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Unit tests for VM operations\n    """'
newline|'\n'
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
name|'XenAPIVMTestCase'
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
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|','
nl|'\n'
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
op|'='
string|"'test_url'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
op|'='
string|"'test_pass'"
newline|'\n'
name|'xenapi_fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'xenapi_fake'
op|'.'
name|'create_local_srs'
op|'('
op|')'
newline|'\n'
name|'db_fakes'
op|'.'
name|'stub_out_db_instance_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'xenapi_fake'
op|'.'
name|'create_network'
op|'('
string|"'fake'"
op|','
name|'FLAGS'
op|'.'
name|'flat_network_bridge'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVMTests'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_get_this_vm_uuid'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_stream_disk'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_lookup_image'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'VMOps'
op|','
string|"'reset_network'"
op|','
name|'reset_network'
op|')'
newline|'\n'
name|'glance_stubs'
op|'.'
name|'stubout_glance_client'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
nl|'\n'
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'xenapi_conn'
op|'.'
name|'get_connection'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_instances_0
dedent|''
name|'def'
name|'test_list_instances_0'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instances'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_diagnostics
dedent|''
name|'def'
name|'test_get_diagnostics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_diagnostics'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_snapshot
dedent|''
name|'def'
name|'test_instance_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stubs'
op|'.'
name|'stubout_instance_snapshot'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'name'
op|'='
string|'"MySnapshot"'
newline|'\n'
name|'template_vm_ref'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'snapshot'
op|'('
name|'instance'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|function|ensure_vm_was_torn_down
name|'def'
name|'ensure_vm_was_torn_down'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vm_labels'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'vm_ref'
name|'in'
name|'xenapi_fake'
op|'.'
name|'get_all'
op|'('
string|"'VM'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'vm_rec'
op|'='
name|'xenapi_fake'
op|'.'
name|'get_record'
op|'('
string|"'VM'"
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'vm_rec'
op|'['
string|'"is_control_domain"'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'vm_labels'
op|'.'
name|'append'
op|'('
name|'vm_rec'
op|'['
string|'"name_label"'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_labels'
op|','
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|ensure_vbd_was_torn_down
dedent|''
name|'def'
name|'ensure_vbd_was_torn_down'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vbd_labels'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'vbd_ref'
name|'in'
name|'xenapi_fake'
op|'.'
name|'get_all'
op|'('
string|"'VBD'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'vbd_rec'
op|'='
name|'xenapi_fake'
op|'.'
name|'get_record'
op|'('
string|"'VBD'"
op|','
name|'vbd_ref'
op|')'
newline|'\n'
name|'vbd_labels'
op|'.'
name|'append'
op|'('
name|'vbd_rec'
op|'['
string|'"vm_name_label"'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vbd_labels'
op|','
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|ensure_vdi_was_torn_down
dedent|''
name|'def'
name|'ensure_vdi_was_torn_down'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'vdi_ref'
name|'in'
name|'xenapi_fake'
op|'.'
name|'get_all'
op|'('
string|"'VDI'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'vdi_rec'
op|'='
name|'xenapi_fake'
op|'.'
name|'get_record'
op|'('
string|"'VDI'"
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'name_label'
op|'='
name|'vdi_rec'
op|'['
string|'"name_label"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'name_label'
op|'.'
name|'endswith'
op|'('
string|"'snapshot'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|check
dedent|''
dedent|''
name|'def'
name|'check'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ensure_vm_was_torn_down'
op|'('
op|')'
newline|'\n'
name|'ensure_vbd_was_torn_down'
op|'('
op|')'
newline|'\n'
name|'ensure_vdi_was_torn_down'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'check'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_vm_record
dedent|''
name|'def'
name|'check_vm_record'
op|'('
name|'self'
op|','
name|'conn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instances'
op|','
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get Nova record for VM'
nl|'\n'
name|'vm_info'
op|'='
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get XenAPI record for VM'
nl|'\n'
name|'vms'
op|'='
op|'['
name|'rec'
name|'for'
name|'ref'
op|','
name|'rec'
nl|'\n'
name|'in'
name|'xenapi_fake'
op|'.'
name|'get_all_records'
op|'('
string|"'VM'"
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'not'
name|'rec'
op|'['
string|"'is_control_domain'"
op|']'
op|']'
newline|'\n'
name|'vm'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Check that m1.large above turned into the right thing.'
nl|'\n'
name|'instance_type'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
string|"'m1.large'"
op|']'
newline|'\n'
name|'mem_kib'
op|'='
name|'long'
op|'('
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|'<<'
number|'10'
newline|'\n'
name|'mem_bytes'
op|'='
name|'str'
op|'('
name|'mem_kib'
op|'<<'
number|'10'
op|')'
newline|'\n'
name|'vcpus'
op|'='
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_info'
op|'['
string|"'max_mem'"
op|']'
op|','
name|'mem_kib'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_info'
op|'['
string|"'mem'"
op|']'
op|','
name|'mem_kib'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'['
string|"'memory_static_max'"
op|']'
op|','
name|'mem_bytes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'['
string|"'memory_dynamic_max'"
op|']'
op|','
name|'mem_bytes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'['
string|"'memory_dynamic_min'"
op|']'
op|','
name|'mem_bytes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'['
string|"'VCPUs_max'"
op|']'
op|','
name|'str'
op|'('
name|'vcpus'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'['
string|"'VCPUs_at_startup'"
op|']'
op|','
name|'str'
op|'('
name|'vcpus'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check that the VM is running according to Nova'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_info'
op|'['
string|"'state'"
op|']'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check that the VM is running according to XenAPI.'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'['
string|"'power_state'"
op|']'
op|','
string|"'Running'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_spawn
dedent|''
name|'def'
name|'_test_spawn'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'kernel_id'
op|','
name|'ramdisk_id'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|'"m1.large"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVMTests'
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'name'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
name|'kernel_id'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'ramdisk_id'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'aa:bb:cc:dd:ee:ff'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'conn'
op|'='
name|'xenapi_conn'
op|'.'
name|'get_connection'
op|'('
name|'False'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'values'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'spawn'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'check_vm_record'
op|'('
name|'conn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_not_enough_memory
dedent|''
name|'def'
name|'test_spawn_not_enough_memory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'glance'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_spawn'
op|','
nl|'\n'
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
string|'"m1.xlarge"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_raw_objectstore
dedent|''
name|'def'
name|'test_spawn_raw_objectstore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'objectstore'"
newline|'\n'
name|'self'
op|'.'
name|'_test_spawn'
op|'('
number|'1'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_objectstore
dedent|''
name|'def'
name|'test_spawn_objectstore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'objectstore'"
newline|'\n'
name|'self'
op|'.'
name|'_test_spawn'
op|'('
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_raw_glance
dedent|''
name|'def'
name|'test_spawn_raw_glance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'glance'"
newline|'\n'
name|'self'
op|'.'
name|'_test_spawn'
op|'('
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_RAW'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_vhd_glance
dedent|''
name|'def'
name|'test_spawn_vhd_glance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'glance'"
newline|'\n'
name|'self'
op|'.'
name|'_test_spawn'
op|'('
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_VHD'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_glance
dedent|''
name|'def'
name|'test_spawn_glance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'glance'"
newline|'\n'
name|'self'
op|'.'
name|'_test_spawn'
op|'('
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_MACHINE'
op|','
nl|'\n'
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_KERNEL'
op|','
nl|'\n'
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_RAMDISK'
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
name|'XenAPIVMTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and spawns a test instance"""'
newline|'\n'
name|'values'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'image_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
string|"'m1.large'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'aa:bb:cc:dd:ee:ff'"
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'spawn'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIDiffieHellmanTestCase
dedent|''
dedent|''
name|'class'
name|'XenAPIDiffieHellmanTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Unit tests for Diffie-Hellman code\n    """'
newline|'\n'
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
name|'XenAPIDiffieHellmanTestCase'
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
name|'alice'
op|'='
name|'SimpleDH'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'bob'
op|'='
name|'SimpleDH'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shared
dedent|''
name|'def'
name|'test_shared'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'alice_pub'
op|'='
name|'self'
op|'.'
name|'alice'
op|'.'
name|'get_public'
op|'('
op|')'
newline|'\n'
name|'bob_pub'
op|'='
name|'self'
op|'.'
name|'bob'
op|'.'
name|'get_public'
op|'('
op|')'
newline|'\n'
name|'alice_shared'
op|'='
name|'self'
op|'.'
name|'alice'
op|'.'
name|'compute_shared'
op|'('
name|'bob_pub'
op|')'
newline|'\n'
name|'bob_shared'
op|'='
name|'self'
op|'.'
name|'bob'
op|'.'
name|'compute_shared'
op|'('
name|'alice_pub'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'alice_shared'
op|','
name|'bob_shared'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_encryption
dedent|''
name|'def'
name|'test_encryption'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
string|'"This is a top-secret message"'
newline|'\n'
name|'enc'
op|'='
name|'self'
op|'.'
name|'alice'
op|'.'
name|'encrypt'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'dec'
op|'='
name|'self'
op|'.'
name|'bob'
op|'.'
name|'decrypt'
op|'('
name|'enc'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'dec'
op|','
name|'msg'
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
name|'XenAPIDiffieHellmanTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIDetermineDiskImageTestCase
dedent|''
dedent|''
name|'class'
name|'XenAPIDetermineDiskImageTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Unit tests for code that detects the ImageType\n    """'
newline|'\n'
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
name|'XenAPIDetermineDiskImageTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'glance_stubs'
op|'.'
name|'stubout_glance_client'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
nl|'\n'
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeInstance
name|'class'
name|'FakeInstance'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fake_instance'
op|'='
name|'FakeInstance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'id'
op|'='
number|'42'
newline|'\n'
nl|'\n'
DECL|member|assert_disk_type
dedent|''
name|'def'
name|'assert_disk_type'
op|'('
name|'self'
op|','
name|'disk_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dt'
op|'='
name|'vm_utils'
op|'.'
name|'VMHelper'
op|'.'
name|'determine_disk_image_type'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'disk_type'
op|','
name|'dt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_disk
dedent|''
name|'def'
name|'test_instance_disk'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        If a kernel is specified then the image type is DISK (aka machine)\n        """'
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'objectstore'"
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'image_id'
op|'='
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_MACHINE'
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'kernel_id'
op|'='
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_KERNEL'
newline|'\n'
name|'self'
op|'.'
name|'assert_disk_type'
op|'('
name|'vm_utils'
op|'.'
name|'ImageType'
op|'.'
name|'DISK'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_disk_raw
dedent|''
name|'def'
name|'test_instance_disk_raw'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        If the kernel isn\'t specified, and we\'re not using Glance, then\n        DISK_RAW is assumed.\n        """'
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'objectstore'"
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'image_id'
op|'='
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_RAW'
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'kernel_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assert_disk_type'
op|'('
name|'vm_utils'
op|'.'
name|'ImageType'
op|'.'
name|'DISK_RAW'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_glance_disk_raw
dedent|''
name|'def'
name|'test_glance_disk_raw'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        If we\'re using Glance, then defer to the image_type field, which in\n        this case will be \'raw\'.\n        """'
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'glance'"
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'image_id'
op|'='
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_RAW'
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'kernel_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assert_disk_type'
op|'('
name|'vm_utils'
op|'.'
name|'ImageType'
op|'.'
name|'DISK_RAW'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_glance_disk_vhd
dedent|''
name|'def'
name|'test_glance_disk_vhd'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        If we\'re using Glance, then defer to the image_type field, which in\n        this case will be \'vhd\'.\n        """'
newline|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_image_service'
op|'='
string|"'glance'"
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'image_id'
op|'='
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|'.'
name|'IMAGE_VHD'
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'.'
name|'kernel_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assert_disk_type'
op|'('
name|'vm_utils'
op|'.'
name|'ImageType'
op|'.'
name|'DISK_VHD'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
