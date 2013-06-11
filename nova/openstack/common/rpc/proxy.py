begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012-2013 Red Hat, Inc.'
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
string|'"""\nA helper class for proxy objects to remote APIs.\n\nFor more information about rpc API version numbers, see:\n    rpc/dispatcher.py\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
name|'import'
name|'serializer'
name|'as'
name|'rpc_serializer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RpcProxy
name|'class'
name|'RpcProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A helper class for rpc clients.\n\n    This class is a wrapper around the RPC client API.  It allows you to\n    specify the topic and API version in a single place.  This is intended to\n    be used as a base class for a class that implements the client side of an\n    rpc API.\n    """'
newline|'\n'
nl|'\n'
comment|'# The default namespace, which can be overriden in a subclass.'
nl|'\n'
DECL|variable|RPC_API_NAMESPACE
name|'RPC_API_NAMESPACE'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'default_version'
op|','
name|'version_cap'
op|'='
name|'None'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize an RpcProxy.\n\n        :param topic: The topic to use for all messages.\n        :param default_version: The default API version to request in all\n               outgoing messages.  This can be overridden on a per-message\n               basis.\n        :param version_cap: Optionally cap the maximum version used for sent\n               messages.\n        :param serializer: Optionaly (de-)serialize entities with a\n               provided helper.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'default_version'
op|'='
name|'default_version'
newline|'\n'
name|'self'
op|'.'
name|'version_cap'
op|'='
name|'version_cap'
newline|'\n'
name|'if'
name|'serializer'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'serializer'
op|'='
name|'rpc_serializer'
op|'.'
name|'NoOpSerializer'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'serializer'
op|'='
name|'serializer'
newline|'\n'
name|'super'
op|'('
name|'RpcProxy'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_version
dedent|''
name|'def'
name|'_set_version'
op|'('
name|'self'
op|','
name|'msg'
op|','
name|'vers'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Helper method to set the version in a message.\n\n        :param msg: The message having a version added to it.\n        :param vers: The version number to add to the message.\n        """'
newline|'\n'
name|'v'
op|'='
name|'vers'
name|'if'
name|'vers'
name|'else'
name|'self'
op|'.'
name|'default_version'
newline|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'version_cap'
name|'and'
name|'not'
nl|'\n'
name|'rpc_common'
op|'.'
name|'version_is_compatible'
op|'('
name|'self'
op|'.'
name|'version_cap'
op|','
name|'v'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'rpc_common'
op|'.'
name|'RpcVersionCapError'
op|'('
name|'version'
op|'='
name|'self'
op|'.'
name|'version_cap'
op|')'
newline|'\n'
dedent|''
name|'msg'
op|'['
string|"'version'"
op|']'
op|'='
name|'v'
newline|'\n'
nl|'\n'
DECL|member|_get_topic
dedent|''
name|'def'
name|'_get_topic'
op|'('
name|'self'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the topic to use for a message."""'
newline|'\n'
name|'return'
name|'topic'
name|'if'
name|'topic'
name|'else'
name|'self'
op|'.'
name|'topic'
newline|'\n'
nl|'\n'
DECL|member|can_send_version
dedent|''
name|'def'
name|'can_send_version'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'not'
name|'self'
op|'.'
name|'version_cap'
name|'or'
nl|'\n'
name|'rpc_common'
op|'.'
name|'version_is_compatible'
op|'('
name|'self'
op|'.'
name|'version_cap'
op|','
name|'version'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|make_namespaced_msg
name|'def'
name|'make_namespaced_msg'
op|'('
name|'method'
op|','
name|'namespace'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'namespace'"
op|':'
name|'namespace'
op|','
string|"'args'"
op|':'
name|'kwargs'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|make_msg
dedent|''
name|'def'
name|'make_msg'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'make_namespaced_msg'
op|'('
name|'method'
op|','
name|'self'
op|'.'
name|'RPC_API_NAMESPACE'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_serialize_msg_args
dedent|''
name|'def'
name|'_serialize_msg_args'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Helper method called to serialize message arguments.\n\n        This calls our serializer on each argument, returning a new\n        set of args that have been serialized.\n\n        :param context: The request context\n        :param kwargs: The arguments to serialize\n        :returns: A new set of serialized arguments\n        """'
newline|'\n'
name|'new_kwargs'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'for'
name|'argname'
op|','
name|'arg'
name|'in'
name|'kwargs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_kwargs'
op|'['
name|'argname'
op|']'
op|'='
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'serialize_entity'
op|'('
name|'context'
op|','
nl|'\n'
name|'arg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'new_kwargs'
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
name|'msg'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'version'
op|'='
name|'None'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""rpc.call() a remote method.\n\n        :param context: The request context\n        :param msg: The message to send, including the method and args.\n        :param topic: Override the topic for this message.\n        :param version: (Optional) Override the requested API version in this\n               message.\n        :param timeout: (Optional) A timeout to use when waiting for the\n               response.  If no timeout is specified, a default timeout will be\n               used that is usually sufficient.\n\n        :returns: The return value from the remote method.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_version'
op|'('
name|'msg'
op|','
name|'version'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'args'"
op|']'
op|'='
name|'self'
op|'.'
name|'_serialize_msg_args'
op|'('
name|'context'
op|','
name|'msg'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
name|'real_topic'
op|'='
name|'self'
op|'.'
name|'_get_topic'
op|'('
name|'topic'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'real_topic'
op|','
name|'msg'
op|','
name|'timeout'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'deserialize_entity'
op|'('
name|'context'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'common'
op|'.'
name|'Timeout'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'rpc'
op|'.'
name|'common'
op|'.'
name|'Timeout'
op|'('
nl|'\n'
name|'exc'
op|'.'
name|'info'
op|','
name|'real_topic'
op|','
name|'msg'
op|'.'
name|'get'
op|'('
string|"'method'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|multicall
dedent|''
dedent|''
name|'def'
name|'multicall'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'msg'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'version'
op|'='
name|'None'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""rpc.multicall() a remote method.\n\n        :param context: The request context\n        :param msg: The message to send, including the method and args.\n        :param topic: Override the topic for this message.\n        :param version: (Optional) Override the requested API version in this\n               message.\n        :param timeout: (Optional) A timeout to use when waiting for the\n               response.  If no timeout is specified, a default timeout will be\n               used that is usually sufficient.\n\n        :returns: An iterator that lets you process each of the returned values\n                  from the remote method as they arrive.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_version'
op|'('
name|'msg'
op|','
name|'version'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'args'"
op|']'
op|'='
name|'self'
op|'.'
name|'_serialize_msg_args'
op|'('
name|'context'
op|','
name|'msg'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
name|'real_topic'
op|'='
name|'self'
op|'.'
name|'_get_topic'
op|'('
name|'topic'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'rpc'
op|'.'
name|'multicall'
op|'('
name|'context'
op|','
name|'real_topic'
op|','
name|'msg'
op|','
name|'timeout'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'deserialize_entity'
op|'('
name|'context'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'common'
op|'.'
name|'Timeout'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'rpc'
op|'.'
name|'common'
op|'.'
name|'Timeout'
op|'('
nl|'\n'
name|'exc'
op|'.'
name|'info'
op|','
name|'real_topic'
op|','
name|'msg'
op|'.'
name|'get'
op|'('
string|"'method'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cast
dedent|''
dedent|''
name|'def'
name|'cast'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'msg'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""rpc.cast() a remote method.\n\n        :param context: The request context\n        :param msg: The message to send, including the method and args.\n        :param topic: Override the topic for this message.\n        :param version: (Optional) Override the requested API version in this\n               message.\n\n        :returns: None.  rpc.cast() does not wait on any return value from the\n                  remote method.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_version'
op|'('
name|'msg'
op|','
name|'version'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'args'"
op|']'
op|'='
name|'self'
op|'.'
name|'_serialize_msg_args'
op|'('
name|'context'
op|','
name|'msg'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'_get_topic'
op|'('
name|'topic'
op|')'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fanout_cast
dedent|''
name|'def'
name|'fanout_cast'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'msg'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""rpc.fanout_cast() a remote method.\n\n        :param context: The request context\n        :param msg: The message to send, including the method and args.\n        :param topic: Override the topic for this message.\n        :param version: (Optional) Override the requested API version in this\n               message.\n\n        :returns: None.  rpc.fanout_cast() does not wait on any return value\n                  from the remote method.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_version'
op|'('
name|'msg'
op|','
name|'version'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'args'"
op|']'
op|'='
name|'self'
op|'.'
name|'_serialize_msg_args'
op|'('
name|'context'
op|','
name|'msg'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'fanout_cast'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'_get_topic'
op|'('
name|'topic'
op|')'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cast_to_server
dedent|''
name|'def'
name|'cast_to_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_params'
op|','
name|'msg'
op|','
name|'topic'
op|'='
name|'None'
op|','
nl|'\n'
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""rpc.cast_to_server() a remote method.\n\n        :param context: The request context\n        :param server_params: Server parameters.  See rpc.cast_to_server() for\n               details.\n        :param msg: The message to send, including the method and args.\n        :param topic: Override the topic for this message.\n        :param version: (Optional) Override the requested API version in this\n               message.\n\n        :returns: None.  rpc.cast_to_server() does not wait on any\n                  return values.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_version'
op|'('
name|'msg'
op|','
name|'version'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'args'"
op|']'
op|'='
name|'self'
op|'.'
name|'_serialize_msg_args'
op|'('
name|'context'
op|','
name|'msg'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast_to_server'
op|'('
name|'context'
op|','
name|'server_params'
op|','
name|'self'
op|'.'
name|'_get_topic'
op|'('
name|'topic'
op|')'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fanout_cast_to_server
dedent|''
name|'def'
name|'fanout_cast_to_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_params'
op|','
name|'msg'
op|','
name|'topic'
op|'='
name|'None'
op|','
nl|'\n'
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""rpc.fanout_cast_to_server() a remote method.\n\n        :param context: The request context\n        :param server_params: Server parameters.  See rpc.cast_to_server() for\n               details.\n        :param msg: The message to send, including the method and args.\n        :param topic: Override the topic for this message.\n        :param version: (Optional) Override the requested API version in this\n               message.\n\n        :returns: None.  rpc.fanout_cast_to_server() does not wait on any\n                  return values.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_version'
op|'('
name|'msg'
op|','
name|'version'
op|')'
newline|'\n'
name|'msg'
op|'['
string|"'args'"
op|']'
op|'='
name|'self'
op|'.'
name|'_serialize_msg_args'
op|'('
name|'context'
op|','
name|'msg'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'fanout_cast_to_server'
op|'('
name|'context'
op|','
name|'server_params'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_topic'
op|'('
name|'topic'
op|')'
op|','
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
