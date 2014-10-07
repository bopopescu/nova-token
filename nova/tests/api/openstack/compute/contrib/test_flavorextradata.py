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
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'flavorid'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
name|'str'
op|'('
name|'flavorid'
op|')'
op|','
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
string|"u'test'"
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
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
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
number|'512'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
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
string|"'swap'"
op|':'
number|'0'
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
name|'fake_get_flavor_by_flavor_id'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'fake_get_flavor_by_flavor_id'
op|'('
number|'2'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorExtraDataTestV21
dedent|''
name|'class'
name|'FlavorExtraDataTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|base_url
indent|'    '
name|'base_url'
op|'='
string|"'/v2/fake/flavors'"
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
name|'FlavorExtraDataTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'ext'
op|'='
op|'('
string|"'nova.api.openstack.compute.contrib'"
nl|'\n'
string|"'.flavorextradata.Flavorextradata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'osapi_compute_extension'
op|'='
op|'['
name|'ext'
op|']'
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
string|"'get_flavor_by_flavor_id'"
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
string|"'get_all_flavors_sorted_list'"
op|','
nl|'\n'
name|'fake_get_all_flavors_sorted_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_app'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_app
dedent|''
name|'def'
name|'_setup_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'flavors'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_flavor_response
dedent|''
name|'def'
name|'_verify_flavor_response'
op|'('
name|'self'
op|','
name|'flavor'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'expected'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flavor'
op|'['
name|'key'
op|']'
op|','
name|'expected'
op|'['
name|'key'
op|']'
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
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'flavor'"
op|':'
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disk'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'OS-FLV-EXT-DATA:ephemeral'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'/1'"
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
name|'self'
op|'.'
name|'_verify_flavor_response'
op|'('
name|'body'
op|'['
string|"'flavor'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavor'"
op|']'
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
name|'expected'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disk'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'OS-FLV-EXT-DATA:ephemeral'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disk'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'OS-FLV-EXT-DATA:ephemeral'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'/detail'"
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
name|'i'
op|','
name|'flavor'
name|'in'
name|'enumerate'
op|'('
name|'body'
op|'['
string|"'flavors'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_verify_flavor_response'
op|'('
name|'flavor'
op|','
name|'expected'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorExtraDataTestV2
dedent|''
dedent|''
dedent|''
name|'class'
name|'FlavorExtraDataTestV2'
op|'('
name|'FlavorExtraDataTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_setup_app
indent|'    '
name|'def'
name|'_setup_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
dedent|''
dedent|''
endmarker|''
end_unit
