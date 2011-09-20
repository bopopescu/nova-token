begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.ips'"
op|')'
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
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The servers addresses API controller for the Openstack API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'compute_api'
op|'='
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'='
name|'nova'
op|'.'
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance
dedent|''
name|'def'
name|'_get_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance does not exist"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerV10
dedent|''
dedent|''
name|'class'
name|'ControllerV10'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'_get_networks_for_instance'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'network_api'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
op|'.'
name|'ViewBuilderV10'
op|'('
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'addresses'"
op|':'
name|'builder'
op|'.'
name|'build'
op|'('
name|'networks'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'_get_networks_for_instance'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'network_api'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'id'
op|'=='
string|"'private'"
op|':'
newline|'\n'
indent|'            '
name|'view'
op|'='
name|'builder'
op|'.'
name|'build_private_parts'
op|'('
name|'networks'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'id'
op|'=='
string|"'public'"
op|':'
newline|'\n'
indent|'            '
name|'view'
op|'='
name|'builder'
op|'.'
name|'build_public_parts'
op|'('
name|'networks'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Only private and public networks available"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
name|'id'
op|':'
name|'view'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_view_builder
dedent|''
name|'def'
name|'_get_view_builder'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
op|'.'
name|'ViewBuilderV10'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerV11
dedent|''
dedent|''
name|'class'
name|'ControllerV11'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'_get_networks_for_instance'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'network_api'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'addresses'"
op|':'
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
op|'('
name|'networks'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'_get_networks_for_instance'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'network_api'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'network'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build_network'
op|'('
name|'networks'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'network'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance is not a member of specified network"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'network'
newline|'\n'
nl|'\n'
DECL|member|_get_view_builder
dedent|''
name|'def'
name|'_get_view_builder'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
op|'.'
name|'ViewBuilderV11'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IPXMLSerializer
dedent|''
dedent|''
name|'class'
name|'IPXMLSerializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|NSMAP
indent|'    '
name|'NSMAP'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'xmlns'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'IPXMLSerializer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'xmlns'
op|'='
name|'xmlns'
op|')'
newline|'\n'
nl|'\n'
DECL|member|populate_addresses_node
dedent|''
name|'def'
name|'populate_addresses_node'
op|'('
name|'self'
op|','
name|'addresses_elem'
op|','
name|'addresses_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
op|'('
name|'network_id'
op|','
name|'ip_dicts'
op|')'
name|'in'
name|'addresses_dict'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_elem'
op|'='
name|'self'
op|'.'
name|'_create_network_node'
op|'('
name|'network_id'
op|','
name|'ip_dicts'
op|')'
newline|'\n'
name|'addresses_elem'
op|'.'
name|'append'
op|'('
name|'network_elem'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_network_node
dedent|''
dedent|''
name|'def'
name|'_create_network_node'
op|'('
name|'self'
op|','
name|'network_id'
op|','
name|'ip_dicts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_elem'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'network'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'network_elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|','
name|'str'
op|'('
name|'network_id'
op|')'
op|')'
newline|'\n'
name|'for'
name|'ip_dict'
name|'in'
name|'ip_dicts'
op|':'
newline|'\n'
indent|'            '
name|'ip_elem'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'network_elem'
op|','
string|"'ip'"
op|')'
newline|'\n'
name|'ip_elem'
op|'.'
name|'set'
op|'('
string|"'version'"
op|','
name|'str'
op|'('
name|'ip_dict'
op|'['
string|"'version'"
op|']'
op|')'
op|')'
newline|'\n'
name|'ip_elem'
op|'.'
name|'set'
op|'('
string|"'addr'"
op|','
name|'ip_dict'
op|'['
string|"'addr'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_elem'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'network_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'network_id'
op|','
name|'ip_dicts'
op|')'
op|'='
name|'network_dict'
op|'.'
name|'items'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'network'
op|'='
name|'self'
op|'.'
name|'_create_network_node'
op|'('
name|'network_id'
op|','
name|'ip_dicts'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_to_xml'
op|'('
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'addresses_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'addresses'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'addresses'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'populate_addresses_node'
op|'('
name|'addresses'
op|','
nl|'\n'
name|'addresses_dict'
op|'.'
name|'get'
op|'('
string|"'addresses'"
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_to_xml'
op|'('
name|'addresses'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_networks_for_instance
dedent|''
dedent|''
name|'def'
name|'_get_networks_for_instance'
op|'('
name|'context'
op|','
name|'network_api'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a prepared nw_info list for passing into the view\n    builders\n\n    We end up with a datastructure like:\n    {\'public\': {\'ips\': [{\'addr\': \'10.0.0.1\', \'version\': 4},\n                        {\'addr\': \'2001::1\', \'version\': 6}],\n                \'floating_ips\': [{\'addr\': \'172.16.0.1\', \'version\': 4},\n                                 {\'addr\': \'172.16.2.1\', \'version\': 4}]},\n     ...}\n    """'
newline|'\n'
DECL|function|_get_floats
name|'def'
name|'_get_floats'
op|'('
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network_api'
op|'.'
name|'get_floating_ips_by_fixed_address'
op|'('
name|'context'
op|','
name|'ip'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_emit_addr
dedent|''
name|'def'
name|'_emit_addr'
op|'('
name|'ip'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'addr'"
op|':'
name|'ip'
op|','
string|"'version'"
op|':'
name|'version'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'stub_network'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'nw_info'
op|'='
name|'network_api'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'networks'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'net'
op|','
name|'info'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'='
op|'{'
string|"'ips'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
name|'network'
op|'['
string|"'floating_ips'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
string|"'ip6s'"
name|'in'
name|'info'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'ips'"
op|']'
op|'.'
name|'extend'
op|'('
op|'['
name|'_emit_addr'
op|'('
name|'ip'
op|'['
string|"'ip'"
op|']'
op|','
nl|'\n'
number|'6'
op|')'
name|'for'
name|'ip'
name|'in'
name|'info'
op|'['
string|"'ip6s'"
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'ip'
name|'in'
name|'info'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'['
string|"'ips'"
op|']'
op|'.'
name|'append'
op|'('
name|'_emit_addr'
op|'('
name|'ip'
op|'['
string|"'ip'"
op|']'
op|','
number|'4'
op|')'
op|')'
newline|'\n'
name|'floats'
op|'='
op|'['
name|'_emit_addr'
op|'('
name|'addr'
op|','
nl|'\n'
number|'4'
op|')'
name|'for'
name|'addr'
name|'in'
name|'_get_floats'
op|'('
name|'ip'
op|'['
string|"'ip'"
op|']'
op|')'
op|']'
newline|'\n'
name|'network'
op|'['
string|"'floating_ips'"
op|']'
op|'.'
name|'extend'
op|'('
name|'floats'
op|')'
newline|'\n'
dedent|''
name|'networks'
op|'['
name|'info'
op|'['
string|"'label'"
op|']'
op|']'
op|'='
name|'network'
newline|'\n'
dedent|''
name|'return'
name|'networks'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
name|'def'
name|'create_resource'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'controller'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'ControllerV10'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'ControllerV11'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|"'list_collections'"
op|':'
op|'{'
nl|'\n'
string|"'public'"
op|':'
op|'{'
string|"'item_name'"
op|':'
string|"'ip'"
op|','
string|"'item_key'"
op|':'
string|"'addr'"
op|'}'
op|','
nl|'\n'
string|"'private'"
op|':'
op|'{'
string|"'item_name'"
op|':'
string|"'ip'"
op|','
string|"'item_key'"
op|':'
string|"'addr'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'xml_serializer'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|','
name|'xmlns'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|')'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'IPXMLSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
newline|'\n'
nl|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
op|'{'
string|"'application/xml'"
op|':'
name|'xml_serializer'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'controller'
op|','
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
