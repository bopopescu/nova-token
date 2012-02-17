begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
comment|'#    under the License'
nl|'\n'
nl|'\n'
string|'"""Disk Config extension."""'
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
name|'db'
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
string|"'OS-DCF'"
newline|'\n'
DECL|variable|XMLNS_DCF
name|'XMLNS_DCF'
op|'='
string|'"http://docs.openstack.org/compute/ext/disk_config/api/v1.1"'
newline|'\n'
DECL|variable|API_DISK_CONFIG
name|'API_DISK_CONFIG'
op|'='
string|'"%s:diskConfig"'
op|'%'
name|'ALIAS'
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
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'disk_config'"
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
op|'%'
name|'API_DISK_CONFIG'
op|')'
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
DECL|class|ImageDiskConfigTemplate
dedent|''
dedent|''
name|'class'
name|'ImageDiskConfigTemplate'
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
string|"'image'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
name|'API_DISK_CONFIG'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesDiskConfigTemplate
dedent|''
dedent|''
name|'class'
name|'ImagesDiskConfigTemplate'
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
string|"'images'"
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
string|"'image'"
op|','
name|'selector'
op|'='
string|"'images'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
name|'API_DISK_CONFIG'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
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
name|'utils'
op|'.'
name|'bool_from_str'
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
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ImageDiskConfigTemplate'
op|'('
op|')'
op|')'
newline|'\n'
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
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ImagesDiskConfigTemplate'
op|'('
op|')'
op|')'
newline|'\n'
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
DECL|class|ServerDiskConfigTemplate
dedent|''
dedent|''
dedent|''
name|'class'
name|'ServerDiskConfigTemplate'
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
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
name|'API_DISK_CONFIG'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersDiskConfigTemplate
dedent|''
dedent|''
name|'class'
name|'ServersDiskConfigTemplate'
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
name|'elem'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
name|'API_DISK_CONFIG'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerDiskConfigController
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
name|'context'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
comment|'# Get DB information for servers'
nl|'\n'
indent|'        '
name|'uuids'
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
name|'db_servers'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
name|'uuids'
op|'}'
op|')'
newline|'\n'
name|'db_servers_by_uuid'
op|'='
name|'dict'
op|'('
op|'('
name|'s'
op|'['
string|"'uuid'"
op|']'
op|','
name|'s'
op|')'
name|'for'
name|'s'
name|'in'
name|'db_servers'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'db_server'
op|'='
name|'db_servers_by_uuid'
op|'.'
name|'get'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'db_server'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'db_server'
op|'['
name|'INTERNAL_DISK_CONFIG'
op|']'
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
dedent|''
name|'def'
name|'_show'
op|'('
name|'self'
op|','
name|'context'
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
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ServerDiskConfigTemplate'
op|'('
op|')'
op|')'
newline|'\n'
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
name|'context'
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
name|'context'
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
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ServersDiskConfigTemplate'
op|'('
op|')'
op|')'
newline|'\n'
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
name|'context'
op|','
name|'servers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_disk_config
dedent|''
dedent|''
name|'def'
name|'_set_disk_config'
op|'('
name|'self'
op|','
name|'dict_'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'API_DISK_CONFIG'
name|'in'
name|'dict_'
op|':'
newline|'\n'
indent|'            '
name|'api_value'
op|'='
name|'dict_'
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
name|'dict_'
op|'['
name|'INTERNAL_DISK_CONFIG'
op|']'
op|'='
name|'internal_value'
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
name|'_set_disk_config'
op|'('
name|'body'
op|'['
string|"'server'"
op|']'
op|')'
newline|'\n'
name|'resp_obj'
op|'='
op|'('
name|'yield'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_show'
op|'('
name|'context'
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
name|'_set_disk_config'
op|'('
name|'body'
op|'['
string|"'server'"
op|']'
op|')'
newline|'\n'
name|'resp_obj'
op|'='
op|'('
name|'yield'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_show'
op|'('
name|'context'
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
name|'_set_disk_config'
op|'('
name|'body'
op|'['
string|"'rebuild'"
op|']'
op|')'
newline|'\n'
name|'resp_obj'
op|'='
op|'('
name|'yield'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_show'
op|'('
name|'context'
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
string|"'resize'"
op|')'
newline|'\n'
DECL|member|_action_resize
name|'def'
name|'_action_resize'
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
name|'_set_disk_config'
op|'('
name|'body'
op|'['
string|"'resize'"
op|']'
op|')'
newline|'\n'
name|'yield'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Disk_config
dedent|''
dedent|''
dedent|''
name|'class'
name|'Disk_config'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Disk Management Extension"""'
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
DECL|variable|namespace
name|'namespace'
op|'='
name|'XMLNS_DCF'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-09-27T00:00:00+00:00"'
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
dedent|''
dedent|''
endmarker|''
end_unit
