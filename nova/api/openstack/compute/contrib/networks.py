begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Grid Dynamics'
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
nl|'\n'
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
name|'extensions'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'networks'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_dict
name|'def'
name|'network_dict'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'network'
op|':'
newline|'\n'
indent|'        '
name|'fields'
op|'='
op|'('
string|"'bridge'"
op|','
string|"'vpn_public_port'"
op|','
string|"'dhcp_start'"
op|','
nl|'\n'
string|"'bridge_interface'"
op|','
string|"'updated_at'"
op|','
string|"'id'"
op|','
string|"'cidr_v6'"
op|','
nl|'\n'
string|"'deleted_at'"
op|','
string|"'gateway'"
op|','
string|"'label'"
op|','
string|"'project_id'"
op|','
nl|'\n'
string|"'vpn_private_address'"
op|','
string|"'deleted'"
op|','
string|"'vlan'"
op|','
string|"'broadcast'"
op|','
nl|'\n'
string|"'netmask'"
op|','
string|"'injected'"
op|','
string|"'cidr'"
op|','
string|"'vpn_public_address'"
op|','
nl|'\n'
string|"'multi_host'"
op|','
string|"'dns1'"
op|','
string|"'host'"
op|','
string|"'gateway_v6'"
op|','
string|"'netmask_v6'"
op|','
nl|'\n'
string|"'created_at'"
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
op|'('
name|'field'
op|','
name|'network'
op|'['
name|'field'
op|']'
op|')'
name|'for'
name|'field'
name|'in'
name|'fields'
op|')'
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
name|'nova'
op|'.'
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|action
dedent|''
name|'def'
name|'action'
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
name|'_actions'
op|'='
op|'{'
nl|'\n'
string|"'disassociate'"
op|':'
name|'self'
op|'.'
name|'_disassociate'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'action'
op|','
name|'data'
name|'in'
name|'body'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'_actions'
op|'['
name|'action'
op|']'
op|'('
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Network does not have %s action"'
op|')'
op|'%'
name|'action'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Invalid request body"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_disassociate
dedent|''
name|'def'
name|'_disassociate'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'network_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'request'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Disassociating network with id %s"'
op|'%'
name|'network_id'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'disassociate'
op|'('
name|'context'
op|','
name|'network_id'
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
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'_'
op|'('
string|'"Network not found"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
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
DECL|member|show
dedent|''
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
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Showing network with id %s"'
op|')'
op|'%'
name|'id'
op|')'
newline|'\n'
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
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'_'
op|'('
string|'"Network not found"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'network'"
op|':'
name|'network_dict'
op|'('
name|'network'
op|')'
op|'}'
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
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Deleting network with id %s"'
op|')'
op|'%'
name|'id'
op|')'
newline|'\n'
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
name|'NetworkNotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'_'
op|'('
string|'"Network not found"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
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
name|'id'
op|','
name|'body'
op|'='
name|'None'
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
DECL|class|Networks
dedent|''
dedent|''
name|'class'
name|'Networks'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only Network Management Extension"""'
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
string|'"os-networks"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/networks/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-12-23T00:00:00+00:00"'
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
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-networks'"
op|','
nl|'\n'
name|'NetworkController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
name|'member_actions'
op|')'
newline|'\n'
name|'return'
op|'['
name|'res'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
