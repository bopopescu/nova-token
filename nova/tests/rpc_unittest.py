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
string|'"""\nUnit Tests for remote procedure calls using queue\n"""'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
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
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RpcTestCase
name|'class'
name|'RpcTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for rpc"""'
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
name|'RpcTestCase'
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
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'receiver'
op|'='
name|'TestReceiver'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'consumer'
op|'='
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'('
name|'connection'
op|'='
name|'self'
op|'.'
name|'conn'
op|','
nl|'\n'
name|'topic'
op|'='
string|"'test'"
op|','
nl|'\n'
name|'proxy'
op|'='
name|'self'
op|'.'
name|'receiver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'consumer'
op|'.'
name|'attach_to_twisted'
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
nl|'\n'
DECL|member|test_call_succeed
dedent|''
name|'def'
name|'test_call_succeed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a value through rpc call"""'
newline|'\n'
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'yield'
name|'rpc'
op|'.'
name|'call_twisted'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
op|'{'
string|'"method"'
op|':'
string|'"echo"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"value"'
op|':'
name|'value'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_context_passed
dedent|''
name|'def'
name|'test_context_passed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure a context is passed through rpc call"""'
newline|'\n'
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'yield'
name|'rpc'
op|'.'
name|'call_twisted'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
op|'{'
string|'"method"'
op|':'
string|'"context"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"value"'
op|':'
name|'value'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_exception
dedent|''
name|'def'
name|'test_call_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that exception gets passed back properly\n\n        rpc.call returns a RemoteError object.  The value of the\n        exception is converted to a string, so we convert it back\n        to an int in the test.\n        """'
newline|'\n'
name|'value'
op|'='
number|'42'
newline|'\n'
name|'self'
op|'.'
name|'assertFailure'
op|'('
name|'rpc'
op|'.'
name|'call_twisted'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'test'"
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"fail"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"value"'
op|':'
name|'value'
op|'}'
op|'}'
op|')'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'RemoteError'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'rpc'
op|'.'
name|'call_twisted'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
op|'{'
string|'"method"'
op|':'
string|'"fail"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"value"'
op|':'
name|'value'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"should have thrown rpc.RemoteError"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'exc'
op|'.'
name|'value'
op|')'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestReceiver
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestReceiver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simple Proxy class so the consumer has methods to call\n\n    Uses static methods because we aren\'t actually storing any state"""'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|echo
name|'def'
name|'echo'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simply returns whatever value is sent in"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Received %s"'
op|','
name|'value'
op|')'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|context
name|'def'
name|'context'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns dictionary version of context"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Received %s"'
op|','
name|'context'
op|')'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|fail
name|'def'
name|'fail'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Raises an exception with the value sent in"""'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
