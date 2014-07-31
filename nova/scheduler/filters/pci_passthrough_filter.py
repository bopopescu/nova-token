begin_unit
comment|'# Copyright (c) 2013 ISP RAS.'
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
name|'scheduler'
name|'import'
name|'filters'
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
nl|'\n'
DECL|class|PciPassthroughFilter
name|'class'
name|'PciPassthroughFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pci Passthrough Filter based on PCI request\n\n    Filter that schedules instances on a host if the host has devices\n    to meet the device requests in the \'extra_specs\' for the flavor.\n\n    PCI resource tracker provides updated summary information about the\n    PCI devices for each host, like:\n    [{"count": 5, "vendor_id": "8086", "product_id": "1520",\n        "extra_info":\'{}\'}],\n    and VM requests PCI devices via PCI requests, like:\n    [{"count": 1, "vendor_id": "8086", "product_id": "1520",}].\n\n    The filter checks if the host passes or not based on this information.\n    """'
newline|'\n'
nl|'\n'
DECL|member|host_passes
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return true if the host has the required PCI devices."""'
newline|'\n'
name|'pci_requests'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'pci_requests'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pci_requests'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'host_state'
op|'.'
name|'pci_stats'
op|'.'
name|'support_requests'
op|'('
name|'pci_requests'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s doesn\'t have the required PCI devices"'
nl|'\n'
string|'" (%(requests)s)"'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
string|"'requests'"
op|':'
name|'pci_requests'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
