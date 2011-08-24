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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
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
name|'quantum_connection'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'quantum'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"quantum_manager"'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'quantum_ipam_lib'"
op|','
nl|'\n'
string|"'nova.network.quantum.nova_ipam_lib'"
op|','
nl|'\n'
string|'"Indicates underlying IP address management library"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumManager
name|'class'
name|'QuantumManager'
op|'('
name|'manager'
op|'.'
name|'FlatManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" NetworkManager class that communicates with a Quantum service\n        via a web services API to provision VM network connectivity.\n\n        For IP Address management, QuantumManager can be configured to\n        use either Nova\'s local DB or the Melange IPAM service.\n\n        Currently, the QuantumManager does NOT support any of the \'gateway\'\n        functionality implemented by the Nova VlanManager, including:\n            * floating IPs\n            * DHCP\n            * NAT gateway\n\n        Support for these capabilities are targted for future releases.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ipam_lib'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Initialize two key libraries, the connection to a\n            Quantum service, and the library for implementing IPAM.\n\n            Calls inherited FlatManager constructor.\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_network'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'q_conn'
op|'='
name|'fake'
op|'.'
name|'FakeQuantumClientConnection'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'q_conn'
op|'='
name|'quantum_connection'
op|'.'
name|'QuantumClientConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'ipam_lib'
op|':'
newline|'\n'
indent|'            '
name|'ipam_lib'
op|'='
name|'FLAGS'
op|'.'
name|'quantum_ipam_lib'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'ipam'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'ipam_lib'
op|')'
op|'.'
name|'get_ipam_lib'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'QuantumManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_networks
dedent|''
name|'def'
name|'create_networks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'label'
op|','
name|'cidr'
op|','
name|'multi_host'
op|','
name|'num_networks'
op|','
nl|'\n'
name|'network_size'
op|','
name|'cidr_v6'
op|','
name|'gateway_v6'
op|','
name|'bridge'
op|','
nl|'\n'
name|'bridge_interface'
op|','
name|'dns1'
op|'='
name|'None'
op|','
name|'dns2'
op|'='
name|'None'
op|','
name|'uuid'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Unlike other NetworkManagers, with QuantumManager, each\n            create_networks calls should create only a single network.\n\n            Two scenarios exist:\n                - no \'uuid\' is specified, in which case we contact\n                  Quantum and create a new network.\n                - an existing \'uuid\' is specified, corresponding to\n                  a Quantum network created out of band.\n\n            In both cases, we initialize a subnet using the IPAM lib.\n        """'
newline|'\n'
name|'if'
name|'num_networks'
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
string|'"QuantumManager requires that only one"'
nl|'\n'
string|'" network is created per call"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'q_tenant_id'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"project_id"'
op|','
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
op|')'
newline|'\n'
name|'quantum_net_id'
op|'='
name|'uuid'
newline|'\n'
name|'if'
name|'quantum_net_id'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'network_exists'
op|'('
name|'q_tenant_id'
op|','
name|'quantum_net_id'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Unable to find existing quantum "'
string|'" network for tenant \'%s\' with net-id \'%s\'"'
op|'%'
op|'('
name|'q_tenant_id'
op|','
name|'quantum_net_id'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# otherwise, create network from default quantum pool'
nl|'\n'
indent|'            '
name|'quantum_net_id'
op|'='
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'create_network'
op|'('
name|'q_tenant_id'
op|','
name|'label'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ipam_tenant_id'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"project_id"'
op|','
name|'None'
op|')'
newline|'\n'
name|'priority'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"priority"'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'create_subnet'
op|'('
name|'context'
op|','
name|'label'
op|','
name|'ipam_tenant_id'
op|','
name|'quantum_net_id'
op|','
nl|'\n'
name|'priority'
op|','
name|'cidr'
op|','
name|'gateway_v6'
op|','
name|'cidr_v6'
op|','
name|'dns1'
op|','
name|'dns2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_network
dedent|''
name|'def'
name|'delete_network'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_range'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'""" Lookup network by IPv4 cidr, delete both the IPAM\n                subnet and the corresponding Quantum network.\n            """'
newline|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'quantum_net_id'
op|'='
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'get_network_id_by_cidr'
op|'('
nl|'\n'
name|'context'
op|','
name|'fixed_range'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'delete_subnets_by_net_id'
op|'('
name|'context'
op|','
name|'quantum_net_id'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
name|'q_tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'delete_network'
op|'('
name|'q_tenant_id'
op|','
name|'quantum_net_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_for_instance
dedent|''
name|'def'
name|'allocate_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Called by compute when it is creating a new VM.\n\n            There are three key tasks:\n                - Determine the number and order of vNICs to create\n                - Allocate IP addresses\n                - Create ports on a Quantum network and attach vNICs.\n\n            We support two approaches to determining vNICs:\n                - By default, a VM gets a vNIC for any network belonging\n                  to the VM\'s project, and a vNIC for any "global" network\n                  that has a NULL project_id.  vNIC order is determined\n                  by the network\'s \'priority\' field.\n                - If the \'os-create-server-ext\' was used to create the VM,\n                  only the networks in \'requested_networks\' are used to\n                  create vNICs, and the vNIC order is determiend by the\n                  order in the requested_networks array.\n\n            For each vNIC, use the FlatManager to create the entries\n            in the virtual_interfaces table, contact Quantum to\n            create a port and attachment the vNIC, and use the IPAM\n            lib to allocate IP addresses.\n        """'
newline|'\n'
name|'instance_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'instance_id'"
op|')'
newline|'\n'
name|'instance_type_id'
op|'='
name|'kwargs'
op|'['
string|"'instance_type_id'"
op|']'
newline|'\n'
name|'host'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'project_id'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"network allocations for instance %s"'
op|')'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'requested_networks'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'requested_networks'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'requested_networks'
op|':'
newline|'\n'
indent|'            '
name|'net_proj_pairs'
op|'='
op|'['
op|'('
name|'net_id'
op|','
name|'project_id'
op|')'
name|'for'
op|'('
name|'net_id'
op|','
name|'_i'
op|')'
name|'in'
name|'requested_networks'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'net_proj_pairs'
op|'='
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'get_project_and_global_net_ids'
op|'('
name|'context'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create a port via quantum and attach the vif'
nl|'\n'
dedent|''
name|'for'
op|'('
name|'quantum_net_id'
op|','
name|'project_id'
op|')'
name|'in'
name|'net_proj_pairs'
op|':'
newline|'\n'
nl|'\n'
comment|"# FIXME(danwent): We'd like to have the manager be"
nl|'\n'
comment|'# completely decoupled from the nova networks table.'
nl|'\n'
comment|'# However, other parts of nova sometimes go behind our'
nl|'\n'
comment|'# back and access network data directly from the DB.  So'
nl|'\n'
comment|'# for now, the quantum manager knows that there is a nova'
nl|'\n'
comment|'# networks DB table and accesses it here.  updating the'
nl|'\n'
comment|'# virtual_interfaces table to use UUIDs would be one'
nl|'\n'
comment|'# solution, but this would require significant work'
nl|'\n'
comment|'# elsewhere.'
nl|'\n'
indent|'            '
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_get_by_uuid'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'quantum_net_id'
op|')'
newline|'\n'
nl|'\n'
name|'vif_rec'
op|'='
name|'manager'
op|'.'
name|'FlatManager'
op|'.'
name|'add_virtual_interface'
op|'('
name|'self'
op|','
nl|'\n'
name|'context'
op|','
name|'instance_id'
op|','
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# talk to Quantum API to create and attach port.'
nl|'\n'
name|'q_tenant_id'
op|'='
name|'project_id'
name|'or'
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'create_and_attach_port'
op|'('
name|'q_tenant_id'
op|','
name|'quantum_net_id'
op|','
nl|'\n'
name|'vif_rec'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'quantum_net_id'
op|','
nl|'\n'
name|'vif_rec'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'instance_type_id'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_nw_info
dedent|''
name|'def'
name|'get_instance_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'instance_type_id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" This method is used by compute to fetch all network data\n            that should be used when creating the VM.\n\n            The method simply loops through all virtual interfaces\n            stored in the nova DB and queries the IPAM lib to get\n            the associated IP data.\n\n            The format of returned data is \'defined\' by the initial\n            set of NetworkManagers found in nova/network/manager.py .\n            Ideally this \'interface\' will be more formally defined\n            in the future.\n        """'
newline|'\n'
name|'network_info'
op|'='
op|'['
op|']'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'instance'
op|'.'
name|'project_id'
newline|'\n'
nl|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'vifs'
op|'='
name|'db'
op|'.'
name|'virtual_interface_get_by_instance'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'vifs'
op|':'
newline|'\n'
indent|'            '
name|'q_tenant_id'
op|'='
name|'project_id'
newline|'\n'
name|'ipam_tenant_id'
op|'='
name|'project_id'
newline|'\n'
name|'net_id'
op|','
name|'port_id'
op|'='
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'get_port_by_attachment'
op|'('
name|'q_tenant_id'
op|','
nl|'\n'
name|'vif'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'net_id'
op|':'
newline|'\n'
indent|'                '
name|'q_tenant_id'
op|'='
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'ipam_tenant_id'
op|'='
name|'None'
newline|'\n'
name|'net_id'
op|','
name|'port_id'
op|'='
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'get_port_by_attachment'
op|'('
nl|'\n'
name|'q_tenant_id'
op|','
name|'vif'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'net_id'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"No network for for virtual interface %s"'
op|')'
op|'%'
nl|'\n'
name|'vif'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
op|'('
name|'v4_subnet'
op|','
name|'v6_subnet'
op|')'
op|'='
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'get_subnets_by_net_id'
op|'('
name|'context'
op|','
nl|'\n'
name|'ipam_tenant_id'
op|','
name|'net_id'
op|')'
newline|'\n'
name|'v4_ips'
op|'='
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'get_v4_ips_by_interface'
op|'('
name|'context'
op|','
nl|'\n'
name|'net_id'
op|','
name|'vif'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'ipam_tenant_id'
op|')'
newline|'\n'
name|'v6_ips'
op|'='
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'get_v6_ips_by_interface'
op|'('
name|'context'
op|','
nl|'\n'
name|'net_id'
op|','
name|'vif'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'ipam_tenant_id'
op|')'
newline|'\n'
nl|'\n'
name|'quantum_net_id'
op|'='
name|'v4_subnet'
op|'['
string|"'network_id'"
op|']'
name|'or'
name|'v6_subnet'
op|'['
string|"'network_id'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|ip_dict
name|'def'
name|'ip_dict'
op|'('
name|'ip'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'{'
nl|'\n'
string|'"ip"'
op|':'
name|'ip'
op|','
nl|'\n'
string|'"netmask"'
op|':'
name|'subnet'
op|'['
string|'"netmask"'
op|']'
op|','
nl|'\n'
string|'"enabled"'
op|':'
string|'"1"'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'network_dict'
op|'='
op|'{'
nl|'\n'
string|"'cidr'"
op|':'
name|'v4_subnet'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
nl|'\n'
string|"'gateway'"
op|':'
name|'v4_subnet'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'v4_subnet'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'v4_subnet'
op|'['
string|"'broadcast'"
op|']'
op|','
nl|'\n'
string|"'mac'"
op|':'
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'vif_uuid'"
op|':'
name|'vif'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'dns'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
name|'ip_dict'
op|'('
name|'ip'
op|','
name|'v4_subnet'
op|')'
name|'for'
name|'ip'
name|'in'
name|'v4_ips'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'v6_subnet'
op|'['
string|"'cidr'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'network_dict'
op|'['
string|"'cidr_v6'"
op|']'
op|'='
name|'v6_subnet'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
name|'info'
op|'['
string|"'ip6s'"
op|']'
op|'='
op|'['
name|'ip_dict'
op|'('
name|'ip'
op|','
name|'v6_subnet'
op|')'
name|'for'
name|'ip'
name|'in'
name|'v6_ips'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'v6_subnet'
op|'['
string|"'gateway'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
string|"'gateway6'"
op|']'
op|'='
name|'v6_subnet'
op|'['
string|"'gateway'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'dns_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'s'
name|'in'
op|'['
name|'v4_subnet'
op|','
name|'v6_subnet'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'k'
name|'in'
op|'['
string|"'dns1'"
op|','
string|"'dns2'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'s'
op|'['
name|'k'
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'dns_dict'
op|'['
name|'s'
op|'['
name|'k'
op|']'
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'info'
op|'['
string|"'dns'"
op|']'
op|'='
op|'['
name|'d'
name|'for'
name|'d'
name|'in'
name|'dns_dict'
op|'.'
name|'keys'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'network_info'
op|'.'
name|'append'
op|'('
op|'('
name|'network_dict'
op|','
name|'info'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_info'
newline|'\n'
nl|'\n'
DECL|member|deallocate_for_instance
dedent|''
name|'def'
name|'deallocate_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Called when a VM is terminated.  Loop through each virtual\n            interface in the Nova DB and remove the Quantum port and\n            clear the IP allocation using the IPAM.  Finally, remove\n            the virtual interfaces from the Nova DB.\n        """'
newline|'\n'
name|'instance_id'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'instance_id'"
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'project_id'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'vifs'
op|'='
name|'db'
op|'.'
name|'virtual_interface_get_by_instance'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'for'
name|'vif_ref'
name|'in'
name|'vifs'
op|':'
newline|'\n'
indent|'            '
name|'interface_id'
op|'='
name|'vif_ref'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'q_tenant_id'
op|'='
name|'project_id'
newline|'\n'
name|'ipam_tenant_id'
op|'='
name|'project_id'
newline|'\n'
op|'('
name|'net_id'
op|','
name|'port_id'
op|')'
op|'='
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'get_port_by_attachment'
op|'('
name|'q_tenant_id'
op|','
nl|'\n'
name|'interface_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'net_id'
op|':'
newline|'\n'
indent|'                '
name|'q_tenant_id'
op|'='
name|'FLAGS'
op|'.'
name|'quantum_default_tenant_id'
newline|'\n'
name|'ipam_tenant_id'
op|'='
name|'None'
newline|'\n'
op|'('
name|'net_id'
op|','
name|'port_id'
op|')'
op|'='
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'get_port_by_attachment'
op|'('
nl|'\n'
name|'q_tenant_id'
op|','
name|'interface_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'net_id'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"Unable to find port with attachment: %s"'
op|'%'
op|'('
name|'interface_id'
op|')'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'detach_and_delete_port'
op|'('
name|'q_tenant_id'
op|','
nl|'\n'
name|'net_id'
op|','
name|'port_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'deallocate_ips_by_vif'
op|'('
name|'context'
op|','
name|'ipam_tenant_id'
op|','
nl|'\n'
name|'net_id'
op|','
name|'vif_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'db'
op|'.'
name|'virtual_interface_delete_by_instance'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_trigger_security_group_members_refresh_for_instance'
op|'('
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|validate_networks
dedent|''
name|'def'
name|'validate_networks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Validates that this tenant has quantum networks with the associated\n           UUIDs.  This is called by the \'os-create-server-ext\' API extension\n           code so that we can return an API error code to the caller if they\n           request an invalid network.\n        """'
newline|'\n'
name|'if'
name|'networks'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'for'
op|'('
name|'net_id'
op|','
name|'_i'
op|')'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ipam'
op|'.'
name|'verify_subnet_exists'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'net_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'q_conn'
op|'.'
name|'network_exists'
op|'('
name|'project_id'
op|','
name|'net_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|'('
name|'network_id'
op|'='
name|'net_id'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
