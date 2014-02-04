begin_unit
comment|'# Copyright 2011 University of Southern California'
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
name|'mock'
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
name|'flavors_extraspecs'
newline|'\n'
name|'import'
name|'nova'
op|'.'
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
op|'.'
name|'db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
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
DECL|function|return_create_flavor_extra_specs
name|'def'
name|'return_create_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|','
name|'extra_specs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_flavor_extra_specs'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_flavor_extra_specs
dedent|''
name|'def'
name|'return_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_flavor_extra_specs'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_flavor_extra_specs_item
dedent|''
name|'def'
name|'return_flavor_extra_specs_item'
op|'('
name|'context'
op|','
name|'flavor_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
name|'key'
op|':'
name|'stub_flavor_extra_specs'
op|'('
op|')'
op|'['
name|'key'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_empty_flavor_extra_specs
dedent|''
name|'def'
name|'return_empty_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_flavor_extra_specs
dedent|''
name|'def'
name|'delete_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_flavor_extra_specs
dedent|''
name|'def'
name|'stub_flavor_extra_specs'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'specs'
op|'='
op|'{'
nl|'\n'
string|'"key1"'
op|':'
string|'"value1"'
op|','
nl|'\n'
string|'"key2"'
op|':'
string|'"value2"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"value3"'
op|','
nl|'\n'
string|'"key4"'
op|':'
string|'"value4"'
op|','
nl|'\n'
string|'"key5"'
op|':'
string|'"value5"'
op|'}'
newline|'\n'
name|'return'
name|'specs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsExtraSpecsTest
dedent|''
name|'class'
name|'FlavorsExtraSpecsTest'
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
name|'FlavorsExtraSpecsTest'
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
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'flavors_extraspecs'
op|'.'
name|'FlavorExtraSpecsController'
op|'('
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'flavor_extra_specs_get'"
op|','
nl|'\n'
name|'return_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_no_data
dedent|''
name|'def'
name|'test_index_no_data'
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
op|','
string|"'flavor_extra_specs_get'"
op|','
nl|'\n'
name|'return_empty_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'flavor_extra_specs_get_item'"
op|','
nl|'\n'
name|'return_flavor_extra_specs_item'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key5'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
number|'1'
op|','
string|"'key5'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value5'"
op|','
name|'res_dict'
op|'['
string|"'key5'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_spec_not_found
dedent|''
name|'def'
name|'test_show_spec_not_found'
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
op|','
string|"'flavor_extra_specs_get'"
op|','
nl|'\n'
name|'return_empty_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key6'"
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key6'"
op|')'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'flavor_extra_specs_delete'"
op|','
nl|'\n'
name|'delete_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key5'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
number|'1'
op|','
string|"'key5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_no_admin
dedent|''
name|'def'
name|'test_delete_no_admin'
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
op|','
string|"'flavor_extra_specs_delete'"
op|','
nl|'\n'
name|'delete_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key5'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key 5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_spec_not_found
dedent|''
name|'def'
name|'test_delete_spec_not_found'
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
string|"'/v3/flavors/1/extra-specs/key6'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key6'"
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'.'
name|'wsgi_code'
op|','
number|'201'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_no_admin
dedent|''
name|'def'
name|'test_create_no_admin'
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
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_not_found
dedent|''
name|'def'
name|'test_create_flavor_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_instance_type_extra_specs_update_or_create
indent|'        '
name|'def'
name|'fake_instance_type_extra_specs_update_or_create'
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
name|'FlavorNotFound'
op|'('
name|'flavor_id'
op|'='
string|"''"
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
name|'nova'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'fake_instance_type_extra_specs_update_or_create'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_db_duplicate
dedent|''
name|'def'
name|'test_create_flavor_db_duplicate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_instance_type_extra_specs_update_or_create
indent|'        '
name|'def'
name|'fake_instance_type_extra_specs_update_or_create'
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
name|'db_exc'
op|'.'
name|'DBDuplicateEntry'
op|'('
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
name|'nova'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'fake_instance_type_extra_specs_update_or_create'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.flavor_extra_specs_update_or_create'"
op|')'
newline|'\n'
DECL|member|test_create_invalid_specs_key
name|'def'
name|'test_create_invalid_specs_key'
op|'('
name|'self'
op|','
name|'mock_flavor_extra_specs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'invalid_keys'
op|'='
op|'('
string|'"key1/"'
op|','
string|'"<key>"'
op|','
string|'"$$akey$"'
op|','
string|'"!akey"'
op|','
string|'""'
op|')'
newline|'\n'
name|'mock_flavor_extra_specs'
op|'.'
name|'side_effects'
op|'='
name|'return_create_flavor_extra_specs'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'invalid_keys'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
name|'key'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.flavor_extra_specs_update_or_create'"
op|')'
newline|'\n'
DECL|member|test_create_valid_specs_key
name|'def'
name|'test_create_valid_specs_key'
op|'('
name|'self'
op|','
name|'mock_flavor_extra_specs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'valid_keys'
op|'='
op|'('
string|'"key1"'
op|','
string|'"month.price"'
op|','
string|'"I_am-a Key"'
op|','
string|'"finance:g2"'
op|')'
newline|'\n'
name|'mock_flavor_extra_specs'
op|'.'
name|'side_effects'
op|'='
name|'return_create_flavor_extra_specs'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'valid_keys'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
name|'key'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'.'
name|'wsgi_code'
op|','
number|'201'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item
dedent|''
dedent|''
name|'def'
name|'test_update_item'
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
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
number|'1'
op|','
string|"'key1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_no_admin
dedent|''
name|'def'
name|'test_update_item_no_admin'
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
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_empty_body
dedent|''
name|'def'
name|'test_update_item_empty_body'
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
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key1'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_too_many_keys
dedent|''
name|'def'
name|'test_update_item_too_many_keys'
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
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|','
string|'"key2"'
op|':'
string|'"value2"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_body_uri_mismatch
dedent|''
name|'def'
name|'test_update_item_body_uri_mismatch'
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
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/bad'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'bad'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_flavor_not_found
dedent|''
name|'def'
name|'test_update_flavor_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_instance_type_extra_specs_update_or_create
indent|'        '
name|'def'
name|'fake_instance_type_extra_specs_update_or_create'
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
name|'FlavorNotFound'
op|'('
name|'flavor_id'
op|'='
string|"''"
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
name|'nova'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'fake_instance_type_extra_specs_update_or_create'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_flavor_db_duplicate
dedent|''
name|'def'
name|'test_update_flavor_db_duplicate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_instance_type_extra_specs_update_or_create
indent|'        '
name|'def'
name|'fake_instance_type_extra_specs_update_or_create'
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
name|'db_exc'
op|'.'
name|'DBDuplicateEntry'
op|'('
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
name|'nova'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'flavor_extra_specs_update_or_create'"
op|','
nl|'\n'
name|'fake_instance_type_extra_specs_update_or_create'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v3/flavors/1/extra-specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key1'"
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
