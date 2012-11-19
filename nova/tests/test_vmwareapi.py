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
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
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
name|'fake'
name|'as'
name|'vmwareapi_fake'
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
name|'VMWareAPIVMTestCase'
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
name|'vmwareapi_host_ip'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'vmwareapi_host_username'
op|'='
string|"'test_username'"
op|','
nl|'\n'
name|'vmwareapi_host_password'
op|'='
string|"'test_pass'"
op|')'
newline|'\n'
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
name|'vmwareapi_fake'
op|'.'
name|'reset'
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
name|'stubs'
op|'.'
name|'set_stubs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'driver'
op|'.'
name|'VMWareESXDriver'
op|'('
name|'None'
op|','
name|'False'
op|')'
newline|'\n'
comment|'# NOTE(vish): none of the network plugging code is actually'
nl|'\n'
comment|'#             being tested'
nl|'\n'
name|'self'
op|'.'
name|'network_info'
op|'='
op|'['
op|'('
op|'{'
string|"'bridge'"
op|':'
string|"'fa0'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'broadcast'"
op|':'
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'dns'"
op|':'
op|'['
string|"'192.168.0.1'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'dead:beef::1'"
op|','
nl|'\n'
string|"'ip6s'"
op|':'
op|'['
op|'{'
string|"'enabled'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'dead:beef::dcad:beff:feef:0'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'64'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
op|'{'
string|"'enabled'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'192.168.0.100'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'mac'"
op|':'
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\n'
string|"'rxtx_cap'"
op|':'
number|'3'
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'image'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'c1c8ce3d-c2e0-4247-890c-ccf5cc1c004c'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vhd'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'512'
op|','
nl|'\n'
op|'}'
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
name|'VMWareAPIVMTestCase'
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
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService_reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance_in_the_db
dedent|''
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
string|"'image_ref'"
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
string|"'mac_address'"
op|':'
string|'"de:ad:be:ef:be:ef"'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
string|"'m1.large'"
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
name|'None'
op|','
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
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'image'
op|','
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
op|','
name|'admin_password'
op|'='
name|'None'
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
name|'None'
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
DECL|member|test_list_instances_1
dedent|''
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
DECL|member|test_spawn
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
DECL|member|test_snapshot
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
name|'context'
op|','
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
DECL|member|test_snapshot_non_existent
dedent|''
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
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'snapshot'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
string|'"Test-Snapshot"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reboot
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
name|'reboot_type'
op|'='
string|'"SOFT"'
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
op|','
name|'self'
op|'.'
name|'network_info'
op|','
name|'reboot_type'
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
DECL|member|test_reboot_non_existent
dedent|''
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
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'reboot'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'network_info'
op|','
string|"'SOFT'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reboot_not_poweredon
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
name|'exception'
op|'.'
name|'InstanceRebootFailure'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'reboot'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'network_info'
op|','
string|"'SOFT'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_suspend
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
DECL|member|test_suspend_non_existent
dedent|''
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
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'suspend'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resume
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
DECL|member|test_resume_non_existent
dedent|''
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
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'resume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resume_not_suspended
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
name|'exception'
op|'.'
name|'InstanceResumeFailure'
op|','
name|'self'
op|'.'
name|'conn'
op|'.'
name|'resume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_info
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
DECL|member|test_destroy
dedent|''
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
op|'{'
string|"'name'"
op|':'
number|'1'
op|'}'
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
op|','
name|'self'
op|'.'
name|'network_info'
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
DECL|member|test_destroy_non_existent
dedent|''
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
op|','
name|'self'
op|'.'
name|'network_info'
op|')'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause
dedent|''
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
DECL|member|test_unpause
dedent|''
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
DECL|member|test_diagnostics
dedent|''
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
DECL|member|test_get_console_output
dedent|''
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
dedent|''
dedent|''
endmarker|''
end_unit
