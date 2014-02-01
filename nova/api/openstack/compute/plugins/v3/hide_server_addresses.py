begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
string|'"""Extension for hiding server addresses in certain states."""'
newline|'\n'
nl|'\n'
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
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'osapi_hide_server_address_states'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
name|'vm_states'
op|'.'
name|'BUILDING'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'List of instance states that should hide network info'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-hide-server-addresses'"
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
DECL|class|Controller
name|'class'
name|'Controller'
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
name|'Controller'
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
name|'hidden_states'
op|'='
name|'CONF'
op|'.'
name|'osapi_hide_server_address_states'
newline|'\n'
nl|'\n'
comment|'# NOTE(jkoelker) _ is not considered uppercase ;)'
nl|'\n'
name|'valid_vm_states'
op|'='
op|'['
name|'getattr'
op|'('
name|'vm_states'
op|','
name|'state'
op|')'
nl|'\n'
name|'for'
name|'state'
name|'in'
name|'dir'
op|'('
name|'vm_states'
op|')'
nl|'\n'
name|'if'
name|'state'
op|'.'
name|'isupper'
op|'('
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'hide_address_states'
op|'='
op|'['
name|'state'
op|'.'
name|'lower'
op|'('
op|')'
nl|'\n'
name|'for'
name|'state'
name|'in'
name|'hidden_states'
nl|'\n'
name|'if'
name|'state'
name|'in'
name|'valid_vm_states'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_perhaps_hide_addresses
dedent|''
name|'def'
name|'_perhaps_hide_addresses'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'resp_server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'vm_state'"
op|')'
name|'in'
name|'self'
op|'.'
name|'hide_address_states'
op|':'
newline|'\n'
indent|'            '
name|'resp_server'
op|'['
string|"'addresses'"
op|']'
op|'='
op|'{'
op|'}'
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
name|'resp'
op|'='
name|'resp_obj'
newline|'\n'
name|'if'
name|'not'
name|'authorize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'server'"
name|'in'
name|'resp'
op|'.'
name|'obj'
name|'and'
string|"'addresses'"
name|'in'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_perhaps_hide_addresses'
op|'('
name|'instance'
op|','
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
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
name|'resp'
op|'='
name|'resp_obj'
newline|'\n'
name|'if'
name|'not'
name|'authorize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'server'
name|'in'
name|'list'
op|'('
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'addresses'"
name|'in'
name|'server'
op|':'
newline|'\n'
indent|'                '
name|'instance'
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
name|'self'
op|'.'
name|'_perhaps_hide_addresses'
op|'('
name|'instance'
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HideServerAddresses
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'HideServerAddresses'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Support hiding server addresses in certain states."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|"'HideServerAddresses'"
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
DECL|member|get_controller_extensions
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
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'servers'"
op|','
name|'Controller'
op|'('
op|')'
op|')'
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
dedent|''
dedent|''
endmarker|''
end_unit
