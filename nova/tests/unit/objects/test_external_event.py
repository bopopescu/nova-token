begin_unit
comment|'#    Copyright 2014 Red Hat, Inc.'
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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'external_event'
name|'as'
name|'external_event_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceExternalEventObject
name|'class'
name|'_TestInstanceExternalEventObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_make_key
indent|'    '
name|'def'
name|'test_make_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
name|'external_event_obj'
op|'.'
name|'InstanceExternalEvent'
op|'.'
name|'make_key'
op|'('
string|"'foo'"
op|','
string|"'bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo-bar'"
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_make_key_no_tag
dedent|''
name|'def'
name|'test_make_key_no_tag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
name|'external_event_obj'
op|'.'
name|'InstanceExternalEvent'
op|'.'
name|'make_key'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_key
dedent|''
name|'def'
name|'test_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'event'
op|'='
name|'external_event_obj'
op|'.'
name|'InstanceExternalEvent'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'network-changed'"
op|','
nl|'\n'
name|'tag'
op|'='
string|"'bar'"
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'event'
op|','
string|"'make_key'"
op|')'
name|'as'
name|'make_key'
op|':'
newline|'\n'
indent|'            '
name|'make_key'
op|'.'
name|'return_value'
op|'='
string|"'key'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'key'"
op|','
name|'event'
op|'.'
name|'key'
op|')'
newline|'\n'
name|'make_key'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'network-changed'"
op|','
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_event_names
dedent|''
dedent|''
name|'def'
name|'test_event_names'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'event'
name|'in'
name|'external_event_obj'
op|'.'
name|'EVENT_NAMES'
op|':'
newline|'\n'
indent|'            '
name|'external_event_obj'
op|'.'
name|'InstanceExternalEvent'
op|'('
name|'name'
op|'='
name|'event'
op|','
name|'tag'
op|'='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
nl|'\n'
name|'external_event_obj'
op|'.'
name|'InstanceExternalEvent'
op|','
nl|'\n'
name|'name'
op|'='
string|"'foo'"
op|','
name|'tag'
op|'='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceExternalEventObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceExternalEventObject
name|'_TestInstanceExternalEventObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteInstanceExternalEventObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceExternalEventObject
name|'_TestInstanceExternalEventObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
