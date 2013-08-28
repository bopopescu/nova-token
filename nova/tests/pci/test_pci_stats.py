begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'pci_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'pci_stats'
name|'as'
name|'pci'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|fake_pci_1
name|'fake_pci_1'
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
string|"'p1'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'extra_k1'"
op|':'
string|"'v1'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_pci_2
name|'fake_pci_2'
op|'='
name|'dict'
op|'('
name|'fake_pci_1'
op|','
name|'vendor_id'
op|'='
string|"'v2'"
op|','
nl|'\n'
DECL|variable|product_id
name|'product_id'
op|'='
string|"'p2'"
op|','
nl|'\n'
DECL|variable|address
name|'address'
op|'='
string|"'0000:00:00.2'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_pci_3
name|'fake_pci_3'
op|'='
name|'dict'
op|'('
name|'fake_pci_1'
op|','
name|'address'
op|'='
string|"'0000:00:00.3'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|pci_requests
name|'pci_requests'
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
string|"'v1'"
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
string|"'v2'"
op|'}'
op|']'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|pci_requests_multiple
name|'pci_requests_multiple'
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
string|"'v1'"
op|'}'
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'count'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'spec'"
op|':'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v2'"
op|'}'
op|']'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDeviceStatsTestCase
name|'class'
name|'PciDeviceStatsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_create_fake_devs
indent|'    '
name|'def'
name|'_create_fake_devs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fake_dev_1'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'fake_pci_1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_dev_2'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'fake_pci_2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_dev_3'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'fake_pci_3'
op|')'
newline|'\n'
nl|'\n'
name|'map'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'add_device'
op|','
nl|'\n'
op|'['
name|'self'
op|'.'
name|'fake_dev_1'
op|','
name|'self'
op|'.'
name|'fake_dev_2'
op|','
name|'self'
op|'.'
name|'fake_dev_3'
op|']'
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
name|'PciDeviceStatsTestCase'
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
name|'pci_stats'
op|'='
name|'pci'
op|'.'
name|'PciDeviceStats'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_fake_devs'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_device
dedent|''
name|'def'
name|'test_add_device'
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
name|'pci_stats'
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
name|'set'
op|'('
op|'['
name|'d'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
name|'d'
name|'in'
name|'self'
op|'.'
name|'pci_stats'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v1'"
op|','
string|"'v2'"
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
name|'d'
op|'['
string|"'count'"
op|']'
name|'for'
name|'d'
name|'in'
name|'self'
op|'.'
name|'pci_stats'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
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
name|'pci_stats'
op|'.'
name|'consume_device'
op|'('
name|'self'
op|'.'
name|'fake_dev_2'
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
name|'pci_stats'
op|'.'
name|'pools'
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
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'0'
op|']'
op|'['
string|"'count'"
op|']'
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
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'0'
op|']'
op|'['
string|"'vendor_id'"
op|']'
op|','
string|"'v1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_device_exception
dedent|''
name|'def'
name|'test_remove_device_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'consume_device'
op|'('
name|'self'
op|'.'
name|'fake_dev_2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDevicePoolEmpty'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'consume_device'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_dev_2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_json_creat
dedent|''
name|'def'
name|'test_json_creat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|')'
newline|'\n'
name|'new_stats'
op|'='
name|'pci'
op|'.'
name|'PciDeviceStats'
op|'('
name|'m'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'new_stats'
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
name|'set'
op|'('
op|'['
name|'d'
op|'['
string|"'count'"
op|']'
name|'for'
name|'d'
name|'in'
name|'new_stats'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
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
name|'d'
op|'['
string|"'vendor_id'"
op|']'
name|'for'
name|'d'
name|'in'
name|'new_stats'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'v1'"
op|','
string|"'v2'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_support_requests
dedent|''
name|'def'
name|'test_support_requests'
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
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'support_requests'
op|'('
name|'pci_requests'
op|')'
op|','
nl|'\n'
name|'True'
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
name|'pci_stats'
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
name|'set'
op|'('
op|'['
name|'d'
op|'['
string|"'count'"
op|']'
name|'for'
name|'d'
name|'in'
name|'self'
op|'.'
name|'pci_stats'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'('
number|'1'
op|','
number|'2'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_support_requests_failed
dedent|''
name|'def'
name|'test_support_requests_failed'
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
nl|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'support_requests'
op|'('
name|'pci_requests_multiple'
op|')'
op|','
name|'False'
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
name|'pci_stats'
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
name|'set'
op|'('
op|'['
name|'d'
op|'['
string|"'count'"
op|']'
name|'for'
name|'d'
name|'in'
name|'self'
op|'.'
name|'pci_stats'
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_requests
dedent|''
name|'def'
name|'test_apply_requests'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'apply_requests'
op|'('
name|'pci_requests'
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
name|'pci_stats'
op|'.'
name|'pools'
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
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'0'
op|']'
op|'['
string|"'vendor_id'"
op|']'
op|','
string|"'v1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'0'
op|']'
op|'['
string|"'count'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_requests_failed
dedent|''
name|'def'
name|'test_apply_requests_failed'
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
name|'exception'
op|'.'
name|'PciDeviceRequestFailed'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'apply_requests'
op|','
nl|'\n'
name|'pci_requests_multiple'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
