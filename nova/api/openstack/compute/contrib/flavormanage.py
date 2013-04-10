begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
op|'.'
name|'compute'
name|'import'
name|'flavors'
name|'as'
name|'flavors_api'
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
name|'views'
name|'import'
name|'flavors'
name|'as'
name|'flavors_view'
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
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'flavormanage'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorManageController
name|'class'
name|'FlavorManageController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The Flavor Lifecycle API controller for the OpenStack API.\n    """'
newline|'\n'
DECL|variable|_view_builder_class
name|'_view_builder_class'
op|'='
name|'flavors_view'
op|'.'
name|'ViewBuilder'
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
name|'FlavorManageController'
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
name|'action'
op|'('
string|'"delete"'
op|')'
newline|'\n'
DECL|member|_delete
name|'def'
name|'_delete'
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
nl|'\n'
name|'id'
op|','
name|'read_deleted'
op|'='
string|'"no"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_types'
op|'.'
name|'destroy'
op|'('
name|'flavor'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
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
string|'"create"'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'flavors_api'
op|'.'
name|'FlavorTemplate'
op|')'
newline|'\n'
DECL|member|_create
name|'def'
name|'_create'
op|'('
name|'self'
op|','
name|'req'
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
name|'vals'
op|'='
name|'body'
op|'['
string|"'flavor'"
op|']'
newline|'\n'
name|'name'
op|'='
name|'vals'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'flavorid'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'memory_mb'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'ram'"
op|')'
newline|'\n'
name|'vcpus'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'vcpus'"
op|')'
newline|'\n'
name|'root_gb'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'disk'"
op|')'
newline|'\n'
name|'ephemeral_gb'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'OS-FLV-EXT-DATA:ephemeral'"
op|')'
newline|'\n'
name|'swap'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'swap'"
op|')'
newline|'\n'
name|'rxtx_factor'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'rxtx_factor'"
op|')'
newline|'\n'
name|'is_public'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'os-flavor-access:is_public'"
op|','
name|'True'
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
name|'create'
op|'('
name|'name'
op|','
name|'memory_mb'
op|','
name|'vcpus'
op|','
nl|'\n'
name|'root_gb'
op|','
name|'ephemeral_gb'
op|','
name|'flavorid'
op|','
nl|'\n'
name|'swap'
op|','
name|'rxtx_factor'
op|','
name|'is_public'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_flavor'
op|'('
name|'flavor'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'InstanceTypeExists'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InstanceTypeIdExists'
op|')'
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
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Flavormanage
dedent|''
dedent|''
name|'class'
name|'Flavormanage'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Flavor create/delete API support\n    """'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FlavorManage"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-flavor-manage"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"flavor_manage/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-01-19T00:00:00+00:00"'
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
name|'FlavorManageController'
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
dedent|''
dedent|''
endmarker|''
end_unit
