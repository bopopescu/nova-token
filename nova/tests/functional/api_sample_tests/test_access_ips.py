begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
name|'import'
name|'fake'
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
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccessIPsSampleJsonTest
name|'class'
name|'AccessIPsSampleJsonTest'
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
string|"'os-access-ips'"
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
name|'AccessIPsSampleJsonTest'
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
nl|'\n'
string|"'nova.api.openstack.compute.contrib.keypairs.Keypairs'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.extended_ips.Extended_ips'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.extended_ips_mac.'"
nl|'\n'
string|"'Extended_ips_mac'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_servers_post
dedent|''
name|'def'
name|'_servers_post'
op|'('
name|'self'
op|','
name|'subs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers'"
op|','
string|"'server-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_post
dedent|''
name|'def'
name|'test_servers_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_compute_endpoint'
op|'('
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
string|"'fe80::'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_servers_post'
op|'('
name|'subs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_get
dedent|''
name|'def'
name|'test_servers_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_compute_endpoint'
op|'('
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
string|"'fe80::'"
nl|'\n'
op|'}'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_servers_post'
op|'('
name|'subs'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_details
dedent|''
name|'def'
name|'test_servers_details'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_compute_endpoint'
op|'('
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
string|"'fe80::'"
nl|'\n'
op|'}'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_servers_post'
op|'('
name|'subs'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/detail'"
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-details-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_rebuild
dedent|''
name|'def'
name|'test_servers_rebuild'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_compute_endpoint'
op|'('
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
string|"'fe80::'"
nl|'\n'
op|'}'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_servers_post'
op|'('
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|'"4.3.2.1"'
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"'80fe::'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'server-action-rebuild'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-action-rebuild-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_update
dedent|''
name|'def'
name|'test_servers_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_compute_endpoint'
op|'('
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
string|"'fe80::'"
nl|'\n'
op|'}'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_servers_post'
op|'('
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|'"4.3.2.1"'
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"'80fe::'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
op|','
string|"'server-put-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-put-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
