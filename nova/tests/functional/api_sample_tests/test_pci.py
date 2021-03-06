begin_unit
comment|'# Copyright 2013 Intel.'
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
name|'collections'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'testtools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'pci_device_pool'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'test_servers'
newline|'\n'
nl|'\n'
DECL|variable|skip_msg
name|'skip_msg'
op|'='
string|'"Bug 1426241"'
newline|'\n'
nl|'\n'
DECL|variable|fake_db_dev_1
name|'fake_db_dev_1'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'0000:04:10.0'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'8086'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'1520'"
op|','
nl|'\n'
string|"'dev_type'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'SRIOV_VF'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'dev_id'"
op|':'
string|"'pci_0000_04_10_0'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'label_8086_1520'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'69ba1044-0766-4ec0-b60d-09595de034a1'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'extra_info'"
op|':'
string|'\'{"key1": "value1", "key2": "value2"}\''
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|fake_db_dev_2
name|'fake_db_dev_2'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'0000:04:10.1'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'8086'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'1520'"
op|','
nl|'\n'
string|"'dev_type'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'SRIOV_VF'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'dev_id'"
op|':'
string|"'pci_0000_04_10_1'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'label_8086_1520'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'d5b446a6-a1b4-4d01-b4f0-eac37b3a62fc'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'extra_info'"
op|':'
string|'\'{"key3": "value3", "key4": "value4"}\''
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedServerPciSampleJsonTest
name|'class'
name|'ExtendedServerPciSampleJsonTest'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-pci"'
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
name|'raise'
name|'testtools'
op|'.'
name|'TestCase'
op|'.'
name|'skipException'
op|'('
name|'skip_msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'hostid'"
op|':'
string|"'[a-f0-9]+'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/detail'"
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'hostid'"
op|':'
string|"'[a-f0-9]+'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-detail-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedHyervisorPciSampleJsonTest
dedent|''
dedent|''
name|'class'
name|'ExtendedHyervisorPciSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|"'os-hypervisors'"
op|']'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|"'os-pci'"
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
name|'raise'
name|'testtools'
op|'.'
name|'TestCase'
op|'.'
name|'skipException'
op|'('
name|'skip_msg'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ExtendedHyervisorPciSampleJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'cpu_info'
op|'='
name|'collections'
op|'.'
name|'OrderedDict'
op|'('
op|'['
nl|'\n'
op|'('
string|"'arch'"
op|','
string|"'x86_64'"
op|')'
op|','
nl|'\n'
op|'('
string|"'model'"
op|','
string|"'Nehalem'"
op|')'
op|','
nl|'\n'
op|'('
string|"'vendor'"
op|','
string|"'Intel'"
op|')'
op|','
nl|'\n'
op|'('
string|"'features'"
op|','
op|'['
string|"'pge'"
op|','
string|"'clflush'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'topology'"
op|','
op|'{'
nl|'\n'
string|"'cores'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'threads'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'sockets'"
op|':'
number|'4'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_compute_node'
op|'='
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
nl|'\n'
name|'cpu_info'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'cpu_info'
op|')'
op|','
nl|'\n'
name|'current_workload'
op|'='
number|'0'
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'0'
op|','
nl|'\n'
name|'host_ip'
op|'='
string|'"1.1.1.1"'
op|','
nl|'\n'
name|'state'
op|'='
string|'"up"'
op|','
nl|'\n'
name|'status'
op|'='
string|'"enabled"'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'1028'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
number|'7680'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"fake-mini"'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|'"fake"'
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'1000'
op|','
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'1028'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'8192'
op|','
nl|'\n'
name|'memory_mb_used'
op|'='
number|'512'
op|','
nl|'\n'
name|'running_vms'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'service_id'
op|'='
number|'2'
op|','
nl|'\n'
name|'host'
op|'='
string|"'043b3cacf6f34c90a7245151fc8ebcda'"
op|','
nl|'\n'
name|'pci_device_pools'
op|'='
name|'pci_device_pool'
op|'.'
name|'from_pci_stats'
op|'('
nl|'\n'
op|'{'
string|'"count"'
op|':'
number|'5'
op|','
nl|'\n'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"1520"'
op|','
nl|'\n'
string|'"keya"'
op|':'
string|'"valuea"'
op|','
nl|'\n'
string|'"key1"'
op|':'
string|'"value1"'
op|','
nl|'\n'
string|'"numa_node"'
op|':'
number|'1'
op|'}'
op|')'
op|','
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_service'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'('
nl|'\n'
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
name|'host'
op|'='
string|"'043b3cacf6f34c90a7245151fc8ebcda'"
op|','
nl|'\n'
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
name|'disabled_reason'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.servicegroup.API.service_is_up"'
op|','
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.objects.Service.get_by_compute_host"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.objects.ComputeNode.get_by_id"'
op|')'
newline|'\n'
DECL|member|test_pci_show
name|'def'
name|'test_pci_show'
op|'('
name|'self'
op|','
name|'mock_obj'
op|','
name|'mock_svc_get'
op|','
name|'mock_service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_obj'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_compute_node'
newline|'\n'
name|'mock_svc_get'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_service'
newline|'\n'
name|'hypervisor_id'
op|'='
number|'1'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/%s'"
op|'%'
name|'hypervisor_id'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'hypervisor_id'"
op|':'
name|'hypervisor_id'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-pci-show-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.servicegroup.API.service_is_up"'
op|','
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.objects.Service.get_by_compute_host"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.objects.ComputeNodeList.get_all"'
op|')'
newline|'\n'
DECL|member|test_pci_detail
name|'def'
name|'test_pci_detail'
op|'('
name|'self'
op|','
name|'mock_obj'
op|','
name|'mock_svc_get'
op|','
name|'mock_service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_obj'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'fake_compute_node'
op|']'
newline|'\n'
name|'mock_svc_get'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_service'
newline|'\n'
name|'hypervisor_id'
op|'='
number|'1'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'hypervisor_id'"
op|':'
name|'hypervisor_id'
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/detail'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-pci-detail-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciSampleJsonTest
dedent|''
dedent|''
name|'class'
name|'PciSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-pci"'
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
name|'raise'
name|'testtools'
op|'.'
name|'TestCase'
op|'.'
name|'skipException'
op|'('
name|'skip_msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_fake_pci_device_get_by_id
dedent|''
name|'def'
name|'_fake_pci_device_get_by_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake_db_dev_1'
newline|'\n'
nl|'\n'
DECL|member|_fake_pci_device_get_all_by_node
dedent|''
name|'def'
name|'_fake_pci_device_get_all_by_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'fake_db_dev_1'
op|','
name|'fake_db_dev_2'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_pci_show
dedent|''
name|'def'
name|'test_pci_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.pci_device_get_by_id'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_fake_pci_device_get_by_id'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-pci/1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'pci-show-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_index
dedent|''
name|'def'
name|'test_pci_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.pci_device_get_all_by_node'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_fake_pci_device_get_all_by_node'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-pci'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'pci-index-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_detail
dedent|''
name|'def'
name|'test_pci_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.pci_device_get_all_by_node'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_fake_pci_device_get_all_by_node'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-pci/detail'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'pci-detail-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
