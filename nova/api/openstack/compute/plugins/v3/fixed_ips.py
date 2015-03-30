begin_unit
comment|'# Copyright 2012 IBM Corp.'
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
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
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
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'fixed_ips'
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
name|'objects'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-fixed-ips'"
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
DECL|class|FixedIPController
name|'class'
name|'FixedIPController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|"'2.1'"
op|','
string|"'2.3'"
op|')'
newline|'\n'
DECL|member|_fill_reserved_status
name|'def'
name|'_fill_reserved_status'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'fixed_ip'
op|','
name|'fixed_ip_info'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mriedem): To be backwards compatible, < 2.4 version does not'
nl|'\n'
comment|'# show anything about reserved status.'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|"'2.4'"
op|')'
comment|'# noqa'
newline|'\n'
DECL|member|_fill_reserved_status
name|'def'
name|'_fill_reserved_status'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'fixed_ip'
op|','
name|'fixed_ip_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'reserved'"
op|']'
op|'='
name|'fixed_ip'
op|'.'
name|'reserved'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|')'
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
string|'"""Return data about the given fixed ip."""'
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
name|'attrs'
op|'='
op|'['
string|"'network'"
op|','
string|"'instance'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'.'
name|'get_by_address'
op|'('
name|'context'
op|','
name|'id'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'attrs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFoundForAddress'
name|'as'
name|'ex'
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
name|'except'
name|'exception'
op|'.'
name|'FixedIpInvalid'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
nl|'\n'
dedent|''
name|'fixed_ip_info'
op|'='
op|'{'
string|'"fixed_ip"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'if'
name|'fixed_ip'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fixed IP %s has been deleted"'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'str'
op|'('
name|'fixed_ip'
op|'.'
name|'network'
op|'.'
name|'cidr'
op|')'
newline|'\n'
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'address'"
op|']'
op|'='
name|'str'
op|'('
name|'fixed_ip'
op|'.'
name|'address'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'fixed_ip'
op|'.'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'hostname'"
op|']'
op|'='
name|'fixed_ip'
op|'.'
name|'instance'
op|'.'
name|'hostname'
newline|'\n'
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'host'"
op|']'
op|'='
name|'fixed_ip'
op|'.'
name|'instance'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'hostname'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'host'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_fill_reserved_status'
op|'('
name|'req'
op|','
name|'fixed_ip'
op|','
name|'fixed_ip_info'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'fixed_ip_info'
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
number|'404'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'fixed_ips'
op|'.'
name|'reserve'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'reserve'"
op|')'
newline|'\n'
DECL|member|reserve
name|'def'
name|'reserve'
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
name|'return'
name|'self'
op|'.'
name|'_set_reserved'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'True'
op|')'
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
number|'404'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'fixed_ips'
op|'.'
name|'unreserve'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'unreserve'"
op|')'
newline|'\n'
DECL|member|unreserve
name|'def'
name|'unreserve'
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
name|'return'
name|'self'
op|'.'
name|'_set_reserved'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_reserved
dedent|''
name|'def'
name|'_set_reserved'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
name|'reserved'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'.'
name|'get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'fixed_ip'
op|'.'
name|'reserved'
op|'='
name|'reserved'
newline|'\n'
name|'fixed_ip'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFoundForAddress'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fixed IP %s not found"'
op|')'
op|'%'
name|'address'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'exception'
op|'.'
name|'FixedIpInvalid'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fixed IP %s not valid"'
op|')'
op|'%'
name|'address'
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
nl|'\n'
DECL|class|FixedIps
dedent|''
dedent|''
dedent|''
name|'class'
name|'FixedIps'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fixed IPs support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FixedIPs"'
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
name|'resources'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'FixedIPController'
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
name|'resources'
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
