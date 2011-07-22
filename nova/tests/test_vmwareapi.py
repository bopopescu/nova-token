begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nTest suite for VMWareAPI.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
newline|'\n'
nl|'\n'
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
name|'compute'
name|'import'
name|'power_state'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'vmwareapi'
name|'import'
name|'db_fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'vmwareapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'vmwareapi_conn'
newline|'\n'
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
newline|'\n'
nl|'\n'
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
DECL|class|VMWareAPIVMTestCase
name|'class'
name|'VMWareAPIVMTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for Vmware API connection calls."""'
newline|'\n'
nl|'\n'
comment|'# NOTE(jkoelker): This is leaking stubs into the db module.'
nl|'\n'
comment|'#                 Commenting out until updated for multi-nic.'
nl|'\n'
comment|'#def setUp(self):'
nl|'\n'
comment|'#    super(VMWareAPIVMTestCase, self).setUp()'
nl|'\n'
comment|"#    self.flags(vmwareapi_host_ip='test_url',"
nl|'\n'
comment|"#               vmwareapi_host_username='test_username',"
nl|'\n'
comment|"#               vmwareapi_host_password='test_pass')"
nl|'\n'
comment|'#    self.network = utils.import_object(FLAGS.network_manager)'
nl|'\n'
comment|"#    self.user_id = 'fake'"
nl|'\n'
comment|"#    self.project_id = 'fake'"
nl|'\n'
comment|'#    self.context = context.RequestContext(self.user_id, self.project_id)'
nl|'\n'
comment|'#    vmwareapi_fake.reset()'
nl|'\n'
comment|'#    db_fakes.stub_out_db_instance_api(self.stubs)'
nl|'\n'
comment|'#    stubs.set_stubs(self.stubs)'
nl|'\n'
comment|'#    glance_stubs.stubout_glance_client(self.stubs,'
nl|'\n'
comment|'#                                       glance_stubs.FakeGlance)'
nl|'\n'
comment|'#    self.conn = vmwareapi_conn.get_connection(False)'
nl|'\n'
nl|'\n'
comment|'#def tearDown(self):'
nl|'\n'
comment|'#    super(VMWareAPIVMTestCase, self).tearDown()'
nl|'\n'
comment|'#    vmwareapi_fake.cleanup()'
nl|'\n'
comment|'#    self.stubs.UnsetAll()'
nl|'\n'
nl|'\n'
DECL|member|_create_instance_in_the_db
name|'def'
name|'_create_instance_in_the_db'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'image_id'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|'"1"'
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
newline|'\n'
nl|'\n'
DECL|member|_create_vm
dedent|''
name|'def'
name|'_create_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create and spawn the VM."""'
newline|'\n'
name|'self'
op|'.'
name|'_create_instance_in_the_db'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'type_data'
op|'='
name|'db'
op|'.'
name|'instance_type_get_by_name'
op|'('
name|'None'
op|','
string|"'m1.large'"
op|')'
newline|'\n'
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
newline|'\n'
name|'self'
op|'.'
name|'_check_vm_record'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_vm_record
dedent|''
name|'def'
name|'_check_vm_record'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check if the spawned VM\'s properties correspond to the instance in\n        the db.\n        """'
newline|'\n'
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
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get Nova record for VM'
nl|'\n'
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
newline|'\n'
nl|'\n'
comment|'# Get record for VM'
nl|'\n'
name|'vms'
op|'='
name|'vmwareapi_fake'
op|'.'
name|'_get_objects'
op|'('
string|'"VirtualMachine"'
op|')'
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
newline|'\n'
name|'vcpus'
op|'='
name|'self'
op|'.'
name|'type_data'
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
op|'.'
name|'get'
op|'('
string|'"summary.config.numCpu"'
op|')'
op|','
name|'vcpus'
op|')'
newline|'\n'
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
nl|'\n'
name|'self'
op|'.'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
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
comment|'# Check that the VM is running according to vSphere API.'
nl|'\n'
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
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""\n        Check if the get_info returned values correspond to the instance\n        object in the db.\n        """'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_list_instances
name|'def'
name|'test_list_instances'
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
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_list_instances_1
name|'def'
name|'test_list_instances_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_spawn
name|'def'
name|'test_spawn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_snapshot
name|'def'
name|'test_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_snapshot_non_existent
name|'def'
name|'test_snapshot_non_existent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_instance_in_the_db'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'snapshot'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
string|'"Test-Snapshot"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_reboot
name|'def'
name|'test_reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_reboot_non_existent
name|'def'
name|'test_reboot_non_existent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_instance_in_the_db'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'reboot'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_reboot_not_poweredon
name|'def'
name|'test_reboot_not_poweredon'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'reboot'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_suspend
name|'def'
name|'test_suspend'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_suspend_non_existent
name|'def'
name|'test_suspend_non_existent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_instance_in_the_db'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'suspend'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'dummy_callback_handler'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_resume
name|'def'
name|'test_resume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_resume_non_existent
name|'def'
name|'test_resume_non_existent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_instance_in_the_db'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'resume'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'dummy_callback_handler'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_resume_not_suspended
name|'def'
name|'test_resume_not_suspended'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Exception'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'resume'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'dummy_callback_handler'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_get_info
name|'def'
name|'test_get_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_destroy
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_vm'
op|'('
op|')'
newline|'\n'
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
newline|'\n'
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
newline|'\n'
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
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
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
newline|'\n'
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
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_destroy_non_existent
name|'def'
name|'test_destroy_non_existent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_instance_in_the_db'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
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
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_pause
name|'def'
name|'test_pause'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_unpause
name|'def'
name|'test_unpause'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_diagnostics
name|'def'
name|'test_diagnostics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_get_console_output
name|'def'
name|'test_get_console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|test_get_ajax_console
name|'def'
name|'test_get_ajax_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"DB stubbing not removed, needs updating for multi-nic"'
op|')'
newline|'\n'
DECL|member|dummy_callback_handler
name|'def'
name|'dummy_callback_handler'
op|'('
name|'self'
op|','
name|'ret'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Dummy callback function to be passed to suspend, resume, etc., calls.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
