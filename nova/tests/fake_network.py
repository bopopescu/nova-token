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
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'manager'
name|'as'
name|'compute_manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
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
op|'.'
name|'network'
name|'import'
name|'api'
name|'as'
name|'network_api'
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
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'nova_ipam_lib'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'rpcapi'
name|'as'
name|'network_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
name|'as'
name|'libvirt_config'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|HOST
name|'HOST'
op|'='
string|'"testhost"'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_ipv6'"
op|','
string|"'nova.config'"
op|')'
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
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
name|'conf'
op|'='
name|'libvirt_config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'attr'
op|','
name|'val'
name|'in'
name|'conf'
op|'.'
name|'__dict__'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'val'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'conf'
op|','
name|'attr'
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'conf'
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
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
DECL|variable|vifs
indent|'        '
name|'vifs'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'00000000-0000-0000-0000-000000000010'"
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
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'00000000-0000-0000-0000-000000000020'"
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
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'00000000-0000-0000-0000-000000000030'"
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
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|floating_ips
name|'floating_ips'
op|'='
op|'['
name|'dict'
op|'('
name|'address'
op|'='
string|"'172.16.1.1'"
op|','
nl|'\n'
DECL|variable|fixed_ip_id
name|'fixed_ip_id'
op|'='
number|'100'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'172.16.1.2'"
op|','
nl|'\n'
DECL|variable|fixed_ip_id
name|'fixed_ip_id'
op|'='
number|'200'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'173.16.1.2'"
op|','
nl|'\n'
DECL|variable|fixed_ip_id
name|'fixed_ip_id'
op|'='
number|'210'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|fixed_ips
name|'fixed_ips'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
number|'100'
op|','
nl|'\n'
DECL|variable|address
name|'address'
op|'='
string|"'172.16.0.1'"
op|','
nl|'\n'
DECL|variable|virtual_interface_id
name|'virtual_interface_id'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'200'
op|','
nl|'\n'
DECL|variable|address
name|'address'
op|'='
string|"'172.16.0.2'"
op|','
nl|'\n'
DECL|variable|virtual_interface_id
name|'virtual_interface_id'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'210'
op|','
nl|'\n'
DECL|variable|address
name|'address'
op|'='
string|"'173.16.0.2'"
op|','
nl|'\n'
DECL|variable|virtual_interface_id
name|'virtual_interface_id'
op|'='
number|'2'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|fixed_ip_get_by_instance
name|'def'
name|'fixed_ip_get_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
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
op|','
name|'project_only'
op|'='
string|'"allow_none"'
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
DECL|member|network_get_by_uuid
dedent|''
name|'def'
name|'network_get_by_uuid'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFoundForUUID'
op|'('
op|')'
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
op|','
name|'project_only'
op|'='
string|'"allow_none"'
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
name|'return'
name|'self'
op|'.'
name|'vifs'
newline|'\n'
nl|'\n'
DECL|member|fixed_ips_by_virtual_interface
dedent|''
name|'def'
name|'fixed_ips_by_virtual_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vif_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'ip'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'.'
name|'fixed_ips'
nl|'\n'
name|'if'
name|'ip'
op|'['
string|"'virtual_interface_id'"
op|']'
op|'=='
name|'vif_id'
op|']'
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
name|'self'
op|'.'
name|'deallocate_fixed_ip_calls'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'network_rpcapi'
op|'='
name|'network_rpcapi'
op|'.'
name|'NetworkAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(matelakat) method signature should align with the faked one's"
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
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'deallocate_fixed_ip_calls'
op|'.'
name|'append'
op|'('
op|'('
name|'context'
op|','
name|'address'
op|','
name|'host'
op|')'
op|')'
newline|'\n'
comment|'# TODO(matelakat) use the deallocate_fixed_ip_calls instead'
nl|'\n'
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
op|','
name|'fixed_cidr'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_network
dedent|''
dedent|''
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
name|'CONF'
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
string|"'dns3'"
op|':'
string|"'192.168.%d.3'"
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
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'flat_injected'
op|':'
newline|'\n'
indent|'        '
name|'fake_network'
op|'['
string|"'injected'"
op|']'
op|'='
name|'True'
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
number|'1'
op|','
name|'n'
op|'+'
number|'1'
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
number|'1'
op|','
number|'100'
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
number|'1'
op|','
number|'100'
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
string|"'192.168.%d.%03d'"
op|'%'
op|'('
name|'network_id'
op|','
op|'('
name|'next_id'
op|'+'
number|'99'
op|')'
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
number|'1'
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
string|"'10.10.10.%03d'"
op|'%'
op|'('
name|'next_id'
op|'+'
number|'99'
op|')'
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
op|','
nl|'\n'
name|'spectacular'
op|'='
name|'False'
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
op|','
name|'fixed_ips'
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
name|'fixed_ips'
op|'='
op|'['
op|']'
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
number|'1'
op|','
name|'num_networks'
op|'+'
number|'1'
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
name|'global'
name|'fixed_ips'
newline|'\n'
name|'ips'
op|'='
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
number|'1'
op|','
name|'num_networks'
op|'+'
number|'1'
op|')'
nl|'\n'
name|'for'
name|'j'
name|'in'
name|'xrange'
op|'('
name|'ips_per_vif'
op|')'
op|']'
newline|'\n'
name|'fixed_ips'
op|'='
name|'ips'
newline|'\n'
name|'return'
name|'ips'
newline|'\n'
nl|'\n'
DECL|function|floating_ips_fake
dedent|''
name|'def'
name|'floating_ips_fake'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ip'
name|'in'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'address'
op|'=='
name|'ip'
op|'['
string|"'address'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'ip'
op|'['
string|"'floating_ips'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fixed_ips_v6_fake
dedent|''
name|'def'
name|'fixed_ips_v6_fake'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|"'2001:db8:0:%x::1'"
op|'%'
name|'i'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
name|'num_networks'
op|'+'
number|'1'
op|')'
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
DECL|function|vif_by_uuid_fake
dedent|''
name|'def'
name|'vif_by_uuid_fake'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:01'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'uuid'
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
number|'0'
op|'}'
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
op|','
name|'project_only'
op|'='
string|"'allow_none'"
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
DECL|function|get_subnets_by_net_id
dedent|''
name|'def'
name|'get_subnets_by_net_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'network_uuid'
op|','
nl|'\n'
name|'vif_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'i'
op|'='
name|'int'
op|'('
name|'network_uuid'
op|'['
op|'-'
number|'2'
op|':'
op|']'
op|')'
newline|'\n'
name|'subnet_v4'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'cidr'
op|'='
string|"'192.168.%d.0/24'"
op|'%'
name|'i'
op|','
nl|'\n'
name|'dns1'
op|'='
string|"'192.168.%d.3'"
op|'%'
name|'i'
op|','
nl|'\n'
name|'dns2'
op|'='
string|"'192.168.%d.4'"
op|'%'
name|'i'
op|','
nl|'\n'
name|'gateway'
op|'='
string|"'192.168.%d.1'"
op|'%'
name|'i'
op|')'
newline|'\n'
nl|'\n'
name|'subnet_v6'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'cidr'
op|'='
string|"'2001:db8:0:%x::/64'"
op|'%'
name|'i'
op|','
nl|'\n'
name|'gateway'
op|'='
string|"'fe80::def'"
op|')'
newline|'\n'
name|'return'
op|'['
name|'subnet_v4'
op|','
name|'subnet_v6'
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_network_by_uuid
dedent|''
name|'def'
name|'get_network_by_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'cidr_v6'
op|'='
string|"'fe80::/64'"
op|','
nl|'\n'
name|'bridge'
op|'='
string|"'br0'"
op|','
nl|'\n'
name|'label'
op|'='
string|"'public'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|get_v4_fake
dedent|''
name|'def'
name|'get_v4_fake'
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
name|'ips'
op|'='
name|'fixed_ips_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'ips'
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_v6_fake
dedent|''
name|'def'
name|'get_v6_fake'
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
name|'fixed_ips_v6_fake'
op|'('
op|')'
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
string|"'virtual_interface_get_by_uuid'"
op|','
name|'vif_by_uuid_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_by_uuid'"
op|','
name|'get_network_by_uuid'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova_ipam_lib'
op|'.'
name|'QuantumNovaIPAMLib'
op|','
string|"'get_subnets_by_net_id'"
op|','
nl|'\n'
name|'get_subnets_by_net_id'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova_ipam_lib'
op|'.'
name|'QuantumNovaIPAMLib'
op|','
string|"'get_v4_ips_by_interface'"
op|','
nl|'\n'
name|'get_v4_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova_ipam_lib'
op|'.'
name|'QuantumNovaIPAMLib'
op|','
string|"'get_v6_ips_by_interface'"
op|','
nl|'\n'
name|'get_v6_fake'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeContext
name|'class'
name|'FakeContext'
op|'('
name|'nova'
op|'.'
name|'context'
op|'.'
name|'RequestContext'
op|')'
op|':'
newline|'\n'
DECL|member|is_admin
indent|'        '
name|'def'
name|'is_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'nw_model'
op|'='
name|'network'
op|'.'
name|'get_instance_nw_info'
op|'('
nl|'\n'
name|'FakeContext'
op|'('
string|"'fakeuser'"
op|','
string|"'fake_project'"
op|')'
op|','
nl|'\n'
number|'0'
op|','
number|'0'
op|','
number|'3'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'spectacular'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nw_model'
newline|'\n'
dedent|''
name|'return'
name|'nw_model'
op|'.'
name|'legacy'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_nw_api_get_instance_nw_info
dedent|''
name|'def'
name|'stub_out_nw_api_get_instance_nw_info'
op|'('
name|'stubs'
op|','
name|'func'
op|'='
name|'None'
op|','
nl|'\n'
name|'num_networks'
op|'='
number|'1'
op|','
nl|'\n'
name|'ips_per_vif'
op|'='
number|'1'
op|','
nl|'\n'
name|'floating_ips_per_fixed_ip'
op|'='
number|'0'
op|','
nl|'\n'
name|'spectacular'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|get_instance_nw_info
indent|'    '
name|'def'
name|'get_instance_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake_get_instance_nw_info'
op|'('
name|'stubs'
op|','
name|'num_networks'
op|'='
name|'num_networks'
op|','
nl|'\n'
name|'ips_per_vif'
op|'='
name|'ips_per_vif'
op|','
nl|'\n'
name|'floating_ips_per_fixed_ip'
op|'='
name|'floating_ips_per_fixed_ip'
op|','
nl|'\n'
name|'spectacular'
op|'='
name|'spectacular'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'func'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'='
name|'get_instance_nw_info'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'get_instance_nw_info'"
op|','
name|'func'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_real_functions
dedent|''
name|'_real_functions'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_stub_network_methods
name|'def'
name|'set_stub_network_methods'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_real_functions'
newline|'\n'
name|'cm'
op|'='
name|'compute_manager'
op|'.'
name|'ComputeManager'
newline|'\n'
name|'if'
name|'not'
name|'_real_functions'
op|':'
newline|'\n'
indent|'        '
name|'_real_functions'
op|'='
op|'{'
nl|'\n'
string|"'_get_instance_nw_info'"
op|':'
name|'cm'
op|'.'
name|'_get_instance_nw_info'
op|','
nl|'\n'
string|"'_allocate_network'"
op|':'
name|'cm'
op|'.'
name|'_allocate_network'
op|','
nl|'\n'
string|"'_deallocate_network'"
op|':'
name|'cm'
op|'.'
name|'_deallocate_network'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_networkinfo
dedent|''
name|'def'
name|'fake_networkinfo'
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
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cm'
op|','
string|"'_get_instance_nw_info'"
op|','
name|'fake_networkinfo'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cm'
op|','
string|"'_allocate_network'"
op|','
name|'fake_networkinfo'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cm'
op|','
string|"'_deallocate_network'"
op|','
name|'lambda'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|':'
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unset_stub_network_methods
dedent|''
name|'def'
name|'unset_stub_network_methods'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_real_functions'
newline|'\n'
name|'if'
name|'_real_functions'
op|':'
newline|'\n'
indent|'        '
name|'cm'
op|'='
name|'compute_manager'
op|'.'
name|'ComputeManager'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'_real_functions'
op|':'
newline|'\n'
indent|'            '
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cm'
op|','
name|'name'
op|','
name|'_real_functions'
op|'['
name|'name'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_compute_with_ips
dedent|''
dedent|''
dedent|''
name|'def'
name|'stub_compute_with_ips'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'orig_get'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get'
newline|'\n'
name|'orig_get_all'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get_all'
newline|'\n'
nl|'\n'
DECL|function|fake_get
name|'def'
name|'fake_get'
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
name|'_get_instances_with_cached_ips'
op|'('
name|'orig_get'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get_all
dedent|''
name|'def'
name|'fake_get_all'
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
name|'_get_instances_with_cached_ips'
op|'('
name|'orig_get_all'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_all'"
op|','
name|'fake_get_all'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_fake_cache
dedent|''
name|'def'
name|'_get_fake_cache'
op|'('
op|')'
op|':'
newline|'\n'
DECL|function|_ip
indent|'    '
name|'def'
name|'_ip'
op|'('
name|'ip'
op|','
name|'fixed'
op|'='
name|'True'
op|','
name|'floats'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_dict'
op|'='
op|'{'
string|"'address'"
op|':'
name|'ip'
op|','
string|"'type'"
op|':'
string|"'fixed'"
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'fixed'
op|':'
newline|'\n'
indent|'            '
name|'ip_dict'
op|'['
string|"'type'"
op|']'
op|'='
string|"'floating'"
newline|'\n'
dedent|''
name|'if'
name|'fixed'
name|'and'
name|'floats'
op|':'
newline|'\n'
indent|'            '
name|'ip_dict'
op|'['
string|"'floating_ips'"
op|']'
op|'='
op|'['
name|'_ip'
op|'('
name|'f'
op|','
name|'fixed'
op|'='
name|'False'
op|')'
name|'for'
name|'f'
name|'in'
name|'floats'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'ip_dict'
newline|'\n'
nl|'\n'
dedent|''
name|'info'
op|'='
op|'['
op|'{'
string|"'address'"
op|':'
string|"'aa:bb:cc:dd:ee:ff'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'network'"
op|':'
op|'{'
string|"'bridge'"
op|':'
string|"'br0'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'private'"
op|','
nl|'\n'
string|"'subnets'"
op|':'
op|'['
op|'{'
string|"'cidr'"
op|':'
string|"'192.168.0.0/24'"
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
name|'_ip'
op|'('
string|"'192.168.0.3'"
op|')'
op|']'
op|'}'
op|']'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'        '
name|'ipv6_addr'
op|'='
string|"'fe80:b33f::a8bb:ccff:fedd:eeff'"
newline|'\n'
name|'info'
op|'['
number|'0'
op|']'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|'.'
name|'append'
op|'('
op|'{'
string|"'cidr'"
op|':'
string|"'fe80:b33f::/64'"
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
name|'_ip'
op|'('
name|'ipv6_addr'
op|')'
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_instances_with_cached_ips
dedent|''
name|'def'
name|'_get_instances_with_cached_ips'
op|'('
name|'orig_func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Kludge the cache into instance(s) without having to create DB\n    entries\n    """'
newline|'\n'
name|'instances'
op|'='
name|'orig_func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instances'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'['
string|"'info_cache'"
op|']'
op|'='
op|'{'
string|"'network_info'"
op|':'
name|'_get_fake_cache'
op|'('
op|')'
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'['
string|"'info_cache'"
op|']'
op|'='
op|'{'
string|"'network_info'"
op|':'
name|'_get_fake_cache'
op|'('
op|')'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'instances'
newline|'\n'
dedent|''
endmarker|''
end_unit
