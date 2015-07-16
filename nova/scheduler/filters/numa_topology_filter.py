begin_unit
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'hardware'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NUMATopologyFilter
name|'class'
name|'NUMATopologyFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filter on requested NUMA topology."""'
newline|'\n'
nl|'\n'
op|'@'
name|'filters'
op|'.'
name|'compat_legacy_props'
newline|'\n'
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
name|'ram_ratio'
op|'='
name|'host_state'
op|'.'
name|'ram_allocation_ratio'
newline|'\n'
name|'cpu_ratio'
op|'='
name|'host_state'
op|'.'
name|'cpu_allocation_ratio'
newline|'\n'
name|'request_spec'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'request_spec'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'requested_topology'
op|'='
name|'hardware'
op|'.'
name|'instance_topology_from_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'host_topology'
op|','
name|'_fmt'
op|'='
name|'hardware'
op|'.'
name|'host_topology_and_format_from_host'
op|'('
nl|'\n'
name|'host_state'
op|')'
newline|'\n'
name|'pci_requests'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'pci_requests'"
op|')'
newline|'\n'
name|'if'
name|'pci_requests'
op|':'
newline|'\n'
indent|'            '
name|'pci_requests'
op|'='
name|'pci_requests'
op|'.'
name|'requests'
newline|'\n'
dedent|''
name|'if'
name|'requested_topology'
name|'and'
name|'host_topology'
op|':'
newline|'\n'
indent|'            '
name|'limits'
op|'='
name|'objects'
op|'.'
name|'NUMATopologyLimits'
op|'('
nl|'\n'
name|'cpu_allocation_ratio'
op|'='
name|'cpu_ratio'
op|','
nl|'\n'
name|'ram_allocation_ratio'
op|'='
name|'ram_ratio'
op|')'
newline|'\n'
name|'instance_topology'
op|'='
op|'('
name|'hardware'
op|'.'
name|'numa_fit_instance_to_host'
op|'('
nl|'\n'
name|'host_topology'
op|','
name|'requested_topology'
op|','
nl|'\n'
name|'limits'
op|'='
name|'limits'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'pci_requests'
op|','
nl|'\n'
name|'pci_stats'
op|'='
name|'host_state'
op|'.'
name|'pci_stats'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_topology'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'host_state'
op|'.'
name|'limits'
op|'['
string|"'numa_topology'"
op|']'
op|'='
name|'limits'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'requested_topology'
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
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
