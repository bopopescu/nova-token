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
comment|'# Copyright 2011 - 2012, Red Hat, Inc.'
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
string|'"""\nShared code between AMQP based nova.rpc implementations.\n\nThe code in this module is shared between the rpc implemenations based on AMQP.\nSpecifically, this includes impl_kombu and impl_qpid.  impl_carrot also uses\nAMQP, but is deprecated and predates this code.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'pools'
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
name|'local'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'rpc'
op|'.'
name|'common'
name|'as'
name|'rpc_common'
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
DECL|class|Pool
name|'class'
name|'Pool'
op|'('
name|'pools'
op|'.'
name|'Pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class that implements a Pool of Connections."""'
newline|'\n'
DECL|member|__init__
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
name|'self'
op|'.'
name|'connection_cls'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|'"connection_cls"'
op|','
name|'None'
op|')'
newline|'\n'
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|'"max_size"'
op|','
name|'FLAGS'
op|'.'
name|'rpc_conn_pool_size'
op|')'
newline|'\n'
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|'"order_as_stack"'
op|','
name|'True'
op|')'
newline|'\n'
name|'super'
op|'('
name|'Pool'
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
nl|'\n'
comment|'# TODO(comstud): Timeout connections not used in a while'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Pool creating new connection'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection_cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|empty
dedent|''
name|'def'
name|'empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'while'
name|'self'
op|'.'
name|'free_items'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'get'
op|'('
op|')'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConnectionContext
dedent|''
dedent|''
dedent|''
name|'class'
name|'ConnectionContext'
op|'('
name|'rpc_common'
op|'.'
name|'Connection'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The class that is actually returned to the caller of\n    create_connection().  This is a essentially a wrapper around\n    Connection that supports \'with\' and can return a new Connection or\n    one from a pool.  It will also catch when an instance of this class\n    is to be deleted so that we can return Connections to the pool on\n    exceptions and so forth without making the caller be responsible for\n    catching all exceptions and making sure to return a connection to\n    the pool.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection_pool'
op|','
name|'pooled'
op|'='
name|'True'
op|','
name|'server_params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new connection, or get one from the pool"""'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'connection_pool'
op|'='
name|'connection_pool'
newline|'\n'
name|'if'
name|'pooled'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection_pool'
op|'.'
name|'get'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection_pool'
op|'.'
name|'connection_cls'
op|'('
nl|'\n'
name|'server_params'
op|'='
name|'server_params'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'pooled'
op|'='
name|'pooled'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""When with ConnectionContext() is used, return self"""'
newline|'\n'
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|_done
dedent|''
name|'def'
name|'_done'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""If the connection came from a pool, clean it up and put it back.\n        If it did not come from a pool, close it.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'connection'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'pooled'
op|':'
newline|'\n'
comment|"# Reset the connection so it's ready for the next caller"
nl|'\n'
comment|'# to grab from the pool'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'connection'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection_pool'
op|'.'
name|'put'
op|'('
name|'self'
op|'.'
name|'connection'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'connection'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'exc_type'
op|','
name|'exc_value'
op|','
name|'tb'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""End of \'with\' statement.  We\'re done here."""'
newline|'\n'
name|'self'
op|'.'
name|'_done'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__del__
dedent|''
name|'def'
name|'__del__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Caller is done with this connection.  Make sure we cleaned up."""'
newline|'\n'
name|'self'
op|'.'
name|'_done'
op|'('
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
string|'"""Caller is done with this connection."""'
newline|'\n'
name|'self'
op|'.'
name|'_done'
op|'('
op|')'
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
name|'self'
op|'.'
name|'connection'
op|'.'
name|'create_consumer'
op|'('
name|'topic'
op|','
name|'proxy'
op|','
name|'fanout'
op|')'
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
name|'self'
op|'.'
name|'connection'
op|'.'
name|'consume_in_thread'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Proxy all other calls to the Connection instance"""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'connection'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'connection'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidRPCConnectionReuse'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|msg_reply
dedent|''
dedent|''
dedent|''
name|'def'
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'connection_pool'
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
indent|'    '
string|'"""Sends a reply or an error on the channel signified by msg_id.\n\n    Failure should be a sys.exc_info() tuple.\n\n    """'
newline|'\n'
name|'with'
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|')'
name|'as'
name|'conn'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'failure'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
name|'str'
op|'('
name|'failure'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'tb'
op|'='
name|'traceback'
op|'.'
name|'format_exception'
op|'('
op|'*'
name|'failure'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Returning exception %s to caller"'
op|')'
op|','
name|'message'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'tb'
op|')'
newline|'\n'
name|'failure'
op|'='
op|'('
name|'failure'
op|'['
number|'0'
op|']'
op|'.'
name|'__name__'
op|','
name|'str'
op|'('
name|'failure'
op|'['
number|'1'
op|']'
op|')'
op|','
name|'tb'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'{'
string|"'result'"
op|':'
name|'reply'
op|','
string|"'failure'"
op|':'
name|'failure'
op|'}'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'{'
string|"'result'"
op|':'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'repr'
op|'('
name|'v'
op|')'
op|')'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'reply'
op|'.'
name|'__dict__'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'failure'"
op|':'
name|'failure'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'ending'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'['
string|"'ending'"
op|']'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'conn'
op|'.'
name|'direct_send'
op|'('
name|'msg_id'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RpcContext
dedent|''
dedent|''
name|'class'
name|'RpcContext'
op|'('
name|'context'
op|'.'
name|'RequestContext'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Context that supports replying to a rpc.call"""'
newline|'\n'
DECL|member|__init__
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
name|'self'
op|'.'
name|'msg_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'msg_id'"
op|','
name|'None'
op|')'
newline|'\n'
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
op|','
nl|'\n'
name|'connection_pool'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'msg_id'
op|':'
newline|'\n'
indent|'            '
name|'msg_reply'
op|'('
name|'self'
op|'.'
name|'msg_id'
op|','
name|'connection_pool'
op|','
name|'reply'
op|','
name|'failure'
op|','
nl|'\n'
name|'ending'
op|')'
newline|'\n'
name|'if'
name|'ending'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'msg_id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unpack_context
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'unpack_context'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unpack context from msg."""'
newline|'\n'
name|'context_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'list'
op|'('
name|'msg'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(vish): Some versions of python don't like unicode keys"
nl|'\n'
comment|'#             in kwargs.'
nl|'\n'
indent|'        '
name|'key'
op|'='
name|'str'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'key'
op|'.'
name|'startswith'
op|'('
string|"'_context_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'msg'
op|'.'
name|'pop'
op|'('
name|'key'
op|')'
newline|'\n'
name|'context_dict'
op|'['
name|'key'
op|'['
number|'9'
op|':'
op|']'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'context_dict'
op|'['
string|"'msg_id'"
op|']'
op|'='
name|'msg'
op|'.'
name|'pop'
op|'('
string|"'_msg_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'ctx'
op|'='
name|'RpcContext'
op|'.'
name|'from_dict'
op|'('
name|'context_dict'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'unpacked context: %s'"
op|')'
op|','
name|'ctx'
op|'.'
name|'to_dict'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'ctx'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pack_context
dedent|''
name|'def'
name|'pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pack context into msg.\n\n    Values for message keys need to be less than 255 chars, so we pull\n    context out into a bunch of separate keys. If we want to support\n    more arguments in rabbit messages, we may want to do the same\n    for args at some point.\n\n    """'
newline|'\n'
name|'context_d'
op|'='
name|'dict'
op|'('
op|'['
op|'('
string|"'_context_%s'"
op|'%'
name|'key'
op|','
name|'value'
op|')'
nl|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'msg'
op|'.'
name|'update'
op|'('
name|'context_d'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProxyCallback
dedent|''
name|'class'
name|'ProxyCallback'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Calls methods on a proxy object based on method and args."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'proxy'
op|','
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'proxy'
op|'='
name|'proxy'
newline|'\n'
name|'self'
op|'.'
name|'pool'
op|'='
name|'greenpool'
op|'.'
name|'GreenPool'
op|'('
name|'FLAGS'
op|'.'
name|'rpc_thread_pool_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection_pool'
op|'='
name|'connection_pool'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'message_data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Consumer callback to call a method on a proxy object.\n\n        Parses the message for validity and fires off a thread to call the\n        proxy object method.\n\n        Message data should be a dictionary with two keys:\n            method: string representing the method to call\n            args: dictionary of arg: value\n\n        Example: {\'method\': \'echo\', \'args\': {\'value\': 42}}\n\n        """'
newline|'\n'
comment|'# It is important to clear the context here, because at this point'
nl|'\n'
comment|'# the previous context is stored in local.store.context'
nl|'\n'
name|'if'
name|'hasattr'
op|'('
name|'local'
op|'.'
name|'store'
op|','
string|"'context'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'local'
op|'.'
name|'store'
op|'.'
name|'context'
newline|'\n'
dedent|''
name|'rpc_common'
op|'.'
name|'_safe_log'
op|'('
name|'LOG'
op|'.'
name|'debug'
op|','
name|'_'
op|'('
string|"'received %s'"
op|')'
op|','
name|'message_data'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'unpack_context'
op|'('
name|'message_data'
op|')'
newline|'\n'
name|'method'
op|'='
name|'message_data'
op|'.'
name|'get'
op|'('
string|"'method'"
op|')'
newline|'\n'
name|'args'
op|'='
name|'message_data'
op|'.'
name|'get'
op|'('
string|"'args'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'method'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'no method for message: %s'"
op|')'
op|'%'
name|'message_data'
op|')'
newline|'\n'
name|'ctxt'
op|'.'
name|'reply'
op|'('
name|'_'
op|'('
string|"'No method for message: %s'"
op|')'
op|'%'
name|'message_data'
op|','
nl|'\n'
name|'connection_pool'
op|'='
name|'self'
op|'.'
name|'connection_pool'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'pool'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_process_data'
op|','
name|'ctxt'
op|','
name|'method'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
DECL|member|_process_data
name|'def'
name|'_process_data'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'method'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Thread that magically looks for a method on the proxy\n        object and calls it.\n        """'
newline|'\n'
name|'ctxt'
op|'.'
name|'update_store'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'node_func'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'proxy'
op|','
name|'str'
op|'('
name|'method'
op|')'
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
comment|'# NOTE(vish): magic is fun!'
nl|'\n'
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
comment|'# Check if the result was a generator'
nl|'\n'
name|'if'
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'rval'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'x'
name|'in'
name|'rval'
op|':'
newline|'\n'
indent|'                    '
name|'ctxt'
op|'.'
name|'reply'
op|'('
name|'x'
op|','
name|'None'
op|','
name|'connection_pool'
op|'='
name|'self'
op|'.'
name|'connection_pool'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'ctxt'
op|'.'
name|'reply'
op|'('
name|'rval'
op|','
name|'None'
op|','
name|'connection_pool'
op|'='
name|'self'
op|'.'
name|'connection_pool'
op|')'
newline|'\n'
comment|'# This final None tells multicall that it is done.'
nl|'\n'
dedent|''
name|'ctxt'
op|'.'
name|'reply'
op|'('
name|'ending'
op|'='
name|'True'
op|','
name|'connection_pool'
op|'='
name|'self'
op|'.'
name|'connection_pool'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
string|"'Exception during message handling'"
op|')'
newline|'\n'
name|'ctxt'
op|'.'
name|'reply'
op|'('
name|'None'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|','
nl|'\n'
name|'connection_pool'
op|'='
name|'self'
op|'.'
name|'connection_pool'
op|')'
newline|'\n'
dedent|''
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MulticallWaiter
dedent|''
dedent|''
name|'class'
name|'MulticallWaiter'
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
name|'connection'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'_iterator'
op|'='
name|'connection'
op|'.'
name|'iterconsume'
op|'('
nl|'\n'
name|'timeout'
op|'='
name|'timeout'
name|'or'
name|'FLAGS'
op|'.'
name|'rpc_response_timeout'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_result'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_done'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'_got_ending'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|done
dedent|''
name|'def'
name|'done'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_done'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_done'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'_iterator'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_iterator'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The consume() callback will call this.  Store the result."""'
newline|'\n'
name|'if'
name|'data'
op|'['
string|"'failure'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_result'
op|'='
name|'rpc_common'
op|'.'
name|'RemoteError'
op|'('
op|'*'
name|'data'
op|'['
string|"'failure'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'data'
op|'.'
name|'get'
op|'('
string|"'ending'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_got_ending'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_result'
op|'='
name|'data'
op|'['
string|"'result'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
dedent|''
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a result until we get a \'None\' response from consumer"""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_done'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'StopIteration'
newline|'\n'
dedent|''
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_iterator'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_got_ending'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'done'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'StopIteration'
newline|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'_result'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'result'
op|','
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'done'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'result'
newline|'\n'
dedent|''
name|'yield'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_connection
dedent|''
dedent|''
dedent|''
name|'def'
name|'create_connection'
op|'('
name|'new'
op|','
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a connection"""'
newline|'\n'
name|'return'
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|','
name|'pooled'
op|'='
name|'not'
name|'new'
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
op|','
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make a call that returns multiple times."""'
newline|'\n'
comment|"# Can't use 'with' for multicall, as it returns an iterator"
nl|'\n'
comment|"# that will continue to use the connection.  When it's done,"
nl|'\n'
comment|'# connection.close() will get called which will put it back into'
nl|'\n'
comment|'# the pool'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Making asynchronous call on %s ...'"
op|')'
op|','
name|'topic'
op|')'
newline|'\n'
name|'msg_id'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
name|'msg'
op|'.'
name|'update'
op|'('
op|'{'
string|"'_msg_id'"
op|':'
name|'msg_id'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'MSG_ID is %s'"
op|')'
op|'%'
op|'('
name|'msg_id'
op|')'
op|')'
newline|'\n'
name|'pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|')'
newline|'\n'
name|'wait_msg'
op|'='
name|'MulticallWaiter'
op|'('
name|'conn'
op|','
name|'timeout'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'declare_direct_consumer'
op|'('
name|'msg_id'
op|','
name|'wait_msg'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'topic_send'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
name|'return'
name|'wait_msg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|call
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
op|','
name|'connection_pool'
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
op|','
name|'connection_pool'
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
op|','
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a topic without waiting for a response."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Making asynchronous cast on %s...'"
op|')'
op|','
name|'topic'
op|')'
newline|'\n'
name|'pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
name|'with'
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|')'
name|'as'
name|'conn'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'.'
name|'topic_send'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fanout_cast
dedent|''
dedent|''
name|'def'
name|'fanout_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a fanout exchange without waiting for a response."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Making asynchronous fanout cast...'"
op|')'
op|')'
newline|'\n'
name|'pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
name|'with'
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|')'
name|'as'
name|'conn'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'.'
name|'fanout_send'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast_to_server
dedent|''
dedent|''
name|'def'
name|'cast_to_server'
op|'('
name|'context'
op|','
name|'server_params'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a topic to a specific server."""'
newline|'\n'
name|'pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
name|'with'
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|','
name|'pooled'
op|'='
name|'False'
op|','
nl|'\n'
name|'server_params'
op|'='
name|'server_params'
op|')'
name|'as'
name|'conn'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'.'
name|'topic_send'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fanout_cast_to_server
dedent|''
dedent|''
name|'def'
name|'fanout_cast_to_server'
op|'('
name|'context'
op|','
name|'server_params'
op|','
name|'topic'
op|','
name|'msg'
op|','
nl|'\n'
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a fanout exchange to a specific server."""'
newline|'\n'
name|'pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
name|'with'
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|','
name|'pooled'
op|'='
name|'False'
op|','
nl|'\n'
name|'server_params'
op|'='
name|'server_params'
op|')'
name|'as'
name|'conn'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'.'
name|'fanout_send'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
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
op|','
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a notification event on a topic."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Sending notification on %s...'"
op|')'
op|','
name|'topic'
op|')'
newline|'\n'
name|'pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
name|'with'
name|'ConnectionContext'
op|'('
name|'connection_pool'
op|')'
name|'as'
name|'conn'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'.'
name|'notify_send'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cleanup
dedent|''
dedent|''
name|'def'
name|'cleanup'
op|'('
name|'connection_pool'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'connection_pool'
op|'.'
name|'empty'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
