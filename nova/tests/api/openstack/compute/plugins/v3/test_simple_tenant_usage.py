begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'simple_tenant_usage'
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
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'policy'
name|'as'
name|'common_policy'
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
name|'from'
name|'nova'
name|'import'
name|'policy'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|ROOT_GB
name|'ROOT_GB'
op|'='
number|'10'
newline|'\n'
DECL|variable|EPHEMERAL_GB
name|'EPHEMERAL_GB'
op|'='
number|'20'
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
DECL|variable|NOW
name|'NOW'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
DECL|variable|START
name|'START'
op|'='
name|'NOW'
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
DECL|variable|STOP
name|'STOP'
op|'='
name|'NOW'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_INST_TYPE
name|'FAKE_INST_TYPE'
op|'='
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
string|"'root_gb'"
op|':'
name|'ROOT_GB'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'EPHEMERAL_GB'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'MEMORY_MB'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeflavor'"
op|','
nl|'\n'
string|"'flavorid'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'vcpu_weight'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fake_db_instance
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
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'dict_to_metadata'
op|'('
nl|'\n'
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
op|'{'
op|'}'
op|','
name|'FAKE_INST_TYPE'
op|')'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'id'"
op|':'
name|'instance_id'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000%02d'"
op|'%'
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
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get_active_by_window_joined
dedent|''
name|'def'
name|'fake_instance_get_active_by_window_joined'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|','
nl|'\n'
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
string|'"get_active_by_window"'
op|','
nl|'\n'
name|'fake_instance_get_active_by_window_joined'
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
name|'self'
op|'.'
name|'flags'
op|'('
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Simple_tenant_usage'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_verify_index
dedent|''
name|'def'
name|'_test_verify_index'
op|'('
name|'self'
op|','
name|'start'
op|','
name|'stop'
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
string|"'/v3/os-simple-tenant-usage?start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'start'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'stop'
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
name|'wsgi_app_v3'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|','
nl|'\n'
name|'init_only'
op|'='
op|'('
string|"'os-simple-tenant-usage'"
op|','
nl|'\n'
string|"'servers'"
op|')'
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
name|'jsonutils'
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
op|'('
name|'ROOT_GB'
op|'+'
name|'EPHEMERAL_GB'
op|')'
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
DECL|member|test_verify_index
dedent|''
dedent|''
name|'def'
name|'test_verify_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_verify_index'
op|'('
name|'START'
op|','
name|'STOP'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_index_future_end_time
dedent|''
name|'def'
name|'test_verify_index_future_end_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'future'
op|'='
name|'NOW'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
name|'HOURS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_verify_index'
op|'('
name|'START'
op|','
name|'future'
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
name|'self'
op|'.'
name|'_test_verify_show'
op|'('
name|'START'
op|','
name|'STOP'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_show_future_end_time
dedent|''
name|'def'
name|'test_verify_show_future_end_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'future'
op|'='
name|'NOW'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
name|'HOURS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_verify_show'
op|'('
name|'START'
op|','
name|'future'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_tenant_usages
dedent|''
name|'def'
name|'_get_tenant_usages'
op|'('
name|'self'
op|','
name|'detailed'
op|'='
string|"''"
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
string|"'/v3/os-simple-tenant-usage?'"
nl|'\n'
string|"'detailed=%s&start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'detailed'
op|','
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
name|'wsgi_app_v3'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|','
nl|'\n'
name|'init_only'
op|'='
op|'('
string|"'os-simple-tenant-usage'"
op|','
nl|'\n'
string|"'servers'"
op|')'
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
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'return'
name|'res_dict'
op|'['
string|"'tenant_usages'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_verify_detailed_index
dedent|''
name|'def'
name|'test_verify_detailed_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usages'
op|'='
name|'self'
op|'.'
name|'_get_tenant_usages'
op|'('
string|"'1'"
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
DECL|member|test_verify_simple_index
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_verify_simple_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usages'
op|'='
name|'self'
op|'.'
name|'_get_tenant_usages'
op|'('
name|'detailed'
op|'='
string|"'0'"
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
name|'usages'
op|'['
name|'i'
op|']'
op|'.'
name|'get'
op|'('
string|"'server_usages'"
op|')'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_simple_index_empty_param
dedent|''
dedent|''
name|'def'
name|'test_verify_simple_index_empty_param'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(lzyeval): 'detailed=&start=..&end=..'"
nl|'\n'
indent|'        '
name|'usages'
op|'='
name|'self'
op|'.'
name|'_get_tenant_usages'
op|'('
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
name|'usages'
op|'['
name|'i'
op|']'
op|'.'
name|'get'
op|'('
string|"'server_usages'"
op|')'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_verify_show
dedent|''
dedent|''
name|'def'
name|'_test_verify_show'
op|'('
name|'self'
op|','
name|'start'
op|','
name|'stop'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_id'
op|'='
number|'0'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/os-simple-tenant-usage/'"
nl|'\n'
string|"'faketenant_%s?start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'tenant_id'
op|','
name|'start'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'stop'
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
name|'wsgi_app_v3'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'user_context'
op|','
nl|'\n'
name|'init_only'
op|'='
op|'('
string|"'os-simple-tenant-usage'"
op|','
nl|'\n'
string|"'servers'"
op|')'
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
name|'jsonutils'
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
name|'uuids'
op|'='
op|'['
string|"'00000000-0000-0000-0000-00000000000000%02d'"
op|'%'
nl|'\n'
op|'('
name|'x'
op|'+'
op|'('
name|'tenant_id'
op|'*'
name|'SERVERS'
op|')'
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'SERVERS'
op|')'
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
indent|'            '
name|'delta'
op|'='
name|'STOP'
op|'-'
name|'START'
newline|'\n'
name|'uptime'
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
string|"'uptime'"
op|']'
op|')'
op|','
name|'uptime'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'servers'
op|'['
name|'j'
op|']'
op|'['
string|"'instance_id'"
op|']'
name|'in'
name|'uuids'
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
string|"'/v3/os-simple-tenant-usage/'"
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
name|'rules'
op|'='
op|'{'
nl|'\n'
string|'"compute_extension:simple_tenant_usage:show"'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
op|'['
nl|'\n'
op|'['
string|'"role:admin"'
op|']'
op|','
op|'['
string|'"project_id:%(project_id)s"'
op|']'
nl|'\n'
op|']'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'common_policy'
op|'.'
name|'set_rules'
op|'('
name|'common_policy'
op|'.'
name|'Rules'
op|'('
name|'rules'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v3'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'alt_user_context'
op|','
nl|'\n'
name|'init_only'
op|'='
op|'('
string|"'os-simple-tenant-usage'"
op|','
nl|'\n'
string|"'servers'"
op|')'
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
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_tenants_usage_with_bad_start_date
dedent|''
dedent|''
name|'def'
name|'test_get_tenants_usage_with_bad_start_date'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'future'
op|'='
name|'NOW'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
name|'HOURS'
op|')'
newline|'\n'
name|'tenant_id'
op|'='
number|'0'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v3/os-simple-tenant-usage/'"
nl|'\n'
string|"'faketenant_%s?start=%s&end=%s'"
op|'%'
nl|'\n'
op|'('
name|'tenant_id'
op|','
name|'future'
op|'.'
name|'isoformat'
op|'('
op|')'
op|','
name|'NOW'
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
name|'wsgi_app_v3'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'user_context'
op|','
nl|'\n'
name|'init_only'
op|'='
op|'('
string|"'os-simple-tenant-usage'"
op|','
nl|'\n'
string|"'servers'"
op|')'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsageSerializerTest
dedent|''
dedent|''
name|'class'
name|'SimpleTenantUsageSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_verify_server_usage
indent|'    '
name|'def'
name|'_verify_server_usage'
op|'('
name|'self'
op|','
name|'raw_usage'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'server_usage'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
nl|'\n'
comment|'# Figure out what fields we expect'
nl|'\n'
name|'not_seen'
op|'='
name|'set'
op|'('
name|'raw_usage'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'child'
op|'.'
name|'tag'
name|'in'
name|'not_seen'
op|')'
newline|'\n'
name|'not_seen'
op|'.'
name|'remove'
op|'('
name|'child'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'raw_usage'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
op|','
name|'child'
op|'.'
name|'text'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'not_seen'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_tenant_usage
dedent|''
name|'def'
name|'_verify_tenant_usage'
op|'('
name|'self'
op|','
name|'raw_usage'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'tenant_usage'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
nl|'\n'
comment|'# Figure out what fields we expect'
nl|'\n'
name|'not_seen'
op|'='
name|'set'
op|'('
name|'raw_usage'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'child'
op|'.'
name|'tag'
name|'in'
name|'not_seen'
op|')'
newline|'\n'
name|'not_seen'
op|'.'
name|'remove'
op|'('
name|'child'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'if'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'server_usages'"
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'idx'
op|','
name|'gr_child'
name|'in'
name|'enumerate'
op|'('
name|'child'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_verify_server_usage'
op|'('
name|'raw_usage'
op|'['
string|"'server_usages'"
op|']'
op|'['
name|'idx'
op|']'
op|','
nl|'\n'
name|'gr_child'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'raw_usage'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
op|','
name|'child'
op|'.'
name|'text'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'not_seen'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serializer_show
dedent|''
name|'def'
name|'test_serializer_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'simple_tenant_usage'
op|'.'
name|'SimpleTenantUsageTemplate'
op|'('
op|')'
newline|'\n'
name|'today'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'yesterday'
op|'='
name|'today'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'days'
op|'='
number|'1'
op|')'
newline|'\n'
name|'raw_usage'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant'"
op|','
nl|'\n'
name|'total_local_gb_usage'
op|'='
number|'789'
op|','
nl|'\n'
name|'total_vcpus_usage'
op|'='
number|'456'
op|','
nl|'\n'
name|'total_memory_mb_usage'
op|'='
number|'123'
op|','
nl|'\n'
name|'total_hours'
op|'='
number|'24'
op|','
nl|'\n'
name|'start'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'stop'
op|'='
name|'today'
op|','
nl|'\n'
name|'server_usages'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
string|"'00000000-0000-0000-0000-0000000000000000'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'test'"
op|','
nl|'\n'
name|'hours'
op|'='
number|'24'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'50'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant'"
op|','
nl|'\n'
name|'flavor'
op|'='
string|"'m1.small'"
op|','
nl|'\n'
name|'started_at'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'ended_at'
op|'='
name|'today'
op|','
nl|'\n'
name|'state'
op|'='
string|"'terminated'"
op|','
nl|'\n'
name|'uptime'
op|'='
number|'86400'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
string|"'00000000-0000-0000-0000-0000000000000002'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'test2'"
op|','
nl|'\n'
name|'hours'
op|'='
number|'12'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'25'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'2'
op|','
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant'"
op|','
nl|'\n'
name|'flavor'
op|'='
string|"'m1.tiny'"
op|','
nl|'\n'
name|'started_at'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'ended_at'
op|'='
name|'today'
op|','
nl|'\n'
name|'state'
op|'='
string|"'terminated'"
op|','
nl|'\n'
name|'uptime'
op|'='
number|'43200'
op|')'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'tenant_usage'
op|'='
name|'dict'
op|'('
name|'tenant_usage'
op|'='
name|'raw_usage'
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'tenant_usage'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_tenant_usage'
op|'('
name|'raw_usage'
op|','
name|'tree'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serializer_index
dedent|''
name|'def'
name|'test_serializer_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'simple_tenant_usage'
op|'.'
name|'SimpleTenantUsagesTemplate'
op|'('
op|')'
newline|'\n'
name|'today'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'yesterday'
op|'='
name|'today'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'days'
op|'='
number|'1'
op|')'
newline|'\n'
name|'raw_usages'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant1'"
op|','
nl|'\n'
name|'total_local_gb_usage'
op|'='
number|'1024'
op|','
nl|'\n'
name|'total_vcpus_usage'
op|'='
number|'23'
op|','
nl|'\n'
name|'total_memory_mb_usage'
op|'='
number|'512'
op|','
nl|'\n'
name|'total_hours'
op|'='
number|'24'
op|','
nl|'\n'
name|'start'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'stop'
op|'='
name|'today'
op|','
nl|'\n'
name|'server_usages'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
string|"'00000000-0000-0000-0000-0000000000000001'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'test1'"
op|','
nl|'\n'
name|'hours'
op|'='
number|'24'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'50'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'2'
op|','
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant1'"
op|','
nl|'\n'
name|'flavor'
op|'='
string|"'m1.small'"
op|','
nl|'\n'
name|'started_at'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'ended_at'
op|'='
name|'today'
op|','
nl|'\n'
name|'state'
op|'='
string|"'terminated'"
op|','
nl|'\n'
name|'uptime'
op|'='
number|'86400'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
string|"'00000000-0000-0000-0000-0000000000000002'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'test2'"
op|','
nl|'\n'
name|'hours'
op|'='
number|'42'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'4201'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'25'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant1'"
op|','
nl|'\n'
name|'flavor'
op|'='
string|"'m1.tiny'"
op|','
nl|'\n'
name|'started_at'
op|'='
name|'today'
op|','
nl|'\n'
name|'ended_at'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'state'
op|'='
string|"'terminated'"
op|','
nl|'\n'
name|'uptime'
op|'='
number|'43200'
op|')'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant2'"
op|','
nl|'\n'
name|'total_local_gb_usage'
op|'='
number|'512'
op|','
nl|'\n'
name|'total_vcpus_usage'
op|'='
number|'32'
op|','
nl|'\n'
name|'total_memory_mb_usage'
op|'='
number|'1024'
op|','
nl|'\n'
name|'total_hours'
op|'='
number|'42'
op|','
nl|'\n'
name|'start'
op|'='
name|'today'
op|','
nl|'\n'
name|'stop'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'server_usages'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
string|"'00000000-0000-0000-0000-0000000000000003'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'test3'"
op|','
nl|'\n'
name|'hours'
op|'='
number|'24'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'50'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'2'
op|','
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant2'"
op|','
nl|'\n'
name|'flavor'
op|'='
string|"'m1.small'"
op|','
nl|'\n'
name|'started_at'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'ended_at'
op|'='
name|'today'
op|','
nl|'\n'
name|'state'
op|'='
string|"'terminated'"
op|','
nl|'\n'
name|'uptime'
op|'='
number|'86400'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
string|"'00000000-0000-0000-0000-0000000000000002'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'test2'"
op|','
nl|'\n'
name|'hours'
op|'='
number|'42'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'4201'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'25'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'tenant_id'
op|'='
string|"'tenant4'"
op|','
nl|'\n'
name|'flavor'
op|'='
string|"'m1.tiny'"
op|','
nl|'\n'
name|'started_at'
op|'='
name|'today'
op|','
nl|'\n'
name|'ended_at'
op|'='
name|'yesterday'
op|','
nl|'\n'
name|'state'
op|'='
string|"'terminated'"
op|','
nl|'\n'
name|'uptime'
op|'='
number|'43200'
op|')'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'tenant_usages'
op|'='
name|'dict'
op|'('
name|'tenant_usages'
op|'='
name|'raw_usages'
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'tenant_usages'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'tenant_usages'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'raw_usages'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'idx'
op|','
name|'child'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_verify_tenant_usage'
op|'('
name|'raw_usages'
op|'['
name|'idx'
op|']'
op|','
name|'child'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsageControllerTest
dedent|''
dedent|''
dedent|''
name|'class'
name|'SimpleTenantUsageControllerTest'
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
name|'SimpleTenantUsageControllerTest'
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
name|'controller'
op|'='
name|'simple_tenant_usage'
op|'.'
name|'SimpleTenantUsageController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeComputeAPI
name|'class'
name|'FakeComputeAPI'
op|':'
newline|'\n'
DECL|member|get_instance_type
indent|'            '
name|'def'
name|'get_instance_type'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'flavor_type'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'flavor_type'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
op|'('
name|'flavor_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'FakeComputeAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'baseinst'
op|'='
name|'dict'
op|'('
name|'display_name'
op|'='
string|"'foo'"
op|','
nl|'\n'
name|'launched_at'
op|'='
name|'now'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'terminated_at'
op|'='
name|'now'
op|','
nl|'\n'
name|'instance_type_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'vm_state'
op|'='
string|"'deleted'"
op|','
nl|'\n'
name|'deleted'
op|'='
number|'0'
op|')'
newline|'\n'
name|'basetype'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'dict_to_metadata'
op|'('
nl|'\n'
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
op|'{'
op|'}'
op|','
name|'basetype'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'baseinst'
op|'['
string|"'system_metadata'"
op|']'
op|'='
name|'sys_meta'
newline|'\n'
name|'self'
op|'.'
name|'basetype'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'self'
op|'.'
name|'baseinst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_from_sys_meta
dedent|''
name|'def'
name|'test_get_flavor_from_sys_meta'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Non-deleted instances get their type information from their'
nl|'\n'
comment|'# system_metadata'
nl|'\n'
indent|'        '
name|'flavor'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_flavor'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'compute_api'
op|','
nl|'\n'
name|'self'
op|'.'
name|'baseinst'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|','
name|'self'
op|'.'
name|'basetype'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_from_non_deleted_with_id_fails
dedent|''
name|'def'
name|'test_get_flavor_from_non_deleted_with_id_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# If an instance is not deleted and missing type information from'
nl|'\n'
comment|"# system_metadata, then that's a bug"
nl|'\n'
indent|'        '
name|'inst_without_sys_meta'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'baseinst'
op|','
name|'system_metadata'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'KeyError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_flavor'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|','
name|'inst_without_sys_meta'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_from_deleted_with_id
dedent|''
name|'def'
name|'test_get_flavor_from_deleted_with_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Deleted instances may not have type info in system_metadata,'
nl|'\n'
comment|'# so verify that they get their type from a lookup of their'
nl|'\n'
comment|'# instance_type_id'
nl|'\n'
indent|'        '
name|'inst_without_sys_meta'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'baseinst'
op|','
name|'system_metadata'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'deleted'
op|'='
number|'1'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_flavor'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'compute_api'
op|','
nl|'\n'
name|'inst_without_sys_meta'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|','
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_from_deleted_with_id_of_deleted
dedent|''
name|'def'
name|'test_get_flavor_from_deleted_with_id_of_deleted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Verify the legacy behavior of instance_type_id pointing to a'
nl|'\n'
comment|'# missing type being non-fatal'
nl|'\n'
indent|'        '
name|'inst_without_sys_meta'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'baseinst'
op|','
name|'system_metadata'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'deleted'
op|'='
number|'1'
op|','
name|'instance_type_id'
op|'='
number|'2'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_flavor'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'compute_api'
op|','
nl|'\n'
name|'inst_without_sys_meta'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
