begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Nicira, Inc.'
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
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_session'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
op|'.'
name|'network'
op|'.'
name|'quantum'
name|'import'
name|'manager'
name|'as'
name|'quantum_manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.quantum_network'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|networks
name|'networks'
op|'='
op|'['
op|'{'
string|"'label'"
op|':'
string|"'project1-net1'"
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
string|"'192.168.0.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'2001:1db8::/64'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'2001:1db8::1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'192.168.0.2'"
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
string|"'vpn_public_address'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project1'"
op|','
nl|'\n'
string|"'priority'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'label'"
op|':'
string|"'project2-net1'"
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
string|"'192.168.1.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'2001:1db9::/64'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'2001:1db9::1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.1.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'192.168.1.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'192.168.0.2'"
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
string|"'fake_project2'"
op|','
nl|'\n'
string|"'priority'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'label'"
op|':'
string|'"public"'
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
string|"'10.0.0.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'2001:1dba::/64'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'2001:1dba::1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'10.0.0.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'10.0.0.2'"
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
name|'None'
op|','
nl|'\n'
string|"'priority'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'label'"
op|':'
string|'"project2-net2"'
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
string|"'9.0.0.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'2001:1dbb::/64'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'2001:1dbb::1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'9.0.0.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'9.0.0.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'9.0.0.1'"
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'9.0.0.2'"
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
string|'"fake_project2"'
op|','
nl|'\n'
string|"'priority'"
op|':'
number|'2'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# this is a base class to be used by all other Quantum Test classes'
nl|'\n'
DECL|class|QuantumTestCaseBase
name|'class'
name|'QuantumTestCaseBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_delete_nets
indent|'    '
name|'def'
name|'test_create_and_delete_nets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nets'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_delete_nets'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_nets
dedent|''
name|'def'
name|'_create_nets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'n'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
name|'n'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'create_networks'
op|'('
name|'ctx'
op|','
nl|'\n'
name|'label'
op|'='
name|'n'
op|'['
string|"'label'"
op|']'
op|','
name|'cidr'
op|'='
name|'n'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
name|'multi_host'
op|'='
name|'n'
op|'['
string|"'multi_host'"
op|']'
op|','
nl|'\n'
name|'num_networks'
op|'='
number|'1'
op|','
name|'network_size'
op|'='
number|'256'
op|','
name|'cidr_v6'
op|'='
name|'n'
op|'['
string|"'cidr_v6'"
op|']'
op|','
nl|'\n'
name|'gateway_v6'
op|'='
name|'n'
op|'['
string|"'gateway_v6'"
op|']'
op|','
name|'bridge'
op|'='
name|'None'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
name|'None'
op|','
name|'dns1'
op|'='
name|'n'
op|'['
string|"'dns1'"
op|']'
op|','
nl|'\n'
name|'dns2'
op|'='
name|'n'
op|'['
string|"'dns2'"
op|']'
op|','
name|'project_id'
op|'='
name|'n'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
name|'priority'
op|'='
name|'n'
op|'['
string|"'priority'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_nets
dedent|''
dedent|''
name|'def'
name|'_delete_nets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'n'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
name|'n'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'delete_network'
op|'('
name|'ctx'
op|','
name|'n'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_and_deallocate_instance_static
dedent|''
dedent|''
name|'def'
name|'test_allocate_and_deallocate_instance_static'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nets'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'project_id'
op|'='
string|'"fake_project1"'
newline|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_create'
op|'('
name|'ctx'
op|','
nl|'\n'
op|'{'
string|'"project_id"'
op|':'
name|'project_id'
op|'}'
op|')'
newline|'\n'
name|'nw_info'
op|'='
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'allocate_for_instance'
op|'('
name|'ctx'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|','
name|'host'
op|'='
string|'""'
op|','
nl|'\n'
name|'instance_type_id'
op|'='
name|'instance_ref'
op|'['
string|"'instance_type_id'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'nw_info'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
comment|"# we don't know which order the NICs will be in until we"
nl|'\n'
comment|'# introduce the notion of priority'
nl|'\n'
comment|'# v4 cidr'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"10."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"192."'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# v4 address'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"10."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"192."'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# v6 cidr'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr_v6'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1dba:"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr_v6'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1db8:"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# v6 address'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
nl|'\n'
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ip6s'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1dba:"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
nl|'\n'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ip6s'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1db8:"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'deallocate_for_instance'
op|'('
name|'ctx'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_delete_nets'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_and_deallocate_instance_dynamic
dedent|''
name|'def'
name|'test_allocate_and_deallocate_instance_dynamic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nets'
op|'('
op|')'
newline|'\n'
name|'project_id'
op|'='
string|'"fake_project2"'
newline|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'net_ids'
op|'='
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'q_conn'
op|'.'
name|'get_networks_for_tenant'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'requested_networks'
op|'='
op|'['
op|'('
name|'net_id'
op|','
name|'None'
op|')'
name|'for'
name|'net_id'
name|'in'
name|'net_ids'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'validate_networks'
op|'('
name|'ctx'
op|','
name|'requested_networks'
op|')'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_create'
op|'('
name|'ctx'
op|','
nl|'\n'
op|'{'
string|'"project_id"'
op|':'
name|'project_id'
op|'}'
op|')'
newline|'\n'
name|'nw_info'
op|'='
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'allocate_for_instance'
op|'('
name|'ctx'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|','
name|'host'
op|'='
string|'""'
op|','
nl|'\n'
name|'instance_type_id'
op|'='
name|'instance_ref'
op|'['
string|"'instance_type_id'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'nw_info'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
comment|"# we don't know which order the NICs will be in until we"
nl|'\n'
comment|'# introduce the notion of priority'
nl|'\n'
comment|'# v4 cidr'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"9."'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"9."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"192."'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"192."'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# v4 address'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"9."'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"9."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"192."'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"192."'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# v6 cidr'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr_v6'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1dbb:"'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr_v6'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1dbb:"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr_v6'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1db9:"'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'cidr_v6'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1db9:"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# v6 address'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ip6s'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1dbb:"'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ip6s'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1dbb:"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ip6s'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1db9:"'
op|')'
name|'or'
name|'nw_info'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ip6s'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'.'
name|'startswith'
op|'('
string|'"2001:1db9:"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'deallocate_for_instance'
op|'('
name|'ctx'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_delete_nets'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_bad_network
dedent|''
name|'def'
name|'test_validate_bad_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
string|"'fake_project1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NetworkNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'net_man'
op|'.'
name|'validate_networks'
op|','
name|'ctx'
op|','
op|'['
op|'('
string|'""'
op|','
name|'None'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumNovaIPAMTestCase
dedent|''
dedent|''
name|'class'
name|'QuantumNovaIPAMTestCase'
op|'('
name|'QuantumTestCaseBase'
op|','
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'QuantumNovaIPAMTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'net_man'
op|'='
name|'quantum_manager'
op|'.'
name|'QuantumManager'
op|'('
name|'ipam_lib'
op|'='
string|'"nova.network.quantum.nova_ipam_lib"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Tests seem to create some networks by default, which'
nl|'\n'
comment|"# we don't want.  So we delete them."
nl|'\n'
nl|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
string|"'fake_project1'"
op|')'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'for'
name|'n'
name|'in'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctx'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'network_delete_safe'
op|'('
name|'ctx'
op|','
name|'n'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(danwent): I've found that other unit tests have a nasty"
nl|'\n'
comment|'# habit of of creating fixed IPs and not cleaning up, which'
nl|'\n'
comment|'# can confuse these tests, so we clean them all.'
nl|'\n'
dedent|''
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'FixedIp'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'fip_ref'
name|'in'
name|'result'
op|':'
newline|'\n'
indent|'                '
name|'session'
op|'.'
name|'delete'
op|'('
name|'fip_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME(danwent): Cannot run this unit tests automatically for now, as'
nl|'\n'
comment|'# it requires melange to be running locally.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#class QuantumMelangeIPAMTestCase(QuantumTestCaseBase, test.TestCase):'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    def setUp(self):'
nl|'\n'
comment|'#        super(QuantumMelangeIPAMTestCase, self).setUp()'
nl|'\n'
comment|'#        self.net_man = quantum_manager.QuantumManager( \\'
nl|'\n'
comment|'#                ipam_lib="nova.network.quantum.melange_ipam_lib")'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
