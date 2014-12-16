begin_unit
comment|'# Copyright (c) 2014 Red Hat, Inc.'
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
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LazyLoader
name|'class'
name|'LazyLoader'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'klass'
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
name|'klass'
op|'='
name|'klass'
newline|'\n'
name|'self'
op|'.'
name|'args'
op|'='
name|'args'
newline|'\n'
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'kwargs'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'functools'
op|'.'
name|'partial'
op|'('
name|'self'
op|'.'
name|'__run_method'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__run_method
dedent|''
name|'def'
name|'__run_method'
op|'('
name|'self'
op|','
name|'__name'
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
name|'if'
name|'self'
op|'.'
name|'instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance'
op|'='
name|'self'
op|'.'
name|'klass'
op|'('
op|'*'
name|'self'
op|'.'
name|'args'
op|','
op|'**'
name|'self'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
name|'__name'
op|')'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerClient
dedent|''
dedent|''
name|'class'
name|'SchedulerClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Client library for placing calls to the scheduler."""'
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
name|'queryclient'
op|'='
name|'LazyLoader'
op|'('
name|'importutils'
op|'.'
name|'import_class'
op|'('
nl|'\n'
string|"'nova.scheduler.client.query.SchedulerQueryClient'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reportclient'
op|'='
name|'LazyLoader'
op|'('
name|'importutils'
op|'.'
name|'import_class'
op|'('
nl|'\n'
string|"'nova.scheduler.client.report.SchedulerReportClient'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'retry_select_destinations'
newline|'\n'
DECL|member|select_destinations
name|'def'
name|'select_destinations'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'queryclient'
op|'.'
name|'select_destinations'
op|'('
nl|'\n'
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_resource_stats
dedent|''
name|'def'
name|'update_resource_stats'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'stats'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'reportclient'
op|'.'
name|'update_resource_stats'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'stats'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
