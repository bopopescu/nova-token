begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
op|'.'
name|'v3'
name|'import'
name|'remote_consoles'
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
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-remote-consoles"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteConsolesController
name|'class'
name|'RemoteConsolesController'
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
name|'super'
op|'('
name|'RemoteConsolesController'
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
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'get_vnc_console'"
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'remote_consoles'
op|'.'
name|'get_vnc_console'
op|')'
newline|'\n'
DECL|member|get_vnc_console
name|'def'
name|'get_vnc_console'
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
string|'"""Get text console output."""'
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
nl|'\n'
comment|'# If type is not supplied or unknown, get_vnc_console below will cope'
nl|'\n'
name|'console_type'
op|'='
name|'body'
op|'['
string|"'get_vnc_console'"
op|']'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'output'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_vnc_console'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'console_type'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleTypeInvalid'
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
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleTypeUnavailable'
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
name|'exception'
op|'.'
name|'InstanceNotReady'
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
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unable to get vnc console, functionality not implemented"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'type'"
op|':'
name|'console_type'
op|','
string|"'url'"
op|':'
name|'output'
op|'['
string|"'url'"
op|']'
op|'}'
op|'}'
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
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'get_spice_console'"
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'remote_consoles'
op|'.'
name|'get_spice_console'
op|')'
newline|'\n'
DECL|member|get_spice_console
name|'def'
name|'get_spice_console'
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
string|'"""Get text console output."""'
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
nl|'\n'
comment|'# If type is not supplied or unknown, get_spice_console below will cope'
nl|'\n'
name|'console_type'
op|'='
name|'body'
op|'['
string|"'get_spice_console'"
op|']'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'output'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_spice_console'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'console_type'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleTypeInvalid'
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
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleTypeUnavailable'
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
name|'exception'
op|'.'
name|'InstanceNotReady'
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
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unable to get spice console, "'
nl|'\n'
string|'"functionality not implemented"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'type'"
op|':'
name|'console_type'
op|','
string|"'url'"
op|':'
name|'output'
op|'['
string|"'url'"
op|']'
op|'}'
op|'}'
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
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'get_rdp_console'"
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'remote_consoles'
op|'.'
name|'get_rdp_console'
op|')'
newline|'\n'
DECL|member|get_rdp_console
name|'def'
name|'get_rdp_console'
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
string|'"""Get text console output."""'
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
nl|'\n'
comment|'# If type is not supplied or unknown, get_rdp_console below will cope'
nl|'\n'
name|'console_type'
op|'='
name|'body'
op|'['
string|"'get_rdp_console'"
op|']'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
newline|'\n'
nl|'\n'
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
comment|'# NOTE(mikal): get_rdp_console() can raise InstanceNotFound, so'
nl|'\n'
comment|'# we still need to catch it here.'
nl|'\n'
indent|'            '
name|'output'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_rdp_console'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'console_type'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleTypeInvalid'
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
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleTypeUnavailable'
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
name|'exception'
op|'.'
name|'InstanceNotReady'
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
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unable to get rdp console, functionality not implemented"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'type'"
op|':'
name|'console_type'
op|','
string|"'url'"
op|':'
name|'output'
op|'['
string|"'url'"
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteConsoles
dedent|''
dedent|''
name|'class'
name|'RemoteConsoles'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Interactive Console support."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"RemoteConsoles"'
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
name|'controller'
op|'='
name|'RemoteConsolesController'
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
dedent|''
dedent|''
endmarker|''
end_unit
