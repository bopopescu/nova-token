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
op|'.'
name|'conductor'
op|'.'
name|'tasks'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'utils'
name|'as'
name|'scheduler_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationTask
name|'class'
name|'MigrationTask'
op|'('
name|'base'
op|'.'
name|'TaskBase'
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
name|'context'
op|','
name|'instance'
op|','
name|'flavor'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'reservations'
op|','
name|'clean_shutdown'
op|','
name|'compute_rpcapi'
op|','
nl|'\n'
name|'scheduler_client'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MigrationTask'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'clean_shutdown'
op|'='
name|'clean_shutdown'
newline|'\n'
name|'self'
op|'.'
name|'request_spec'
op|'='
name|'request_spec'
newline|'\n'
name|'self'
op|'.'
name|'reservations'
op|'='
name|'reservations'
newline|'\n'
name|'self'
op|'.'
name|'filter_properties'
op|'='
name|'filter_properties'
newline|'\n'
name|'self'
op|'.'
name|'flavor'
op|'='
name|'flavor'
newline|'\n'
name|'self'
op|'.'
name|'quotas'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'='
name|'compute_rpcapi'
newline|'\n'
name|'self'
op|'.'
name|'scheduler_client'
op|'='
name|'scheduler_client'
newline|'\n'
nl|'\n'
DECL|member|_execute
dedent|''
name|'def'
name|'_execute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'self'
op|'.'
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'quotas'
op|'='
name|'objects'
op|'.'
name|'Quotas'
op|'.'
name|'from_reservations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'reservations'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'setup_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'request_spec'
op|','
nl|'\n'
name|'self'
op|'.'
name|'filter_properties'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'populate_retry'
op|'('
name|'self'
op|'.'
name|'filter_properties'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'request_spec'
op|','
name|'self'
op|'.'
name|'filter_properties'
op|')'
newline|'\n'
name|'host_state'
op|'='
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'populate_filter_properties'
op|'('
name|'self'
op|'.'
name|'filter_properties'
op|','
nl|'\n'
name|'host_state'
op|')'
newline|'\n'
comment|'# context is not serializable'
nl|'\n'
name|'self'
op|'.'
name|'filter_properties'
op|'.'
name|'pop'
op|'('
string|"'context'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'host'
op|','
name|'node'
op|')'
op|'='
op|'('
name|'host_state'
op|'['
string|"'host'"
op|']'
op|','
name|'host_state'
op|'['
string|"'nodename'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'prep_resize'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'image'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'flavor'
op|','
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'reservations'
op|','
name|'request_spec'
op|'='
name|'self'
op|'.'
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'self'
op|'.'
name|'filter_properties'
op|','
name|'node'
op|'='
name|'node'
op|','
nl|'\n'
name|'clean_shutdown'
op|'='
name|'self'
op|'.'
name|'clean_shutdown'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rollback
dedent|''
name|'def'
name|'rollback'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'quotas'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'quotas'
op|'.'
name|'rollback'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
