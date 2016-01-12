begin_unit
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
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'six'
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
name|'devspec'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|dev
name|'dev'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"5057"'
op|','
nl|'\n'
string|'"address"'
op|':'
string|'"1234:5678:8988.5"'
op|','
nl|'\n'
string|'"parent_addr"'
op|':'
string|'"0000:0a:00.0"'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciAddressTestCase
name|'class'
name|'PciAddressTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_wrong_address
indent|'    '
name|'def'
name|'test_wrong_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
string|'"address"'
op|':'
string|'"*: *: *.6"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"5057"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_address_too_big
dedent|''
name|'def'
name|'test_address_too_big'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'"0000:0a:0b:00.5"'
op|','
nl|'\n'
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceWrongAddressFormat'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_address_invalid_character
dedent|''
name|'def'
name|'test_address_invalid_character'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'"0000:h4.12:6"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceWrongAddressFormat'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_func
dedent|''
name|'def'
name|'test_max_func'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'"0000:0a:00.%s"'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_FUNC'
op|'+'
number|'1'
op|')'
op|','
nl|'\n'
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceInvalidAddressField'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
name|'msg'
op|'='
op|'('
string|"'Invalid PCI Whitelist: '"
nl|'\n'
string|"'The PCI address 0000:0a:00.%s has an invalid function.'"
nl|'\n'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_FUNC'
op|'+'
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_domain
dedent|''
name|'def'
name|'test_max_domain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'"%x:0a:00.5"'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_DOMAIN'
op|'+'
number|'1'
op|')'
op|','
nl|'\n'
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
name|'msg'
op|'='
op|'('
string|"'Invalid PCI devices Whitelist config invalid domain %x'"
nl|'\n'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_DOMAIN'
op|'+'
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_bus
dedent|''
name|'def'
name|'test_max_bus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'"0000:%x:00.5"'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_BUS'
op|'+'
number|'1'
op|')'
op|','
nl|'\n'
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
name|'msg'
op|'='
op|'('
string|"'Invalid PCI devices Whitelist config invalid bus %x'"
nl|'\n'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_BUS'
op|'+'
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_slot
dedent|''
name|'def'
name|'test_max_slot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'"0000:0a:%x.5"'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_SLOT'
op|'+'
number|'1'
op|')'
op|','
nl|'\n'
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
name|'msg'
op|'='
op|'('
string|"'Invalid PCI devices Whitelist config invalid slot %x'"
nl|'\n'
op|'%'
op|'('
name|'devspec'
op|'.'
name|'MAX_SLOT'
op|'+'
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_address_is_undefined
dedent|''
name|'def'
name|'test_address_is_undefined'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
string|'"product_id"'
op|':'
string|'"5057"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_partial_address
dedent|''
name|'def'
name|'test_partial_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'":0a:00."'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'dev'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"1137"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"0071"'
op|','
nl|'\n'
string|'"address"'
op|':'
string|'"0000:0a:00.5"'
op|','
nl|'\n'
string|'"parent_addr"'
op|':'
string|'"0000:0a:00.0"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
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
string|"'nova.pci.utils.is_physical_function'"
op|','
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|member|test_address_is_pf
name|'def'
name|'test_address_is_pf'
op|'('
name|'self'
op|','
name|'mock_is_physical_function'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"address"'
op|':'
string|'"0000:0a:00.0"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDevSpecTestCase
dedent|''
dedent|''
name|'class'
name|'PciDevSpecTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_spec_match
indent|'    '
name|'def'
name|'test_spec_match'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
string|'"address"'
op|':'
string|'"*: *: *.5"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"5057"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_vendor_id
dedent|''
name|'def'
name|'test_invalid_vendor_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8087"'
op|','
string|'"address"'
op|':'
string|'"*: *: *.5"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"5057"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vendor_id_out_of_range
dedent|''
name|'def'
name|'test_vendor_id_out_of_range'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"80860"'
op|','
string|'"address"'
op|':'
string|'"*:*:*.5"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"5057"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Invalid PCI devices Whitelist config "'
nl|'\n'
string|'"invalid vendor_id 80860"'
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_product_id
dedent|''
name|'def'
name|'test_invalid_product_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
string|'"address"'
op|':'
string|'"*: *: *.5"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"5056"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_product_id_out_of_range
dedent|''
name|'def'
name|'test_product_id_out_of_range'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
string|'"address"'
op|':'
string|'"*:*:*.5"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"50570"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Invalid PCI devices Whitelist config "'
nl|'\n'
string|'"invalid product_id 50570"'
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_devname_and_address
dedent|''
name|'def'
name|'test_devname_and_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"devname"'
op|':'
string|'"eth0"'
op|','
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
nl|'\n'
string|'"address"'
op|':'
string|'"*:*:*.5"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceInvalidDeviceName'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.pci.utils.get_function_by_ifname'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'('
string|'"0000:0a:00.0"'
op|','
name|'True'
op|')'
op|')'
newline|'\n'
DECL|member|test_by_name
name|'def'
name|'test_by_name'
op|'('
name|'self'
op|','
name|'mock_get_function_by_ifname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"devname"'
op|':'
string|'"eth0"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'pci'
op|'.'
name|'match'
op|'('
name|'dev'
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
string|"'nova.pci.utils.get_function_by_ifname'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'('
name|'None'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
DECL|member|test_invalid_name
name|'def'
name|'test_invalid_name'
op|'('
name|'self'
op|','
name|'mock_get_function_by_ifname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"devname"'
op|':'
string|'"lo"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|','
nl|'\n'
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|','
name|'pci_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'PCI device lo not found'"
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pci_obj
dedent|''
name|'def'
name|'test_pci_obj'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_info'
op|'='
op|'{'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
string|'"address"'
op|':'
string|'"*:*:*.5"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"5057"'
op|','
string|'"physical_network"'
op|':'
string|'"hr_net"'
op|'}'
newline|'\n'
nl|'\n'
name|'pci'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'pci_info'
op|')'
newline|'\n'
name|'pci_dev'
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
string|"'0000:00:00.5'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'5057'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'8086'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'parent_addr'"
op|':'
name|'None'
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
name|'pci_obj'
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
name|'assertTrue'
op|'('
name|'pci'
op|'.'
name|'match_pci_obj'
op|'('
name|'pci_obj'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
