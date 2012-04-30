begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack LLC.'
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
string|'"""The volume types extra specs extension"""'
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
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'volume_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'volume'"
op|','
string|"'types_extra_specs'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeTypeExtraSpecsTemplate
name|'class'
name|'VolumeTypeExtraSpecsTemplate'
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
name|'make_flat_dict'
op|'('
string|"'extra_specs'"
op|','
name|'selector'
op|'='
string|"'extra_specs'"
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
DECL|class|VolumeTypeExtraSpecTemplate
dedent|''
dedent|''
name|'class'
name|'VolumeTypeExtraSpecTemplate'
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
name|'tagname'
op|'='
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
string|"'key'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|extraspec_sel
name|'def'
name|'extraspec_sel'
op|'('
name|'obj'
op|','
name|'do_raise'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# Have to extract the key and value for later use...'
nl|'\n'
indent|'            '
name|'key'
op|','
name|'value'
op|'='
name|'obj'
op|'.'
name|'items'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'key'
op|'='
name|'key'
op|','
name|'value'
op|'='
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
name|'tagname'
op|','
name|'selector'
op|'='
name|'extraspec_sel'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'text'
op|'='
string|"'value'"
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
DECL|class|VolumeTypeExtraSpecsController
dedent|''
dedent|''
name|'class'
name|'VolumeTypeExtraSpecsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" The volume type extra specs API controller for the OpenStack API """'
newline|'\n'
nl|'\n'
DECL|member|_get_extra_specs
name|'def'
name|'_get_extra_specs'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'type_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'extra_specs'
op|'='
name|'db'
op|'.'
name|'volume_type_extra_specs_get'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
name|'specs_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'extra_specs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'specs_dict'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'extra_specs'
op|'='
name|'specs_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_body
dedent|''
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
name|'not'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'No Request Body'"
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
nl|'\n'
DECL|member|_check_type
dedent|''
dedent|''
name|'def'
name|'_check_type'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'type_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_types'
op|'.'
name|'get_volume_type'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
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
name|'unicode'
op|'('
name|'ex'
op|')'
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
name|'VolumeTypeExtraSpecsTemplate'
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
name|'type_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Returns the list of extra specs for a given volume type """'
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
name|'self'
op|'.'
name|'_check_type'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_extra_specs'
op|'('
name|'context'
op|','
name|'type_id'
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
name|'VolumeTypeExtraSpecsTemplate'
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
name|'type_id'
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
name|'self'
op|'.'
name|'_check_type'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_body'
op|'('
name|'body'
op|')'
newline|'\n'
name|'specs'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'specs'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Malformed extra specs'"
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
name|'db'
op|'.'
name|'volume_type_extra_specs_update_or_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'type_id'
op|','
nl|'\n'
name|'specs'
op|')'
newline|'\n'
name|'return'
name|'body'
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
name|'VolumeTypeExtraSpecTemplate'
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
name|'type_id'
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
name|'_check_type'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_body'
op|'('
name|'body'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'id'
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
name|'if'
name|'len'
op|'('
name|'body'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Request body contains too many items'"
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
name|'db'
op|'.'
name|'volume_type_extra_specs_update_or_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'type_id'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
name|'return'
name|'body'
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
name|'VolumeTypeExtraSpecTemplate'
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
name|'type_id'
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_type'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
name|'specs'
op|'='
name|'self'
op|'.'
name|'_get_extra_specs'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
name|'if'
name|'id'
name|'in'
name|'specs'
op|'['
string|"'extra_specs'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
name|'id'
op|':'
name|'specs'
op|'['
string|"'extra_specs'"
op|']'
op|'['
name|'id'
op|']'
op|'}'
newline|'\n'
dedent|''
name|'else'
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
DECL|member|delete
dedent|''
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'type_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Deletes an existing extra spec """'
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
name|'self'
op|'.'
name|'_check_type'
op|'('
name|'context'
op|','
name|'type_id'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_type_extra_specs_delete'
op|'('
name|'context'
op|','
name|'type_id'
op|','
name|'id'
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
nl|'\n'
DECL|class|Types_extra_specs
dedent|''
dedent|''
name|'class'
name|'Types_extra_specs'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Types extra specs support"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"TypesExtraSpecs"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-types-extra-specs"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/volume/ext/types-extra-specs/api/v1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-08-24T00:00:00+00:00"'
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
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'extra_specs'"
op|','
nl|'\n'
name|'VolumeTypeExtraSpecsController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'member_name'
op|'='
string|"'type'"
op|','
nl|'\n'
name|'collection_name'
op|'='
string|"'types'"
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
dedent|''
dedent|''
endmarker|''
end_unit
