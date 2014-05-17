begin_unit
comment|'# Copyright 2013 Nebula, Inc.'
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
name|'contrib'
name|'import'
name|'extended_ips'
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
name|'import'
name|'compute'
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
DECL|variable|NW_CACHE
name|'NW_CACHE'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|"'aa:aa:aa:aa:aa:aa'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'network'"
op|':'
op|'{'
nl|'\n'
string|"'bridge'"
op|':'
string|"'br0'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'private'"
op|','
nl|'\n'
string|"'subnets'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.1.0/24'"
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.1.100'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'fixed'"
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'5.0.0.1'"
op|','
string|"'type'"
op|':'
string|"'floating'"
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|"'bb:bb:bb:bb:bb:bb'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'network'"
op|':'
op|'{'
nl|'\n'
string|"'bridge'"
op|':'
string|"'br1'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'public'"
op|','
nl|'\n'
string|"'subnets'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'cidr'"
op|':'
string|"'10.0.0.0/24'"
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|"'10.0.0.100'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'fixed'"
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'5.0.0.2'"
op|','
string|"'type'"
op|':'
string|"'floating'"
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|']'
newline|'\n'
DECL|variable|ALL_IPS
name|'ALL_IPS'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'cache'
name|'in'
name|'NW_CACHE'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'subnet'
name|'in'
name|'cache'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'fixed'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
DECL|variable|sanitized
indent|'            '
name|'sanitized'
op|'='
name|'dict'
op|'('
name|'fixed'
op|')'
newline|'\n'
name|'sanitized'
op|'.'
name|'pop'
op|'('
string|"'floating_ips'"
op|')'
newline|'\n'
name|'ALL_IPS'
op|'.'
name|'append'
op|'('
name|'sanitized'
op|')'
newline|'\n'
name|'for'
name|'floating'
name|'in'
name|'fixed'
op|'['
string|"'floating_ips'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'ALL_IPS'
op|'.'
name|'append'
op|'('
name|'floating'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'ALL_IPS'
op|'.'
name|'sort'
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
name|'nw_cache'
op|'='
name|'NW_CACHE'
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
name|'nw_cache'
op|'='
name|'NW_CACHE'
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
name|'nw_cache'
op|'='
name|'NW_CACHE'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
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
DECL|class|ExtendedIpsTest
dedent|''
name|'class'
name|'ExtendedIpsTest'
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
string|"'OS-EXT-IPS:'"
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
name|'ExtendedIpsTest'
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
string|"'Extended_ips'"
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
DECL|member|_get_ips
dedent|''
name|'def'
name|'_get_ips'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'network'
name|'in'
name|'server'
op|'['
string|"'addresses'"
op|']'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ip'
name|'in'
name|'network'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'ip'
newline|'\n'
nl|'\n'
DECL|member|assertServerStates
dedent|''
dedent|''
dedent|''
name|'def'
name|'assertServerStates'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'results'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'.'
name|'_get_ips'
op|'('
name|'server'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'results'
op|'.'
name|'append'
op|'('
op|'{'
string|"'address'"
op|':'
name|'ip'
op|'.'
name|'get'
op|'('
string|"'addr'"
op|')'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'ip'
op|'.'
name|'get'
op|'('
string|"'%stype'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ALL_IPS'
op|','
name|'sorted'
op|'('
name|'results'
op|')'
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
string|"'/v2/fake/servers/%s'"
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
string|"'/v2/fake/servers/detail'"
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedIpsXmlTest
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExtendedIpsXmlTest'
op|'('
name|'ExtendedIpsTest'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/xml'"
newline|'\n'
DECL|variable|prefix
name|'prefix'
op|'='
string|"'{%s}'"
op|'%'
name|'extended_ips'
op|'.'
name|'Extended_ips'
op|'.'
name|'namespace'
newline|'\n'
nl|'\n'
DECL|member|_get_server
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
name|'etree'
op|'.'
name|'XML'
op|'('
name|'body'
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
DECL|member|_get_ips
dedent|''
name|'def'
name|'_get_ips'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'network'
name|'in'
name|'server'
op|'.'
name|'find'
op|'('
string|"'{%s}addresses'"
op|'%'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ip'
name|'in'
name|'network'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'ip'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
