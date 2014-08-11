begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2012 Justin Santa Barbara'
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
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'import'
name|'plugins'
newline|'\n'
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
name|'security_groups'
newline|'\n'
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
name|'servers'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
op|'.'
name|'tests'
name|'import'
name|'fake_instance'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
newline|'\n'
DECL|variable|FAKE_UUID1
name|'FAKE_UUID1'
op|'='
string|"'a47ae74e-ab08-447f-8eee-ffd43fc46c16'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_gen_uuid
name|'def'
name|'fake_gen_uuid'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FAKE_UUID'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_security_group
dedent|''
name|'def'
name|'return_security_group'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|UUID1
dedent|''
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
DECL|function|fake_compute_get_all
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
name|'base'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'description'"
op|':'
string|"'foo'"
op|','
string|"'user_id'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'baz'"
op|','
string|"'deleted'"
op|':'
name|'False'
op|','
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
string|"'created_at'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'db_list'
op|'='
op|'['
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
nl|'\n'
number|'1'
op|','
name|'uuid'
op|'='
name|'UUID1'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
name|'dict'
op|'('
name|'base'
op|','
op|'**'
op|'{'
string|"'name'"
op|':'
string|"'fake-0-0'"
op|'}'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'base'
op|','
op|'**'
op|'{'
string|"'name'"
op|':'
string|"'fake-0-1'"
op|'}'
op|')'
op|']'
op|')'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
nl|'\n'
number|'2'
op|','
name|'uuid'
op|'='
name|'UUID2'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
name|'dict'
op|'('
name|'base'
op|','
op|'**'
op|'{'
string|"'name'"
op|':'
string|"'fake-1-0'"
op|'}'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'base'
op|','
op|'**'
op|'{'
string|"'name'"
op|':'
string|"'fake-1-1'"
op|'}'
op|')'
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
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
nl|'\n'
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|','
nl|'\n'
string|"'security_groups'"
op|','
string|"'info_cache'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get
dedent|''
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
nl|'\n'
name|'security_groups'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-2-0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'fake-2-1'"
op|'}'
op|']'
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
nl|'\n'
name|'expected_attrs'
op|'='
name|'instance_obj'
op|'.'
name|'INSTANCE_DEFAULT_FIELDS'
op|','
op|'**'
name|'inst'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_create
dedent|''
name|'def'
name|'fake_compute_create'
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
name|'return'
op|'('
op|'['
name|'fake_compute_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instance_security_groups
dedent|''
name|'def'
name|'fake_get_instance_security_groups'
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
name|'return'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instances_security_groups_bindings
dedent|''
name|'def'
name|'fake_get_instances_security_groups_bindings'
op|'('
name|'inst'
op|','
name|'context'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'groups'
op|'='
op|'{'
name|'UUID1'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-0-0'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'fake-0-1'"
op|'}'
op|']'
op|','
nl|'\n'
name|'UUID2'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-1-0'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'fake-1-1'"
op|'}'
op|']'
op|','
nl|'\n'
name|'UUID3'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-2-0'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'fake-2-1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
name|'server'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'groups'
op|'.'
name|'get'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupsOutputTest
dedent|''
name|'class'
name|'SecurityGroupsOutputTest'
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
nl|'\n'
DECL|member|setUp
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
name|'SecurityGroupsOutputTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'security_group_api'"
op|','
string|"'nova'"
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
op|'('
name|'self'
op|'.'
name|'stubs'
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
string|"'create'"
op|','
name|'fake_compute_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v3'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
nl|'\n'
string|"'os-security-groups'"
op|')'
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
op|','
name|'body'
op|'='
name|'None'
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
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'self'
op|'.'
name|'_encode_body'
op|'('
name|'body'
op|')'
newline|'\n'
dedent|''
name|'req'
op|'.'
name|'content_type'
op|'='
name|'self'
op|'.'
name|'content_type'
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
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_encode_body
dedent|''
name|'def'
name|'_encode_body'
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
name|'dumps'
op|'('
name|'body'
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
DECL|member|_get_groups
dedent|''
name|'def'
name|'_get_groups'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'server'
op|'.'
name|'get'
op|'('
string|"'os-security-groups:security_groups'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'/v3/servers'"
newline|'\n'
name|'image_uuid'
op|'='
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
newline|'\n'
name|'server'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'image_ref'
op|'='
name|'image_uuid'
op|','
name|'flavor_ref'
op|'='
number|'2'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
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
number|'202'
op|')'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_get_server'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'group'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_groups'
op|'('
name|'server'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
string|"'fake-2-%s'"
op|'%'
name|'i'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
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
string|"'/v3/servers/%s'"
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
name|'server'
op|'='
name|'self'
op|'.'
name|'_get_server'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'group'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_groups'
op|'('
name|'server'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
string|"'fake-2-%s'"
op|'%'
name|'i'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
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
string|"'/v3/servers/detail'"
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
name|'for'
name|'j'
op|','
name|'group'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_groups'
op|'('
name|'server'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'name'
op|'='
string|"'fake-%s-%s'"
op|'%'
op|'('
name|'i'
op|','
name|'j'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_instance_passthrough_404
dedent|''
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
string|"'/v3/servers/70f6db34-de8d-4fbd-aafb-4065bdfa6115'"
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
DECL|class|ServersControllerCreateTest
dedent|''
dedent|''
name|'class'
name|'ServersControllerCreateTest'
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
string|'"""Shared implementation for tests below that create instance."""'
newline|'\n'
name|'super'
op|'('
name|'ServersControllerCreateTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|','
nl|'\n'
name|'enable_instance_password'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'ext_info'
op|'='
name|'plugins'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
string|"'os-security-groups'"
op|','
nl|'\n'
string|"'osapi_v3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'no_security_groups_controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|function|instance_create
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst_type'
op|'='
name|'flavors'
op|'.'
name|'get_flavor_by_flavor_id'
op|'('
number|'3'
op|')'
newline|'\n'
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'def_image_ref'
op|'='
string|"'http://localhost/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'+='
number|'1'
newline|'\n'
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|'**'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'instance_cache_num'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'inst'
op|'['
string|"'display_name'"
op|']'
name|'or'
string|"'test'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'dict'
op|'('
name|'inst_type'
op|')'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fead::1234'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'image_ref'"
op|','
name|'def_image_ref'
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"user_data"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"progress"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"task_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"root_device_name"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'root_device_name'"
op|','
string|"'vda'"
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Stub for compute/api create() pulling in instance after\n            scheduling\n            """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance_id'
op|']'
newline|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'uuid'
op|']'
newline|'\n'
name|'instance'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|server_update
dedent|''
name|'def'
name|'server_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance_uuid'
op|']'
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
op|'('
name|'inst'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_method
dedent|''
name|'def'
name|'fake_method'
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|project_get_networks
dedent|''
name|'def'
name|'project_get_networks'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
string|"'1'"
op|','
name|'host'
op|'='
string|"'localhost'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|queue_get_for
dedent|''
name|'def'
name|'queue_get_for'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'network_topic'"
newline|'\n'
nl|'\n'
dedent|''
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'uuid'
op|','
string|"'uuid4'"
op|','
name|'fake_gen_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_add_security_group'"
op|','
nl|'\n'
name|'return_security_group'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'project_get_networks'"
op|','
nl|'\n'
name|'project_get_networks'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_create'"
op|','
name|'instance_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_system_metadata_update'"
op|','
nl|'\n'
name|'fake_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get'"
op|','
name|'instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_update'"
op|','
name|'instance_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_update_and_get_original'"
op|','
nl|'\n'
name|'server_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'manager'
op|'.'
name|'VlanManager'
op|','
string|"'allocate_fixed_ip'"
op|','
nl|'\n'
name|'fake_method'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_extra
dedent|''
name|'def'
name|'_test_create_extra'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'False'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
newline|'\n'
name|'server'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'image_ref'
op|'='
name|'image_uuid'
op|','
name|'flavor_ref'
op|'='
number|'2'
op|')'
newline|'\n'
name|'if'
name|'no_image'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'.'
name|'pop'
op|'('
string|"'image_ref'"
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'server'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
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
name|'if'
name|'override_controller'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'override_controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_security_group_enabled
dedent|''
dedent|''
name|'def'
name|'test_create_instance_with_security_group_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
string|"'foo'"
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|sec_group_get
name|'def'
name|'sec_group_get'
op|'('
name|'ctx'
op|','
name|'proj'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
name|'group'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SecurityGroupNotFoundForProject'
op|'('
nl|'\n'
name|'project_id'
op|'='
name|'proj'
op|','
name|'security_group_id'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|function|create
dedent|''
dedent|''
name|'def'
name|'create'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'security_group'"
op|']'
op|','
op|'['
name|'group'
op|']'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
name|'sec_group_get'
op|')'
newline|'\n'
comment|'# negative test'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|','
nl|'\n'
op|'{'
name|'security_groups'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
nl|'\n'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'bogus'"
op|'}'
op|']'
op|'}'
op|')'
newline|'\n'
comment|'# positive test - extra assert in create path'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
op|'{'
name|'security_groups'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
nl|'\n'
op|'['
op|'{'
string|"'name'"
op|':'
name|'group'
op|'}'
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_security_group_disabled
dedent|''
name|'def'
name|'test_create_instance_with_security_group_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
string|"'foo'"
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'security_groups'"
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
name|'group'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): if the security groups extension is not'
nl|'\n'
comment|'#             enabled, then security groups passed in'
nl|'\n'
comment|'#             are ignored.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'security_group'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'self'
op|'.'
name|'no_security_groups_controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_invalid_key_security_group
dedent|''
name|'def'
name|'test_create_with_invalid_key_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
name|'security_groups'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
op|'['
op|'{'
string|"'invalid'"
op|':'
string|"'group'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|','
name|'param'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_no_string_value_security_group
dedent|''
name|'def'
name|'test_create_with_no_string_value_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
name|'security_groups'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
number|'12345'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|','
name|'param'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_too_long_value_security_group
dedent|''
name|'def'
name|'test_create_with_too_long_value_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
name|'security_groups'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
op|'('
string|"'a'"
op|'*'
number|'260'
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|','
name|'param'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
