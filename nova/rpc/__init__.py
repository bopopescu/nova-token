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
name|'from'
name|'nova'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'utils'
name|'import'
name|'import_object'
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
name|'LOG'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
nl|'\n'
name|'rpc_backend_opt'
op|'='
DECL|variable|rpc_backend_opt
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rpc_backend'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.rpc.impl_kombu'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"The messaging module to use, defaults to kombu."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'add_option'
op|'('
name|'rpc_backend_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_connection
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
string|'"""Create a connection to the message bus used for rpc.\n\n    For some example usage of creating a connection and some consumers on that\n    connection, see nova.service.\n\n    :param new: Whether or not to create a new connection.  A new connection\n                will be created by default.  If new is False, the\n                implementation is free to return an existing connection from a\n                pool.\n\n    :returns: An instance of nova.rpc.common.Connection\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'new'
op|')'
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
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Invoke a remote method that returns something.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  nova.rpc.common.Connection.create_consumer() and only applies\n                  when the consumer was created with fanout=False.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n    :param timeout: int, number of seconds to use for a response timeout.\n                    If set, this overrides the rpc_response_timeout option.\n\n    :returns: A dict from the remote method.\n\n    :raises: nova.rpc.common.Timeout if a complete response is not received\n             before the timeout is reached.\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'call'
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
string|'"""Invoke a remote method that does not return anything.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  nova.rpc.common.Connection.create_consumer() and only applies\n                  when the consumer was created with fanout=False.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
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
string|'"""Broadcast a remote method invocation with no return.\n\n    This method will get invoked on all consumers that were set up with this\n    topic name and fanout=True.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  nova.rpc.common.Connection.create_consumer() and only applies\n                  when the consumer was created with fanout=True.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'fanout_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
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
string|'"""Invoke a remote method and get back an iterator.\n\n    In this case, the remote method will be returning multiple values in\n    separate messages, so the return values can be processed as the come in via\n    an iterator.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  nova.rpc.common.Connection.create_consumer() and only applies\n                  when the consumer was created with fanout=False.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n    :param timeout: int, number of seconds to use for a response timeout.\n                    If set, this overrides the rpc_response_timeout option.\n\n    :returns: An iterator.  The iterator will yield a tuple (N, X) where N is\n              an index that starts at 0 and increases by one for each value\n              returned and X is the Nth value that was returned by the remote\n              method.\n\n    :raises: nova.rpc.common.Timeout if a complete response is not received\n             before the timeout is reached.\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
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
nl|'\n'
nl|'\n'
DECL|function|notify
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
string|'"""Send notification event.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the notification to.\n    :param msg: This is a dict of content of event.\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
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
string|'"""Clean up resoruces in use by implementation.\n\n    Clean up any resources that have been allocated by the RPC implementation.\n    This is typically open connections to a messaging service.  This function\n    would get called before an application using this API exits to allow\n    connections to get torn down cleanly.\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_RPCIMPL
dedent|''
name|'_RPCIMPL'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_impl
name|'def'
name|'_get_impl'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delay import of rpc_backend until FLAGS are loaded."""'
newline|'\n'
name|'global'
name|'_RPCIMPL'
newline|'\n'
name|'if'
name|'_RPCIMPL'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_RPCIMPL'
op|'='
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'rpc_backend'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_RPCIMPL'
newline|'\n'
dedent|''
endmarker|''
end_unit
