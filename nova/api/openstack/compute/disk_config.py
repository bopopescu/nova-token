begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""Disk Config extension."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'schemas'
name|'import'
name|'disk_config'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-disk-config'"
newline|'\n'
DECL|variable|API_DISK_CONFIG
name|'API_DISK_CONFIG'
op|'='
string|'"OS-DCF:diskConfig"'
newline|'\n'
DECL|variable|INTERNAL_DISK_CONFIG
name|'INTERNAL_DISK_CONFIG'
op|'='
string|'"auto_disk_config"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_soft_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|disk_config_to_api
name|'def'
name|'disk_config_to_api'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'AUTO'"
name|'if'
name|'value'
name|'else'
string|"'MANUAL'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|disk_config_from_api
dedent|''
name|'def'
name|'disk_config_from_api'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'value'
op|'=='
string|"'AUTO'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'value'
op|'=='
string|"'MANUAL'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"%s must be either \'MANUAL\' or \'AUTO\'."'
op|')'
op|'%'
name|'API_DISK_CONFIG'
newline|'\n'
name|'raise'
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
DECL|class|ImageDiskConfigController
dedent|''
dedent|''
name|'class'
name|'ImageDiskConfigController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_add_disk_config
indent|'    '
name|'def'
name|'_add_disk_config'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'images'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'image'
name|'in'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'image'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
name|'if'
name|'INTERNAL_DISK_CONFIG'
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'                '
name|'raw_value'
op|'='
name|'metadata'
op|'['
name|'INTERNAL_DISK_CONFIG'
op|']'
newline|'\n'
name|'value'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'raw_value'
op|')'
newline|'\n'
name|'image'
op|'['
name|'API_DISK_CONFIG'
op|']'
op|'='
name|'disk_config_to_api'
op|'('
name|'value'
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
string|"'image'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
name|'and'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'image'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_add_disk_config'
op|'('
name|'context'
op|','
op|'['
name|'image'
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
string|"'images'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
name|'and'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'images'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'images'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_add_disk_config'
op|'('
name|'context'
op|','
name|'images'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerDiskConfigController
dedent|''
dedent|''
dedent|''
name|'class'
name|'ServerDiskConfigController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_add_disk_config
indent|'    '
name|'def'
name|'_add_disk_config'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'db_server'
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
comment|"# server['id'] is guaranteed to be in the cache due to"
nl|'\n'
comment|"# the core API adding it in its 'show'/'detail' methods."
nl|'\n'
name|'value'
op|'='
name|'db_server'
op|'.'
name|'get'
op|'('
name|'INTERNAL_DISK_CONFIG'
op|')'
newline|'\n'
name|'server'
op|'['
name|'API_DISK_CONFIG'
op|']'
op|'='
name|'disk_config_to_api'
op|'('
name|'value'
op|')'
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
name|'_add_disk_config'
op|'('
name|'req'
op|','
op|'['
name|'server'
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
string|"'servers'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
name|'and'
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
name|'self'
op|'.'
name|'_add_disk_config'
op|'('
name|'req'
op|','
name|'servers'
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
op|':'
newline|'\n'
indent|'            '
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
DECL|member|_action_rebuild
name|'def'
name|'_action_rebuild'
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
nl|'\n'
DECL|class|DiskConfig
dedent|''
dedent|''
dedent|''
name|'class'
name|'DiskConfig'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Disk Management Extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"DiskConfig"'
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
name|'servers_extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
string|"'servers'"
op|','
name|'ServerDiskConfigController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'images_extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
string|"'images'"
op|','
name|'ImageDiskConfigController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'servers_extension'
op|','
name|'images_extension'
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
name|'API_DISK_CONFIG'
name|'in'
name|'server_dict'
op|':'
newline|'\n'
indent|'            '
name|'api_value'
op|'='
name|'server_dict'
op|'['
name|'API_DISK_CONFIG'
op|']'
newline|'\n'
name|'internal_value'
op|'='
name|'disk_config_from_api'
op|'('
name|'api_value'
op|')'
newline|'\n'
name|'create_kwargs'
op|'['
name|'INTERNAL_DISK_CONFIG'
op|']'
op|'='
name|'internal_value'
newline|'\n'
nl|'\n'
DECL|variable|server_update
dedent|''
dedent|''
name|'server_update'
op|'='
name|'server_create'
newline|'\n'
DECL|variable|server_rebuild
name|'server_rebuild'
op|'='
name|'server_create'
newline|'\n'
DECL|variable|server_resize
name|'server_resize'
op|'='
name|'server_create'
newline|'\n'
nl|'\n'
DECL|member|get_server_create_schema
name|'def'
name|'get_server_create_schema'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'disk_config'
op|'.'
name|'server_create'
newline|'\n'
nl|'\n'
DECL|variable|get_server_update_schema
dedent|''
name|'get_server_update_schema'
op|'='
name|'get_server_create_schema'
newline|'\n'
DECL|variable|get_server_rebuild_schema
name|'get_server_rebuild_schema'
op|'='
name|'get_server_create_schema'
newline|'\n'
DECL|variable|get_server_resize_schema
name|'get_server_resize_schema'
op|'='
name|'get_server_create_schema'
newline|'\n'
dedent|''
endmarker|''
end_unit
