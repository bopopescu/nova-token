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
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|TaskLog
name|'class'
name|'TaskLog'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'task_name'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'state'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'period_beginning'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
op|')'
op|','
nl|'\n'
string|"'period_ending'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
op|')'
op|','
nl|'\n'
string|"'message'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'task_items'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'errors'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'task_log'
op|','
name|'db_task_log'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'task_log'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'task_log'
op|','
name|'field'
op|','
name|'db_task_log'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
name|'task_log'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'task_log'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'task_log'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'serialize_args'
newline|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'period_beginning'
op|','
name|'period_ending'
op|','
name|'host'
op|','
nl|'\n'
name|'state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_task_log'
op|'='
name|'db'
op|'.'
name|'task_log_get'
op|'('
name|'context'
op|','
name|'task_name'
op|','
name|'period_beginning'
op|','
nl|'\n'
name|'period_ending'
op|','
name|'host'
op|','
name|'state'
op|'='
name|'state'
op|')'
newline|'\n'
name|'if'
name|'db_task_log'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_task_log'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|begin_task
name|'def'
name|'begin_task'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'task_log_begin_task'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'task_name'
op|','
name|'self'
op|'.'
name|'period_beginning'
op|','
nl|'\n'
name|'self'
op|'.'
name|'period_ending'
op|','
name|'self'
op|'.'
name|'host'
op|','
name|'task_items'
op|'='
name|'self'
op|'.'
name|'task_items'
op|','
nl|'\n'
name|'message'
op|'='
name|'self'
op|'.'
name|'message'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|end_task
name|'def'
name|'end_task'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'task_log_end_task'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'task_name'
op|','
name|'self'
op|'.'
name|'period_beginning'
op|','
nl|'\n'
name|'self'
op|'.'
name|'period_ending'
op|','
name|'self'
op|'.'
name|'host'
op|','
name|'errors'
op|'='
name|'self'
op|'.'
name|'errors'
op|','
nl|'\n'
name|'message'
op|'='
name|'self'
op|'.'
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|TaskLogList
name|'class'
name|'TaskLogList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'TaskLog'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'serialize_args'
newline|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'period_beginning'
op|','
name|'period_ending'
op|','
nl|'\n'
name|'host'
op|'='
name|'None'
op|','
name|'state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_task_logs'
op|'='
name|'db'
op|'.'
name|'task_log_get_all'
op|'('
name|'context'
op|','
name|'task_name'
op|','
nl|'\n'
name|'period_beginning'
op|','
name|'period_ending'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'state'
op|'='
name|'state'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'TaskLog'
op|','
name|'db_task_logs'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
