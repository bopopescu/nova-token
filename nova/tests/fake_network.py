begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Rackspace'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
name|'as'
name|'network_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|HOST
name|'HOST'
op|'='
string|'"testhost"'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeIptablesFirewallDriver
name|'class'
name|'FakeIptablesFirewallDriver'
op|'('
name|'object'
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
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|setattr
dedent|''
name|'def'
name|'setattr'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__setattr__'
op|'('
name|'key'
op|','
name|'val'
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
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeVIFDriver
dedent|''
dedent|''
name|'class'
name|'FakeVIFDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|setattr
dedent|''
name|'def'
name|'setattr'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__setattr__'
op|'('
name|'key'
op|','
name|'val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'ip_address'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'extra_params'"
op|':'
string|"'fake'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeModel
dedent|''
dedent|''
name|'class'
name|'FakeModel'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represent a model from the db"""'
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
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|function|__getattr__
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeNetworkManager
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeNetworkManager'
op|'('
name|'network_manager'
op|'.'
name|'NetworkManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This NetworkManager doesn\'t call the base class so we can bypass all\n    inherited service cruft and just perform unit tests.\n    """'
newline|'\n'
nl|'\n'
DECL|class|FakeDB
name|'class'
name|'FakeDB'
op|':'
newline|'\n'
DECL|member|fixed_ip_get_by_instance
indent|'        '
name|'def'
name|'fixed_ip_get_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.0.0.0'"
op|')'
op|','
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.0.0.1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.0.0.2'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|network_get_by_cidr
dedent|''
name|'def'
name|'network_get_by_cidr'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFoundForCidr'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|network_create_safe
dedent|''
name|'def'
name|'network_create_safe'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fakenet'
op|'='
name|'dict'
op|'('
name|'net'
op|')'
newline|'\n'
name|'fakenet'
op|'['
string|"'id'"
op|']'
op|'='
number|'999'
newline|'\n'
name|'return'
name|'fakenet'
newline|'\n'
nl|'\n'
DECL|member|network_get
dedent|''
name|'def'
name|'network_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'cidr_v6'"
op|':'
string|"'2001:db8:69:%x::/64'"
op|'%'
name|'network_id'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|network_get_all
dedent|''
name|'def'
name|'network_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoNetworksFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|network_get_all_by_uuids
dedent|''
name|'def'
name|'network_get_all_by_uuids'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoNetworksFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|network_disassociate
dedent|''
name|'def'
name|'network_disassociate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|virtual_interface_get_all
dedent|''
name|'def'
name|'virtual_interface_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'floats'
op|'='
op|'['
op|'{'
string|"'address'"
op|':'
string|"'172.16.1.1'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'172.16.1.2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'173.16.1.2'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'vifs'
op|'='
op|'['
op|'{'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DC:AD:BE:FF:EF:01'"
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
string|"'172.16.0.1'"
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
name|'floats'
op|'['
number|'0'
op|']'
op|']'
op|'}'
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'instance_id'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'21'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DC:AD:BE:FF:EF:02'"
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
string|"'172.16.0.2'"
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
name|'floats'
op|'['
number|'1'
op|']'
op|']'
op|'}'
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'instance_id'"
op|':'
number|'30'
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'31'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DC:AD:BE:FF:EF:03'"
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
string|"'173.16.0.2'"
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
name|'floats'
op|'['
number|'2'
op|']'
op|']'
op|'}'
op|']'
op|'}'
op|']'
newline|'\n'
name|'return'
name|'vifs'
newline|'\n'
nl|'\n'
DECL|member|instance_get_id_to_uuid_mapping
dedent|''
name|'def'
name|'instance_get_id_to_uuid_mapping'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'ids'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(jkoelker): This is just here until we can rely on UUIDs'
nl|'\n'
indent|'            '
name|'mapping'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'id'
name|'in'
name|'ids'
op|':'
newline|'\n'
indent|'                '
name|'mapping'
op|'['
name|'id'
op|']'
op|'='
name|'str'
op|'('
name|'utils'
op|'.'
name|'gen_uuid'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'mapping'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
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
name|'db'
op|'='
name|'self'
op|'.'
name|'FakeDB'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deallocate_called'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'deallocate_called'
op|'='
name|'address'
newline|'\n'
nl|'\n'
DECL|member|_create_fixed_ips
dedent|''
name|'def'
name|'_create_fixed_ips'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|flavor
dedent|''
dedent|''
name|'flavor'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fake_flavor'"
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'flavor_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'3'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_network
name|'def'
name|'fake_network'
op|'('
name|'network_id'
op|','
name|'ipv6'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'ipv6'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ipv6'
op|'='
name|'FLAGS'
op|'.'
name|'use_ipv6'
newline|'\n'
dedent|''
name|'fake_network'
op|'='
op|'{'
string|"'id'"
op|':'
name|'network_id'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000%02d'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'test%d'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.%d.0/24'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'fake_br%d'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'fake_eth%d'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.%d.1'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'192.168.%d.255'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'192.168.%d.3'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'192.168.%d.4'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\n'
string|"'vpn_public_address'"
op|':'
string|"'192.168.%d.2'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'rxtx_base'"
op|':'
string|"'%d'"
op|'%'
name|'network_id'
op|'*'
number|'10'
op|'}'
newline|'\n'
name|'if'
name|'ipv6'
op|':'
newline|'\n'
indent|'        '
name|'fake_network'
op|'['
string|"'cidr_v6'"
op|']'
op|'='
string|"'2001:db8:0:%x::/64'"
op|'%'
name|'network_id'
newline|'\n'
name|'fake_network'
op|'['
string|"'gateway_v6'"
op|']'
op|'='
string|"'2001:db8:0:%x::1'"
op|'%'
name|'network_id'
newline|'\n'
name|'fake_network'
op|'['
string|"'netmask_v6'"
op|']'
op|'='
string|"'64'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'fake_network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vifs
dedent|''
name|'def'
name|'vifs'
op|'('
name|'n'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'n'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'{'
string|"'id'"
op|':'
name|'x'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:%02x'"
op|'%'
name|'x'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000%02d'"
op|'%'
name|'x'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'x'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'FakeModel'
op|'('
op|'**'
name|'fake_network'
op|'('
name|'x'
op|')'
op|')'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_ids
dedent|''
dedent|''
name|'def'
name|'floating_ip_ids'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'99'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'i'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_ids
dedent|''
dedent|''
name|'def'
name|'fixed_ip_ids'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'99'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'i'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|floating_ip_id
dedent|''
dedent|''
name|'floating_ip_id'
op|'='
name|'floating_ip_ids'
op|'('
op|')'
newline|'\n'
DECL|variable|fixed_ip_id
name|'fixed_ip_id'
op|'='
name|'fixed_ip_ids'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|next_fixed_ip
name|'def'
name|'next_fixed_ip'
op|'('
name|'network_id'
op|','
name|'num_floating_ips'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'next_id'
op|'='
name|'fixed_ip_id'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'f_ips'
op|'='
op|'['
name|'FakeModel'
op|'('
op|'**'
name|'next_floating_ip'
op|'('
name|'next_id'
op|')'
op|')'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'num_floating_ips'
op|')'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'id'"
op|':'
name|'next_id'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'network_id'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.%d.1%02d'"
op|'%'
op|'('
name|'network_id'
op|','
name|'next_id'
op|')'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'allocated'"
op|':'
name|'False'
op|','
nl|'\n'
comment|'# and since network_id and vif_id happen to be equivalent'
nl|'\n'
string|"'virtual_interface_id'"
op|':'
name|'network_id'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
name|'f_ips'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|next_floating_ip
dedent|''
name|'def'
name|'next_floating_ip'
op|'('
name|'fixed_ip_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'next_id'
op|'='
name|'floating_ip_id'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'id'"
op|':'
name|'next_id'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'10.10.10.1%02d'"
op|'%'
name|'next_id'
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
name|'fixed_ip_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'auto_assigned'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ipv4_like
dedent|''
name|'def'
name|'ipv4_like'
op|'('
name|'ip'
op|','
name|'match_string'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ip'
op|'='
name|'ip'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'match_octets'
op|'='
name|'match_string'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
op|','
name|'octet'
name|'in'
name|'enumerate'
op|'('
name|'match_octets'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'octet'
op|'=='
string|"'*'"
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'octet'
op|'!='
name|'ip'
op|'['
name|'i'
op|']'
op|':'
newline|'\n'
indent|'            '
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
DECL|function|fake_get_instance_nw_info
dedent|''
name|'def'
name|'fake_get_instance_nw_info'
op|'('
name|'stubs'
op|','
name|'num_networks'
op|'='
number|'1'
op|','
name|'ips_per_vif'
op|'='
number|'2'
op|','
nl|'\n'
name|'floating_ips_per_fixed_ip'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
comment|'# stubs is the self.stubs from the test'
nl|'\n'
comment|'# ips_per_vif is the number of ips each vif will have'
nl|'\n'
comment|'# num_floating_ips is number of float ips for each fixed ip'
nl|'\n'
indent|'    '
name|'network'
op|'='
name|'network_manager'
op|'.'
name|'FlatManager'
op|'('
name|'host'
op|'='
name|'HOST'
op|')'
newline|'\n'
name|'network'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
nl|'\n'
comment|'# reset the fixed and floating ip generators'
nl|'\n'
name|'global'
name|'floating_ip_id'
op|','
name|'fixed_ip_id'
newline|'\n'
name|'floating_ip_id'
op|'='
name|'floating_ip_ids'
op|'('
op|')'
newline|'\n'
name|'fixed_ip_id'
op|'='
name|'fixed_ip_ids'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'networks'
op|'='
op|'['
name|'fake_network'
op|'('
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'num_networks'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fixed_ips_fake
name|'def'
name|'fixed_ips_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'next_fixed_ip'
op|'('
name|'i'
op|','
name|'floating_ips_per_fixed_ip'
op|')'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'num_networks'
op|')'
name|'for'
name|'j'
name|'in'
name|'xrange'
op|'('
name|'ips_per_vif'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|floating_ips_fake
dedent|''
name|'def'
name|'floating_ips_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|virtual_interfaces_fake
dedent|''
name|'def'
name|'virtual_interfaces_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'vif'
name|'for'
name|'vif'
name|'in'
name|'vifs'
op|'('
name|'num_networks'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|instance_type_fake
dedent|''
name|'def'
name|'instance_type_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'flavor'
newline|'\n'
nl|'\n'
DECL|function|network_get_fake
dedent|''
name|'def'
name|'network_get_fake'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nets'
op|'='
op|'['
name|'n'
name|'for'
name|'n'
name|'in'
name|'networks'
name|'if'
name|'n'
op|'['
string|"'id'"
op|']'
op|'=='
name|'network_id'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'nets'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|'('
name|'network_id'
op|'='
name|'network_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'nets'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|function|update_cache_fake
dedent|''
name|'def'
name|'update_cache_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
name|'fixed_ips_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'floating_ip_get_by_fixed_address'"
op|','
name|'floating_ips_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'virtual_interface_get_by_instance'"
op|','
name|'virtual_interfaces_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get'"
op|','
name|'instance_type_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get'"
op|','
name|'network_get_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_info_cache_update'"
op|','
name|'update_cache_fake'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeContext
name|'class'
name|'FakeContext'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'project_id'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'network'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'FakeContext'
op|'('
op|')'
op|','
number|'0'
op|','
number|'0'
op|','
number|'0'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
