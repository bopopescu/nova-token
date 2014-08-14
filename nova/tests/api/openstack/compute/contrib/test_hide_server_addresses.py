begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'itertools'
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
name|'import'
name|'wsgi'
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
name|'vm_states'
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
nl|'\n'
nl|'\n'
DECL|variable|SENTINEL
name|'SENTINEL'
op|'='
name|'object'
op|'('
op|')'
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
DECL|function|_return_server
indent|'    '
name|'def'
name|'_return_server'
op|'('
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'_args'
op|'['
number|'1'
op|']'
op|','
op|'**'
name|'inst'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_return_server'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HideServerAddressesTestV21
dedent|''
name|'class'
name|'HideServerAddressesTestV21'
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
DECL|variable|base_url
name|'base_url'
op|'='
string|"'/v3/servers'"
newline|'\n'
nl|'\n'
DECL|member|_setup_wsgi
name|'def'
name|'_setup_wsgi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'wsgi_app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v3'
op|'('
nl|'\n'
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
string|"'os-hide-server-addresses'"
op|')'
op|')'
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
name|'HideServerAddressesTestV21'
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
op|'.'
name|'stubs'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_wsgi'
op|'('
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
name|'self'
op|'.'
name|'wsgi_app'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_server
name|'def'
name|'_get_server'
op|'('
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
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_servers
name|'def'
name|'_get_servers'
op|'('
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
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_addresses
name|'def'
name|'_get_addresses'
op|'('
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
string|"'addresses'"
op|','
name|'SENTINEL'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_addresses
dedent|''
name|'def'
name|'_check_addresses'
op|'('
name|'self'
op|','
name|'addresses'
op|','
name|'exists'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'addresses'
name|'is'
name|'not'
name|'SENTINEL'
op|')'
newline|'\n'
name|'if'
name|'exists'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'addresses'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'addresses'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_hides_in_building
dedent|''
dedent|''
name|'def'
name|'test_show_hides_in_building'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
number|'1'
newline|'\n'
name|'uuid'
op|'='
name|'fakes'
op|'.'
name|'get_fake_uuid'
op|'('
name|'instance_id'
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
nl|'\n'
name|'fake_compute_get'
op|'('
name|'instance_id'
op|','
name|'uuid'
op|'='
name|'uuid'
op|','
nl|'\n'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'BUILDING'
op|')'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'/%s'"
op|'%'
name|'uuid'
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
nl|'\n'
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
name|'addresses'
op|'='
name|'self'
op|'.'
name|'_get_addresses'
op|'('
name|'server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_addresses'
op|'('
name|'addresses'
op|','
name|'exists'
op|'='
name|'False'
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
name|'instance_id'
op|'='
number|'1'
newline|'\n'
name|'uuid'
op|'='
name|'fakes'
op|'.'
name|'get_fake_uuid'
op|'('
name|'instance_id'
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
nl|'\n'
name|'fake_compute_get'
op|'('
name|'instance_id'
op|','
name|'uuid'
op|'='
name|'uuid'
op|','
nl|'\n'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'/%s'"
op|'%'
name|'uuid'
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
nl|'\n'
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
name|'addresses'
op|'='
name|'self'
op|'.'
name|'_get_addresses'
op|'('
name|'server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_addresses'
op|'('
name|'addresses'
op|','
name|'exists'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_hides_building_server_addresses
dedent|''
name|'def'
name|'test_detail_hides_building_server_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_0'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'0'
op|','
name|'uuid'
op|'='
name|'fakes'
op|'.'
name|'get_fake_uuid'
op|'('
number|'0'
op|')'
op|','
nl|'\n'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
name|'instance_1'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
name|'uuid'
op|'='
name|'fakes'
op|'.'
name|'get_fake_uuid'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'BUILDING'
op|')'
newline|'\n'
name|'instances'
op|'='
op|'['
name|'instance_0'
op|','
name|'instance_1'
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_all
name|'def'
name|'get_all'
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
nl|'\n'
name|'args'
op|'['
number|'1'
op|']'
op|','
name|'objects'
op|'.'
name|'InstanceList'
op|'('
op|')'
op|','
name|'instances'
op|','
name|'fields'
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
string|"'get_all'"
op|','
name|'get_all'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'/detail'"
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
name|'servers'
op|'='
name|'self'
op|'.'
name|'_get_servers'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'servers'
op|')'
op|','
name|'len'
op|'('
name|'instances'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'instance'
op|','
name|'server'
name|'in'
name|'itertools'
op|'.'
name|'izip'
op|'('
name|'instances'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'addresses'
op|'='
name|'self'
op|'.'
name|'_get_addresses'
op|'('
name|'server'
op|')'
newline|'\n'
name|'exists'
op|'='
op|'('
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|'=='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_addresses'
op|'('
name|'addresses'
op|','
name|'exists'
op|'='
name|'exists'
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
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'/'"
op|'+'
name|'fakes'
op|'.'
name|'get_fake_uuid'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HideServerAddressesTestV2
dedent|''
dedent|''
name|'class'
name|'HideServerAddressesTestV2'
op|'('
name|'HideServerAddressesTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|base_url
indent|'    '
name|'base_url'
op|'='
string|"'/v2/fake/servers'"
newline|'\n'
nl|'\n'
DECL|member|_setup_wsgi
name|'def'
name|'_setup_wsgi'
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
string|"'Hide_server_addresses'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'wsgi_app'
op|'='
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
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HideAddressesXmlTest
dedent|''
dedent|''
name|'class'
name|'HideAddressesXmlTest'
op|'('
name|'HideServerAddressesTestV2'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/xml'"
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_server
name|'def'
name|'_get_server'
op|'('
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'etree'
op|'.'
name|'XML'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_servers
name|'def'
name|'_get_servers'
op|'('
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'etree'
op|'.'
name|'XML'
op|'('
name|'body'
op|')'
op|'.'
name|'getchildren'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_addresses
name|'def'
name|'_get_addresses'
op|'('
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'addresses'
op|'='
name|'server'
op|'.'
name|'find'
op|'('
string|"'{%s}addresses'"
op|'%'
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|')'
newline|'\n'
name|'if'
name|'addresses'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'SENTINEL'
newline|'\n'
dedent|''
name|'return'
name|'addresses'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
