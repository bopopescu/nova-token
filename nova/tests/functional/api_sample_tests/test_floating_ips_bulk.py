begin_unit
comment|'# Copyright 2014 IBM Corp.'
nl|'\n'
comment|'#'
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
name|'nova'
op|'.'
name|'conf'
newline|'\n'
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
name|'nova'
op|'.'
name|'conf'
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
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpsBulkTest
name|'class'
name|'FloatingIpsBulkTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-floating-ips-bulk"'
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
name|'FloatingIpsBulkTest'
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
string|"'contrib.floating_ips_bulk.Floating_ips_bulk'"
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
name|'FloatingIpsBulkTest'
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
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
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
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
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
op|','
nl|'\n'
string|"'host'"
op|':'
string|'"testHost"'
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
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'db'
op|'.'
name|'floating_ip_bulk_destroy'
op|','
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
DECL|member|test_floating_ips_bulk_list
dedent|''
name|'def'
name|'test_floating_ips_bulk_list'
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
string|"'os-floating-ips-bulk'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-bulk-list-resp'"
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
DECL|member|test_floating_ips_bulk_list_by_host
dedent|''
name|'def'
name|'test_floating_ips_bulk_list_by_host'
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
string|"'os-floating-ips-bulk/testHost'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-bulk-list-by-host-resp'"
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
DECL|member|test_floating_ips_bulk_create
dedent|''
name|'def'
name|'test_floating_ips_bulk_create'
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
string|"'os-floating-ips-bulk'"
op|','
nl|'\n'
string|"'floating-ips-bulk-create-req'"
op|','
nl|'\n'
op|'{'
string|'"ip_range"'
op|':'
string|'"192.168.1.0/24"'
op|','
nl|'\n'
string|'"pool"'
op|':'
name|'CONF'
op|'.'
name|'default_floating_pool'
op|','
nl|'\n'
string|'"interface"'
op|':'
name|'CONF'
op|'.'
name|'public_interface'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-bulk-create-resp'"
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_bulk_delete
dedent|''
name|'def'
name|'test_floating_ips_bulk_delete'
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
name|'_do_put'
op|'('
string|"'os-floating-ips-bulk/delete'"
op|','
nl|'\n'
string|"'floating-ips-bulk-delete-req'"
op|','
nl|'\n'
op|'{'
string|'"ip_range"'
op|':'
string|'"192.168.1.0/24"'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ips-bulk-delete-resp'"
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
