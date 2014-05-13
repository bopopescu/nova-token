begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved'
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
comment|'#'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'neutronclient'
op|'.'
name|'common'
name|'import'
name|'exceptions'
name|'as'
name|'n_exc'
newline|'\n'
name|'from'
name|'neutronclient'
op|'.'
name|'v2_0'
name|'import'
name|'client'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'security_groups'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'neutronv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'security_group'
name|'import'
name|'neutron_driver'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestNeutronDriver
name|'class'
name|'TestNeutronDriver'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
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
name|'TestNeutronDriver'
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
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'neutronv2'
op|','
string|"'get_client'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'client'
op|'.'
name|'Client'
op|')'
newline|'\n'
name|'neutronv2'
op|'.'
name|'get_client'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'MultipleTimes'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'userid'"
op|','
string|"'my_tenantid'"
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'auth_token'"
op|','
nl|'\n'
string|"'bff4a5a6b9eb4ea2a6efec6eefb77936'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_with_project
dedent|''
name|'def'
name|'test_list_with_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
string|"'0af70a4d22cf4652824ddc1f2435dd85'"
newline|'\n'
name|'security_groups_list'
op|'='
op|'{'
string|"'security_groups'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_security_groups'
op|'('
name|'tenant_id'
op|'='
name|'project_id'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'security_groups_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'sg_api'
op|'='
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'sg_api'
op|'.'
name|'list'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'project'
op|'='
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_exceed_quota
dedent|''
name|'def'
name|'test_create_security_group_exceed_quota'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
string|"'test-security-group'"
newline|'\n'
name|'description'
op|'='
string|"'test-security-group'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'security_group'"
op|':'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'description'
op|'}'
op|'}'
newline|'\n'
name|'message'
op|'='
string|'"Quota exceeded for resources: [\'security_group\']"'
newline|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'create_security_group'
op|'('
nl|'\n'
name|'body'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'n_exc'
op|'.'
name|'NeutronClientException'
op|'('
name|'status_code'
op|'='
number|'409'
op|','
nl|'\n'
name|'message'
op|'='
name|'message'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'sg_api'
op|'='
name|'security_groups'
op|'.'
name|'NativeNeutronSecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'SecurityGroupLimitExceeded'
op|','
nl|'\n'
name|'sg_api'
op|'.'
name|'create_security_group'
op|','
name|'self'
op|'.'
name|'context'
op|','
name|'name'
op|','
nl|'\n'
name|'description'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_rules_exceed_quota
dedent|''
name|'def'
name|'test_create_security_group_rules_exceed_quota'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vals'
op|'='
op|'{'
string|"'protocol'"
op|':'
string|"'tcp'"
op|','
string|"'cidr'"
op|':'
string|"'0.0.0.0/0'"
op|','
nl|'\n'
string|"'parent_group_id'"
op|':'
string|"'7ae75663-277e-4a0e-8f87-56ea4e70cb47'"
op|','
nl|'\n'
string|"'group_id'"
op|':'
name|'None'
op|','
string|"'from_port'"
op|':'
number|'1025'
op|','
string|"'to_port'"
op|':'
number|'1025'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'security_group_rules'"
op|':'
op|'['
op|'{'
string|"'remote_group_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'direction'"
op|':'
string|"'ingress'"
op|','
string|"'protocol'"
op|':'
string|"'tcp'"
op|','
string|"'ethertype'"
op|':'
string|"'IPv4'"
op|','
nl|'\n'
string|"'port_range_max'"
op|':'
number|'1025'
op|','
string|"'port_range_min'"
op|':'
number|'1025'
op|','
nl|'\n'
string|"'security_group_id'"
op|':'
string|"'7ae75663-277e-4a0e-8f87-56ea4e70cb47'"
op|','
nl|'\n'
string|"'remote_ip_prefix'"
op|':'
string|"'0.0.0.0/0'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'name'
op|'='
string|"'test-security-group'"
newline|'\n'
name|'message'
op|'='
string|'"Quota exceeded for resources: [\'security_group_rule\']"'
newline|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'create_security_group_rule'
op|'('
nl|'\n'
name|'body'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'n_exc'
op|'.'
name|'NeutronClientException'
op|'('
name|'status_code'
op|'='
number|'409'
op|','
nl|'\n'
name|'message'
op|'='
name|'message'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'sg_api'
op|'='
name|'security_groups'
op|'.'
name|'NativeNeutronSecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'SecurityGroupLimitExceeded'
op|','
nl|'\n'
name|'sg_api'
op|'.'
name|'add_rules'
op|','
name|'self'
op|'.'
name|'context'
op|','
name|'None'
op|','
name|'name'
op|','
op|'['
name|'vals'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_security_group_with_no_port_range_and_not_tcp_udp_icmp
dedent|''
name|'def'
name|'test_list_security_group_with_no_port_range_and_not_tcp_udp_icmp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sg1'
op|'='
op|'{'
string|"'description'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'07f1362f-34f6-4136-819a-2dcde112269e'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
string|"'c166d9316f814891bcb66b96c4c891d6'"
op|','
nl|'\n'
string|"'security_group_rules'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'direction'"
op|':'
string|"'ingress'"
op|','
nl|'\n'
string|"'ethertype'"
op|':'
string|"'IPv4'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'0a4647f1-e1aa-488d-90e1-97a7d0293beb'"
op|','
nl|'\n'
string|"'port_range_max'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'port_range_min'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'protocol'"
op|':'
string|"'51'"
op|','
nl|'\n'
string|"'remote_group_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'remote_ip_prefix'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'security_group_id'"
op|':'
nl|'\n'
string|"'07f1362f-34f6-4136-819a-2dcde112269e'"
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
string|"'c166d9316f814891bcb66b96c4c891d6'"
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_security_groups'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'{'
string|"'security_groups'"
op|':'
op|'['
name|'sg1'
op|']'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'sg_api'
op|'='
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'sg_api'
op|'.'
name|'list'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
op|'{'
string|"'rules'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'from_port'"
op|':'
op|'-'
number|'1'
op|','
string|"'protocol'"
op|':'
string|"'51'"
op|','
string|"'to_port'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|"'parent_group_id'"
op|':'
string|"'07f1362f-34f6-4136-819a-2dcde112269e'"
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'0.0.0.0/0'"
op|','
string|"'group_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'0a4647f1-e1aa-488d-90e1-97a7d0293beb'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'c166d9316f814891bcb66b96c4c891d6'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'07f1362f-34f6-4136-819a-2dcde112269e'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'default'"
op|','
string|"'description'"
op|':'
string|"'default'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instances_security_group_bindings
dedent|''
name|'def'
name|'test_instances_security_group_bindings'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_id'
op|'='
string|"'c5a20e8d-c4b0-47cf-9dca-ebe4f758acb1'"
newline|'\n'
name|'port1_id'
op|'='
string|"'4c505aec-09aa-47bc-bcc0-940477e84dc0'"
newline|'\n'
name|'port2_id'
op|'='
string|"'b3b31a53-6e29-479f-ae5c-00b7b71a6d44'"
newline|'\n'
name|'sg1_id'
op|'='
string|"'2f7ce969-1a73-4ef9-bbd6-c9a91780ecd4'"
newline|'\n'
name|'sg2_id'
op|'='
string|"'20c89ce5-9388-4046-896e-64ffbd3eb584'"
newline|'\n'
name|'servers'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
name|'server_id'
op|'}'
op|']'
newline|'\n'
name|'ports'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
name|'port1_id'
op|','
string|"'device_id'"
op|':'
name|'server_id'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
op|'['
name|'sg1_id'
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'port2_id'
op|','
string|"'device_id'"
op|':'
name|'server_id'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
op|'['
name|'sg2_id'
op|']'
op|'}'
op|']'
newline|'\n'
name|'port_list'
op|'='
op|'{'
string|"'ports'"
op|':'
name|'ports'
op|'}'
newline|'\n'
name|'sg1'
op|'='
op|'{'
string|"'id'"
op|':'
name|'sg1_id'
op|','
string|"'name'"
op|':'
string|"'wol'"
op|'}'
newline|'\n'
name|'sg2'
op|'='
op|'{'
string|"'id'"
op|':'
name|'sg2_id'
op|','
string|"'name'"
op|':'
string|"'eor'"
op|'}'
newline|'\n'
name|'security_groups_list'
op|'='
op|'{'
string|"'security_groups'"
op|':'
op|'['
name|'sg1'
op|','
name|'sg2'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'sg_bindings'
op|'='
op|'{'
name|'server_id'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'wol'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'eor'"
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_ports'
op|'('
name|'device_id'
op|'='
op|'['
name|'server_id'
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'port_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_security_groups'
op|'('
name|'id'
op|'='
op|'['
name|'sg2_id'
op|','
name|'sg1_id'
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'security_groups_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'sg_api'
op|'='
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'sg_api'
op|'.'
name|'get_instances_security_groups_bindings'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'servers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'sg_bindings'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_instances_security_group_bindings_scale
dedent|''
name|'def'
name|'_test_instances_security_group_bindings_scale'
op|'('
name|'self'
op|','
name|'num_servers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'max_query'
op|'='
number|'150'
newline|'\n'
name|'sg1_id'
op|'='
string|"'2f7ce969-1a73-4ef9-bbd6-c9a91780ecd4'"
newline|'\n'
name|'sg2_id'
op|'='
string|"'20c89ce5-9388-4046-896e-64ffbd3eb584'"
newline|'\n'
name|'sg1'
op|'='
op|'{'
string|"'id'"
op|':'
name|'sg1_id'
op|','
string|"'name'"
op|':'
string|"'wol'"
op|'}'
newline|'\n'
name|'sg2'
op|'='
op|'{'
string|"'id'"
op|':'
name|'sg2_id'
op|','
string|"'name'"
op|':'
string|"'eor'"
op|'}'
newline|'\n'
name|'security_groups_list'
op|'='
op|'{'
string|"'security_groups'"
op|':'
op|'['
name|'sg1'
op|','
name|'sg2'
op|']'
op|'}'
newline|'\n'
name|'servers'
op|'='
op|'['
op|']'
newline|'\n'
name|'device_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'ports'
op|'='
op|'['
op|']'
newline|'\n'
name|'sg_bindings'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'0'
op|','
name|'num_servers'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server_id'
op|'='
string|'"server-%d"'
op|'%'
name|'i'
newline|'\n'
name|'port_id'
op|'='
string|'"port-%d"'
op|'%'
name|'i'
newline|'\n'
name|'servers'
op|'.'
name|'append'
op|'('
op|'{'
string|"'id'"
op|':'
name|'server_id'
op|'}'
op|')'
newline|'\n'
name|'device_ids'
op|'.'
name|'append'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'ports'
op|'.'
name|'append'
op|'('
op|'{'
string|"'id'"
op|':'
name|'port_id'
op|','
nl|'\n'
string|"'device_id'"
op|':'
name|'server_id'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
op|'['
name|'sg1_id'
op|','
name|'sg2_id'
op|']'
op|'}'
op|')'
newline|'\n'
name|'sg_bindings'
op|'['
name|'server_id'
op|']'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'wol'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'eor'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'0'
op|','
name|'num_servers'
op|','
name|'max_query'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_ports'
op|'('
nl|'\n'
name|'device_id'
op|'='
name|'device_ids'
op|'['
name|'x'
op|':'
name|'x'
op|'+'
name|'max_query'
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
string|"'ports'"
op|':'
name|'ports'
op|'['
name|'x'
op|':'
name|'x'
op|'+'
name|'max_query'
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_security_groups'
op|'('
name|'id'
op|'='
op|'['
name|'sg2_id'
op|','
name|'sg1_id'
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'security_groups_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'sg_api'
op|'='
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'sg_api'
op|'.'
name|'get_instances_security_groups_bindings'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'servers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'sg_bindings'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instances_security_group_bindings_less_than_max
dedent|''
name|'def'
name|'test_instances_security_group_bindings_less_than_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_instances_security_group_bindings_scale'
op|'('
number|'100'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instances_security_group_bindings_max
dedent|''
name|'def'
name|'test_instances_security_group_bindings_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_instances_security_group_bindings_scale'
op|'('
number|'150'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instances_security_group_bindings_more_then_max
dedent|''
name|'def'
name|'test_instances_security_group_bindings_more_then_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_instances_security_group_bindings_scale'
op|'('
number|'300'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instances_security_group_bindings_with_hidden_sg
dedent|''
name|'def'
name|'test_instances_security_group_bindings_with_hidden_sg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'servers'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
string|"'server_1'"
op|'}'
op|']'
newline|'\n'
name|'ports'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|','
string|"'device_id'"
op|':'
string|"'dev_1'"
op|','
string|"'security_groups'"
op|':'
op|'['
string|"'1'"
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|','
string|"'device_id'"
op|':'
string|"'dev_1'"
op|','
string|"'security_groups'"
op|':'
op|'['
string|"'2'"
op|']'
op|'}'
op|']'
newline|'\n'
name|'port_list'
op|'='
op|'{'
string|"'ports'"
op|':'
name|'ports'
op|'}'
newline|'\n'
name|'sg1'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|','
string|"'name'"
op|':'
string|"'wol'"
op|'}'
newline|'\n'
name|'sg2'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|','
string|"'name'"
op|':'
string|"'eor'"
op|'}'
newline|'\n'
comment|"# User doesn't have access to sg2"
nl|'\n'
name|'security_groups_list'
op|'='
op|'{'
string|"'security_groups'"
op|':'
op|'['
name|'sg1'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'sg_bindings'
op|'='
op|'{'
string|"'dev_1'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'wol'"
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_ports'
op|'('
name|'device_id'
op|'='
op|'['
string|"'server_1'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'port_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_security_groups'
op|'('
name|'id'
op|'='
op|'['
string|"'1'"
op|','
string|"'2'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'security_groups_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'sg_api'
op|'='
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'sg_api'
op|'.'
name|'get_instances_security_groups_bindings'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'servers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'sg_bindings'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_empty_security_groups
dedent|''
name|'def'
name|'test_instance_empty_security_groups'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'port_list'
op|'='
op|'{'
string|"'ports'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'device_id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'security_groups'"
op|':'
op|'['
op|']'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'moxed_client'
op|'.'
name|'list_ports'
op|'('
name|'device_id'
op|'='
op|'['
string|"'1'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'port_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'sg_api'
op|'='
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'sg_api'
op|'.'
name|'get_instance_security_groups'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
