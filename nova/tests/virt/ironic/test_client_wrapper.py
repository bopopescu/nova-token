begin_unit
comment|'# Copyright 2014 Red Hat, Inc.'
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
name|'ironicclient'
name|'import'
name|'client'
name|'as'
name|'ironic_client'
newline|'\n'
name|'from'
name|'ironicclient'
name|'import'
name|'exc'
name|'as'
name|'ironic_exception'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
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
name|'virt'
op|'.'
name|'ironic'
name|'import'
name|'utils'
name|'as'
name|'ironic_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'ironic'
name|'import'
name|'client_wrapper'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_CLIENT
name|'FAKE_CLIENT'
op|'='
name|'ironic_utils'
op|'.'
name|'FakeClient'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IronicClientWrapperTestCase
name|'class'
name|'IronicClientWrapperTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'IronicClientWrapperTestCase'
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
name|'ironicclient'
op|'='
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|'('
op|')'
newline|'\n'
comment|'# Do not waste time sleeping'
nl|'\n'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'api_retry_interval'"
op|','
number|'0'
op|','
string|"'ironic'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_multi_getattr'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_get_client'"
op|')'
newline|'\n'
DECL|member|test_call_good_no_args
name|'def'
name|'test_call_good_no_args'
op|'('
name|'self'
op|','
name|'mock_get_client'
op|','
name|'mock_multi_getattr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_client'
op|'.'
name|'return_value'
op|'='
name|'FAKE_CLIENT'
newline|'\n'
name|'self'
op|'.'
name|'ironicclient'
op|'.'
name|'call'
op|'('
string|'"node.list"'
op|')'
newline|'\n'
name|'mock_get_client'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'mock_multi_getattr'
op|'.'
name|'assert_called_once_with'
op|'('
name|'FAKE_CLIENT'
op|','
string|'"node.list"'
op|')'
newline|'\n'
name|'mock_multi_getattr'
op|'.'
name|'return_value'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_multi_getattr'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_get_client'"
op|')'
newline|'\n'
DECL|member|test_call_good_with_args
name|'def'
name|'test_call_good_with_args'
op|'('
name|'self'
op|','
name|'mock_get_client'
op|','
name|'mock_multi_getattr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_client'
op|'.'
name|'return_value'
op|'='
name|'FAKE_CLIENT'
newline|'\n'
name|'self'
op|'.'
name|'ironicclient'
op|'.'
name|'call'
op|'('
string|'"node.list"'
op|','
string|"'test'"
op|','
name|'associated'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_get_client'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'mock_multi_getattr'
op|'.'
name|'assert_called_once_with'
op|'('
name|'FAKE_CLIENT'
op|','
string|'"node.list"'
op|')'
newline|'\n'
name|'mock_multi_getattr'
op|'.'
name|'return_value'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
string|"'test'"
op|','
name|'associated'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ironic_client'
op|','
string|"'get_client'"
op|')'
newline|'\n'
DECL|member|test__get_client_no_auth_token
name|'def'
name|'test__get_client_no_auth_token'
op|'('
name|'self'
op|','
name|'mock_ir_cli'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'admin_auth_token'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|"'ironic'"
op|')'
newline|'\n'
name|'ironicclient'
op|'='
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|'('
op|')'
newline|'\n'
comment|'# dummy call to have _get_client() called'
nl|'\n'
name|'ironicclient'
op|'.'
name|'call'
op|'('
string|'"node.list"'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'os_username'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_username'
op|','
nl|'\n'
string|"'os_password'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_password'
op|','
nl|'\n'
string|"'os_auth_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_url'
op|','
nl|'\n'
string|"'os_tenant_name'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_tenant_name'
op|','
nl|'\n'
string|"'os_service_type'"
op|':'
string|"'baremetal'"
op|','
nl|'\n'
string|"'os_endpoint_type'"
op|':'
string|"'public'"
op|','
nl|'\n'
string|"'ironic_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_endpoint'
op|'}'
newline|'\n'
name|'mock_ir_cli'
op|'.'
name|'assert_called_once_with'
op|'('
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_version'
op|','
nl|'\n'
op|'**'
name|'expected'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ironic_client'
op|','
string|"'get_client'"
op|')'
newline|'\n'
DECL|member|test__get_client_with_auth_token
name|'def'
name|'test__get_client_with_auth_token'
op|'('
name|'self'
op|','
name|'mock_ir_cli'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'admin_auth_token'
op|'='
string|"'fake-token'"
op|','
name|'group'
op|'='
string|"'ironic'"
op|')'
newline|'\n'
name|'ironicclient'
op|'='
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|'('
op|')'
newline|'\n'
comment|'# dummy call to have _get_client() called'
nl|'\n'
name|'ironicclient'
op|'.'
name|'call'
op|'('
string|'"node.list"'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'os_auth_token'"
op|':'
string|"'fake-token'"
op|','
nl|'\n'
string|"'ironic_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_endpoint'
op|'}'
newline|'\n'
name|'mock_ir_cli'
op|'.'
name|'assert_called_once_with'
op|'('
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_version'
op|','
nl|'\n'
op|'**'
name|'expected'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_multi_getattr'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_get_client'"
op|')'
newline|'\n'
DECL|member|test_call_fail
name|'def'
name|'test_call_fail'
op|'('
name|'self'
op|','
name|'mock_get_client'
op|','
name|'mock_multi_getattr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'api_max_retries'"
op|','
number|'2'
op|','
string|"'ironic'"
op|')'
newline|'\n'
name|'test_obj'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'test_obj'
op|'.'
name|'side_effect'
op|'='
name|'ironic_exception'
op|'.'
name|'HTTPServiceUnavailable'
newline|'\n'
name|'mock_multi_getattr'
op|'.'
name|'return_value'
op|'='
name|'test_obj'
newline|'\n'
name|'mock_get_client'
op|'.'
name|'return_value'
op|'='
name|'FAKE_CLIENT'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
name|'self'
op|'.'
name|'ironicclient'
op|'.'
name|'call'
op|','
nl|'\n'
string|'"node.list"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'test_obj'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_multi_getattr'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'client_wrapper'
op|'.'
name|'IronicClientWrapper'
op|','
string|"'_get_client'"
op|')'
newline|'\n'
DECL|member|test_call_fail_unexpected_exception
name|'def'
name|'test_call_fail_unexpected_exception'
op|'('
name|'self'
op|','
name|'mock_get_client'
op|','
nl|'\n'
name|'mock_multi_getattr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_obj'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'test_obj'
op|'.'
name|'side_effect'
op|'='
name|'ironic_exception'
op|'.'
name|'HTTPNotFound'
newline|'\n'
name|'mock_multi_getattr'
op|'.'
name|'return_value'
op|'='
name|'test_obj'
newline|'\n'
name|'mock_get_client'
op|'.'
name|'return_value'
op|'='
name|'FAKE_CLIENT'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ironic_exception'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ironicclient'
op|'.'
name|'call'
op|','
string|'"node.list"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ironic_client'
op|','
string|"'get_client'"
op|')'
newline|'\n'
DECL|member|test__get_client_unauthorized
name|'def'
name|'test__get_client_unauthorized'
op|'('
name|'self'
op|','
name|'mock_get_client'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_client'
op|'.'
name|'side_effect'
op|'='
name|'ironic_exception'
op|'.'
name|'Unauthorized'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ironicclient'
op|'.'
name|'_get_client'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ironic_client'
op|','
string|"'get_client'"
op|')'
newline|'\n'
DECL|member|test__get_client_unexpected_exception
name|'def'
name|'test__get_client_unexpected_exception'
op|'('
name|'self'
op|','
name|'mock_get_client'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_client'
op|'.'
name|'side_effect'
op|'='
name|'ironic_exception'
op|'.'
name|'ConnectionRefused'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ironic_exception'
op|'.'
name|'ConnectionRefused'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ironicclient'
op|'.'
name|'_get_client'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__multi_getattr_good
dedent|''
name|'def'
name|'test__multi_getattr_good'
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
name|'ironicclient'
op|'.'
name|'_multi_getattr'
op|'('
name|'FAKE_CLIENT'
op|','
string|'"node.list"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'FAKE_CLIENT'
op|'.'
name|'node'
op|'.'
name|'list'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__multi_getattr_fail
dedent|''
name|'def'
name|'test__multi_getattr_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AttributeError'
op|','
name|'self'
op|'.'
name|'ironicclient'
op|'.'
name|'_multi_getattr'
op|','
nl|'\n'
name|'FAKE_CLIENT'
op|','
string|'"nonexistent"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
