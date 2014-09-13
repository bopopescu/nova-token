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
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
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
name|'vm_states'
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
name|'pci_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_pci
name|'fake_pci'
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
string|"'0000:00:00.1'"
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
string|"'request_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|'}'
newline|'\n'
DECL|variable|fake_pci_1
name|'fake_pci_1'
op|'='
name|'dict'
op|'('
name|'fake_pci'
op|','
name|'address'
op|'='
string|"'0000:00:00.2'"
op|','
nl|'\n'
name|'product_id'
op|'='
string|"'p1'"
op|','
name|'vendor_id'
op|'='
string|"'v1'"
op|')'
newline|'\n'
DECL|variable|fake_pci_2
name|'fake_pci_2'
op|'='
name|'dict'
op|'('
name|'fake_pci'
op|','
name|'address'
op|'='
string|"'0000:00:00.3'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_db_dev
name|'fake_db_dev'
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
string|"'0000:00:00.1'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p'"
op|','
nl|'\n'
string|"'dev_type'"
op|':'
string|"'t'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'dev_id'"
op|':'
string|"'i'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'l'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'extra_info'"
op|':'
string|"'{}'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|fake_db_dev_1
name|'fake_db_dev_1'
op|'='
name|'dict'
op|'('
name|'fake_db_dev'
op|','
name|'vendor_id'
op|'='
string|"'v1'"
op|','
nl|'\n'
name|'product_id'
op|'='
string|"'p1'"
op|','
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|address
name|'address'
op|'='
string|"'0000:00:00.2'"
op|')'
newline|'\n'
DECL|variable|fake_db_dev_2
name|'fake_db_dev_2'
op|'='
name|'dict'
op|'('
name|'fake_db_dev'
op|','
name|'id'
op|'='
number|'3'
op|','
name|'address'
op|'='
string|"'0000:00:00.3'"
op|')'
newline|'\n'
DECL|variable|fake_db_devs
name|'fake_db_devs'
op|'='
op|'['
name|'fake_db_dev'
op|','
name|'fake_db_dev_1'
op|','
name|'fake_db_dev_2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_pci_requests
name|'fake_pci_requests'
op|'='
op|'['
nl|'\n'
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
op|'}'
op|']'
op|'}'
op|','
nl|'\n'
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
string|"'v1'"
op|'}'
op|']'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDevTrackerTestCase
name|'class'
name|'PciDevTrackerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_create_fake_instance
indent|'    '
name|'def'
name|'_create_fake_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'uuid'
op|'='
string|"'fake-inst-uuid'"
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'pci_devices'
op|'='
name|'objects'
op|'.'
name|'PciDeviceList'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'task_state'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_fake_get_pci_devices
dedent|''
name|'def'
name|'_fake_get_pci_devices'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake_db_devs'
op|'['
op|':'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_fake_pci_device_update
dedent|''
name|'def'
name|'_fake_pci_device_update'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'node_id'
op|','
name|'address'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'update_called'
op|'+='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'called_values'
op|'='
name|'value'
newline|'\n'
name|'fake_return'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_db_dev'
op|')'
newline|'\n'
name|'return'
name|'fake_return'
newline|'\n'
nl|'\n'
DECL|member|_fake_pci_device_destroy
dedent|''
name|'def'
name|'_fake_pci_device_destroy'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'node_id'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'destroy_called'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|_create_pci_requests_object
dedent|''
name|'def'
name|'_create_pci_requests_object'
op|'('
name|'self'
op|','
name|'mock_get'
op|','
name|'requests'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_reqs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'pci_req_obj'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
name|'request'
op|'['
string|"'count'"
op|']'
op|','
nl|'\n'
name|'spec'
op|'='
name|'request'
op|'['
string|"'spec'"
op|']'
op|')'
newline|'\n'
name|'pci_reqs'
op|'.'
name|'append'
op|'('
name|'pci_req_obj'
op|')'
newline|'\n'
dedent|''
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'objects'
op|'.'
name|'InstancePCIRequests'
op|'('
name|'requests'
op|'='
name|'pci_reqs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'PciDevTrackerTestCase'
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
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'pci_device_get_all_by_node'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_fake_get_pci_devices'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'='
name|'pci_manager'
op|'.'
name|'PciDevTracker'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pcidev_tracker_create
dedent|''
name|'def'
name|'test_pcidev_tracker_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'stale'
op|'.'
name|'keys'
op|'('
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'stats'
op|'.'
name|'pools'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'node_id'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pcidev_tracker_create_no_nodeid
dedent|''
name|'def'
name|'test_pcidev_tracker_create_no_nodeid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'tracker'
op|'='
name|'pci_manager'
op|'.'
name|'PciDevTracker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_hvdev_new_dev
dedent|''
name|'def'
name|'test_set_hvdev_new_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_pci_3'
op|'='
name|'dict'
op|'('
name|'fake_pci'
op|','
name|'address'
op|'='
string|"'0000:00:00.4'"
op|','
name|'vendor_id'
op|'='
string|"'v2'"
op|')'
newline|'\n'
name|'fake_pci_devs'
op|'='
op|'['
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_1'
op|')'
op|','
nl|'\n'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_2'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_3'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_hvdevs'
op|'('
name|'fake_pci_devs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|')'
op|','
number|'4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'address'"
op|']'
name|'for'
nl|'\n'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'0000:00:00.1'"
op|','
string|"'0000:00:00.2'"
op|','
nl|'\n'
string|"'0000:00:00.3'"
op|','
string|"'0000:00:00.4'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
nl|'\n'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v'"
op|','
string|"'v1'"
op|','
string|"'v2'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_hvdev_changed
dedent|''
name|'def'
name|'test_set_hvdev_changed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_pci_v2'
op|'='
name|'dict'
op|'('
name|'fake_pci'
op|','
name|'address'
op|'='
string|"'0000:00:00.2'"
op|','
name|'vendor_id'
op|'='
string|"'v1'"
op|')'
newline|'\n'
name|'fake_pci_devs'
op|'='
op|'['
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_2'
op|')'
op|','
nl|'\n'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_v2'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_hvdevs'
op|'('
name|'fake_pci_devs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
nl|'\n'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v'"
op|','
string|"'v1'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_hvdev_remove
dedent|''
name|'def'
name|'test_set_hvdev_remove'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_hvdevs'
op|'('
op|'['
name|'fake_pci'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
op|'['
name|'dev'
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
nl|'\n'
name|'if'
name|'dev'
op|'['
string|"'status'"
op|']'
op|'=='
string|"'removed'"
op|']'
op|')'
op|','
nl|'\n'
number|'2'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_set_hvdev_changed_stal
name|'def'
name|'test_set_hvdev_changed_stal'
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
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
nl|'\n'
op|'['
op|'{'
string|"'count'"
op|':'
number|'1'
op|','
string|"'spec'"
op|':'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|'}'
op|']'
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'_claim_instance'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'fake_pci_3'
op|'='
name|'dict'
op|'('
name|'fake_pci'
op|','
name|'address'
op|'='
string|"'0000:00:00.2'"
op|','
name|'vendor_id'
op|'='
string|"'v2'"
op|')'
newline|'\n'
name|'fake_pci_devs'
op|'='
op|'['
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_2'
op|')'
op|','
nl|'\n'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_3'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_hvdevs'
op|'('
name|'fake_pci_devs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'stale'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'stale'
op|'['
string|"'0000:00:00.2'"
op|']'
op|'['
string|"'vendor_id'"
op|']'
op|','
string|"'v2'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_update_pci_for_instance_active
name|'def'
name|'test_update_pci_for_instance_active'
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
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
name|'fake_pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'free_devs'
op|'['
number|'0'
op|']'
op|'['
string|"'vendor_id'"
op|']'
op|','
string|"'v'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_update_pci_for_instance_fail
name|'def'
name|'test_update_pci_for_instance_fail'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_requests'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_requests'
op|')'
newline|'\n'
name|'pci_requests'
op|'['
number|'0'
op|']'
op|'['
string|"'count'"
op|']'
op|'='
number|'4'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
name|'pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceRequestFailed'
op|','
nl|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_update_pci_for_instance_deleted
name|'def'
name|'test_update_pci_for_instance_deleted'
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
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
name|'fake_pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
nl|'\n'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v'"
op|','
string|"'v1'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_update_pci_for_instance_resize_source
name|'def'
name|'test_update_pci_for_instance_resize_source'
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
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
name|'fake_pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'RESIZE_MIGRATED'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_update_pci_for_instance_resize_dest
name|'def'
name|'test_update_pci_for_instance_resize_dest'
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
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
name|'fake_pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_migration'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'claims'
op|'['
string|"'fake-inst-uuid'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'fake-inst-uuid'"
op|','
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'allocations'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'RESIZE_FINISH'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'allocations'
op|'['
string|"'fake-inst-uuid'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'fake-inst-uuid'"
op|','
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'claims'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_update_pci_for_migration_in
name|'def'
name|'test_update_pci_for_migration_in'
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
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
name|'fake_pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_migration'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'free_devs'
op|'['
number|'0'
op|']'
op|'['
string|"'vendor_id'"
op|']'
op|','
string|"'v'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_update_pci_for_migration_out
name|'def'
name|'test_update_pci_for_migration_out'
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
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
name|'fake_pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_migration'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_migration'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|','
name|'sign'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
nl|'\n'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v'"
op|','
string|"'v1'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save
dedent|''
name|'def'
name|'test_save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"pci_device_update"'
op|','
name|'self'
op|'.'
name|'_fake_pci_device_update'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_pci_v3'
op|'='
name|'dict'
op|'('
name|'fake_pci'
op|','
name|'address'
op|'='
string|"'0000:00:00.2'"
op|','
name|'vendor_id'
op|'='
string|"'v3'"
op|')'
newline|'\n'
name|'fake_pci_devs'
op|'='
op|'['
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_2'
op|')'
op|','
nl|'\n'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_v3'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_hvdevs'
op|'('
name|'fake_pci_devs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'update_called'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'save'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'update_called'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_removed
dedent|''
name|'def'
name|'test_save_removed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"pci_device_update"'
op|','
name|'self'
op|'.'
name|'_fake_pci_device_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"pci_device_destroy"'
op|','
name|'self'
op|'.'
name|'_fake_pci_device_destroy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'destroy_called'
op|'='
number|'0'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'update_called'
op|'='
number|'0'
newline|'\n'
name|'pci_device'
op|'.'
name|'remove'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'save'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'destroy_called'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_compute_node_id
dedent|''
name|'def'
name|'test_set_compute_node_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'tracker'
op|'='
name|'pci_manager'
op|'.'
name|'PciDevTracker'
op|'('
op|')'
newline|'\n'
name|'fake_pci_devs'
op|'='
op|'['
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_1'
op|')'
op|','
nl|'\n'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_2'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_hvdevs'
op|'('
name|'fake_pci_devs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_compute_node_id'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'node_id'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|'['
number|'0'
op|']'
op|'.'
name|'compute_node_id'
op|','
number|'1'
op|')'
newline|'\n'
name|'fake_pci_3'
op|'='
name|'dict'
op|'('
name|'fake_pci'
op|','
name|'address'
op|'='
string|"'0000:00:00.4'"
op|','
name|'vendor_id'
op|'='
string|"'v2'"
op|')'
newline|'\n'
name|'fake_pci_devs'
op|'='
op|'['
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_1'
op|')'
op|','
nl|'\n'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_3'
op|')'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci_3'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'set_hvdevs'
op|'('
name|'fake_pci_devs'
op|')'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_devs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dev'
op|'.'
name|'compute_node_id'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_clean_usage
name|'def'
name|'test_clean_usage'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_2'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'inst_2'
op|'.'
name|'uuid'
op|'='
string|"'uuid5'"
newline|'\n'
name|'migr'
op|'='
op|'{'
string|"'instance_uuid'"
op|':'
string|"'uuid2'"
op|','
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|'}'
newline|'\n'
name|'orph'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'uuid3'"
op|','
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
nl|'\n'
op|'['
op|'{'
string|"'count'"
op|':'
number|'1'
op|','
string|"'spec'"
op|':'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|'}'
op|']'
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
nl|'\n'
op|'['
op|'{'
string|"'count'"
op|':'
number|'1'
op|','
string|"'spec'"
op|':'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|'}'
op|']'
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'inst_2'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'free_devs'
op|'['
number|'0'
op|']'
op|'['
string|"'vendor_id'"
op|']'
op|','
string|"'v'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'clean_usage'
op|'('
op|'['
name|'self'
op|'.'
name|'inst'
op|']'
op|','
op|'['
name|'migr'
op|']'
op|','
op|'['
name|'orph'
op|']'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
name|'dev'
name|'in'
name|'free_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v'"
op|','
string|"'v1'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_clean_usage_claims
name|'def'
name|'test_clean_usage_claims'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_2'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'inst_2'
op|'.'
name|'uuid'
op|'='
string|"'uuid5'"
newline|'\n'
name|'migr'
op|'='
op|'{'
string|"'instance_uuid'"
op|':'
string|"'uuid2'"
op|','
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|'}'
newline|'\n'
name|'orph'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'uuid3'"
op|','
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
nl|'\n'
op|'['
op|'{'
string|"'count'"
op|':'
number|'1'
op|','
string|"'spec'"
op|':'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v'"
op|'}'
op|']'
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_instance'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
nl|'\n'
op|'['
op|'{'
string|"'count'"
op|':'
number|'1'
op|','
string|"'spec'"
op|':'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|'}'
op|']'
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_migration'
op|'('
name|'None'
op|','
name|'inst_2'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'clean_usage'
op|'('
op|'['
name|'self'
op|'.'
name|'inst'
op|']'
op|','
op|'['
name|'migr'
op|']'
op|','
op|'['
name|'orph'
op|']'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'free_devs'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
name|'dev'
name|'in'
name|'free_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v'"
op|','
string|"'v1'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstancePCIRequests.get_by_instance'"
op|')'
newline|'\n'
DECL|member|test_clean_usage_no_request_match_no_claims
name|'def'
name|'test_clean_usage_no_request_match_no_claims'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
comment|'# Tests the case that there is no match for the request so the'
nl|'\n'
comment|'# claims mapping is set to None for the instance when the tracker'
nl|'\n'
comment|'# calls clean_usage.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_pci_requests_object'
op|'('
name|'mock_get'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'update_pci_for_migration'
op|'('
name|'None'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'inst'
op|','
name|'sign'
op|'='
number|'1'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'free_devs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'clean_usage'
op|'('
op|'['
op|']'
op|','
op|'['
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'free_devs'
op|'='
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'pci_stats'
op|'.'
name|'get_free_devs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'free_devs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'address'"
op|']'
name|'for'
name|'dev'
name|'in'
name|'free_devs'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'0000:00:00.1'"
op|','
string|"'0000:00:00.2'"
op|','
string|"'0000:00:00.3'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciGetInstanceDevs
dedent|''
dedent|''
name|'class'
name|'PciGetInstanceDevs'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_devs_non_object
indent|'    '
name|'def'
name|'test_get_devs_non_object'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_fake_pci_device_get_by_instance_uuid
indent|'        '
name|'def'
name|'_fake_pci_device_get_by_instance_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_get_by_uuid'
op|'='
name|'True'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'pci_device_get_all_by_instance_uuid'"
op|','
nl|'\n'
name|'_fake_pci_device_get_by_instance_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_get_by_uuid'
op|'='
name|'False'
newline|'\n'
name|'pci_manager'
op|'.'
name|'get_instance_pci_devs'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_get_by_uuid'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_devs_object
dedent|''
name|'def'
name|'test_get_devs_object'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_fake_obj_load_attr
indent|'        '
name|'def'
name|'_fake_obj_load_attr'
op|'('
name|'foo'
op|','
name|'attrname'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'attrname'
op|'=='
string|"'pci_devices'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'load_attr_called'
op|'='
name|'True'
newline|'\n'
name|'foo'
op|'.'
name|'pci_devices'
op|'='
name|'objects'
op|'.'
name|'PciDeviceList'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'inst'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'id'
op|'='
string|"'1'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'ctxt'
op|','
string|"'1'"
op|','
name|'columns_to_join'
op|'='
op|'['
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'inst'
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
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'get_by_id'
op|'('
name|'ctxt'
op|','
string|"'1'"
op|','
name|'expected_attrs'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'objects'
op|'.'
name|'Instance'
op|','
string|"'obj_load_attr'"
op|','
name|'_fake_obj_load_attr'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'load_attr_called'
op|'='
name|'False'
newline|'\n'
name|'pci_manager'
op|'.'
name|'get_instance_pci_devs'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'load_attr_called'
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
