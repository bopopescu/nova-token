begin_unit
comment|'# Copyright 2015 OpenStack Foundation'
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
name|'mock'
newline|'\n'
nl|'\n'
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
DECL|class|TestNotifier
name|'class'
name|'TestNotifier'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'oslo_messaging.get_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'oslo_messaging.get_notification_transport'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'oslo_messaging.Notifier'"
op|')'
newline|'\n'
DECL|member|test_notification_format_affects_notification_driver
name|'def'
name|'test_notification_format_affects_notification_driver'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_notifier'
op|','
nl|'\n'
name|'mock_noti_trans'
op|','
nl|'\n'
name|'mock_transport'
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
nl|'\n'
name|'cases'
op|'='
op|'{'
nl|'\n'
string|"'unversioned'"
op|':'
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'serializer'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'serializer'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'driver'
op|'='
string|"'noop'"
op|')'
op|']'
op|','
nl|'\n'
string|"'both'"
op|':'
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'serializer'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'serializer'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'topics'
op|'='
op|'['
string|"'versioned_notifications'"
op|']'
op|')'
op|']'
op|','
nl|'\n'
string|"'versioned'"
op|':'
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'serializer'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'driver'
op|'='
string|"'noop'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'serializer'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'topics'
op|'='
op|'['
string|"'versioned_notifications'"
op|']'
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'config'
name|'in'
name|'cases'
op|':'
newline|'\n'
indent|'            '
name|'mock_notifier'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'mock_notifier'
op|'.'
name|'side_effect'
op|'='
op|'['
string|"'first'"
op|','
string|"'second'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'notification_format'
op|'='
name|'config'
newline|'\n'
name|'rpc'
op|'.'
name|'init'
op|'('
name|'conf'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cases'
op|'['
name|'config'
op|']'
op|','
name|'mock_notifier'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'first'"
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
string|"'second'"
op|','
name|'rpc'
op|'.'
name|'NOTIFIER'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
