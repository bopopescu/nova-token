begin_unit
comment|'#   Copyright 2013 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
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
name|'import'
name|'common'
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
name|'import'
name|'compute'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'evacuate'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
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
name|'Controller'
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
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'='
name|'compute'
op|'.'
name|'HostAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'ext_mgr'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'evacuate'"
op|')'
newline|'\n'
DECL|member|_evacuate
name|'def'
name|'_evacuate'
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
string|'"""Permit admins to evacuate a server from a failed host\n        to a new one.\n        If host is empty, the scheduler will select one.\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|'"evacuate"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|'"Malformed request body"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'evacuate_body'
op|'='
name|'body'
op|'['
string|'"evacuate"'
op|']'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'evacuate_body'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'not'
name|'host'
name|'and'
nl|'\n'
name|'not'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-extended-evacuate-find-host'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"host must be specified."'
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
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'on_shared_storage'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
nl|'\n'
name|'evacuate_body'
op|'['
string|'"onSharedStorage"'
op|']'
op|')'
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
name|'msg'
op|'='
name|'_'
op|'('
string|'"onSharedStorage must be specified."'
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
dedent|''
name|'password'
op|'='
name|'None'
newline|'\n'
name|'if'
string|"'adminPass'"
name|'in'
name|'evacuate_body'
op|':'
newline|'\n'
comment|'# check that if requested to evacuate server on shared storage'
nl|'\n'
comment|'# password not specified'
nl|'\n'
indent|'            '
name|'if'
name|'on_shared_storage'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"admin password can\'t be changed on existing disk"'
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
dedent|''
name|'password'
op|'='
name|'evacuate_body'
op|'['
string|"'adminPass'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'on_shared_storage'
op|':'
newline|'\n'
indent|'            '
name|'password'
op|'='
name|'utils'
op|'.'
name|'generate_password'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'host'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Compute host %s not found."'
op|')'
op|'%'
name|'host'
newline|'\n'
name|'raise'
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
dedent|''
dedent|''
name|'instance'
op|'='
name|'common'
op|'.'
name|'get_instance'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
name|'context'
op|','
name|'id'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance'
op|'.'
name|'host'
op|'=='
name|'host'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"The target host can\'t be the same one."'
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
dedent|''
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'evacuate'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'host'
op|','
nl|'\n'
name|'on_shared_storage'
op|','
name|'password'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceInvalidState'
name|'as'
name|'state_error'
op|':'
newline|'\n'
indent|'            '
name|'common'
op|'.'
name|'raise_http_conflict_for_instance_invalid_state'
op|'('
name|'state_error'
op|','
nl|'\n'
string|"'evacuate'"
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'ComputeServiceInUse'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
name|'if'
name|'password'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'adminPass'"
op|':'
name|'password'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Evacuate
dedent|''
dedent|''
dedent|''
name|'class'
name|'Evacuate'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Enables server evacuation."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Evacuate"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-evacuate"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/evacuate/api/v2"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2013-01-06T00:00:00Z"'
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
