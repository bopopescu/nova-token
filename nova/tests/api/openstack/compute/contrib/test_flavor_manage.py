begin_unit
comment|'# Copyright 2011 Andrew Bogott for the Wikimedia Foundation'
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
name|'flavor_access'
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
name|'contrib'
name|'import'
name|'flavormanage'
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
nl|'\n'
DECL|function|fake_get_flavor_by_flavor_id
name|'def'
name|'fake_get_flavor_by_flavor_id'
op|'('
name|'flavorid'
op|','
name|'ctxt'
op|'='
name|'None'
op|','
name|'read_deleted'
op|'='
string|"'yes'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'flavorid'
op|'=='
string|"'failtest'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Not found sucka!"'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'str'
op|'('
name|'flavorid'
op|')'
op|'=='
string|"'1234'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"This test expects flavorid 1234, not %s"'
op|'%'
name|'flavorid'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'read_deleted'
op|'!='
string|"'no'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"Should not be reading deleted"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
nl|'\n'
string|"'root_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"u'frob'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'19'
op|','
number|'18'
op|','
number|'49'
op|','
number|'30'
op|','
number|'877329'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'256'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
name|'flavorid'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'extra_specs'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vcpu_weight'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'7'
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_destroy
dedent|''
name|'def'
name|'fake_destroy'
op|'('
name|'flavorname'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_create
dedent|''
name|'def'
name|'fake_create'
op|'('
name|'context'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flavorid'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'flavorid'"
op|')'
newline|'\n'
name|'if'
name|'flavorid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'flavorid'
op|'='
number|'1234'
newline|'\n'
nl|'\n'
dedent|''
name|'newflavor'
op|'='
op|'{'
string|"'flavorid'"
op|':'
name|'flavorid'
op|'}'
newline|'\n'
name|'newflavor'
op|'['
string|'"name"'
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"memory_mb"'
op|']'
op|'='
name|'int'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'memory_mb'"
op|')'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"vcpus"'
op|']'
op|'='
name|'int'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'vcpus'"
op|')'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"root_gb"'
op|']'
op|'='
name|'int'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'root_gb'"
op|')'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"ephemeral_gb"'
op|']'
op|'='
name|'int'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'ephemeral_gb'"
op|')'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"swap"'
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'swap'"
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"rxtx_factor"'
op|']'
op|'='
name|'float'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'rxtx_factor'"
op|')'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"is_public"'
op|']'
op|'='
name|'bool'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'is_public'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'newflavor'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorManageTest
dedent|''
name|'class'
name|'FlavorManageTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'FlavorManageTest'
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
name|'flavors'
op|','
nl|'\n'
string|'"get_flavor_by_flavor_id"'
op|','
nl|'\n'
name|'fake_get_flavor_by_flavor_id'
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
string|'"destroy"'
op|','
name|'fake_destroy'
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
string|'"flavor_create"'
op|','
name|'fake_create'
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
string|"'Flavormanage'"
op|','
string|"'Flavorextradata'"
op|','
nl|'\n'
string|"'Flavor_access'"
op|','
string|"'Flavor_rxtx'"
op|','
string|"'Flavor_swap'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'flavormanage'
op|'.'
name|'FlavorManageController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'flavors'"
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'request_body'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"test"'
op|','
nl|'\n'
string|'"ram"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"disk"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"OS-FLV-EXT-DATA:ephemeral"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"id"'
op|':'
name|'unicode'
op|'('
string|"'1234'"
op|')'
op|','
nl|'\n'
string|'"swap"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"rxtx_factor"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"os-flavor-access:is_public"'
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'expected_flavor'
op|'='
name|'self'
op|'.'
name|'request_body'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/123/flavors/1234'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_delete'
op|'('
name|'req'
op|','
number|'1234'
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
nl|'\n'
comment|'# subsequent delete should fail'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_delete'
op|','
name|'req'
op|','
string|'"failtest"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_flavor_success_case
dedent|''
name|'def'
name|'_create_flavor_success_case'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'/v2/fake/flavors'"
newline|'\n'
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'return'
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
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_flavor_success_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'expected_flavor'
op|'['
string|'"flavor"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'expected_flavor'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_public_default
dedent|''
dedent|''
name|'def'
name|'test_create_public_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'os-flavor-access:is_public'"
op|']'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_flavor_success_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'expected_flavor'
op|'['
string|'"flavor"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'expected_flavor'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_name_with_leading_trailing_whitespace
dedent|''
dedent|''
name|'def'
name|'test_create_flavor_name_with_leading_trailing_whitespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'name'"
op|']'
op|'='
string|'" test "'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_flavor_success_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"test"'
op|','
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
string|'"name"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_without_flavorid
dedent|''
name|'def'
name|'test_create_without_flavorid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_flavor_success_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'expected_flavor'
op|'['
string|'"flavor"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'expected_flavor'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_flavor_bad_request_case
dedent|''
dedent|''
name|'def'
name|'_create_flavor_bad_request_case'
op|'('
name|'self'
op|','
name|'body'
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
nl|'\n'
name|'url'
op|'='
string|"'/v2/fake/flavors'"
newline|'\n'
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_code'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_invalid_name
dedent|''
name|'def'
name|'test_create_invalid_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'name'"
op|']'
op|'='
string|"'bad !@#!$% name'"
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_name_is_whitespace
dedent|''
name|'def'
name|'test_create_flavor_name_is_whitespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'name'"
op|']'
op|'='
string|"' '"
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_without_flavorname
dedent|''
name|'def'
name|'test_create_without_flavorname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_empty_body
dedent|''
name|'def'
name|'test_create_empty_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_no_body
dedent|''
name|'def'
name|'test_create_no_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_invalid_format_body
dedent|''
name|'def'
name|'test_create_invalid_format_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'['
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_invalid_flavorid
dedent|''
name|'def'
name|'test_create_invalid_flavorid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|'='
string|'"!@#!$#!$^#&^$&"'
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_check_flavor_id_length
dedent|''
name|'def'
name|'test_create_check_flavor_id_length'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'MAX_LENGTH'
op|'='
number|'255'
newline|'\n'
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|'='
string|'"a"'
op|'*'
op|'('
name|'MAX_LENGTH'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_leading_trailing_whitespaces_in_flavor_id
dedent|''
name|'def'
name|'test_create_with_leading_trailing_whitespaces_in_flavor_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request_body'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|'='
string|'"   bad_id   "'
newline|'\n'
name|'self'
op|'.'
name|'_create_flavor_bad_request_case'
op|'('
name|'self'
op|'.'
name|'request_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_exists_exception_returns_409
dedent|''
name|'def'
name|'test_flavor_exists_exception_returns_409'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"test"'
op|','
nl|'\n'
string|'"ram"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"disk"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"OS-FLV-EXT-DATA:ephemeral"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"id"'
op|':'
number|'1235'
op|','
nl|'\n'
string|'"swap"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"rxtx_factor"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"os-flavor-access:is_public"'
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_create
name|'def'
name|'fake_create'
op|'('
name|'name'
op|','
name|'memory_mb'
op|','
name|'vcpus'
op|','
name|'root_gb'
op|','
name|'ephemeral_gb'
op|','
nl|'\n'
name|'flavorid'
op|','
name|'swap'
op|','
name|'rxtx_factor'
op|','
name|'is_public'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FlavorExists'
op|'('
name|'name'
op|'='
name|'name'
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
name|'flavors'
op|','
string|'"create"'
op|','
name|'fake_create'
op|')'
newline|'\n'
name|'url'
op|'='
string|"'/v2/fake/flavors'"
newline|'\n'
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'expected'
op|')'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_memory_mb
dedent|''
name|'def'
name|'test_invalid_memory_mb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check negative and decimal number can\'t be accepted."""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
name|'flavors'
op|'.'
name|'create'
op|','
string|'"abc"'
op|','
nl|'\n'
op|'-'
number|'512'
op|','
number|'2'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1234'
op|','
number|'512'
op|','
number|'1'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
name|'flavors'
op|'.'
name|'create'
op|','
string|'"abcd"'
op|','
nl|'\n'
number|'512.2'
op|','
number|'2'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1234'
op|','
number|'512'
op|','
number|'1'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
name|'flavors'
op|'.'
name|'create'
op|','
string|'"abcde"'
op|','
nl|'\n'
name|'None'
op|','
number|'2'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1234'
op|','
number|'512'
op|','
number|'1'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
name|'flavors'
op|'.'
name|'create'
op|','
string|'"abcdef"'
op|','
nl|'\n'
number|'512'
op|','
number|'2'
op|','
name|'None'
op|','
number|'1'
op|','
number|'1234'
op|','
number|'512'
op|','
number|'1'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
name|'flavors'
op|'.'
name|'create'
op|','
string|'"abcdef"'
op|','
nl|'\n'
string|'"test_memory_mb"'
op|','
number|'2'
op|','
name|'None'
op|','
number|'1'
op|','
number|'1234'
op|','
number|'512'
op|','
number|'1'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
dedent|''
dedent|''
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PrivateFlavorManageTest
dedent|''
name|'class'
name|'PrivateFlavorManageTest'
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
name|'PrivateFlavorManageTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# self.stubs.Set(flavors,'
nl|'\n'
comment|'#                "get_flavor_by_flavor_id",'
nl|'\n'
comment|'#                fake_get_flavor_by_flavor_id)'
nl|'\n'
comment|'# self.stubs.Set(flavors, "destroy", fake_destroy)'
nl|'\n'
comment|'# self.stubs.Set(flavors, "create", fake_create)'
nl|'\n'
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
string|"'Flavormanage'"
op|','
string|"'Flavorextradata'"
op|','
nl|'\n'
string|"'Flavor_access'"
op|','
string|"'Flavor_rxtx'"
op|','
string|"'Flavor_swap'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'flavormanage'
op|'.'
name|'FlavorManageController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavor_access_controller'
op|'='
name|'flavor_access'
op|'.'
name|'FlavorAccessController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'flavors'"
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_private_flavor_should_not_grant_flavor_access
dedent|''
name|'def'
name|'test_create_private_flavor_should_not_grant_flavor_access'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"test"'
op|','
nl|'\n'
string|'"ram"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"disk"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"OS-FLV-EXT-DATA:ephemeral"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"swap"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"rxtx_factor"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"os-flavor-access:is_public"'
op|':'
name|'False'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
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
op|','
name|'auth_token'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'flavors'"
op|','
op|')'
op|','
nl|'\n'
name|'fake_auth_context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'url'
op|'='
string|"'/v2/fake/flavors'"
newline|'\n'
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'expected'
op|')'
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
name|'body'
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
name|'for'
name|'key'
name|'in'
name|'expected'
op|'['
string|'"flavor"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|','
name|'expected'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'flavor_access_body'
op|'='
name|'self'
op|'.'
name|'flavor_access_controller'
op|'.'
name|'index'
op|'('
nl|'\n'
name|'FakeRequest'
op|'('
op|')'
op|','
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
name|'expected_flavor_access_body'
op|'='
op|'{'
nl|'\n'
string|'"tenant_id"'
op|':'
string|'"%s"'
op|'%'
name|'ctxt'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|'"flavor_id"'
op|':'
string|'"%s"'
op|'%'
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
string|'"id"'
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'expected_flavor_access_body'
op|','
nl|'\n'
name|'flavor_access_body'
op|'['
string|'"flavor_access"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_public_flavor_should_not_create_flavor_access
dedent|''
name|'def'
name|'test_create_public_flavor_should_not_create_flavor_access'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"test"'
op|','
nl|'\n'
string|'"ram"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"disk"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"OS-FLV-EXT-DATA:ephemeral"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"swap"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"rxtx_factor"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"os-flavor-access:is_public"'
op|':'
name|'True'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
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
op|','
name|'auth_token'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'flavors'"
op|','
op|')'
op|','
nl|'\n'
name|'fake_auth_context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'flavors'
op|','
string|'"add_flavor_access"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'url'
op|'='
string|"'/v2/fake/flavors'"
newline|'\n'
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
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'expected'
op|')'
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
name|'body'
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
name|'for'
name|'key'
name|'in'
name|'expected'
op|'['
string|'"flavor"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|','
name|'expected'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
