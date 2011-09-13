begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'import'
name|'xml'
op|'.'
name|'dom'
op|'.'
name|'minidom'
name|'as'
name|'minidom'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'flavors'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_flavor
name|'def'
name|'stub_flavor'
op|'('
name|'flavorid'
op|','
name|'name'
op|','
name|'memory_mb'
op|'='
string|'"256"'
op|','
name|'local_gb'
op|'='
string|'"10"'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|'"flavorid"'
op|':'
name|'str'
op|'('
name|'flavorid'
op|')'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'name'
op|','
nl|'\n'
string|'"memory_mb"'
op|':'
name|'memory_mb'
op|','
nl|'\n'
string|'"local_gb"'
op|':'
name|'local_gb'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_instance_type_by_flavor_id
dedent|''
name|'def'
name|'return_instance_type_by_flavor_id'
op|'('
name|'context'
op|','
name|'flavorid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_flavor'
op|'('
name|'flavorid'
op|','
string|'"flavor %s"'
op|'%'
op|'('
name|'flavorid'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_instance_types
dedent|''
name|'def'
name|'return_instance_types'
op|'('
name|'context'
op|','
name|'num'
op|'='
number|'2'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_types'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
name|'num'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
string|'"flavor %s"'
op|'%'
op|'('
name|'i'
op|','
op|')'
newline|'\n'
name|'instance_types'
op|'['
name|'name'
op|']'
op|'='
name|'stub_flavor'
op|'('
name|'i'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_instance_type_not_found
dedent|''
name|'def'
name|'return_instance_type_not_found'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
op|'('
name|'flavor_id'
op|'='
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsTest
dedent|''
name|'class'
name|'FlavorsTest'
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
name|'FlavorsTest'
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
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|'"instance_type_get_all"'
op|','
nl|'\n'
name|'return_instance_types'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|'"instance_type_get_by_flavor_id"'
op|','
nl|'\n'
name|'return_instance_type_by_flavor_id'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'FlavorsTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_list_v1_0
dedent|''
name|'def'
name|'test_get_flavor_list_v1_0'
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
string|"'/v1.0/flavors'"
op|')'
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
name|'flavors'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|'"flavors"'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 1"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 2"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavors'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_empty_flavor_list_v1_0
dedent|''
name|'def'
name|'test_get_empty_flavor_list_v1_0'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_return_empty
indent|'        '
name|'def'
name|'_return_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|'"instance_type_get_all"'
op|','
nl|'\n'
name|'_return_empty'
op|')'
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
string|"'/v1.0/flavors'"
op|')'
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
name|'flavors'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|'"flavors"'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavors'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_list_detail_v1_0
dedent|''
name|'def'
name|'test_get_flavor_list_detail_v1_0'
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
string|"'/v1.0/flavors/detail'"
op|')'
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
name|'flavors'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|'"flavors"'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 1"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"rxtx_cap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"rxtx_quota"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"swap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
string|'""'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 2"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"rxtx_cap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"rxtx_quota"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"swap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
string|'""'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavors'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_by_id_v1_0
dedent|''
name|'def'
name|'test_get_flavor_by_id_v1_0'
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
string|"'/v1.0/flavors/12'"
op|')'
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
name|'flavor'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|'"flavor"'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"12"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 12"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"rxtx_cap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"rxtx_quota"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"swap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
string|'""'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_by_invalid_id
dedent|''
name|'def'
name|'test_get_flavor_by_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|'"instance_type_get_by_flavor_id"'
op|','
nl|'\n'
name|'return_instance_type_not_found'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/flavors/asdf'"
op|')'
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
DECL|member|test_get_flavor_by_id_v1_1
dedent|''
name|'def'
name|'test_get_flavor_by_id_v1_1'
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
string|"'/v1.1/fake/flavors/12'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
name|'flavor'
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
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"12"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 12"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"rxtx_cap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"rxtx_quota"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"swap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/12"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/12"'
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
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_list_v1_1
dedent|''
name|'def'
name|'test_get_flavor_list_v1_1'
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
string|"'/v1.1/fake/flavors'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
name|'flavor'
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
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"flavors"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 1"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/1"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/1"'
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
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 2"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/2"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/2"'
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
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_flavor_list_detail_v1_1
dedent|''
name|'def'
name|'test_get_flavor_list_detail_v1_1'
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
string|"'/v1.1/fake/flavors/detail'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
name|'flavor'
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
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"flavors"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 1"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"rxtx_cap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"rxtx_quota"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"swap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/1"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/1"'
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
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 2"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"rxtx_cap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"rxtx_quota"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"swap"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/2"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/2"'
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
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_empty_flavor_list_v1_1
dedent|''
name|'def'
name|'test_get_empty_flavor_list_v1_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_return_empty
indent|'        '
name|'def'
name|'_return_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|'"instance_type_get_all"'
op|','
name|'_return_empty'
op|')'
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
string|"'/v1.1/fake/flavors'"
op|')'
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
name|'flavors'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|'"flavors"'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavors'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsXMLSerializationTest
dedent|''
dedent|''
name|'class'
name|'FlavorsXMLSerializationTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_show
indent|'    '
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'flavors'
op|'.'
name|'FlavorXMLSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"12"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"asdf"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/12"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/12"'
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
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'input'
op|','
string|"'show'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n        <flavor xmlns="http://docs.openstack.org/compute/api/v1.1"\n                xmlns:atom="http://www.w3.org/2005/Atom"\n                id="12"\n                name="asdf"\n                ram="256"\n                disk="10">\n            <atom:link href="http://localhost/v1.1/fake/flavors/12"\n                 rel="self"/>\n            <atom:link href="http://localhost/fake/flavors/12"\n                 rel="bookmark"/>\n        </flavor>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_handles_integers
dedent|''
name|'def'
name|'test_show_handles_integers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'flavors'
op|'.'
name|'FlavorXMLSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'12'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"asdf"'
op|','
nl|'\n'
string|'"ram"'
op|':'
number|'256'
op|','
nl|'\n'
string|'"disk"'
op|':'
number|'10'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/12"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/12"'
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
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'input'
op|','
string|"'show'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n        <flavor xmlns="http://docs.openstack.org/compute/api/v1.1"\n                xmlns:atom="http://www.w3.org/2005/Atom"\n                id="12"\n                name="asdf"\n                ram="256"\n                disk="10">\n            <atom:link href="http://localhost/v1.1/fake/flavors/12"\n                 rel="self"/>\n            <atom:link href="http://localhost/fake/flavors/12"\n                 rel="bookmark"/>\n        </flavor>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
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
name|'serializer'
op|'='
name|'flavors'
op|'.'
name|'FlavorXMLSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
nl|'\n'
string|'"flavors"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"23"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 23"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"512"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"20"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/23"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/23"'
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
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"13"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 13"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/13"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/13"'
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
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'input'
op|','
string|"'detail'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n        <flavors xmlns="http://docs.openstack.org/compute/api/v1.1"\n                 xmlns:atom="http://www.w3.org/2005/Atom">\n            <flavor id="23"\n                    name="flavor 23"\n                    ram="512"\n                    disk="20">\n                <atom:link href="http://localhost/v1.1/fake/flavors/23"\n                     rel="self"/>\n                <atom:link href="http://localhost/fake/flavors/23"\n                     rel="bookmark"/>\n            </flavor>\n            <flavor id="13"\n                    name="flavor 13"\n                    ram="256"\n                    disk="10">\n                <atom:link href="http://localhost/v1.1/fake/flavors/13"\n                     rel="self"/>\n                <atom:link href="http://localhost/fake/flavors/13"\n                     rel="bookmark"/>\n            </flavor>\n        </flavors>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'flavors'
op|'.'
name|'FlavorXMLSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
nl|'\n'
string|'"flavors"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"23"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 23"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"512"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"20"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/23"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/23"'
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
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"13"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"flavor 13"'
op|','
nl|'\n'
string|'"ram"'
op|':'
string|'"256"'
op|','
nl|'\n'
string|'"disk"'
op|':'
string|'"10"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/fake/flavors/13"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/fake/flavors/13"'
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
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'input'
op|','
string|"'index'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n        <flavors xmlns="http://docs.openstack.org/compute/api/v1.1"\n                 xmlns:atom="http://www.w3.org/2005/Atom">\n            <flavor id="23" name="flavor 23">\n                <atom:link href="http://localhost/v1.1/fake/flavors/23"\n                     rel="self"/>\n                <atom:link href="http://localhost/fake/flavors/23"\n                     rel="bookmark"/>\n            </flavor>\n            <flavor id="13" name="flavor 13">\n                <atom:link href="http://localhost/v1.1/fake/flavors/13"\n                     rel="self"/>\n                <atom:link href="http://localhost/fake/flavors/13"\n                     rel="bookmark"/>\n            </flavor>\n        </flavors>\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_empty
dedent|''
name|'def'
name|'test_index_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'flavors'
op|'.'
name|'FlavorXMLSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
nl|'\n'
string|'"flavors"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'input'
op|','
string|"'index'"
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'output'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
string|'"""\n        <flavors xmlns="http://docs.openstack.org/compute/api/v1.1"\n                 xmlns:atom="http://www.w3.org/2005/Atom" />\n        """'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
