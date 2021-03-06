begin_unit
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
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cloudpipe'
name|'import'
name|'pipelib'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'firewall'
name|'as'
name|'base_firewall'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|libvirt
name|'libvirt'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NWFilterFirewall
name|'class'
name|'NWFilterFirewall'
op|'('
name|'base_firewall'
op|'.'
name|'FirewallDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This class implements a network filtering mechanism by using\n    libvirt\'s nwfilter.\n    all instances get a filter ("nova-base") applied. This filter\n    provides some basic security such as protection against MAC\n    spoofing, IP spoofing, and ARP spoofing.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an NWFilter firewall driver\n\n        :param host: nova.virt.libvirt.host.Host instance\n        :param kwargs: currently unused\n        """'
newline|'\n'
nl|'\n'
name|'global'
name|'libvirt'
newline|'\n'
name|'if'
name|'libvirt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'libvirt'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
string|"'libvirt'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Libvirt module could not be loaded. "'
nl|'\n'
string|'"NWFilterFirewall will not work correctly."'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'static_filters_configured'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'handle_security_groups'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|apply_instance_filter
dedent|''
name|'def'
name|'apply_instance_filter'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No-op. Everything is done in prepare_instance_filter."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_get_connection
dedent|''
name|'def'
name|'_get_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_host'
op|'.'
name|'get_connection'
op|'('
op|')'
newline|'\n'
DECL|variable|_conn
dedent|''
name|'_conn'
op|'='
name|'property'
op|'('
name|'_get_connection'
op|')'
newline|'\n'
nl|'\n'
DECL|member|nova_no_nd_reflection_filter
name|'def'
name|'nova_no_nd_reflection_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This filter protects false positives on IPv6 Duplicate Address\n        Detection(DAD).\n        """'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_get_filter_uuid'
op|'('
string|"'nova-no-nd-reflection'"
op|')'
newline|'\n'
name|'return'
string|"'''<filter name='nova-no-nd-reflection' chain='ipv6'>\n                  <!-- no nd reflection -->\n                  <!-- drop if destination mac is v6 mcast mac addr and\n                       we sent it. -->\n                  <uuid>%s</uuid>\n                  <rule action='drop' direction='in'>\n                      <mac dstmacaddr='33:33:00:00:00:00'\n                           dstmacmask='ff:ff:00:00:00:00' srcmacaddr='$MAC'/>\n                  </rule>\n                  </filter>'''"
op|'%'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|nova_dhcp_filter
dedent|''
name|'def'
name|'nova_dhcp_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The standard allow-dhcp-server filter is an <ip> one, so it uses\n           ebtables to allow traffic through. Without a corresponding rule in\n           iptables, it\'ll get blocked anyway.\n        """'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_get_filter_uuid'
op|'('
string|"'nova-allow-dhcp-server'"
op|')'
newline|'\n'
name|'return'
string|"'''<filter name='nova-allow-dhcp-server' chain='ipv4'>\n                    <uuid>%s</uuid>\n                    <rule action='accept' direction='out'\n                          priority='100'>\n                      <udp srcipaddr='0.0.0.0'\n                           dstipaddr='255.255.255.255'\n                           srcportstart='68'\n                           dstportstart='67'/>\n                    </rule>\n                    <rule action='accept' direction='in'\n                          priority='100'>\n                      <udp srcipaddr='$DHCPSERVER'\n                           srcportstart='67'\n                           dstportstart='68'/>\n                    </rule>\n                  </filter>'''"
op|'%'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|setup_basic_filtering
dedent|''
name|'def'
name|'setup_basic_filtering'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set up basic filtering (MAC, IP, and ARP spoofing protection)."""'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Called setup_basic_filtering in nwfilter'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'handle_security_groups'
op|':'
newline|'\n'
comment|"# No point in setting up a filter set that we'll be overriding"
nl|'\n'
comment|'# anyway.'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Ensuring static filters'"
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_static_filters'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'nodhcp_base_filter'
op|'='
name|'self'
op|'.'
name|'get_base_filter_list'
op|'('
name|'instance'
op|','
name|'False'
op|')'
newline|'\n'
name|'dhcp_base_filter'
op|'='
name|'self'
op|'.'
name|'get_base_filter_list'
op|'('
name|'instance'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'_base_filter'
op|'='
name|'nodhcp_base_filter'
newline|'\n'
name|'for'
name|'subnet'
name|'in'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'subnet'
op|'.'
name|'get_meta'
op|'('
string|"'dhcp_server'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'_base_filter'
op|'='
name|'dhcp_base_filter'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_get_instance_filter_xml'
op|'('
name|'instance'
op|','
nl|'\n'
name|'_base_filter'
op|','
nl|'\n'
name|'vif'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_filter_parameters
dedent|''
dedent|''
name|'def'
name|'_get_instance_filter_parameters'
op|'('
name|'self'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parameters'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|format_parameter
name|'def'
name|'format_parameter'
op|'('
name|'parameter'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|'"<parameter name=\'%s\' value=\'%s\'/>"'
op|'%'
op|'('
name|'parameter'
op|','
name|'value'
op|')'
op|')'
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
name|'return'
name|'parameters'
newline|'\n'
nl|'\n'
dedent|''
name|'v4_subnets'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'network'
op|'['
string|"'subnets'"
op|']'
name|'if'
name|'s'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|']'
newline|'\n'
name|'v6_subnets'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'network'
op|'['
string|"'subnets'"
op|']'
name|'if'
name|'s'
op|'['
string|"'version'"
op|']'
op|'=='
number|'6'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'subnet'
name|'in'
name|'v4_subnets'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'parameters'
op|'.'
name|'append'
op|'('
name|'format_parameter'
op|'('
string|"'IP'"
op|','
name|'ip'
op|'['
string|"'address'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'dhcp_server'
op|'='
name|'subnet'
op|'.'
name|'get_meta'
op|'('
string|"'dhcp_server'"
op|')'
newline|'\n'
name|'if'
name|'dhcp_server'
op|':'
newline|'\n'
indent|'                '
name|'parameters'
op|'.'
name|'append'
op|'('
name|'format_parameter'
op|'('
string|"'DHCPSERVER'"
op|','
name|'dhcp_server'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'subnet'
name|'in'
name|'v6_subnets'
op|':'
newline|'\n'
indent|'                '
name|'gateway'
op|'='
name|'subnet'
op|'.'
name|'get'
op|'('
string|"'gateway'"
op|')'
newline|'\n'
name|'if'
name|'gateway'
op|':'
newline|'\n'
indent|'                    '
name|'ra_server'
op|'='
name|'gateway'
op|'['
string|"'address'"
op|']'
op|'+'
string|'"/128"'
newline|'\n'
name|'parameters'
op|'.'
name|'append'
op|'('
name|'format_parameter'
op|'('
string|"'RASERVER'"
op|','
name|'ra_server'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'allow_same_net_traffic'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'subnet'
name|'in'
name|'v4_subnets'
op|':'
newline|'\n'
indent|'                '
name|'ipv4_cidr'
op|'='
name|'subnet'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
name|'net'
op|','
name|'mask'
op|'='
name|'netutils'
op|'.'
name|'get_net_and_mask'
op|'('
name|'ipv4_cidr'
op|')'
newline|'\n'
name|'parameters'
op|'.'
name|'append'
op|'('
name|'format_parameter'
op|'('
string|"'PROJNET'"
op|','
name|'net'
op|')'
op|')'
newline|'\n'
name|'parameters'
op|'.'
name|'append'
op|'('
name|'format_parameter'
op|'('
string|"'PROJMASK'"
op|','
name|'mask'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'subnet'
name|'in'
name|'v6_subnets'
op|':'
newline|'\n'
indent|'                    '
name|'ipv6_cidr'
op|'='
name|'subnet'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
name|'net'
op|','
name|'prefix'
op|'='
name|'netutils'
op|'.'
name|'get_net_and_prefixlen'
op|'('
name|'ipv6_cidr'
op|')'
newline|'\n'
name|'parameters'
op|'.'
name|'append'
op|'('
name|'format_parameter'
op|'('
string|"'PROJNET6'"
op|','
name|'net'
op|')'
op|')'
newline|'\n'
name|'parameters'
op|'.'
name|'append'
op|'('
name|'format_parameter'
op|'('
string|"'PROJMASK6'"
op|','
name|'prefix'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'parameters'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_filter_xml
dedent|''
name|'def'
name|'_get_instance_filter_xml'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'filters'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nic_id'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_filter_name'
op|'='
name|'self'
op|'.'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|')'
newline|'\n'
name|'parameters'
op|'='
name|'self'
op|'.'
name|'_get_instance_filter_parameters'
op|'('
name|'vif'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_get_filter_uuid'
op|'('
name|'instance_filter_name'
op|')'
newline|'\n'
name|'xml'
op|'='
string|"'''<filter name='%s' chain='root'>'''"
op|'%'
name|'instance_filter_name'
newline|'\n'
name|'xml'
op|'+='
string|"'<uuid>%s</uuid>'"
op|'%'
name|'uuid'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'filters'
op|':'
newline|'\n'
indent|'            '
name|'xml'
op|'+='
string|"'''<filterref filter='%s'>'''"
op|'%'
name|'f'
newline|'\n'
name|'xml'
op|'+='
string|"''"
op|'.'
name|'join'
op|'('
name|'parameters'
op|')'
newline|'\n'
name|'xml'
op|'+='
string|"'</filterref>'"
newline|'\n'
dedent|''
name|'xml'
op|'+='
string|"'</filter>'"
newline|'\n'
name|'return'
name|'xml'
newline|'\n'
nl|'\n'
DECL|member|get_base_filter_list
dedent|''
name|'def'
name|'get_base_filter_list'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'allow_dhcp'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Obtain a list of base filters to apply to an instance.\n        The return value should be a list of strings, each\n        specifying a filter name.  Subclasses can override this\n        function to add additional filters as needed.  Additional\n        filters added to the list must also be correctly defined\n        within the subclass.\n        """'
newline|'\n'
name|'if'
name|'pipelib'
op|'.'
name|'is_vpn_image'
op|'('
name|'instance'
op|'.'
name|'image_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'='
string|"'nova-vpn'"
newline|'\n'
dedent|''
name|'elif'
name|'allow_dhcp'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'='
string|"'nova-base'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'='
string|"'nova-nodhcp'"
newline|'\n'
dedent|''
name|'return'
op|'['
name|'base_filter'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_ensure_static_filters
dedent|''
name|'def'
name|'_ensure_static_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Static filters are filters that have no need to be IP aware.\n\n        There is no configuration or tuneability of these filters, so they\n        can be set up once and forgotten about.\n\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'static_filters_configured'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'filter_set'
op|'='
op|'['
string|"'no-mac-spoofing'"
op|','
nl|'\n'
string|"'no-ip-spoofing'"
op|','
nl|'\n'
string|"'no-arp-spoofing'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'nova_no_nd_reflection_filter'
op|'('
op|')'
op|')'
newline|'\n'
name|'filter_set'
op|'.'
name|'append'
op|'('
string|"'nova-no-nd-reflection'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_filter_container'
op|'('
string|"'nova-nodhcp'"
op|','
name|'filter_set'
op|')'
op|')'
newline|'\n'
name|'filter_set'
op|'.'
name|'append'
op|'('
string|"'allow-dhcp-server'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_filter_container'
op|'('
string|"'nova-base'"
op|','
name|'filter_set'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_filter_container'
op|'('
string|"'nova-vpn'"
op|','
nl|'\n'
op|'['
string|"'allow-dhcp-server'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'nova_dhcp_filter'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'static_filters_configured'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_filter_container
dedent|''
name|'def'
name|'_filter_container'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_get_filter_uuid'
op|'('
name|'name'
op|')'
newline|'\n'
name|'xml'
op|'='
string|"'''<filter name='%s' chain='root'>\n                   <uuid>%s</uuid>\n                   %s\n                 </filter>'''"
op|'%'
op|'('
name|'name'
op|','
name|'uuid'
op|','
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|'"<filterref filter=\'%s\'/>"'
op|'%'
op|'('
name|'f'
op|','
op|')'
name|'for'
name|'f'
name|'in'
name|'filters'
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'xml'
newline|'\n'
nl|'\n'
DECL|member|_get_filter_uuid
dedent|''
name|'def'
name|'_get_filter_uuid'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flt'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterLookupByName'
op|'('
name|'name'
op|')'
newline|'\n'
name|'xml'
op|'='
name|'flt'
op|'.'
name|'XMLDesc'
op|'('
number|'0'
op|')'
newline|'\n'
name|'doc'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'u'
op|'='
name|'doc'
op|'.'
name|'find'
op|'('
string|'"./uuid"'
op|')'
op|'.'
name|'text'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'u"Cannot find UUID for filter \'%(name)s\': \'%(e)s\'"'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'u'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"UUID for filter \'%s\' is \'%s\'"'
op|','
name|'name'
op|','
name|'u'
op|')'
newline|'\n'
name|'return'
name|'u'
newline|'\n'
nl|'\n'
DECL|member|_define_filter
dedent|''
name|'def'
name|'_define_filter'
op|'('
name|'self'
op|','
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'callable'
op|'('
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'xml'
op|'='
name|'xml'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterDefineXML'
op|'('
name|'xml'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Clear out the nwfilter rules."""'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'nic_id'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_filter_name'
op|'='
name|'self'
op|'.'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# nwfilters may be defined in a separate thread in the case'
nl|'\n'
comment|'# of libvirt non-blocking mode, so we wait for completion'
nl|'\n'
name|'max_retry'
op|'='
name|'CONF'
op|'.'
name|'live_migration_retry_count'
newline|'\n'
name|'for'
name|'cnt'
name|'in'
name|'range'
op|'('
name|'max_retry'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'_nw'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterLookupByName'
op|'('
name|'instance_filter_name'
op|')'
newline|'\n'
name|'_nw'
op|'.'
name|'undefine'
op|'('
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'libvirt'
op|'.'
name|'libvirtError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'cnt'
op|'=='
name|'max_retry'
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
dedent|''
name|'errcode'
op|'='
name|'e'
op|'.'
name|'get_error_code'
op|'('
op|')'
newline|'\n'
name|'if'
name|'errcode'
op|'=='
name|'libvirt'
op|'.'
name|'VIR_ERR_OPERATION_INVALID'
op|':'
newline|'\n'
comment|'# This happens when the instance filter is still in use'
nl|'\n'
comment|'# (ie. when the instance has not terminated properly)'
nl|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Failed to undefine network filter '"
nl|'\n'
string|"'%(name)s. Try %(cnt)d of '"
nl|'\n'
string|"'%(max_retry)d.'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'instance_filter_name'
op|','
nl|'\n'
string|"'cnt'"
op|':'
name|'cnt'
op|'+'
number|'1'
op|','
nl|'\n'
string|"'max_retry'"
op|':'
name|'max_retry'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'The nwfilter(%s) is not found.'"
op|','
nl|'\n'
name|'instance_filter_name'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_instance_filter_name
name|'def'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'nic_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'nova-instance-%s'"
op|'%'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'nova-instance-%s-%s'"
op|'%'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
name|'nic_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_filter_exists
dedent|''
name|'def'
name|'instance_filter_exists'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check nova-instance-instance-xxx exists."""'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'nic_id'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_filter_name'
op|'='
name|'self'
op|'.'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterLookupByName'
op|'('
name|'instance_filter_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'libvirt'
op|'.'
name|'libvirtError'
op|':'
newline|'\n'
indent|'                '
name|'name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'The nwfilter(%(instance_filter_name)s) for'"
nl|'\n'
string|"'%(name)s is not found.'"
op|','
nl|'\n'
op|'{'
string|"'instance_filter_name'"
op|':'
name|'instance_filter_name'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'name'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IptablesFirewallDriver
dedent|''
dedent|''
name|'class'
name|'IptablesFirewallDriver'
op|'('
name|'base_firewall'
op|'.'
name|'IptablesFirewallDriver'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'execute'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an IP tables firewall driver instance\n\n        :param execute: unused, pass None\n        :param kwargs: extra arguments\n\n        The @kwargs parameter must contain a key \'host\' that\n        maps to an instance of the nova.virt.libvirt.host.Host\n        class.\n        """'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'IptablesFirewallDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nwfilter'
op|'='
name|'NWFilterFirewall'
op|'('
name|'kwargs'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_basic_filtering
dedent|''
name|'def'
name|'setup_basic_filtering'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set up basic NWFilter."""'
newline|'\n'
name|'self'
op|'.'
name|'nwfilter'
op|'.'
name|'setup_basic_filtering'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|apply_instance_filter
dedent|''
name|'def'
name|'apply_instance_filter'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No-op. Everything is done in prepare_instance_filter."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(salvatore-orlando):'
nl|'\n'
comment|'# Overriding base class method for applying nwfilter operation'
nl|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'instance_info'
op|'.'
name|'pop'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'remove_filters_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'apply'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nwfilter'
op|'.'
name|'unfilter_instance'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Attempted to unfilter instance which is not '"
nl|'\n'
string|"'filtered'"
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_filter_exists
dedent|''
dedent|''
name|'def'
name|'instance_filter_exists'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check nova-instance-instance-xxx exists."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'nwfilter'
op|'.'
name|'instance_filter_exists'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
