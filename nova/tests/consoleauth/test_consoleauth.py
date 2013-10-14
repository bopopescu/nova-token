begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nTests for Consoleauth Code.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'consoleauth'
name|'import'
name|'manager'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleauthTestCase
name|'class'
name|'ConsoleauthTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Case for consoleauth."""'
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
name|'ConsoleauthTestCase'
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
name|'manager_api'
op|'='
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'ConsoleAuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_tokens_expire
dedent|''
name|'def'
name|'test_tokens_expire'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test that tokens expire correctly.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'test'
op|'.'
name|'TimeOverride'
op|'('
op|')'
op|')'
newline|'\n'
name|'token'
op|'='
string|"u'mytok'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'console_token_ttl'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_stub_validate_console_port'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'authorize_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|','
string|"'novnc'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
string|"'8080'"
op|','
string|"'host'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'check_token'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|')'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'check_token'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_validate_console_port
dedent|''
name|'def'
name|'_stub_validate_console_port'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
DECL|function|fake_validate_console_port
indent|'        '
name|'def'
name|'fake_validate_console_port'
op|'('
name|'ctxt'
op|','
name|'instance'
op|','
name|'port'
op|','
name|'console_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'result'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'compute_rpcapi'
op|','
nl|'\n'
string|"'validate_console_port'"
op|','
nl|'\n'
name|'fake_validate_console_port'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_tokens_for_instance
dedent|''
name|'def'
name|'test_multiple_tokens_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tokens'
op|'='
op|'['
string|'u"token"'
op|'+'
name|'str'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_stub_validate_console_port'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'token'
name|'in'
name|'tokens'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'authorize_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|','
string|"'novnc'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
string|"'8080'"
op|','
string|"'host'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'token'
name|'in'
name|'tokens'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'check_token'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_tokens_for_instance
dedent|''
dedent|''
name|'def'
name|'test_delete_tokens_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tokens'
op|'='
op|'['
string|'u"token"'
op|'+'
name|'str'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|']'
newline|'\n'
name|'for'
name|'token'
name|'in'
name|'tokens'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'authorize_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|','
string|"'novnc'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
string|"'8080'"
op|','
string|"'host'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'delete_tokens_for_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'stored_tokens'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_get_tokens_for_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'stored_tokens'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'token'
name|'in'
name|'tokens'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'check_token'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wrong_token_has_port
dedent|''
dedent|''
name|'def'
name|'test_wrong_token_has_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'token'
op|'='
string|"u'mytok'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_stub_validate_console_port'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'authorize_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|','
string|"'novnc'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
string|"'8080'"
op|','
string|"'host'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'check_token'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_expired_tokens
dedent|''
name|'def'
name|'test_delete_expired_tokens'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'test'
op|'.'
name|'TimeOverride'
op|'('
op|')'
op|')'
newline|'\n'
name|'token'
op|'='
string|"u'mytok'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'console_token_ttl'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_stub_validate_console_port'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'authorize_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|','
string|"'novnc'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
string|"'8080'"
op|','
string|"'host'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'check_token'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'token1'
op|'='
string|"u'mytok2'"
newline|'\n'
name|'self'
op|'.'
name|'manager_api'
op|'.'
name|'authorize_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'token1'
op|','
string|"'novnc'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
string|"'8080'"
op|','
string|"'host'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'stored_tokens'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_get_tokens_for_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
comment|'# when trying to store token1, expired token is removed fist.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'stored_tokens'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'stored_tokens'
op|'['
number|'0'
op|']'
op|','
name|'token1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControlauthMemcacheEncodingTestCase
dedent|''
dedent|''
name|'class'
name|'ControlauthMemcacheEncodingTestCase'
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
name|'ControlauthMemcacheEncodingTestCase'
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
name|'manager'
op|'='
name|'manager'
op|'.'
name|'ConsoleAuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'u_token'
op|'='
string|'u"token"'
newline|'\n'
name|'self'
op|'.'
name|'u_instance'
op|'='
string|'u"instance"'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_console_encoding
dedent|''
name|'def'
name|'test_authorize_console_encoding'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|','
string|'"set"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|','
string|'"get"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|'.'
name|'get'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'authorize_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'u_token'
op|','
string|"'novnc'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
string|"'8080'"
op|','
string|"'host'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'u_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_token_encoding
dedent|''
name|'def'
name|'test_check_token_encoding'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|','
string|'"get"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|'.'
name|'get'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'check_token'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'u_token'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_tokens_for_instance_encoding
dedent|''
name|'def'
name|'test_delete_tokens_for_instance_encoding'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|','
string|'"delete"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|','
string|'"get"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|'.'
name|'get'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'\'["token"]\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|'.'
name|'delete'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'mc'
op|'.'
name|'delete'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_tokens_for_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'u_instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsConsoleauthTestCase
dedent|''
dedent|''
name|'class'
name|'CellsConsoleauthTestCase'
op|'('
name|'ConsoleauthTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Case for consoleauth w/ cells enabled."""'
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
name|'CellsConsoleauthTestCase'
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
name|'flags'
op|'('
name|'enable'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_validate_console_port
dedent|''
name|'def'
name|'_stub_validate_console_port'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
DECL|function|fake_validate_console_port
indent|'        '
name|'def'
name|'fake_validate_console_port'
op|'('
name|'ctxt'
op|','
name|'instance_uuid'
op|','
name|'console_port'
op|','
nl|'\n'
name|'console_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'result'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'cells_rpcapi'
op|','
nl|'\n'
string|"'validate_console_port'"
op|','
nl|'\n'
name|'fake_validate_console_port'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
