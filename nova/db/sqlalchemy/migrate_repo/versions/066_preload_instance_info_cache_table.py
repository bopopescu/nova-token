begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'json'
newline|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'migrate'
name|'import'
op|'*'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|meta
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
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
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
comment|'# grab tables'
nl|'\n'
name|'instance_info_caches'
op|'='
name|'Table'
op|'('
string|"'instance_info_caches'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instances'
op|'='
name|'Table'
op|'('
string|"'instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'vifs'
op|'='
name|'Table'
op|'('
string|"'virtual_interfaces'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'Table'
op|'('
string|"'networks'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'fixed_ips'
op|'='
name|'Table'
op|'('
string|"'fixed_ips'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'floating_ips'
op|'='
name|'Table'
op|'('
string|"'floating_ips'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# all of these functions return a python list of python dicts'
nl|'\n'
comment|'# that have nothing to do with sqlalchemy objects whatsoever'
nl|'\n'
comment|'# after returning'
nl|'\n'
DECL|function|get_instances
name|'def'
name|'get_instances'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# want all instances whether there is network info or not'
nl|'\n'
indent|'        '
name|'s'
op|'='
name|'select'
op|'('
op|'['
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|','
name|'instances'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|']'
op|')'
newline|'\n'
name|'keys'
op|'='
op|'('
string|"'id'"
op|','
string|"'uuid'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'dict'
op|'('
name|'zip'
op|'('
name|'keys'
op|','
name|'row'
op|')'
op|')'
name|'for'
name|'row'
name|'in'
name|'s'
op|'.'
name|'execute'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_vifs_by_instance_id
dedent|''
name|'def'
name|'get_vifs_by_instance_id'
op|'('
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'select'
op|'('
op|'['
name|'vifs'
op|'.'
name|'c'
op|'.'
name|'id'
op|','
name|'vifs'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|','
name|'vifs'
op|'.'
name|'c'
op|'.'
name|'address'
op|','
name|'vifs'
op|'.'
name|'c'
op|'.'
name|'network_id'
op|']'
op|','
nl|'\n'
name|'vifs'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|'=='
name|'instance_id'
op|')'
newline|'\n'
name|'keys'
op|'='
op|'('
string|"'id'"
op|','
string|"'uuid'"
op|','
string|"'address'"
op|','
string|"'network_id'"
op|')'
newline|'\n'
name|'return'
op|'['
name|'dict'
op|'('
name|'zip'
op|'('
name|'keys'
op|','
name|'row'
op|')'
op|')'
name|'for'
name|'row'
name|'in'
name|'s'
op|'.'
name|'execute'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_network_by_id
dedent|''
name|'def'
name|'get_network_by_id'
op|'('
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'select'
op|'('
op|'['
name|'networks'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|','
name|'networks'
op|'.'
name|'c'
op|'.'
name|'label'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'dns1'
op|','
name|'networks'
op|'.'
name|'c'
op|'.'
name|'dns2'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'cidr'
op|','
name|'networks'
op|'.'
name|'c'
op|'.'
name|'cidr_v6'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'gateway'
op|','
name|'networks'
op|'.'
name|'c'
op|'.'
name|'gateway_v6'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'injected'
op|','
name|'networks'
op|'.'
name|'c'
op|'.'
name|'multi_host'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'bridge'
op|','
name|'networks'
op|'.'
name|'c'
op|'.'
name|'bridge_interface'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'vlan'
op|']'
op|','
nl|'\n'
name|'networks'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
name|'network_id'
op|')'
newline|'\n'
name|'keys'
op|'='
op|'('
string|"'uuid'"
op|','
string|"'label'"
op|','
string|"'project_id'"
op|','
string|"'dns1'"
op|','
string|"'dns2'"
op|','
nl|'\n'
string|"'cidr'"
op|','
string|"'cidr_v6'"
op|','
string|"'gateway'"
op|','
string|"'gateway_v6'"
op|','
nl|'\n'
string|"'injected'"
op|','
string|"'multi_host'"
op|','
string|"'bridge'"
op|','
string|"'bridge_interface'"
op|','
string|"'vlan'"
op|')'
newline|'\n'
name|'return'
op|'['
name|'dict'
op|'('
name|'zip'
op|'('
name|'keys'
op|','
name|'row'
op|')'
op|')'
name|'for'
name|'row'
name|'in'
name|'s'
op|'.'
name|'execute'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_fixed_ips_by_vif_id
dedent|''
name|'def'
name|'get_fixed_ips_by_vif_id'
op|'('
name|'vif_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'select'
op|'('
op|'['
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'id'
op|','
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'address'
op|']'
op|','
nl|'\n'
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'virtual_interface_id'
op|'=='
name|'vif_id'
op|')'
newline|'\n'
name|'keys'
op|'='
op|'('
string|"'id'"
op|','
string|"'address'"
op|')'
newline|'\n'
name|'fixed_ip_list'
op|'='
op|'['
name|'dict'
op|'('
name|'zip'
op|'('
name|'keys'
op|','
name|'row'
op|')'
op|')'
name|'for'
name|'row'
name|'in'
name|'s'
op|'.'
name|'execute'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
comment|'# fixed ips have floating ips, so here they are'
nl|'\n'
name|'for'
name|'fixed_ip'
name|'in'
name|'fixed_ip_list'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'['
string|"'version'"
op|']'
op|'='
number|'4'
newline|'\n'
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|'='
name|'get_floating_ips_by_fixed_ip_id'
op|'('
nl|'\n'
name|'fixed_ip'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'fixed_ip'
op|'['
string|"'type'"
op|']'
op|'='
string|"'fixed'"
newline|'\n'
name|'del'
name|'fixed_ip'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'fixed_ip_list'
newline|'\n'
nl|'\n'
DECL|function|get_floating_ips_by_fixed_ip_id
dedent|''
name|'def'
name|'get_floating_ips_by_fixed_ip_id'
op|'('
name|'fixed_ip_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'select'
op|'('
op|'['
name|'floating_ips'
op|'.'
name|'c'
op|'.'
name|'address'
op|']'
op|','
nl|'\n'
name|'floating_ips'
op|'.'
name|'c'
op|'.'
name|'fixed_ip_id'
op|'=='
name|'fixed_ip_id'
op|')'
newline|'\n'
name|'keys'
op|'='
op|'('
string|"'address'"
op|')'
newline|'\n'
name|'floating_ip_list'
op|'='
op|'['
name|'dict'
op|'('
name|'zip'
op|'('
name|'keys'
op|','
name|'row'
op|')'
op|')'
name|'for'
name|'row'
name|'in'
name|'s'
op|'.'
name|'execute'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'floating_ip_list'
op|':'
newline|'\n'
indent|'            '
name|'floating_ip'
op|'['
string|"'version'"
op|']'
op|'='
number|'4'
newline|'\n'
name|'floating_ip'
op|'['
string|"'type'"
op|']'
op|'='
string|"'floating'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'floating_ip_list'
newline|'\n'
nl|'\n'
DECL|function|_ip_dict_from_string
dedent|''
name|'def'
name|'_ip_dict_from_string'
op|'('
name|'ip_string'
op|','
name|'type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ip_string'
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'='
op|'{'
string|"'address'"
op|':'
name|'ip_string'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'type'
op|'}'
newline|'\n'
name|'if'
string|"':'"
name|'in'
name|'ip_string'
op|':'
newline|'\n'
indent|'                '
name|'ip'
op|'['
string|"'version'"
op|']'
op|'='
number|'6'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'ip'
op|'['
string|"'version'"
op|']'
op|'='
number|'4'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'ip'
newline|'\n'
nl|'\n'
DECL|function|_get_fixed_ipv6_dict
dedent|''
dedent|''
name|'def'
name|'_get_fixed_ipv6_dict'
op|'('
name|'cidr'
op|','
name|'mac'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_string'
op|'='
name|'ipv6'
op|'.'
name|'to_global'
op|'('
name|'cidr'
op|','
name|'mac'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'version'"
op|':'
number|'6'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'ip_string'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_create_subnet
dedent|''
name|'def'
name|'_create_subnet'
op|'('
name|'version'
op|','
name|'network'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'            '
name|'cidr'
op|'='
name|'network'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
name|'gateway'
op|'='
name|'network'
op|'['
string|"'gateway'"
op|']'
newline|'\n'
name|'ips'
op|'='
name|'get_fixed_ips_by_vif_id'
op|'('
name|'vif'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cidr'
op|'='
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
newline|'\n'
name|'gateway'
op|'='
name|'network'
op|'['
string|"'gateway_v6'"
op|']'
newline|'\n'
name|'ips'
op|'='
op|'['
name|'_get_fixed_ipv6_dict'
op|'('
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
op|','
nl|'\n'
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
name|'network'
op|'['
string|"'project_id'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(tr3buchet) routes is left empty for now because there'
nl|'\n'
comment|'# is no good way to generate them or determine which is default'
nl|'\n'
dedent|''
name|'subnet'
op|'='
op|'{'
string|"'version'"
op|':'
name|'version'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'cidr'
op|','
nl|'\n'
string|"'dns'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'_ip_dict_from_string'
op|'('
name|'gateway'
op|','
string|"'gateway'"
op|')'
op|','
nl|'\n'
string|"'routes'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
name|'ips'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'network'
op|'['
string|"'dns1'"
op|']'
name|'and'
name|'network'
op|'['
string|"'dns1'"
op|']'
op|'['
string|"'version'"
op|']'
op|'=='
name|'version'
op|':'
newline|'\n'
indent|'            '
name|'subnet'
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
name|'and'
name|'network'
op|'['
string|"'dns2'"
op|']'
op|'['
string|"'version'"
op|']'
op|'=='
name|'version'
op|':'
newline|'\n'
indent|'            '
name|'subnet'
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
name|'return'
name|'subnet'
newline|'\n'
nl|'\n'
DECL|function|_update_network
dedent|''
name|'def'
name|'_update_network'
op|'('
name|'vif'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
comment|'# vifs have a network which has subnets, so create the subnets'
nl|'\n'
comment|'# subnets contain all of the ip information'
nl|'\n'
indent|'        '
name|'network'
op|'['
string|"'subnets'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'network'
op|'['
string|"'dns1'"
op|']'
op|'='
name|'_ip_dict_from_string'
op|'('
name|'network'
op|'['
string|"'dns1'"
op|']'
op|','
string|"'dns'"
op|')'
newline|'\n'
name|'network'
op|'['
string|"'dns2'"
op|']'
op|'='
name|'_ip_dict_from_string'
op|'('
name|'network'
op|'['
string|"'dns2'"
op|']'
op|','
string|"'dns'"
op|')'
newline|'\n'
nl|'\n'
comment|'# nova networks can only have 2 subnets'
nl|'\n'
name|'if'
name|'network'
op|'['
string|"'cidr'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'subnets'"
op|']'
op|'.'
name|'append'
op|'('
name|'_create_subnet'
op|'('
number|'4'
op|','
name|'network'
op|','
name|'vif'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'subnets'"
op|']'
op|'.'
name|'append'
op|'('
name|'_create_subnet'
op|'('
number|'6'
op|','
name|'network'
op|','
name|'vif'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# put network together to fit model'
nl|'\n'
dedent|''
name|'network'
op|'['
string|"'id'"
op|']'
op|'='
name|'network'
op|'.'
name|'pop'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
name|'network'
op|'['
string|"'meta'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|"# NOTE(tr3buchet) this isn't absolutely necessary as hydration"
nl|'\n'
comment|'# would still work with these as keys, but cache generated by'
nl|'\n'
comment|'# the model would show these keys as a part of meta. i went'
nl|'\n'
comment|'# ahead and set it up the same way just so it looks the same'
nl|'\n'
name|'if'
name|'network'
op|'['
string|"'project_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'network'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
dedent|''
name|'del'
name|'network'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'if'
name|'network'
op|'['
string|"'injected'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'injected'"
op|']'
op|'='
name|'network'
op|'['
string|"'injected'"
op|']'
newline|'\n'
dedent|''
name|'del'
name|'network'
op|'['
string|"'injected'"
op|']'
newline|'\n'
name|'if'
name|'network'
op|'['
string|"'multi_host'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'multi_host'"
op|']'
op|'='
name|'network'
op|'['
string|"'multi_host'"
op|']'
newline|'\n'
dedent|''
name|'del'
name|'network'
op|'['
string|"'multi_host'"
op|']'
newline|'\n'
name|'if'
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'bridge_interface'"
op|']'
op|'='
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
newline|'\n'
dedent|''
name|'del'
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
newline|'\n'
name|'if'
name|'network'
op|'['
string|"'vlan'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'vlan'"
op|']'
op|'='
name|'network'
op|'['
string|"'vlan'"
op|']'
newline|'\n'
dedent|''
name|'del'
name|'network'
op|'['
string|"'vlan'"
op|']'
newline|'\n'
nl|'\n'
comment|'# ip information now lives in the subnet, pull them out of network'
nl|'\n'
name|'del'
name|'network'
op|'['
string|"'dns1'"
op|']'
newline|'\n'
name|'del'
name|'network'
op|'['
string|"'dns2'"
op|']'
newline|'\n'
name|'del'
name|'network'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
name|'del'
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
newline|'\n'
name|'del'
name|'network'
op|'['
string|"'gateway'"
op|']'
newline|'\n'
name|'del'
name|'network'
op|'['
string|"'gateway_v6'"
op|']'
newline|'\n'
nl|'\n'
comment|"# don't need meta if it's empty"
nl|'\n'
name|'if'
name|'not'
name|'network'
op|'['
string|"'meta'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'network'
op|'['
string|"'meta'"
op|']'
newline|'\n'
nl|'\n'
comment|'# preload caches table'
nl|'\n'
comment|'# list is made up of a row(instance_id, nw_info_json) for each instance'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'instance'
name|'in'
name|'get_instances'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"Updating %s"'
op|'%'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
comment|'# instances have vifs so aninstance nw_info is'
nl|'\n'
comment|'# is a list of dicts, 1 dict for each vif'
nl|'\n'
name|'nw_info'
op|'='
name|'get_vifs_by_instance_id'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"VIFs for Instance %s: \\n %s"'
op|'%'
nl|'\n'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'nw_info'
op|')'
op|')'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'            '
name|'networks_'
op|'='
name|'get_network_by_id'
op|'('
name|'vif'
op|'['
string|"'network_id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'networks_'
op|':'
newline|'\n'
indent|'                '
name|'network'
op|'='
name|'networks_'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"Network for Instance %s: \\n %s"'
op|'%'
nl|'\n'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'network'
op|')'
op|')'
newline|'\n'
name|'_update_network'
op|'('
name|'vif'
op|','
name|'network'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'network'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# put vif together to fit model'
nl|'\n'
dedent|''
name|'del'
name|'vif'
op|'['
string|"'network_id'"
op|']'
newline|'\n'
name|'vif'
op|'['
string|"'id'"
op|']'
op|'='
name|'vif'
op|'.'
name|'pop'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'='
name|'network'
newline|'\n'
comment|"# vif['meta'] could also be set to contain rxtx data here"
nl|'\n'
comment|"# but it isn't exposed in the api and is still being rewritten"
nl|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"VIF network for instance %s: \\n %s"'
op|'%'
nl|'\n'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'vif'
op|'['
string|"'network'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# jsonify nw_info'
nl|'\n'
dedent|''
name|'row'
op|'='
op|'{'
string|"'created_at'"
op|':'
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'network_info'"
op|':'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'nw_info'
op|')'
op|'}'
newline|'\n'
nl|'\n'
comment|'# write write row to table'
nl|'\n'
name|'insert'
op|'='
name|'instance_info_caches'
op|'.'
name|'insert'
op|'('
op|')'
op|'.'
name|'values'
op|'('
op|'**'
name|'row'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'insert'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
comment|'# facepalm'
nl|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'instance_info_caches'
op|'='
name|'Table'
op|'('
string|"'instance_info_caches'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# there is really no way to know what data was added by the migration and'
nl|'\n'
comment|'# what was added afterward. Of note is the fact that before this migration'
nl|'\n'
comment|'# the cache table was empty; therefore, delete everything. Also, aliens.'
nl|'\n'
name|'instance_info_caches'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
