begin_unit
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
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
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
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
nl|'\n'
DECL|variable|UUID1
name|'UUID1'
op|'='
string|"'00000000-0000-0000-0000-000000000001'"
newline|'\n'
DECL|variable|UUID2
name|'UUID2'
op|'='
string|"'00000000-0000-0000-0000-000000000002'"
newline|'\n'
DECL|variable|UUID3
name|'UUID3'
op|'='
string|"'00000000-0000-0000-0000-000000000003'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get
name|'def'
name|'fake_compute_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'inst'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
name|'uuid'
op|'='
name|'UUID3'
op|','
name|'task_state'
op|'='
string|'"kayaking"'
op|','
nl|'\n'
name|'vm_state'
op|'='
string|'"slightly crunchy"'
op|','
name|'power_state'
op|'='
number|'1'
op|')'
newline|'\n'
name|'return'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'args'
op|'['
number|'1'
op|']'
op|','
op|'**'
name|'inst'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get_all
dedent|''
name|'def'
name|'fake_compute_get_all'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'db_list'
op|'='
op|'['
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
name|'uuid'
op|'='
name|'UUID1'
op|','
name|'task_state'
op|'='
string|'"task-1"'
op|','
nl|'\n'
name|'vm_state'
op|'='
string|'"vm-1"'
op|','
name|'power_state'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'2'
op|','
name|'uuid'
op|'='
name|'UUID2'
op|','
name|'task_state'
op|'='
string|'"task-2"'
op|','
nl|'\n'
name|'vm_state'
op|'='
string|'"vm-2"'
op|','
name|'power_state'
op|'='
number|'2'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'fields'
op|'='
name|'instance_obj'
op|'.'
name|'INSTANCE_DEFAULT_FIELDS'
newline|'\n'
name|'return'
name|'instance_obj'
op|'.'
name|'_make_instance_list'
op|'('
name|'args'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceList'
op|'('
op|')'
op|','
nl|'\n'
name|'db_list'
op|','
name|'fields'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedStatusTestV21
dedent|''
name|'class'
name|'ExtendedStatusTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
DECL|variable|prefix
name|'prefix'
op|'='
string|"'OS-EXT-STS:'"
newline|'\n'
DECL|variable|fake_url
name|'fake_url'
op|'='
string|"'/v2/fake'"
newline|'\n'
nl|'\n'
DECL|member|_set_flags
name|'def'
name|'_set_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_make_request
dedent|''
name|'def'
name|'_make_request'
op|'('
name|'self'
op|','
name|'url'
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
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
name|'self'
op|'.'
name|'content_type'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
nl|'\n'
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
nl|'\n'
string|"'os-extended-status'"
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ExtendedStatusTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get_all'"
op|','
name|'fake_compute_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_flags'
op|'('
op|')'
newline|'\n'
name|'return_server'
op|'='
name|'fakes'
op|'.'
name|'fake_instance_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_get_by_uuid'"
op|','
name|'return_server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_server
dedent|''
name|'def'
name|'_get_server'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'server'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_servers
dedent|''
name|'def'
name|'_get_servers'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'servers'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertServerStates
dedent|''
name|'def'
name|'assertServerStates'
op|'('
name|'self'
op|','
name|'server'
op|','
name|'vm_state'
op|','
name|'power_state'
op|','
name|'task_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'server'
op|'.'
name|'get'
op|'('
string|"'%svm_state'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|','
name|'vm_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'server'
op|'.'
name|'get'
op|'('
string|"'%spower_state'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|')'
op|','
nl|'\n'
name|'power_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'server'
op|'.'
name|'get'
op|'('
string|"'%stask_state'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|','
name|'task_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
name|'self'
op|'.'
name|'fake_url'
op|'+'
string|"'/servers/%s'"
op|'%'
name|'UUID3'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
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
name|'assertServerStates'
op|'('
name|'self'
op|'.'
name|'_get_server'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
nl|'\n'
name|'vm_state'
op|'='
string|"'slightly crunchy'"
op|','
nl|'\n'
name|'power_state'
op|'='
number|'1'
op|','
nl|'\n'
name|'task_state'
op|'='
string|"'kayaking'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
name|'self'
op|'.'
name|'fake_url'
op|'+'
string|"'/servers/detail'"
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
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
name|'for'
name|'i'
op|','
name|'server'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_servers'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertServerStates'
op|'('
name|'server'
op|','
nl|'\n'
name|'vm_state'
op|'='
string|"'vm-%s'"
op|'%'
op|'('
name|'i'
op|'+'
number|'1'
op|')'
op|','
nl|'\n'
name|'power_state'
op|'='
op|'('
name|'i'
op|'+'
number|'1'
op|')'
op|','
nl|'\n'
name|'task_state'
op|'='
string|"'task-%s'"
op|'%'
op|'('
name|'i'
op|'+'
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_instance_passthrough_404
dedent|''
dedent|''
name|'def'
name|'test_no_instance_passthrough_404'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_compute_get
indent|'        '
name|'def'
name|'fake_compute_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'fake_url'
op|'+'
string|"'/servers/70f6db34-de8d-4fbd-aafb-4065bdfa6115'"
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedStatusTestV2
dedent|''
dedent|''
name|'class'
name|'ExtendedStatusTestV2'
op|'('
name|'ExtendedStatusTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_set_flags
indent|'    '
name|'def'
name|'_set_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'Extended_status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_request
dedent|''
name|'def'
name|'_make_request'
op|'('
name|'self'
op|','
name|'url'
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
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
name|'self'
op|'.'
name|'content_type'
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
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
