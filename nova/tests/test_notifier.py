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
name|'from'
name|'nova'
name|'import'
name|'notifier'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
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
name|'self'
op|','
name|'model'
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
name|'set'
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
name|'model'
op|'='
name|'dict'
op|'('
name|'x'
op|'='
number|'1'
op|','
name|'y'
op|'='
number|'2'
op|')'
newline|'\n'
name|'notifier'
op|'.'
name|'notify'
op|'('
name|'model'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'self'
op|'.'
name|'notify_called'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
