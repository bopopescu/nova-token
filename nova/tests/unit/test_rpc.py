begin_unit
comment|'#    Copyright 2016 IBM Corp.'
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
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'testtools'
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
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Make a class that resets all of the global variables in nova.rpc'
nl|'\n'
DECL|class|RPCResetFixture
name|'class'
name|'RPCResetFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
DECL|member|_setUp
indent|'    '
name|'def'
name|'_setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'trans'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'rpc'
op|'.'
name|'TRANSPORT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'noti_trans'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'noti'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'rpc'
op|'.'
name|'NOTIFIER'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'all_mods'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'rpc'
op|'.'
name|'ALLOWED_EXMODS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mods'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'rpc'
op|'.'
name|'EXTRA_EXMODS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_reset_everything'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_reset_everything
dedent|''
name|'def'
name|'_reset_everything'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'='
name|'self'
op|'.'
name|'trans'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|'='
name|'self'
op|'.'
name|'noti_trans'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'='
name|'self'
op|'.'
name|'noti'
newline|'\n'
name|'rpc'
op|'.'
name|'ALLOWED_EXMODS'
op|'='
name|'self'
op|'.'
name|'all_mods'
newline|'\n'
name|'rpc'
op|'.'
name|'EXTRA_EXMODS'
op|'='
name|'self'
op|'.'
name|'ext_mods'
newline|'\n'
nl|'\n'
nl|'\n'
comment|"# We can't import nova.test.TestCase because that sets up an RPCFixture"
nl|'\n'
comment|'# that pretty much nullifies all of this testing'
nl|'\n'
DECL|class|TestRPC
dedent|''
dedent|''
name|'class'
name|'TestRPC'
op|'('
name|'testtools'
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
name|'TestRPC'
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
name|'useFixture'
op|'('
name|'RPCResetFixture'
op|'('
op|')'
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
name|'rpc'
op|','
string|"'get_allowed_exmods'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'rpc'
op|','
string|"'RequestContextSerializer'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'get_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'get_notification_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'Notifier'"
op|')'
newline|'\n'
DECL|member|test_init_unversioned
name|'def'
name|'test_init_unversioned'
op|'('
name|'self'
op|','
name|'mock_notif'
op|','
name|'mock_noti_trans'
op|','
name|'mock_trans'
op|','
nl|'\n'
name|'mock_ser'
op|','
name|'mock_exmods'
op|')'
op|':'
newline|'\n'
comment|'# The expected call to get the legacy notifier will require no new'
nl|'\n'
comment|'# kwargs, and we expect the new notifier will need the noop driver'
nl|'\n'
indent|'        '
name|'expected'
op|'='
op|'['
op|'{'
op|'}'
op|','
op|'{'
string|"'driver'"
op|':'
string|"'noop'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_test_init'
op|'('
name|'mock_notif'
op|','
name|'mock_noti_trans'
op|','
name|'mock_trans'
op|','
name|'mock_ser'
op|','
nl|'\n'
name|'mock_exmods'
op|','
string|"'unversioned'"
op|','
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
name|'rpc'
op|','
string|"'get_allowed_exmods'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'rpc'
op|','
string|"'RequestContextSerializer'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'get_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'get_notification_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'Notifier'"
op|')'
newline|'\n'
DECL|member|test_init_both
name|'def'
name|'test_init_both'
op|'('
name|'self'
op|','
name|'mock_notif'
op|','
name|'mock_noti_trans'
op|','
name|'mock_trans'
op|','
nl|'\n'
name|'mock_ser'
op|','
name|'mock_exmods'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'['
op|'{'
op|'}'
op|','
op|'{'
string|"'topic'"
op|':'
string|"'versioned_notifications'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_test_init'
op|'('
name|'mock_notif'
op|','
name|'mock_noti_trans'
op|','
name|'mock_trans'
op|','
name|'mock_ser'
op|','
nl|'\n'
name|'mock_exmods'
op|','
string|"'both'"
op|','
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
name|'rpc'
op|','
string|"'get_allowed_exmods'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'rpc'
op|','
string|"'RequestContextSerializer'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'get_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'get_notification_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'Notifier'"
op|')'
newline|'\n'
DECL|member|test_init_versioned
name|'def'
name|'test_init_versioned'
op|'('
name|'self'
op|','
name|'mock_notif'
op|','
name|'mock_noti_trans'
op|','
name|'mock_trans'
op|','
nl|'\n'
name|'mock_ser'
op|','
name|'mock_exmods'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'['
op|'{'
string|"'driver'"
op|':'
string|"'noop'"
op|'}'
op|','
op|'{'
string|"'topic'"
op|':'
string|"'versioned_notifications'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_test_init'
op|'('
name|'mock_notif'
op|','
name|'mock_noti_trans'
op|','
name|'mock_trans'
op|','
name|'mock_ser'
op|','
nl|'\n'
name|'mock_exmods'
op|','
string|"'versioned'"
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cleanup_transport_null
dedent|''
name|'def'
name|'test_cleanup_transport_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AssertionError'
op|','
name|'rpc'
op|'.'
name|'cleanup'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cleanup_notification_transport_null
dedent|''
name|'def'
name|'test_cleanup_notification_transport_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AssertionError'
op|','
name|'rpc'
op|'.'
name|'cleanup'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cleanup_legacy_notifier_null
dedent|''
name|'def'
name|'test_cleanup_legacy_notifier_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cleanup_notifier_null
dedent|''
name|'def'
name|'test_cleanup_notifier_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AssertionError'
op|','
name|'rpc'
op|'.'
name|'cleanup'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cleanup
dedent|''
name|'def'
name|'test_cleanup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'trans_cleanup'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'not_trans_cleanup'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'.'
name|'cleanup'
op|'='
name|'trans_cleanup'
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|'.'
name|'cleanup'
op|'='
name|'not_trans_cleanup'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'trans_cleanup'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'not_trans_cleanup'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'rpc'
op|'.'
name|'TRANSPORT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'rpc'
op|'.'
name|'NOTIFICATION_TRANSPORT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'rpc'
op|'.'
name|'NOTIFIER'
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
name|'messaging'
op|','
string|"'set_transport_defaults'"
op|')'
newline|'\n'
DECL|member|test_set_defaults
name|'def'
name|'test_set_defaults'
op|'('
name|'self'
op|','
name|'mock_set'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'control_exchange'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'set_defaults'
op|'('
name|'control_exchange'
op|')'
newline|'\n'
nl|'\n'
name|'mock_set'
op|'.'
name|'assert_called_once_with'
op|'('
name|'control_exchange'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_extra_exmods
dedent|''
name|'def'
name|'test_add_extra_exmods'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'EXTRA_EXMODS'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'add_extra_exmods'
op|'('
string|"'foo'"
op|','
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|','
name|'rpc'
op|'.'
name|'EXTRA_EXMODS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_clear_extra_exmods
dedent|''
name|'def'
name|'test_clear_extra_exmods'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'EXTRA_EXMODS'
op|'='
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'clear_extra_exmods'
op|'('
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
name|'rpc'
op|'.'
name|'EXTRA_EXMODS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_allowed_exmods
dedent|''
name|'def'
name|'test_get_allowed_exmods'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'ALLOWED_EXMODS'
op|'='
op|'['
string|"'foo'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'EXTRA_EXMODS'
op|'='
op|'['
string|"'bar'"
op|']'
newline|'\n'
nl|'\n'
name|'exmods'
op|'='
name|'rpc'
op|'.'
name|'get_allowed_exmods'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|','
name|'exmods'
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
name|'messaging'
op|','
string|"'TransportURL'"
op|')'
newline|'\n'
DECL|member|test_get_transport_url
name|'def'
name|'test_get_transport_url'
op|'('
name|'self'
op|','
name|'mock_url'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'CONF'
op|'='
name|'conf'
newline|'\n'
name|'mock_url'
op|'.'
name|'parse'
op|'.'
name|'return_value'
op|'='
string|"'foo'"
newline|'\n'
nl|'\n'
name|'url'
op|'='
name|'rpc'
op|'.'
name|'get_transport_url'
op|'('
name|'url_str'
op|'='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'url'
op|')'
newline|'\n'
name|'mock_url'
op|'.'
name|'parse'
op|'.'
name|'assert_called_once_with'
op|'('
name|'conf'
op|','
string|"'bar'"
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'TRANSPORT_ALIASES'
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
name|'messaging'
op|','
string|"'TransportURL'"
op|')'
newline|'\n'
DECL|member|test_get_transport_url_null
name|'def'
name|'test_get_transport_url_null'
op|'('
name|'self'
op|','
name|'mock_url'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'CONF'
op|'='
name|'conf'
newline|'\n'
name|'mock_url'
op|'.'
name|'parse'
op|'.'
name|'return_value'
op|'='
string|"'foo'"
newline|'\n'
nl|'\n'
name|'url'
op|'='
name|'rpc'
op|'.'
name|'get_transport_url'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'url'
op|')'
newline|'\n'
name|'mock_url'
op|'.'
name|'parse'
op|'.'
name|'assert_called_once_with'
op|'('
name|'conf'
op|','
name|'None'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'TRANSPORT_ALIASES'
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
name|'rpc'
op|','
string|"'RequestContextSerializer'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'RPCClient'"
op|')'
newline|'\n'
DECL|member|test_get_client
name|'def'
name|'test_get_client'
op|'('
name|'self'
op|','
name|'mock_client'
op|','
name|'mock_ser'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'tgt'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'ser'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_client'
op|'.'
name|'return_value'
op|'='
string|"'client'"
newline|'\n'
name|'mock_ser'
op|'.'
name|'return_value'
op|'='
name|'ser'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'tgt'
op|','
name|'version_cap'
op|'='
string|"'1.0'"
op|','
name|'serializer'
op|'='
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_ser'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'mock_client'
op|'.'
name|'assert_called_once_with'
op|'('
name|'rpc'
op|'.'
name|'TRANSPORT'
op|','
nl|'\n'
name|'tgt'
op|','
name|'version_cap'
op|'='
string|"'1.0'"
op|','
nl|'\n'
name|'serializer'
op|'='
name|'ser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'client'"
op|','
name|'client'
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
name|'rpc'
op|','
string|"'RequestContextSerializer'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'messaging'
op|','
string|"'get_rpc_server'"
op|')'
newline|'\n'
DECL|member|test_get_server
name|'def'
name|'test_get_server'
op|'('
name|'self'
op|','
name|'mock_get'
op|','
name|'mock_ser'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'TRANSPORT'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'ser'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'tgt'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'ends'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_ser'
op|'.'
name|'return_value'
op|'='
name|'ser'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
string|"'server'"
newline|'\n'
nl|'\n'
name|'server'
op|'='
name|'rpc'
op|'.'
name|'get_server'
op|'('
name|'tgt'
op|','
name|'ends'
op|','
name|'serializer'
op|'='
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_ser'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'rpc'
op|'.'
name|'TRANSPORT'
op|','
name|'tgt'
op|','
name|'ends'
op|','
nl|'\n'
name|'executor'
op|'='
string|"'eventlet'"
op|','
name|'serializer'
op|'='
name|'ser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'server'"
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_notifier
dedent|''
name|'def'
name|'test_get_notifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_prep'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_prep'
op|'.'
name|'return_value'
op|'='
string|"'notifier'"
newline|'\n'
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|'.'
name|'prepare'
op|'='
name|'mock_prep'
newline|'\n'
nl|'\n'
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
string|"'service'"
op|','
name|'publisher_id'
op|'='
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_prep'
op|'.'
name|'assert_called_once_with'
op|'('
name|'publisher_id'
op|'='
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'notifier'"
op|','
name|'notifier'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_notifier_null_publisher
dedent|''
name|'def'
name|'test_get_notifier_null_publisher'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_prep'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_prep'
op|'.'
name|'return_value'
op|'='
string|"'notifier'"
newline|'\n'
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|'.'
name|'prepare'
op|'='
name|'mock_prep'
newline|'\n'
nl|'\n'
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
string|"'service'"
op|','
name|'host'
op|'='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_prep'
op|'.'
name|'assert_called_once_with'
op|'('
name|'publisher_id'
op|'='
string|"'service.bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'notifier'"
op|','
name|'notifier'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_versioned_notifier
dedent|''
name|'def'
name|'test_get_versioned_notifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_prep'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_prep'
op|'.'
name|'return_value'
op|'='
string|"'notifier'"
newline|'\n'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'.'
name|'prepare'
op|'='
name|'mock_prep'
newline|'\n'
nl|'\n'
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_versioned_notifier'
op|'('
string|"'service.foo'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_prep'
op|'.'
name|'assert_called_once_with'
op|'('
name|'publisher_id'
op|'='
string|"'service.foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'notifier'"
op|','
name|'notifier'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_init
dedent|''
name|'def'
name|'_test_init'
op|'('
name|'self'
op|','
name|'mock_notif'
op|','
name|'mock_noti_trans'
op|','
name|'mock_trans'
op|','
name|'mock_ser'
op|','
nl|'\n'
name|'mock_exmods'
op|','
name|'notif_format'
op|','
name|'expected_driver_topic_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'legacy_notifier'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'notifier'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'notif_transport'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'transport'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'notification_format'
op|'='
name|'notif_format'
newline|'\n'
name|'mock_exmods'
op|'.'
name|'return_value'
op|'='
op|'['
string|"'foo'"
op|']'
newline|'\n'
name|'mock_trans'
op|'.'
name|'return_value'
op|'='
name|'transport'
newline|'\n'
name|'mock_noti_trans'
op|'.'
name|'return_value'
op|'='
name|'notif_transport'
newline|'\n'
name|'mock_ser'
op|'.'
name|'return_value'
op|'='
name|'serializer'
newline|'\n'
name|'mock_notif'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'legacy_notifier'
op|','
name|'notifier'
op|']'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'init'
op|'('
name|'conf'
op|')'
newline|'\n'
nl|'\n'
name|'mock_exmods'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'mock_trans'
op|'.'
name|'assert_called_once_with'
op|'('
name|'conf'
op|','
nl|'\n'
name|'allowed_remote_exmods'
op|'='
op|'['
string|"'foo'"
op|']'
op|','
nl|'\n'
name|'aliases'
op|'='
name|'rpc'
op|'.'
name|'TRANSPORT_ALIASES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'rpc'
op|'.'
name|'TRANSPORT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'rpc'
op|'.'
name|'NOTIFIER'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'legacy_notifier'
op|','
name|'rpc'
op|'.'
name|'LEGACY_NOTIFIER'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'notifier'
op|','
name|'rpc'
op|'.'
name|'NOTIFIER'
op|')'
newline|'\n'
nl|'\n'
name|'expected_calls'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'kwargs'
name|'in'
name|'expected_driver_topic_kwargs'
op|':'
newline|'\n'
indent|'            '
name|'expected_kwargs'
op|'='
op|'{'
string|"'serializer'"
op|':'
name|'serializer'
op|'}'
newline|'\n'
name|'expected_kwargs'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'expected_calls'
op|'.'
name|'append'
op|'('
op|'('
op|'('
name|'notif_transport'
op|','
op|')'
op|','
name|'expected_kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_calls'
op|','
name|'mock_notif'
op|'.'
name|'call_args_list'
op|','
nl|'\n'
string|'"The calls to messaging.Notifier() did not create "'
nl|'\n'
string|'"the legacy and versioned notifiers properly."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestJsonPayloadSerializer
dedent|''
dedent|''
name|'class'
name|'TestJsonPayloadSerializer'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_serialize_entity
indent|'    '
name|'def'
name|'test_serialize_entity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'jsonutils'
op|','
string|"'to_primitive'"
op|')'
name|'as'
name|'mock_prim'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'JsonPayloadSerializer'
op|'.'
name|'serialize_entity'
op|'('
string|"'context'"
op|','
string|"'entity'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_prim'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'entity'"
op|','
name|'convert_instances'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestRequestContextSerializer
dedent|''
dedent|''
name|'class'
name|'TestRequestContextSerializer'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'TestRequestContextSerializer'
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
name|'mock_base'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ser'
op|'='
name|'rpc'
op|'.'
name|'RequestContextSerializer'
op|'('
name|'self'
op|'.'
name|'mock_base'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ser_null'
op|'='
name|'rpc'
op|'.'
name|'RequestContextSerializer'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialize_entity
dedent|''
name|'def'
name|'test_serialize_entity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_base'
op|'.'
name|'serialize_entity'
op|'.'
name|'return_value'
op|'='
string|"'foo'"
newline|'\n'
nl|'\n'
name|'ser_ent'
op|'='
name|'self'
op|'.'
name|'ser'
op|'.'
name|'serialize_entity'
op|'('
string|"'context'"
op|','
string|"'entity'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_base'
op|'.'
name|'serialize_entity'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'context'"
op|','
nl|'\n'
string|"'entity'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'ser_ent'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialize_entity_null_base
dedent|''
name|'def'
name|'test_serialize_entity_null_base'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ser_ent'
op|'='
name|'self'
op|'.'
name|'ser_null'
op|'.'
name|'serialize_entity'
op|'('
string|"'context'"
op|','
string|"'entity'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'entity'"
op|','
name|'ser_ent'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserialize_entity
dedent|''
name|'def'
name|'test_deserialize_entity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_base'
op|'.'
name|'deserialize_entity'
op|'.'
name|'return_value'
op|'='
string|"'foo'"
newline|'\n'
nl|'\n'
name|'deser_ent'
op|'='
name|'self'
op|'.'
name|'ser'
op|'.'
name|'deserialize_entity'
op|'('
string|"'context'"
op|','
string|"'entity'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_base'
op|'.'
name|'deserialize_entity'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'context'"
op|','
nl|'\n'
string|"'entity'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'deser_ent'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserialize_entity_null_base
dedent|''
name|'def'
name|'test_deserialize_entity_null_base'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'deser_ent'
op|'='
name|'self'
op|'.'
name|'ser_null'
op|'.'
name|'deserialize_entity'
op|'('
string|"'context'"
op|','
string|"'entity'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'entity'"
op|','
name|'deser_ent'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialize_context
dedent|''
name|'def'
name|'test_serialize_context'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ser'
op|'.'
name|'serialize_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'context'
op|'.'
name|'to_dict'
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
name|'context'
op|','
string|"'RequestContext'"
op|')'
newline|'\n'
DECL|member|test_deserialize_context
name|'def'
name|'test_deserialize_context'
op|'('
name|'self'
op|','
name|'mock_req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ser'
op|'.'
name|'deserialize_context'
op|'('
string|"'context'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_req'
op|'.'
name|'from_dict'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'context'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
