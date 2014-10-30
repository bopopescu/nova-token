begin_unit
comment|'# Copyright 2010 OpenStack Foundation'
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
name|'console'
name|'import'
name|'api'
name|'as'
name|'console_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_keys
name|'def'
name|'_translate_keys'
op|'('
name|'cons'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Coerces a console instance into proper dictionary format."""'
newline|'\n'
name|'pool'
op|'='
name|'cons'
op|'['
string|"'pool'"
op|']'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'id'"
op|':'
name|'cons'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'console_type'"
op|':'
name|'pool'
op|'['
string|"'console_type'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_detail_keys
dedent|''
name|'def'
name|'_translate_detail_keys'
op|'('
name|'cons'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Coerces a console instance into proper dictionary format with detail."""'
newline|'\n'
name|'pool'
op|'='
name|'cons'
op|'['
string|"'pool'"
op|']'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'id'"
op|':'
name|'cons'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'console_type'"
op|':'
name|'pool'
op|'['
string|"'console_type'"
op|']'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'cons'
op|'['
string|"'password'"
op|']'
op|','
nl|'\n'
string|"'instance_name'"
op|':'
name|'cons'
op|'['
string|"'instance_name'"
op|']'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'cons'
op|'['
string|"'port'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'pool'
op|'['
string|"'public_hostname'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'console'
op|'='
name|'info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesController
dedent|''
name|'class'
name|'ConsolesController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Consoles controller for the OpenStack API."""'
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
name|'self'
op|'.'
name|'console_api'
op|'='
name|'console_api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
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
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of consoles for this instance."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'consoles'
op|'='
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'get_consoles'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'server_id'
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
name|'return'
name|'dict'
op|'('
name|'consoles'
op|'='
op|'['
name|'_translate_keys'
op|'('
name|'console'
op|')'
nl|'\n'
name|'for'
name|'console'
name|'in'
name|'consoles'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'201'
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
name|'server_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new console."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'create_console'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'server_id'
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
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
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
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shows in-depth information on a specific console."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'console'
op|'='
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'get_console'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleNotFound'
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
name|'return'
name|'_translate_detail_keys'
op|'('
name|'console'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes a console."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'delete_console'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ConsoleNotFound'
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
nl|'\n'
nl|'\n'
DECL|class|Consoles
dedent|''
dedent|''
dedent|''
name|'class'
name|'Consoles'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consoles."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Consoles"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"consoles"'
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
name|'parent'
op|'='
op|'{'
string|"'member_name'"
op|':'
string|"'server'"
op|','
nl|'\n'
string|"'collection_name'"
op|':'
string|"'servers'"
op|'}'
newline|'\n'
name|'resources'
op|'='
op|'['
nl|'\n'
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'consoles'"
op|','
name|'ConsolesController'
op|'('
op|')'
op|','
name|'parent'
op|'='
name|'parent'
op|','
nl|'\n'
name|'member_name'
op|'='
string|"'console'"
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
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
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
