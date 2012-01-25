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
comment|'# Copyright 2011 Red Hat, Inc.'
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
name|'copy'
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
name|'log'
name|'as'
name|'logging'
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
string|"'nova.rpc'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'rpc_thread_pool_size'"
op|','
number|'1024'
op|','
nl|'\n'
string|"'Size of RPC thread pool'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'rpc_conn_pool_size'"
op|','
number|'30'
op|','
nl|'\n'
string|"'Size of RPC connection pool'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteError
name|'class'
name|'RemoteError'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Signifies that a remote class has raised an exception.\n\n    Contains a string representation of the type of the original exception,\n    the value of the original exception, and the traceback.  These are\n    sent to the parent as a joined string so printing the exception\n    contains all of the relevant info.\n\n    """'
newline|'\n'
DECL|variable|message
name|'message'
op|'='
name|'_'
op|'('
string|'"Remote error: %(exc_type)s %(value)s\\n%(traceback)s."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'exc_type'
op|'='
name|'None'
op|','
name|'value'
op|'='
name|'None'
op|','
name|'traceback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'exc_type'
op|'='
name|'exc_type'
newline|'\n'
name|'self'
op|'.'
name|'value'
op|'='
name|'value'
newline|'\n'
name|'self'
op|'.'
name|'traceback'
op|'='
name|'traceback'
newline|'\n'
name|'super'
op|'('
name|'RemoteError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'exc_type'
op|'='
name|'exc_type'
op|','
nl|'\n'
name|'value'
op|'='
name|'value'
op|','
nl|'\n'
name|'traceback'
op|'='
name|'traceback'
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
string|'"""A connection, returned by rpc.create_connection().\n\n    This class represents a connection to the message bus used for rpc.\n    An instance of this class should never be created by users of the rpc API.\n    Use rpc.create_connection() instead.\n    """'
newline|'\n'
DECL|member|close
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Close the connection.\n\n        This method must be called when the connection will no longer be used.\n        It will ensure that any resources associated with the connection, such\n        as a network connection, and cleaned up.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
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
string|'"""Create a consumer on this connection.\n\n        A consumer is associated with a message queue on the backend message\n        bus.  The consumer will read messages from the queue, unpack them, and\n        dispatch them to the proxy object.  The contents of the message pulled\n        off of the queue will determine which method gets called on the proxy\n        object.\n\n        :param topic: This is a name associated with what to consume from.\n                      Multiple instances of a service may consume from the same\n                      topic. For example, all instances of nova-compute consume\n                      from a queue called "compute".  In that case, the\n                      messages will get distributed amongst the consumers in a\n                      round-robin fashion if fanout=False.  If fanout=True,\n                      every consumer associated with this topic will get a\n                      copy of every message.\n        :param proxy: The object that will handle all incoming messages.\n        :param fanout: Whether or not this is a fanout topic.  See the\n                       documentation for the topic parameter for some\n                       additional comments on this.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Spawn a thread to handle incoming messages.\n\n        Spawn a thread that will be responsible for handling all incoming\n        messages for consumers that were set up on this connection.\n\n        Message dispatching inside of this is expected to be implemented in a\n        non-blocking manner.  An example implementation would be having this\n        thread pull messages in for all of the consumers, but utilize a thread\n        pool for dispatching the messages to the proxy objects.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_safe_log
dedent|''
dedent|''
name|'def'
name|'_safe_log'
op|'('
name|'log_func'
op|','
name|'msg'
op|','
name|'msg_data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sanitizes the msg_data field before logging."""'
newline|'\n'
name|'SANITIZE'
op|'='
op|'{'
nl|'\n'
string|"'set_admin_password'"
op|':'
op|'('
string|"'new_pass'"
op|','
op|')'
op|','
nl|'\n'
string|"'run_instance'"
op|':'
op|'('
string|"'admin_password'"
op|','
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'method'
op|'='
name|'msg_data'
op|'['
string|"'method'"
op|']'
newline|'\n'
name|'if'
name|'method'
name|'in'
name|'SANITIZE'
op|':'
newline|'\n'
indent|'        '
name|'msg_data'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'msg_data'
op|')'
newline|'\n'
name|'args_to_sanitize'
op|'='
name|'SANITIZE'
op|'['
name|'method'
op|']'
newline|'\n'
name|'for'
name|'arg'
name|'in'
name|'args_to_sanitize'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'msg_data'
op|'['
string|"'args'"
op|']'
op|'['
name|'arg'
op|']'
op|'='
string|'"<SANITIZED>"'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'log_func'
op|'('
name|'msg'
op|','
name|'msg_data'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
