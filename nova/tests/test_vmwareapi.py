begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
string|'"""\r\nTest suite for VMWareAPI\r\n"""'
newline|'\r\n'
name|'import'
name|'stubout'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\r\n'
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
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'vmwareapi'
name|'import'
name|'db_fakes'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'vmwareapi'
name|'import'
name|'stubs'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'vmwareapi_conn'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
name|'as'
name|'vmwareapi_fake'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VMWareAPIVMTestCase
name|'class'
name|'VMWareAPIVMTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Unit tests for Vmware API connection calls\r\n    """'
newline|'\r\n'
nl|'\r\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'super'
op|'('
name|'VMWareAPIVMTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'admin'
op|'='
name|'True'
op|')'
newline|'\r\n'
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
newline|'\r\n'
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
newline|'\r\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\r\n'
name|'FLAGS'
op|'.'
name|'vmwareapi_host_ip'
op|'='
string|"'test_url'"
newline|'\r\n'
name|'FLAGS'
op|'.'
name|'vmwareapi_host_username'
op|'='
string|"'test_username'"
newline|'\r\n'
name|'FLAGS'
op|'.'
name|'vmwareapi_host_password'
op|'='
string|"'test_pass'"
newline|'\r\n'
name|'vmwareapi_fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\r\n'
name|'db_fakes'
op|'.'
name|'stub_out_db_instance_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'set_stubs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\r\n'
name|'glance_stubs'
op|'.'
name|'stubout_glance_client'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
nl|'\r\n'
name|'glance_stubs'
op|'.'
name|'FakeGlance'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'vmwareapi_conn'
op|'.'
name|'get_connection'
op|'('
name|'False'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_create_vm
dedent|''
name|'def'
name|'_create_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'""" Create and spawn the VM """'
newline|'\r\n'
name|'values'
op|'='
op|'{'
string|"'name'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
nl|'\r\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
nl|'\r\n'
string|"'image_id'"
op|':'
string|'"1"'
op|','
nl|'\r\n'
string|"'kernel_id'"
op|':'
string|'"1"'
op|','
nl|'\r\n'
string|"'ramdisk_id'"
op|':'
string|'"1"'
op|','
nl|'\r\n'
string|"'instance_type'"
op|':'
string|"'m1.large'"
op|','
nl|'\r\n'
string|"'mac_address'"
op|':'
string|"'aa:bb:cc:dd:ee:ff'"
op|','
nl|'\r\n'
op|'}'
newline|'\r\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'values'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'type_data'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'values'
op|'['
string|"'instance_type'"
op|']'
op|']'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_record'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_check_vm_record
dedent|''
name|'def'
name|'_check_vm_record'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'""" Check if the spawned VM\'s properties corresponds to the instance in\r\n        the db """'
newline|'\r\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'# Get Nova record for VM'
nl|'\r\n'
name|'vm_info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'# Get XenAPI record for VM'
nl|'\r\n'
name|'vms'
op|'='
name|'vmwareapi_fake'
op|'.'
name|'_get_objects'
op|'('
string|'"VirtualMachine"'
op|')'
newline|'\r\n'
name|'vm'
op|'='
name|'vms'
op|'['
number|'0'
op|']'
newline|'\r\n'
nl|'\r\n'
comment|'# Check that m1.large above turned into the right thing.'
nl|'\r\n'
name|'mem_kib'
op|'='
name|'long'
op|'('
name|'self'
op|'.'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|'<<'
number|'10'
newline|'\r\n'
name|'vcpus'
op|'='
name|'self'
op|'.'
name|'type_data'
op|'['
string|"'vcpus'"
op|']'
newline|'\r\n'
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
newline|'\r\n'
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
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'.'
name|'get'
op|'('
string|'"summary.config.numCpu"'
op|')'
op|','
name|'vcpus'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'.'
name|'get'
op|'('
string|'"summary.config.memorySizeMB"'
op|')'
op|','
nl|'\r\n'
name|'self'
op|'.'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'# Check that the VM is running according to Nova'
nl|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
comment|'# Check that the VM is running according to XenAPI.'
nl|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vm'
op|'.'
name|'get'
op|'('
string|'"runtime.powerState"'
op|')'
op|','
string|"'poweredOn'"
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_check_vm_info
dedent|''
name|'def'
name|'_check_vm_info'
op|'('
name|'self'
op|','
name|'info'
op|','
name|'pwr_state'
op|'='
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'""" Check if the get_info returned values correspond to the instance\r\n        object in the db """'
newline|'\r\n'
name|'mem_kib'
op|'='
name|'long'
op|'('
name|'self'
op|'.'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|'<<'
number|'10'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'info'
op|'['
string|'"state"'
op|']'
op|','
name|'pwr_state'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'info'
op|'['
string|'"max_mem"'
op|']'
op|','
name|'mem_kib'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'info'
op|'['
string|'"mem"'
op|']'
op|','
name|'mem_kib'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'info'
op|'['
string|'"num_cpu"'
op|']'
op|','
name|'self'
op|'.'
name|'type_data'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_list_instances
dedent|''
name|'def'
name|'test_list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
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
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'0'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_list_instances_1
dedent|''
name|'def'
name|'test_list_instances_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_spawn
dedent|''
name|'def'
name|'test_spawn'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_snapshot
dedent|''
name|'def'
name|'test_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'snapshot'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
string|'"Test-Snapshot"'
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_reboot
dedent|''
name|'def'
name|'test_reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'reboot'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_suspend
dedent|''
name|'def'
name|'test_suspend'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'suspend'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'dummy_callback_handler'
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'PAUSED'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_resume
dedent|''
name|'def'
name|'test_resume'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'suspend'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'dummy_callback_handler'
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'PAUSED'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'resume'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'dummy_callback_handler'
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_get_info
dedent|''
name|'def'
name|'test_get_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_destroy
dedent|''
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\r\n'
name|'info'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_info'
op|'('
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_check_vm_info'
op|'('
name|'info'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\r\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|'=='
number|'1'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\r\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|'=='
number|'0'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_pause
dedent|''
name|'def'
name|'test_pause'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_unpause
dedent|''
name|'def'
name|'test_unpause'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_diagnostics
dedent|''
name|'def'
name|'test_diagnostics'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_get_console_output
dedent|''
name|'def'
name|'test_get_console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_get_ajax_console
dedent|''
name|'def'
name|'test_get_ajax_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|dummy_callback_handler
dedent|''
name|'def'
name|'dummy_callback_handler'
op|'('
name|'self'
op|','
name|'ret'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'""" Dummy callback function to be passed to suspend, resume, etc.\r\n        calls """'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'super'
op|'('
name|'VMWareAPIVMTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\r\n'
name|'vmwareapi_fake'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\r\n'
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
newline|'\r\n'
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
newline|'\r\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\r\n'
dedent|''
dedent|''
endmarker|''
end_unit
