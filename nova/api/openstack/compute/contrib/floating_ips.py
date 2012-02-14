begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
nl|'\n'
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2011 Eldar Nugaev, Kirill Shileev, Ilya Alekseyev'
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
comment|'#    under the License'
nl|'\n'
nl|'\n'
name|'import'
name|'webob'
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
name|'from'
name|'nova'
name|'import'
name|'compute'
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
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
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
string|"'floating_ips'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_float_ip
name|'def'
name|'make_float_ip'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'ip'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'pool'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'fixed_ip'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'instance_id'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPTemplate
dedent|''
name|'class'
name|'FloatingIPTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'floating_ip'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'floating_ip'"
op|')'
newline|'\n'
name|'make_float_ip'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPsTemplate
dedent|''
dedent|''
name|'class'
name|'FloatingIPsTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'floating_ips'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'floating_ip'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'floating_ips'"
op|')'
newline|'\n'
name|'make_float_ip'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ip_view
dedent|''
dedent|''
name|'def'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'floating_ip'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'ip'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'floating_ip'
op|'['
string|"'pool'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'floating_ip'
op|'['
string|"'instance'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'floating_ip'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ips_view
dedent|''
name|'def'
name|'_translate_floating_ips_view'
op|'('
name|'floating_ips'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'floating_ips'"
op|':'
op|'['
name|'_translate_floating_ip_view'
op|'('
name|'ip'
op|')'
op|'['
string|"'floating_ip'"
op|']'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'floating_ips'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPController
dedent|''
name|'class'
name|'FloatingIPController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Floating IPs API controller for the OpenStack API."""'
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
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIPController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_fixed_ip
dedent|''
name|'def'
name|'_get_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_ip_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'fixed_ip_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_fixed_ip'
op|'('
name|'context'
op|','
name|'fixed_ip_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_instance
dedent|''
dedent|''
name|'def'
name|'_get_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_metadata
dedent|''
name|'def'
name|'_set_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip_id'
op|'='
name|'floating_ip'
op|'['
string|"'fixed_ip_id'"
op|']'
newline|'\n'
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'self'
op|'.'
name|'_get_fixed_ip'
op|'('
name|'context'
op|','
nl|'\n'
name|'fixed_ip_id'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'instance_id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'instance_id'
op|':'
newline|'\n'
indent|'            '
name|'floating_ip'
op|'['
string|"'instance'"
op|']'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'floating_ip'
op|'['
string|"'instance'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'FloatingIPTemplate'
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
string|'"""Return data about the given floating ip."""'
newline|'\n'
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
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip'
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
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_set_metadata'
op|'('
name|'context'
op|','
name|'floating_ip'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'FloatingIPsTemplate'
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
string|'"""Return a list of floating ips allocated to a project."""'
newline|'\n'
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
name|'floating_ips'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ips_by_project'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'floating_ips'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_set_metadata'
op|'('
name|'context'
op|','
name|'floating_ip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_translate_floating_ips_view'
op|'('
name|'floating_ips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'FloatingIPTemplate'
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
op|'='
name|'None'
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
name|'pool'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'body'
name|'and'
string|"'pool'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'pool'
op|'='
name|'body'
op|'['
string|"'pool'"
op|']'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'allocate_floating_ip'
op|'('
name|'context'
op|','
name|'pool'
op|')'
newline|'\n'
name|'ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|'# NOTE(tr3buchet) - why does this block exist?'
nl|'\n'
indent|'            '
name|'if'
name|'ex'
op|'.'
name|'exc_type'
op|'=='
string|"'NoMoreFloatingIps'"
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'pool'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No more floating ips in pool %s."'
op|')'
op|'%'
name|'pool'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No more floating ips available."'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'_translate_floating_ip_view'
op|'('
name|'ip'
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
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'fixed_ip_id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'disassociate_floating_ip'
op|'('
name|'context'
op|','
nl|'\n'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'release_floating_ip'
op|'('
name|'context'
op|','
nl|'\n'
name|'address'
op|'='
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_ip_by_id
dedent|''
name|'def'
name|'_get_ip_by_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks that value is id and then returns its address."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPActionController
dedent|''
dedent|''
name|'class'
name|'FloatingIPActionController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FloatingIPActionController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
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
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'addFloatingIp'"
op|')'
newline|'\n'
DECL|member|_add_floating_ip
name|'def'
name|'_add_floating_ip'
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
string|'"""Associate floating_ip to an instance."""'
newline|'\n'
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
name|'address'
op|'='
name|'body'
op|'['
string|"'addFloatingIp'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Missing parameter dict"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Address not specified"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'associate_floating_ip'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFoundForInstance'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No fixed ips associated to instance"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Associate floating ip failed"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'removeFloatingIp'"
op|')'
newline|'\n'
DECL|member|_remove_floating_ip
name|'def'
name|'_remove_floating_ip'
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
string|'"""Dissociate floating_ip from an instance."""'
newline|'\n'
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
name|'address'
op|'='
name|'body'
op|'['
string|"'removeFloatingIp'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Missing parameter dict"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Address not specified"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip_by_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'address'
op|')'
newline|'\n'
name|'if'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'fixed_ip_id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'disassociate_floating_ip'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Floating_ips
dedent|''
dedent|''
name|'class'
name|'Floating_ips'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Floating IPs support"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Floating_ips"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-floating-ips"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/floating_ips/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-06-16T00:00:00+00:00"'
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
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-floating-ips'"
op|','
nl|'\n'
name|'FloatingIPController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
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
name|'controller'
op|'='
name|'FloatingIPActionController'
op|'('
op|')'
newline|'\n'
name|'extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'servers'"
op|','
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'extension'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
