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
nl|'\n'
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
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
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|PCI_VENDOR_PATTERN
name|'PCI_VENDOR_PATTERN'
op|'='
string|'"^(hex{4})$"'
op|'.'
name|'replace'
op|'('
string|'"hex"'
op|','
string|'"[\\da-fA-F]"'
op|')'
newline|'\n'
DECL|variable|_PCI_ADDRESS_PATTERN
name|'_PCI_ADDRESS_PATTERN'
op|'='
op|'('
string|'"^(hex{4}):(hex{2}):(hex{2}).(oct{1})$"'
op|'.'
nl|'\n'
name|'replace'
op|'('
string|'"hex"'
op|','
string|'"[\\da-fA-F]"'
op|')'
op|'.'
nl|'\n'
name|'replace'
op|'('
string|'"oct"'
op|','
string|'"[0-7]"'
op|')'
op|')'
newline|'\n'
DECL|variable|_PCI_ADDRESS_REGEX
name|'_PCI_ADDRESS_REGEX'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
name|'_PCI_ADDRESS_PATTERN'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_SRIOV_TOTALVFS
name|'_SRIOV_TOTALVFS'
op|'='
string|'"sriov_totalvfs"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pci_device_prop_match
name|'def'
name|'pci_device_prop_match'
op|'('
name|'pci_dev'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if the pci_dev meet spec requirement\n\n    Specs is a list of PCI device property requirements.\n    An example of device requirement that the PCI should be either:\n    a) Device with vendor_id as 0x8086 and product_id as 0x8259, or\n    b) Device with vendor_id as 0x10de and product_id as 0x10d8:\n\n    [{"vendor_id":"8086", "product_id":"8259"},\n     {"vendor_id":"10de", "product_id":"10d8"}]\n\n    """'
newline|'\n'
DECL|function|_matching_devices
name|'def'
name|'_matching_devices'
op|'('
name|'spec'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'all'
op|'('
name|'pci_dev'
op|'.'
name|'get'
op|'('
name|'k'
op|')'
op|'=='
name|'v'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'spec'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'any'
op|'('
name|'_matching_devices'
op|'('
name|'spec'
op|')'
name|'for'
name|'spec'
name|'in'
name|'specs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_address
dedent|''
name|'def'
name|'parse_address'
op|'('
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns (domain, bus, slot, function) from PCI address that is stored in\n    PciDevice DB table.\n    """'
newline|'\n'
name|'m'
op|'='
name|'_PCI_ADDRESS_REGEX'
op|'.'
name|'match'
op|'('
name|'address'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'m'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceWrongAddressFormat'
op|'('
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'m'
op|'.'
name|'groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pci_address_fields
dedent|''
name|'def'
name|'get_pci_address_fields'
op|'('
name|'pci_addr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'dbs'
op|','
name|'sep'
op|','
name|'func'
op|'='
name|'pci_addr'
op|'.'
name|'partition'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'domain'
op|','
name|'bus'
op|','
name|'slot'
op|'='
name|'dbs'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'return'
op|'('
name|'domain'
op|','
name|'bus'
op|','
name|'slot'
op|','
name|'func'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pci_address
dedent|''
name|'def'
name|'get_pci_address'
op|'('
name|'domain'
op|','
name|'bus'
op|','
name|'slot'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'%s:%s:%s.%s'"
op|'%'
op|'('
name|'domain'
op|','
name|'bus'
op|','
name|'slot'
op|','
name|'func'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_function_by_ifname
dedent|''
name|'def'
name|'get_function_by_ifname'
op|'('
name|'ifname'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Given the device name, returns the PCI address of a device\n    and returns True if the address in a physical function.\n    """'
newline|'\n'
name|'dev_path'
op|'='
string|'"/sys/class/net/%s/device"'
op|'%'
name|'ifname'
newline|'\n'
name|'sriov_totalvfs'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'dev_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|'# sriov_totalvfs contains the maximum possible VFs for this PF'
nl|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'dev_path'
op|'+'
name|'_SRIOV_TOTALVFS'
op|')'
name|'as'
name|'fd'
op|':'
newline|'\n'
indent|'                '
name|'sriov_totalvfs'
op|'='
name|'int'
op|'('
name|'fd'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'os'
op|'.'
name|'readlink'
op|'('
name|'dev_path'
op|')'
op|'.'
name|'strip'
op|'('
string|'"./"'
op|')'
op|','
nl|'\n'
name|'sriov_totalvfs'
op|'>'
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'IOError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'os'
op|'.'
name|'readlink'
op|'('
name|'dev_path'
op|')'
op|'.'
name|'strip'
op|'('
string|'"./"'
op|')'
op|','
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
op|','
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_physical_function
dedent|''
name|'def'
name|'is_physical_function'
op|'('
name|'domain'
op|','
name|'bus'
op|','
name|'slot'
op|','
name|'function'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'dev_path'
op|'='
string|'"/sys/bus/pci/devices/%(d)s:%(b)s:%(s)s.%(f)s/"'
op|'%'
op|'{'
nl|'\n'
string|'"d"'
op|':'
name|'domain'
op|','
string|'"b"'
op|':'
name|'bus'
op|','
string|'"s"'
op|':'
name|'slot'
op|','
string|'"f"'
op|':'
name|'function'
op|'}'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'dev_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sriov_totalvfs'
op|'='
number|'0'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'dev_path'
op|'+'
name|'_SRIOV_TOTALVFS'
op|')'
name|'as'
name|'fd'
op|':'
newline|'\n'
indent|'                '
name|'sriov_totalvfs'
op|'='
name|'int'
op|'('
name|'fd'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'sriov_totalvfs'
op|'>'
number|'0'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'IOError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_sysfs_netdev_path
dedent|''
name|'def'
name|'_get_sysfs_netdev_path'
op|'('
name|'pci_addr'
op|','
name|'pf_interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the sysfs path based on the PCI address of the device.\n\n    Assumes a networking device - will not check for the existence of the path.\n    """'
newline|'\n'
name|'if'
name|'pf_interface'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"/sys/bus/pci/devices/%s/physfn/net"'
op|'%'
op|'('
name|'pci_addr'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"/sys/bus/pci/devices/%s/net"'
op|'%'
op|'('
name|'pci_addr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ifname_by_pci_address
dedent|''
name|'def'
name|'get_ifname_by_pci_address'
op|'('
name|'pci_addr'
op|','
name|'pf_interface'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the interface name based on a VF\'s pci address\n\n    The returned interface name is either the parent PF\'s or that of the VF\n    itself based on the argument of pf_interface.\n    """'
newline|'\n'
name|'dev_path'
op|'='
name|'_get_sysfs_netdev_path'
op|'('
name|'pci_addr'
op|','
name|'pf_interface'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'dev_info'
op|'='
name|'os'
op|'.'
name|'listdir'
op|'('
name|'dev_path'
op|')'
newline|'\n'
name|'return'
name|'dev_info'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|'('
name|'id'
op|'='
name|'pci_addr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_mac_by_pci_address
dedent|''
dedent|''
name|'def'
name|'get_mac_by_pci_address'
op|'('
name|'pci_addr'
op|','
name|'pf_interface'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the MAC address of the nic based on it\'s PCI address\n\n    Raises PciDeviceNotFoundById in case the pci device is not a NIC\n    """'
newline|'\n'
name|'dev_path'
op|'='
name|'_get_sysfs_netdev_path'
op|'('
name|'pci_addr'
op|','
name|'pf_interface'
op|')'
newline|'\n'
name|'if_name'
op|'='
name|'get_ifname_by_pci_address'
op|'('
name|'pci_addr'
op|','
name|'pf_interface'
op|')'
newline|'\n'
name|'addr_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'dev_path'
op|','
name|'if_name'
op|','
string|"'address'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'addr_file'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'mac'
op|'='
name|'next'
op|'('
name|'f'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'return'
name|'mac'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'IOError'
op|','
name|'StopIteration'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Could not find the expected sysfs file for "'
nl|'\n'
string|'"determining the MAC address of the PCI device "'
nl|'\n'
string|'"%(addr)s. May not be a NIC. Error: %(e)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'addr'"
op|':'
name|'pci_addr'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|'('
name|'id'
op|'='
name|'pci_addr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vf_num_by_pci_address
dedent|''
dedent|''
name|'def'
name|'get_vf_num_by_pci_address'
op|'('
name|'pci_addr'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the VF number based on a VF\'s pci address\n\n    A VF is associated with an VF number, which ip link command uses to\n    configure it. This number can be obtained from the PCI device filesystem.\n    """'
newline|'\n'
name|'VIRTFN_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"virtfn(\\d+)"'
op|')'
newline|'\n'
name|'virtfns_path'
op|'='
string|'"/sys/bus/pci/devices/%s/physfn/virtfn*"'
op|'%'
op|'('
name|'pci_addr'
op|')'
newline|'\n'
name|'vf_num'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'vf_path'
name|'in'
name|'glob'
op|'.'
name|'iglob'
op|'('
name|'virtfns_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
name|'pci_addr'
op|','
name|'os'
op|'.'
name|'readlink'
op|'('
name|'vf_path'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'t'
op|'='
name|'VIRTFN_RE'
op|'.'
name|'search'
op|'('
name|'vf_path'
op|')'
newline|'\n'
name|'vf_num'
op|'='
name|'t'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'if'
name|'vf_num'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|'('
name|'id'
op|'='
name|'pci_addr'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'vf_num'
newline|'\n'
dedent|''
endmarker|''
end_unit
