begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2011 Eldar Nugaev, Kirill Shileev, Ilya Alekseyev'
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
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
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
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'extensions'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.v2.contrib.console_output'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Console_output
name|'class'
name|'Console_output'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Console log output support, with tailing ability."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Console_output"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-console-output"'
newline|'\n'
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/"'
DECL|variable|namespace
string|'"os-console-output/api/v2"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-12-08T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
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
name|'Console_output'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ext_mgr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'server_id'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'routing_get'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
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
name|'_'
op|'('
string|"'Instance not found'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'length'
op|'='
name|'input_dict'
op|'['
string|"'os-getConsoleOutput'"
op|']'
op|'.'
name|'get'
op|'('
string|"'length'"
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
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|"'Malformed request body'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'output'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_console_output'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'length'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ApiError'
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
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
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
name|'HTTPUnauthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'output'"
op|':'
name|'output'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the actions the extension adds, as required by contract."""'
newline|'\n'
name|'actions'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ActionExtension'
op|'('
string|'"servers"'
op|','
string|'"os-getConsoleOutput"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_console_output'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'actions'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
