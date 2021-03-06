begin_unit
comment|'# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.'
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
name|'nova'
name|'import'
name|'objects'
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
name|'fake_pci_device_pools'
name|'as'
name|'fake_pci'
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
nl|'\n'
DECL|class|_TestPciDevicePoolObject
name|'class'
name|'_TestPciDevicePoolObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_pci_pool_from_dict_not_distructive
indent|'    '
name|'def'
name|'test_pci_pool_from_dict_not_distructive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_dict'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'fake_pci'
op|'.'
name|'fake_pool_dict'
op|')'
newline|'\n'
name|'objects'
op|'.'
name|'PciDevicePool'
op|'.'
name|'from_dict'
op|'('
name|'test_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_pci'
op|'.'
name|'fake_pool_dict'
op|','
name|'test_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_pool_from_dict
dedent|''
name|'def'
name|'test_pci_pool_from_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevicePool'
op|'.'
name|'from_dict'
op|'('
name|'fake_pci'
op|'.'
name|'fake_pool_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool_obj'
op|'.'
name|'product_id'
op|','
string|"'fake-product'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool_obj'
op|'.'
name|'vendor_id'
op|','
string|"'fake-vendor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool_obj'
op|'.'
name|'numa_node'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool_obj'
op|'.'
name|'tags'
op|','
op|'{'
string|"'t1'"
op|':'
string|"'v1'"
op|','
string|"'t2'"
op|':'
string|"'v2'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool_obj'
op|'.'
name|'count'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_pool_from_dict_bad_tags
dedent|''
name|'def'
name|'test_pci_pool_from_dict_bad_tags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_dict'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_pci'
op|'.'
name|'fake_pool_dict'
op|')'
newline|'\n'
name|'bad_dict'
op|'['
string|"'bad'"
op|']'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'PciDevicePool'
op|'.'
name|'from_dict'
op|','
nl|'\n'
name|'value'
op|'='
name|'bad_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_pool_from_dict_no_tags
dedent|''
name|'def'
name|'test_pci_pool_from_dict_no_tags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dict_notag'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'fake_pci'
op|'.'
name|'fake_pool_dict'
op|')'
newline|'\n'
name|'dict_notag'
op|'.'
name|'pop'
op|'('
string|"'t1'"
op|')'
newline|'\n'
name|'dict_notag'
op|'.'
name|'pop'
op|'('
string|"'t2'"
op|')'
newline|'\n'
name|'pool_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevicePool'
op|'.'
name|'from_dict'
op|'('
name|'dict_notag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool_obj'
op|'.'
name|'tags'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_pool_to_dict
dedent|''
name|'def'
name|'test_pci_pool_to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tags'
op|'='
op|'{'
string|"'t1'"
op|':'
string|"'foo'"
op|','
string|"'t2'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
name|'pool_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevicePool'
op|'('
name|'product_id'
op|'='
string|"'pid'"
op|','
name|'tags'
op|'='
name|'tags'
op|')'
newline|'\n'
name|'pool_dict'
op|'='
name|'pool_obj'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'product_id'"
op|':'
string|"'pid'"
op|','
nl|'\n'
string|"'t1'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'t2'"
op|':'
string|"'bar'"
op|'}'
op|','
name|'pool_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_pool_to_dict_no_tags
dedent|''
name|'def'
name|'test_pci_pool_to_dict_no_tags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevicePool'
op|'('
name|'product_id'
op|'='
string|"'pid'"
op|','
name|'tags'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'pool_dict'
op|'='
name|'pool_obj'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'product_id'"
op|':'
string|"'pid'"
op|'}'
op|','
name|'pool_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_pool_to_dict_with_tags_unset
dedent|''
name|'def'
name|'test_pci_pool_to_dict_with_tags_unset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevicePool'
op|'('
name|'product_id'
op|'='
string|"'pid'"
op|')'
newline|'\n'
name|'pool_dict'
op|'='
name|'pool_obj'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'product_id'"
op|':'
string|"'pid'"
op|'}'
op|','
name|'pool_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_obj_make_compatible
dedent|''
name|'def'
name|'test_obj_make_compatible'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool_obj'
op|'='
name|'objects'
op|'.'
name|'PciDevicePool'
op|'('
name|'product_id'
op|'='
string|"'pid'"
op|','
name|'numa_node'
op|'='
number|'1'
op|')'
newline|'\n'
name|'primitive'
op|'='
name|'pool_obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'numa_node'"
op|','
name|'primitive'
op|'['
string|"'nova_object.data'"
op|']'
op|')'
newline|'\n'
name|'pool_obj'
op|'.'
name|'obj_make_compatible'
op|'('
name|'primitive'
op|'['
string|"'nova_object.data'"
op|']'
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'numa_node'"
op|','
name|'primitive'
op|'['
string|"'nova_object.data'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestPciDevicePoolObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestPciDevicePoolObject
name|'_TestPciDevicePoolObject'
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
name|'TestRemotePciDevicePoolObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemotePciDevicePoolObject
name|'_TestPciDevicePoolObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestConvertPciStats
dedent|''
name|'class'
name|'TestConvertPciStats'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_from_pci_stats_obj
indent|'    '
name|'def'
name|'test_from_pci_stats_obj'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prim'
op|'='
name|'fake_pci'
op|'.'
name|'fake_pool_list_primitive'
newline|'\n'
name|'pools'
op|'='
name|'pci_device_pool'
op|'.'
name|'from_pci_stats'
op|'('
name|'prim'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'pools'
op|','
name|'pci_device_pool'
op|'.'
name|'PciDevicePoolList'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'pools'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_pci_stats_dict
dedent|''
name|'def'
name|'test_from_pci_stats_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prim'
op|'='
name|'fake_pci'
op|'.'
name|'fake_pool_dict'
newline|'\n'
name|'pools'
op|'='
name|'pci_device_pool'
op|'.'
name|'from_pci_stats'
op|'('
name|'prim'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'pools'
op|','
name|'pci_device_pool'
op|'.'
name|'PciDevicePoolList'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'pools'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_pci_stats_list_of_dicts
dedent|''
name|'def'
name|'test_from_pci_stats_list_of_dicts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prim'
op|'='
name|'fake_pci'
op|'.'
name|'fake_pool_dict'
newline|'\n'
name|'pools'
op|'='
name|'pci_device_pool'
op|'.'
name|'from_pci_stats'
op|'('
op|'['
name|'prim'
op|','
name|'prim'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'pools'
op|','
name|'pci_device_pool'
op|'.'
name|'PciDevicePoolList'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'pools'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_pci_stats_bad
dedent|''
name|'def'
name|'test_from_pci_stats_bad'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prim'
op|'='
string|'"not a valid json string for an object"'
newline|'\n'
name|'pools'
op|'='
name|'pci_device_pool'
op|'.'
name|'from_pci_stats'
op|'('
name|'prim'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'pools'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
