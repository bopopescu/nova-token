begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
string|'"""Network-related utilities for supporting libvirt connection code."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'jinja2'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|netutils_opts
name|'netutils_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'injected_network_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'basedir_def'
op|'('
string|"'nova/virt/interfaces.template'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Template file for injected network'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'netutils_opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_ipv6'"
op|','
string|"'nova.netconf'"
op|')'
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
DECL|function|_get_first_network
dedent|''
name|'def'
name|'_get_first_network'
op|'('
name|'network'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
comment|'# Using a generator expression with a next() call for the first element'
nl|'\n'
comment|"# of a list since we don't want to evaluate the whole list as we can"
nl|'\n'
comment|'# have a lot of subnets'
nl|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'next'
op|'('
name|'i'
name|'for'
name|'i'
name|'in'
name|'network'
op|'['
string|"'subnets'"
op|']'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'version'"
op|']'
op|'=='
name|'version'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_injected_network_template
dedent|''
dedent|''
name|'def'
name|'get_injected_network_template'
op|'('
name|'network_info'
op|','
name|'use_ipv6'
op|'='
name|'None'
op|','
name|'template'
op|'='
name|'None'
op|','
nl|'\n'
name|'libvirt_virt_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a rendered network template for the given network_info.\n\n    :param network_info:\n        :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n    :param use_ipv6: If False, do not return IPv6 template information\n        even if an IPv6 subnet is present in network_info.\n    :param template: Path to the interfaces template file.\n    :param libvirt_virt_type: The Libvirt `virt_type`, will be `None` for\n        other hypervisors..\n    """'
newline|'\n'
name|'if'
name|'use_ipv6'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'use_ipv6'
op|'='
name|'CONF'
op|'.'
name|'use_ipv6'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'template'
op|':'
newline|'\n'
indent|'        '
name|'template'
op|'='
name|'CONF'
op|'.'
name|'injected_network_template'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
op|'('
name|'network_info'
name|'and'
name|'template'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'nets'
op|'='
op|'['
op|']'
newline|'\n'
name|'ifc_num'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'ipv6_is_available'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'vif'
op|'['
string|"'network'"
op|']'
name|'or'
name|'not'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
newline|'\n'
comment|'# NOTE(bnemec): The template only supports a single subnet per'
nl|'\n'
comment|"# interface and I'm not sure how/if that can be fixed, so this"
nl|'\n'
comment|'# code only takes the first subnet of the appropriate type.'
nl|'\n'
name|'subnet_v4'
op|'='
name|'_get_first_network'
op|'('
name|'network'
op|','
number|'4'
op|')'
newline|'\n'
name|'subnet_v6'
op|'='
name|'_get_first_network'
op|'('
name|'network'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
name|'ifc_num'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'injected'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'hwaddress'
op|'='
name|'vif'
op|'.'
name|'get'
op|'('
string|"'address'"
op|')'
newline|'\n'
name|'address'
op|'='
name|'None'
newline|'\n'
name|'netmask'
op|'='
name|'None'
newline|'\n'
name|'gateway'
op|'='
string|"''"
newline|'\n'
name|'broadcast'
op|'='
name|'None'
newline|'\n'
name|'dns'
op|'='
name|'None'
newline|'\n'
name|'routes'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'subnet_v4'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'subnet_v4'
op|'.'
name|'get_meta'
op|'('
string|"'dhcp_server'"
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'subnet_v4'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'ip'
op|'='
name|'subnet_v4'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'address'
op|'='
name|'ip'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'netmask'
op|'='
name|'model'
op|'.'
name|'get_netmask'
op|'('
name|'ip'
op|','
name|'subnet_v4'
op|')'
newline|'\n'
name|'if'
name|'subnet_v4'
op|'['
string|"'gateway'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'gateway'
op|'='
name|'subnet_v4'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'broadcast'
op|'='
name|'str'
op|'('
name|'subnet_v4'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'broadcast'
op|')'
newline|'\n'
name|'dns'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
op|'['
name|'i'
op|'['
string|"'address'"
op|']'
name|'for'
name|'i'
name|'in'
name|'subnet_v4'
op|'['
string|"'dns'"
op|']'
op|']'
op|')'
newline|'\n'
name|'for'
name|'route_ref'
name|'in'
name|'subnet_v4'
op|'['
string|"'routes'"
op|']'
op|':'
newline|'\n'
indent|'                    '
op|'('
name|'net'
op|','
name|'mask'
op|')'
op|'='
name|'get_net_and_mask'
op|'('
name|'route_ref'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'route'
op|'='
op|'{'
string|"'gateway'"
op|':'
name|'str'
op|'('
name|'route_ref'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
op|')'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'str'
op|'('
name|'route_ref'
op|'['
string|"'cidr'"
op|']'
op|')'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'net'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'mask'
op|'}'
newline|'\n'
name|'routes'
op|'.'
name|'append'
op|'('
name|'route'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'address_v6'
op|'='
name|'None'
newline|'\n'
name|'gateway_v6'
op|'='
string|"''"
newline|'\n'
name|'netmask_v6'
op|'='
name|'None'
newline|'\n'
name|'dns_v6'
op|'='
name|'None'
newline|'\n'
name|'have_ipv6'
op|'='
op|'('
name|'use_ipv6'
name|'and'
name|'subnet_v6'
op|')'
newline|'\n'
name|'if'
name|'have_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'subnet_v6'
op|'.'
name|'get_meta'
op|'('
string|"'dhcp_server'"
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'subnet_v6'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'ipv6_is_available'
op|'='
name|'True'
newline|'\n'
name|'ip_v6'
op|'='
name|'subnet_v6'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'address_v6'
op|'='
name|'ip_v6'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'netmask_v6'
op|'='
name|'model'
op|'.'
name|'get_netmask'
op|'('
name|'ip_v6'
op|','
name|'subnet_v6'
op|')'
newline|'\n'
name|'if'
name|'subnet_v6'
op|'['
string|"'gateway'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'gateway_v6'
op|'='
name|'subnet_v6'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'dns_v6'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
op|'['
name|'i'
op|'['
string|"'address'"
op|']'
name|'for'
name|'i'
name|'in'
name|'subnet_v6'
op|'['
string|"'dns'"
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'net_info'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'eth%d'"
op|'%'
name|'ifc_num'
op|','
nl|'\n'
string|"'hwaddress'"
op|':'
name|'hwaddress'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'netmask'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'gateway'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'broadcast'
op|','
nl|'\n'
string|"'dns'"
op|':'
name|'dns'
op|','
nl|'\n'
string|"'routes'"
op|':'
name|'routes'
op|','
nl|'\n'
string|"'address_v6'"
op|':'
name|'address_v6'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'gateway_v6'
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'netmask_v6'
op|','
nl|'\n'
string|"'dns_v6'"
op|':'
name|'dns_v6'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'nets'
op|'.'
name|'append'
op|'('
name|'net_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'nets'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'tmpl_path'
op|','
name|'tmpl_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
name|'template'
op|')'
newline|'\n'
name|'env'
op|'='
name|'jinja2'
op|'.'
name|'Environment'
op|'('
name|'loader'
op|'='
name|'jinja2'
op|'.'
name|'FileSystemLoader'
op|'('
name|'tmpl_path'
op|')'
op|','
nl|'\n'
name|'trim_blocks'
op|'='
name|'True'
op|')'
newline|'\n'
name|'template'
op|'='
name|'env'
op|'.'
name|'get_template'
op|'('
name|'tmpl_file'
op|')'
newline|'\n'
name|'return'
name|'template'
op|'.'
name|'render'
op|'('
op|'{'
string|"'interfaces'"
op|':'
name|'nets'
op|','
nl|'\n'
string|"'use_ipv6'"
op|':'
name|'ipv6_is_available'
op|','
nl|'\n'
string|"'libvirt_virt_type'"
op|':'
name|'libvirt_virt_type'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_network_metadata
dedent|''
name|'def'
name|'get_network_metadata'
op|'('
name|'network_info'
op|','
name|'use_ipv6'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets a more complete representation of the instance network information.\n\n    This data is exposed as network_data.json in the metadata service and\n    the config drive.\n\n    :param network_info: `nova.network.models.NetworkInfo` object describing\n        the network metadata.\n    :param use_ipv6: If False, do not return IPv6 template information\n        even if an IPv6 subnet is present in network_info. Defaults to\n        nova.netconf.use_ipv6.\n    """'
newline|'\n'
name|'if'
name|'not'
name|'network_info'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'use_ipv6'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'use_ipv6'
op|'='
name|'CONF'
op|'.'
name|'use_ipv6'
newline|'\n'
nl|'\n'
comment|'# IPv4 or IPv6 networks'
nl|'\n'
dedent|''
name|'nets'
op|'='
op|'['
op|']'
newline|'\n'
comment|"# VIFs, physical NICs, or VLANs. Physical NICs will have type 'phy'."
nl|'\n'
name|'links'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# Non-network bound services, such as DNS'
nl|'\n'
name|'services'
op|'='
op|'['
op|']'
newline|'\n'
name|'ifc_num'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'net_num'
op|'='
op|'-'
number|'1'
newline|'\n'
nl|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'vif'
op|'.'
name|'get'
op|'('
string|"'network'"
op|')'
name|'or'
name|'not'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'.'
name|'get'
op|'('
string|"'subnets'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
newline|'\n'
comment|'# NOTE(JoshNang) currently, only supports the first IPv4 and first'
nl|'\n'
comment|'# IPv6 subnet on network, a limitation that also exists in the'
nl|'\n'
comment|'# network template.'
nl|'\n'
name|'subnet_v4'
op|'='
name|'_get_first_network'
op|'('
name|'network'
op|','
number|'4'
op|')'
newline|'\n'
name|'subnet_v6'
op|'='
name|'_get_first_network'
op|'('
name|'network'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
name|'ifc_num'
op|'+='
number|'1'
newline|'\n'
name|'link'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# Get the VIF or physical NIC data'
nl|'\n'
name|'if'
name|'subnet_v4'
name|'or'
name|'subnet_v6'
op|':'
newline|'\n'
indent|'            '
name|'link'
op|'='
name|'_get_eth_link'
op|'('
name|'vif'
op|','
name|'ifc_num'
op|')'
newline|'\n'
name|'links'
op|'.'
name|'append'
op|'('
name|'link'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add IPv4 and IPv6 networks if they exist'
nl|'\n'
dedent|''
name|'if'
name|'subnet_v4'
name|'and'
name|'subnet_v4'
op|'.'
name|'get'
op|'('
string|"'ips'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'net_num'
op|'+='
number|'1'
newline|'\n'
name|'nets'
op|'.'
name|'append'
op|'('
name|'_get_nets'
op|'('
name|'vif'
op|','
name|'subnet_v4'
op|','
number|'4'
op|','
name|'net_num'
op|','
name|'link'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
name|'services'
op|'+='
op|'['
name|'dns'
name|'for'
name|'dns'
name|'in'
name|'_get_dns_services'
op|'('
name|'subnet_v4'
op|')'
nl|'\n'
name|'if'
name|'dns'
name|'not'
name|'in'
name|'services'
op|']'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'use_ipv6'
name|'and'
name|'subnet_v6'
op|')'
name|'and'
name|'subnet_v6'
op|'.'
name|'get'
op|'('
string|"'ips'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'net_num'
op|'+='
number|'1'
newline|'\n'
name|'nets'
op|'.'
name|'append'
op|'('
name|'_get_nets'
op|'('
name|'vif'
op|','
name|'subnet_v6'
op|','
number|'6'
op|','
name|'net_num'
op|','
name|'link'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
name|'services'
op|'+='
op|'['
name|'dns'
name|'for'
name|'dns'
name|'in'
name|'_get_dns_services'
op|'('
name|'subnet_v6'
op|')'
nl|'\n'
name|'if'
name|'dns'
name|'not'
name|'in'
name|'services'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
nl|'\n'
string|'"links"'
op|':'
name|'links'
op|','
nl|'\n'
string|'"networks"'
op|':'
name|'nets'
op|','
nl|'\n'
string|'"services"'
op|':'
name|'services'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_eth_link
dedent|''
name|'def'
name|'_get_eth_link'
op|'('
name|'vif'
op|','
name|'ifc_num'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a VIF or physical NIC representation.\n\n    :param vif: Neutron VIF\n    :param ifc_num: Interface index for generating name if the VIF\'s\n        \'devname\' isn\'t defined.\n    :return: A dict with \'id\', \'vif_id\', \'type\', \'mtu\' and\n        \'ethernet_mac_address\' as keys\n    """'
newline|'\n'
name|'link_id'
op|'='
name|'vif'
op|'.'
name|'get'
op|'('
string|"'devname'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'link_id'
op|':'
newline|'\n'
indent|'        '
name|'link_id'
op|'='
string|"'interface%d'"
op|'%'
name|'ifc_num'
newline|'\n'
nl|'\n'
comment|"# Use 'phy' for physical links. Ethernet can be confusing"
nl|'\n'
dedent|''
name|'if'
name|'vif'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|'=='
string|"'ethernet'"
op|':'
newline|'\n'
indent|'        '
name|'nic_type'
op|'='
string|"'phy'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'nic_type'
op|'='
name|'vif'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'link'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'link_id'
op|','
nl|'\n'
string|"'vif_id'"
op|':'
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'nic_type'
op|','
nl|'\n'
string|"'mtu'"
op|':'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'.'
name|'get'
op|'('
string|"'mtu'"
op|')'
op|','
nl|'\n'
string|"'ethernet_mac_address'"
op|':'
name|'vif'
op|'.'
name|'get'
op|'('
string|"'address'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'link'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_nets
dedent|''
name|'def'
name|'_get_nets'
op|'('
name|'vif'
op|','
name|'subnet'
op|','
name|'version'
op|','
name|'net_num'
op|','
name|'link_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get networks for the given VIF and subnet\n\n    :param vif: Neutron VIF\n    :param subnet: Neutron subnet\n    :param version: IP version as an int, either \'4\' or \'6\'\n    :param net_num: Network index for generating name of each network\n    :param link_id: Arbitrary identifier for the link the networks are\n        attached to\n    """'
newline|'\n'
name|'if'
name|'subnet'
op|'.'
name|'get_meta'
op|'('
string|"'dhcp_server'"
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'net_info'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'network%d'"
op|'%'
name|'net_num'
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'ipv%d_dhcp'"
op|'%'
name|'version'
op|','
nl|'\n'
string|"'link'"
op|':'
name|'link_id'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'net_info'
newline|'\n'
nl|'\n'
dedent|''
name|'ip'
op|'='
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'address'
op|'='
name|'ip'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'        '
name|'netmask'
op|'='
name|'model'
op|'.'
name|'get_netmask'
op|'('
name|'ip'
op|','
name|'subnet'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'version'
op|'=='
number|'6'
op|':'
newline|'\n'
indent|'        '
name|'netmask'
op|'='
name|'str'
op|'('
name|'subnet'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'netmask'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'net_info'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'network%d'"
op|'%'
name|'net_num'
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'ipv%d'"
op|'%'
name|'version'
op|','
nl|'\n'
string|"'link'"
op|':'
name|'link_id'
op|','
nl|'\n'
string|"'ip_address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'netmask'
op|','
nl|'\n'
string|"'routes'"
op|':'
name|'_get_default_route'
op|'('
name|'version'
op|','
name|'subnet'
op|')'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Add any additional routes beyond the default route'
nl|'\n'
name|'for'
name|'route'
name|'in'
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'route_addr'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'route'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'new_route'
op|'='
op|'{'
nl|'\n'
string|"'network'"
op|':'
name|'str'
op|'('
name|'route_addr'
op|'.'
name|'network'
op|')'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'str'
op|'('
name|'route_addr'
op|'.'
name|'netmask'
op|')'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'route'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'net_info'
op|'['
string|"'routes'"
op|']'
op|'.'
name|'append'
op|'('
name|'new_route'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'net_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_default_route
dedent|''
name|'def'
name|'_get_default_route'
op|'('
name|'version'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a default route for a network\n\n    :param version: IP version as an int, either \'4\' or \'6\'\n    :param subnet: Neutron subnet\n    """'
newline|'\n'
name|'if'
name|'subnet'
op|'.'
name|'get'
op|'('
string|"'gateway'"
op|')'
name|'and'
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|'.'
name|'get'
op|'('
string|"'address'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'gateway'
op|'='
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'{'
nl|'\n'
string|"'network'"
op|':'
string|"'0.0.0.0'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'0.0.0.0'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'gateway'
nl|'\n'
op|'}'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'version'
op|'=='
number|'6'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'{'
nl|'\n'
string|"'network'"
op|':'
string|"'::'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'::'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'gateway'
nl|'\n'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_dns_services
dedent|''
dedent|''
name|'def'
name|'_get_dns_services'
op|'('
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the DNS servers for the subnet."""'
newline|'\n'
name|'services'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'not'
name|'subnet'
op|'.'
name|'get'
op|'('
string|"'dns'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'services'
newline|'\n'
dedent|''
name|'return'
op|'['
op|'{'
string|"'type'"
op|':'
string|"'dns'"
op|','
string|"'address'"
op|':'
name|'ip'
op|'.'
name|'get'
op|'('
string|"'address'"
op|')'
op|'}'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
