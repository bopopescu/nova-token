begin_unit
comment|'# Copyright (c) 2013 Intel, Inc.'
nl|'\n'
comment|'# Copyright (c) 2013 OpenStack Foundation'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
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
name|'_LE'
newline|'\n'
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
name|'pci'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'whitelist'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
nl|'\n'
DECL|class|PciDeviceStats
name|'class'
name|'PciDeviceStats'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""PCI devices summary information.\n\n    According to the PCI SR-IOV spec, a PCI physical function can have up to\n    256 PCI virtual functions, thus the number of assignable PCI functions in\n    a cloud can be big. The scheduler needs to know all device availability\n    information in order to determine which compute hosts can support a PCI\n    request. Passing individual virtual device information to the scheduler\n    does not scale, so we provide summary information.\n\n    Usually the virtual functions provided by a host PCI device have the same\n    value for most properties, like vendor_id, product_id and class type.\n    The PCI stats class summarizes this information for the scheduler.\n\n    The pci stats information is maintained exclusively by compute node\n    resource tracker and updated to database. The scheduler fetches the\n    information and selects the compute node accordingly. If a compute\n    node is selected, the resource tracker allocates the devices to the\n    instance and updates the pci stats information.\n\n    This summary information will be helpful for cloud management also.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|pool_keys
name|'pool_keys'
op|'='
op|'['
string|"'product_id'"
op|','
string|"'vendor_id'"
op|','
string|"'numa_node'"
op|','
string|"'dev_type'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stats'
op|'='
name|'None'
op|','
name|'dev_filter'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PciDeviceStats'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(sbauza): Stats are a PCIDevicePoolList object'
nl|'\n'
name|'self'
op|'.'
name|'pools'
op|'='
op|'['
name|'pci_pool'
op|'.'
name|'to_dict'
op|'('
op|')'
nl|'\n'
name|'for'
name|'pci_pool'
name|'in'
name|'stats'
op|']'
name|'if'
name|'stats'
name|'else'
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'pools'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'lambda'
name|'item'
op|':'
name|'len'
op|'('
name|'item'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dev_filter'
op|'='
name|'dev_filter'
name|'or'
name|'whitelist'
op|'.'
name|'Whitelist'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'pci_passthrough_whitelist'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_equal_properties
dedent|''
name|'def'
name|'_equal_properties'
op|'('
name|'self'
op|','
name|'dev'
op|','
name|'entry'
op|','
name|'matching_keys'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'all'
op|'('
name|'dev'
op|'.'
name|'get'
op|'('
name|'prop'
op|')'
op|'=='
name|'entry'
op|'.'
name|'get'
op|'('
name|'prop'
op|')'
nl|'\n'
name|'for'
name|'prop'
name|'in'
name|'matching_keys'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_find_pool
dedent|''
name|'def'
name|'_find_pool'
op|'('
name|'self'
op|','
name|'dev_pool'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the first pool that matches dev."""'
newline|'\n'
name|'for'
name|'pool'
name|'in'
name|'self'
op|'.'
name|'pools'
op|':'
newline|'\n'
indent|'            '
name|'pool_keys'
op|'='
name|'pool'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'del'
name|'pool_keys'
op|'['
string|"'count'"
op|']'
newline|'\n'
name|'del'
name|'pool_keys'
op|'['
string|"'devices'"
op|']'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'pool_keys'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'=='
name|'len'
op|'('
name|'dev_pool'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'_equal_properties'
op|'('
name|'dev_pool'
op|','
name|'pool_keys'
op|','
name|'dev_pool'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'pool'
newline|'\n'
nl|'\n'
DECL|member|_create_pool_keys_from_dev
dedent|''
dedent|''
dedent|''
name|'def'
name|'_create_pool_keys_from_dev'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""create a stats pool dict that this dev is supposed to be part of\n\n        Note that this pool dict contains the stats pool\'s keys and their\n        values. \'count\' and \'devices\' are not included.\n        """'
newline|'\n'
comment|"# Don't add a device that doesn't have a matching device spec."
nl|'\n'
comment|'# This can happen during initial sync up with the controller'
nl|'\n'
name|'devspec'
op|'='
name|'self'
op|'.'
name|'dev_filter'
op|'.'
name|'get_devspec'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'devspec'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'tags'
op|'='
name|'devspec'
op|'.'
name|'get_tags'
op|'('
op|')'
newline|'\n'
name|'pool'
op|'='
op|'{'
name|'k'
op|':'
name|'getattr'
op|'('
name|'dev'
op|','
name|'k'
op|')'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'pool_keys'
op|'}'
newline|'\n'
name|'if'
name|'tags'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'.'
name|'update'
op|'('
name|'tags'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'pool'
newline|'\n'
nl|'\n'
DECL|member|add_device
dedent|''
name|'def'
name|'add_device'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a device to its matching pool."""'
newline|'\n'
name|'dev_pool'
op|'='
name|'self'
op|'.'
name|'_create_pool_keys_from_dev'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'if'
name|'dev_pool'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'='
name|'self'
op|'.'
name|'_find_pool'
op|'('
name|'dev_pool'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pool'
op|':'
newline|'\n'
indent|'                '
name|'dev_pool'
op|'['
string|"'count'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'dev_pool'
op|'['
string|"'devices'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'pools'
op|'.'
name|'append'
op|'('
name|'dev_pool'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pools'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'lambda'
name|'item'
op|':'
name|'len'
op|'('
name|'item'
op|')'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'dev_pool'
newline|'\n'
dedent|''
name|'pool'
op|'['
string|"'count'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'pool'
op|'['
string|"'devices'"
op|']'
op|'.'
name|'append'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_decrease_pool_count
name|'def'
name|'_decrease_pool_count'
op|'('
name|'pool_list'
op|','
name|'pool'
op|','
name|'count'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Decrement pool\'s size by count.\n\n        If pool becomes empty, remove pool from pool_list.\n        """'
newline|'\n'
name|'if'
name|'pool'
op|'['
string|"'count'"
op|']'
op|'>'
name|'count'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'['
string|"'count'"
op|']'
op|'-='
name|'count'
newline|'\n'
name|'count'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'count'
op|'-='
name|'pool'
op|'['
string|"'count'"
op|']'
newline|'\n'
name|'pool_list'
op|'.'
name|'remove'
op|'('
name|'pool'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'count'
newline|'\n'
nl|'\n'
DECL|member|remove_device
dedent|''
name|'def'
name|'remove_device'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove one device from the first pool that it matches."""'
newline|'\n'
name|'dev_pool'
op|'='
name|'self'
op|'.'
name|'_create_pool_keys_from_dev'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'if'
name|'dev_pool'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'='
name|'self'
op|'.'
name|'_find_pool'
op|'('
name|'dev_pool'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pool'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'PciDevicePoolEmpty'
op|'('
nl|'\n'
name|'compute_node_id'
op|'='
name|'dev'
op|'.'
name|'compute_node_id'
op|','
name|'address'
op|'='
name|'dev'
op|'.'
name|'address'
op|')'
newline|'\n'
dedent|''
name|'pool'
op|'['
string|"'devices'"
op|']'
op|'.'
name|'remove'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_decrease_pool_count'
op|'('
name|'self'
op|'.'
name|'pools'
op|','
name|'pool'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_free_devs
dedent|''
dedent|''
name|'def'
name|'get_free_devs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'free_devs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'pool'
name|'in'
name|'self'
op|'.'
name|'pools'
op|':'
newline|'\n'
indent|'            '
name|'free_devs'
op|'.'
name|'extend'
op|'('
name|'pool'
op|'['
string|"'devices'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'free_devs'
newline|'\n'
nl|'\n'
DECL|member|consume_requests
dedent|''
name|'def'
name|'consume_requests'
op|'('
name|'self'
op|','
name|'pci_requests'
op|','
name|'numa_cells'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'alloc_devices'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'request'
name|'in'
name|'pci_requests'
op|':'
newline|'\n'
indent|'            '
name|'count'
op|'='
name|'request'
op|'.'
name|'count'
newline|'\n'
name|'spec'
op|'='
name|'request'
op|'.'
name|'spec'
newline|'\n'
comment|'# For now, keep the same algorithm as during scheduling:'
nl|'\n'
comment|'# a spec may be able to match multiple pools.'
nl|'\n'
name|'pools'
op|'='
name|'self'
op|'.'
name|'_filter_pools_for_spec'
op|'('
name|'self'
op|'.'
name|'pools'
op|','
name|'spec'
op|')'
newline|'\n'
name|'if'
name|'numa_cells'
op|':'
newline|'\n'
indent|'                '
name|'pools'
op|'='
name|'self'
op|'.'
name|'_filter_pools_for_numa_cells'
op|'('
name|'pools'
op|','
name|'numa_cells'
op|')'
newline|'\n'
dedent|''
name|'pools'
op|'='
name|'self'
op|'.'
name|'_filter_non_requested_pfs'
op|'('
name|'request'
op|','
name|'pools'
op|')'
newline|'\n'
comment|'# Failed to allocate the required number of devices'
nl|'\n'
comment|'# Return the devices already allocated back to their pools'
nl|'\n'
name|'if'
name|'sum'
op|'('
op|'['
name|'pool'
op|'['
string|"'count'"
op|']'
name|'for'
name|'pool'
name|'in'
name|'pools'
op|']'
op|')'
op|'<'
name|'count'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Failed to allocate PCI devices for instance."'
nl|'\n'
string|'" Unassigning devices back to pools."'
nl|'\n'
string|'" This should not happen, since the scheduler"'
nl|'\n'
string|'" should have accurate information, and allocation"'
nl|'\n'
string|'" during claims is controlled via a hold"'
nl|'\n'
string|'" on the compute node semaphore"'
op|')'
op|')'
newline|'\n'
name|'for'
name|'d'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'alloc_devices'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'add_device'
op|'('
name|'alloc_devices'
op|'.'
name|'pop'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'for'
name|'pool'
name|'in'
name|'pools'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'pool'
op|'['
string|"'count'"
op|']'
op|'>='
name|'count'
op|':'
newline|'\n'
indent|'                    '
name|'num_alloc'
op|'='
name|'count'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'num_alloc'
op|'='
name|'pool'
op|'['
string|"'count'"
op|']'
newline|'\n'
dedent|''
name|'count'
op|'-='
name|'num_alloc'
newline|'\n'
name|'pool'
op|'['
string|"'count'"
op|']'
op|'-='
name|'num_alloc'
newline|'\n'
name|'for'
name|'d'
name|'in'
name|'range'
op|'('
name|'num_alloc'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'pci_dev'
op|'='
name|'pool'
op|'['
string|"'devices'"
op|']'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_handle_device_dependents'
op|'('
name|'pci_dev'
op|')'
newline|'\n'
name|'pci_dev'
op|'.'
name|'request_id'
op|'='
name|'request'
op|'.'
name|'request_id'
newline|'\n'
name|'alloc_devices'
op|'.'
name|'append'
op|'('
name|'pci_dev'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'count'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'alloc_devices'
newline|'\n'
nl|'\n'
DECL|member|_handle_device_dependents
dedent|''
name|'def'
name|'_handle_device_dependents'
op|'('
name|'self'
op|','
name|'pci_dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove device dependents or a parent from pools.\n\n        In case the device is a PF, all of it\'s dependent VFs should\n        be removed from pools count, if these are present.\n        When the device is a VF, it\'s parent PF pool count should be\n        decreased, unless it is no longer in a pool.\n        """'
newline|'\n'
name|'if'
name|'pci_dev'
op|'.'
name|'dev_type'
op|'=='
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'SRIOV_PF'
op|':'
newline|'\n'
indent|'            '
name|'vfs_list'
op|'='
name|'objects'
op|'.'
name|'PciDeviceList'
op|'.'
name|'get_by_parent_address'
op|'('
nl|'\n'
name|'pci_dev'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'pci_dev'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'pci_dev'
op|'.'
name|'address'
op|')'
newline|'\n'
name|'if'
name|'vfs_list'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'vf'
name|'in'
name|'vfs_list'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'remove_device'
op|'('
name|'vf'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'elif'
name|'pci_dev'
op|'.'
name|'dev_type'
op|'=='
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'SRIOV_VF'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'parent'
op|'='
name|'pci_dev'
op|'.'
name|'get_by_dev_addr'
op|'('
name|'pci_dev'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'pci_dev'
op|'.'
name|'compute_node_id'
op|','
nl|'\n'
name|'pci_dev'
op|'.'
name|'parent_addr'
op|')'
newline|'\n'
comment|'# Make sure not to decrease PF pool count if this parent has'
nl|'\n'
comment|'# been already removed from pools'
nl|'\n'
name|'if'
name|'parent'
name|'in'
name|'self'
op|'.'
name|'get_free_devs'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'remove_device'
op|'('
name|'parent'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PciDeviceNotFound'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_filter_pools_for_spec
name|'def'
name|'_filter_pools_for_spec'
op|'('
name|'pools'
op|','
name|'request_specs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'pool'
name|'for'
name|'pool'
name|'in'
name|'pools'
nl|'\n'
name|'if'
name|'utils'
op|'.'
name|'pci_device_prop_match'
op|'('
name|'pool'
op|','
name|'request_specs'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_filter_pools_for_numa_cells
name|'def'
name|'_filter_pools_for_numa_cells'
op|'('
name|'pools'
op|','
name|'numa_cells'
op|')'
op|':'
newline|'\n'
comment|"# Some systems don't report numa node info for pci devices, in"
nl|'\n'
comment|'# that case None is reported in pci_device.numa_node, by adding None'
nl|'\n'
comment|'# to numa_cells we allow assigning those devices to instances with'
nl|'\n'
comment|'# numa topology'
nl|'\n'
indent|'        '
name|'numa_cells'
op|'='
op|'['
name|'None'
op|']'
op|'+'
op|'['
name|'cell'
op|'.'
name|'id'
name|'for'
name|'cell'
name|'in'
name|'numa_cells'
op|']'
newline|'\n'
comment|'# filter out pools which numa_node is not included in numa_cells'
nl|'\n'
name|'return'
op|'['
name|'pool'
name|'for'
name|'pool'
name|'in'
name|'pools'
name|'if'
name|'any'
op|'('
name|'utils'
op|'.'
name|'pci_device_prop_match'
op|'('
nl|'\n'
name|'pool'
op|','
op|'['
op|'{'
string|"'numa_node'"
op|':'
name|'cell'
op|'}'
op|']'
op|')'
nl|'\n'
name|'for'
name|'cell'
name|'in'
name|'numa_cells'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_filter_non_requested_pfs
dedent|''
name|'def'
name|'_filter_non_requested_pfs'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'matching_pools'
op|')'
op|':'
newline|'\n'
comment|'# Remove SRIOV_PFs from pools, unless it has been explicitly requested'
nl|'\n'
comment|'# This is especially needed in cases where PFs and VFs has the same'
nl|'\n'
comment|'# product_id.'
nl|'\n'
indent|'        '
name|'if'
name|'all'
op|'('
name|'spec'
op|'.'
name|'get'
op|'('
string|"'dev_type'"
op|')'
op|'!='
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'SRIOV_PF'
name|'for'
nl|'\n'
name|'spec'
name|'in'
name|'request'
op|'.'
name|'spec'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'matching_pools'
op|'='
name|'self'
op|'.'
name|'_filter_pools_for_pfs'
op|'('
name|'matching_pools'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'matching_pools'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_filter_pools_for_pfs
name|'def'
name|'_filter_pools_for_pfs'
op|'('
name|'pools'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'pool'
name|'for'
name|'pool'
name|'in'
name|'pools'
nl|'\n'
name|'if'
name|'not'
name|'pool'
op|'.'
name|'get'
op|'('
string|"'dev_type'"
op|')'
op|'=='
name|'fields'
op|'.'
name|'PciDeviceType'
op|'.'
name|'SRIOV_PF'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_apply_request
dedent|''
name|'def'
name|'_apply_request'
op|'('
name|'self'
op|','
name|'pools'
op|','
name|'request'
op|','
name|'numa_cells'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vladikr): This code maybe open to race conditions.'
nl|'\n'
comment|'# Two concurrent requests may succeed when called support_requests'
nl|'\n'
comment|'# because this method does not remove related devices from the pools'
nl|'\n'
indent|'        '
name|'count'
op|'='
name|'request'
op|'.'
name|'count'
newline|'\n'
name|'matching_pools'
op|'='
name|'self'
op|'.'
name|'_filter_pools_for_spec'
op|'('
name|'pools'
op|','
name|'request'
op|'.'
name|'spec'
op|')'
newline|'\n'
name|'if'
name|'numa_cells'
op|':'
newline|'\n'
indent|'            '
name|'matching_pools'
op|'='
name|'self'
op|'.'
name|'_filter_pools_for_numa_cells'
op|'('
name|'matching_pools'
op|','
nl|'\n'
name|'numa_cells'
op|')'
newline|'\n'
dedent|''
name|'matching_pools'
op|'='
name|'self'
op|'.'
name|'_filter_non_requested_pfs'
op|'('
name|'request'
op|','
nl|'\n'
name|'matching_pools'
op|')'
newline|'\n'
name|'if'
name|'sum'
op|'('
op|'['
name|'pool'
op|'['
string|"'count'"
op|']'
name|'for'
name|'pool'
name|'in'
name|'matching_pools'
op|']'
op|')'
op|'<'
name|'count'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'pool'
name|'in'
name|'matching_pools'
op|':'
newline|'\n'
indent|'                '
name|'count'
op|'='
name|'self'
op|'.'
name|'_decrease_pool_count'
op|'('
name|'pools'
op|','
name|'pool'
op|','
name|'count'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'count'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|support_requests
dedent|''
name|'def'
name|'support_requests'
op|'('
name|'self'
op|','
name|'requests'
op|','
name|'numa_cells'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if the pci requests can be met.\n\n        Scheduler checks compute node\'s PCI stats to decide if an\n        instance can be scheduled into the node. Support does not\n        mean real allocation.\n        If numa_cells is provided then only devices contained in\n        those nodes are considered.\n        """'
newline|'\n'
comment|'# note (yjiang5): this function has high possibility to fail,'
nl|'\n'
comment|'# so no exception should be triggered for performance reason.'
nl|'\n'
name|'pools'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'pools'
op|')'
newline|'\n'
name|'return'
name|'all'
op|'('
op|'['
name|'self'
op|'.'
name|'_apply_request'
op|'('
name|'pools'
op|','
name|'r'
op|','
name|'numa_cells'
op|')'
nl|'\n'
name|'for'
name|'r'
name|'in'
name|'requests'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|apply_requests
dedent|''
name|'def'
name|'apply_requests'
op|'('
name|'self'
op|','
name|'requests'
op|','
name|'numa_cells'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Apply PCI requests to the PCI stats.\n\n        This is used in multiple instance creation, when the scheduler has to\n        maintain how the resources are consumed by the instances.\n        If numa_cells is provided then only devices contained in\n        those nodes are considered.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'all'
op|'('
op|'['
name|'self'
op|'.'
name|'_apply_request'
op|'('
name|'self'
op|'.'
name|'pools'
op|','
name|'r'
op|','
name|'numa_cells'
op|')'
nl|'\n'
name|'for'
name|'r'
name|'in'
name|'requests'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceRequestFailed'
op|'('
name|'requests'
op|'='
name|'requests'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
dedent|''
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# 'devices' shouldn't be part of stats"
nl|'\n'
indent|'        '
name|'pools'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'pool'
name|'in'
name|'self'
op|'.'
name|'pools'
op|':'
newline|'\n'
indent|'            '
name|'tmp'
op|'='
op|'{'
name|'k'
op|':'
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
name|'pool'
op|')'
name|'if'
name|'k'
op|'!='
string|"'devices'"
op|'}'
newline|'\n'
name|'pools'
op|'.'
name|'append'
op|'('
name|'tmp'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'iter'
op|'('
name|'pools'
op|')'
newline|'\n'
nl|'\n'
DECL|member|clear
dedent|''
name|'def'
name|'clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Clear all the stats maintained."""'
newline|'\n'
name|'self'
op|'.'
name|'pools'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cmp'
op|'('
name|'self'
op|'.'
name|'pools'
op|','
name|'other'
op|'.'
name|'pools'
op|')'
op|'=='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
op|'('
name|'self'
op|'=='
name|'other'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_device_pools_obj
dedent|''
name|'def'
name|'to_device_pools_obj'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the contents of the pools as a PciDevicePoolList object."""'
newline|'\n'
name|'stats'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'self'
op|']'
newline|'\n'
name|'return'
name|'pci_device_pool'
op|'.'
name|'from_pci_stats'
op|'('
name|'stats'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
