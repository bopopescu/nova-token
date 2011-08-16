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
name|'json'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
name|'as'
name|'auth_manager'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
op|'.'
name|'quotas'
name|'import'
name|'QuotasController'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_set
name|'def'
name|'quota_set'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'quota_set'"
op|':'
op|'{'
string|"'id'"
op|':'
name|'id'
op|','
string|"'metadata_items'"
op|':'
number|'128'
op|','
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|','
string|"'injected_files'"
op|':'
number|'5'
op|','
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_set_list
dedent|''
name|'def'
name|'quota_set_list'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'quota_set_list'"
op|':'
op|'['
name|'quota_set'
op|'('
string|"'1234'"
op|')'
op|','
name|'quota_set'
op|'('
string|"'5678'"
op|')'
op|','
nl|'\n'
name|'quota_set'
op|'('
string|"'update_me'"
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_project
dedent|''
name|'def'
name|'create_project'
op|'('
name|'project_name'
op|','
name|'manager_user'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'create_project'
op|'('
name|'project_name'
op|','
name|'manager_user'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_project
dedent|''
name|'def'
name|'delete_project'
op|'('
name|'project_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_project'
op|'('
name|'project_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_admin_user
dedent|''
name|'def'
name|'create_admin_user'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'create_user'
op|'('
name|'name'
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_user
dedent|''
name|'def'
name|'delete_user'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_user'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotasTest
dedent|''
name|'class'
name|'QuotasTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'QuotasTest'
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
name|'QuotasController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'create_admin_user'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'create_project'
op|'('
string|"'1234'"
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'create_project'
op|'('
string|"'5678'"
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'create_project'
op|'('
string|"'update_me'"
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'delete_project'
op|'('
string|"'1234'"
op|')'
newline|'\n'
name|'delete_project'
op|'('
string|"'5678'"
op|')'
newline|'\n'
name|'delete_project'
op|'('
string|"'update_me'"
op|')'
newline|'\n'
name|'delete_user'
op|'('
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_quota_set
dedent|''
name|'def'
name|'test_format_quota_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raw_quota_set'
op|'='
op|'{'
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
nl|'\n'
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'quota_set'
op|'='
name|'QuotasController'
op|'('
op|')'
op|'.'
name|'_format_quota_set'
op|'('
string|"'1234'"
op|','
name|'raw_quota_set'
op|')'
newline|'\n'
name|'quota_set_check'
op|'='
name|'quota_set'
op|'['
string|"'quota_set'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'id'"
op|']'
op|','
string|"'1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'instances'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'cores'"
op|']'
op|','
number|'20'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'ram'"
op|']'
op|','
number|'51200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'volumes'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'gigabytes'"
op|']'
op|','
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'floating_ips'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'metadata_items'"
op|']'
op|','
number|'128'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'injected_files'"
op|']'
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'quota_set_check'
op|'['
string|"'injected_file_content_bytes'"
op|']'
op|','
number|'10240'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_index_with_default_param
dedent|''
name|'def'
name|'test_quotas_index_with_default_param'
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
string|"'/v1.1/os-quotas?defaults=True'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
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
name|'expected'
op|'='
op|'{'
string|"'quota_set_list'"
op|':'
op|'['
op|'{'
string|"'quota_set'"
op|':'
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'__defaults__'"
op|','
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
nl|'\n'
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_index
dedent|''
name|'def'
name|'test_quotas_index'
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
string|"'/v1.1/os-quotas'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
name|'quota_set_list'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_show
dedent|''
name|'def'
name|'test_quotas_show'
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
string|"'/v1.1/os-quotas/1234'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
name|'quota_set'
op|'('
string|"'1234'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update
dedent|''
name|'def'
name|'test_quotas_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updated_quota_set'
op|'='
op|'{'
string|"'quota_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'50'
op|','
nl|'\n'
string|"'cores'"
op|':'
number|'50'
op|','
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/os-quotas/update_me'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'updated_quota_set'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'fake_auth_context'
op|'='
nl|'\n'
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
name|'updated_quota_set'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
