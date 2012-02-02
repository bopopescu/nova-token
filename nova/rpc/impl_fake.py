begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
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
string|'"""Fake RPC implementation which calls proxy methods directly with no\nqueues.  Casts will block, but this is very useful for tests.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
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
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
newline|'\n'
nl|'\n'
DECL|variable|CONSUMERS
name|'CONSUMERS'
op|'='
op|'{'
op|'}'
newline|'\n'
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
DECL|class|RpcContext
name|'class'
name|'RpcContext'
op|'('
name|'context'
op|'.'
name|'RequestContext'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'RpcContext'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_response'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_done'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|reply
dedent|''
name|'def'
name|'reply'
op|'('
name|'self'
op|','
name|'reply'
op|'='
name|'None'
op|','
name|'failure'
op|'='
name|'None'
op|','
name|'ending'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ending'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_done'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_done'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_response'
op|'.'
name|'append'
op|'('
op|'('
name|'reply'
op|','
name|'failure'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Consumer
dedent|''
dedent|''
dedent|''
name|'class'
name|'Consumer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'proxy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'topic'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'proxy'
op|'='
name|'proxy'
newline|'\n'
nl|'\n'
DECL|member|call
dedent|''
name|'def'
name|'call'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'method'
op|','
name|'args'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node_func'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'proxy'
op|','
name|'method'
op|')'
newline|'\n'
name|'node_args'
op|'='
name|'dict'
op|'('
op|'('
name|'str'
op|'('
name|'k'
op|')'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'args'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
name|'done'
op|'='
name|'eventlet'
op|'.'
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_inner
name|'def'
name|'_inner'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'RpcContext'
op|'.'
name|'from_dict'
op|'('
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'rval'
op|'='
name|'node_func'
op|'('
name|'context'
op|'='
name|'ctxt'
op|','
op|'**'
name|'node_args'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# Caller might have called ctxt.reply() manually'
nl|'\n'
name|'for'
op|'('
name|'reply'
op|','
name|'failure'
op|')'
name|'in'
name|'ctxt'
op|'.'
name|'_response'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'failure'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
name|'failure'
op|'['
number|'0'
op|']'
op|','
name|'failure'
op|'['
number|'1'
op|']'
op|','
name|'failure'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'res'
op|'.'
name|'append'
op|'('
name|'reply'
op|')'
newline|'\n'
comment|"# if ending not 'sent'...we might have more data to"
nl|'\n'
comment|'# return from the function itself'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'ctxt'
op|'.'
name|'_done'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'rval'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'for'
name|'val'
name|'in'
name|'rval'
op|':'
newline|'\n'
indent|'                            '
name|'res'
op|'.'
name|'append'
op|'('
name|'val'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'res'
op|'.'
name|'append'
op|'('
name|'rval'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'done'
op|'.'
name|'send'
op|'('
name|'res'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'exc_info'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
nl|'\n'
name|'rpc_common'
op|'.'
name|'RemoteError'
op|'('
name|'exc_info'
op|'['
number|'0'
op|']'
op|'.'
name|'__name__'
op|','
nl|'\n'
name|'str'
op|'('
name|'exc_info'
op|'['
number|'1'
op|']'
op|')'
op|','
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
name|'traceback'
op|'.'
name|'format_exception'
op|'('
op|'*'
name|'exc_info'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'thread'
op|'='
name|'eventlet'
op|'.'
name|'greenthread'
op|'.'
name|'spawn'
op|'('
name|'_inner'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'timeout'
op|':'
newline|'\n'
indent|'            '
name|'start_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'while'
name|'not'
name|'done'
op|'.'
name|'ready'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'eventlet'
op|'.'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'cur_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'if'
op|'('
name|'cur_time'
op|'-'
name|'start_time'
op|')'
op|'>'
name|'timeout'
op|':'
newline|'\n'
indent|'                    '
name|'thread'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'rpc_common'
op|'.'
name|'Timeout'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Connection
dedent|''
dedent|''
name|'class'
name|'Connection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Connection object."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'consumers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|create_consumer
dedent|''
name|'def'
name|'create_consumer'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'proxy'
op|','
name|'fanout'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'consumer'
op|'='
name|'Consumer'
op|'('
name|'topic'
op|','
name|'proxy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'consumers'
op|'.'
name|'append'
op|'('
name|'consumer'
op|')'
newline|'\n'
name|'if'
name|'topic'
name|'not'
name|'in'
name|'CONSUMERS'
op|':'
newline|'\n'
indent|'            '
name|'CONSUMERS'
op|'['
name|'topic'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'CONSUMERS'
op|'['
name|'topic'
op|']'
op|'.'
name|'append'
op|'('
name|'consumer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'consumer'
name|'in'
name|'self'
op|'.'
name|'consumers'
op|':'
newline|'\n'
indent|'            '
name|'CONSUMERS'
op|'['
name|'consumer'
op|'.'
name|'topic'
op|']'
op|'.'
name|'remove'
op|'('
name|'consumer'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'consumers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|consume_in_thread
dedent|''
name|'def'
name|'consume_in_thread'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_connection
dedent|''
dedent|''
name|'def'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a connection"""'
newline|'\n'
name|'return'
name|'Connection'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|multicall
dedent|''
name|'def'
name|'multicall'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make a call that returns multiple times."""'
newline|'\n'
nl|'\n'
name|'method'
op|'='
name|'msg'
op|'.'
name|'get'
op|'('
string|"'method'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'method'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'args'
op|'='
name|'msg'
op|'.'
name|'get'
op|'('
string|"'args'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'consumer'
op|'='
name|'CONSUMERS'
op|'['
name|'topic'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'IndexError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iter'
op|'('
op|'['
name|'None'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'consumer'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'args'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|call
dedent|''
dedent|''
name|'def'
name|'call'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a topic and wait for a response."""'
newline|'\n'
name|'rv'
op|'='
name|'multicall'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|')'
newline|'\n'
comment|'# NOTE(vish): return the last result from the multicall'
nl|'\n'
name|'rv'
op|'='
name|'list'
op|'('
name|'rv'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'rv'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'rv'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast
dedent|''
name|'def'
name|'cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'call'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc_common'
op|'.'
name|'RemoteError'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
dedent|''
dedent|''
name|'def'
name|'notify'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cleanup
dedent|''
name|'def'
name|'cleanup'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fanout_cast
dedent|''
name|'def'
name|'fanout_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Cast to all consumers of a topic"""'
newline|'\n'
name|'method'
op|'='
name|'msg'
op|'.'
name|'get'
op|'('
string|"'method'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'method'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'args'
op|'='
name|'msg'
op|'.'
name|'get'
op|'('
string|"'args'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'consumer'
name|'in'
name|'CONSUMERS'
op|'.'
name|'get'
op|'('
name|'topic'
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'consumer'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'args'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc_common'
op|'.'
name|'RemoteError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
