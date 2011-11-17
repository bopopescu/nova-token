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
name|'json'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
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
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
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
DECL|variable|SERVERS
name|'SERVERS'
op|'='
number|'5'
newline|'\n'
DECL|variable|TENANTS
name|'TENANTS'
op|'='
number|'2'
newline|'\n'
DECL|variable|HOURS
name|'HOURS'
op|'='
number|'24'
newline|'\n'
DECL|variable|LOCAL_GB
name|'LOCAL_GB'
op|'='
number|'10'
newline|'\n'
DECL|variable|MEMORY_MB
name|'MEMORY_MB'
op|'='
number|'1024'
newline|'\n'
DECL|variable|VCPUS
name|'VCPUS'
op|'='
number|'2'
newline|'\n'
DECL|variable|STOP
name|'STOP'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
DECL|variable|START
name|'START'
op|'='
name|'STOP'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
name|'HOURS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_type_get
name|'def'
name|'fake_instance_type_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_type_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'VCPUS'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'LOCAL_GB'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'MEMORY_MB'
op|','
nl|'\n'
string|"'name'"
op|':'
nl|'\n'
string|"'fakeflavor'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fake_db_instance
dedent|''
name|'def'
name|'get_fake_db_instance'
op|'('
name|'start'
op|','
name|'end'
op|','
name|'instance_id'
op|','
name|'tenant_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'instance_id'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'tenant_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fakeuser'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'name'"
op|','
nl|'\n'
string|"'state_description'"
op|':'
string|"'state'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'launched_at'"
op|':'
name|'start'
op|','
nl|'\n'
string|"'terminated_at'"
op|':'
name|'end'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get_active_by_window
dedent|''
name|'def'
name|'fake_instance_get_active_by_window'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'get_fake_db_instance'
op|'('
name|'START'
op|','
nl|'\n'
name|'STOP'
op|','
nl|'\n'
name|'x'
op|','
nl|'\n'
string|'"faketenant_%s"'
op|'%'
op|'('
name|'x'
op|'/'
name|'SERVERS'
op|')'
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'TENANTS'
op|'*'
name|'SERVERS'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsageTest
dedent|''
name|'class'
name|'SimpleTenantUsageTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'SimpleTenantUsageTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|'.'
name|'API'
op|','
string|'"get_instance_type"'
op|','
nl|'\n'
name|'fake_instance_type_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|'.'
name|'API'
op|','
string|'"get_active_by_window"'
op|','
nl|'\n'
name|'fake_instance_get_active_by_window'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fakeadmin_0'"
op|','
nl|'\n'
string|"'faketenant_0'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fakeadmin_0'"
op|','
nl|'\n'
string|"'faketenant_0'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'alt_user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fakeadmin_0'"
op|','
nl|'\n'
string|"'faketenant_1'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'False'
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|test_verify_index
dedent|''
name|'def'
name|'test_verify_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/os-simple-tenant-usage?start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'START'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'STOP'
op|'.'
name|'isoformat'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"GET"'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'usages'
op|'='
name|'res_dict'
op|'['
string|"'tenant_usages'"
op|']'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'logging'
op|'.'
name|'warn'
op|'('
name|'usages'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'TENANTS'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'usages'
op|'['
name|'i'
op|']'
op|'['
string|"'total_hours'"
op|']'
op|')'
op|','
nl|'\n'
name|'SERVERS'
op|'*'
name|'HOURS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'usages'
op|'['
name|'i'
op|']'
op|'['
string|"'total_local_gb_usage'"
op|']'
op|')'
op|','
nl|'\n'
name|'SERVERS'
op|'*'
name|'LOCAL_GB'
op|'*'
name|'HOURS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'usages'
op|'['
name|'i'
op|']'
op|'['
string|"'total_memory_mb_usage'"
op|']'
op|')'
op|','
nl|'\n'
name|'SERVERS'
op|'*'
name|'MEMORY_MB'
op|'*'
name|'HOURS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'usages'
op|'['
name|'i'
op|']'
op|'['
string|"'total_vcpus_usage'"
op|']'
op|')'
op|','
nl|'\n'
name|'SERVERS'
op|'*'
name|'VCPUS'
op|'*'
name|'HOURS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'usages'
op|'['
name|'i'
op|']'
op|'.'
name|'get'
op|'('
string|"'server_usages'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_detailed_index
dedent|''
dedent|''
name|'def'
name|'test_verify_detailed_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/os-simple-tenant-usage?'"
nl|'\n'
string|"'detailed=1&start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'START'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'STOP'
op|'.'
name|'isoformat'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"GET"'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'usages'
op|'='
name|'res_dict'
op|'['
string|"'tenant_usages'"
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'TENANTS'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'servers'
op|'='
name|'usages'
op|'['
name|'i'
op|']'
op|'['
string|"'server_usages'"
op|']'
newline|'\n'
name|'for'
name|'j'
name|'in'
name|'xrange'
op|'('
name|'SERVERS'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'servers'
op|'['
name|'j'
op|']'
op|'['
string|"'hours'"
op|']'
op|')'
op|','
name|'HOURS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_index_fails_for_nonadmin
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_verify_index_fails_for_nonadmin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/os-simple-tenant-usage?'"
nl|'\n'
string|"'detailed=1&start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'START'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'STOP'
op|'.'
name|'isoformat'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"GET"'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_show
dedent|''
name|'def'
name|'test_verify_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/faketenant_0/os-simple-tenant-usage/'"
nl|'\n'
string|"'faketenant_0?start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'START'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'STOP'
op|'.'
name|'isoformat'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"GET"'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'user_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'usage'
op|'='
name|'res_dict'
op|'['
string|"'tenant_usage'"
op|']'
newline|'\n'
name|'servers'
op|'='
name|'usage'
op|'['
string|"'server_usages'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'usage'
op|'['
string|"'server_usages'"
op|']'
op|')'
op|','
name|'SERVERS'
op|')'
newline|'\n'
name|'for'
name|'j'
name|'in'
name|'xrange'
op|'('
name|'SERVERS'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'servers'
op|'['
name|'j'
op|']'
op|'['
string|"'hours'"
op|']'
op|')'
op|','
name|'HOURS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_show_cant_view_other_tenant
dedent|''
dedent|''
name|'def'
name|'test_verify_show_cant_view_other_tenant'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/faketenant_1/os-simple-tenant-usage/'"
nl|'\n'
string|"'faketenant_0?start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'START'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'STOP'
op|'.'
name|'isoformat'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"GET"'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'alt_user_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
