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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
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
name|'evacuate'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'enable_instance_password'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.servers'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-evacuate"'
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
DECL|class|EvacuateController
name|'class'
name|'EvacuateController'
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
name|'EvacuateController'
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
name|'skip_policy_check'
op|'='
name|'True'
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
nl|'\n'
DECL|member|_get_on_shared_storage
dedent|''
name|'def'
name|'_get_on_shared_storage'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'evacuate_body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.14'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'evacuate_body'
op|'['
string|'"onSharedStorage"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_password
dedent|''
dedent|''
name|'def'
name|'_get_password'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'evacuate_body'
op|','
name|'on_shared_storage'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'return'
name|'password'
newline|'\n'
nl|'\n'
DECL|member|_get_password_v214
dedent|''
name|'def'
name|'_get_password_v214'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'evacuate_body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'adminPass'"
name|'in'
name|'evacuate_body'
op|':'
newline|'\n'
indent|'            '
name|'password'
op|'='
name|'evacuate_body'
op|'['
string|"'adminPass'"
op|']'
newline|'\n'
dedent|''
name|'else'
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
name|'return'
name|'password'
newline|'\n'
nl|'\n'
comment|'# TODO(eliqiao): Should be responding here with 202 Accept'
nl|'\n'
comment|'# because evacuate is an async call, but keep to 200 for'
nl|'\n'
comment|'# backwards compatibility reasons.'
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
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'evacuate'"
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'evacuate'
op|'.'
name|'evacuate'
op|','
string|'"2.1"'
op|','
string|'"2.12"'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'evacuate'
op|'.'
name|'evacuate_v214'
op|','
string|'"2.14"'
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
string|'"""Permit admins to evacuate a server from a failed host\n        to a new one.\n        """'
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
name|'evacuate_body'
op|'='
name|'body'
op|'['
string|'"evacuate"'
op|']'
newline|'\n'
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
name|'on_shared_storage'
op|'='
name|'self'
op|'.'
name|'_get_on_shared_storage'
op|'('
name|'req'
op|','
name|'evacuate_body'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.14'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'password'
op|'='
name|'self'
op|'.'
name|'_get_password_v214'
op|'('
name|'req'
op|','
name|'evacuate_body'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'password'
op|'='
name|'self'
op|'.'
name|'_get_password'
op|'('
name|'req'
op|','
name|'evacuate_body'
op|','
nl|'\n'
name|'on_shared_storage'
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
name|'ComputeHostNotFound'
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
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'host'
op|'=='
name|'host'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'InstanceUnknownCell'
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
op|'('
name|'not'
name|'api_version_request'
op|'.'
name|'is_supported'
op|'('
name|'req'
op|','
name|'min_version'
op|'='
string|"'2.14'"
op|')'
name|'and'
nl|'\n'
name|'CONF'
op|'.'
name|'enable_instance_password'
op|')'
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
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
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
name|'V21APIExtensionBase'
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
name|'return'
op|'['
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
name|'controller'
op|'='
name|'EvacuateController'
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
