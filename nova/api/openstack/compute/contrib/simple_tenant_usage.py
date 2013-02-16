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
name|'datetime'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
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
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
DECL|variable|authorize_show
name|'authorize_show'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'simple_tenant_usage:show'"
op|')'
newline|'\n'
DECL|variable|authorize_list
name|'authorize_list'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'simple_tenant_usage:list'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_usage
name|'def'
name|'make_usage'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'subelem_tag'
name|'in'
op|'('
string|"'tenant_id'"
op|','
string|"'total_local_gb_usage'"
op|','
nl|'\n'
string|"'total_vcpus_usage'"
op|','
string|"'total_memory_mb_usage'"
op|','
nl|'\n'
string|"'total_hours'"
op|','
string|"'start'"
op|','
string|"'stop'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subelem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
name|'subelem_tag'
op|')'
newline|'\n'
name|'subelem'
op|'.'
name|'text'
op|'='
name|'subelem_tag'
newline|'\n'
nl|'\n'
dedent|''
name|'server_usages'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
string|"'server_usages'"
op|')'
newline|'\n'
name|'server_usage'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'server_usages'
op|','
string|"'server_usage'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'server_usages'"
op|')'
newline|'\n'
name|'for'
name|'subelem_tag'
name|'in'
op|'('
string|"'instance_id'"
op|','
string|"'name'"
op|','
string|"'hours'"
op|','
string|"'memory_mb'"
op|','
nl|'\n'
string|"'local_gb'"
op|','
string|"'vcpus'"
op|','
string|"'tenant_id'"
op|','
string|"'flavor'"
op|','
nl|'\n'
string|"'started_at'"
op|','
string|"'ended_at'"
op|','
string|"'state'"
op|','
string|"'uptime'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subelem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'server_usage'
op|','
name|'subelem_tag'
op|')'
newline|'\n'
name|'subelem'
op|'.'
name|'text'
op|'='
name|'subelem_tag'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsageTemplate
dedent|''
dedent|''
name|'class'
name|'SimpleTenantUsageTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'tenant_usage'"
op|','
name|'selector'
op|'='
string|"'tenant_usage'"
op|')'
newline|'\n'
name|'make_usage'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsagesTemplate
dedent|''
dedent|''
name|'class'
name|'SimpleTenantUsagesTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'tenant_usages'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'tenant_usage'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'tenant_usages'"
op|')'
newline|'\n'
name|'make_usage'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsageController
dedent|''
dedent|''
name|'class'
name|'SimpleTenantUsageController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_hours_for
indent|'    '
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
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'terminated_at'
op|'='
name|'timeutils'
op|'.'
name|'parse_strtime'
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
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'launched_at'
op|'='
name|'timeutils'
op|'.'
name|'parse_strtime'
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
op|'('
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
nl|'\n'
name|'dt'
op|'.'
name|'microseconds'
op|'/'
number|'100000.0'
op|')'
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
name|'compute_api'
op|'='
name|'api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'instances'
op|'='
name|'compute_api'
op|'.'
name|'get_active_by_window'
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
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'info'
op|'['
string|"'hours'"
op|']'
op|'='
name|'self'
op|'.'
name|'_hours_for'
op|'('
name|'instance'
op|','
nl|'\n'
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|')'
newline|'\n'
name|'flavor_type'
op|'='
name|'instance'
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
name|'it_ref'
op|'='
name|'compute_api'
op|'.'
name|'get_instance_type'
op|'('
name|'context'
op|','
nl|'\n'
name|'flavor_type'
op|')'
newline|'\n'
name|'flavors'
op|'['
name|'flavor_type'
op|']'
op|'='
name|'it_ref'
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
string|"'instance_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'info'
op|'['
string|"'name'"
op|']'
op|'='
name|'instance'
op|'['
string|"'display_name'"
op|']'
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
string|"'root_gb'"
op|']'
op|'+'
name|'flavor'
op|'['
string|"'ephemeral_gb'"
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
name|'instance'
op|'['
string|"'project_id'"
op|']'
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
nl|'\n'
name|'info'
op|'['
string|"'started_at'"
op|']'
op|'='
name|'instance'
op|'['
string|"'launched_at'"
op|']'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|'='
name|'instance'
op|'['
string|"'terminated_at'"
op|']'
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
name|'instance'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'now'
op|'='
name|'timeutils'
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
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|'-'
name|'info'
op|'['
string|"'started_at'"
op|']'
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
name|'info'
op|'['
string|"'started_at'"
op|']'
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
number|'3600'
op|'+'
name|'delta'
op|'.'
name|'seconds'
newline|'\n'
nl|'\n'
name|'if'
name|'info'
op|'['
string|"'tenant_id'"
op|']'
name|'not'
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
op|'('
name|'info'
op|'['
string|"'memory_mb'"
op|']'
op|'*'
nl|'\n'
name|'info'
op|'['
string|"'hours'"
op|']'
op|')'
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
name|'not'
name|'dtstr'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'dtstr'
op|','
name|'datetime'
op|'.'
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
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'dtstr'
op|','
string|'"%Y-%m-%dT%H:%M:%S"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'dtstr'
op|','
string|'"%Y-%m-%dT%H:%M:%S.%f"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'timeutils'
op|'.'
name|'parse_strtime'
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
comment|'# NOTE(lzyeval): env.get() always returns a list'
nl|'\n'
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
op|'['
name|'None'
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
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'period_start'
op|'<'
name|'period_stop'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid start time. The start time cannot occur after "'
nl|'\n'
string|'"the end time."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'detailed'
op|'='
name|'env'
op|'.'
name|'get'
op|'('
string|"'detailed'"
op|','
op|'['
string|"'0'"
op|']'
op|')'
op|'['
number|'0'
op|']'
op|'=='
string|"'1'"
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
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'SimpleTenantUsagesTemplate'
op|')'
newline|'\n'
DECL|member|index
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
string|'"""Retrieve tenant_usage for all tenants."""'
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
name|'authorize_list'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
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
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'if'
name|'period_stop'
op|'>'
name|'now'
op|':'
newline|'\n'
indent|'            '
name|'period_stop'
op|'='
name|'now'
newline|'\n'
dedent|''
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
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'SimpleTenantUsageTemplate'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve tenant_usage for a specified tenant."""'
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
name|'authorize_show'
op|'('
name|'context'
op|','
op|'{'
string|"'project_id'"
op|':'
name|'tenant_id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'if'
name|'period_stop'
op|'>'
name|'now'
op|':'
newline|'\n'
indent|'            '
name|'period_stop'
op|'='
name|'now'
newline|'\n'
dedent|''
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
indent|'    '
string|'"""Simple tenant usage extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"SimpleTenantUsage"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-simple-tenant-usage"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"os-simple-tenant-usage/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-08-19T00:00:00+00:00"'
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
