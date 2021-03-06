begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
string|'"""The flavor access extension."""'
newline|'\n'
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
name|'api_version_request'
newline|'\n'
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
name|'flavor_access'
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
string|"'os-flavor-access'"
newline|'\n'
DECL|variable|soft_authorize
name|'soft_authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_soft_authorizer'
op|'('
name|'ALIAS'
op|')'
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
DECL|function|_marshall_flavor_access
name|'def'
name|'_marshall_flavor_access'
op|'('
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'rval'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'project_id'
name|'in'
name|'flavor'
op|'.'
name|'projects'
op|':'
newline|'\n'
indent|'        '
name|'rval'
op|'.'
name|'append'
op|'('
op|'{'
string|"'flavor_id'"
op|':'
name|'flavor'
op|'.'
name|'flavorid'
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
name|'project_id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'flavor_access'"
op|':'
name|'rval'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorAccessController
dedent|''
name|'class'
name|'FlavorAccessController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The flavor access API controller for the OpenStack API."""'
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
name|'super'
op|'('
name|'FlavorAccessController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
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
name|'flavor'
op|'='
name|'common'
op|'.'
name|'get_flavor'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# public flavor to all projects'
nl|'\n'
name|'if'
name|'flavor'
op|'.'
name|'is_public'
op|':'
newline|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Access list not available for public flavors."'
op|')'
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
name|'explanation'
op|')'
newline|'\n'
nl|'\n'
comment|'# private flavor to listed projects only'
nl|'\n'
dedent|''
name|'return'
name|'_marshall_flavor_access'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorActionController
dedent|''
dedent|''
name|'class'
name|'FlavorActionController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The flavor access API controller for the OpenStack API."""'
newline|'\n'
DECL|member|_extend_flavor
name|'def'
name|'_extend_flavor'
op|'('
name|'self'
op|','
name|'flavor_rval'
op|','
name|'flavor_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
string|'"%s:is_public"'
op|'%'
op|'('
name|'FlavorAccess'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'flavor_rval'
op|'['
name|'key'
op|']'
op|'='
name|'flavor_ref'
op|'['
string|"'is_public'"
op|']'
newline|'\n'
nl|'\n'
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
name|'soft_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db_flavor'
op|'='
name|'req'
op|'.'
name|'get_db_flavor'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_extend_flavor'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
op|']'
op|','
name|'db_flavor'
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
name|'soft_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'flavors'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'flavor_rval'
name|'in'
name|'flavors'
op|':'
newline|'\n'
indent|'                '
name|'db_flavor'
op|'='
name|'req'
op|'.'
name|'get_db_flavor'
op|'('
name|'flavor_rval'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_flavor'
op|'('
name|'flavor_rval'
op|','
name|'db_flavor'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
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
name|'body'
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
name|'soft_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db_flavor'
op|'='
name|'req'
op|'.'
name|'get_db_flavor'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_extend_flavor'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
op|']'
op|','
name|'db_flavor'
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
number|'403'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|'"addTenantAccess"'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'flavor_access'
op|'.'
name|'add_tenant_access'
op|')'
newline|'\n'
DECL|member|_add_tenant_access
name|'def'
name|'_add_tenant_access'
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
op|','
name|'action'
op|'='
string|'"add_tenant_access"'
op|')'
newline|'\n'
nl|'\n'
name|'vals'
op|'='
name|'body'
op|'['
string|"'addTenantAccess'"
op|']'
newline|'\n'
name|'tenant'
op|'='
name|'vals'
op|'['
string|"'tenant'"
op|']'
newline|'\n'
nl|'\n'
name|'flavor'
op|'='
name|'common'
op|'.'
name|'get_flavor'
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
name|'if'
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.7'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'flavor'
op|'.'
name|'is_public'
op|':'
newline|'\n'
indent|'                    '
name|'exp'
op|'='
name|'_'
op|'('
string|'"Can not add access to a public flavor."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'exp'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'flavor'
op|'.'
name|'add_access'
op|'('
name|'tenant'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
name|'as'
name|'e'
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
name|'FlavorAccessExists'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'err'
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
name|'AdminRequired'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
name|'return'
name|'_marshall_flavor_access'
op|'('
name|'flavor'
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
number|'400'
op|','
number|'403'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|'"removeTenantAccess"'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'flavor_access'
op|'.'
name|'remove_tenant_access'
op|')'
newline|'\n'
DECL|member|_remove_tenant_access
name|'def'
name|'_remove_tenant_access'
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
op|','
name|'action'
op|'='
string|'"remove_tenant_access"'
op|')'
newline|'\n'
nl|'\n'
name|'vals'
op|'='
name|'body'
op|'['
string|"'removeTenantAccess'"
op|']'
newline|'\n'
name|'tenant'
op|'='
name|'vals'
op|'['
string|"'tenant'"
op|']'
newline|'\n'
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'flavorid'
op|'='
name|'id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'.'
name|'remove_access'
op|'('
name|'tenant'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'FlavorAccessNotFound'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'FlavorNotFound'
op|')'
name|'as'
name|'e'
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
name|'AdminRequired'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
name|'return'
name|'_marshall_flavor_access'
op|'('
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorAccess
dedent|''
dedent|''
name|'class'
name|'FlavorAccess'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Flavor access support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FlavorAccess"'
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
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
name|'ALIAS'
op|','
nl|'\n'
name|'controller'
op|'='
name|'FlavorAccessController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
name|'member_name'
op|'='
string|"'flavor'"
op|','
name|'collection_name'
op|'='
string|"'flavors'"
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
string|"'flavors'"
op|','
name|'FlavorActionController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'extension'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
