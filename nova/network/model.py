begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'functools'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_string_keys
name|'def'
name|'ensure_string_keys'
op|'('
name|'d'
op|')'
op|':'
newline|'\n'
comment|'# http://bugs.python.org/issue4978'
nl|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
op|'['
op|'('
name|'str'
op|'('
name|'k'
op|')'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'d'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|"# Constants for the 'vif_type' field in VIF class"
nl|'\n'
DECL|variable|VIF_TYPE_OVS
dedent|''
name|'VIF_TYPE_OVS'
op|'='
string|"'ovs'"
newline|'\n'
DECL|variable|VIF_TYPE_IVS
name|'VIF_TYPE_IVS'
op|'='
string|"'ivs'"
newline|'\n'
DECL|variable|VIF_TYPE_IOVISOR
name|'VIF_TYPE_IOVISOR'
op|'='
string|"'iovisor'"
newline|'\n'
DECL|variable|VIF_TYPE_BRIDGE
name|'VIF_TYPE_BRIDGE'
op|'='
string|"'bridge'"
newline|'\n'
DECL|variable|VIF_TYPE_802_QBG
name|'VIF_TYPE_802_QBG'
op|'='
string|"'802.1qbg'"
newline|'\n'
DECL|variable|VIF_TYPE_802_QBH
name|'VIF_TYPE_802_QBH'
op|'='
string|"'802.1qbh'"
newline|'\n'
DECL|variable|VIF_TYPE_MLNX_DIRECT
name|'VIF_TYPE_MLNX_DIRECT'
op|'='
string|"'mlnx_direct'"
newline|'\n'
DECL|variable|VIF_TYPE_MIDONET
name|'VIF_TYPE_MIDONET'
op|'='
string|"'midonet'"
newline|'\n'
DECL|variable|VIF_TYPE_OTHER
name|'VIF_TYPE_OTHER'
op|'='
string|"'other'"
newline|'\n'
nl|'\n'
comment|"# Constants for dictionary keys in the 'vif_details' field in the VIF"
nl|'\n'
comment|'# class'
nl|'\n'
DECL|variable|VIF_DETAIL_PORT_FILTER
name|'VIF_DETAIL_PORT_FILTER'
op|'='
string|"'port_filter'"
newline|'\n'
DECL|variable|VIF_DETAIL_OVS_HYBRID_PLUG
name|'VIF_DETAIL_OVS_HYBRID_PLUG'
op|'='
string|"'ovs_hybrid_plug'"
newline|'\n'
DECL|variable|VIF_DETAILS_PHYSICAL_NETWORK
name|'VIF_DETAILS_PHYSICAL_NETWORK'
op|'='
string|"'physical_network'"
newline|'\n'
nl|'\n'
comment|"# Constants for the 'vif_model' values"
nl|'\n'
DECL|variable|VIF_MODEL_VIRTIO
name|'VIF_MODEL_VIRTIO'
op|'='
string|"'virtio'"
newline|'\n'
DECL|variable|VIF_MODEL_NE2K_PCI
name|'VIF_MODEL_NE2K_PCI'
op|'='
string|"'ne2k_pci'"
newline|'\n'
DECL|variable|VIF_MODEL_PCNET
name|'VIF_MODEL_PCNET'
op|'='
string|"'pcnet'"
newline|'\n'
DECL|variable|VIF_MODEL_RTL8139
name|'VIF_MODEL_RTL8139'
op|'='
string|"'rtl8139'"
newline|'\n'
DECL|variable|VIF_MODEL_E1000
name|'VIF_MODEL_E1000'
op|'='
string|"'e1000'"
newline|'\n'
DECL|variable|VIF_MODEL_E1000E
name|'VIF_MODEL_E1000E'
op|'='
string|"'e1000e'"
newline|'\n'
DECL|variable|VIF_MODEL_NETFRONT
name|'VIF_MODEL_NETFRONT'
op|'='
string|"'netfront'"
newline|'\n'
DECL|variable|VIF_MODEL_SPAPR_VLAN
name|'VIF_MODEL_SPAPR_VLAN'
op|'='
string|"'spapr-vlan'"
newline|'\n'
nl|'\n'
comment|'# Constant for max length of network interface names'
nl|'\n'
comment|"# eg 'bridge' in the Network class or 'devname' in"
nl|'\n'
comment|'# the VIF class'
nl|'\n'
DECL|variable|NIC_NAME_LEN
name|'NIC_NAME_LEN'
op|'='
number|'14'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Model
name|'class'
name|'Model'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Defines some necessary structures for most of the network models."""'
newline|'\n'
DECL|member|__repr__
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'+'
string|"'('"
op|'+'
name|'dict'
op|'.'
name|'__repr__'
op|'('
name|'self'
op|')'
op|'+'
string|"')'"
newline|'\n'
nl|'\n'
DECL|member|_set_meta
dedent|''
name|'def'
name|'_set_meta'
op|'('
name|'self'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|"# pull meta out of kwargs if it's there"
nl|'\n'
indent|'        '
name|'self'
op|'['
string|"'meta'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'meta'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
comment|'# update meta with any additional kwargs that may exist'
nl|'\n'
name|'self'
op|'['
string|"'meta'"
op|']'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_meta
dedent|''
name|'def'
name|'get_meta'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""calls get(key, default) on self[\'meta\']."""'
newline|'\n'
name|'return'
name|'self'
op|'['
string|"'meta'"
op|']'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IP
dedent|''
dedent|''
name|'class'
name|'IP'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents an IP address in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'address'
op|'='
name|'None'
op|','
name|'type'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'IP'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'address'"
op|']'
op|'='
name|'address'
newline|'\n'
name|'self'
op|'['
string|"'type'"
op|']'
op|'='
name|'type'
newline|'\n'
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# determine version from address if not passed in'
nl|'\n'
name|'if'
name|'self'
op|'['
string|"'address'"
op|']'
name|'and'
name|'not'
name|'self'
op|'['
string|"'version'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'self'
op|'['
string|"'address'"
op|']'
op|')'
op|'.'
name|'version'
newline|'\n'
dedent|''
name|'except'
name|'netaddr'
op|'.'
name|'AddrFormatError'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid IP format %s"'
op|')'
op|'%'
name|'self'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidIpAddressError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
dedent|''
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'='
op|'['
string|"'address'"
op|','
string|"'type'"
op|','
string|"'version'"
op|']'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'self'
op|'['
name|'k'
op|']'
op|'=='
name|'other'
op|'['
name|'k'
op|']'
name|'for'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
name|'self'
op|'.'
name|'__eq__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_in_subnet
dedent|''
name|'def'
name|'is_in_subnet'
op|'('
name|'self'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'['
string|"'address'"
op|']'
name|'and'
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'self'
op|'['
string|"'address'"
op|']'
op|')'
name|'in'
nl|'\n'
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ip'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'ip'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIP
dedent|''
dedent|''
name|'class'
name|'FixedIP'
op|'('
name|'IP'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Fixed IP address in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'floating_ips'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FixedIP'
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
op|'['
string|"'floating_ips'"
op|']'
op|'='
name|'floating_ips'
name|'or'
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'['
string|"'type'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'type'"
op|']'
op|'='
string|"'fixed'"
newline|'\n'
nl|'\n'
DECL|member|add_floating_ip
dedent|''
dedent|''
name|'def'
name|'add_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'floating_ip'
name|'not'
name|'in'
name|'self'
op|'['
string|"'floating_ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'floating_ips'"
op|']'
op|'.'
name|'append'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|floating_ip_addresses
dedent|''
dedent|''
name|'def'
name|'floating_ip_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'['
string|"'floating_ips'"
op|']'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'FixedIP'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'fixed_ip'
op|')'
op|')'
newline|'\n'
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|'='
op|'['
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'floating_ip'
op|')'
nl|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|']'
newline|'\n'
name|'return'
name|'fixed_ip'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'='
op|'['
string|"'address'"
op|','
string|"'type'"
op|','
string|"'version'"
op|','
string|"'floating_ips'"
op|']'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'self'
op|'['
name|'k'
op|']'
op|'=='
name|'other'
op|'['
name|'k'
op|']'
name|'for'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
name|'self'
op|'.'
name|'__eq__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Route
dedent|''
dedent|''
name|'class'
name|'Route'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents an IP Route in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cidr'
op|'='
name|'None'
op|','
name|'gateway'
op|'='
name|'None'
op|','
name|'interface'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Route'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
name|'self'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'gateway'
newline|'\n'
name|'self'
op|'['
string|"'interface'"
op|']'
op|'='
name|'interface'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'route'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'route'
op|'='
name|'cls'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'route'
op|')'
op|')'
newline|'\n'
name|'route'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'route'
op|'['
string|"'gateway'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'route'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Subnet
dedent|''
dedent|''
name|'class'
name|'Subnet'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Subnet in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cidr'
op|'='
name|'None'
op|','
name|'dns'
op|'='
name|'None'
op|','
name|'gateway'
op|'='
name|'None'
op|','
name|'ips'
op|'='
name|'None'
op|','
nl|'\n'
name|'routes'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Subnet'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
name|'self'
op|'['
string|"'dns'"
op|']'
op|'='
name|'dns'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'gateway'
newline|'\n'
name|'self'
op|'['
string|"'ips'"
op|']'
op|'='
name|'ips'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'['
string|"'routes'"
op|']'
op|'='
name|'routes'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'['
string|"'cidr'"
op|']'
name|'and'
name|'not'
name|'self'
op|'['
string|"'version'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'self'
op|'['
string|"'cidr'"
op|']'
op|')'
op|'.'
name|'version'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'='
op|'['
string|"'cidr'"
op|','
string|"'dns'"
op|','
string|"'gateway'"
op|','
string|"'ips'"
op|','
string|"'routes'"
op|','
string|"'version'"
op|']'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'self'
op|'['
name|'k'
op|']'
op|'=='
name|'other'
op|'['
name|'k'
op|']'
name|'for'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
name|'self'
op|'.'
name|'__eq__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_route
dedent|''
name|'def'
name|'add_route'
op|'('
name|'self'
op|','
name|'new_route'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'new_route'
name|'not'
name|'in'
name|'self'
op|'['
string|"'routes'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
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
DECL|member|add_dns
dedent|''
dedent|''
name|'def'
name|'add_dns'
op|'('
name|'self'
op|','
name|'dns'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'dns'
name|'not'
name|'in'
name|'self'
op|'['
string|"'dns'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'dns'"
op|']'
op|'.'
name|'append'
op|'('
name|'dns'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_ip
dedent|''
dedent|''
name|'def'
name|'add_ip'
op|'('
name|'self'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ip'
name|'not'
name|'in'
name|'self'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'ips'"
op|']'
op|'.'
name|'append'
op|'('
name|'ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|as_netaddr
dedent|''
dedent|''
name|'def'
name|'as_netaddr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convience function to get cidr as a netaddr object."""'
newline|'\n'
name|'return'
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'self'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'cls'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'subnet'
op|')'
op|')'
newline|'\n'
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|'='
op|'['
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'dns'
op|')'
name|'for'
name|'dns'
name|'in'
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|']'
newline|'\n'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|'='
op|'['
name|'FixedIP'
op|'.'
name|'hydrate'
op|'('
name|'ip'
op|')'
name|'for'
name|'ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|']'
newline|'\n'
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|'='
op|'['
name|'Route'
op|'.'
name|'hydrate'
op|'('
name|'route'
op|')'
name|'for'
name|'route'
name|'in'
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|']'
newline|'\n'
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'subnet'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Network
dedent|''
dedent|''
name|'class'
name|'Network'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Network in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'id'
op|'='
name|'None'
op|','
name|'bridge'
op|'='
name|'None'
op|','
name|'label'
op|'='
name|'None'
op|','
nl|'\n'
name|'subnets'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Network'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
name|'self'
op|'['
string|"'bridge'"
op|']'
op|'='
name|'bridge'
newline|'\n'
name|'self'
op|'['
string|"'label'"
op|']'
op|'='
name|'label'
newline|'\n'
name|'self'
op|'['
string|"'subnets'"
op|']'
op|'='
name|'subnets'
name|'or'
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_subnet
dedent|''
name|'def'
name|'add_subnet'
op|'('
name|'self'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'subnet'
name|'not'
name|'in'
name|'self'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'subnets'"
op|']'
op|'.'
name|'append'
op|'('
name|'subnet'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'network'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'='
name|'cls'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'network'
op|')'
op|')'
newline|'\n'
name|'network'
op|'['
string|"'subnets'"
op|']'
op|'='
op|'['
name|'Subnet'
op|'.'
name|'hydrate'
op|'('
name|'subnet'
op|')'
nl|'\n'
name|'for'
name|'subnet'
name|'in'
name|'network'
op|'['
string|"'subnets'"
op|']'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'network'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'='
op|'['
string|"'id'"
op|','
string|"'bridge'"
op|','
string|"'label'"
op|','
string|"'subnets'"
op|']'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'self'
op|'['
name|'k'
op|']'
op|'=='
name|'other'
op|'['
name|'k'
op|']'
name|'for'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
name|'self'
op|'.'
name|'__eq__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VIF8021QbgParams
dedent|''
dedent|''
name|'class'
name|'VIF8021QbgParams'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents the parameters for a 802.1qbg VIF."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'managerid'
op|','
name|'typeid'
op|','
name|'typeidversion'
op|','
name|'instanceid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'['
string|"'managerid'"
op|']'
op|'='
name|'managerid'
newline|'\n'
name|'self'
op|'['
string|"'typeid'"
op|']'
op|'='
name|'typeid'
newline|'\n'
name|'self'
op|'['
string|"'typeidversion'"
op|']'
op|'='
name|'typeidversion'
newline|'\n'
name|'self'
op|'['
string|"'instanceid'"
op|']'
op|'='
name|'instanceid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VIF8021QbhParams
dedent|''
dedent|''
name|'class'
name|'VIF8021QbhParams'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents the parameters for a 802.1qbh VIF."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'profileid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'['
string|"'profileid'"
op|']'
op|'='
name|'profileid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VIF
dedent|''
dedent|''
name|'class'
name|'VIF'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Virtual Interface in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'id'
op|'='
name|'None'
op|','
name|'address'
op|'='
name|'None'
op|','
name|'network'
op|'='
name|'None'
op|','
name|'type'
op|'='
name|'None'
op|','
nl|'\n'
name|'details'
op|'='
name|'None'
op|','
name|'devname'
op|'='
name|'None'
op|','
name|'ovs_interfaceid'
op|'='
name|'None'
op|','
nl|'\n'
name|'qbh_params'
op|'='
name|'None'
op|','
name|'qbg_params'
op|'='
name|'None'
op|','
name|'active'
op|'='
name|'False'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VIF'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
name|'self'
op|'['
string|"'address'"
op|']'
op|'='
name|'address'
newline|'\n'
name|'self'
op|'['
string|"'network'"
op|']'
op|'='
name|'network'
name|'or'
name|'None'
newline|'\n'
name|'self'
op|'['
string|"'type'"
op|']'
op|'='
name|'type'
newline|'\n'
name|'self'
op|'['
string|"'details'"
op|']'
op|'='
name|'details'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'['
string|"'devname'"
op|']'
op|'='
name|'devname'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'ovs_interfaceid'"
op|']'
op|'='
name|'ovs_interfaceid'
newline|'\n'
name|'self'
op|'['
string|"'qbh_params'"
op|']'
op|'='
name|'qbh_params'
newline|'\n'
name|'self'
op|'['
string|"'qbg_params'"
op|']'
op|'='
name|'qbg_params'
newline|'\n'
name|'self'
op|'['
string|"'active'"
op|']'
op|'='
name|'active'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'='
op|'['
string|"'id'"
op|','
string|"'address'"
op|','
string|"'network'"
op|','
string|"'type'"
op|','
string|"'details'"
op|','
string|"'devname'"
op|','
nl|'\n'
string|"'ovs_interfaceid'"
op|','
string|"'qbh_params'"
op|','
string|"'qbg_params'"
op|','
nl|'\n'
string|"'active'"
op|']'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'self'
op|'['
name|'k'
op|']'
op|'=='
name|'other'
op|'['
name|'k'
op|']'
name|'for'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not'
name|'self'
op|'.'
name|'__eq__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fixed_ips
dedent|''
name|'def'
name|'fixed_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'fixed_ip'
name|'for'
name|'subnet'
name|'in'
name|'self'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
nl|'\n'
name|'for'
name|'fixed_ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|member|floating_ips
dedent|''
name|'def'
name|'floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'floating_ip'
name|'for'
name|'fixed_ip'
name|'in'
name|'self'
op|'.'
name|'fixed_ips'
op|'('
op|')'
nl|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|member|labeled_ips
dedent|''
name|'def'
name|'labeled_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of all IPs\n\n        The return value looks like this flat structure::\n\n            {\'network_label\': \'my_network\',\n             \'network_id\': \'n8v29837fn234782f08fjxk3ofhb84\',\n             \'ips\': [{\'address\': \'123.123.123.123\',\n                      \'version\': 4,\n                      \'type: \'fixed\',\n                      \'meta\': {...}},\n                     {\'address\': \'124.124.124.124\',\n                      \'version\': 4,\n                      \'type\': \'floating\',\n                      \'meta\': {...}},\n                     {\'address\': \'fe80::4\',\n                      \'version\': 6,\n                      \'type\': \'fixed\',\n                      \'meta\': {...}}]\n        """'
newline|'\n'
name|'if'
name|'self'
op|'['
string|"'network'"
op|']'
op|':'
newline|'\n'
comment|'# remove unnecessary fields on fixed_ips'
nl|'\n'
indent|'            '
name|'ips'
op|'='
op|'['
name|'IP'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'ip'
op|')'
op|')'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'.'
name|'fixed_ips'
op|'('
op|')'
op|']'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'ips'
op|':'
newline|'\n'
comment|'# remove floating ips from IP, since this is a flat structure'
nl|'\n'
comment|'# of all IPs'
nl|'\n'
indent|'                '
name|'del'
name|'ip'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'floating_ips'"
op|']'
newline|'\n'
comment|'# add floating ips to list (if any)'
nl|'\n'
dedent|''
name|'ips'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'floating_ips'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'network_label'"
op|':'
name|'self'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'self'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
name|'ips'
op|'}'
newline|'\n'
dedent|''
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|is_hybrid_plug_enabled
dedent|''
name|'def'
name|'is_hybrid_plug_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'['
string|"'details'"
op|']'
op|'.'
name|'get'
op|'('
name|'VIF_DETAIL_OVS_HYBRID_PLUG'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_neutron_filtering_enabled
dedent|''
name|'def'
name|'is_neutron_filtering_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'['
string|"'details'"
op|']'
op|'.'
name|'get'
op|'('
name|'VIF_DETAIL_PORT_FILTER'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_physical_network
dedent|''
name|'def'
name|'get_physical_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'phy_network'
op|'='
name|'self'
op|'['
string|"'network'"
op|']'
op|'['
string|"'meta'"
op|']'
op|'.'
name|'get'
op|'('
string|"'physical_network'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'phy_network'
op|':'
newline|'\n'
indent|'            '
name|'phy_network'
op|'='
name|'self'
op|'['
string|"'details'"
op|']'
op|'.'
name|'get'
op|'('
name|'VIF_DETAILS_PHYSICAL_NETWORK'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'phy_network'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif'
op|'='
name|'cls'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'vif'
op|')'
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'='
name|'Network'
op|'.'
name|'hydrate'
op|'('
name|'vif'
op|'['
string|"'network'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'vif'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_netmask
dedent|''
dedent|''
name|'def'
name|'get_netmask'
op|'('
name|'ip'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the netmask appropriate for injection into a guest."""'
newline|'\n'
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'        '
name|'return'
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
dedent|''
name|'return'
name|'subnet'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'_prefixlen'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkInfo
dedent|''
name|'class'
name|'NetworkInfo'
op|'('
name|'list'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stores and manipulates network information for a Nova instance."""'
newline|'\n'
nl|'\n'
comment|'# NetworkInfo is a list of VIFs'
nl|'\n'
nl|'\n'
DECL|member|fixed_ips
name|'def'
name|'fixed_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all fixed_ips without floating_ips attached."""'
newline|'\n'
name|'return'
op|'['
name|'ip'
name|'for'
name|'vif'
name|'in'
name|'self'
name|'for'
name|'ip'
name|'in'
name|'vif'
op|'.'
name|'fixed_ips'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|floating_ips
dedent|''
name|'def'
name|'floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all floating_ips."""'
newline|'\n'
name|'return'
op|'['
name|'ip'
name|'for'
name|'vif'
name|'in'
name|'self'
name|'for'
name|'ip'
name|'in'
name|'vif'
op|'.'
name|'floating_ips'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'network_info'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_info'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'network_info'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'('
op|'['
name|'VIF'
op|'.'
name|'hydrate'
op|'('
name|'vif'
op|')'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|json
dedent|''
name|'def'
name|'json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|','
name|'do_raise'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""A no-op method.\n\n        This is useful to avoid type checking when NetworkInfo might be\n        subclassed with NetworkInfoAsyncWrapper.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkInfoAsyncWrapper
dedent|''
dedent|''
name|'class'
name|'NetworkInfoAsyncWrapper'
op|'('
name|'NetworkInfo'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around NetworkInfo that allows retrieving NetworkInfo\n    in an async manner.\n\n    This allows one to start querying for network information before\n    you know you will need it.  If you have a long-running\n    operation, this allows the network model retrieval to occur in the\n    background.  When you need the data, it will ensure the async\n    operation has completed.\n\n    As an example:\n\n    def allocate_net_info(arg1, arg2)\n        return call_neutron_to_allocate(arg1, arg2)\n\n    network_info = NetworkInfoAsyncWrapper(allocate_net_info, arg1, arg2)\n    [do a long running operation -- real network_info will be retrieved\n    in the background]\n    [do something with network_info]\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'async_method'
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
name|'_gt'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'async_method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'methods'
op|'='
op|'['
string|"'json'"
op|','
string|"'fixed_ips'"
op|','
string|"'floating_ips'"
op|']'
newline|'\n'
name|'for'
name|'method'
name|'in'
name|'methods'
op|':'
newline|'\n'
indent|'            '
name|'fn'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'method'
op|')'
newline|'\n'
name|'wrapper'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'self'
op|'.'
name|'_sync_wrapper'
op|','
name|'fn'
op|')'
newline|'\n'
name|'functools'
op|'.'
name|'update_wrapper'
op|'('
name|'wrapper'
op|','
name|'fn'
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'wrapper'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_sync_wrapper
dedent|''
dedent|''
name|'def'
name|'_sync_wrapper'
op|'('
name|'self'
op|','
name|'wrapped'
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
string|'"""Synchronize the model before running a method."""'
newline|'\n'
name|'self'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'return'
name|'wrapped'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
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
name|'fn'
op|'='
name|'super'
op|'('
name|'NetworkInfoAsyncWrapper'
op|','
name|'self'
op|')'
op|'.'
name|'__getitem__'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_sync_wrapper'
op|'('
name|'fn'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
name|'def'
name|'__iter__'
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
name|'fn'
op|'='
name|'super'
op|'('
name|'NetworkInfoAsyncWrapper'
op|','
name|'self'
op|')'
op|'.'
name|'__iter__'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_sync_wrapper'
op|'('
name|'fn'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__len__
dedent|''
name|'def'
name|'__len__'
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
name|'fn'
op|'='
name|'super'
op|'('
name|'NetworkInfoAsyncWrapper'
op|','
name|'self'
op|')'
op|'.'
name|'__len__'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_sync_wrapper'
op|'('
name|'fn'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
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
name|'fn'
op|'='
name|'super'
op|'('
name|'NetworkInfoAsyncWrapper'
op|','
name|'self'
op|')'
op|'.'
name|'__str__'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_sync_wrapper'
op|'('
name|'fn'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
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
name|'fn'
op|'='
name|'super'
op|'('
name|'NetworkInfoAsyncWrapper'
op|','
name|'self'
op|')'
op|'.'
name|'__repr__'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_sync_wrapper'
op|'('
name|'fn'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|','
name|'do_raise'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait for async call to finish."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_gt'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(comstud): This looks funky, but this object is'
nl|'\n'
comment|"# subclassed from list.  In other words, 'self' is really"
nl|'\n'
comment|'# just a list with a bunch of extra methods.  So this'
nl|'\n'
comment|'# line just replaces the current list (which should be'
nl|'\n'
comment|'# empty) with the result.'
nl|'\n'
indent|'                '
name|'self'
op|'['
op|':'
op|']'
op|'='
name|'self'
op|'.'
name|'_gt'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'do_raise'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_gt'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
