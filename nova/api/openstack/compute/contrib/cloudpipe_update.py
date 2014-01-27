begin_unit
comment|'# Copyright 2012 IBM Corp.'
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
nl|'\n'
name|'import'
name|'webob'
op|'.'
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
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
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
string|"'cloudpipe_update'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudpipeUpdateController
name|'class'
name|'CloudpipeUpdateController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Handle updating the vpn ip/port for cloudpipe instances."""'
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
name|'CloudpipeUpdateController'
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
string|'"update"'
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
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Configure cloudpipe parameters for the project."""'
newline|'\n'
nl|'\n'
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
name|'if'
name|'id'
op|'!='
string|'"configure-project"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unknown action %s"'
op|')'
op|'%'
name|'id'
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
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'body'
op|'['
string|"'configure_project'"
op|']'
newline|'\n'
name|'vpn_ip'
op|'='
name|'params'
op|'['
string|"'vpn_ip'"
op|']'
newline|'\n'
name|'vpn_port'
op|'='
name|'params'
op|'['
string|"'vpn_port'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'networks'
op|'='
name|'db'
op|'.'
name|'project_get_networks'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'for'
name|'network'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'network'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'vpn_public_address'"
op|':'
name|'vpn_ip'
op|','
nl|'\n'
string|"'vpn_public_port'"
op|':'
name|'int'
op|'('
name|'vpn_port'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Cloudpipe_update
dedent|''
dedent|''
name|'class'
name|'Cloudpipe_update'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds the ability to set the vpn ip/port for cloudpipe instances."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"CloudpipeUpdate"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-cloudpipe-update"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/cloudpipe-update/api/v2"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-11-14T00:00:00+00:00"'
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
name|'CloudpipeUpdateController'
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
string|"'os-cloudpipe'"
op|','
nl|'\n'
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
