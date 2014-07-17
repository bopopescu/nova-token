begin_unit
comment|'# Copyright 2012 SINA Inc.'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'attach_interfaces'
newline|'\n'
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
name|'api'
name|'as'
name|'network_api'
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
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_network_cache_model'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID1
name|'FAKE_UUID1'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
DECL|variable|FAKE_UUID2
name|'FAKE_UUID2'
op|'='
string|"'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'"
newline|'\n'
nl|'\n'
DECL|variable|FAKE_PORT_ID1
name|'FAKE_PORT_ID1'
op|'='
string|"'11111111-1111-1111-1111-111111111111'"
newline|'\n'
DECL|variable|FAKE_PORT_ID2
name|'FAKE_PORT_ID2'
op|'='
string|"'22222222-2222-2222-2222-222222222222'"
newline|'\n'
DECL|variable|FAKE_PORT_ID3
name|'FAKE_PORT_ID3'
op|'='
string|"'33333333-3333-3333-3333-333333333333'"
newline|'\n'
nl|'\n'
DECL|variable|FAKE_NET_ID1
name|'FAKE_NET_ID1'
op|'='
string|"'44444444-4444-4444-4444-444444444444'"
newline|'\n'
DECL|variable|FAKE_NET_ID2
name|'FAKE_NET_ID2'
op|'='
string|"'55555555-5555-5555-5555-555555555555'"
newline|'\n'
DECL|variable|FAKE_NET_ID3
name|'FAKE_NET_ID3'
op|'='
string|"'66666666-6666-6666-6666-666666666666'"
newline|'\n'
nl|'\n'
DECL|variable|port_data1
name|'port_data1'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'FAKE_PORT_ID1'
op|','
nl|'\n'
string|'"network_id"'
op|':'
name|'FAKE_NET_ID1'
op|','
nl|'\n'
string|'"admin_state_up"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"ACTIVE"'
op|','
nl|'\n'
string|'"mac_address"'
op|':'
string|'"aa:aa:aa:aa:aa:aa"'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
string|'"10.0.1.2"'
op|']'
op|','
nl|'\n'
string|'"device_id"'
op|':'
name|'FAKE_UUID1'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|port_data2
name|'port_data2'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'FAKE_PORT_ID2'
op|','
nl|'\n'
string|'"network_id"'
op|':'
name|'FAKE_NET_ID2'
op|','
nl|'\n'
string|'"admin_state_up"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"ACTIVE"'
op|','
nl|'\n'
string|'"mac_address"'
op|':'
string|'"bb:bb:bb:bb:bb:bb"'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
string|'"10.0.2.2"'
op|']'
op|','
nl|'\n'
string|'"device_id"'
op|':'
name|'FAKE_UUID1'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|port_data3
name|'port_data3'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'FAKE_PORT_ID3'
op|','
nl|'\n'
string|'"network_id"'
op|':'
name|'FAKE_NET_ID3'
op|','
nl|'\n'
string|'"admin_state_up"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"ACTIVE"'
op|','
nl|'\n'
string|'"mac_address"'
op|':'
string|'"bb:bb:bb:bb:bb:bb"'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
string|'"10.0.2.2"'
op|']'
op|','
nl|'\n'
string|'"device_id"'
op|':'
string|"''"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|fake_networks
name|'fake_networks'
op|'='
op|'['
name|'FAKE_NET_ID1'
op|','
name|'FAKE_NET_ID2'
op|']'
newline|'\n'
DECL|variable|ports
name|'ports'
op|'='
op|'['
name|'port_data1'
op|','
name|'port_data2'
op|','
name|'port_data3'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_list_ports
name|'def'
name|'fake_list_ports'
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
indent|'    '
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'port'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'port'
op|'['
string|"'device_id'"
op|']'
op|'=='
name|'kwargs'
op|'['
string|"'device_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'append'
op|'('
name|'port'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
string|"'ports'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_show_port
dedent|''
name|'def'
name|'fake_show_port'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'port_id'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'port'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'port'
op|'['
string|"'id'"
op|']'
op|'=='
name|'port_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'port'"
op|':'
name|'port'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_attach_interface
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_attach_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_id'
op|','
name|'port_id'
op|','
nl|'\n'
name|'requested_ip'
op|'='
string|"'192.168.1.3'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'network_id'
op|':'
newline|'\n'
comment|'# if no network_id is given when add a port to an instance, use the'
nl|'\n'
comment|'# first default network.'
nl|'\n'
indent|'        '
name|'network_id'
op|'='
name|'fake_networks'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'network_id'
op|'=='
string|"'bad_id'"
op|':'
newline|'\n'
indent|'        '
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
name|'if'
name|'not'
name|'port_id'
op|':'
newline|'\n'
indent|'        '
name|'port_id'
op|'='
name|'ports'
op|'['
name|'fake_networks'
op|'.'
name|'index'
op|'('
name|'network_id'
op|')'
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'vif'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'id'"
op|']'
op|'='
name|'port_id'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|'='
name|'network_id'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
op|'='
name|'requested_ip'
newline|'\n'
name|'return'
name|'vif'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_detach_interface
dedent|''
name|'def'
name|'fake_detach_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'port_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'port'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'port'
op|'['
string|"'id'"
op|']'
op|'=='
name|'port_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'PortNotFound'
op|'('
name|'port_id'
op|'='
name|'port_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instance
dedent|''
name|'def'
name|'fake_get_instance'
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
indent|'    '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InterfaceAttachTests
dedent|''
name|'class'
name|'InterfaceAttachTests'
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
name|'InterfaceAttachTests'
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
name|'flags'
op|'('
name|'auth_strategy'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'url'
op|'='
string|"'http://anyhost/'"
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'url_timeout'
op|'='
number|'30'
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'show_port'"
op|','
name|'fake_show_port'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'list_ports'"
op|','
name|'fake_list_ports'
op|')'
newline|'\n'
name|'self'
op|'.'
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
name|'fake_get_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'expected_show'
op|'='
op|'{'
string|"'interface_attachment'"
op|':'
nl|'\n'
op|'{'
string|"'net_id'"
op|':'
name|'FAKE_NET_ID1'
op|','
nl|'\n'
string|"'port_id'"
op|':'
name|'FAKE_PORT_ID1'
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
name|'port_data1'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
string|"'port_state'"
op|':'
name|'port_data1'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
name|'port_data1'
op|'['
string|"'fixed_ips'"
op|']'
op|','
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_item_instance_not_found
dedent|''
name|'def'
name|'test_item_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v3/servers/fake/os-attach-interfaces/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
DECL|function|fake_get_instance_exception
name|'def'
name|'fake_get_instance_exception'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
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
name|'fake_get_instance_exception'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'attachments'
op|'.'
name|'index'
op|','
nl|'\n'
name|'req'
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v3/servers/fake/os-attach-interfaces/show'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'attachments'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'FAKE_UUID1'
op|','
name|'FAKE_PORT_ID1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'expected_show'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_instance_not_found
dedent|''
name|'def'
name|'test_show_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v3/servers/fake/os-attach-interfaces/show'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
DECL|function|fake_get_instance_exception
name|'def'
name|'fake_get_instance_exception'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
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
name|'fake_get_instance_exception'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'attachments'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
string|"'fake'"
op|','
name|'FAKE_PORT_ID1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_invalid
dedent|''
name|'def'
name|'test_show_invalid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v3/servers/fake/os-attach-interfaces/show'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'show'
op|','
name|'req'
op|','
name|'FAKE_UUID2'
op|','
name|'FAKE_PORT_ID1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'detach_interface'"
op|','
nl|'\n'
name|'fake_detach_interface'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/delete'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'attachments'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
name|'FAKE_UUID1'
op|','
name|'FAKE_PORT_ID1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'202 Accepted'"
op|','
name|'result'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_interface_instance_locked
dedent|''
name|'def'
name|'test_detach_interface_instance_locked'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_detach_interface_from_locked_server
indent|'        '
name|'def'
name|'fake_detach_interface_from_locked_server'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
name|'port_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
name|'instance_uuid'
op|'='
name|'FAKE_UUID1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
nl|'\n'
string|"'detach_interface'"
op|','
nl|'\n'
name|'fake_detach_interface_from_locked_server'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/delete'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID1'
op|','
nl|'\n'
name|'FAKE_PORT_ID1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_interface_not_found
dedent|''
name|'def'
name|'test_delete_interface_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'detach_interface'"
op|','
nl|'\n'
name|'fake_detach_interface'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/delete'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID1'
op|','
nl|'\n'
string|"'invaid-port-id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_instance_not_found
dedent|''
name|'def'
name|'test_delete_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'detach_interface'"
op|','
nl|'\n'
name|'fake_detach_interface'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/delete'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
DECL|function|fake_get_instance_exception
name|'def'
name|'fake_get_instance_exception'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
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
name|'fake_get_instance_exception'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
string|"'fake'"
op|','
nl|'\n'
string|"'invaid-port-id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_instance_locked
dedent|''
name|'def'
name|'test_attach_interface_instance_locked'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_attach_interface_to_locked_server
indent|'        '
name|'def'
name|'fake_attach_interface_to_locked_server'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
name|'network_id'
op|','
name|'port_id'
op|','
name|'requested_ip'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
name|'instance_uuid'
op|'='
name|'FAKE_UUID1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
nl|'\n'
string|"'attach_interface'"
op|','
nl|'\n'
name|'fake_attach_interface_to_locked_server'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/attach'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'FAKE_UUID1'
op|','
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_without_network_id
dedent|''
name|'def'
name|'test_attach_interface_without_network_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'attach_interface'"
op|','
nl|'\n'
name|'fake_attach_interface'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/attach'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'result'
op|'='
name|'attachments'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'FAKE_UUID1'
op|','
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'interface_attachment'"
op|']'
op|'['
string|"'net_id'"
op|']'
op|','
nl|'\n'
name|'FAKE_NET_ID1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_with_network_id
dedent|''
name|'def'
name|'test_attach_interface_with_network_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'attach_interface'"
op|','
nl|'\n'
name|'fake_attach_interface'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/attach'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'interface_attachment'"
op|':'
nl|'\n'
op|'{'
string|"'net_id'"
op|':'
name|'FAKE_NET_ID2'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'result'
op|'='
name|'attachments'
op|'.'
name|'create'
op|'('
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID1'
op|','
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'interface_attachment'"
op|']'
op|'['
string|"'net_id'"
op|']'
op|','
nl|'\n'
name|'FAKE_NET_ID2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_with_port_and_network_id
dedent|''
name|'def'
name|'test_attach_interface_with_port_and_network_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'attach_interface'"
op|','
nl|'\n'
name|'fake_attach_interface'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/attach'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'interface_attachment'"
op|':'
nl|'\n'
op|'{'
string|"'port_id'"
op|':'
name|'FAKE_PORT_ID1'
op|','
nl|'\n'
string|"'net_id'"
op|':'
name|'FAKE_NET_ID2'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'FAKE_UUID1'
op|','
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_instance_not_found
dedent|''
name|'def'
name|'test_attach_interface_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/attach'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'interface_attachment'"
op|':'
nl|'\n'
op|'{'
string|"'net_id'"
op|':'
name|'FAKE_NET_ID2'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
DECL|function|fake_get_instance_exception
name|'def'
name|'fake_get_instance_exception'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
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
name|'fake_get_instance_exception'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'create'
op|','
name|'req'
op|','
string|"'fake'"
op|','
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_attach_interface_with_invalid_parameter
dedent|''
name|'def'
name|'_test_attach_interface_with_invalid_parameter'
op|'('
name|'self'
op|','
name|'param'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'attach_interface'"
op|','
nl|'\n'
name|'fake_attach_interface'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/attach'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'interface_attachment'"
op|':'
name|'param'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'FAKE_UUID1'
op|','
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_instance_with_non_uuid_net_id
dedent|''
name|'def'
name|'test_attach_interface_instance_with_non_uuid_net_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
string|"'net_id'"
op|':'
string|"'non_uuid'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_attach_interface_with_invalid_parameter'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_instance_with_non_uuid_port_id
dedent|''
name|'def'
name|'test_attach_interface_instance_with_non_uuid_port_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
string|"'port_id'"
op|':'
string|"'non_uuid'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_attach_interface_with_invalid_parameter'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_interface_instance_with_non_array_fixed_ips
dedent|''
name|'def'
name|'test_attach_interface_instance_with_non_array_fixed_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
string|"'fixed_ips'"
op|':'
string|"'non_array'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_attach_interface_with_invalid_parameter'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InterfaceAttachTestsWithMock
dedent|''
dedent|''
name|'class'
name|'InterfaceAttachTestsWithMock'
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
name|'InterfaceAttachTestsWithMock'
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
name|'flags'
op|'('
name|'auth_strategy'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'url'
op|'='
string|"'http://anyhost/'"
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'url_timeout'
op|'='
number|'30'
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'attach_interface'"
op|')'
newline|'\n'
DECL|member|test_attach_interface_fixed_ip_already_in_use
name|'def'
name|'test_attach_interface_fixed_ip_already_in_use'
op|'('
name|'self'
op|','
nl|'\n'
name|'attach_mock'
op|','
nl|'\n'
name|'get_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_mock'
op|'.'
name|'side_effect'
op|'='
name|'fake_get_instance'
newline|'\n'
name|'attach_mock'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FixedIpAlreadyInUse'
op|'('
nl|'\n'
name|'address'
op|'='
string|"'10.0.3.2'"
op|','
name|'instance_uuid'
op|'='
name|'FAKE_UUID1'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'attach_interfaces'
op|'.'
name|'InterfaceAttachmentController'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/servers/fake/os-attach-interfaces/attach'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'FAKE_UUID1'
op|','
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
name|'attach_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'get_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'FAKE_UUID1'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
