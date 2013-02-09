begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
string|"'flavor_access'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_flavor
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
string|"'{%s}is_public'"
op|'%'
name|'Flavor_access'
op|'.'
name|'namespace'
op|','
nl|'\n'
string|"'%s:is_public'"
op|'%'
name|'Flavor_access'
op|'.'
name|'alias'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_flavor_access
dedent|''
name|'def'
name|'make_flavor_access'
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
string|"'flavor_id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'tenant_id'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorTemplate
dedent|''
name|'class'
name|'FlavorTemplate'
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
name|'Flavor_access'
op|'.'
name|'alias'
newline|'\n'
name|'namespace'
op|'='
name|'Flavor_access'
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
DECL|class|FlavorsTemplate
dedent|''
dedent|''
name|'class'
name|'FlavorsTemplate'
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
name|'Flavor_access'
op|'.'
name|'alias'
newline|'\n'
name|'namespace'
op|'='
name|'Flavor_access'
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
DECL|class|FlavorAccessTemplate
dedent|''
dedent|''
name|'class'
name|'FlavorAccessTemplate'
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
string|"'flavor_access'"
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
string|"'access'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'flavor_access'"
op|')'
newline|'\n'
name|'make_flavor_access'
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
DECL|function|_marshall_flavor_access
dedent|''
dedent|''
name|'def'
name|'_marshall_flavor_access'
op|'('
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'rval'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'access_list'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_access_by_flavor_id'
op|'('
name|'flavor_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
op|':'
newline|'\n'
indent|'        '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Flavor not found."'
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
dedent|''
name|'for'
name|'access'
name|'in'
name|'access_list'
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
name|'flavor_id'
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
name|'access'
op|'['
string|"'project_id'"
op|']'
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
name|'object'
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
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'FlavorAccessTemplate'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_flavor_id'
op|'('
name|'flavor_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
op|':'
newline|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Flavor not found."'
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
comment|'# public flavor to all projects'
nl|'\n'
dedent|''
name|'if'
name|'flavor'
op|'['
string|"'is_public'"
op|']'
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
name|'flavor_id'
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
nl|'\n'
DECL|member|_check_body
name|'def'
name|'_check_body'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'body'
name|'is'
name|'None'
name|'or'
name|'body'
op|'=='
string|'""'
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
name|'_'
op|'('
string|'"No request body"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flavor_refs
dedent|''
dedent|''
name|'def'
name|'_get_flavor_refs'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a dictionary mapping flavorid to flavor_ref."""'
newline|'\n'
nl|'\n'
name|'flavor_refs'
op|'='
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
name|'context'
op|')'
newline|'\n'
name|'rval'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'name'
op|','
name|'obj'
name|'in'
name|'flavor_refs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rval'
op|'['
name|'obj'
op|'['
string|"'flavorid'"
op|']'
op|']'
op|'='
name|'obj'
newline|'\n'
dedent|''
name|'return'
name|'rval'
newline|'\n'
nl|'\n'
DECL|member|_extend_flavor
dedent|''
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
name|'Flavor_access'
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
name|'FlavorTemplate'
op|'('
op|')'
op|')'
newline|'\n'
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
name|'FlavorsTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'FlavorTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'FlavorAccessTemplate'
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
DECL|member|_addTenantAccess
name|'def'
name|'_addTenantAccess'
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
name|'self'
op|'.'
name|'_check_body'
op|'('
name|'body'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance_types'
op|'.'
name|'add_instance_type_access'
op|'('
name|'id'
op|','
name|'tenant'
op|','
name|'context'
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
name|'str'
op|'('
name|'err'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_marshall_flavor_access'
op|'('
name|'id'
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
name|'FlavorAccessTemplate'
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
DECL|member|_removeTenantAccess
name|'def'
name|'_removeTenantAccess'
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
name|'self'
op|'.'
name|'_check_body'
op|'('
name|'body'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance_types'
op|'.'
name|'remove_instance_type_access'
op|'('
name|'id'
op|','
name|'tenant'
op|','
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorAccessNotFound'
op|','
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
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_marshall_flavor_access'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Flavor_access
dedent|''
dedent|''
name|'class'
name|'Flavor_access'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
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
string|'"os-flavor-access"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"flavor_access/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-08-01T00:00:00+00:00"'
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
nl|'\n'
string|"'os-flavor-access'"
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
