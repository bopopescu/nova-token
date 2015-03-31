begin_unit
comment|'#  Copyright 2014 Cloudbase Solutions Srl'
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
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'test_vmutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutilsv2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMUtilsV2TestCase
name|'class'
name|'VMUtilsV2TestCase'
op|'('
name|'test_vmutils'
op|'.'
name|'VMUtilsTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V VMUtilsV2 class."""'
newline|'\n'
nl|'\n'
DECL|variable|_DEFINE_SYSTEM
name|'_DEFINE_SYSTEM'
op|'='
string|"'DefineSystem'"
newline|'\n'
DECL|variable|_DESTROY_SYSTEM
name|'_DESTROY_SYSTEM'
op|'='
string|"'DestroySystem'"
newline|'\n'
DECL|variable|_DESTROY_SNAPSHOT
name|'_DESTROY_SNAPSHOT'
op|'='
string|"'DestroySnapshot'"
newline|'\n'
nl|'\n'
DECL|variable|_ADD_RESOURCE
name|'_ADD_RESOURCE'
op|'='
string|"'AddResourceSettings'"
newline|'\n'
DECL|variable|_REMOVE_RESOURCE
name|'_REMOVE_RESOURCE'
op|'='
string|"'RemoveResourceSettings'"
newline|'\n'
DECL|variable|_SETTING_TYPE
name|'_SETTING_TYPE'
op|'='
string|"'VirtualSystemType'"
newline|'\n'
DECL|variable|_VM_GEN
name|'_VM_GEN'
op|'='
name|'constants'
op|'.'
name|'VM_GEN_2'
newline|'\n'
nl|'\n'
DECL|variable|_VIRTUAL_SYSTEM_TYPE_REALIZED
name|'_VIRTUAL_SYSTEM_TYPE_REALIZED'
op|'='
string|"'Microsoft:Hyper-V:System:Realized'"
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
name|'VMUtilsV2TestCase'
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
name|'_vmutils'
op|'='
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
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
DECL|member|test_create_vm
dedent|''
name|'def'
name|'test_create_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VMUtilsV2TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'test_create_vm'
op|'('
op|')'
newline|'\n'
name|'mock_vssd'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_VIRTUAL_SYSTEM_SUBTYPE_GEN2'
op|','
nl|'\n'
name|'mock_vssd'
op|'.'
name|'VirtualSystemSubType'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_vssd'
op|'.'
name|'SecureBootEnabled'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_modify_virt_resource
dedent|''
name|'def'
name|'test_modify_virt_resource'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_svc'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_svc'
op|'.'
name|'ModifyResourceSettings'
op|'.'
name|'return_value'
op|'='
op|'('
name|'self'
op|'.'
name|'_FAKE_JOB_PATH'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_RET_VAL'
op|')'
newline|'\n'
name|'mock_res_setting_data'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_res_setting_data'
op|'.'
name|'GetText_'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_FAKE_RES_DATA'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_modify_virt_resource'
op|'('
name|'mock_res_setting_data'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
op|')'
newline|'\n'
nl|'\n'
name|'mock_svc'
op|'.'
name|'ModifyResourceSettings'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'ResourceSettings'
op|'='
op|'['
name|'self'
op|'.'
name|'_FAKE_RES_DATA'
op|']'
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
name|'vmutilsv2'
op|','
string|"'wmi'"
op|','
name|'create'
op|'='
name|'True'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|','
string|"'check_ret_val'"
op|')'
newline|'\n'
DECL|member|test_take_vm_snapshot
name|'def'
name|'test_take_vm_snapshot'
op|'('
name|'self'
op|','
name|'mock_check_ret_val'
op|','
name|'mock_wmi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_lookup_vm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_svc'
op|'='
name|'self'
op|'.'
name|'_get_snapshot_service'
op|'('
op|')'
newline|'\n'
name|'mock_svc'
op|'.'
name|'CreateSnapshot'
op|'.'
name|'return_value'
op|'='
op|'('
name|'self'
op|'.'
name|'_FAKE_JOB_PATH'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_RET_VAL'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'take_vm_snapshot'
op|'('
name|'self'
op|'.'
name|'_FAKE_VM_NAME'
op|')'
newline|'\n'
nl|'\n'
name|'mock_svc'
op|'.'
name|'CreateSnapshot'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'AffectedSystem'
op|'='
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
op|','
nl|'\n'
name|'SnapshotType'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_SNAPSHOT_FULL'
op|')'
newline|'\n'
nl|'\n'
name|'mock_check_ret_val'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'_FAKE_RET_VAL'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_JOB_PATH'
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
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|','
string|"'_add_virt_resource'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|','
string|"'_get_new_setting_data'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|','
string|"'_get_nic_data_by_name'"
op|')'
newline|'\n'
DECL|member|test_set_nic_connection
name|'def'
name|'test_set_nic_connection'
op|'('
name|'self'
op|','
name|'mock_get_nic_data'
op|','
name|'mock_get_new_sd'
op|','
nl|'\n'
name|'mock_add_virt_res'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_lookup_vm'
op|'('
op|')'
newline|'\n'
name|'fake_eth_port'
op|'='
name|'mock_get_new_sd'
op|'.'
name|'return_value'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'set_nic_connection'
op|'('
name|'self'
op|'.'
name|'_FAKE_VM_NAME'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mock_add_virt_res'
op|'.'
name|'assert_called_with'
op|'('
name|'fake_eth_port'
op|','
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.hyperv.vmutils.VMUtils._get_vm_disks'"
op|')'
newline|'\n'
DECL|member|test_enable_vm_metrics_collection
name|'def'
name|'test_enable_vm_metrics_collection'
op|'('
name|'self'
op|','
name|'mock_get_vm_disks'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_lookup_vm'
op|'('
op|')'
newline|'\n'
name|'mock_svc'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_MetricService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'metric_def'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_disk'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_disk'
op|'.'
name|'path_'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_FAKE_RES_PATH'
newline|'\n'
name|'mock_get_vm_disks'
op|'.'
name|'return_value'
op|'='
op|'('
op|'['
name|'mock_disk'
op|']'
op|','
op|'['
name|'mock_disk'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'fake_metric_def_paths'
op|'='
op|'['
string|"'fake_0'"
op|','
string|"'fake_0'"
op|','
name|'None'
op|']'
newline|'\n'
name|'fake_metric_resource_paths'
op|'='
op|'['
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_RES_PATH'
op|']'
newline|'\n'
nl|'\n'
name|'metric_def'
op|'.'
name|'path_'
op|'.'
name|'side_effect'
op|'='
name|'fake_metric_def_paths'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'CIM_BaseMetricDefinition'
op|'.'
name|'return_value'
op|'='
op|'['
nl|'\n'
name|'metric_def'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'enable_vm_metrics_collection'
op|'('
name|'self'
op|'.'
name|'_FAKE_VM_NAME'
op|')'
newline|'\n'
nl|'\n'
name|'calls'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
name|'Name'
op|'='
name|'def_name'
op|')'
nl|'\n'
name|'for'
name|'def_name'
name|'in'
op|'['
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_METRIC_AGGR_CPU_AVG'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_METRIC_AGGR_MEMORY_AVG'
op|']'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'CIM_BaseMetricDefinition'
op|'.'
name|'assert_has_calls'
op|'('
name|'calls'
op|')'
newline|'\n'
nl|'\n'
name|'calls'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'fake_metric_def_paths'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'calls'
op|'.'
name|'append'
op|'('
name|'mock'
op|'.'
name|'call'
op|'('
nl|'\n'
name|'Subject'
op|'='
name|'fake_metric_resource_paths'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'Definition'
op|'='
name|'fake_metric_def_paths'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'MetricCollectionEnabled'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_METRIC_ENABLED'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_svc'
op|'.'
name|'ControlMetrics'
op|'.'
name|'assert_has_calls'
op|'('
name|'calls'
op|','
name|'any_order'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_snapshot_service
dedent|''
name|'def'
name|'_get_snapshot_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSnapshotService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_assert_add_resources
dedent|''
name|'def'
name|'_assert_add_resources'
op|'('
name|'self'
op|','
name|'mock_svc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'getattr'
op|'('
name|'mock_svc'
op|','
name|'self'
op|'.'
name|'_ADD_RESOURCE'
op|')'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_VM_PATH'
op|','
op|'['
name|'self'
op|'.'
name|'_FAKE_RES_DATA'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assert_remove_resources
dedent|''
name|'def'
name|'_assert_remove_resources'
op|'('
name|'self'
op|','
name|'mock_svc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'getattr'
op|'('
name|'mock_svc'
op|','
name|'self'
op|'.'
name|'_REMOVE_RESOURCE'
op|')'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
op|'['
name|'self'
op|'.'
name|'_FAKE_RES_PATH'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_instance_notes
dedent|''
name|'def'
name|'test_list_instance_notes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vs'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'attrs'
op|'='
op|'{'
string|"'ElementName'"
op|':'
string|"'fake_name'"
op|','
nl|'\n'
string|"'Notes'"
op|':'
op|'['
string|"'4f54fb69-d3a2-45b7-bb9b-b6e6b3d893b3'"
op|']'
op|'}'
newline|'\n'
name|'vs'
op|'.'
name|'configure_mock'
op|'('
op|'**'
name|'attrs'
op|')'
newline|'\n'
name|'vs2'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'ElementName'
op|'='
string|"'fake_name2'"
op|','
name|'Notes'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'.'
name|'return_value'
op|'='
op|'['
name|'vs'
op|','
nl|'\n'
name|'vs2'
op|']'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'list_instance_notes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'('
name|'attrs'
op|'['
string|"'ElementName'"
op|']'
op|','
name|'attrs'
op|'['
string|"'Notes'"
op|']'
op|')'
op|']'
op|','
name|'response'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
op|'['
string|"'ElementName'"
op|','
string|"'Notes'"
op|']'
op|','
nl|'\n'
name|'VirtualSystemType'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_VIRTUAL_SYSTEM_TYPE_REALIZED'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.hyperv.vmutilsv2.VMUtilsV2.check_ret_val'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.hyperv.vmutilsv2.VMUtilsV2._get_wmi_obj'"
op|')'
newline|'\n'
DECL|member|_test_create_vm_obj
name|'def'
name|'_test_create_vm_obj'
op|'('
name|'self'
op|','
name|'mock_get_wmi_obj'
op|','
name|'mock_check_ret_val'
op|','
nl|'\n'
name|'vm_path'
op|','
name|'dynamic_memory_ratio'
op|'='
number|'1.0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_vs_man_svc'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_vs_data'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_job'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'fake_job_path'
op|'='
string|"'fake job path'"
newline|'\n'
name|'fake_ret_val'
op|'='
string|"'fake return value'"
newline|'\n'
name|'_conn'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
newline|'\n'
nl|'\n'
name|'mock_check_ret_val'
op|'.'
name|'return_value'
op|'='
name|'mock_job'
newline|'\n'
name|'_conn'
op|'.'
name|'new'
op|'.'
name|'return_value'
op|'='
name|'mock_vs_data'
newline|'\n'
name|'mock_vs_man_svc'
op|'.'
name|'DefineSystem'
op|'.'
name|'return_value'
op|'='
op|'('
name|'fake_job_path'
op|','
nl|'\n'
name|'vm_path'
op|','
nl|'\n'
name|'fake_ret_val'
op|')'
newline|'\n'
name|'mock_job'
op|'.'
name|'associators'
op|'.'
name|'return_value'
op|'='
op|'['
string|"'fake vm path'"
op|']'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_create_vm_obj'
op|'('
nl|'\n'
name|'vs_man_svc'
op|'='
name|'mock_vs_man_svc'
op|','
nl|'\n'
name|'vm_name'
op|'='
string|"'fake vm'"
op|','
nl|'\n'
name|'vm_gen'
op|'='
string|"'fake vm gen'"
op|','
nl|'\n'
name|'notes'
op|'='
string|"'fake notes'"
op|','
nl|'\n'
name|'dynamic_memory_ratio'
op|'='
name|'dynamic_memory_ratio'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'vm_path'
op|':'
newline|'\n'
indent|'            '
name|'mock_job'
op|'.'
name|'associators'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_AFFECTED_JOB_ELEMENT_CLASS'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_conn'
op|'.'
name|'new'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_vs_data'
op|'.'
name|'ElementName'
op|','
string|"'fake vm'"
op|')'
newline|'\n'
name|'mock_vs_man_svc'
op|'.'
name|'DefineSystem'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'ResourceSettings'
op|'='
op|'['
op|']'
op|','
name|'ReferenceConfiguration'
op|'='
name|'None'
op|','
nl|'\n'
name|'SystemSettings'
op|'='
name|'mock_vs_data'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'mock_check_ret_val'
op|'.'
name|'assert_called_once_with'
op|'('
name|'fake_ret_val'
op|','
name|'fake_job_path'
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
name|'assertFalse'
op|'('
name|'mock_vs_data'
op|'.'
name|'VirtualNumaEnabled'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_get_wmi_obj'
op|'.'
name|'assert_called_with'
op|'('
string|"'fake vm path'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_vs_data'
op|'.'
name|'Notes'
op|','
string|"'fake notes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|','
name|'mock_get_wmi_obj'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vm_obj
dedent|''
name|'def'
name|'test_create_vm_obj'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_vm_obj'
op|'('
name|'vm_path'
op|'='
string|"'fake vm path'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vm_obj_no_vm_path
dedent|''
name|'def'
name|'test_create_vm_obj_no_vm_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_vm_obj'
op|'('
name|'vm_path'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vm_obj_dynamic_memory
dedent|''
name|'def'
name|'test_create_vm_obj_dynamic_memory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_vm_obj'
op|'('
name|'vm_path'
op|'='
name|'None'
op|','
name|'dynamic_memory_ratio'
op|'='
number|'1.1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_instances
dedent|''
name|'def'
name|'test_list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vs'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'attrs'
op|'='
op|'{'
string|"'ElementName'"
op|':'
string|"'fake_name'"
op|'}'
newline|'\n'
name|'vs'
op|'.'
name|'configure_mock'
op|'('
op|'**'
name|'attrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'.'
name|'return_value'
op|'='
op|'['
name|'vs'
op|']'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'('
name|'attrs'
op|'['
string|"'ElementName'"
op|']'
op|')'
op|']'
op|','
name|'response'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSystemSettingData'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
op|'['
string|"'ElementName'"
op|']'
op|','
nl|'\n'
name|'VirtualSystemType'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_VIRTUAL_SYSTEM_TYPE_REALIZED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_attached_disks
dedent|''
name|'def'
name|'test_get_attached_disks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_scsi_ctrl_path'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'expected_query'
op|'='
op|'('
string|'"SELECT * FROM %(class_name)s "'
nl|'\n'
string|'"WHERE (ResourceSubType=\'%(res_sub_type)s\' OR "'
nl|'\n'
string|'"ResourceSubType=\'%(res_sub_type_virt)s\' OR "'
nl|'\n'
string|'"ResourceSubType=\'%(res_sub_type_dvd)s\') AND "'
nl|'\n'
string|'"Parent = \'%(parent)s\'"'
op|'%'
nl|'\n'
op|'{'
string|'"class_name"'
op|':'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_RESOURCE_ALLOC_SETTING_DATA_CLASS'
op|','
nl|'\n'
string|'"res_sub_type"'
op|':'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_PHYS_DISK_RES_SUB_TYPE'
op|','
nl|'\n'
string|'"res_sub_type_virt"'
op|':'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_DISK_DRIVE_RES_SUB_TYPE'
op|','
nl|'\n'
string|'"res_sub_type_dvd"'
op|':'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_DVD_DRIVE_RES_SUB_TYPE'
op|','
nl|'\n'
string|'"parent"'
op|':'
name|'mock_scsi_ctrl_path'
op|'.'
name|'replace'
op|'('
string|'"\'"'
op|','
string|'"\'\'"'
op|')'
op|'}'
op|')'
newline|'\n'
name|'expected_disks'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'.'
name|'return_value'
newline|'\n'
nl|'\n'
name|'ret_disks'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_attached_disks'
op|'('
name|'mock_scsi_ctrl_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'_conn'
op|'.'
name|'query'
op|'.'
name|'assert_called_once_with'
op|'('
name|'expected_query'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_disks'
op|','
name|'ret_disks'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
