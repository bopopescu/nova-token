begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-access-ips"'
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
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccessIPsController
name|'class'
name|'AccessIPsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_extend_server
indent|'    '
name|'def'
name|'_extend_server'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db_instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'ip_v4'
op|'='
name|'db_instance'
op|'.'
name|'get'
op|'('
string|"'access_ip_v4'"
op|')'
newline|'\n'
name|'ip_v6'
op|'='
name|'db_instance'
op|'.'
name|'get'
op|'('
string|"'access_ip_v6'"
op|')'
newline|'\n'
name|'server'
op|'['
string|"'%s:access_ip_v4'"
op|'%'
name|'ALIAS'
op|']'
op|'='
op|'('
nl|'\n'
name|'str'
op|'('
name|'ip_v4'
op|')'
name|'if'
name|'ip_v4'
name|'is'
name|'not'
name|'None'
name|'else'
string|"''"
op|')'
newline|'\n'
name|'server'
op|'['
string|"'%s:access_ip_v6'"
op|'%'
name|'ALIAS'
op|']'
op|'='
op|'('
nl|'\n'
name|'str'
op|'('
name|'ip_v6'
op|')'
name|'if'
name|'ip_v6'
name|'is'
name|'not'
name|'None'
name|'else'
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
name|'and'
string|"'server'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'req'
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'req'
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'req'
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
op|'('
name|'action'
op|'='
string|"'rebuild'"
op|')'
newline|'\n'
DECL|member|rebuild
name|'def'
name|'rebuild'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'req'
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'servers'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'req'
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccessIPs
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'AccessIPs'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Access IPs support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"AccessIPs"'
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
DECL|variable|v4_key
name|'v4_key'
op|'='
string|"'%s:access_ip_v4'"
op|'%'
name|'ALIAS'
newline|'\n'
DECL|variable|v6_key
name|'v6_key'
op|'='
string|"'%s:access_ip_v6'"
op|'%'
name|'ALIAS'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
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
name|'AccessIPsController'
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
nl|'\n'
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'extension'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
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
nl|'\n'
comment|"# NOTE(gmann): This function is not supposed to use 'body_deprecated_param'"
nl|'\n'
comment|'# parameter as this is placed to handle scheduler_hint extension for V2.1.'
nl|'\n'
comment|"# making 'body_deprecated_param' as optional to avoid changes for"
nl|'\n'
comment|'# server_update & server_rebuild'
nl|'\n'
DECL|member|server_create
dedent|''
name|'def'
name|'server_create'
op|'('
name|'self'
op|','
name|'server_dict'
op|','
name|'create_kwargs'
op|','
nl|'\n'
name|'body_deprecated_param'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'AccessIPs'
op|'.'
name|'v4_key'
name|'in'
name|'server_dict'
op|':'
newline|'\n'
indent|'            '
name|'access_ip_v4'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'AccessIPs'
op|'.'
name|'v4_key'
op|')'
newline|'\n'
name|'if'
name|'access_ip_v4'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_validate_access_ipv4'
op|'('
name|'access_ip_v4'
op|')'
newline|'\n'
name|'create_kwargs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
name|'access_ip_v4'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'create_kwargs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'AccessIPs'
op|'.'
name|'v6_key'
name|'in'
name|'server_dict'
op|':'
newline|'\n'
indent|'            '
name|'access_ip_v6'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'AccessIPs'
op|'.'
name|'v6_key'
op|')'
newline|'\n'
name|'if'
name|'access_ip_v6'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_validate_access_ipv6'
op|'('
name|'access_ip_v6'
op|')'
newline|'\n'
name|'create_kwargs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
name|'access_ip_v6'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'create_kwargs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|server_update
dedent|''
dedent|''
dedent|''
name|'server_update'
op|'='
name|'server_create'
newline|'\n'
nl|'\n'
DECL|variable|server_rebuild
name|'server_rebuild'
op|'='
name|'server_create'
newline|'\n'
nl|'\n'
DECL|member|_validate_access_ipv4
name|'def'
name|'_validate_access_ipv4'
op|'('
name|'self'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'utils'
op|'.'
name|'is_valid_ipv4'
op|'('
name|'address'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'access_ip_v4 is not proper IPv4 format'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_access_ipv6
dedent|''
dedent|''
name|'def'
name|'_validate_access_ipv6'
op|'('
name|'self'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'utils'
op|'.'
name|'is_valid_ipv6'
op|'('
name|'address'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'access_ip_v6 is not proper IPv6 format'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
