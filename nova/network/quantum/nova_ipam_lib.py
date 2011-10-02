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
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'ipv6'
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
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'quantum'
name|'import'
name|'melange_connection'
name|'as'
name|'melange'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
string|'"nova.network.quantum.nova_ipam_lib"'
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
name|'QuantumNovaIPAMLib'
op|'('
name|'net_man'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumNovaIPAMLib
dedent|''
name|'class'
name|'QuantumNovaIPAMLib'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements Quantum IP Address Management (IPAM) interface\n       using the local Nova database.  This implementation is inline\n       with how IPAM is used by other NetworkManagers.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'net_manager'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Holds a reference to the "parent" network manager, used\n           to take advantage of various FlatManager methods to avoid\n           code duplication.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'net_manager'
op|'='
name|'net_manager'
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
name|'tenant_id'
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
indent|'        '
string|'"""Re-use the basic FlatManager create_networks method to\n           initialize the networks and fixed_ips tables in Nova DB.\n\n           Also stores a few more fields in the networks table that\n           are needed by Quantum but not the FlatManager.\n        """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'subnet_size'
op|'='
name|'len'
op|'('
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'manager'
op|'.'
name|'FlatManager'
op|'.'
name|'create_networks'
op|'('
name|'self'
op|'.'
name|'net_manager'
op|','
nl|'\n'
name|'admin_context'
op|','
name|'label'
op|','
name|'cidr'
op|','
nl|'\n'
name|'False'
op|','
number|'1'
op|','
name|'subnet_size'
op|','
name|'cidr_v6'
op|','
nl|'\n'
name|'gateway_v6'
op|','
name|'quantum_net_id'
op|','
name|'None'
op|','
name|'dns1'
op|','
name|'dns2'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'networks'
op|')'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Error creating network entry"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'='
name|'networks'
op|'['
number|'0'
op|']'
newline|'\n'
name|'net'
op|'='
op|'{'
string|'"project_id"'
op|':'
name|'tenant_id'
op|','
nl|'\n'
string|'"priority"'
op|':'
name|'priority'
op|','
nl|'\n'
string|'"uuid"'
op|':'
name|'quantum_net_id'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'network_update'
op|'('
name|'admin_context'
op|','
name|'network'
op|'['
string|"'id'"
op|']'
op|','
name|'net'
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
string|'""" Grabs Quantum network UUID based on IPv4 CIDR. """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'network'
op|'='
name|'db'
op|'.'
name|'network_get_by_cidr'
op|'('
name|'admin_context'
op|','
name|'cidr'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'network'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"No network with fixed_range = %s"'
op|'%'
nl|'\n'
name|'fixed_range'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network'
op|'['
string|"'uuid'"
op|']'
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
string|'"""Deletes a network based on Quantum UUID.  Uses FlatManager\n           delete_network to avoid duplication.\n        """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
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
name|'not'
name|'network'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"No network with net_id = %s"'
op|'%'
name|'net_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'manager'
op|'.'
name|'FlatManager'
op|'.'
name|'delete_network'
op|'('
name|'self'
op|'.'
name|'net_manager'
op|','
nl|'\n'
name|'admin_context'
op|','
name|'None'
op|','
nl|'\n'
name|'network'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'require_disassociated'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_project_and_global_net_ids
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
string|'"""Fetches all networks associated with this project, or\n           that are "global" (i.e., have no project set).\n           Returns list sorted by \'priority\'.\n        """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'networks'
op|'='
name|'db'
op|'.'
name|'project_get_networks'
op|'('
name|'admin_context'
op|','
name|'project_id'
op|','
name|'False'
op|')'
newline|'\n'
name|'networks'
op|'.'
name|'extend'
op|'('
name|'db'
op|'.'
name|'project_get_networks'
op|'('
name|'admin_context'
op|','
name|'None'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'id_priority_map'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'net_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'n'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'net_id'
op|'='
name|'n'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'net_list'
op|'.'
name|'append'
op|'('
op|'('
name|'net_id'
op|','
name|'n'
op|'['
string|'"project_id"'
op|']'
op|')'
op|')'
newline|'\n'
name|'id_priority_map'
op|'['
name|'net_id'
op|']'
op|'='
name|'n'
op|'['
string|"'priority'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'sorted'
op|'('
name|'net_list'
op|','
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
DECL|member|allocate_fixed_ip
dedent|''
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'tenant_id'
op|','
name|'quantum_net_id'
op|','
name|'vif_rec'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allocates a single fixed IPv4 address for a virtual interface."""'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'network'
op|'='
name|'db'
op|'.'
name|'network_get_by_uuid'
op|'('
name|'admin_context'
op|','
name|'quantum_net_id'
op|')'
newline|'\n'
name|'if'
name|'network'
op|'['
string|"'cidr'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'db'
op|'.'
name|'fixed_ip_associate_pool'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'vif_rec'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'virtual_interface_id'"
op|':'
name|'vif_rec'
op|'['
string|"'id'"
op|']'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'admin_context'
op|','
name|'address'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_subnets_by_net_id
dedent|''
dedent|''
name|'def'
name|'get_subnets_by_net_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'tenant_id'
op|','
name|'net_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns information about the IPv4 and IPv6 subnets\n           associated with a Quantum Network UUID.\n        """'
newline|'\n'
name|'n'
op|'='
name|'db'
op|'.'
name|'network_get_by_uuid'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'net_id'
op|')'
newline|'\n'
name|'subnet_data_v4'
op|'='
op|'{'
nl|'\n'
string|"'network_id'"
op|':'
name|'n'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'n'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'n'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'n'
op|'['
string|"'broadcast'"
op|']'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'n'
op|'['
string|"'netmask'"
op|']'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'n'
op|'['
string|"'dns1'"
op|']'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'n'
op|'['
string|"'dns2'"
op|']'
op|'}'
newline|'\n'
name|'subnet_data_v6'
op|'='
op|'{'
nl|'\n'
string|"'network_id'"
op|':'
name|'n'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'n'
op|'['
string|"'cidr_v6'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'n'
op|'['
string|"'gateway_v6'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'return'
op|'('
name|'subnet_data_v4'
op|','
name|'subnet_data_v6'
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
string|'"""Returns a list of IPv4 address strings associated with\n           the specified virtual interface, based on the fixed_ips table.\n        """'
newline|'\n'
name|'vif_rec'
op|'='
name|'db'
op|'.'
name|'virtual_interface_get_by_uuid'
op|'('
name|'context'
op|','
name|'vif_id'
op|')'
newline|'\n'
name|'fixed_ips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_virtual_interface'
op|'('
name|'context'
op|','
nl|'\n'
name|'vif_rec'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
op|'['
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'fixed_ip'
name|'in'
name|'fixed_ips'
op|']'
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
string|'"""Returns a list containing a single IPv6 address strings\n           associated with the specified virtual interface.\n        """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
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
name|'vif_rec'
op|'='
name|'db'
op|'.'
name|'virtual_interface_get_by_uuid'
op|'('
name|'context'
op|','
name|'vif_id'
op|')'
newline|'\n'
name|'if'
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'='
name|'ipv6'
op|'.'
name|'to_global'
op|'('
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
op|','
nl|'\n'
name|'vif_rec'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ip'
op|']'
newline|'\n'
dedent|''
name|'return'
op|'['
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
name|'tenant_id'
op|','
name|'quantum_net_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Confirms that a subnet exists that is associated with the\n           specified Quantum Network UUID.  Raises an exception if no\n           such subnet exists.\n        """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'network_get_by_uuid'
op|'('
name|'admin_context'
op|','
name|'quantum_net_id'
op|')'
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
name|'tenant_id'
op|','
name|'net_id'
op|','
name|'vif_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deallocate all fixed IPs associated with the specified\n           virtual interface.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'fixed_ips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_virtual_interface'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'vif_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'fixed_ip'
name|'in'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'admin_context'
op|','
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'allocated'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'virtual_interface_id'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFoundForInstance'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'No fixed IPs to deallocate for vif %s'"
op|'%'
nl|'\n'
name|'vif_ref'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
