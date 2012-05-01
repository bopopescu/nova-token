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
name|'eventlet'
name|'import'
name|'greenthread'
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
name|'db'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|test_service_opts
name|'test_service_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"fake_manager"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"nova.tests.test_service.FakeManager"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Manager for testing"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"test_service_listen"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Host to bind test service to"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"test_service_listen_port"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Port number to bind test service to"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'test_service_opts'
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
DECL|member|test_method
name|'def'
name|'test_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'manager'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedService
dedent|''
dedent|''
name|'class'
name|'ExtendedService'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
DECL|member|test_method
indent|'    '
name|'def'
name|'test_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'service'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceManagerTestCase
dedent|''
dedent|''
name|'class'
name|'ServiceManagerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for Services"""'
newline|'\n'
nl|'\n'
DECL|member|test_message_gets_to_manager
name|'def'
name|'test_message_gets_to_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'nova.tests.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'serv'
op|'.'
name|'test_method'
op|'('
op|')'
op|','
string|"'manager'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_override_manager_method
dedent|''
name|'def'
name|'test_override_manager_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serv'
op|'='
name|'ExtendedService'
op|'('
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'nova.tests.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'serv'
op|'.'
name|'test_method'
op|'('
op|')'
op|','
string|"'service'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceFlagsTestCase
dedent|''
dedent|''
name|'class'
name|'ServiceFlagsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_service_enabled_on_create_based_on_flag
indent|'    '
name|'def'
name|'test_service_enabled_on_create_based_on_flag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_new_services'
op|'='
name|'True'
op|')'
newline|'\n'
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'nova-fake'"
newline|'\n'
name|'app'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'host'
op|'='
name|'host'
op|','
name|'binary'
op|'='
name|'binary'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'app'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'ref'
op|'['
string|"'disabled'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_disabled_on_create_based_on_flag
dedent|''
name|'def'
name|'test_service_disabled_on_create_based_on_flag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_new_services'
op|'='
name|'False'
op|')'
newline|'\n'
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'nova-fake'"
newline|'\n'
name|'app'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'host'
op|'='
name|'host'
op|','
name|'binary'
op|'='
name|'binary'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'app'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'ref'
op|'['
string|"'disabled'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceTestCase
dedent|''
dedent|''
name|'class'
name|'ServiceTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for Services"""'
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
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'nova-fake'"
newline|'\n'
name|'topic'
op|'='
string|"'fake'"
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): Create was moved out of mox replay to make sure that'
nl|'\n'
comment|'#             the looping calls are created in StartService.'
nl|'\n'
name|'app'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'host'
op|'='
name|'host'
op|','
name|'binary'
op|'='
name|'binary'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'app'
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
name|'topic'
op|'='
string|"'test'"
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
string|"'topic'"
op|':'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'nova'"
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
string|"'topic'"
op|':'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'nova'"
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
name|'service_get_by_args'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
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
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'service_create'
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
name|'service_get'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
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
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'host'
op|','
nl|'\n'
name|'binary'
op|','
nl|'\n'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'report_state'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'serv'
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
name|'topic'
op|'='
string|"'test'"
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
string|"'topic'"
op|':'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'nova'"
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
string|"'topic'"
op|':'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'nova'"
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
name|'service_get_by_args'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
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
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'service_create'
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
name|'service_get'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
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
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
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
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'host'
op|','
nl|'\n'
name|'binary'
op|','
nl|'\n'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'serv'
op|'.'
name|'report_state'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'serv'
op|'.'
name|'model_disconnected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestWSGIService
dedent|''
dedent|''
name|'class'
name|'TestWSGIService'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestWSGIService'
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
op|'.'
name|'Set'
op|'('
name|'wsgi'
op|'.'
name|'Loader'
op|','
string|'"load_app"'
op|','
name|'mox'
op|'.'
name|'MockAnything'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_random_port
dedent|''
name|'def'
name|'test_service_random_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"test_service"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'test_service'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'test_service'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLauncher
dedent|''
dedent|''
name|'class'
name|'TestLauncher'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestLauncher'
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
op|'.'
name|'Set'
op|'('
name|'wsgi'
op|'.'
name|'Loader'
op|','
string|'"load_app"'
op|','
name|'mox'
op|'.'
name|'MockAnything'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"test_service"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_launch_app
dedent|''
name|'def'
name|'test_launch_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'service'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'launcher'
op|'='
name|'service'
op|'.'
name|'Launcher'
op|'('
op|')'
newline|'\n'
name|'launcher'
op|'.'
name|'launch_server'
op|'('
name|'self'
op|'.'
name|'service'
op|')'
newline|'\n'
comment|'# Give spawned thread a chance to execute'
nl|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEquals'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'service'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'launcher'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
