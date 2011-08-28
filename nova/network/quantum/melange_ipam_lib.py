begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Nicira Networks, Inc'
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
name|'netaddr'
name|'import'
name|'IPNetwork'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'quantum'
name|'import'
name|'melange_connection'
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
string|'"quantum_melange_ipam"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ipam_lib
name|'def'
name|'get_ipam_lib'
op|'('
name|'net_man'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'QuantumMelangeIPAMLib'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumMelangeIPAMLib
dedent|''
name|'class'
name|'QuantumMelangeIPAMLib'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'m_conn'
op|'='
name|'melange_connection'
op|'.'
name|'MelangeConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_subnet
dedent|''
name|'def'
name|'create_subnet'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'label'
op|','
name|'project_id'
op|','
nl|'\n'
name|'quantum_net_id'
op|','
name|'priority'
op|','
name|'cidr'
op|'='
name|'None'
op|','
nl|'\n'
name|'gateway_v6'
op|'='
name|'None'
op|','
name|'cidr_v6'
op|'='
name|'None'
op|','
nl|'\n'
name|'dns1'
op|'='
name|'None'
op|','
name|'dns2'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'if'
name|'cidr'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'create_block'
op|'('
name|'quantum_net_id'
op|','
name|'cidr'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'tenant_id'
op|','
nl|'\n'
name|'dns1'
op|'='
name|'dns1'
op|','
name|'dns2'
op|'='
name|'dns2'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'cidr_v6'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'create_block'
op|'('
name|'quantum_net_id'
op|','
name|'cidr_v6'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'tenant_id'
op|','
nl|'\n'
name|'dns1'
op|'='
name|'dns1'
op|','
name|'dns2'
op|'='
name|'dns2'
op|')'
newline|'\n'
nl|'\n'
comment|'# create a entry in the network table just to store'
nl|'\n'
comment|'# the priority order for this network'
nl|'\n'
dedent|''
name|'net'
op|'='
op|'{'
string|'"uuid"'
op|':'
name|'quantum_net_id'
op|','
nl|'\n'
string|'"project_id"'
op|':'
name|'project_id'
op|','
nl|'\n'
string|'"priority"'
op|':'
name|'priority'
op|'}'
newline|'\n'
name|'network'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_create_safe'
op|'('
name|'context'
op|','
name|'net'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
dedent|''
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'quantum_net_id'
op|','
name|'vif_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'allocate_ip'
op|'('
name|'quantum_net_id'
op|','
nl|'\n'
name|'vif_ref'
op|'['
string|"'uuid'"
op|']'
op|','
name|'project_id'
op|'='
name|'tenant_id'
op|','
nl|'\n'
name|'mac_address'
op|'='
name|'vif_ref'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_network_id_by_cidr
dedent|''
name|'def'
name|'get_network_id_by_cidr'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cidr'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'all_blocks'
op|'='
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'get_blocks'
op|'('
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'b'
name|'in'
name|'all_blocks'
op|'['
string|"'ip_blocks'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'b'
op|'['
string|"'cidr'"
op|']'
op|'=='
name|'cidr'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'b'
op|'['
string|"'network_id'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'Exception'
op|'('
string|'"No network found for cidr %s"'
op|'%'
name|'cidr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_subnets_by_net_id
dedent|''
name|'def'
name|'delete_subnets_by_net_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'all_blocks'
op|'='
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'get_blocks'
op|'('
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'b'
name|'in'
name|'all_blocks'
op|'['
string|"'ip_blocks'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'b'
op|'['
string|"'network_id'"
op|']'
op|'=='
name|'net_id'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'delete_block'
op|'('
name|'b'
op|'['
string|"'id'"
op|']'
op|','
name|'tenant_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'network'
op|'='
name|'db'
op|'.'
name|'network_get_by_uuid'
op|'('
name|'admin_context'
op|','
name|'net_id'
op|')'
newline|'\n'
name|'if'
name|'network'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'network_delete_safe'
op|'('
name|'context'
op|','
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# get all networks with this project_id, as well as all networks'
nl|'\n'
comment|'# where the project-id is not set (these are shared networks)'
nl|'\n'
DECL|member|get_project_and_global_net_ids
dedent|''
dedent|''
name|'def'
name|'get_project_and_global_net_ids'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'id_proj_map'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'project_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"get_project_and_global_net_ids must be called"'
string|'" with a non-null project_id"'
op|')'
newline|'\n'
dedent|''
name|'tenant_id'
op|'='
name|'project_id'
newline|'\n'
name|'all_tenant_blocks'
op|'='
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'get_blocks'
op|'('
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'b'
name|'in'
name|'all_tenant_blocks'
op|'['
string|"'ip_blocks'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'id_proj_map'
op|'['
name|'b'
op|'['
string|"'network_id'"
op|']'
op|']'
op|'='
name|'tenant_id'
newline|'\n'
dedent|''
name|'tenant_id'
op|'='
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'all_provider_blocks'
op|'='
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'get_blocks'
op|'('
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'b'
name|'in'
name|'all_provider_blocks'
op|'['
string|"'ip_blocks'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'id_proj_map'
op|'['
name|'b'
op|'['
string|"'network_id'"
op|']'
op|']'
op|'='
name|'tenant_id'
newline|'\n'
nl|'\n'
dedent|''
name|'id_priority_map'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'net_id'
op|','
name|'project_id'
name|'in'
name|'id_project_map'
op|'.'
name|'item'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'='
name|'db'
op|'.'
name|'network_get_by_uuid'
op|'('
name|'admin_context'
op|','
name|'net_id'
op|')'
newline|'\n'
name|'if'
name|'network'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'id_proj_map'
op|'['
name|'net_id'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'id_priority_map'
op|'['
name|'net_id'
op|']'
op|'='
name|'network'
op|'['
string|"'priority'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'sorted'
op|'('
name|'id_priority_map'
op|'.'
name|'items'
op|'('
op|')'
op|','
nl|'\n'
name|'key'
op|'='
name|'lambda'
name|'x'
op|':'
name|'id_priority_map'
op|'['
name|'x'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME: (danwent) Melange actually returns the subnet info'
nl|'\n'
comment|'# when we query for a particular interface.  we may want to'
nl|'\n'
comment|'# reworks the ipam_manager python API to let us take advantage of'
nl|'\n'
comment|'# this, as right now we have to get all blocks and cycle through'
nl|'\n'
comment|'# them.'
nl|'\n'
DECL|member|get_subnets_by_net_id
dedent|''
name|'def'
name|'get_subnets_by_net_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'net_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet_v4'
op|'='
name|'None'
newline|'\n'
name|'subnet_v6'
op|'='
name|'None'
newline|'\n'
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'all_blocks'
op|'='
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'get_blocks'
op|'('
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'b'
name|'in'
name|'all_blocks'
op|'['
string|"'ip_blocks'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'b'
op|'['
string|"'network_id'"
op|']'
op|'=='
name|'net_id'
op|':'
newline|'\n'
indent|'                '
name|'subnet'
op|'='
op|'{'
string|"'network_id'"
op|':'
name|'b'
op|'['
string|"'network_id'"
op|']'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'b'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'b'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'b'
op|'['
string|"'broadcast'"
op|']'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'b'
op|'['
string|"'netmask'"
op|']'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'b'
op|'['
string|"'dns1'"
op|']'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'b'
op|'['
string|"'dns2'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'IPNetwork'
op|'('
name|'b'
op|'['
string|"'cidr'"
op|']'
op|')'
op|'.'
name|'version'
op|'=='
number|'6'
op|':'
newline|'\n'
indent|'                    '
name|'subnet_v6'
op|'='
name|'subnet'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'subnet_v4'
op|'='
name|'subnet'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
op|'('
name|'subnet_v4'
op|','
name|'subnet_v6'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_v4_ips_by_interface
dedent|''
name|'def'
name|'get_v4_ips_by_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net_id'
op|','
name|'vif_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'get_ips_by_interface'
op|'('
name|'context'
op|','
name|'net_id'
op|','
name|'vif_id'
op|','
nl|'\n'
name|'project_id'
op|','
number|'4'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_v6_ips_by_interface
dedent|''
name|'def'
name|'get_v6_ips_by_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net_id'
op|','
name|'vif_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'get_ips_by_interface'
op|'('
name|'context'
op|','
name|'net_id'
op|','
name|'vif_id'
op|','
nl|'\n'
name|'project_id'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_ips_by_interface
dedent|''
name|'def'
name|'get_ips_by_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net_id'
op|','
name|'vif_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'ip_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'ip_list'
op|'='
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'get_allocated_ips'
op|'('
name|'net_id'
op|','
name|'vif_id'
op|','
name|'tenant_id'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'ip_list'
name|'if'
name|'IPNetwork'
op|'('
name|'ip'
op|'['
string|"'address'"
op|']'
op|')'
op|'.'
name|'version'
op|'=='
name|'ip_version'
op|']'
newline|'\n'
nl|'\n'
DECL|member|verify_subnet_exists
dedent|''
name|'def'
name|'verify_subnet_exists'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'quantum_net_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'v4_subnet'
op|','
name|'v6_subnet'
op|'='
name|'self'
op|'.'
name|'get_subnets_by_net_id'
op|'('
name|'context'
op|','
name|'tenant_id'
op|','
nl|'\n'
name|'quantum_net_id'
op|')'
newline|'\n'
name|'return'
name|'v4_subnet'
name|'is'
name|'not'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|deallocate_ips_by_vif
dedent|''
name|'def'
name|'deallocate_ips_by_vif'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'net_id'
op|','
name|'vif_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'self'
op|'.'
name|'m_conn'
op|'.'
name|'deallocate_ips'
op|'('
name|'net_id'
op|','
name|'vif_ref'
op|'['
string|"'uuid'"
op|']'
op|','
name|'tenant_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
