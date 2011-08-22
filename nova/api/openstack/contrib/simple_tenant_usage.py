begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'urlparse'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'datetime'
name|'import'
name|'datetime'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
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
name|'views'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_session'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|INSTANCE_FIELDS
name|'INSTANCE_FIELDS'
op|'='
op|'['
string|"'id'"
op|','
nl|'\n'
string|"'image_ref'"
op|','
nl|'\n'
string|"'project_id'"
op|','
nl|'\n'
string|"'user_id'"
op|','
nl|'\n'
string|"'display_name'"
op|','
nl|'\n'
string|"'state_description'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|','
nl|'\n'
string|"'launched_at'"
op|','
nl|'\n'
string|"'terminated_at'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsageController
name|'class'
name|'SimpleTenantUsageController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_get_instances_for_time_period
indent|'    '
name|'def'
name|'_get_instances_for_time_period'
op|'('
name|'self'
op|','
name|'period_start'
op|','
name|'period_stop'
op|','
nl|'\n'
name|'tenant_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_clause'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'tenant_id'
op|':'
newline|'\n'
indent|'            '
name|'tenant_clause'
op|'='
string|'" and project_id=\'%s\'"'
op|'%'
name|'tenant_id'
newline|'\n'
nl|'\n'
dedent|''
name|'conn'
op|'='
name|'get_session'
op|'('
op|')'
op|'.'
name|'connection'
op|'('
op|')'
newline|'\n'
name|'rows'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select %s from instances where \\\n                            (terminated_at is NULL or terminated_at > \'%s\') \\\n                            and (launched_at < \'%s\') %s"'
op|'%'
op|'('
string|"','"
op|'.'
name|'join'
op|'('
name|'INSTANCE_FIELDS'
op|')'
op|','
nl|'\n'
name|'period_start'
op|'.'
name|'isoformat'
op|'('
string|"' '"
op|')'
op|','
name|'period_stop'
op|'.'
name|'isoformat'
op|'('
string|"' '"
op|')'
op|','
nl|'\n'
name|'tenant_clause'
op|')'
op|')'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'rows'
newline|'\n'
nl|'\n'
DECL|member|_hours_for
dedent|''
name|'def'
name|'_hours_for'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'period_start'
op|','
name|'period_stop'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'launched_at'
op|'='
name|'instance'
op|'['
string|"'launched_at'"
op|']'
newline|'\n'
name|'terminated_at'
op|'='
name|'instance'
op|'['
string|"'terminated_at'"
op|']'
newline|'\n'
name|'if'
name|'terminated_at'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'terminated_at'
op|','
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'terminated_at'
op|'='
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'terminated_at'
op|','
nl|'\n'
string|'"%Y-%m-%d %H:%M:%S.%f"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'launched_at'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'launched_at'
op|','
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'launched_at'
op|'='
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'launched_at'
op|','
nl|'\n'
string|'"%Y-%m-%d %H:%M:%S.%f"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'terminated_at'
name|'and'
name|'terminated_at'
op|'<'
name|'period_start'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
comment|'# nothing if it started after the usage report ended'
nl|'\n'
dedent|''
name|'if'
name|'launched_at'
name|'and'
name|'launched_at'
op|'>'
name|'period_stop'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'if'
name|'launched_at'
op|':'
newline|'\n'
comment|"# if instance launched after period_started, don't charge for first"
nl|'\n'
indent|'            '
name|'start'
op|'='
name|'max'
op|'('
name|'launched_at'
op|','
name|'period_start'
op|')'
newline|'\n'
name|'if'
name|'terminated_at'
op|':'
newline|'\n'
comment|"# if instance stopped before period_stop, don't charge after"
nl|'\n'
indent|'                '
name|'stop'
op|'='
name|'min'
op|'('
name|'period_stop'
op|','
name|'terminated_at'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# instance is still running, so charge them up to current time'
nl|'\n'
indent|'                '
name|'stop'
op|'='
name|'period_stop'
newline|'\n'
dedent|''
name|'dt'
op|'='
name|'stop'
op|'-'
name|'start'
newline|'\n'
name|'seconds'
op|'='
name|'dt'
op|'.'
name|'days'
op|'*'
number|'3600'
op|'*'
number|'24'
op|'+'
name|'dt'
op|'.'
name|'seconds'
op|'+'
name|'dt'
op|'.'
name|'microseconds'
op|'/'
number|'100000.0'
newline|'\n'
nl|'\n'
name|'return'
name|'seconds'
op|'/'
number|'3600.0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# instance hasn't launched, so no charge"
nl|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|member|_tenant_usages_for_period
dedent|''
dedent|''
name|'def'
name|'_tenant_usages_for_period'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|','
name|'tenant_id'
op|'='
name|'None'
op|','
name|'detailed'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'rows'
op|'='
name|'self'
op|'.'
name|'_get_instances_for_time_period'
op|'('
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|','
nl|'\n'
name|'tenant_id'
op|')'
newline|'\n'
name|'rval'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'flavors'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'row'
name|'in'
name|'rows'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'INSTANCE_FIELDS'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
name|'INSTANCE_FIELDS'
op|'['
name|'i'
op|']'
op|']'
op|'='
name|'row'
op|'['
name|'i'
op|']'
newline|'\n'
dedent|''
name|'info'
op|'['
string|"'hours'"
op|']'
op|'='
name|'self'
op|'.'
name|'_hours_for'
op|'('
name|'info'
op|','
name|'period_start'
op|','
name|'period_stop'
op|')'
newline|'\n'
name|'flavor_type'
op|'='
name|'info'
op|'['
string|"'instance_type_id'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'flavors'
op|'.'
name|'get'
op|'('
name|'flavor_type'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'flavors'
op|'['
name|'flavor_type'
op|']'
op|'='
name|'db'
op|'.'
name|'instance_type_get'
op|'('
name|'context'
op|','
nl|'\n'
name|'info'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
op|':'
newline|'\n'
comment|"# can't bill if there is no instance type"
nl|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'flavor'
op|'='
name|'flavors'
op|'['
name|'flavor_type'
op|']'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'name'"
op|']'
op|'='
name|'info'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'del'
op|'('
name|'info'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'memory_mb'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'info'
op|'['
string|"'local_gb'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'info'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'info'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'del'
op|'('
name|'info'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'flavor'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'del'
op|'('
name|'info'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'started_at'"
op|']'
op|'='
name|'info'
op|'['
string|"'launched_at'"
op|']'
newline|'\n'
name|'del'
op|'('
name|'info'
op|'['
string|"'launched_at'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|'='
name|'info'
op|'['
string|"'terminated_at'"
op|']'
newline|'\n'
name|'del'
op|'('
name|'info'
op|'['
string|"'terminated_at'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
string|"'state'"
op|']'
op|'='
string|"'terminated'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
string|"'state'"
op|']'
op|'='
name|'info'
op|'['
string|"'state_description'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'del'
op|'('
name|'info'
op|'['
string|"'state_description'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'info'
op|'['
string|"'state'"
op|']'
op|'=='
string|"'terminated'"
op|':'
newline|'\n'
indent|'                '
name|'delta'
op|'='
name|'self'
op|'.'
name|'_parse_datetime'
op|'('
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|')'
op|'-'
name|'self'
op|'.'
name|'_parse_datetime'
op|'('
name|'info'
op|'['
string|"'started_at'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'delta'
op|'='
name|'now'
op|'-'
name|'self'
op|'.'
name|'_parse_datetime'
op|'('
name|'info'
op|'['
string|"'started_at'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'info'
op|'['
string|"'uptime'"
op|']'
op|'='
name|'delta'
op|'.'
name|'days'
op|'*'
number|'24'
op|'*'
number|'60'
op|'+'
name|'delta'
op|'.'
name|'seconds'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'info'
op|'['
string|"'tenant_id'"
op|']'
name|'in'
name|'rval'
op|':'
newline|'\n'
indent|'                '
name|'summary'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'summary'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'info'
op|'['
string|"'tenant_id'"
op|']'
newline|'\n'
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'                    '
name|'summary'
op|'['
string|"'server_usages'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'summary'
op|'['
string|"'total_local_gb_usage'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'total_vcpus_usage'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'total_memory_mb_usage'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'total_hours'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'start'"
op|']'
op|'='
name|'period_start'
newline|'\n'
name|'summary'
op|'['
string|"'stop'"
op|']'
op|'='
name|'period_stop'
newline|'\n'
name|'rval'
op|'['
name|'info'
op|'['
string|"'tenant_id'"
op|']'
op|']'
op|'='
name|'summary'
newline|'\n'
nl|'\n'
dedent|''
name|'summary'
op|'='
name|'rval'
op|'['
name|'info'
op|'['
string|"'tenant_id'"
op|']'
op|']'
newline|'\n'
name|'summary'
op|'['
string|"'total_local_gb_usage'"
op|']'
op|'+='
name|'info'
op|'['
string|"'local_gb'"
op|']'
op|'*'
name|'info'
op|'['
string|"'hours'"
op|']'
newline|'\n'
name|'summary'
op|'['
string|"'total_vcpus_usage'"
op|']'
op|'+='
name|'info'
op|'['
string|"'vcpus'"
op|']'
op|'*'
name|'info'
op|'['
string|"'hours'"
op|']'
newline|'\n'
name|'summary'
op|'['
string|"'total_memory_mb_usage'"
op|']'
op|'+='
name|'info'
op|'['
string|"'memory_mb'"
op|']'
op|'*'
name|'info'
op|'['
string|"'hours'"
op|']'
newline|'\n'
nl|'\n'
name|'summary'
op|'['
string|"'total_hours'"
op|']'
op|'+='
name|'info'
op|'['
string|"'hours'"
op|']'
newline|'\n'
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'                '
name|'summary'
op|'['
string|"'server_usages'"
op|']'
op|'.'
name|'append'
op|'('
name|'info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'rval'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parse_datetime
dedent|''
name|'def'
name|'_parse_datetime'
op|'('
name|'self'
op|','
name|'dtstr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'dtstr'
op|','
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dtstr'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'dtstr'
op|','
string|'"%Y-%m-%dT%H:%M:%S"'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'dtstr'
op|','
string|'"%Y-%m-%dT%H:%M:%S.%f"'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'dtstr'
op|','
string|'"%Y-%m-%d %H:%M:%S.%f"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_datetime_range
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_datetime_range'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'qs'
op|'='
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'QUERY_STRING'"
op|','
string|"''"
op|')'
newline|'\n'
name|'env'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'qs'
op|')'
newline|'\n'
name|'period_start'
op|'='
name|'self'
op|'.'
name|'_parse_datetime'
op|'('
name|'env'
op|'.'
name|'get'
op|'('
string|"'start'"
op|','
nl|'\n'
op|'['
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'isoformat'
op|'('
op|')'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'period_stop'
op|'='
name|'self'
op|'.'
name|'_parse_datetime'
op|'('
name|'env'
op|'.'
name|'get'
op|'('
string|"'end'"
op|','
nl|'\n'
op|'['
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'isoformat'
op|'('
op|')'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'detailed'
op|'='
name|'bool'
op|'('
name|'env'
op|'.'
name|'get'
op|'('
string|"'detailed'"
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'period_start'
op|','
name|'period_stop'
op|','
name|'detailed'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrive tenant_usage for all tenants"""'
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
name|'if'
name|'not'
name|'context'
op|'.'
name|'is_admin'
name|'and'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'('
name|'period_start'
op|','
name|'period_stop'
op|','
name|'detailed'
op|')'
op|'='
name|'self'
op|'.'
name|'_get_datetime_range'
op|'('
name|'req'
op|')'
newline|'\n'
name|'usages'
op|'='
name|'self'
op|'.'
name|'_tenant_usages_for_period'
op|'('
name|'context'
op|','
nl|'\n'
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'detailed'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'tenant_usages'"
op|':'
name|'usages'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrive tenant_usage for a specified tenant"""'
newline|'\n'
name|'tenant_id'
op|'='
name|'id'
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
name|'if'
name|'not'
name|'context'
op|'.'
name|'is_admin'
name|'and'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tenant_id'
op|'!='
name|'context'
op|'.'
name|'project_id'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'('
name|'period_start'
op|','
name|'period_stop'
op|','
name|'ignore'
op|')'
op|'='
name|'self'
op|'.'
name|'_get_datetime_range'
op|'('
name|'req'
op|')'
newline|'\n'
name|'usage'
op|'='
name|'self'
op|'.'
name|'_tenant_usages_for_period'
op|'('
name|'context'
op|','
nl|'\n'
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|','
nl|'\n'
name|'tenant_id'
op|'='
name|'tenant_id'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'usage'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'usage'
op|'='
name|'usage'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'usage'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'tenant_usage'"
op|':'
name|'usage'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Simple_tenant_usage
dedent|''
dedent|''
name|'class'
name|'Simple_tenant_usage'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
DECL|member|get_name
indent|'    '
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Simple_tenant_usage"'
newline|'\n'
nl|'\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"os-simple-tenant-usage"'
newline|'\n'
nl|'\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Simple tenant usage extension"'
newline|'\n'
nl|'\n'
DECL|member|get_namespace
dedent|''
name|'def'
name|'get_namespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"http://docs.openstack.org/ext/os-simple-tenant-usage/api/v1.1"'
newline|'\n'
nl|'\n'
DECL|member|get_updated
dedent|''
name|'def'
name|'get_updated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"2011-08-19T00:00:00+00:00"'
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
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-simple-tenant-usage'"
op|','
nl|'\n'
name|'SimpleTenantUsageController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
