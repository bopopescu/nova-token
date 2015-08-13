begin_unit
comment|'# Copyright 2010 OpenStack Foundation'
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
name|'six'
newline|'\n'
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
name|'flavors_extraspecs'
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
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-flavor-extra-specs'"
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
DECL|class|FlavorExtraSpecsController
name|'class'
name|'FlavorExtraSpecsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The flavor extra specs API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'FlavorExtraSpecsController'
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
nl|'\n'
DECL|member|_get_extra_specs
dedent|''
name|'def'
name|'_get_extra_specs'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'return'
name|'dict'
op|'('
name|'extra_specs'
op|'='
name|'flavor'
op|'.'
name|'extra_specs'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(gmann): Max length for numeric value is being checked'
nl|'\n'
comment|'# explicitly as json schema cannot have max length check for numeric value'
nl|'\n'
DECL|member|_check_extra_specs_value
dedent|''
name|'def'
name|'_check_extra_specs_value'
op|'('
name|'self'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
op|'('
name|'six'
op|'.'
name|'integer_types'
op|','
name|'float'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'value'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'value'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'value'
op|','
string|"'extra_specs value'"
op|','
nl|'\n'
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'error'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
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
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of extra specs for a given flavor."""'
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
op|','
name|'action'
op|'='
string|"'index'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(gmann): Here should be 201 instead of 200 by v2.1'
nl|'\n'
comment|'# +microversions because the flavor extra specs has been created'
nl|'\n'
comment|'# completely when returning a response.'
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
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'flavors_extraspecs'
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
name|'flavor_id'
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
string|"'create'"
op|')'
newline|'\n'
nl|'\n'
name|'specs'
op|'='
name|'body'
op|'['
string|"'extra_specs'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_check_extra_specs_value'
op|'('
name|'specs'
op|')'
newline|'\n'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'.'
name|'extra_specs'
op|'='
name|'dict'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|','
op|'**'
name|'specs'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorExtraSpecUpdateCreateFailed'
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
name|'return'
name|'body'
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
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'flavors_extraspecs'
op|'.'
name|'update'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
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
string|"'update'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_check_extra_specs_value'
op|'('
name|'body'
op|')'
newline|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Request body and URI mismatch'"
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
name|'expl'
op|')'
newline|'\n'
dedent|''
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'.'
name|'extra_specs'
op|'='
name|'dict'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|','
op|'**'
name|'body'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorExtraSpecUpdateCreateFailed'
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
name|'return'
name|'body'
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
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a single extra spec item."""'
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
op|','
name|'action'
op|'='
string|"'show'"
op|')'
newline|'\n'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
name|'id'
op|':'
name|'flavor'
op|'.'
name|'extra_specs'
op|'['
name|'id'
op|']'
op|'}'
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
string|'"Flavor %(flavor_id)s has no extra specs with "'
nl|'\n'
string|'"key %(key)s."'
op|')'
op|'%'
name|'dict'
op|'('
name|'flavor_id'
op|'='
name|'flavor_id'
op|','
nl|'\n'
name|'key'
op|'='
name|'id'
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
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(gmann): Here should be 204(No Content) instead of 200 by v2.1'
nl|'\n'
comment|'# +microversions because the flavor extra specs has been deleted'
nl|'\n'
comment|'# completely when returning a response.'
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
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes an existing extra spec."""'
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
op|','
name|'action'
op|'='
string|"'delete'"
op|')'
newline|'\n'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'flavor'
op|'.'
name|'extra_specs'
op|'['
name|'id'
op|']'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'FlavorExtraSpecsNotFound'
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
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Flavor %(flavor_id)s has no extra specs with "'
nl|'\n'
string|'"key %(key)s."'
op|')'
op|'%'
name|'dict'
op|'('
name|'flavor_id'
op|'='
name|'flavor_id'
op|','
nl|'\n'
name|'key'
op|'='
name|'id'
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
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsExtraSpecs
dedent|''
dedent|''
dedent|''
name|'class'
name|'FlavorsExtraSpecs'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Flavors extra specs support."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|"'FlavorExtraSpecs'"
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
name|'extra_specs'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'os-extra_specs'"
op|','
nl|'\n'
name|'FlavorExtraSpecsController'
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
name|'extra_specs'
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
