begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack LLC.'
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
string|'"""Config Drive extension"""'
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
name|'servers'
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
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'config_drive'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerConfigDriveTemplate
name|'class'
name|'ServerConfigDriveTemplate'
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
string|"'config_drive'"
op|','
string|"'config_drive'"
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersConfigDriveTemplate
dedent|''
dedent|''
name|'class'
name|'ServersConfigDriveTemplate'
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
string|"'config_drive'"
op|','
string|"'config_drive'"
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
dedent|''
name|'class'
name|'Controller'
op|'('
name|'servers'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_add_config_drive
indent|'    '
name|'def'
name|'_add_config_drive'
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
name|'server'
op|'['
string|"'config_drive'"
op|']'
op|'='
name|'db_server'
op|'['
string|"'config_drive'"
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
name|'ServerConfigDriveTemplate'
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
name|'_add_config_drive'
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
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ServersConfigDriveTemplate'
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
name|'_add_config_drive'
op|'('
name|'req'
op|','
name|'servers'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Config_drive
dedent|''
dedent|''
dedent|''
name|'class'
name|'Config_drive'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Config Drive Extension"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ConfigDrive"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-config-drive"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/config_drive/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-07-16T00:00:00+00:00"'
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
name|'Controller'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
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
dedent|''
dedent|''
endmarker|''
end_unit
