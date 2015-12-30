begin_unit
comment|'# Copyright (c) 2013 Intel, Inc.'
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
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
name|'import'
name|'builtins'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDeviceMatchTestCase
name|'class'
name|'PciDeviceMatchTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
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
name|'PciDeviceMatchTestCase'
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
name|'fake_pci_1'
op|'='
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|','
nl|'\n'
string|"'device_id'"
op|':'
string|"'d1'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_single_spec_match
dedent|''
name|'def'
name|'test_single_spec_match'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'pci_device_prop_match'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_pci_1'
op|','
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|','
string|"'device_id'"
op|':'
string|"'d1'"
op|'}'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_spec_match
dedent|''
name|'def'
name|'test_multiple_spec_match'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'pci_device_prop_match'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_pci_1'
op|','
nl|'\n'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|','
string|"'device_id'"
op|':'
string|"'d1'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'vendor_id'"
op|':'
string|"'v3'"
op|','
string|"'device_id'"
op|':'
string|"'d3'"
op|'}'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spec_dismatch
dedent|''
name|'def'
name|'test_spec_dismatch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'utils'
op|'.'
name|'pci_device_prop_match'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_pci_1'
op|','
nl|'\n'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v4'"
op|','
string|"'device_id'"
op|':'
string|"'d4'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'vendor_id'"
op|':'
string|"'v3'"
op|','
string|"'device_id'"
op|':'
string|"'d3'"
op|'}'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spec_extra_key
dedent|''
name|'def'
name|'test_spec_extra_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'utils'
op|'.'
name|'pci_device_prop_match'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_pci_1'
op|','
nl|'\n'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'v1'"
op|','
string|"'device_id'"
op|':'
string|"'d1'"
op|','
string|"'wrong_key'"
op|':'
string|"'k1'"
op|'}'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDeviceAddressParserTestCase
dedent|''
dedent|''
name|'class'
name|'PciDeviceAddressParserTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_parse_address
indent|'    '
name|'def'
name|'test_parse_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'parse_result'
op|'='
name|'utils'
op|'.'
name|'parse_address'
op|'('
string|'"0000:04:12.6"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'parse_result'
op|','
op|'('
string|"'0000'"
op|','
string|"'04'"
op|','
string|"'12'"
op|','
string|"'6'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parse_address_wrong
dedent|''
name|'def'
name|'test_parse_address_wrong'
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
name|'PciDeviceWrongAddressFormat'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'parse_address'
op|','
string|'"0000:04.12:6"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parse_address_invalid_character
dedent|''
name|'def'
name|'test_parse_address_invalid_character'
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
name|'PciDeviceWrongAddressFormat'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'parse_address'
op|','
string|'"0000:h4.12:6"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetFunctionByIfnameTestCase
dedent|''
dedent|''
name|'class'
name|'GetFunctionByIfnameTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.path.isdir'"
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
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'readlink'"
op|')'
newline|'\n'
DECL|member|test_virtual_function
name|'def'
name|'test_virtual_function'
op|'('
name|'self'
op|','
name|'mock_readlink'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_readlink'
op|'.'
name|'return_value'
op|'='
string|"'../../../0000.00.00.1'"
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
nl|'\n'
name|'builtins'
op|','
string|"'open'"
op|','
name|'side_effect'
op|'='
name|'IOError'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|','
name|'physical_function'
op|'='
name|'utils'
op|'.'
name|'get_function_by_ifname'
op|'('
string|"'eth0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|','
string|"'0000.00.00.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'physical_function'
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
string|"'os.path.isdir'"
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
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'readlink'"
op|')'
newline|'\n'
DECL|member|test_physical_function
name|'def'
name|'test_physical_function'
op|'('
name|'self'
op|','
name|'mock_readlink'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_readlink'
op|'.'
name|'return_value'
op|'='
string|"'../../../0000:00:00.1'"
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
nl|'\n'
name|'builtins'
op|','
string|"'open'"
op|','
name|'mock'
op|'.'
name|'mock_open'
op|'('
name|'read_data'
op|'='
string|"'4'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|','
name|'physical_function'
op|'='
name|'utils'
op|'.'
name|'get_function_by_ifname'
op|'('
string|"'eth0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|','
string|"'0000:00:00.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'physical_function'
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
string|"'os.path.isdir'"
op|','
name|'return_value'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|member|test_exception
name|'def'
name|'test_exception'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'address'
op|','
name|'physical_function'
op|'='
name|'utils'
op|'.'
name|'get_function_by_ifname'
op|'('
string|"'lo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'physical_function'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IsPhysicalFunctionTestCase
dedent|''
dedent|''
name|'class'
name|'IsPhysicalFunctionTestCase'
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
name|'IsPhysicalFunctionTestCase'
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
name|'pci_args'
op|'='
name|'utils'
op|'.'
name|'get_pci_address_fields'
op|'('
string|"'0000:00:00.1'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.path.isdir'"
op|','
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|member|test_virtual_function
name|'def'
name|'test_virtual_function'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
nl|'\n'
name|'builtins'
op|','
string|"'open'"
op|','
name|'side_effect'
op|'='
name|'IOError'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'utils'
op|'.'
name|'is_physical_function'
op|'('
op|'*'
name|'self'
op|'.'
name|'pci_args'
op|')'
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
string|"'os.path.isdir'"
op|','
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|member|test_physical_function
name|'def'
name|'test_physical_function'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
nl|'\n'
name|'builtins'
op|','
string|"'open'"
op|','
name|'mock'
op|'.'
name|'mock_open'
op|'('
name|'read_data'
op|'='
string|"'4'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'is_physical_function'
op|'('
op|'*'
name|'self'
op|'.'
name|'pci_args'
op|')'
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
string|"'os.path.isdir'"
op|','
name|'return_value'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|member|test_exception
name|'def'
name|'test_exception'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'utils'
op|'.'
name|'is_physical_function'
op|'('
op|'*'
name|'self'
op|'.'
name|'pci_args'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetIfnameByPciAddressTestCase
dedent|''
dedent|''
name|'class'
name|'GetIfnameByPciAddressTestCase'
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
name|'GetIfnameByPciAddressTestCase'
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
name|'pci_address'
op|'='
string|"'0000:00:00.1'"
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
DECL|member|test_physical_function_inferface_name
name|'def'
name|'test_physical_function_inferface_name'
op|'('
name|'self'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
newline|'\n'
name|'ifname'
op|'='
name|'utils'
op|'.'
name|'get_ifname_by_pci_address'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'pci_address'
op|','
name|'pf_interface'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ifname'
op|','
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
DECL|member|test_virtual_function_inferface_name
name|'def'
name|'test_virtual_function_inferface_name'
op|'('
name|'self'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
newline|'\n'
name|'ifname'
op|'='
name|'utils'
op|'.'
name|'get_ifname_by_pci_address'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'pci_address'
op|','
name|'pf_interface'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ifname'
op|','
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
DECL|member|test_exception
name|'def'
name|'test_exception'
op|'('
name|'self'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_listdir'
op|'.'
name|'side_effect'
op|'='
name|'OSError'
op|'('
string|"'No such file or directory'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_ifname_by_pci_address'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pci_address'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetMacByPciAddressTestCase
dedent|''
dedent|''
name|'class'
name|'GetMacByPciAddressTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
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
name|'GetMacByPciAddressTestCase'
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
name|'pci_address'
op|'='
string|"'0000:07:00.1'"
newline|'\n'
name|'self'
op|'.'
name|'if_name'
op|'='
string|"'enp7s0f1'"
newline|'\n'
name|'self'
op|'.'
name|'tmpdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'tmpdir'
op|'.'
name|'path'
op|','
string|'"address"'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'fake_file'
op|','
string|'"w"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
string|'"a0:36:9f:72:00:00\\n"'
op|')'
newline|'\n'
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
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'join'"
op|')'
newline|'\n'
DECL|member|test_get_mac
name|'def'
name|'test_get_mac'
op|'('
name|'self'
op|','
name|'mock_join'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'if_name'
op|']'
newline|'\n'
name|'mock_join'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_file'
newline|'\n'
name|'mac'
op|'='
name|'utils'
op|'.'
name|'get_mac_by_pci_address'
op|'('
name|'self'
op|'.'
name|'pci_address'
op|')'
newline|'\n'
name|'mock_join'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
string|'"/sys/bus/pci/devices/%s/net"'
op|'%'
name|'self'
op|'.'
name|'pci_address'
op|','
name|'self'
op|'.'
name|'if_name'
op|','
nl|'\n'
string|'"address"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"a0:36:9f:72:00:00"'
op|','
name|'mac'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'join'"
op|')'
newline|'\n'
DECL|member|test_get_mac_fails
name|'def'
name|'test_get_mac_fails'
op|'('
name|'self'
op|','
name|'mock_join'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'self'
op|'.'
name|'fake_file'
op|')'
newline|'\n'
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'if_name'
op|']'
newline|'\n'
name|'mock_join'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_file'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_mac_by_pci_address'
op|','
name|'self'
op|'.'
name|'pci_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'join'"
op|')'
newline|'\n'
DECL|member|test_get_mac_fails_empty
name|'def'
name|'test_get_mac_fails_empty'
op|'('
name|'self'
op|','
name|'mock_join'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'fake_file'
op|','
string|'"w"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'truncate'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'if_name'
op|']'
newline|'\n'
name|'mock_join'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_file'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_mac_by_pci_address'
op|','
name|'self'
op|'.'
name|'pci_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'join'"
op|')'
newline|'\n'
DECL|member|test_get_physical_function_mac
name|'def'
name|'test_get_physical_function_mac'
op|'('
name|'self'
op|','
name|'mock_join'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'if_name'
op|']'
newline|'\n'
name|'mock_join'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_file'
newline|'\n'
name|'mac'
op|'='
name|'utils'
op|'.'
name|'get_mac_by_pci_address'
op|'('
name|'self'
op|'.'
name|'pci_address'
op|','
name|'pf_interface'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_join'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
string|'"/sys/bus/pci/devices/%s/physfn/net"'
op|'%'
name|'self'
op|'.'
name|'pci_address'
op|','
nl|'\n'
name|'self'
op|'.'
name|'if_name'
op|','
string|'"address"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"a0:36:9f:72:00:00"'
op|','
name|'mac'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetVfNumByPciAddressTestCase
dedent|''
dedent|''
name|'class'
name|'GetVfNumByPciAddressTestCase'
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
name|'GetVfNumByPciAddressTestCase'
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
name|'pci_address'
op|'='
string|"'0000:00:00.1'"
newline|'\n'
name|'self'
op|'.'
name|'paths'
op|'='
op|'['
nl|'\n'
string|"'/sys/bus/pci/devices/0000:00:00.1/physfn/virtfn3'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'readlink'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'glob'
op|','
string|"'iglob'"
op|')'
newline|'\n'
DECL|member|test_vf_number_found
name|'def'
name|'test_vf_number_found'
op|'('
name|'self'
op|','
name|'mock_iglob'
op|','
name|'mock_readlink'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_iglob'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'paths'
newline|'\n'
name|'mock_readlink'
op|'.'
name|'return_value'
op|'='
string|"'../../0000:00:00.1'"
newline|'\n'
name|'vf_num'
op|'='
name|'utils'
op|'.'
name|'get_vf_num_by_pci_address'
op|'('
name|'self'
op|'.'
name|'pci_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vf_num'
op|','
string|"'3'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'readlink'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'glob'
op|','
string|"'iglob'"
op|')'
newline|'\n'
DECL|member|test_vf_number_not_found
name|'def'
name|'test_vf_number_not_found'
op|'('
name|'self'
op|','
name|'mock_iglob'
op|','
name|'mock_readlink'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_iglob'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'paths'
newline|'\n'
name|'mock_readlink'
op|'.'
name|'return_value'
op|'='
string|"'../../0000:00:00.2'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_vf_num_by_pci_address'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pci_address'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'readlink'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'glob'
op|','
string|"'iglob'"
op|')'
newline|'\n'
DECL|member|test_exception
name|'def'
name|'test_exception'
op|'('
name|'self'
op|','
name|'mock_iglob'
op|','
name|'mock_readlink'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_iglob'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'paths'
newline|'\n'
name|'mock_readlink'
op|'.'
name|'side_effect'
op|'='
name|'OSError'
op|'('
string|"'No such file or directory'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_vf_num_by_pci_address'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pci_address'
nl|'\n'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
