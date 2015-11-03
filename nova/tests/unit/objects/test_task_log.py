begin_unit
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
name|'datetime'
newline|'\n'
nl|'\n'
name|'import'
name|'iso8601'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|NOW
name|'NOW'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
name|'microsecond'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|fake_task_log
name|'fake_task_log'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'task_name'"
op|':'
string|"'fake-name'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'fake-state'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake-host'"
op|','
nl|'\n'
string|"'period_beginning'"
op|':'
name|'NOW'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
number|'10'
op|')'
op|','
nl|'\n'
string|"'period_ending'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'fake-message'"
op|','
nl|'\n'
string|"'task_items'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'errors'"
op|':'
number|'0'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestTaskLog
name|'class'
name|'_TestTaskLog'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.task_log_get'"
op|','
name|'return_value'
op|'='
name|'fake_task_log'
op|')'
newline|'\n'
DECL|member|test_get
name|'def'
name|'test_get'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'task_log'
op|'='
name|'objects'
op|'.'
name|'TaskLog'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'state'
op|'='
name|'fake_task_log'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'strtime'
op|'('
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'strtime'
op|'('
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
op|')'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'state'
op|'='
name|'fake_task_log'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'task_log'
op|','
name|'fake_task_log'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.task_log_begin_task'"
op|')'
newline|'\n'
DECL|member|test_begin_task
name|'def'
name|'test_begin_task'
op|'('
name|'self'
op|','
name|'mock_begin_task'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'task_log'
op|'='
name|'objects'
op|'.'
name|'TaskLog'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'task_log'
op|'.'
name|'task_name'
op|'='
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'period_beginning'
op|'='
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'period_ending'
op|'='
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'host'
op|'='
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'task_items'
op|'='
name|'fake_task_log'
op|'['
string|"'task_items'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'message'
op|'='
name|'fake_task_log'
op|'['
string|"'message'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'begin_task'
op|'('
op|')'
newline|'\n'
name|'mock_begin_task'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
op|'.'
name|'replace'
op|'('
nl|'\n'
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
op|'.'
name|'replace'
op|'('
nl|'\n'
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'task_items'
op|'='
name|'fake_task_log'
op|'['
string|"'task_items'"
op|']'
op|','
nl|'\n'
name|'message'
op|'='
name|'fake_task_log'
op|'['
string|"'message'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.task_log_end_task'"
op|')'
newline|'\n'
DECL|member|test_end_task
name|'def'
name|'test_end_task'
op|'('
name|'self'
op|','
name|'mock_end_task'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'task_log'
op|'='
name|'objects'
op|'.'
name|'TaskLog'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'task_log'
op|'.'
name|'task_name'
op|'='
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'period_beginning'
op|'='
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'period_ending'
op|'='
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'host'
op|'='
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'errors'
op|'='
name|'fake_task_log'
op|'['
string|"'errors'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'message'
op|'='
name|'fake_task_log'
op|'['
string|"'message'"
op|']'
newline|'\n'
name|'task_log'
op|'.'
name|'end_task'
op|'('
op|')'
newline|'\n'
name|'mock_end_task'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
op|'.'
name|'replace'
op|'('
nl|'\n'
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
op|'.'
name|'replace'
op|'('
nl|'\n'
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'errors'
op|'='
name|'fake_task_log'
op|'['
string|"'errors'"
op|']'
op|','
nl|'\n'
name|'message'
op|'='
name|'fake_task_log'
op|'['
string|"'message'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestTaskLog
dedent|''
dedent|''
name|'class'
name|'TestTaskLog'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
name|'_TestTaskLog'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestRemoteTaskLog
dedent|''
name|'class'
name|'TestRemoteTaskLog'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
name|'_TestTaskLog'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestTaskLogList
dedent|''
name|'class'
name|'_TestTaskLogList'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.task_log_get_all'"
op|')'
newline|'\n'
DECL|member|test_get_all
name|'def'
name|'test_get_all'
op|'('
name|'self'
op|','
name|'mock_get_all'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_task_logs'
op|'='
op|'['
name|'dict'
op|'('
name|'fake_task_log'
op|','
name|'id'
op|'='
number|'1'
op|')'
op|','
name|'dict'
op|'('
name|'fake_task_log'
op|','
name|'id'
op|'='
number|'2'
op|')'
op|']'
newline|'\n'
name|'mock_get_all'
op|'.'
name|'return_value'
op|'='
name|'fake_task_logs'
newline|'\n'
name|'task_logs'
op|'='
name|'objects'
op|'.'
name|'TaskLogList'
op|'.'
name|'get_all'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
op|','
nl|'\n'
name|'host'
op|'='
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'state'
op|'='
name|'fake_task_log'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'mock_get_all'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'fake_task_log'
op|'['
string|"'task_name'"
op|']'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'strtime'
op|'('
name|'fake_task_log'
op|'['
string|"'period_beginning'"
op|']'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'strtime'
op|'('
name|'fake_task_log'
op|'['
string|"'period_ending'"
op|']'
op|')'
op|','
nl|'\n'
name|'host'
op|'='
name|'fake_task_log'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'state'
op|'='
name|'fake_task_log'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'task_log'
name|'in'
name|'enumerate'
op|'('
name|'task_logs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'task_log'
op|','
name|'fake_task_logs'
op|'['
name|'index'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestTaskLogList
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestTaskLogList'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
name|'_TestTaskLogList'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestRemoteTaskLogList
dedent|''
name|'class'
name|'TestRemoteTaskLogList'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
name|'_TestTaskLogList'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
