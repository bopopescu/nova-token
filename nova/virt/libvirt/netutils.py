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
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
nl|'\n'
string|'"""Network-releated utilities for supporting libvirt connection code."""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'utils'
newline|'\n'
nl|'\n'
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
DECL|function|get_net_and_mask
name|'def'
name|'get_net_and_mask'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'net'
op|'.'
name|'ip'
op|')'
op|','
name|'str'
op|'('
name|'net'
op|'.'
name|'netmask'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_net_and_prefixlen
dedent|''
name|'def'
name|'get_net_and_prefixlen'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'net'
op|'.'
name|'ip'
op|')'
op|','
name|'str'
op|'('
name|'net'
op|'.'
name|'_prefixlen'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ip_version
dedent|''
name|'def'
name|'get_ip_version'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'net'
op|'.'
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_network_info
dedent|''
name|'def'
name|'get_network_info'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# TODO(tr3buchet): this function needs to go away! network info'
nl|'\n'
comment|'#                  MUST be passed down from compute'
nl|'\n'
comment|'# TODO(adiantum) If we will keep this function'
nl|'\n'
comment|'# we should cache network_info'
nl|'\n'
indent|'    '
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_instance'
op|'('
name|'admin_context'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFoundForInstance'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ips'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'vifs'
op|'='
name|'db'
op|'.'
name|'virtual_interface_get_by_instance'
op|'('
name|'admin_context'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'db'
op|'.'
name|'instance_type_get'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
newline|'\n'
name|'network_info'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'vif'
name|'in'
name|'vifs'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
newline|'\n'
nl|'\n'
comment|"# determine which of the instance's IPs belong to this network"
nl|'\n'
name|'network_ips'
op|'='
op|'['
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'fixed_ip'
name|'in'
name|'fixed_ips'
name|'if'
nl|'\n'
name|'fixed_ip'
op|'['
string|"'network_id'"
op|']'
op|'=='
name|'network'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|function|ip_dict
name|'def'
name|'ip_dict'
op|'('
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
nl|'\n'
string|"'ip'"
op|':'
name|'ip'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'network'
op|'['
string|"'netmask'"
op|']'
op|','
nl|'\n'
string|"'enabled'"
op|':'
string|"'1'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|ip6_dict
dedent|''
name|'def'
name|'ip6_dict'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'prefix'
op|'='
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
newline|'\n'
name|'mac'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'project_id'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|"'ip'"
op|':'
name|'ipv6'
op|'.'
name|'to_global'
op|'('
name|'prefix'
op|','
name|'mac'
op|','
name|'project_id'
op|')'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'network'
op|'['
string|"'netmask_v6'"
op|']'
op|','
nl|'\n'
string|"'enabled'"
op|':'
string|"'1'"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'mapping'
op|'='
op|'{'
nl|'\n'
string|"'label'"
op|':'
name|'network'
op|'['
string|"'label'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'network'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'network'
op|'['
string|"'broadcast'"
op|']'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'network'
op|'['
string|"'gateway'"
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
string|"'rxtx_cap'"
op|':'
name|'flavor'
op|'['
string|"'rxtx_cap'"
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
op|')'
name|'for'
name|'ip'
name|'in'
name|'network_ips'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'network'
op|'['
string|"'dns1'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'mapping'
op|'['
string|"'dns'"
op|']'
op|'.'
name|'append'
op|'('
name|'network'
op|'['
string|"'dns1'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'network'
op|'['
string|"'dns2'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'mapping'
op|'['
string|"'dns'"
op|']'
op|'.'
name|'append'
op|'('
name|'network'
op|'['
string|"'dns2'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'mapping'
op|'['
string|"'ip6s'"
op|']'
op|'='
op|'['
name|'ip6_dict'
op|'('
op|')'
op|']'
newline|'\n'
name|'mapping'
op|'['
string|"'gateway6'"
op|']'
op|'='
name|'network'
op|'['
string|"'gateway_v6'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'network_info'
op|'.'
name|'append'
op|'('
op|'('
name|'network'
op|','
name|'mapping'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_info'
newline|'\n'
dedent|''
endmarker|''
end_unit
