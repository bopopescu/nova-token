begin_unit
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
string|'"""Tests for the testing base code."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fixtures'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_local'"
op|','
string|"'nova.conductor.api'"
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IsolationTestCase
name|'class'
name|'IsolationTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that things are cleaned up after failed tests.\n\n    These tests don\'t really do much here, but if isolation fails a bunch\n    of other tests should fail.\n\n    """'
newline|'\n'
DECL|member|test_service_isolation
name|'def'
name|'test_service_isolation'
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
name|'use_local'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'ServiceFixture'
op|'('
string|"'compute'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rpc_consumer_isolation
dedent|''
name|'def'
name|'test_rpc_consumer_isolation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|NeverCalled
indent|'        '
name|'class'
name|'NeverCalled'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__getattribute__
indent|'            '
name|'def'
name|'__getattribute__'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'assert'
name|'False'
op|','
string|'"I should never get called."'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'server'
op|'='
name|'rpc'
op|'.'
name|'get_server'
op|'('
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'server'
op|'='
name|'CONF'
op|'.'
name|'host'
op|')'
op|','
nl|'\n'
name|'endpoints'
op|'='
op|'['
name|'NeverCalled'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BadLogTestCase
dedent|''
dedent|''
name|'class'
name|'BadLogTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make sure a mis-formatted debug log will get caught."""'
newline|'\n'
nl|'\n'
DECL|member|test_bad_debug_log
name|'def'
name|'test_bad_debug_log'
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
name|'KeyError'
op|','
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|','
string|'"this is a misformated %(log)s"'
op|','
op|'{'
string|"'nothing'"
op|':'
string|"'nothing'"
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
