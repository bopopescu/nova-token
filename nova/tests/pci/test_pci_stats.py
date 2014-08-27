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
name|'mock'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
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
name|'pci_stats'
name|'as'
name|'pci'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'pci_whitelist'
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
name|'pci'
name|'import'
name|'pci_fakes'
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
string|"'request_id'"
op|':'
name|'None'
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
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|spec
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|'}'
op|']'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|spec
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v2'"
op|'}'
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|pci_requests_multiple
name|'pci_requests_multiple'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|spec
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|'}'
op|']'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstancePCIRequest'
op|'('
name|'count'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|spec
name|'spec'
op|'='
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v2'"
op|'}'
op|']'
op|')'
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
name|'NoDBTestCase'
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
name|'objects'
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
name|'objects'
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
name|'objects'
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
comment|'# The following two calls need to be made before adding the devices.'
nl|'\n'
name|'patcher'
op|'='
name|'pci_fakes'
op|'.'
name|'fake_pci_whitelist'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'patcher'
op|'.'
name|'stop'
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
name|'remove_device'
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
name|'remove_device'
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
name|'remove_device'
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
nl|'\n'
DECL|member|test_consume_requests
dedent|''
name|'def'
name|'test_consume_requests'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'devs'
op|'='
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'consume_requests'
op|'('
name|'pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'devs'
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
string|"'v1'"
op|','
string|"'v2'"
op|']'
op|')'
op|','
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
name|'devs'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_consume_requests_empty
dedent|''
name|'def'
name|'test_consume_requests_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'devs'
op|'='
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'consume_requests'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'devs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_consume_requests_failed
dedent|''
name|'def'
name|'test_consume_requests_failed'
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
name|'consume_requests'
op|','
nl|'\n'
name|'pci_requests_multiple'
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
op|'.'
name|'object'
op|'('
name|'pci_whitelist'
op|','
string|"'get_pci_devices_filter'"
op|')'
newline|'\n'
DECL|class|PciDeviceStatsWithTagsTestCase
name|'class'
name|'PciDeviceStatsWithTagsTestCase'
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
name|'PciDeviceStatsWithTagsTestCase'
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
name|'_create_whitelist'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_whitelist
dedent|''
name|'def'
name|'_create_whitelist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'white_list'
op|'='
op|'['
string|'\'{"vendor_id":"1137","product_id":"0071",\''
nl|'\n'
string|'\'"address":"*:0a:00.*","physical_network":"physnet1"}\''
op|','
nl|'\n'
string|'\'{"vendor_id":"1137","product_id":"0072"}\''
op|']'
newline|'\n'
name|'self'
op|'.'
name|'pci_wlist'
op|'='
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|'('
name|'white_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_pci_devices
dedent|''
name|'def'
name|'_create_pci_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pci_tagged_devices'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'range'
op|'('
number|'4'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pci_dev'
op|'='
op|'{'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'0000:0a:00.%d'"
op|'%'
name|'dev'
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'1137'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'0071'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'pci_tagged_devices'
op|'.'
name|'append'
op|'('
name|'objects'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'pci_dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'pci_untagged_devices'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'range'
op|'('
number|'3'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pci_dev'
op|'='
op|'{'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'0000:0b:00.%d'"
op|'%'
name|'dev'
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'1137'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'0072'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'pci_untagged_devices'
op|'.'
name|'append'
op|'('
name|'objects'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'pci_dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'map'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'add_device'
op|','
name|'self'
op|'.'
name|'pci_tagged_devices'
op|')'
newline|'\n'
name|'map'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'add_device'
op|','
name|'self'
op|'.'
name|'pci_untagged_devices'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assertPoolContent
dedent|''
name|'def'
name|'_assertPoolContent'
op|'('
name|'self'
op|','
name|'pool'
op|','
name|'vendor_id'
op|','
name|'product_id'
op|','
name|'count'
op|','
op|'**'
name|'tags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vendor_id'
op|','
name|'pool'
op|'['
string|"'vendor_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'product_id'
op|','
name|'pool'
op|'['
string|"'product_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'count'
op|','
name|'pool'
op|'['
string|"'count'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'tags'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'tags'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'v'
op|','
name|'pool'
op|'['
name|'k'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assertPools
dedent|''
dedent|''
dedent|''
name|'def'
name|'_assertPools'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Pools are ordered based on the number of keys. 'product_id',"
nl|'\n'
comment|"# 'vendor_id' are always part of the keys. When tags are present,"
nl|'\n'
comment|'# they are also part of the keys. In this test class, we have'
nl|'\n'
comment|"# two pools with the second one having the tag 'physical_network'"
nl|'\n'
comment|"# and the value 'physnet1'"
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPoolContent'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'0'
op|']'
op|','
string|"'1137'"
op|','
string|"'0072'"
op|','
nl|'\n'
name|'len'
op|'('
name|'self'
op|'.'
name|'pci_untagged_devices'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_untagged_devices'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'0'
op|']'
op|'['
string|"'devices'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPoolContent'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'1'
op|']'
op|','
string|"'1137'"
op|','
string|"'0071'"
op|','
nl|'\n'
name|'len'
op|'('
name|'self'
op|'.'
name|'pci_tagged_devices'
op|')'
op|','
nl|'\n'
name|'physical_network'
op|'='
string|"'physnet1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pci_tagged_devices'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'1'
op|']'
op|'['
string|"'devices'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_devices
dedent|''
name|'def'
name|'test_add_devices'
op|'('
name|'self'
op|','
name|'mock_get_dev_filter'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_dev_filter'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'pci_wlist'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_devices'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPools'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_consume_reqeusts
dedent|''
name|'def'
name|'test_consume_reqeusts'
op|'('
name|'self'
op|','
name|'mock_get_dev_filter'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_dev_filter'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'pci_wlist'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_devices'
op|'('
op|')'
newline|'\n'
name|'pci_requests'
op|'='
op|'['
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
string|"'physical_network'"
op|':'
string|"'physnet1'"
op|'}'
op|']'
op|')'
op|','
nl|'\n'
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
string|"'1137'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'0072'"
op|'}'
op|']'
op|')'
op|']'
newline|'\n'
name|'devs'
op|'='
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'consume_requests'
op|'('
name|'pci_requests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'devs'
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
string|"'0071'"
op|','
string|"'0072'"
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
name|'dev'
op|'['
string|"'product_id'"
op|']'
name|'for'
name|'dev'
name|'in'
name|'devs'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPoolContent'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'0'
op|']'
op|','
string|"'1137'"
op|','
string|"'0072'"
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPoolContent'
op|'('
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'pools'
op|'['
number|'1'
op|']'
op|','
string|"'1137'"
op|','
string|"'0071'"
op|','
number|'3'
op|','
nl|'\n'
name|'physical_network'
op|'='
string|"'physnet1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_device_no_devspec
dedent|''
name|'def'
name|'test_add_device_no_devspec'
op|'('
name|'self'
op|','
name|'mock_get_dev_filter'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_dev_filter'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'pci_wlist'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_devices'
op|'('
op|')'
newline|'\n'
name|'pci_dev'
op|'='
op|'{'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'0000:0c:00.1'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'2345'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'0172'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'pci_dev_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'pci_dev'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'add_device'
op|'('
name|'pci_dev_obj'
op|')'
newline|'\n'
comment|'# There should be no change'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'_create_pool_keys_from_dev'
op|'('
name|'pci_dev_obj'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPools'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_device_no_devspec
dedent|''
name|'def'
name|'test_remove_device_no_devspec'
op|'('
name|'self'
op|','
name|'mock_get_dev_filter'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_dev_filter'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'pci_wlist'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_devices'
op|'('
op|')'
newline|'\n'
name|'pci_dev'
op|'='
op|'{'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'0000:0c:00.1'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'2345'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'0172'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'pci_dev_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'pci_dev'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'remove_device'
op|'('
name|'pci_dev_obj'
op|')'
newline|'\n'
comment|'# There should be no change'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'_create_pool_keys_from_dev'
op|'('
name|'pci_dev_obj'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPools'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_device
dedent|''
name|'def'
name|'test_remove_device'
op|'('
name|'self'
op|','
name|'mock_get_dev_filter'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_dev_filter'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'pci_wlist'
newline|'\n'
name|'self'
op|'.'
name|'_create_pci_devices'
op|'('
op|')'
newline|'\n'
name|'dev1'
op|'='
name|'self'
op|'.'
name|'pci_untagged_devices'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'remove_device'
op|'('
name|'dev1'
op|')'
newline|'\n'
name|'dev2'
op|'='
name|'self'
op|'.'
name|'pci_tagged_devices'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_stats'
op|'.'
name|'remove_device'
op|'('
name|'dev2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertPools'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
