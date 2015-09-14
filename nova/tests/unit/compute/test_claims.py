begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
string|'"""Tests for resource tracker claims."""'
newline|'\n'
nl|'\n'
name|'import'
name|'uuid'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'claims'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'manager'
name|'as'
name|'pci_manager'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'pci'
name|'import'
name|'fakes'
name|'as'
name|'pci_fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeResourceHandler
name|'class'
name|'FakeResourceHandler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|test_called
indent|'    '
name|'test_called'
op|'='
name|'False'
newline|'\n'
DECL|variable|usage_is_instance
name|'usage_is_instance'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|test_resources
name|'def'
name|'test_resources'
op|'('
name|'self'
op|','
name|'usage'
op|','
name|'limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_called'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'usage_is_itype'
op|'='
name|'usage'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|'=='
string|"'fakeitype'"
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DummyTracker
dedent|''
dedent|''
name|'class'
name|'DummyTracker'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|icalled
indent|'    '
name|'icalled'
op|'='
name|'False'
newline|'\n'
DECL|variable|rcalled
name|'rcalled'
op|'='
name|'False'
newline|'\n'
DECL|variable|ext_resources_handler
name|'ext_resources_handler'
op|'='
name|'FakeResourceHandler'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'new_pci_tracker'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|abort_instance_claim
dedent|''
name|'def'
name|'abort_instance_claim'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'icalled'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|drop_move_claim
dedent|''
name|'def'
name|'drop_move_claim'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'rcalled'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|new_pci_tracker
dedent|''
name|'def'
name|'new_pci_tracker'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'testuser'"
op|','
string|"'testproject'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_tracker'
op|'='
name|'pci_manager'
op|'.'
name|'PciDevTracker'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
op|']'
op|')'
op|')'
newline|'\n'
DECL|class|ClaimTestCase
name|'class'
name|'ClaimTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'ClaimTestCase'
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
string|"'fake-user'"
op|','
string|"'fake-project'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resources'
op|'='
name|'self'
op|'.'
name|'_fake_resources'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'='
name|'DummyTracker'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_claim
dedent|''
name|'def'
name|'_claim'
op|'('
name|'self'
op|','
name|'limits'
op|'='
name|'None'
op|','
name|'overhead'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'numa_topology'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'numa_topology'"
op|','
name|'None'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_fake_instance'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'numa_topology'
op|':'
newline|'\n'
indent|'            '
name|'db_numa_topology'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
string|"'created_at'"
op|':'
name|'None'
op|','
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'numa_topology'
op|'.'
name|'_to_json'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'db_numa_topology'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'overhead'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'overhead'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'0'
op|'}'
newline|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
nl|'\n'
name|'db'
op|','
string|"'instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'db_numa_topology'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'claims'
op|'.'
name|'Claim'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'self'
op|'.'
name|'tracker'
op|','
nl|'\n'
name|'self'
op|'.'
name|'resources'
op|','
name|'overhead'
op|'='
name|'overhead'
op|','
nl|'\n'
name|'limits'
op|'='
name|'limits'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_fake_instance
dedent|''
dedent|''
name|'def'
name|'_fake_instance'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid1'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'None'
nl|'\n'
op|'}'
newline|'\n'
name|'instance'
op|'.'
name|'update'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_fake_instance_type
dedent|''
name|'def'
name|'_fake_instance_type'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeitype'"
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'2'
nl|'\n'
op|'}'
newline|'\n'
name|'instance_type'
op|'.'
name|'update'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'objects'
op|'.'
name|'Flavor'
op|'('
op|'**'
name|'instance_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_fake_resources
dedent|''
name|'def'
name|'_fake_resources'
op|'('
name|'self'
op|','
name|'values'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'{'
nl|'\n'
string|"'memory_mb'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'free_ram_mb'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'free_disk_gb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'objects'
op|'.'
name|'NUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'memory_usage'
op|'='
number|'0'
op|','
name|'cpu_usage'
op|'='
number|'0'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|','
name|'siblings'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'memory_usage'
op|'='
number|'0'
op|','
name|'cpu_usage'
op|'='
number|'0'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|','
name|'siblings'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|')'
op|']'
nl|'\n'
op|')'
op|'.'
name|'_to_json'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'resources'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|test_memory_unlimited
dedent|''
name|'def'
name|'test_memory_unlimited'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_claim'
op|'('
name|'memory_mb'
op|'='
number|'99999999'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_unlimited_root
dedent|''
name|'def'
name|'test_disk_unlimited_root'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_claim'
op|'('
name|'root_gb'
op|'='
number|'999999'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_unlimited_ephemeral
dedent|''
name|'def'
name|'test_disk_unlimited_ephemeral'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_claim'
op|'('
name|'ephemeral_gb'
op|'='
number|'999999'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_memory_with_overhead
dedent|''
name|'def'
name|'test_memory_with_overhead'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'overhead'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'8'
op|'}'
newline|'\n'
name|'limits'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'2048'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_claim'
op|'('
name|'memory_mb'
op|'='
number|'2040'
op|','
name|'limits'
op|'='
name|'limits'
op|','
nl|'\n'
name|'overhead'
op|'='
name|'overhead'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_memory_with_overhead_insufficient
dedent|''
name|'def'
name|'test_memory_with_overhead_insufficient'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'overhead'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'9'
op|'}'
newline|'\n'
name|'limits'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'2048'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeResourcesUnavailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|','
name|'limits'
op|'='
name|'limits'
op|','
name|'overhead'
op|'='
name|'overhead'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2040'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_memory_oversubscription
dedent|''
name|'def'
name|'test_memory_oversubscription'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_claim'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_memory_insufficient
dedent|''
name|'def'
name|'test_memory_insufficient'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'limits'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'8192'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeResourcesUnavailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|','
name|'limits'
op|'='
name|'limits'
op|','
name|'memory_mb'
op|'='
number|'16384'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_oversubscription
dedent|''
name|'def'
name|'test_disk_oversubscription'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'limits'
op|'='
op|'{'
string|"'disk_gb'"
op|':'
number|'60'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_claim'
op|'('
name|'root_gb'
op|'='
number|'10'
op|','
name|'ephemeral_gb'
op|'='
number|'40'
op|','
nl|'\n'
name|'limits'
op|'='
name|'limits'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_insufficient
dedent|''
name|'def'
name|'test_disk_insufficient'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'limits'
op|'='
op|'{'
string|"'disk_gb'"
op|':'
number|'45'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'ComputeResourcesUnavailable'
op|','
nl|'\n'
string|'"disk"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|','
name|'limits'
op|'='
name|'limits'
op|','
name|'root_gb'
op|'='
number|'10'
op|','
name|'ephemeral_gb'
op|'='
number|'40'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_and_memory_insufficient
dedent|''
name|'def'
name|'test_disk_and_memory_insufficient'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'limits'
op|'='
op|'{'
string|"'disk_gb'"
op|':'
number|'45'
op|','
string|"'memory_mb'"
op|':'
number|'8192'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'ComputeResourcesUnavailable'
op|','
nl|'\n'
string|'"memory.*disk"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|','
name|'limits'
op|'='
name|'limits'
op|','
name|'root_gb'
op|'='
number|'10'
op|','
name|'ephemeral_gb'
op|'='
number|'40'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'16384'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'pci_fakes'
op|'.'
name|'patch_pci_whitelist'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_pci_pass
name|'def'
name|'test_pci_pass'
op|'('
name|'self'
op|','
name|'mock_get_by_instance'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_dict'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'new_pci_tracker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_tracker'
op|'.'
name|'_set_hvdevs'
op|'('
op|'['
name|'dev_dict'
op|']'
op|')'
newline|'\n'
name|'claim'
op|'='
name|'self'
op|'.'
name|'_claim'
op|'('
op|')'
newline|'\n'
name|'request'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'1'
op|','
nl|'\n'
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
string|"'product_id'"
op|':'
string|"'p'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'requests'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
name|'request'
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
name|'mock_get_by_instance'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'claim'
op|'.'
name|'_test_pci'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'pci_fakes'
op|'.'
name|'patch_pci_whitelist'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_pci_fail
name|'def'
name|'test_pci_fail'
op|'('
name|'self'
op|','
name|'mock_get_by_instance'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_dict'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'new_pci_tracker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_tracker'
op|'.'
name|'_set_hvdevs'
op|'('
op|'['
name|'dev_dict'
op|']'
op|')'
newline|'\n'
name|'claim'
op|'='
name|'self'
op|'.'
name|'_claim'
op|'('
op|')'
newline|'\n'
name|'request'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'1'
op|','
nl|'\n'
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
string|"'product_id'"
op|':'
string|"'p'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'requests'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
name|'request'
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
name|'mock_get_by_instance'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
name|'claim'
op|'.'
name|'_test_pci'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'pci_fakes'
op|'.'
name|'patch_pci_whitelist'
newline|'\n'
DECL|member|test_pci_pass_no_requests
name|'def'
name|'test_pci_pass_no_requests'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_dict'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'new_pci_tracker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_tracker'
op|'.'
name|'_set_hvdevs'
op|'('
op|'['
name|'dev_dict'
op|']'
op|')'
newline|'\n'
name|'claim'
op|'='
name|'self'
op|'.'
name|'_claim'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'claim'
op|'.'
name|'_test_pci'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ext_resources
dedent|''
name|'def'
name|'test_ext_resources'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_claim'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'ext_resources_handler'
op|'.'
name|'test_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'ext_resources_handler'
op|'.'
name|'usage_is_itype'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_topology_no_limit
dedent|''
name|'def'
name|'test_numa_topology_no_limit'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'huge_instance'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_claim'
op|'('
name|'numa_topology'
op|'='
name|'huge_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_topology_fails
dedent|''
name|'def'
name|'test_numa_topology_fails'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'huge_instance'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|','
number|'5'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'2048'
op|')'
op|']'
op|')'
newline|'\n'
name|'limit_topo'
op|'='
name|'objects'
op|'.'
name|'NUMATopologyLimits'
op|'('
nl|'\n'
name|'cpu_allocation_ratio'
op|'='
number|'1'
op|','
name|'ram_allocation_ratio'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeResourcesUnavailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|','
nl|'\n'
name|'limits'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'limit_topo'
op|'}'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'huge_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_topology_passes
dedent|''
name|'def'
name|'test_numa_topology_passes'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'huge_instance'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|']'
op|')'
newline|'\n'
name|'limit_topo'
op|'='
name|'objects'
op|'.'
name|'NUMATopologyLimits'
op|'('
nl|'\n'
name|'cpu_allocation_ratio'
op|'='
number|'1'
op|','
name|'ram_allocation_ratio'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_claim'
op|'('
name|'limits'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'limit_topo'
op|'}'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'huge_instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'pci_fakes'
op|'.'
name|'patch_pci_whitelist'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_numa_topology_with_pci
name|'def'
name|'test_numa_topology_with_pci'
op|'('
name|'self'
op|','
name|'mock_get_by_instance'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_dict'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'new_pci_tracker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_tracker'
op|'.'
name|'_set_hvdevs'
op|'('
op|'['
name|'dev_dict'
op|']'
op|')'
newline|'\n'
name|'request'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'1'
op|','
nl|'\n'
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
string|"'product_id'"
op|':'
string|"'p'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'requests'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
name|'request'
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
name|'mock_get_by_instance'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
nl|'\n'
name|'huge_instance'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|'('
name|'numa_topology'
op|'='
name|'huge_instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'pci_fakes'
op|'.'
name|'patch_pci_whitelist'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_numa_topology_with_pci_fail
name|'def'
name|'test_numa_topology_with_pci_fail'
op|'('
name|'self'
op|','
name|'mock_get_by_instance'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_dict'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'dev_dict2'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'new_pci_tracker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_tracker'
op|'.'
name|'_set_hvdevs'
op|'('
op|'['
name|'dev_dict'
op|','
name|'dev_dict2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'2'
op|','
nl|'\n'
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
string|"'product_id'"
op|':'
string|"'p'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'requests'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
name|'request'
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
name|'mock_get_by_instance'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
nl|'\n'
name|'huge_instance'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeResourcesUnavailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'huge_instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'pci_fakes'
op|'.'
name|'patch_pci_whitelist'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_numa_topology_with_pci_no_numa_info
name|'def'
name|'test_numa_topology_with_pci_no_numa_info'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_get_by_instance'
op|','
nl|'\n'
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_dict'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'new_pci_tracker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_tracker'
op|'.'
name|'_set_hvdevs'
op|'('
op|'['
name|'dev_dict'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'1'
op|','
nl|'\n'
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
string|"'product_id'"
op|':'
string|"'p'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'requests'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
name|'request'
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
name|'mock_get_by_instance'
op|'.'
name|'return_value'
op|'='
name|'requests'
newline|'\n'
nl|'\n'
name|'huge_instance'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_claim'
op|'('
name|'numa_topology'
op|'='
name|'huge_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_abort
dedent|''
name|'def'
name|'test_abort'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'claim'
op|'='
name|'self'
op|'.'
name|'_abort'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'claim'
op|'.'
name|'tracker'
op|'.'
name|'icalled'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_abort
dedent|''
name|'def'
name|'_abort'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'claim'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'self'
op|'.'
name|'_claim'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|')'
name|'as'
name|'claim'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"abort"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'test'
op|'.'
name|'TestingException'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'claim'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MoveClaimTestCase
dedent|''
dedent|''
name|'class'
name|'MoveClaimTestCase'
op|'('
name|'ClaimTestCase'
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
name|'MoveClaimTestCase'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'_fake_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'get_numa_constraint_patch'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_claim
dedent|''
name|'def'
name|'_claim'
op|'('
name|'self'
op|','
name|'limits'
op|'='
name|'None'
op|','
name|'overhead'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'numa_constraint'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'numa_topology'"
op|','
name|'None'
op|')'
newline|'\n'
name|'instance_type'
op|'='
name|'self'
op|'.'
name|'_fake_instance_type'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'overhead'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'overhead'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'0'
op|'}'
newline|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
nl|'\n'
string|"'nova.virt.hardware.numa_get_constraints'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'numa_constraint'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'claims'
op|'.'
name|'MoveClaim'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'instance_type'
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'tracker'
op|','
name|'self'
op|'.'
name|'resources'
op|','
nl|'\n'
name|'overhead'
op|'='
name|'overhead'
op|','
name|'limits'
op|'='
name|'limits'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_pci_request
dedent|''
dedent|''
name|'def'
name|'_set_pci_request'
op|'('
name|'self'
op|','
name|'claim'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
op|'['
op|'{'
string|"'count'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'spec'"
op|':'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
string|"'product_id'"
op|':'
string|"'p'"
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
op|']'
newline|'\n'
name|'claim'
op|'.'
name|'instance'
op|'.'
name|'update'
op|'('
nl|'\n'
name|'system_metadata'
op|'='
op|'{'
string|"'new_pci_requests'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'request'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
op|']'
op|')'
op|')'
newline|'\n'
DECL|member|test_ext_resources
name|'def'
name|'test_ext_resources'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_claim'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'ext_resources_handler'
op|'.'
name|'test_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'ext_resources_handler'
op|'.'
name|'usage_is_itype'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
op|'['
op|']'
op|')'
op|')'
newline|'\n'
DECL|member|test_abort
name|'def'
name|'test_abort'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'claim'
op|'='
name|'self'
op|'.'
name|'_abort'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'claim'
op|'.'
name|'tracker'
op|'.'
name|'rcalled'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
