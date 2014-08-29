begin_unit
comment|'#    Copyright 2011 OpenStack Foundation'
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
name|'cinderclient'
op|'.'
name|'v1'
name|'import'
name|'client'
name|'as'
name|'cinder_client_v1'
newline|'\n'
name|'from'
name|'cinderclient'
op|'.'
name|'v2'
name|'import'
name|'client'
name|'as'
name|'cinder_client_v2'
newline|'\n'
name|'from'
name|'requests_mock'
op|'.'
name|'contrib'
name|'import'
name|'fixture'
newline|'\n'
name|'from'
name|'testtools'
name|'import'
name|'matchers'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'volume'
name|'import'
name|'cinder'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_image_metadata
name|'_image_metadata'
op|'='
op|'{'
nl|'\n'
string|"'kernel_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|"'fake'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseCinderTestCase
name|'class'
name|'BaseCinderTestCase'
op|'('
name|'object'
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
name|'BaseCinderTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'reset_globals'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'requests'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixture'
op|'.'
name|'Fixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'cinder'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'username'"
op|','
nl|'\n'
string|"'project_id'"
op|','
nl|'\n'
name|'auth_token'
op|'='
string|"'token'"
op|','
nl|'\n'
name|'service_catalog'
op|'='
name|'self'
op|'.'
name|'CATALOG'
op|')'
newline|'\n'
nl|'\n'
DECL|member|flags
dedent|''
name|'def'
name|'flags'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'BaseCinderTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'flags'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'reset_globals'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_client
dedent|''
name|'def'
name|'create_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cinder'
op|'.'
name|'cinderclient'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_context_with_catalog
dedent|''
name|'def'
name|'test_context_with_catalog'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'URL'
op|','
name|'self'
op|'.'
name|'create_client'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'get_endpoint'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_http_retries
dedent|''
name|'def'
name|'test_cinder_http_retries'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'retries'
op|'='
number|'42'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'http_retries'
op|'='
name|'retries'
op|','
name|'group'
op|'='
string|"'cinder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'retries'
op|','
name|'self'
op|'.'
name|'create_client'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'connect_retries'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_api_insecure
dedent|''
name|'def'
name|'test_cinder_api_insecure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# The True/False negation is awkward, but better for the client'
nl|'\n'
comment|'# to pass us insecure=True and we check verify_cert == False'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'insecure'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'cinder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'create_client'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'session'
op|'.'
name|'verify'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_http_timeout
dedent|''
name|'def'
name|'test_cinder_http_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeout'
op|'='
number|'123'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'timeout'
op|'='
name|'timeout'
op|','
name|'group'
op|'='
string|"'cinder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'timeout'
op|','
name|'self'
op|'.'
name|'create_client'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'session'
op|'.'
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_api_cacert_file
dedent|''
name|'def'
name|'test_cinder_api_cacert_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cacert'
op|'='
string|'"/etc/ssl/certs/ca-certificates.crt"'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'cafile'
op|'='
name|'cacert'
op|','
name|'group'
op|'='
string|"'cinder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'create_client'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'session'
op|'.'
name|'verify'
op|','
name|'cacert'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CinderTestCase
dedent|''
dedent|''
name|'class'
name|'CinderTestCase'
op|'('
name|'BaseCinderTestCase'
op|','
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for cinder volume v1 api."""'
newline|'\n'
nl|'\n'
DECL|variable|URL
name|'URL'
op|'='
string|'"http://localhost:8776/v1/project_id"'
newline|'\n'
nl|'\n'
DECL|variable|CATALOG
name|'CATALOG'
op|'='
op|'['
op|'{'
nl|'\n'
string|'"type"'
op|':'
string|'"volumev2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"cinderv2"'
op|','
nl|'\n'
string|'"endpoints"'
op|':'
op|'['
op|'{'
string|'"publicURL"'
op|':'
name|'URL'
op|'}'
op|']'
nl|'\n'
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|member|create_client
name|'def'
name|'create_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'c'
op|'='
name|'super'
op|'('
name|'CinderTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'create_client'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'c'
op|','
name|'cinder_client_v1'
op|'.'
name|'Client'
op|')'
newline|'\n'
name|'return'
name|'c'
newline|'\n'
nl|'\n'
DECL|member|stub_volume
dedent|''
name|'def'
name|'stub_volume'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
nl|'\n'
string|"'display_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'None'
op|','
nl|'\n'
string|'"attachments"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
string|'"cinder"'
op|','
nl|'\n'
string|'"created_at"'
op|':'
string|'"2012-09-10T00:00:00.000000"'
op|','
nl|'\n'
string|'"id"'
op|':'
string|"'00000000-0000-0000-0000-000000000000'"
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|'"size"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"snapshot_id"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"available"'
op|','
nl|'\n'
string|'"volume_type"'
op|':'
string|'"None"'
op|','
nl|'\n'
string|'"bootable"'
op|':'
string|'"true"'
nl|'\n'
op|'}'
newline|'\n'
name|'volume'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_endpoint_template
dedent|''
name|'def'
name|'test_cinder_endpoint_template'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'endpoint'
op|'='
string|"'http://other_host:8776/v1/%(project_id)s'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'endpoint_template'
op|'='
name|'endpoint'
op|','
name|'group'
op|'='
string|"'cinder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'http://other_host:8776/v1/project_id'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'create_client'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'endpoint_override'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_non_existing_volume
dedent|''
name|'def'
name|'test_get_non_existing_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'requests'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'URL'
op|'+'
string|"'/volumes/nonexisting'"
op|','
nl|'\n'
name|'status_code'
op|'='
number|'404'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeNotFound'
op|','
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'nonexisting'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_with_image_metadata
dedent|''
name|'def'
name|'test_volume_with_image_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'v'
op|'='
name|'self'
op|'.'
name|'stub_volume'
op|'('
name|'id'
op|'='
string|"'1234'"
op|','
name|'volume_image_metadata'
op|'='
name|'_image_metadata'
op|')'
newline|'\n'
name|'m'
op|'='
name|'self'
op|'.'
name|'requests'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'URL'
op|'+'
string|"'/volumes/5678'"
op|','
name|'json'
op|'='
op|'{'
string|"'volume'"
op|':'
name|'v'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'5678'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'m'
op|'.'
name|'last_request'
op|'.'
name|'path'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'EndsWith'
op|'('
string|"'/volumes/5678'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'volume_image_metadata'"
op|','
name|'volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume'
op|'['
string|"'volume_image_metadata'"
op|']'
op|','
name|'_image_metadata'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CinderV2TestCase
dedent|''
dedent|''
name|'class'
name|'CinderV2TestCase'
op|'('
name|'BaseCinderTestCase'
op|','
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for cinder volume v2 api."""'
newline|'\n'
nl|'\n'
DECL|variable|URL
name|'URL'
op|'='
string|'"http://localhost:8776/v2/project_id"'
newline|'\n'
nl|'\n'
DECL|variable|CATALOG
name|'CATALOG'
op|'='
op|'['
op|'{'
nl|'\n'
string|'"type"'
op|':'
string|'"volumev2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"cinder"'
op|','
nl|'\n'
string|'"endpoints"'
op|':'
op|'['
op|'{'
string|'"publicURL"'
op|':'
name|'URL'
op|'}'
op|']'
nl|'\n'
op|'}'
op|']'
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
name|'CinderV2TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'cinder'
op|'.'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'catalog_info'"
op|','
nl|'\n'
string|"'volumev2:cinder:publicURL'"
op|','
name|'group'
op|'='
string|"'cinder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'cinder'
op|'.'
name|'CONF'
op|'.'
name|'reset'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_client
dedent|''
name|'def'
name|'create_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'c'
op|'='
name|'super'
op|'('
name|'CinderV2TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'create_client'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'c'
op|','
name|'cinder_client_v2'
op|'.'
name|'Client'
op|')'
newline|'\n'
name|'return'
name|'c'
newline|'\n'
nl|'\n'
DECL|member|stub_volume
dedent|''
name|'def'
name|'stub_volume'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'None'
op|','
nl|'\n'
string|'"attachments"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
string|'"cinderv2"'
op|','
nl|'\n'
string|'"created_at"'
op|':'
string|'"2013-08-10T00:00:00.000000"'
op|','
nl|'\n'
string|'"id"'
op|':'
string|"'00000000-0000-0000-0000-000000000000'"
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|'"size"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"snapshot_id"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"available"'
op|','
nl|'\n'
string|'"volume_type"'
op|':'
string|'"None"'
op|','
nl|'\n'
string|'"bootable"'
op|':'
string|'"true"'
nl|'\n'
op|'}'
newline|'\n'
name|'volume'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_endpoint_template
dedent|''
name|'def'
name|'test_cinder_endpoint_template'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'endpoint'
op|'='
string|"'http://other_host:8776/v2/%(project_id)s'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'endpoint_template'
op|'='
name|'endpoint'
op|','
name|'group'
op|'='
string|"'cinder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'http://other_host:8776/v2/project_id'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'create_client'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'endpoint_override'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_non_existing_volume
dedent|''
name|'def'
name|'test_get_non_existing_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'requests'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'URL'
op|'+'
string|"'/volumes/nonexisting'"
op|','
nl|'\n'
name|'status_code'
op|'='
number|'404'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeNotFound'
op|','
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'nonexisting'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_with_image_metadata
dedent|''
name|'def'
name|'test_volume_with_image_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'v'
op|'='
name|'self'
op|'.'
name|'stub_volume'
op|'('
name|'id'
op|'='
string|"'1234'"
op|','
name|'volume_image_metadata'
op|'='
name|'_image_metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'requests'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'URL'
op|'+'
string|"'/volumes/5678'"
op|','
name|'json'
op|'='
op|'{'
string|"'volume'"
op|':'
name|'v'
op|'}'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'5678'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'volume_image_metadata'"
op|','
name|'volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_image_metadata'
op|','
name|'volume'
op|'['
string|"'volume_image_metadata'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
