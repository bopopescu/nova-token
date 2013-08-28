begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'nova'
name|'import'
name|'exception'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'pci_utils'
newline|'\n'
nl|'\n'
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
string|'"""PCI devices summary information.\n\n    According to the PCI SR-IOV spec, a PCI physical function can have up to\n    256 PCI virtual functions, thus the number of assignable PCI functions in\n    a cloud can be big. The scheduler needs to know all device availability\n    information in order to determine which compute hosts can support a PCI\n    request. Passing individual virtual device information to the scheduler\n    does not scale, so we provide summary information.\n\n    Usually the virtual functions provided by a host PCI device have the same\n    value for most properties, like vendor_id, product_id and class type.\n    The PCI stats class summarizes this information for the scheduler.\n\n    The pci stats information is maintained exclusively by compute node\n    resource tracker and updated to database. The scheduler fetches the\n    information and selects the compute node accordingly. If a comptue\n    node is selected, the resource tracker allocates the devices to the\n    instance and updates the pci stats information.\n\n    This summary information will be helpful for cloud management also.\n    """'
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
string|"'extra_info'"
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
name|'self'
op|'.'
name|'pools'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'stats'
op|')'
name|'if'
name|'stats'
name|'else'
op|'['
op|']'
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
name|'self'
op|'.'
name|'pool_keys'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_first_pool
dedent|''
name|'def'
name|'_get_first_pool'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the first pool that matches dev."""'
newline|'\n'
name|'return'
name|'next'
op|'('
op|'('
name|'pool'
name|'for'
name|'pool'
name|'in'
name|'self'
op|'.'
name|'pools'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_equal_properties'
op|'('
name|'dev'
op|','
name|'pool'
op|')'
op|')'
op|','
name|'None'
op|')'
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
string|'"""Add a device to the first matching pool."""'
newline|'\n'
name|'pool'
op|'='
name|'self'
op|'.'
name|'_get_first_pool'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pool'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'='
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'dev'
op|'.'
name|'get'
op|'('
name|'k'
op|')'
op|')'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'pool_keys'
op|')'
newline|'\n'
name|'pool'
op|'['
string|"'count'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'pools'
op|'.'
name|'append'
op|'('
name|'pool'
op|')'
newline|'\n'
dedent|''
name|'pool'
op|'['
string|"'count'"
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
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
DECL|member|consume_device
dedent|''
name|'def'
name|'consume_device'
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
name|'pool'
op|'='
name|'self'
op|'.'
name|'_get_first_pool'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pool'
op|':'
newline|'\n'
indent|'            '
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
name|'pci_utils'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'count'
op|'='
name|'request'
op|'['
string|"'count'"
op|']'
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
op|'['
string|"'spec'"
op|']'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if the pci requests can be met.\n\n        Scheduler checks compute node\'s PCI stats to decide if an\n        instance can be scheduled into the node. Support does not\n        mean real allocation.\n        """'
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
op|')'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Apply PCI requests to the PCI stats.\n\n        This is used in multiple instance creation, when the scheduler has to\n        maintain how the resources are consumed by the instances.\n        """'
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
op|')'
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
indent|'        '
name|'return'
name|'iter'
op|'('
name|'self'
op|'.'
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
dedent|''
dedent|''
endmarker|''
end_unit
