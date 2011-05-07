begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifier'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'notifier'
name|'import'
name|'no_op_notifier'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|class|NotifierTestCase
name|'class'
name|'NotifierTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for notifications"""'
newline|'\n'
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
name|'NotifierTestCase'
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
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
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
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'NotifierTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_notification
dedent|''
name|'def'
name|'test_send_notification'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'notify_called'
op|'='
name|'False'
newline|'\n'
DECL|function|mock_notify
name|'def'
name|'mock_notify'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'notify_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'no_op_notifier'
op|'.'
name|'NoopNotifier'
op|','
string|"'notify'"
op|','
nl|'\n'
name|'mock_notify'
op|')'
newline|'\n'
nl|'\n'
DECL|class|Mock
name|'class'
name|'Mock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'notifier'
op|'.'
name|'notify'
op|'('
string|"'derp'"
op|','
name|'Mock'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'notify_called'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_rabbit_notification
dedent|''
name|'def'
name|'test_send_rabbit_notification'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'notification_driver'"
op|','
nl|'\n'
string|"'nova.notifier.rabbit_notifier.RabbitNotifier'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_cast'
op|'='
name|'False'
newline|'\n'
DECL|function|mock_cast
name|'def'
name|'mock_cast'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mock_cast'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|class|Mock
dedent|''
name|'class'
name|'Mock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'rpc'
op|','
string|"'cast'"
op|','
name|'mock_cast'
op|')'
newline|'\n'
name|'notifier'
op|'.'
name|'notify'
op|'('
string|"'derp'"
op|','
name|'Mock'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'mock_cast'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_error_notification
dedent|''
name|'def'
name|'test_error_notification'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'notification_driver'"
op|','
nl|'\n'
string|"'nova.notifier.rabbit_notifier.RabbitNotifier'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'publish_errors'"
op|','
name|'True'
op|')'
newline|'\n'
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'nova'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'setup_from_flags'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'msgs'
op|'='
op|'['
op|']'
newline|'\n'
DECL|function|mock_cast
name|'def'
name|'mock_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'msgs'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'rpc'
op|','
string|"'cast'"
op|','
name|'mock_cast'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|"'foo'"
op|')'
op|';'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'msgs'
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'msgs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|'['
string|"'event_name'"
op|']'
op|','
string|"'error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|'['
string|"'model'"
op|']'
op|'['
string|"'msg'"
op|']'
op|','
string|"'foo'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
