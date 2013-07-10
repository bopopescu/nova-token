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
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'local'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
string|"'''RPC Envelope Version.\n\nThis version number applies to the top level structure of messages sent out.\nIt does *not* apply to the message payload, which must be versioned\nindependently.  For example, when using rpc APIs, a version number is applied\nfor changes to the API being exposed over rpc.  This version number is handled\nin the rpc proxy and dispatcher modules.\n\nThis version number applies to the message envelope that is used in the\nserialization done inside the rpc layer.  See serialize_msg() and\ndeserialize_msg().\n\nThe current message format (version 2.0) is very simple.  It is:\n\n    {\n        'oslo.version': <RPC Envelope Version as a String>,\n        'oslo.message': <Application Message Payload, JSON encoded>\n    }\n\nMessage format version '1.0' is just considered to be the messages we sent\nwithout a message envelope.\n\nSo, the current message envelope just includes the envelope version.  It may\neventually contain additional information, such as a signature for the message\npayload.\n\nWe will JSON encode the application message payload.  The message envelope,\nwhich includes the JSON encoded application message body, will be passed down\nto the messaging libraries as a dict.\n'''"
newline|'\n'
DECL|variable|_RPC_ENVELOPE_VERSION
name|'_RPC_ENVELOPE_VERSION'
op|'='
string|"'2.0'"
newline|'\n'
nl|'\n'
DECL|variable|_VERSION_KEY
name|'_VERSION_KEY'
op|'='
string|"'oslo.version'"
newline|'\n'
DECL|variable|_MESSAGE_KEY
name|'_MESSAGE_KEY'
op|'='
string|"'oslo.message'"
newline|'\n'
nl|'\n'
DECL|variable|_REMOTE_POSTFIX
name|'_REMOTE_POSTFIX'
op|'='
string|"'_Remote'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RPCException
name|'class'
name|'RPCException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"An unknown RPC related exception occurred."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'kwargs'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'message'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'message'
op|'='
name|'self'
op|'.'
name|'message'
op|'%'
name|'kwargs'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
comment|"# kwargs doesn't match a variable in the message"
nl|'\n'
comment|'# log the issue and the kwargs'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Exception in string format operation'"
op|')'
op|')'
newline|'\n'
name|'for'
name|'name'
op|','
name|'value'
name|'in'
name|'kwargs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"%s: %s"'
op|'%'
op|'('
name|'name'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
comment|'# at least get the core message out if something happened'
nl|'\n'
dedent|''
name|'message'
op|'='
name|'self'
op|'.'
name|'message'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'super'
op|'('
name|'RPCException'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteError
dedent|''
dedent|''
name|'class'
name|'RemoteError'
op|'('
name|'RPCException'
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
DECL|class|Timeout
dedent|''
dedent|''
name|'class'
name|'Timeout'
op|'('
name|'RPCException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Signifies that a timeout has occurred.\n\n    This exception is raised if the rpc_response_timeout is reached while\n    waiting for a response from the remote side.\n    """'
newline|'\n'
DECL|variable|message
name|'message'
op|'='
name|'_'
op|'('
string|"'Timeout while waiting on RPC response - '"
nl|'\n'
string|'\'topic: "%(topic)s", RPC method: "%(method)s" \''
nl|'\n'
string|'\'info: "%(info)s"\''
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'info'
op|'='
name|'None'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'method'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initiates Timeout object.\n\n        :param info: Extra info to convey to the user\n        :param topic: The topic that the rpc call was sent to\n        :param rpc_method_name: The name of the rpc method being\n                                called\n        """'
newline|'\n'
name|'self'
op|'.'
name|'info'
op|'='
name|'info'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'method'
op|'='
name|'method'
newline|'\n'
name|'super'
op|'('
name|'Timeout'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'info'
op|'='
name|'info'
name|'or'
name|'_'
op|'('
string|"'<unknown>'"
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
name|'or'
name|'_'
op|'('
string|"'<unknown>'"
op|')'
op|','
nl|'\n'
name|'method'
op|'='
name|'method'
name|'or'
name|'_'
op|'('
string|"'<unknown>'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DuplicateMessageError
dedent|''
dedent|''
name|'class'
name|'DuplicateMessageError'
op|'('
name|'RPCException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Found duplicate message(%(msg_id)s). Skipping it."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidRPCConnectionReuse
dedent|''
name|'class'
name|'InvalidRPCConnectionReuse'
op|'('
name|'RPCException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Invalid reuse of an RPC connection."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnsupportedRpcVersion
dedent|''
name|'class'
name|'UnsupportedRpcVersion'
op|'('
name|'RPCException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Specified RPC version, %(version)s, not supported by "'
nl|'\n'
string|'"this endpoint."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnsupportedRpcEnvelopeVersion
dedent|''
name|'class'
name|'UnsupportedRpcEnvelopeVersion'
op|'('
name|'RPCException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Specified RPC envelope version, %(version)s, "'
nl|'\n'
string|'"not supported by this endpoint."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RpcVersionCapError
dedent|''
name|'class'
name|'RpcVersionCapError'
op|'('
name|'RPCException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Specified RPC version cap, %(version_cap)s, is too low"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Connection
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
DECL|member|create_worker
dedent|''
name|'def'
name|'create_worker'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'proxy'
op|','
name|'pool_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a worker on this connection.\n\n        A worker is like a regular consumer of messages directed to a\n        topic, except that it is part of a set of such consumers (the\n        "pool") which may run in parallel. Every pool of workers will\n        receive a given message, but only one worker in the pool will\n        be asked to process it. Load is distributed across the members\n        of the pool in round-robin fashion.\n\n        :param topic: This is a name associated with what to consume from.\n                      Multiple instances of a service may consume from the same\n                      topic.\n        :param proxy: The object that will handle all incoming messages.\n        :param pool_name: String containing the name of the pool of workers\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|join_consumer_pool
dedent|''
name|'def'
name|'join_consumer_pool'
op|'('
name|'self'
op|','
name|'callback'
op|','
name|'pool_name'
op|','
name|'topic'
op|','
name|'exchange_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Register as a member of a group of consumers.\n\n        Uses given topic from the specified exchange.\n        Exactly one member of a given pool will receive each message.\n\n        A message will be delivered to multiple pools, if more than\n        one is created.\n\n        :param callback: Callable to be invoked for each message.\n        :type callback: callable accepting one argument\n        :param pool_name: The name of the consumer pool.\n        :type pool_name: str\n        :param topic: The routing topic for desired messages.\n        :type topic: str\n        :param exchange_name: The name of the message exchange where\n                              the client should attach. Defaults to\n                              the configured exchange.\n        :type exchange_name: str\n        """'
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
op|'['
string|"'_context_auth_token'"
op|','
string|"'auth_token'"
op|','
string|"'new_pass'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|_fix_passwords
name|'def'
name|'_fix_passwords'
op|'('
name|'d'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sanitizes the password fields in the dictionary."""'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'d'
op|'.'
name|'iterkeys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'find'
op|'('
string|"'password'"
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'['
name|'k'
op|']'
op|'='
string|"'<SANITIZED>'"
newline|'\n'
dedent|''
name|'elif'
name|'k'
op|'.'
name|'lower'
op|'('
op|')'
name|'in'
name|'SANITIZE'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'['
name|'k'
op|']'
op|'='
string|"'<SANITIZED>'"
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'d'
op|'['
name|'k'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'_fix_passwords'
op|'('
name|'d'
op|'['
name|'k'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'log_func'
op|'('
name|'msg'
op|','
name|'_fix_passwords'
op|'('
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'msg_data'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serialize_remote_exception
dedent|''
name|'def'
name|'serialize_remote_exception'
op|'('
name|'failure_info'
op|','
name|'log_failure'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Prepares exception data to be sent over rpc.\n\n    Failure_info should be a sys.exc_info() tuple.\n\n    """'
newline|'\n'
name|'tb'
op|'='
name|'traceback'
op|'.'
name|'format_exception'
op|'('
op|'*'
name|'failure_info'
op|')'
newline|'\n'
name|'failure'
op|'='
name|'failure_info'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'log_failure'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Returning exception %s to caller"'
op|')'
op|','
nl|'\n'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'failure'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'tb'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'failure'
op|','
string|"'kwargs'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
name|'failure'
op|'.'
name|'kwargs'
newline|'\n'
nl|'\n'
comment|"# NOTE(matiu): With cells, it's possible to re-raise remote, remote"
nl|'\n'
comment|'# exceptions. Lets turn it back into the original exception type.'
nl|'\n'
dedent|''
name|'cls_name'
op|'='
name|'str'
op|'('
name|'failure'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
name|'mod_name'
op|'='
name|'str'
op|'('
name|'failure'
op|'.'
name|'__class__'
op|'.'
name|'__module__'
op|')'
newline|'\n'
name|'if'
op|'('
name|'cls_name'
op|'.'
name|'endswith'
op|'('
name|'_REMOTE_POSTFIX'
op|')'
name|'and'
nl|'\n'
name|'mod_name'
op|'.'
name|'endswith'
op|'('
name|'_REMOTE_POSTFIX'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cls_name'
op|'='
name|'cls_name'
op|'['
op|':'
op|'-'
name|'len'
op|'('
name|'_REMOTE_POSTFIX'
op|')'
op|']'
newline|'\n'
name|'mod_name'
op|'='
name|'mod_name'
op|'['
op|':'
op|'-'
name|'len'
op|'('
name|'_REMOTE_POSTFIX'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
op|'{'
nl|'\n'
string|"'class'"
op|':'
name|'cls_name'
op|','
nl|'\n'
string|"'module'"
op|':'
name|'mod_name'
op|','
nl|'\n'
string|"'message'"
op|':'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'failure'
op|')'
op|','
nl|'\n'
string|"'tb'"
op|':'
name|'tb'
op|','
nl|'\n'
string|"'args'"
op|':'
name|'failure'
op|'.'
name|'args'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
name|'kwargs'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'json_data'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'json_data'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|deserialize_remote_exception
dedent|''
name|'def'
name|'deserialize_remote_exception'
op|'('
name|'conf'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'failure'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'trace'
op|'='
name|'failure'
op|'.'
name|'get'
op|'('
string|"'tb'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'message'
op|'='
name|'failure'
op|'.'
name|'get'
op|'('
string|"'message'"
op|','
string|'""'
op|')'
op|'+'
string|'"\\n"'
op|'+'
string|'"\\n"'
op|'.'
name|'join'
op|'('
name|'trace'
op|')'
newline|'\n'
name|'name'
op|'='
name|'failure'
op|'.'
name|'get'
op|'('
string|"'class'"
op|')'
newline|'\n'
name|'module'
op|'='
name|'failure'
op|'.'
name|'get'
op|'('
string|"'module'"
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(ameade): We DO NOT want to allow just any module to be imported, in'
nl|'\n'
comment|'# order to prevent arbitrary code execution.'
nl|'\n'
name|'if'
name|'module'
name|'not'
name|'in'
name|'conf'
op|'.'
name|'allowed_rpc_exception_modules'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'RemoteError'
op|'('
name|'name'
op|','
name|'failure'
op|'.'
name|'get'
op|'('
string|"'message'"
op|')'
op|','
name|'trace'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'mod'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
name|'module'
op|')'
newline|'\n'
name|'klass'
op|'='
name|'getattr'
op|'('
name|'mod'
op|','
name|'name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'issubclass'
op|'('
name|'klass'
op|','
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'TypeError'
op|'('
string|'"Can only deserialize Exceptions"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'failure'
op|'='
name|'klass'
op|'('
op|'*'
name|'failure'
op|'.'
name|'get'
op|'('
string|"'args'"
op|','
op|'['
op|']'
op|')'
op|','
op|'**'
name|'failure'
op|'.'
name|'get'
op|'('
string|"'kwargs'"
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'AttributeError'
op|','
name|'TypeError'
op|','
name|'ImportError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'RemoteError'
op|'('
name|'name'
op|','
name|'failure'
op|'.'
name|'get'
op|'('
string|"'message'"
op|')'
op|','
name|'trace'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ex_type'
op|'='
name|'type'
op|'('
name|'failure'
op|')'
newline|'\n'
name|'str_override'
op|'='
name|'lambda'
name|'self'
op|':'
name|'message'
newline|'\n'
name|'new_ex_type'
op|'='
name|'type'
op|'('
name|'ex_type'
op|'.'
name|'__name__'
op|'+'
name|'_REMOTE_POSTFIX'
op|','
op|'('
name|'ex_type'
op|','
op|')'
op|','
nl|'\n'
op|'{'
string|"'__str__'"
op|':'
name|'str_override'
op|','
string|"'__unicode__'"
op|':'
name|'str_override'
op|'}'
op|')'
newline|'\n'
name|'new_ex_type'
op|'.'
name|'__module__'
op|'='
string|"'%s%s'"
op|'%'
op|'('
name|'module'
op|','
name|'_REMOTE_POSTFIX'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(ameade): Dynamically create a new exception type and swap it in'
nl|'\n'
comment|'# as the new type for the exception. This only works on user defined'
nl|'\n'
comment|'# Exceptions and not core python exceptions. This is important because'
nl|'\n'
comment|'# we cannot necessarily change an exception message so we must override'
nl|'\n'
comment|'# the __str__ method.'
nl|'\n'
indent|'        '
name|'failure'
op|'.'
name|'__class__'
op|'='
name|'new_ex_type'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|'# NOTE(ameade): If a core exception then just add the traceback to the'
nl|'\n'
comment|'# first exception argument.'
nl|'\n'
indent|'        '
name|'failure'
op|'.'
name|'args'
op|'='
op|'('
name|'message'
op|','
op|')'
op|'+'
name|'failure'
op|'.'
name|'args'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'failure'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CommonRpcContext
dedent|''
name|'class'
name|'CommonRpcContext'
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
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'values'
op|'='
name|'kwargs'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AttributeError'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_dict
dedent|''
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'values'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deepcopy
dedent|''
name|'def'
name|'deepcopy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'from_dict'
op|'('
name|'self'
op|'.'
name|'to_dict'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_store
dedent|''
name|'def'
name|'update_store'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'local'
op|'.'
name|'store'
op|'.'
name|'context'
op|'='
name|'self'
newline|'\n'
nl|'\n'
DECL|member|elevated
dedent|''
name|'def'
name|'elevated'
op|'('
name|'self'
op|','
name|'read_deleted'
op|'='
name|'None'
op|','
name|'overwrite'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a version of this context with admin flag set."""'
newline|'\n'
comment|'# TODO(russellb) This method is a bit of a nova-ism.  It makes'
nl|'\n'
comment|'# some assumptions about the data in the request context sent'
nl|'\n'
comment|'# across rpc, while the rest of this class does not.  We could get'
nl|'\n'
comment|'# rid of this if we changed the nova code that uses this to'
nl|'\n'
comment|'# convert the RpcContext back to its native RequestContext doing'
nl|'\n'
comment|'# something like nova.context.RequestContext.from_dict(ctxt.to_dict())'
nl|'\n'
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'deepcopy'
op|'('
op|')'
newline|'\n'
name|'context'
op|'.'
name|'values'
op|'['
string|"'is_admin'"
op|']'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'context'
op|'.'
name|'values'
op|'.'
name|'setdefault'
op|'('
string|"'roles'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'admin'"
name|'not'
name|'in'
name|'context'
op|'.'
name|'values'
op|'['
string|"'roles'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'.'
name|'values'
op|'['
string|"'roles'"
op|']'
op|'.'
name|'append'
op|'('
string|"'admin'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'read_deleted'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'.'
name|'values'
op|'['
string|"'read_deleted'"
op|']'
op|'='
name|'read_deleted'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'context'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ClientException
dedent|''
dedent|''
name|'class'
name|'ClientException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Encapsulates actual exception expected to be hit by a RPC proxy object.\n\n    Merely instantiating it records the current exception information, which\n    will be passed back to the RPC client without exceptional logging.\n    """'
newline|'\n'
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
name|'_exc_info'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|catch_client_exception
dedent|''
dedent|''
name|'def'
name|'catch_client_exception'
op|'('
name|'exceptions'
op|','
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'type'
op|'('
name|'e'
op|')'
name|'in'
name|'exceptions'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ClientException'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|client_exceptions
dedent|''
dedent|''
dedent|''
name|'def'
name|'client_exceptions'
op|'('
op|'*'
name|'exceptions'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator for manager methods that raise expected exceptions.\n\n    Marking a Manager method with this decorator allows the declaration\n    of expected exceptions that the RPC layer should not consider fatal,\n    and not log as if they were generated in a real error scenario. Note\n    that this will cause listed exceptions to be wrapped in a\n    ClientException, which is used internally by the RPC layer.\n    """'
newline|'\n'
DECL|function|outer
name|'def'
name|'outer'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
DECL|function|inner
indent|'        '
name|'def'
name|'inner'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'catch_client_exception'
op|'('
name|'exceptions'
op|','
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'inner'
newline|'\n'
dedent|''
name|'return'
name|'outer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|version_is_compatible
dedent|''
name|'def'
name|'version_is_compatible'
op|'('
name|'imp_version'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine whether versions are compatible.\n\n    :param imp_version: The version implemented\n    :param version: The version requested by an incoming message.\n    """'
newline|'\n'
name|'version_parts'
op|'='
name|'version'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'imp_version_parts'
op|'='
name|'imp_version'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'if'
name|'int'
op|'('
name|'version_parts'
op|'['
number|'0'
op|']'
op|')'
op|'!='
name|'int'
op|'('
name|'imp_version_parts'
op|'['
number|'0'
op|']'
op|')'
op|':'
comment|'# Major'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'int'
op|'('
name|'version_parts'
op|'['
number|'1'
op|']'
op|')'
op|'>'
name|'int'
op|'('
name|'imp_version_parts'
op|'['
number|'1'
op|']'
op|')'
op|':'
comment|'# Minor'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serialize_msg
dedent|''
name|'def'
name|'serialize_msg'
op|'('
name|'raw_msg'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(russellb) See the docstring for _RPC_ENVELOPE_VERSION for more'
nl|'\n'
comment|'# information about this format.'
nl|'\n'
indent|'    '
name|'msg'
op|'='
op|'{'
name|'_VERSION_KEY'
op|':'
name|'_RPC_ENVELOPE_VERSION'
op|','
nl|'\n'
name|'_MESSAGE_KEY'
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw_msg'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'msg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|deserialize_msg
dedent|''
name|'def'
name|'deserialize_msg'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(russellb): Hang on to your hats, this road is about to'
nl|'\n'
comment|'# get a little bumpy.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Robustness Principle:'
nl|'\n'
comment|'#    "Be strict in what you send, liberal in what you accept."'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# At this point we have to do a bit of guessing about what it'
nl|'\n'
comment|'# is we just received.  Here is the set of possibilities:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# 1) We received a dict.  This could be 2 things:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   a) Inspect it to see if it looks like a standard message envelope.'
nl|'\n'
comment|'#      If so, great!'
nl|'\n'
comment|'#'
nl|'\n'
comment|"#   b) If it doesn't look like a standard message envelope, it could either"
nl|'\n'
comment|'#      be a notification, or a message from before we added a message'
nl|'\n'
comment|'#      envelope (referred to as version 1.0).'
nl|'\n'
comment|'#      Just return the message as-is.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# 2) It's any other non-dict type.  Just return it and hope for the best."
nl|'\n'
comment|'#    This case covers return values from rpc.call() from before message'
nl|'\n'
comment|'#    envelopes were used.  (messages to call a method were always a dict)'
nl|'\n'
nl|'\n'
indent|'    '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'msg'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
comment|'# See #2 above.'
nl|'\n'
indent|'        '
name|'return'
name|'msg'
newline|'\n'
nl|'\n'
dedent|''
name|'base_envelope_keys'
op|'='
op|'('
name|'_VERSION_KEY'
op|','
name|'_MESSAGE_KEY'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'all'
op|'('
name|'map'
op|'('
name|'lambda'
name|'key'
op|':'
name|'key'
name|'in'
name|'msg'
op|','
name|'base_envelope_keys'
op|')'
op|')'
op|':'
newline|'\n'
comment|'#  See #1.b above.'
nl|'\n'
indent|'        '
name|'return'
name|'msg'
newline|'\n'
nl|'\n'
comment|'# At this point we think we have the message envelope'
nl|'\n'
comment|'# format we were expecting. (#1.a above)'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'version_is_compatible'
op|'('
name|'_RPC_ENVELOPE_VERSION'
op|','
name|'msg'
op|'['
name|'_VERSION_KEY'
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'UnsupportedRpcEnvelopeVersion'
op|'('
name|'version'
op|'='
name|'msg'
op|'['
name|'_VERSION_KEY'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'raw_msg'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'msg'
op|'['
name|'_MESSAGE_KEY'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'raw_msg'
newline|'\n'
dedent|''
endmarker|''
end_unit
