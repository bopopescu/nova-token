begin_unit
comment|'#   Copyright 2012 Openstack, LLC.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
string|'"""The Extended Server Attributes API extension."""'
newline|'\n'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
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
string|'"nova.api.openstack.compute.contrib."'
nl|'\n'
string|'"extended_server_attributes"'
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
nl|'\n'
string|"'extended_server_attributes'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedServerAttributesController
name|'class'
name|'ExtendedServerAttributesController'
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
name|'ExtendedServerAttributesController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
nl|'\n'
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
nl|'\n'
DECL|member|_get_instances
dedent|''
name|'def'
name|'_get_instances'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuids'
op|'}'
newline|'\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
name|'filters'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'instance'
op|')'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extend_server
dedent|''
name|'def'
name|'_extend_server'
op|'('
name|'self'
op|','
name|'server'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'attr'
name|'in'
op|'['
string|"'host'"
op|','
string|"'name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'attr'
op|'=='
string|"'name'"
op|':'
newline|'\n'
indent|'                '
name|'key'
op|'='
string|'"%s:instance_%s"'
op|'%'
op|'('
name|'Extended_server_attributes'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'key'
op|'='
string|'"%s:%s"'
op|'%'
op|'('
name|'Extended_server_attributes'
op|'.'
name|'alias'
op|','
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'['
name|'key'
op|']'
op|'='
name|'instance'
op|'['
name|'attr'
op|']'
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
comment|'# Attach our slave template to the response object'
nl|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ExtendedServerAttributesTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
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
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Server not found."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'explanation'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|','
name|'instance'
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
comment|'# Attach our slave template to the response object'
nl|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ExtendedServerAttributesTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'servers'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'instance_uuids'
op|'='
op|'['
name|'server'
op|'['
string|"'id'"
op|']'
name|'for'
name|'server'
name|'in'
name|'servers'
op|']'
newline|'\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'_get_instances'
op|'('
name|'context'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'server_object'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'instance_data'
op|'='
name|'instances'
op|'['
name|'server_object'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|'# Ignore missing instance data'
nl|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'server_object'
op|','
name|'instance_data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Extended_server_attributes
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Extended_server_attributes'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extended Server Attributes support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ExtendedServerAttributes"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"OS-EXT-SRV-ATTR"'
newline|'\n'
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/"'
DECL|variable|namespace
string|'"extended_status/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-11-03T00:00:00+00:00"'
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
name|'ExtendedServerAttributesController'
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
nl|'\n'
nl|'\n'
DECL|function|make_server
dedent|''
dedent|''
name|'def'
name|'make_server'
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
string|"'{%s}instance_name'"
op|'%'
name|'Extended_server_attributes'
op|'.'
name|'namespace'
op|','
nl|'\n'
string|"'%s:instance_name'"
op|'%'
name|'Extended_server_attributes'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'{%s}host'"
op|'%'
name|'Extended_server_attributes'
op|'.'
name|'namespace'
op|','
nl|'\n'
string|"'%s:host'"
op|'%'
name|'Extended_server_attributes'
op|'.'
name|'alias'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedServerAttributeTemplate
dedent|''
name|'class'
name|'ExtendedServerAttributeTemplate'
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
string|"'server'"
op|','
name|'selector'
op|'='
string|"'server'"
op|')'
newline|'\n'
name|'make_server'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
nl|'\n'
name|'Extended_server_attributes'
op|'.'
name|'alias'
op|':'
name|'Extended_server_attributes'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedServerAttributesTemplate
dedent|''
dedent|''
name|'class'
name|'ExtendedServerAttributesTemplate'
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
string|"'servers'"
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
string|"'server'"
op|','
name|'selector'
op|'='
string|"'servers'"
op|')'
newline|'\n'
name|'make_server'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
nl|'\n'
name|'Extended_server_attributes'
op|'.'
name|'alias'
op|':'
name|'Extended_server_attributes'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
