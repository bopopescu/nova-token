begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright (c) 2011-2014 OpenStack Foundation'
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
string|'"""\nIronic host manager.\n\nThis host manager will consume all cpu\'s, disk space, and\nram from a host / node as it is supporting Baremetal hosts, which can not be\nsubdivided into multiple instances.\n"""'
newline|'\n'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'hv_type'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'host_manager'
newline|'\n'
nl|'\n'
DECL|variable|host_manager_opts
name|'host_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'baremetal_scheduler_default_filters'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'RetryFilter'"
op|','
nl|'\n'
string|"'AvailabilityZoneFilter'"
op|','
nl|'\n'
string|"'ComputeFilter'"
op|','
nl|'\n'
string|"'ComputeCapabilitiesFilter'"
op|','
nl|'\n'
string|"'ImagePropertiesFilter'"
op|','
nl|'\n'
string|"'ExactRamFilter'"
op|','
nl|'\n'
string|"'ExactDiskFilter'"
op|','
nl|'\n'
string|"'ExactCoreFilter'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Which filter class names to use for filtering '"
nl|'\n'
string|"'baremetal hosts when not specified in the request.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'scheduler_use_baremetal_filters'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Flag to decide whether to use '"
nl|'\n'
string|"'baremetal_scheduler_default_filters or not.'"
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'host_manager_opts'
op|')'
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
DECL|class|IronicNodeState
name|'class'
name|'IronicNodeState'
op|'('
name|'host_manager'
op|'.'
name|'HostState'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mutable and immutable information tracked for a host.\n    This is an attempt to remove the ad-hoc data structures\n    previously used and lock down access.\n    """'
newline|'\n'
nl|'\n'
DECL|member|update_from_compute_node
name|'def'
name|'update_from_compute_node'
op|'('
name|'self'
op|','
name|'compute'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update information about a host from a ComputeNode object."""'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_total'
op|'='
name|'compute'
op|'.'
name|'vcpus'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_used'
op|'='
name|'compute'
op|'.'
name|'vcpus_used'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'free_ram_mb'
op|'='
name|'compute'
op|'.'
name|'free_ram_mb'
newline|'\n'
name|'self'
op|'.'
name|'total_usable_ram_mb'
op|'='
name|'compute'
op|'.'
name|'memory_mb'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'='
name|'compute'
op|'.'
name|'free_disk_gb'
op|'*'
number|'1024'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stats'
op|'='
name|'compute'
op|'.'
name|'stats'
name|'or'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'total_usable_disk_gb'
op|'='
name|'compute'
op|'.'
name|'local_gb'
newline|'\n'
name|'self'
op|'.'
name|'hypervisor_type'
op|'='
name|'compute'
op|'.'
name|'hypervisor_type'
newline|'\n'
name|'self'
op|'.'
name|'hypervisor_version'
op|'='
name|'compute'
op|'.'
name|'hypervisor_version'
newline|'\n'
name|'self'
op|'.'
name|'hypervisor_hostname'
op|'='
name|'compute'
op|'.'
name|'hypervisor_hostname'
newline|'\n'
name|'self'
op|'.'
name|'cpu_info'
op|'='
name|'compute'
op|'.'
name|'cpu_info'
newline|'\n'
name|'if'
name|'compute'
op|'.'
name|'supported_hv_specs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'supported_instances'
op|'='
op|'['
name|'spec'
op|'.'
name|'to_list'
op|'('
op|')'
name|'for'
name|'spec'
nl|'\n'
name|'in'
name|'compute'
op|'.'
name|'supported_hv_specs'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'supported_instances'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'updated'
op|'='
name|'compute'
op|'.'
name|'updated_at'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'host_manager'
op|'.'
name|'set_update_time_on_success'
newline|'\n'
DECL|member|consume_from_instance
name|'def'
name|'consume_from_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Consume nodes entire resources regardless of instance request."""'
newline|'\n'
name|'self'
op|'.'
name|'free_ram_mb'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_used'
op|'='
name|'self'
op|'.'
name|'vcpus_total'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IronicHostManager
dedent|''
dedent|''
name|'class'
name|'IronicHostManager'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ironic HostManager class."""'
newline|'\n'
nl|'\n'
DECL|member|_load_filters
name|'def'
name|'_load_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'scheduler_use_baremetal_filters'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'CONF'
op|'.'
name|'baremetal_scheduler_default_filters'
newline|'\n'
dedent|''
name|'return'
name|'super'
op|'('
name|'IronicHostManager'
op|','
name|'self'
op|')'
op|'.'
name|'_load_filters'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_state_cls
dedent|''
name|'def'
name|'host_state_cls'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'node'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Factory function/property to create a new HostState."""'
newline|'\n'
name|'compute'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'compute'"
op|')'
newline|'\n'
name|'if'
name|'compute'
name|'and'
name|'compute'
op|'.'
name|'get'
op|'('
string|"'hypervisor_type'"
op|')'
op|'=='
name|'hv_type'
op|'.'
name|'IRONIC'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'IronicNodeState'
op|'('
name|'host'
op|','
name|'node'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'host_manager'
op|'.'
name|'HostState'
op|'('
name|'host'
op|','
name|'node'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_init_instance_info
dedent|''
dedent|''
name|'def'
name|'_init_instance_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ironic hosts should not pass instance info."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_add_instance_info
dedent|''
name|'def'
name|'_add_instance_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'compute'
op|','
name|'host_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ironic hosts should not pass instance info."""'
newline|'\n'
name|'host_state'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
