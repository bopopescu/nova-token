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
string|'"""\nUnit Tests for remote procedure calls shared between all implementations\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'nose'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
op|'.'
name|'common'
name|'import'
name|'RemoteError'
op|','
name|'Timeout'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
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
nl|'\n'
DECL|class|_BaseRpcTestCase
name|'class'
name|'_BaseRpcTestCase'
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
op|','
name|'supports_timeouts'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'_BaseRpcTestCase'
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
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
name|'True'
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
name|'conn'
op|'.'
name|'create_consumer'
op|'('
string|"'test'"
op|','
name|'self'
op|'.'
name|'receiver'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'consume_in_thread'
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
name|'supports_timeouts'
op|'='
name|'supports_timeouts'
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
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'_BaseRpcTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
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
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'context'
op|','
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
DECL|member|test_call_succeed_despite_multiple_returns
dedent|''
name|'def'
name|'test_call_succeed_despite_multiple_returns'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
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
string|'"echo_three_times"'
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
op|'+'
number|'2'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_succeed_despite_multiple_returns_yield
dedent|''
name|'def'
name|'test_call_succeed_despite_multiple_returns_yield'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
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
string|'"echo_three_times_yield"'
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
op|'+'
number|'2'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multicall_succeed_once
dedent|''
name|'def'
name|'test_multicall_succeed_once'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'multicall'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
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
name|'for'
name|'i'
op|','
name|'x'
name|'in'
name|'enumerate'
op|'('
name|'result'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'i'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'should only receive one response'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|'+'
name|'i'
op|','
name|'x'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multicall_succeed_three_times
dedent|''
dedent|''
name|'def'
name|'test_multicall_succeed_three_times'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'multicall'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"echo_three_times"'
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
name|'for'
name|'i'
op|','
name|'x'
name|'in'
name|'enumerate'
op|'('
name|'result'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|'+'
name|'i'
op|','
name|'x'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multicall_three_nones
dedent|''
dedent|''
name|'def'
name|'test_multicall_three_nones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'multicall'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"multicall_three_nones"'
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
name|'for'
name|'i'
op|','
name|'x'
name|'in'
name|'enumerate'
op|'('
name|'result'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'x'
op|','
name|'None'
op|')'
newline|'\n'
comment|'# i should have been 0, 1, and finally 2:'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'i'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multicall_succeed_three_times_yield
dedent|''
name|'def'
name|'test_multicall_succeed_three_times_yield'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'multicall'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"echo_three_times_yield"'
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
name|'for'
name|'i'
op|','
name|'x'
name|'in'
name|'enumerate'
op|'('
name|'result'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|'+'
name|'i'
op|','
name|'x'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_context_passed
dedent|''
dedent|''
name|'def'
name|'test_context_passed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure a context is passed through rpc call."""'
newline|'\n'
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
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
string|'"""Test that exception gets passed back properly.\n\n        rpc.call returns a RemoteError object.  The value of the\n        exception is converted to a string, so we convert it back\n        to an int in the test.\n\n        """'
newline|'\n'
name|'value'
op|'='
number|'42'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'RemoteError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
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
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
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
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"should have thrown RemoteError"'
op|')'
newline|'\n'
dedent|''
name|'except'
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
DECL|member|test_nested_calls
dedent|''
dedent|''
name|'def'
name|'test_nested_calls'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that we can do an rpc.call inside another call."""'
newline|'\n'
DECL|class|Nested
name|'class'
name|'Nested'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|echo
name|'def'
name|'echo'
op|'('
name|'context'
op|','
name|'queue'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'                '
string|'"""Calls echo in the passed queue"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Nested received %(queue)s, %(value)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# TODO: so, it will replay the context and use the same REQID?'
nl|'\n'
comment|"# that's bizarre."
nl|'\n'
name|'ret'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'queue'
op|','
nl|'\n'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Nested return %s"'
op|')'
op|','
name|'ret'
op|')'
newline|'\n'
name|'return'
name|'value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'nested'
op|'='
name|'Nested'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
name|'True'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'create_consumer'
op|'('
string|"'nested'"
op|','
name|'nested'
op|','
name|'False'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'consume_in_thread'
op|'('
op|')'
newline|'\n'
name|'value'
op|'='
number|'42'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'nested'"
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
string|'"queue"'
op|':'
string|'"test"'
op|','
nl|'\n'
string|'"value"'
op|':'
name|'value'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
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
DECL|member|test_call_timeout
dedent|''
name|'def'
name|'test_call_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure rpc.call will time out"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'supports_timeouts'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'nose'
op|'.'
name|'SkipTest'
op|'('
name|'_'
op|'('
string|'"RPC backend does not support timeouts"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'value'
op|'='
number|'42'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'Timeout'
op|','
nl|'\n'
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"block"'
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
op|','
name|'timeout'
op|'='
number|'1'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"block"'
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
op|','
nl|'\n'
name|'timeout'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"should have thrown Timeout"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Timeout'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'pass'
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
string|'"""Simple Proxy class so the consumer has methods to call.\n\n    Uses static methods because we aren\'t actually storing any state.\n\n    """'
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
string|'"""Simply returns whatever value is sent in."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Received %s"'
op|')'
op|','
name|'value'
op|')'
newline|'\n'
name|'return'
name|'value'
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
string|'"""Returns dictionary version of context."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Received %s"'
op|')'
op|','
name|'context'
op|')'
newline|'\n'
name|'return'
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|echo_three_times
name|'def'
name|'echo_three_times'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'.'
name|'reply'
op|'('
name|'value'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'reply'
op|'('
name|'value'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'reply'
op|'('
name|'value'
op|'+'
number|'2'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'reply'
op|'('
name|'ending'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|multicall_three_nones
name|'def'
name|'multicall_three_nones'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'None'
newline|'\n'
name|'yield'
name|'None'
newline|'\n'
name|'yield'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|echo_three_times_yield
name|'def'
name|'echo_three_times_yield'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'value'
newline|'\n'
name|'yield'
name|'value'
op|'+'
number|'1'
newline|'\n'
name|'yield'
name|'value'
op|'+'
number|'2'
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
string|'"""Raises an exception with the value sent in."""'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|block
name|'def'
name|'block'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'2'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
