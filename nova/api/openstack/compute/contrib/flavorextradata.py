begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack, LLC'
nl|'\n'
comment|'# Copyright 2011 Canonical Ltd.'
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
string|'"""The Flavor extra data extension\n\nOpenStack API version 1.1 lists "name", "ram", "disk", "vcpus" as flavor\nattributes.  This extension adds to that list:\n\n- OS-FLV-EXT-DATA:ephemeral\n"""'
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
nl|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'flavorextradata'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorextradataController
name|'class'
name|'FlavorextradataController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_extend_flavors
indent|'    '
name|'def'
name|'_extend_flavors'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavors'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'flavor'
name|'in'
name|'flavors'
op|':'
newline|'\n'
indent|'            '
name|'db_flavor'
op|'='
name|'req'
op|'.'
name|'get_db_flavor'
op|'('
name|'flavor'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'key'
op|'='
string|'"%s:ephemeral"'
op|'%'
name|'Flavorextradata'
op|'.'
name|'alias'
newline|'\n'
name|'flavor'
op|'['
name|'key'
op|']'
op|'='
name|'db_flavor'
op|'['
string|"'ephemeral_gb'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_show
dedent|''
dedent|''
name|'def'
name|'_show'
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
dedent|''
name|'if'
string|"'flavor'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
op|':'
newline|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'FlavorextradatumTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_flavors'
op|'('
name|'req'
op|','
op|'['
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
op|']'
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
name|'return'
name|'self'
op|'.'
name|'_show'
op|'('
name|'req'
op|','
name|'resp_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
op|'('
name|'action'
op|'='
string|"'create'"
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
name|'resp_obj'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_show'
op|'('
name|'req'
op|','
name|'resp_obj'
op|')'
newline|'\n'
nl|'\n'
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
dedent|''
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'FlavorextradataTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_flavors'
op|'('
name|'req'
op|','
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'flavors'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Flavorextradata
dedent|''
dedent|''
name|'class'
name|'Flavorextradata'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provide additional data for flavors."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FlavorExtraData"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"OS-FLV-EXT-DATA"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"flavor_extra_data/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-09-14T00:00:00+00:00"'
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
name|'FlavorextradataController'
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
string|"'flavors'"
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
DECL|function|make_flavor
dedent|''
dedent|''
name|'def'
name|'make_flavor'
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
string|"'{%s}ephemeral'"
op|'%'
name|'Flavorextradata'
op|'.'
name|'namespace'
op|','
nl|'\n'
string|"'%s:ephemeral'"
op|'%'
name|'Flavorextradata'
op|'.'
name|'alias'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorextradatumTemplate
dedent|''
name|'class'
name|'FlavorextradatumTemplate'
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
string|"'flavor'"
op|','
name|'selector'
op|'='
string|"'flavor'"
op|')'
newline|'\n'
name|'make_flavor'
op|'('
name|'root'
op|')'
newline|'\n'
name|'alias'
op|'='
name|'Flavorextradata'
op|'.'
name|'alias'
newline|'\n'
name|'namespace'
op|'='
name|'Flavorextradata'
op|'.'
name|'namespace'
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
name|'alias'
op|':'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorextradataTemplate
dedent|''
dedent|''
name|'class'
name|'FlavorextradataTemplate'
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
string|"'flavors'"
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
string|"'flavor'"
op|','
name|'selector'
op|'='
string|"'flavors'"
op|')'
newline|'\n'
name|'make_flavor'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'alias'
op|'='
name|'Flavorextradata'
op|'.'
name|'alias'
newline|'\n'
name|'namespace'
op|'='
name|'Flavorextradata'
op|'.'
name|'namespace'
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
name|'alias'
op|':'
name|'namespace'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
