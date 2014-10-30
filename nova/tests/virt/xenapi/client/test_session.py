begin_unit
comment|'# Copyright (c) 2014 Rackspace Hosting'
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
name|'errno'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'client'
name|'import'
name|'session'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SessionTestCase
name|'class'
name|'SessionTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'session'
op|'.'
name|'XenAPISession'
op|','
string|"'_create_session'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'session'
op|'.'
name|'XenAPISession'
op|','
string|"'_get_product_version_and_brand'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'session'
op|'.'
name|'XenAPISession'
op|','
string|"'_verify_plugin_version'"
op|')'
newline|'\n'
DECL|member|test_session_passes_version
name|'def'
name|'test_session_passes_version'
op|'('
name|'self'
op|','
name|'mock_verify'
op|','
name|'mock_version'
op|','
nl|'\n'
name|'create_session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sess'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'create_session'
op|'.'
name|'return_value'
op|'='
name|'sess'
newline|'\n'
name|'mock_version'
op|'.'
name|'return_value'
op|'='
op|'('
string|"'version'"
op|','
string|"'brand'"
op|')'
newline|'\n'
nl|'\n'
name|'session'
op|'.'
name|'XenAPISession'
op|'('
string|"'url'"
op|','
string|"'username'"
op|','
string|"'password'"
op|')'
newline|'\n'
nl|'\n'
name|'expected_version'
op|'='
string|"'%s %s %s'"
op|'%'
op|'('
name|'version'
op|'.'
name|'vendor_string'
op|'('
op|')'
op|','
nl|'\n'
name|'version'
op|'.'
name|'product_string'
op|'('
op|')'
op|','
nl|'\n'
name|'version'
op|'.'
name|'version_string_with_package'
op|'('
op|')'
op|')'
newline|'\n'
name|'sess'
op|'.'
name|'login_with_password'
op|'.'
name|'assert_called_with'
op|'('
string|"'username'"
op|','
string|"'password'"
op|','
nl|'\n'
name|'expected_version'
op|','
nl|'\n'
string|"'OpenStack'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApplySessionHelpersTestCase
dedent|''
dedent|''
name|'class'
name|'ApplySessionHelpersTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
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
name|'ApplySessionHelpersTestCase'
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
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'apply_session_helpers'
op|'('
name|'self'
op|'.'
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_VM
dedent|''
name|'def'
name|'test_apply_session_helpers_add_VM'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"VM.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_SR
dedent|''
name|'def'
name|'test_apply_session_helpers_add_SR'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'SR'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"SR.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_VDI
dedent|''
name|'def'
name|'test_apply_session_helpers_add_VDI'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'VDI'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"VDI.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_VBD
dedent|''
name|'def'
name|'test_apply_session_helpers_add_VBD'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'VBD'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"VBD.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_PBD
dedent|''
name|'def'
name|'test_apply_session_helpers_add_PBD'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'PBD'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"PBD.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_PIF
dedent|''
name|'def'
name|'test_apply_session_helpers_add_PIF'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'PIF'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"PIF.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_VLAN
dedent|''
name|'def'
name|'test_apply_session_helpers_add_VLAN'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'VLAN'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"VLAN.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_host
dedent|''
name|'def'
name|'test_apply_session_helpers_add_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'host'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"host.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_network
dedent|''
name|'def'
name|'test_apply_session_helpers_add_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'network'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"network.get_X"'
op|','
nl|'\n'
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_apply_session_helpers_add_pool
dedent|''
name|'def'
name|'test_apply_session_helpers_add_pool'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'pool'
op|'.'
name|'get_X'
op|'('
string|'"ref"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"pool.get_X"'
op|','
string|'"ref"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CallPluginTestCase
dedent|''
dedent|''
name|'class'
name|'CallPluginTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
op|')'
op|':'
newline|'\n'
DECL|member|_get_fake_xapisession
indent|'    '
name|'def'
name|'_get_fake_xapisession'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeXapiSession
indent|'        '
name|'class'
name|'FakeXapiSession'
op|'('
name|'session'
op|'.'
name|'XenAPISession'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
string|'"Skip the superclass\'s dirty init"'
newline|'\n'
name|'self'
op|'.'
name|'XenAPI'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'FakeXapiSession'
op|'('
op|')'
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
name|'CallPluginTestCase'
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
name|'session'
op|'='
name|'self'
op|'.'
name|'_get_fake_xapisession'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialized_with_retry_socket_error_conn_reset
dedent|''
name|'def'
name|'test_serialized_with_retry_socket_error_conn_reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exc'
op|'='
name|'socket'
op|'.'
name|'error'
newline|'\n'
name|'exc'
op|'.'
name|'errno'
op|'='
name|'errno'
op|'.'
name|'ECONNRESET'
newline|'\n'
name|'plugin'
op|'='
string|"'glance'"
newline|'\n'
name|'fn'
op|'='
string|"'download_vhd'"
newline|'\n'
name|'num_retries'
op|'='
number|'1'
newline|'\n'
name|'callback'
op|'='
name|'None'
newline|'\n'
name|'retry_cb'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|','
nl|'\n'
name|'autospec'
op|'='
name|'True'
op|')'
name|'as'
name|'call_plugin_serialized'
op|':'
newline|'\n'
indent|'            '
name|'call_plugin_serialized'
op|'.'
name|'side_effect'
op|'='
name|'exc'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PluginRetriesExceeded'
op|','
nl|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized_with_retry'
op|','
name|'plugin'
op|','
name|'fn'
op|','
nl|'\n'
name|'num_retries'
op|','
name|'callback'
op|','
name|'retry_cb'
op|')'
newline|'\n'
name|'call_plugin_serialized'
op|'.'
name|'assert_called_with'
op|'('
name|'plugin'
op|','
name|'fn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'call_plugin_serialized'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'retry_cb'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialized_with_retry_socket_error_reraised
dedent|''
dedent|''
name|'def'
name|'test_serialized_with_retry_socket_error_reraised'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exc'
op|'='
name|'socket'
op|'.'
name|'error'
newline|'\n'
name|'exc'
op|'.'
name|'errno'
op|'='
name|'errno'
op|'.'
name|'ECONNREFUSED'
newline|'\n'
name|'plugin'
op|'='
string|"'glance'"
newline|'\n'
name|'fn'
op|'='
string|"'download_vhd'"
newline|'\n'
name|'num_retries'
op|'='
number|'1'
newline|'\n'
name|'callback'
op|'='
name|'None'
newline|'\n'
name|'retry_cb'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|','
nl|'\n'
name|'autospec'
op|'='
name|'True'
op|')'
name|'as'
name|'call_plugin_serialized'
op|':'
newline|'\n'
indent|'            '
name|'call_plugin_serialized'
op|'.'
name|'side_effect'
op|'='
name|'exc'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'socket'
op|'.'
name|'error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized_with_retry'
op|','
name|'plugin'
op|','
name|'fn'
op|','
nl|'\n'
name|'num_retries'
op|','
name|'callback'
op|','
name|'retry_cb'
op|')'
newline|'\n'
name|'call_plugin_serialized'
op|'.'
name|'assert_called_once_with'
op|'('
name|'plugin'
op|','
name|'fn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'retry_cb'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialized_with_retry_socket_reset_reraised
dedent|''
dedent|''
name|'def'
name|'test_serialized_with_retry_socket_reset_reraised'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exc'
op|'='
name|'socket'
op|'.'
name|'error'
newline|'\n'
name|'exc'
op|'.'
name|'errno'
op|'='
name|'errno'
op|'.'
name|'ECONNRESET'
newline|'\n'
name|'plugin'
op|'='
string|"'glance'"
newline|'\n'
name|'fn'
op|'='
string|"'download_vhd'"
newline|'\n'
name|'num_retries'
op|'='
number|'1'
newline|'\n'
name|'callback'
op|'='
name|'None'
newline|'\n'
name|'retry_cb'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|','
nl|'\n'
name|'autospec'
op|'='
name|'True'
op|')'
name|'as'
name|'call_plugin_serialized'
op|':'
newline|'\n'
indent|'            '
name|'call_plugin_serialized'
op|'.'
name|'side_effect'
op|'='
name|'exc'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PluginRetriesExceeded'
op|','
nl|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized_with_retry'
op|','
name|'plugin'
op|','
name|'fn'
op|','
nl|'\n'
name|'num_retries'
op|','
name|'callback'
op|','
name|'retry_cb'
op|')'
newline|'\n'
name|'call_plugin_serialized'
op|'.'
name|'assert_called_with'
op|'('
name|'plugin'
op|','
name|'fn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'call_plugin_serialized'
op|'.'
name|'call_count'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
