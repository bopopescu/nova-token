begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nNetwork Nodes are responsible for allocating ips and setting up network\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'datastore'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
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
string|"'network_type'"
op|','
nl|'\n'
string|"'flat'"
op|','
nl|'\n'
string|"'Service Class for Networking'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_bridge'"
op|','
string|"'br100'"
op|','
nl|'\n'
string|"'Bridge for simple network instances'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_list'
op|'('
string|"'flat_network_ips'"
op|','
nl|'\n'
op|'['
string|"'192.168.0.2'"
op|','
string|"'192.168.0.3'"
op|','
string|"'192.168.0.4'"
op|']'
op|','
nl|'\n'
string|"'Available ips for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_network'"
op|','
string|"'192.168.0.0'"
op|','
nl|'\n'
string|"'Network for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_netmask'"
op|','
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'Netmask for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_gateway'"
op|','
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'Broadcast for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_broadcast'"
op|','
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'Broadcast for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_dns'"
op|','
string|"'8.8.4.4'"
op|','
nl|'\n'
string|"'Dns for simple network'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|get_host_for_project
name|'def'
name|'get_host_for_project'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'host'
op|'='
name|'redis'
op|'.'
name|'get'
op|'('
name|'__host_key'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|__host_key
dedent|''
name|'def'
name|'__host_key'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"network_host:%s"'
op|'%'
name|'project_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseNetworkService
dedent|''
name|'class'
name|'BaseNetworkService'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements common network service functionality\n\n    This class must be subclassed.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'self'
op|'.'
name|'network'
op|'='
name|'model'
op|'.'
name|'PublicNetworkController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_network_host
dedent|''
name|'def'
name|'get_network_host'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
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
string|'"""Safely becomes the host of the projects network"""'
newline|'\n'
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
name|'__host_key'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'redis'
op|'.'
name|'setnx'
op|'('
name|'key'
op|','
name|'FLAGS'
op|'.'
name|'node_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'redis'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
dedent|''
dedent|''
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|'='
string|"'default'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Subclass implements getting fixed ip from the pool"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'fixed_ip'
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
string|'"""Subclass implements return of ip to the pool"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_elastic_ip
dedent|''
name|'def'
name|'allocate_elastic_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets a elastic ip from the pool"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_ip'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate_elastic_ip
dedent|''
name|'def'
name|'associate_elastic_ip'
op|'('
name|'self'
op|','
name|'elastic_ip'
op|','
name|'fixed_ip'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associates an elastic ip to a fixed ip"""'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'associate_address'
op|'('
name|'elastic_ip'
op|','
name|'fixed_ip'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate_elastic_ip
dedent|''
name|'def'
name|'disassociate_elastic_ip'
op|'('
name|'self'
op|','
name|'elastic_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disassociates a elastic ip"""'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'disassociate_address'
op|'('
name|'elastic_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_elastic_ip
dedent|''
name|'def'
name|'deallocate_elastic_ip'
op|'('
name|'self'
op|','
name|'elastic_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a elastic ip to the pool"""'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'elastic_ip'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlatNetworkService
dedent|''
dedent|''
name|'class'
name|'FlatNetworkService'
op|'('
name|'BaseNetworkService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Basic network where no vlans are used"""'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|'='
string|"'default'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets a fixed ip from the pool\n\n        Flat network just grabs the next available ip from the pool\n        """'
newline|'\n'
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'redis'
op|'.'
name|'exists'
op|'('
string|"'ips'"
op|')'
name|'and'
name|'not'
name|'len'
op|'('
name|'redis'
op|'.'
name|'keys'
op|'('
string|"'instances:*'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'fixed_ip'
name|'in'
name|'FLAGS'
op|'.'
name|'flat_network_ips'
op|':'
newline|'\n'
indent|'                '
name|'redis'
op|'.'
name|'sadd'
op|'('
string|"'ips'"
op|','
name|'fixed_ip'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'fixed_ip'
op|'='
name|'redis'
op|'.'
name|'spop'
op|'('
string|"'ips'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ip'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoMoreAddresses'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'network_type'"
op|':'
string|"'injected'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|','
nl|'\n'
string|"'private_dns_name'"
op|':'
name|'str'
op|'('
name|'fixed_ip'
op|')'
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_bridge'
op|','
nl|'\n'
string|"'network_network'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_network'
op|','
nl|'\n'
string|"'network_netmask'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_netmask'
op|','
nl|'\n'
string|"'network_gateway'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_gateway'
op|','
nl|'\n'
string|"'network_broadcast'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_broadcast'
op|','
nl|'\n'
string|"'network_dns'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_dns'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'fixed_ip'
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
string|'"""Returns an ip to the pool"""'
newline|'\n'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sadd'
op|'('
string|"'ips'"
op|','
name|'fixed_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|class|VlanNetworkService
dedent|''
dedent|''
name|'class'
name|'VlanNetworkService'
op|'('
name|'BaseNetworkService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Vlan network with dhcp"""'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|'='
string|"'default'"
op|','
nl|'\n'
name|'vpn'
op|'='
name|'False'
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
string|'"""Gets a fixed ip from the pool """'
newline|'\n'
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'net'
op|'='
name|'model'
op|'.'
name|'get_project_network'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'vpn'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'net'
op|'.'
name|'allocate_vpn_ip'
op|'('
name|'user_id'
op|','
name|'project_id'
op|','
name|'mac'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'net'
op|'.'
name|'allocate_ip'
op|'('
name|'user_id'
op|','
name|'project_id'
op|','
name|'mac'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'network_type'"
op|':'
string|"'dhcp'"
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'mac'
op|','
nl|'\n'
string|"'private_dns_name'"
op|':'
name|'fixed_ip'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'fixed_ip'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns an ip to the pool"""'
newline|'\n'
name|'model'
op|'.'
name|'get_network_by_address'
op|'('
name|'fixed_ip'
op|')'
op|'.'
name|'deallocate_ip'
op|'('
name|'fixed_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lease_ip
dedent|''
name|'def'
name|'lease_ip'
op|'('
name|'self'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'__get_network_by_address'
op|'('
name|'address'
op|')'
op|'.'
name|'lease_ip'
op|'('
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|release_ip
dedent|''
name|'def'
name|'release_ip'
op|'('
name|'self'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'model'
op|'.'
name|'get_network_by_address'
op|'('
name|'address'
op|')'
op|'.'
name|'release_ip'
op|'('
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|restart_nets
dedent|''
name|'def'
name|'restart_nets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Ensure the network for each user is enabled"""'
newline|'\n'
name|'for'
name|'project'
name|'in'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_projects'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'model'
op|'.'
name|'get_project_network'
op|'('
name|'project'
op|'.'
name|'id'
op|')'
op|'.'
name|'express'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
