begin_unit
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
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
name|'netaddr'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'schemas'
name|'import'
name|'networks'
name|'as'
name|'schema'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
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
name|'import'
name|'validation'
newline|'\n'
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
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'base_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
name|'as'
name|'obj_fields'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-networks'"
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_dict
name|'def'
name|'network_dict'
op|'('
name|'context'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fields'
op|'='
op|'('
string|"'id'"
op|','
string|"'cidr'"
op|','
string|"'netmask'"
op|','
string|"'gateway'"
op|','
string|"'broadcast'"
op|','
string|"'dns1'"
op|','
string|"'dns2'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|','
string|"'gateway_v6'"
op|','
string|"'label'"
op|','
string|"'netmask_v6'"
op|')'
newline|'\n'
name|'admin_fields'
op|'='
op|'('
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'deleted_at'"
op|','
string|"'deleted'"
op|','
nl|'\n'
string|"'injected'"
op|','
string|"'bridge'"
op|','
string|"'vlan'"
op|','
string|"'vpn_public_address'"
op|','
nl|'\n'
string|"'vpn_public_port'"
op|','
string|"'vpn_private_address'"
op|','
string|"'dhcp_start'"
op|','
nl|'\n'
string|"'project_id'"
op|','
string|"'host'"
op|','
string|"'bridge_interface'"
op|','
string|"'multi_host'"
op|','
nl|'\n'
string|"'priority'"
op|','
string|"'rxtx_base'"
op|','
string|"'mtu'"
op|','
string|"'dhcp_server'"
op|','
nl|'\n'
string|"'enable_dhcp'"
op|','
string|"'share_address'"
op|')'
newline|'\n'
name|'if'
name|'network'
op|':'
newline|'\n'
comment|'# NOTE(mnaser): We display a limited set of fields so users can know'
nl|'\n'
comment|'#               what networks are available, extra system-only fields'
nl|'\n'
comment|'#               are only visible if they are an admin.'
nl|'\n'
indent|'        '
name|'if'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'fields'
op|'+='
name|'admin_fields'
newline|'\n'
comment|'# TODO(mriedem): Remove the NovaObject type check once the'
nl|'\n'
comment|'# network.create API is returning objects.'
nl|'\n'
dedent|''
name|'is_obj'
op|'='
name|'isinstance'
op|'('
name|'network'
op|','
name|'base_obj'
op|'.'
name|'NovaObject'
op|')'
newline|'\n'
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'fields'
op|':'
newline|'\n'
comment|'# NOTE(mriedem): If network is an object, IPAddress fields need to'
nl|'\n'
comment|'# be cast to a string so they look the same in the response as'
nl|'\n'
comment|'# before the objects conversion.'
nl|'\n'
indent|'            '
name|'if'
name|'is_obj'
name|'and'
name|'isinstance'
op|'('
name|'network'
op|'.'
name|'fields'
op|'['
name|'field'
op|']'
op|'.'
name|'AUTO_TYPE'
op|','
nl|'\n'
name|'obj_fields'
op|'.'
name|'IPAddress'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): Here, network should be an object, which could'
nl|'\n'
comment|'# have come from neutron and thus be missing most of the'
nl|'\n'
comment|'# attributes. Providing a default to get() avoids trying to'
nl|'\n'
comment|'# lazy-load missing attributes.'
nl|'\n'
indent|'                '
name|'val'
op|'='
name|'network'
op|'.'
name|'get'
op|'('
name|'field'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'val'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'['
name|'field'
op|']'
op|'='
name|'str'
op|'('
name|'val'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'['
name|'field'
op|']'
op|'='
name|'val'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# It's either not an object or it's not an IPAddress field."
nl|'\n'
indent|'                '
name|'result'
op|'['
name|'field'
op|']'
op|'='
name|'network'
op|'.'
name|'get'
op|'('
name|'field'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'uuid'
op|'='
name|'network'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
name|'if'
name|'uuid'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkController
dedent|''
dedent|''
name|'class'
name|'NetworkController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
name|'network_api'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'network_api'
op|'='
name|'network_api'
name|'or'
name|'network'
op|'.'
name|'API'
op|'('
name|'skip_policy_check'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'view'"
op|')'
newline|'\n'
name|'networks'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'result'
op|'='
op|'['
name|'network_dict'
op|'('
name|'context'
op|','
name|'net_ref'
op|')'
name|'for'
name|'net_ref'
name|'in'
name|'networks'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'networks'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|'"disassociate"'
op|')'
newline|'\n'
DECL|member|_disassociate_host_and_project
name|'def'
name|'_disassociate_host_and_project'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'associate'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'project'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Network not found"'
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
name|'except'
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'common'
op|'.'
name|'raise_feature_not_supported'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'view'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Network not found"'
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
op|'{'
string|"'network'"
op|':'
name|'network_dict'
op|'('
name|'context'
op|','
name|'network'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkInUse'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Network not found"'
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
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'409'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'schema'
op|'.'
name|'create'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
name|'body'
op|'['
string|'"network"'
op|']'
newline|'\n'
nl|'\n'
name|'cidr'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|'"cidr"'
op|')'
name|'or'
name|'params'
op|'.'
name|'get'
op|'('
string|'"cidr_v6"'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'['
string|'"num_networks"'
op|']'
op|'='
number|'1'
newline|'\n'
name|'params'
op|'['
string|'"network_size"'
op|']'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
op|'.'
name|'size'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
op|'**'
name|'params'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'InvalidCidr'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidIntValue'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidAddress'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'NetworkNotCreated'
op|')'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'ex'
op|'.'
name|'format_message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CidrConflict'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'ex'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"network"'
op|':'
name|'network_dict'
op|'('
name|'context'
op|','
name|'network'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'schema'
op|'.'
name|'add_network_to_project'
op|')'
newline|'\n'
DECL|member|add
name|'def'
name|'add'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'network_id'
op|'='
name|'body'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'add_network_to_project'
op|'('
nl|'\n'
name|'context'
op|','
name|'project_id'
op|','
name|'network_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'common'
op|'.'
name|'raise_feature_not_supported'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'NoMoreNetworks'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'NetworkNotFoundForUUID'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Networks
dedent|''
dedent|''
dedent|''
name|'class'
name|'Networks'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only Network Management Extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Networks"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'member_actions'
op|'='
op|'{'
string|"'action'"
op|':'
string|"'POST'"
op|'}'
newline|'\n'
name|'collection_actions'
op|'='
op|'{'
string|"'add'"
op|':'
string|"'POST'"
op|'}'
newline|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
name|'ALIAS'
op|','
name|'NetworkController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
name|'member_actions'
op|','
nl|'\n'
name|'collection_actions'
op|'='
name|'collection_actions'
op|')'
newline|'\n'
name|'return'
op|'['
name|'res'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
