begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
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
nl|'\n'
string|'"""\nUnit Tests for remote procedure calls using queue\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
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
name|'flags'
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
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|'"fake_manager"'
op|','
string|'"nova.tests.service_unittest.FakeManager"'
op|','
nl|'\n'
string|'"Manager for testing"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeManager
name|'class'
name|'FakeManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fake manager for tests"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceTestCase
dedent|''
name|'class'
name|'ServiceTestCase'
op|'('
name|'test'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for rpc"""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable=C0103'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ServiceTestCase'
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
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'service'
op|','
string|"'db'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
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
name|'rpc'
op|','
nl|'\n'
string|"'AdapterConsumer'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'service'
op|'.'
name|'task'
op|','
string|"'LoopingCall'"
op|','
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'('
name|'connection'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'proxy'
op|'='
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|')'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'('
name|'connection'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
string|"'fake.%s'"
op|'%'
name|'FLAGS'
op|'.'
name|'host'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|')'
newline|'\n'
nl|'\n'
comment|"# Stub out looping call a bit needlessly since we don't have an easy"
nl|'\n'
comment|'# way to cancel it (yet) when the tests finishes'
nl|'\n'
name|'service'
op|'.'
name|'task'
op|'.'
name|'LoopingCall'
op|'('
nl|'\n'
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
nl|'\n'
name|'service'
op|'.'
name|'task'
op|'.'
name|'LoopingCall'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'task'
op|'.'
name|'LoopingCall'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'now'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'.'
name|'attach_to_twisted'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'.'
name|'attach_to_twisted'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'app'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'bin_name'
op|'='
string|"'nova-fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'app'
op|')'
newline|'\n'
nl|'\n'
comment|"# We're testing sort of weird behavior in how report_state decides"
nl|'\n'
comment|'# whether it is disconnected, it looks for a variable on itself called'
nl|'\n'
comment|"# 'model_disconnected' and report_state doesn't really do much so this"
nl|'\n'
comment|'# these are mostly just for coverage'
nl|'\n'
DECL|member|test_report_state
dedent|''
name|'def'
name|'test_report_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'bar'"
newline|'\n'
name|'service_ref'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'__getattr__'
op|'('
string|"'report_state'"
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'None'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'binary'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'service_ref'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_update'
op|'('
name|'None'
op|','
name|'service_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'ContainsKeyValue'
op|'('
string|"'report_count'"
op|','
number|'1'
op|')'
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
name|'s'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'s'
op|'.'
name|'report_state'
op|'('
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_state_no_service
dedent|''
name|'def'
name|'test_report_state_no_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'bar'"
newline|'\n'
name|'service_create'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|'}'
newline|'\n'
name|'service_ref'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'__getattr__'
op|'('
string|"'report_state'"
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'None'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'binary'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_create'
op|'('
name|'None'
op|','
nl|'\n'
name|'service_create'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'service_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_get'
op|'('
name|'None'
op|','
name|'service_ref'
op|'['
string|"'id'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'service_ref'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_update'
op|'('
name|'None'
op|','
name|'service_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'ContainsKeyValue'
op|'('
string|"'report_count'"
op|','
number|'1'
op|')'
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
name|'s'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'s'
op|'.'
name|'report_state'
op|'('
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_state_newly_disconnected
dedent|''
name|'def'
name|'test_report_state_newly_disconnected'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'bar'"
newline|'\n'
name|'service_ref'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'__getattr__'
op|'('
string|"'report_state'"
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'None'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'binary'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'Exception'
op|'('
op|')'
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
name|'s'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'s'
op|'.'
name|'report_state'
op|'('
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'s'
op|'.'
name|'model_disconnected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_state_newly_connected
dedent|''
name|'def'
name|'test_report_state_newly_connected'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'bar'"
newline|'\n'
name|'service_ref'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'__getattr__'
op|'('
string|"'report_state'"
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'None'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'binary'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'service_ref'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'db'
op|'.'
name|'service_update'
op|'('
name|'None'
op|','
name|'service_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'ContainsKeyValue'
op|'('
string|"'report_count'"
op|','
number|'1'
op|')'
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
name|'s'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'s'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'rv'
op|'='
name|'yield'
name|'s'
op|'.'
name|'report_state'
op|'('
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'s'
op|'.'
name|'model_disconnected'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
