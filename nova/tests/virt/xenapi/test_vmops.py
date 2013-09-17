begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 OpenStack Foundation'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_mode'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
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
name|'xenapi'
name|'import'
name|'driver'
name|'as'
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
name|'vm_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vmops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMOpsTestBase
name|'class'
name|'VMOpsTestBase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBase'
op|')'
op|':'
newline|'\n'
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
name|'VMOpsTestBase'
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
name|'_setup_mock_vmops'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vms'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_setup_mock_vmops
dedent|''
name|'def'
name|'_setup_mock_vmops'
op|'('
name|'self'
op|','
name|'product_brand'
op|'='
name|'None'
op|','
name|'product_version'
op|'='
name|'None'
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
name|'xenapi_fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|'('
string|"'test_url'"
op|','
string|"'root'"
op|','
nl|'\n'
string|"'test_pass'"
op|','
nl|'\n'
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vmops'
op|'='
name|'vmops'
op|'.'
name|'VMOps'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_vm
dedent|''
name|'def'
name|'create_vm'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'state'
op|'='
string|'"running"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_ref'
op|'='
name|'xenapi_fake'
op|'.'
name|'create_vm'
op|'('
name|'name'
op|','
name|'state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vms'
op|'.'
name|'append'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'vm'
op|'='
name|'xenapi_fake'
op|'.'
name|'get_record'
op|'('
string|'"VM"'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'return'
name|'vm'
op|','
name|'vm_ref'
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
name|'VMOpsTestBase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'for'
name|'vm'
name|'in'
name|'self'
op|'.'
name|'vms'
op|':'
newline|'\n'
indent|'            '
name|'xenapi_fake'
op|'.'
name|'destroy_vm'
op|'('
name|'vm'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMOpsTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'VMOpsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'VMOpsTestCase'
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
name|'_setup_mock_vmops'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_mock_vmops
dedent|''
name|'def'
name|'_setup_mock_vmops'
op|'('
name|'self'
op|','
name|'product_brand'
op|'='
name|'None'
op|','
name|'product_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'self'
op|'.'
name|'_get_mock_session'
op|'('
name|'product_brand'
op|','
name|'product_version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'vmops'
op|'.'
name|'VMOps'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_mock_session
dedent|''
name|'def'
name|'_get_mock_session'
op|'('
name|'self'
op|','
name|'product_brand'
op|','
name|'product_version'
op|')'
op|':'
newline|'\n'
DECL|class|Mock
indent|'        '
name|'class'
name|'Mock'
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
name|'mock_session'
op|'='
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_session'
op|'.'
name|'product_brand'
op|'='
name|'product_brand'
newline|'\n'
name|'mock_session'
op|'.'
name|'product_version'
op|'='
name|'product_version'
newline|'\n'
name|'return'
name|'mock_session'
newline|'\n'
nl|'\n'
DECL|member|test_check_resize_func_name_defaults_to_VDI_resize
dedent|''
name|'def'
name|'test_check_resize_func_name_defaults_to_VDI_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
string|"'VDI.resize'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'check_resize_func_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_finish_revert_migration_after_crash
dedent|''
name|'def'
name|'_test_finish_revert_migration_after_crash'
op|'('
name|'self'
op|','
name|'backup_made'
op|','
name|'new_made'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'lookup'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'_vmops'
op|','
string|"'_destroy'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'set_vm_name_label'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'_vmops'
op|','
string|"'_attach_mapped_block_devices'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'_vmops'
op|','
string|"'_start'"
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|"'foo-orig'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'backup_made'
name|'and'
string|"'foo'"
name|'or'
name|'None'
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|"'foo'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'('
name|'not'
name|'backup_made'
name|'or'
name|'new_made'
op|')'
name|'and'
string|"'foo'"
name|'or'
name|'None'
op|')'
newline|'\n'
name|'if'
name|'backup_made'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'new_made'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_destroy'
op|'('
name|'instance'
op|','
string|"'foo'"
op|')'
newline|'\n'
dedent|''
name|'vm_utils'
op|'.'
name|'set_vm_name_label'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|"'foo'"
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_attach_mapped_block_devices'
op|'('
name|'instance'
op|','
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_start'
op|'('
name|'instance'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'finish_revert_migration'
op|'('
name|'instance'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_finish_revert_migration_after_crash
dedent|''
name|'def'
name|'test_finish_revert_migration_after_crash'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_finish_revert_migration_after_crash'
op|'('
name|'True'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_finish_revert_migration_after_crash_before_new
dedent|''
name|'def'
name|'test_finish_revert_migration_after_crash_before_new'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_finish_revert_migration_after_crash'
op|'('
name|'True'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_finish_revert_migration_after_crash_before_backup
dedent|''
name|'def'
name|'test_finish_revert_migration_after_crash_before_backup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_finish_revert_migration_after_crash'
op|'('
name|'False'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_determine_vm_mode_returns_xen
dedent|''
name|'def'
name|'test_determine_vm_mode_returns_xen'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_mode'
op|','
string|"'get_from_instance'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
string|'"instance"'
newline|'\n'
name|'vm_mode'
op|'.'
name|'get_from_instance'
op|'('
name|'fake_instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vm_mode'
op|'.'
name|'XEN'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_mode'
op|'.'
name|'XEN'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_determine_vm_mode'
op|'('
name|'fake_instance'
op|','
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_determine_vm_mode_returns_hvm
dedent|''
name|'def'
name|'test_determine_vm_mode_returns_hvm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_mode'
op|','
string|"'get_from_instance'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
string|'"instance"'
newline|'\n'
name|'vm_mode'
op|'.'
name|'get_from_instance'
op|'('
name|'fake_instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vm_mode'
op|'.'
name|'HVM'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_mode'
op|'.'
name|'HVM'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_determine_vm_mode'
op|'('
name|'fake_instance'
op|','
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_determine_vm_mode_returns_is_pv
dedent|''
name|'def'
name|'test_determine_vm_mode_returns_is_pv'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_mode'
op|','
string|"'get_from_instance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'determine_is_pv'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
op|'{'
string|'"os_type"'
op|':'
string|'"foo"'
op|'}'
newline|'\n'
name|'fake_vdis'
op|'='
op|'{'
string|"'root'"
op|':'
op|'{'
string|'"ref"'
op|':'
string|"'fake'"
op|'}'
op|'}'
newline|'\n'
name|'fake_disk_type'
op|'='
string|'"disk"'
newline|'\n'
name|'vm_mode'
op|'.'
name|'get_from_instance'
op|'('
name|'fake_instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'determine_is_pv'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|'"fake"'
op|','
name|'fake_disk_type'
op|','
nl|'\n'
string|'"foo"'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_mode'
op|'.'
name|'XEN'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_determine_vm_mode'
op|'('
name|'fake_instance'
op|','
name|'fake_vdis'
op|','
nl|'\n'
name|'fake_disk_type'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_determine_vm_mode_returns_is_not_pv
dedent|''
name|'def'
name|'test_determine_vm_mode_returns_is_not_pv'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_mode'
op|','
string|"'get_from_instance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'determine_is_pv'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
op|'{'
string|'"os_type"'
op|':'
string|'"foo"'
op|'}'
newline|'\n'
name|'fake_vdis'
op|'='
op|'{'
string|"'root'"
op|':'
op|'{'
string|'"ref"'
op|':'
string|"'fake'"
op|'}'
op|'}'
newline|'\n'
name|'fake_disk_type'
op|'='
string|'"disk"'
newline|'\n'
name|'vm_mode'
op|'.'
name|'get_from_instance'
op|'('
name|'fake_instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'determine_is_pv'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|'"fake"'
op|','
name|'fake_disk_type'
op|','
nl|'\n'
string|'"foo"'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_mode'
op|'.'
name|'HVM'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_determine_vm_mode'
op|'('
name|'fake_instance'
op|','
name|'fake_vdis'
op|','
nl|'\n'
name|'fake_disk_type'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_determine_vm_mode_returns_is_not_pv_no_root_disk
dedent|''
name|'def'
name|'test_determine_vm_mode_returns_is_not_pv_no_root_disk'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_mode'
op|','
string|"'get_from_instance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'determine_is_pv'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_instance'
op|'='
op|'{'
string|'"os_type"'
op|':'
string|'"foo"'
op|'}'
newline|'\n'
name|'fake_vdis'
op|'='
op|'{'
string|"'iso'"
op|':'
op|'{'
string|'"ref"'
op|':'
string|"'fake'"
op|'}'
op|'}'
newline|'\n'
name|'fake_disk_type'
op|'='
string|'"disk"'
newline|'\n'
name|'vm_mode'
op|'.'
name|'get_from_instance'
op|'('
name|'fake_instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm_mode'
op|'.'
name|'HVM'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_determine_vm_mode'
op|'('
name|'fake_instance'
op|','
name|'fake_vdis'
op|','
nl|'\n'
name|'fake_disk_type'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_xsm_sr_check_relaxed_cached
dedent|''
name|'def'
name|'test_xsm_sr_check_relaxed_cached'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'make_plugin_call_count'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|function|fake_make_plugin_call
name|'def'
name|'fake_make_plugin_call'
op|'('
name|'plugin'
op|','
name|'method'
op|','
op|'**'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'make_plugin_call_count'
op|'='
name|'self'
op|'.'
name|'make_plugin_call_count'
op|'+'
number|'1'
newline|'\n'
name|'return'
string|'"true"'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'_vmops'
op|','
string|'"_make_plugin_call"'
op|','
nl|'\n'
name|'fake_make_plugin_call'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_is_xsm_sr_check_relaxed'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_is_xsm_sr_check_relaxed'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'make_plugin_call_count'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vm_opaque_ref_raises_instance_not_found
dedent|''
name|'def'
name|'test_get_vm_opaque_ref_raises_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'lookup'"
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'_get_vm_opaque_ref'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InjectAutoDiskConfigTestCase
dedent|''
dedent|''
name|'class'
name|'InjectAutoDiskConfigTestCase'
op|'('
name|'VMOpsTestBase'
op|')'
op|':'
newline|'\n'
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
name|'InjectAutoDiskConfigTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_auto_disk_config_when_present
dedent|''
name|'def'
name|'test_inject_auto_disk_config_when_present'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|','
name|'vm_ref'
op|'='
name|'self'
op|'.'
name|'create_vm'
op|'('
string|'"dummy"'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|','
string|'"uuid"'
op|':'
string|'"1234"'
op|','
string|'"auto_disk_config"'
op|':'
name|'True'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'inject_auto_disk_config'
op|'('
name|'instance'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'xenstore_data'
op|'='
name|'vm'
op|'['
string|"'xenstore_data'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'xenstore_data'
op|'['
string|"'vm-data/auto-disk-config'"
op|']'
op|','
string|"'True'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_auto_disk_config_none_as_false
dedent|''
name|'def'
name|'test_inject_auto_disk_config_none_as_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|','
name|'vm_ref'
op|'='
name|'self'
op|'.'
name|'create_vm'
op|'('
string|'"dummy"'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|','
string|'"uuid"'
op|':'
string|'"1234"'
op|','
string|'"auto_disk_config"'
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'inject_auto_disk_config'
op|'('
name|'instance'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'xenstore_data'
op|'='
name|'vm'
op|'['
string|"'xenstore_data'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'xenstore_data'
op|'['
string|"'vm-data/auto-disk-config'"
op|']'
op|','
string|"'False'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetConsoleOutputTestCase
dedent|''
dedent|''
name|'class'
name|'GetConsoleOutputTestCase'
op|'('
name|'VMOpsTestBase'
op|')'
op|':'
newline|'\n'
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
name|'GetConsoleOutputTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_works
dedent|''
name|'def'
name|'test_get_console_output_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'vmops'
op|','
string|"'_get_dom_id'"
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'_get_dom_id'
op|'('
name|'instance'
op|','
name|'check_rescue'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'42'
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
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"dom_id: 42"'
op|','
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'get_console_output'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_throws_nova_exception
dedent|''
name|'def'
name|'test_get_console_output_throws_nova_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'vmops'
op|','
string|"'_get_dom_id'"
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|'}'
newline|'\n'
comment|'# dom_id=0 used to trigger exception in fake XenAPI'
nl|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'_get_dom_id'
op|'('
name|'instance'
op|','
name|'check_rescue'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'0'
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'get_console_output'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dom_id_works
dedent|''
name|'def'
name|'test_get_dom_id_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|'}'
newline|'\n'
name|'vm'
op|','
name|'vm_ref'
op|'='
name|'self'
op|'.'
name|'create_vm'
op|'('
string|'"dummy"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm'
op|'['
string|'"domid"'
op|']'
op|','
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'_get_dom_id'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dom_id_works_with_rescue_vm
dedent|''
name|'def'
name|'test_get_dom_id_works_with_rescue_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|'}'
newline|'\n'
name|'vm'
op|','
name|'vm_ref'
op|'='
name|'self'
op|'.'
name|'create_vm'
op|'('
string|'"dummy-rescue"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm'
op|'['
string|'"domid"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'_get_dom_id'
op|'('
name|'instance'
op|','
name|'check_rescue'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dom_id_raises_not_found
dedent|''
name|'def'
name|'test_get_dom_id_raises_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'create_vm'
op|'('
string|'"not-dummy"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'_get_dom_id'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dom_id_works_with_vmref
dedent|''
name|'def'
name|'test_get_dom_id_works_with_vmref'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|','
name|'vm_ref'
op|'='
name|'self'
op|'.'
name|'create_vm'
op|'('
string|'"dummy"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm'
op|'['
string|'"domid"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'_get_dom_id'
op|'('
name|'vm_ref'
op|'='
name|'vm_ref'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoveHostnameTestCase
dedent|''
dedent|''
name|'class'
name|'RemoveHostnameTestCase'
op|'('
name|'VMOpsTestBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_remove_hostname
indent|'    '
name|'def'
name|'test_remove_hostname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|','
name|'vm_ref'
op|'='
name|'self'
op|'.'
name|'create_vm'
op|'('
string|'"dummy"'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"name"'
op|':'
string|'"dummy"'
op|','
string|'"uuid"'
op|':'
string|'"1234"'
op|','
string|'"auto_disk_config"'
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|"'call_xenapi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VM.remove_from_xenstore_data"'
op|','
name|'vm_ref'
op|','
nl|'\n'
string|'"vm-data/hostname"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vmops'
op|'.'
name|'remove_hostname'
op|'('
name|'instance'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
