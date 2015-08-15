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
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
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
name|'exception'
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
name|'instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'pci_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
DECL|variable|dev_dict
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
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|'}'
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
string|"'a'"
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
string|"'numa_node'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'dev_type'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'STANDARD'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
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
nl|'\n'
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
string|"'a1'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'p1'"
op|','
nl|'\n'
string|"'numa_node'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'dev_type'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'STANDARD'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
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
nl|'\n'
nl|'\n'
DECL|class|_TestPciDeviceObject
name|'class'
name|'_TestPciDeviceObject'
op|'('
name|'object'
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
name|'instance'
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
name|'pci_device'
op|'.'
name|'PciDeviceList'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_fake_pci_device
dedent|''
name|'def'
name|'_create_fake_pci_device'
op|'('
name|'self'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'ctxt'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'pci_device_get_by_addr'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_get_by_addr'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
string|"'a'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_db_dev'
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
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'get_by_dev_addr'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
string|"'a'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_pci_device
dedent|''
name|'def'
name|'test_create_pci_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'product_id'
op|','
string|"'p'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'compute_node_id'"
op|','
string|"'product_id'"
op|','
string|"'vendor_id'"
op|','
nl|'\n'
string|"'numa_node'"
op|','
string|"'status'"
op|','
string|"'address'"
op|','
string|"'extra_info'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_device_extra_info
dedent|''
name|'def'
name|'test_pci_device_extra_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'dev_dict'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dev_dict'
op|'['
string|"'k1'"
op|']'
op|'='
string|"'v1'"
newline|'\n'
name|'self'
op|'.'
name|'dev_dict'
op|'['
string|"'k2'"
op|']'
op|'='
string|"'v2'"
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'dev_dict'
op|')'
newline|'\n'
name|'extra_value'
op|'='
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'extra_info'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'extra_value'
op|'.'
name|'get'
op|'('
string|"'k1'"
op|')'
op|','
string|"'v1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'extra_value'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
name|'set'
op|'('
op|'('
string|"'k1'"
op|','
string|"'k2'"
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'compute_node_id'"
op|','
string|"'address'"
op|','
string|"'product_id'"
op|','
nl|'\n'
string|"'vendor_id'"
op|','
string|"'numa_node'"
op|','
string|"'status'"
op|','
nl|'\n'
string|"'extra_info'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_device
dedent|''
name|'def'
name|'test_update_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'changes'
op|'='
op|'{'
string|"'product_id'"
op|':'
string|"'p2'"
op|','
string|"'vendor_id'"
op|':'
string|"'v2'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'update_device'
op|'('
name|'changes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'vendor_id'
op|','
string|"'v2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'vendor_id'"
op|','
string|"'product_id'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_device_same_value
dedent|''
name|'def'
name|'test_update_device_same_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'changes'
op|'='
op|'{'
string|"'product_id'"
op|':'
string|"'p'"
op|','
string|"'vendor_id'"
op|':'
string|"'v2'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'update_device'
op|'('
name|'changes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'product_id'
op|','
string|"'p'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'vendor_id'
op|','
string|"'v2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'vendor_id'"
op|','
string|"'product_id'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_dev_addr
dedent|''
name|'def'
name|'test_get_by_dev_addr'
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
string|"'pci_device_get_by_addr'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_get_by_addr'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
string|"'a'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_db_dev'
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
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'get_by_dev_addr'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
string|"'a'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'product_id'
op|','
string|"'p'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_dev_id
dedent|''
name|'def'
name|'test_get_by_dev_id'
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
string|"'pci_device_get_by_id'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_get_by_id'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_db_dev'
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
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'get_by_dev_id'
op|'('
name|'ctxt'
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
name|'pci_device'
op|'.'
name|'product_id'
op|','
string|"'p'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
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
name|'_create_fake_pci_device'
op|'('
name|'ctxt'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'return_dev'
op|'='
name|'dict'
op|'('
name|'fake_db_dev'
op|','
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake-uuid-3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'instance_uuid'
op|'='
string|"'fake-uuid-2'"
newline|'\n'
name|'expected_updates'
op|'='
name|'dict'
op|'('
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake-uuid-2'"
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
string|"'pci_device_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_update'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
string|"'a'"
op|','
nl|'\n'
name|'expected_updates'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'return_dev'
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
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'status'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
string|"'fake-uuid-3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_no_extra_info
dedent|''
name|'def'
name|'test_save_no_extra_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return_dev'
op|'='
name|'dict'
op|'('
name|'fake_db_dev'
op|','
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake-uuid-3'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fake_update
name|'def'
name|'_fake_update'
op|'('
name|'ctxt'
op|','
name|'node_id'
op|','
name|'addr'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'extra_info'
op|'='
name|'updates'
op|'.'
name|'get'
op|'('
string|"'extra_info'"
op|')'
newline|'\n'
name|'return'
name|'return_dev'
newline|'\n'
nl|'\n'
dedent|''
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'pci_device_update'"
op|','
name|'_fake_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'_context'
op|'='
name|'ctxt'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'extra_info'
op|','
string|"'{}'"
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
name|'_create_fake_pci_device'
op|'('
name|'ctxt'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'REMOVED'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'pci_device_destroy'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_destroy'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
string|"'a'"
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
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'status'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'DELETED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_deleted
dedent|''
name|'def'
name|'test_save_deleted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_fake_destroy
indent|'        '
name|'def'
name|'_fake_destroy'
op|'('
name|'ctxt'
op|','
name|'node_id'
op|','
name|'addr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|function|_fake_update
dedent|''
name|'def'
name|'_fake_update'
op|'('
name|'ctxt'
op|','
name|'node_id'
op|','
name|'addr'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'called'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'pci_device_destroy'"
op|','
name|'_fake_destroy'
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
string|"'pci_device_update'"
op|','
name|'_fake_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_fake_pci_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'called'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_numa_node
dedent|''
name|'def'
name|'test_update_numa_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'numa_node'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'dev_dict'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dev_dict'
op|'['
string|"'numa_node'"
op|']'
op|'='
string|"'1'"
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'numa_node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_device_equivalent
dedent|''
name|'def'
name|'test_pci_device_equivalent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_device1'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'pci_device2'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pci_device1'
op|','
name|'pci_device2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_device_equivalent_with_ignore_field
dedent|''
name|'def'
name|'test_pci_device_equivalent_with_ignore_field'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_device1'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'pci_device2'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'pci_device2'
op|'.'
name|'updated_at'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pci_device1'
op|','
name|'pci_device2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_device_not_equivalent1
dedent|''
name|'def'
name|'test_pci_device_not_equivalent1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_device1'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'dev_dict2'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'dev_dict2'
op|'['
string|"'address'"
op|']'
op|'='
string|"'b'"
newline|'\n'
name|'pci_device2'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'pci_device1'
op|','
name|'pci_device2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_device_not_equivalent2
dedent|''
name|'def'
name|'test_pci_device_not_equivalent2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_device1'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'pci_device2'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'delattr'
op|'('
name|'pci_device2'
op|','
string|"'address'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'pci_device1'
op|','
name|'pci_device2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_device_not_equivalent_with_none
dedent|''
name|'def'
name|'test_pci_device_not_equivalent_with_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_device1'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'pci_device2'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'pci_device1'
op|'.'
name|'instance_uuid'
op|'='
string|"'aaa'"
newline|'\n'
name|'pci_device2'
op|'.'
name|'instance_uuid'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'pci_device1'
op|','
name|'pci_device2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_claim_device
dedent|''
name|'def'
name|'test_claim_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'claim'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devobj'
op|'.'
name|'status'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'CLAIMED'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devobj'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'uuid'
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
name|'inst'
op|'.'
name|'pci_devices'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_claim_device_fail
dedent|''
name|'def'
name|'test_claim_device_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|','
nl|'\n'
name|'devobj'
op|'.'
name|'claim'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_device
dedent|''
name|'def'
name|'test_allocate_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'claim'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'allocate'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devobj'
op|'.'
name|'status'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devobj'
op|'.'
name|'instance_uuid'
op|','
string|"'fake-inst-uuid'"
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
name|'inst'
op|'.'
name|'pci_devices'
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
name|'inst'
op|'.'
name|'pci_devices'
op|'['
number|'0'
op|']'
op|'.'
name|'vendor_id'
op|','
nl|'\n'
string|"'v'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'inst'
op|'.'
name|'pci_devices'
op|'['
number|'0'
op|']'
op|'.'
name|'status'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_device_fail_status
dedent|''
name|'def'
name|'test_allocate_device_fail_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'status'
op|'='
string|"'removed'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|','
nl|'\n'
name|'devobj'
op|'.'
name|'allocate'
op|','
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_device_fail_owner
dedent|''
name|'def'
name|'test_allocate_device_fail_owner'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'inst_2'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'inst_2'
op|'.'
name|'uuid'
op|'='
string|"'fake-inst-uuid-2'"
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'claim'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceInvalidOwner'
op|','
nl|'\n'
name|'devobj'
op|'.'
name|'allocate'
op|','
name|'inst_2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_free_claimed_device
dedent|''
name|'def'
name|'test_free_claimed_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'claim'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'free'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devobj'
op|'.'
name|'status'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'devobj'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_free_allocated_device
dedent|''
name|'def'
name|'test_free_allocated_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'ctx'
op|','
name|'pci_device'
op|'.'
name|'PciDevice'
op|'('
op|')'
op|','
name|'fake_db_dev'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'claim'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'allocate'
op|'('
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
name|'inst'
op|'.'
name|'pci_devices'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'free'
op|'('
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
name|'inst'
op|'.'
name|'pci_devices'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devobj'
op|'.'
name|'status'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'AVAILABLE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'devobj'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_free_device_fail
dedent|''
name|'def'
name|'test_free_device_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'REMOVED'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|','
name|'devobj'
op|'.'
name|'free'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_device
dedent|''
name|'def'
name|'test_remove_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'remove'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devobj'
op|'.'
name|'status'
op|','
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'REMOVED'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'devobj'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_device_fail
dedent|''
name|'def'
name|'test_remove_device_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'devobj'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'devobj'
op|'.'
name|'claim'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceInvalidStatus'
op|','
name|'devobj'
op|'.'
name|'remove'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestPciDeviceObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestPciDeviceObject
name|'_TestPciDeviceObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestPciDeviceObjectRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestPciDeviceObjectRemote
name|'_TestPciDeviceObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_pci_devs
dedent|''
name|'fake_pci_devs'
op|'='
op|'['
name|'fake_db_dev'
op|','
name|'fake_db_dev_1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestPciDeviceListObject
name|'class'
name|'_TestPciDeviceListObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_by_compute_node
indent|'    '
name|'def'
name|'test_get_by_compute_node'
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
string|"'pci_device_get_all_by_node'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_get_all_by_node'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_pci_devs'
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
name|'devs'
op|'='
name|'pci_device'
op|'.'
name|'PciDeviceList'
op|'.'
name|'get_by_compute_node'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'fake_pci_devs'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'devs'
op|'['
name|'i'
op|']'
op|','
name|'pci_device'
op|'.'
name|'PciDevice'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_pci_devs'
op|'['
name|'i'
op|']'
op|'['
string|"'vendor_id'"
op|']'
op|','
name|'devs'
op|'['
name|'i'
op|']'
op|'.'
name|'vendor_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_instance_uuid
dedent|''
dedent|''
name|'def'
name|'test_get_by_instance_uuid'
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
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_db_1'
op|'='
name|'dict'
op|'('
name|'fake_db_dev'
op|','
name|'address'
op|'='
string|"'a1'"
op|','
nl|'\n'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'1'"
op|')'
newline|'\n'
name|'fake_db_2'
op|'='
name|'dict'
op|'('
name|'fake_db_dev'
op|','
name|'address'
op|'='
string|"'a2'"
op|','
nl|'\n'
name|'status'
op|'='
name|'fields'
op|'.'
name|'PciDeviceStatus'
op|'.'
name|'ALLOCATED'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'1'"
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
string|"'pci_device_get_all_by_instance_uuid'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'pci_device_get_all_by_instance_uuid'
op|'('
name|'ctxt'
op|','
string|"'1'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
name|'fake_db_1'
op|','
name|'fake_db_2'
op|']'
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
name|'devs'
op|'='
name|'pci_device'
op|'.'
name|'PciDeviceList'
op|'.'
name|'get_by_instance_uuid'
op|'('
name|'ctxt'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'devs'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'fake_pci_devs'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'devs'
op|'['
name|'i'
op|']'
op|','
name|'pci_device'
op|'.'
name|'PciDevice'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devs'
op|'['
number|'0'
op|']'
op|'.'
name|'vendor_id'
op|','
string|"'v'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'devs'
op|'['
number|'1'
op|']'
op|'.'
name|'vendor_id'
op|','
string|"'v'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestPciDeviceListObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestPciDeviceListObject
name|'_TestPciDeviceListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestPciDeviceListObjectRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestPciDeviceListObjectRemote
name|'_TestPciDeviceListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
