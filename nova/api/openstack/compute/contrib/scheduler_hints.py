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
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerHintsController
name|'class'
name|'SchedulerHintsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_extract_scheduler_hints
name|'def'
name|'_extract_scheduler_hints'
op|'('
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hints'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'hints'
op|'.'
name|'update'
op|'('
name|'body'
op|'['
string|"'os:scheduler_hints'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Ignore if data is not present'
nl|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
comment|'# Fail if non-dict provided'
nl|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Malformed scheduler_hints attribute"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'hints'
newline|'\n'
nl|'\n'
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
name|'hints'
op|'='
name|'self'
op|'.'
name|'_extract_scheduler_hints'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'server'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'scheduler_hints'"
op|']'
op|'='
name|'hints'
newline|'\n'
name|'yield'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Missing server attribute"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Scheduler_hints
dedent|''
dedent|''
dedent|''
name|'class'
name|'Scheduler_hints'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pass arbitrary key/value pairs to the scheduler"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"SchedulerHints"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-scheduler-hints"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"scheduler-hints/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-07-19T00:00:00+00:00"'
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
name|'SchedulerHintsController'
op|'('
op|')'
newline|'\n'
name|'ext'
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
name|'ext'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
