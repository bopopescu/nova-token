begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
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
name|'compute'
name|'import'
name|'flavors'
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
nl|'\n'
DECL|variable|FAKE_FLAVORS
name|'FAKE_FLAVORS'
op|'='
op|'{'
nl|'\n'
string|"'flavor 1'"
op|':'
op|'{'
nl|'\n'
string|'"flavorid"'
op|':'
string|"'1'"
op|','
nl|'\n'
string|'"name"'
op|':'
string|"'flavor 1'"
op|','
nl|'\n'
string|'"memory_mb"'
op|':'
string|"'256'"
op|','
nl|'\n'
string|'"root_gb"'
op|':'
string|"'10'"
op|','
nl|'\n'
string|'"rxtx_factor"'
op|':'
string|"'1.0'"
op|','
nl|'\n'
string|'"swap"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"ephemeral_gb"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"disabled"'
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'flavor 2'"
op|':'
op|'{'
nl|'\n'
string|'"flavorid"'
op|':'
string|"'2'"
op|','
nl|'\n'
string|'"name"'
op|':'
string|"'flavor 2'"
op|','
nl|'\n'
string|'"memory_mb"'
op|':'
string|"'512'"
op|','
nl|'\n'
string|'"root_gb"'
op|':'
string|"'10'"
op|','
nl|'\n'
string|'"rxtx_factor"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"swap"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"ephemeral_gb"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"disabled"'
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_flavor_get_by_flavor_id
name|'def'
name|'fake_flavor_get_by_flavor_id'
op|'('
name|'flavorid'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FAKE_FLAVORS'
op|'['
string|"'flavor %s'"
op|'%'
name|'flavorid'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_all_flavors_sorted_list
dedent|''
name|'def'
name|'fake_get_all_flavors_sorted_list'
op|'('
name|'context'
op|'='
name|'None'
op|','
name|'inactive'
op|'='
name|'False'
op|','
nl|'\n'
name|'filters'
op|'='
name|'None'
op|','
name|'sort_key'
op|'='
string|"'flavorid'"
op|','
nl|'\n'
name|'sort_dir'
op|'='
string|"'asc'"
op|','
name|'limit'
op|'='
name|'None'
op|','
name|'marker'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
name|'fake_flavor_get_by_flavor_id'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'fake_flavor_get_by_flavor_id'
op|'('
number|'2'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorRxtxTest
dedent|''
name|'class'
name|'FlavorRxtxTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
string|"''"
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
name|'FlavorRxtxTest'
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
name|'flavors'
op|','
string|'"get_all_flavors_sorted_list"'
op|','
nl|'\n'
name|'fake_get_all_flavors_sorted_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'flavors'
op|','
nl|'\n'
string|'"get_flavor_by_flavor_id"'
op|','
nl|'\n'
name|'fake_flavor_get_by_flavor_id'
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
string|"'flavors'"
op|','
nl|'\n'
string|"'os-flavor-rxtx'"
op|')'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_get_flavor
dedent|''
name|'def'
name|'_get_flavor'
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
string|"'flavor'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flavors
dedent|''
name|'def'
name|'_get_flavors'
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
string|"'flavors'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertFlavorRxtx
dedent|''
name|'def'
name|'assertFlavorRxtx'
op|'('
name|'self'
op|','
name|'flavor'
op|','
name|'rxtx'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'flavor'
op|'.'
name|'get'
op|'('
string|"'rxtx_factor'"
op|')'
op|')'
op|','
name|'rxtx'
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
string|"'/v3/flavors/1'"
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
name|'assertFlavorRxtx'
op|'('
name|'self'
op|'.'
name|'_get_flavor'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
string|"'1.0'"
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
string|"'/v3/flavors/detail'"
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
name|'flavors'
op|'='
name|'self'
op|'.'
name|'_get_flavors'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFlavorRxtx'
op|'('
name|'flavors'
op|'['
number|'0'
op|']'
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFlavorRxtx'
op|'('
name|'flavors'
op|'['
number|'1'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorRxtxXmlTest
dedent|''
dedent|''
name|'class'
name|'FlavorRxtxXmlTest'
op|'('
name|'FlavorRxtxTest'
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
DECL|member|_get_flavor
name|'def'
name|'_get_flavor'
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
DECL|member|_get_flavors
dedent|''
name|'def'
name|'_get_flavors'
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
dedent|''
dedent|''
endmarker|''
end_unit
