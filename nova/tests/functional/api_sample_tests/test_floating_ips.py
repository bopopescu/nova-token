begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'default_floating_pool'"
op|','
string|"'nova.network.floating_ips'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'public_interface'"
op|','
string|"'nova.network.linux_net'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpsTest
name|'class'
name|'FloatingIpsTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-floating-ips"'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'FloatingIpsTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.floating_ips.Floating_ips'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.extended_floating_ips.Extended_floating_ips'"
op|')'
newline|'\n'
name|'return'
name|'f'
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
name|'FloatingIpsTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'pool'
op|'='
name|'CONF'
op|'.'
name|'default_floating_pool'
newline|'\n'
name|'interface'
op|'='
name|'CONF'
op|'.'
name|'public_interface'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ip_pool'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|'"10.10.10.1"'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'interface'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|'"10.10.10.2"'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'interface'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'address'"
op|':'
string|'"10.10.10.3"'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'interface'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'db'
op|'.'
name|'floating_ip_bulk_create'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'ip_pool'
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
name|'compute'
op|'.'
name|'db'
op|'.'
name|'floating_ip_bulk_destroy'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'ip_pool'
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIpsTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_list_empty
dedent|''
name|'def'
name|'test_floating_ips_list_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-floating-ips'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-list-empty-resp'"
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_list
dedent|''
name|'def'
name|'test_floating_ips_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-floating-ips'"
op|','
nl|'\n'
string|"'floating-ips-create-nopool-req'"
op|','
nl|'\n'
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-floating-ips'"
op|','
nl|'\n'
string|"'floating-ips-create-nopool-req'"
op|','
nl|'\n'
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-floating-ips'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-list-resp'"
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_create_nopool
dedent|''
name|'def'
name|'test_floating_ips_create_nopool'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-floating-ips'"
op|','
nl|'\n'
string|"'floating-ips-create-nopool-req'"
op|','
nl|'\n'
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-create-resp'"
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_create
dedent|''
name|'def'
name|'test_floating_ips_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-floating-ips'"
op|','
nl|'\n'
string|"'floating-ips-create-req'"
op|','
nl|'\n'
op|'{'
string|'"pool"'
op|':'
name|'CONF'
op|'.'
name|'default_floating_pool'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-create-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_get
dedent|''
name|'def'
name|'test_floating_ips_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_floating_ips_create'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(sdague): the first floating ip will always have 1 as an id,'
nl|'\n'
comment|'# but it would be better if we could get this from the create'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-floating-ips/%d'"
op|'%'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-get-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_delete
dedent|''
name|'def'
name|'test_floating_ips_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_floating_ips_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-floating-ips/%d'"
op|'%'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'""'
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
