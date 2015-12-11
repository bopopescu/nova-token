begin_unit
comment|'# Copyright 2015 Intel Corporation.'
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
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api'
name|'import'
name|'client'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
name|'import'
name|'test_servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LegacyV2CompatibleTestBase
name|'class'
name|'LegacyV2CompatibleTestBase'
op|'('
name|'test_servers'
op|'.'
name|'ServersTestBase'
op|')'
op|':'
newline|'\n'
DECL|variable|api_major_version
indent|'    '
name|'api_major_version'
op|'='
string|"'v2'"
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
name|'LegacyV2CompatibleTestBase'
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
name|'_check_api_endpoint'
op|'('
string|"'/v2'"
op|','
op|'['
name|'compute'
op|'.'
name|'APIRouterV21'
op|','
nl|'\n'
name|'openstack'
op|'.'
name|'LegacyV2CompatibleWrapper'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_request_with_microversion_headers
dedent|''
name|'def'
name|'test_request_with_microversion_headers'
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
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'os-keypairs'"
op|','
nl|'\n'
op|'{'
string|'"keypair"'
op|':'
op|'{'
string|'"name"'
op|':'
string|'"test"'
op|'}'
op|'}'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
name|'wsgi'
op|'.'
name|'API_VERSION_REQUEST_HEADER'
op|':'
string|"'2.100'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'wsgi'
op|'.'
name|'API_VERSION_REQUEST_HEADER'
op|','
name|'response'
op|'.'
name|'headers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'Vary'"
op|','
name|'response'
op|'.'
name|'headers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'type'"
op|','
name|'response'
op|'.'
name|'body'
op|'['
string|'"keypair"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_request_without_addtional_properties_check
dedent|''
name|'def'
name|'test_request_without_addtional_properties_check'
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
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'os-keypairs'"
op|','
nl|'\n'
op|'{'
string|'"keypair"'
op|':'
op|'{'
string|'"name"'
op|':'
string|'"test"'
op|','
string|'"foooooo"'
op|':'
string|'"barrrrrr"'
op|'}'
op|'}'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
name|'wsgi'
op|'.'
name|'API_VERSION_REQUEST_HEADER'
op|':'
string|"'2.100'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'wsgi'
op|'.'
name|'API_VERSION_REQUEST_HEADER'
op|','
name|'response'
op|'.'
name|'headers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'Vary'"
op|','
name|'response'
op|'.'
name|'headers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'type'"
op|','
name|'response'
op|'.'
name|'body'
op|'['
string|'"keypair"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_request_with_pattern_properties_check
dedent|''
name|'def'
name|'test_request_with_pattern_properties_check'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_network'
op|'.'
name|'set_stub_network_methods'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_for_state_change'
op|'('
name|'created_server'
op|','
string|"'BUILD'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_metadata'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'a'"
op|':'
string|"'b'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|','
op|'{'
string|"'a'"
op|':'
string|"'b'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_request_with_pattern_properties_with_avoid_metadata
dedent|''
name|'def'
name|'test_request_with_pattern_properties_with_avoid_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_network'
op|'.'
name|'set_stub_network_methods'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_metadata'
op|','
nl|'\n'
name|'created_server'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'a'"
op|':'
string|"'b'"
op|','
nl|'\n'
string|"'x'"
op|'*'
number|'300'
op|':'
string|"'y'"
op|','
nl|'\n'
string|"'h'"
op|'*'
number|'300'
op|':'
string|"'i'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exc'
op|'.'
name|'response'
op|'.'
name|'status_code'
op|','
number|'400'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
