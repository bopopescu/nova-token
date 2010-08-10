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
string|'"""Network Data for projects"""'
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
name|'utils'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vpn_ip'"
op|','
name|'utils'
op|'.'
name|'get_my_ip'
op|'('
op|')'
op|','
nl|'\n'
string|"'Public IP for the cloudpipe VPN servers'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'vpn_start_port'"
op|','
number|'1000'
op|','
nl|'\n'
string|"'Start port for the cloudpipe VPN servers'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'vpn_end_port'"
op|','
number|'2000'
op|','
nl|'\n'
string|"'End port for the cloudpipe VPN servers'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoMorePorts
name|'class'
name|'NoMorePorts'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkData
dedent|''
name|'class'
name|'NetworkData'
op|'('
name|'datastore'
op|'.'
name|'BasicModel'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages network host, and vpn ip and port for projects"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'super'
op|'('
name|'NetworkData'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|identifier
name|'def'
name|'identifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Identifier used for key in redis"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'project_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'cls'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a vpn for project\n\n        This method finds a free ip and port and stores the associated\n        values in the datastore.\n        """'
newline|'\n'
comment|'# TODO(vish): will we ever need multiiple ips per host?'
nl|'\n'
name|'port'
op|'='
name|'cls'
op|'.'
name|'find_free_port_for_ip'
op|'('
name|'FLAGS'
op|'.'
name|'vpn_ip'
op|')'
newline|'\n'
name|'network_data'
op|'='
name|'cls'
op|'('
name|'project_id'
op|')'
newline|'\n'
comment|'# save ip for project'
nl|'\n'
name|'network_data'
op|'['
string|"'host'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
name|'network_data'
op|'['
string|"'project'"
op|']'
op|'='
name|'project_id'
newline|'\n'
name|'network_data'
op|'['
string|"'ip'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'vpn_ip'
newline|'\n'
name|'network_data'
op|'['
string|"'port'"
op|']'
op|'='
name|'port'
newline|'\n'
name|'network_data'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'network_data'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_free_port_for_ip
name|'def'
name|'find_free_port_for_ip'
op|'('
name|'cls'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Finds a free port for a given ip from the redis set"""'
newline|'\n'
comment|'# TODO(vish): these redis commands should be generalized and'
nl|'\n'
comment|'#             placed into a base class. Conceptually, it is'
nl|'\n'
comment|'#             similar to an association, but we are just'
nl|'\n'
comment|'#             storing a set of values instead of keys that'
nl|'\n'
comment|'#             should be turned into objects.'
nl|'\n'
name|'cls'
op|'.'
name|'_ensure_set_exists'
op|'('
name|'ip'
op|')'
newline|'\n'
nl|'\n'
name|'port'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'spop'
op|'('
name|'cls'
op|'.'
name|'_redis_ports_key'
op|'('
name|'ip'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'port'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NoMorePorts'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'port'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_redis_ports_key
name|'def'
name|'_redis_ports_key'
op|'('
name|'cls'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'ip:%s:ports'"
op|'%'
name|'ip'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_ensure_set_exists
name|'def'
name|'_ensure_set_exists'
op|'('
name|'cls'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): these ports should be allocated through an admin'
nl|'\n'
comment|'#             command instead of a flag'
nl|'\n'
indent|'        '
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
op|'('
name|'not'
name|'redis'
op|'.'
name|'exists'
op|'('
name|'cls'
op|'.'
name|'_redis_ports_key'
op|'('
name|'ip'
op|')'
op|')'
name|'and'
nl|'\n'
name|'not'
name|'redis'
op|'.'
name|'exists'
op|'('
name|'cls'
op|'.'
name|'_redis_association_name'
op|'('
string|"'ip'"
op|','
name|'ip'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'vpn_start_port'
op|','
name|'FLAGS'
op|'.'
name|'vpn_end_port'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'redis'
op|'.'
name|'sadd'
op|'('
name|'cls'
op|'.'
name|'_redis_ports_key'
op|'('
name|'ip'
op|')'
op|','
name|'i'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|num_ports_for_ip
name|'def'
name|'num_ports_for_ip'
op|'('
name|'cls'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Calculates the number of free ports for a given ip"""'
newline|'\n'
name|'cls'
op|'.'
name|'_ensure_set_exists'
op|'('
name|'ip'
op|')'
newline|'\n'
name|'return'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'scard'
op|'('
string|"'ip:%s:ports'"
op|'%'
name|'ip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|ip
name|'def'
name|'ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The ip assigned to the project"""'
newline|'\n'
name|'return'
name|'self'
op|'['
string|"'ip'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|port
name|'def'
name|'port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The port assigned to the project"""'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'self'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Saves the association to the given ip"""'
newline|'\n'
name|'self'
op|'.'
name|'associate_with'
op|'('
string|"'ip'"
op|','
name|'self'
op|'.'
name|'ip'
op|')'
newline|'\n'
name|'super'
op|'('
name|'NetworkData'
op|','
name|'self'
op|')'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Cleans up datastore and adds port back to pool"""'
newline|'\n'
name|'self'
op|'.'
name|'unassociate_with'
op|'('
string|"'ip'"
op|','
name|'self'
op|'.'
name|'ip'
op|')'
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
string|"'ip:%s:ports'"
op|'%'
name|'self'
op|'.'
name|'ip'
op|','
name|'self'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'super'
op|'('
name|'NetworkData'
op|','
name|'self'
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
