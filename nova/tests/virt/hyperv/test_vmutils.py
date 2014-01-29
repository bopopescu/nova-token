begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMUtilsTestCase
name|'class'
name|'VMUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V VMUtils class."""'
newline|'\n'
nl|'\n'
DECL|variable|_FAKE_VM_NAME
name|'_FAKE_VM_NAME'
op|'='
string|"'fake_vm'"
newline|'\n'
DECL|variable|_FAKE_MEMORY_MB
name|'_FAKE_MEMORY_MB'
op|'='
number|'2'
newline|'\n'
DECL|variable|_FAKE_VM_PATH
name|'_FAKE_VM_PATH'
op|'='
string|'"fake_vm_path"'
newline|'\n'
DECL|variable|_FAKE_VHD_PATH
name|'_FAKE_VHD_PATH'
op|'='
string|'"fake_vhd_path"'
newline|'\n'
DECL|variable|_FAKE_DVD_PATH
name|'_FAKE_DVD_PATH'
op|'='
string|'"fake_dvd_path"'
newline|'\n'
DECL|variable|_FAKE_VOLUME_DRIVE_PATH
name|'_FAKE_VOLUME_DRIVE_PATH'
op|'='
string|'"fake_volume_drive_path"'
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
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'vmutils'
op|'.'
name|'VMUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'VMUtilsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enable_vm_metrics_collection
dedent|''
name|'def'
name|'test_enable_vm_metrics_collection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'enable_vm_metrics_collection'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_VM_NAME'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_lookup_vm
dedent|''
name|'def'
name|'_lookup_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_vm'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_lookup_vm_check'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
name|'return_value'
op|'='
name|'mock_vm'
op|')'
newline|'\n'
name|'mock_vm'
op|'.'
name|'path_'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
newline|'\n'
name|'return'
name|'mock_vm'
newline|'\n'
nl|'\n'
DECL|member|test_set_vm_memory_static
dedent|''
name|'def'
name|'test_set_vm_memory_static'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_set_vm_memory_dynamic'
op|'('
number|'1.0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_vm_memory_dynamic
dedent|''
name|'def'
name|'test_set_vm_memory_dynamic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_set_vm_memory_dynamic'
op|'('
number|'2.0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_set_vm_memory_dynamic
dedent|''
name|'def'
name|'_test_set_vm_memory_dynamic'
op|'('
name|'self'
op|','
name|'dynamic_memory_ratio'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_s'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_s'
op|'.'
name|'SystemType'
op|'='
number|'3'
newline|'\n'
nl|'\n'
name|'mock_vmsetting'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_vmsetting'
op|'.'
name|'associators'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock_s'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_modify_virt_resource'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_set_vm_memory'
op|'('
name|'mock_vm'
op|','
name|'mock_vmsetting'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_MEMORY_MB'
op|','
nl|'\n'
name|'dynamic_memory_ratio'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_modify_virt_resource'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'mock_s'
op|','
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'dynamic_memory_ratio'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_s'
op|'.'
name|'DynamicMemoryEnabled'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_s'
op|'.'
name|'DynamicMemoryEnabled'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vm_storage_paths
dedent|''
dedent|''
name|'def'
name|'test_get_vm_storage_paths'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_vm'
op|'='
name|'self'
op|'.'
name|'_lookup_vm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_vmsettings'
op|'='
op|'['
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
op|']'
newline|'\n'
name|'mock_vm'
op|'.'
name|'associators'
op|'.'
name|'return_value'
op|'='
name|'mock_vmsettings'
newline|'\n'
name|'mock_rasds'
op|'='
op|'['
op|']'
newline|'\n'
name|'mock_rasd1'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_rasd1'
op|'.'
name|'ResourceSubType'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_IDE_DISK_RES_SUB_TYPE'
newline|'\n'
name|'mock_rasd1'
op|'.'
name|'Connection'
op|'='
op|'['
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|']'
newline|'\n'
name|'mock_rasd2'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_rasd2'
op|'.'
name|'ResourceSubType'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_IDE_DVD_RES_SUB_TYPE'
newline|'\n'
name|'mock_rasd2'
op|'.'
name|'Connection'
op|'='
op|'['
name|'self'
op|'.'
name|'_FAKE_DVD_PATH'
op|']'
newline|'\n'
name|'mock_rasd3'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_rasd3'
op|'.'
name|'ResourceSubType'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_PHYS_DISK_RES_SUB_TYPE'
newline|'\n'
name|'mock_rasd3'
op|'.'
name|'HostResource'
op|'='
op|'['
name|'self'
op|'.'
name|'_FAKE_VOLUME_DRIVE_PATH'
op|']'
newline|'\n'
name|'mock_rasds'
op|'.'
name|'append'
op|'('
name|'mock_rasd1'
op|')'
newline|'\n'
name|'mock_rasds'
op|'.'
name|'append'
op|'('
name|'mock_rasd2'
op|')'
newline|'\n'
name|'mock_rasds'
op|'.'
name|'append'
op|'('
name|'mock_rasd3'
op|')'
newline|'\n'
name|'mock_vmsettings'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'.'
name|'return_value'
op|'='
name|'mock_rasds'
newline|'\n'
nl|'\n'
name|'storage'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_storage_paths'
op|'('
name|'self'
op|'.'
name|'_FAKE_VM_NAME'
op|')'
newline|'\n'
op|'('
name|'disk_files'
op|','
name|'volume_drives'
op|')'
op|'='
name|'storage'
newline|'\n'
nl|'\n'
name|'mock_vm'
op|'.'
name|'associators'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
newline|'\n'
name|'mock_vmsettings'
op|'['
number|'0'
op|']'
op|'.'
name|'associators'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_ResourceAllocationSettingData'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
name|'self'
op|'.'
name|'_FAKE_DVD_PATH'
op|']'
op|','
nl|'\n'
name|'disk_files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'_FAKE_VOLUME_DRIVE_PATH'
op|']'
op|','
name|'volume_drives'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
