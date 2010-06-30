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
comment|'# Copyright 2010 Anso Labs, LLC'
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
string|'"""\nAMQP-based RPC. Queues have consumers and publishers.\nNo fan-out support yet.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'from'
name|'carrot'
name|'import'
name|'connection'
newline|'\n'
name|'from'
name|'carrot'
name|'import'
name|'messaging'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'task'
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
name|'fakerabbit'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
DECL|variable|_log
name|'_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'amqplib'"
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'WARN'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Connection
name|'class'
name|'Connection'
op|'('
name|'connection'
op|'.'
name|'BrokerConnection'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'cls'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'dict'
op|'('
name|'hostname'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_host'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_port'
op|','
nl|'\n'
name|'userid'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_userid'
op|','
nl|'\n'
name|'password'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_password'
op|','
nl|'\n'
name|'virtual_host'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_virtual_host'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'['
string|"'backend_cls'"
op|']'
op|'='
name|'fakerabbit'
op|'.'
name|'Backend'
newline|'\n'
nl|'\n'
dedent|''
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'cls'
op|'('
op|'**'
name|'params'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Consumer
dedent|''
dedent|''
name|'class'
name|'Consumer'
op|'('
name|'messaging'
op|'.'
name|'Consumer'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): it would be nice to give these some way of automatically'
nl|'\n'
comment|'#               cleaning up after themselves'
nl|'\n'
DECL|member|attach_to_tornado
indent|'    '
name|'def'
name|'attach_to_tornado'
op|'('
name|'self'
op|','
name|'io_inst'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'tornado'
name|'import'
name|'ioloop'
newline|'\n'
name|'if'
name|'io_inst'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'io_inst'
op|'='
name|'ioloop'
op|'.'
name|'IOLoop'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'injected'
op|'='
name|'ioloop'
op|'.'
name|'PeriodicCallback'
op|'('
nl|'\n'
name|'lambda'
op|':'
name|'self'
op|'.'
name|'fetch'
op|'('
name|'enable_callbacks'
op|'='
name|'True'
op|')'
op|','
number|'100'
op|','
name|'io_loop'
op|'='
name|'io_inst'
op|')'
newline|'\n'
name|'injected'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'return'
name|'injected'
newline|'\n'
nl|'\n'
DECL|variable|attachToTornado
dedent|''
name|'attachToTornado'
op|'='
name|'attach_to_tornado'
newline|'\n'
nl|'\n'
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|fetch
name|'def'
name|'fetch'
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
name|'Consumer'
op|','
name|'self'
op|')'
op|'.'
name|'fetch'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_to_twisted
dedent|''
name|'def'
name|'attach_to_twisted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'loop'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'fetch'
op|','
name|'enable_callbacks'
op|'='
name|'True'
op|')'
newline|'\n'
name|'loop'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.1'
op|')'
newline|'\n'
nl|'\n'
DECL|class|Publisher
dedent|''
dedent|''
name|'class'
name|'Publisher'
op|'('
name|'messaging'
op|'.'
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TopicConsumer
dedent|''
name|'class'
name|'TopicConsumer'
op|'('
name|'Consumer'
op|')'
op|':'
newline|'\n'
DECL|variable|exchange_type
indent|'    '
name|'exchange_type'
op|'='
string|'"topic"'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'topic'
op|'='
string|'"broadcast"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'queue'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'FLAGS'
op|'.'
name|'control_exchange'
newline|'\n'
name|'super'
op|'('
name|'TopicConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdapterConsumer
dedent|''
dedent|''
name|'class'
name|'AdapterConsumer'
op|'('
name|'TopicConsumer'
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
op|'='
name|'None'
op|','
name|'topic'
op|'='
string|'"broadcast"'
op|','
name|'proxy'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'Initing the Adapter Consumer for %s'"
op|'%'
op|'('
name|'topic'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'proxy'
op|'='
name|'proxy'
newline|'\n'
name|'super'
op|'('
name|'AdapterConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|receive
name|'def'
name|'receive'
op|'('
name|'self'
op|','
name|'message_data'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'received %s'"
op|'%'
op|'('
name|'message_data'
op|')'
op|')'
newline|'\n'
name|'msg_id'
op|'='
name|'message_data'
op|'.'
name|'pop'
op|'('
string|"'_msg_id'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
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
name|'message'
op|'.'
name|'ack'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'method'
op|':'
newline|'\n'
comment|'# vish: we may not want to ack here, but that means that bad messages'
nl|'\n'
comment|'#       stay in the queue indefinitely, so for now we just log the'
nl|'\n'
comment|'#       message and send an error string back to the caller'
nl|'\n'
indent|'            '
name|'_log'
op|'.'
name|'warn'
op|'('
string|"'no method for message: %s'"
op|'%'
op|'('
name|'message_data'
op|')'
op|')'
newline|'\n'
name|'msg_reply'
op|'('
name|'msg_id'
op|','
string|"'No method for message: %s'"
op|'%'
name|'message_data'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
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
name|'d'
op|'='
name|'defer'
op|'.'
name|'maybeDeferred'
op|'('
name|'node_func'
op|','
op|'**'
name|'node_args'
op|')'
newline|'\n'
name|'if'
name|'msg_id'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'rval'
op|':'
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'rval'
op|')'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addErrback'
op|'('
name|'lambda'
name|'e'
op|':'
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'str'
op|'('
name|'e'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TopicPublisher
dedent|''
dedent|''
name|'class'
name|'TopicPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
DECL|variable|exchange_type
indent|'    '
name|'exchange_type'
op|'='
string|'"topic"'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'topic'
op|'='
string|'"broadcast"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'FLAGS'
op|'.'
name|'control_exchange'
newline|'\n'
name|'super'
op|'('
name|'TopicPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectConsumer
dedent|''
dedent|''
name|'class'
name|'DirectConsumer'
op|'('
name|'Consumer'
op|')'
op|':'
newline|'\n'
DECL|variable|exchange_type
indent|'    '
name|'exchange_type'
op|'='
string|'"direct"'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'msg_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'queue'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'auto_delete'
op|'='
name|'True'
newline|'\n'
name|'super'
op|'('
name|'DirectConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectPublisher
dedent|''
dedent|''
name|'class'
name|'DirectPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
DECL|variable|exchange_type
indent|'    '
name|'exchange_type'
op|'='
string|'"direct"'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'msg_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'auto_delete'
op|'='
name|'True'
newline|'\n'
name|'super'
op|'('
name|'DirectPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|msg_reply
dedent|''
dedent|''
name|'def'
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'reply'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'publisher'
op|'='
name|'DirectPublisher'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'msg_id'
op|'='
name|'msg_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'publisher'
op|'.'
name|'send'
op|'('
op|'{'
string|"'result'"
op|':'
name|'reply'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'        '
name|'publisher'
op|'.'
name|'send'
op|'('
nl|'\n'
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
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|call
dedent|''
name|'def'
name|'call'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_log'
op|'.'
name|'debug'
op|'('
string|'"Making asynchronous call..."'
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
name|'_log'
op|'.'
name|'debug'
op|'('
string|'"MSG_ID is %s"'
op|'%'
op|'('
name|'msg_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'consumer'
op|'='
name|'DirectConsumer'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'msg_id'
op|'='
name|'msg_id'
op|')'
newline|'\n'
name|'consumer'
op|'.'
name|'register_callback'
op|'('
name|'lambda'
name|'data'
op|','
name|'message'
op|':'
name|'d'
op|'.'
name|'callback'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
name|'injected'
op|'='
name|'consumer'
op|'.'
name|'attach_to_tornado'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# clean up after the injected listened and return x'
nl|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'x'
op|':'
name|'injected'
op|'.'
name|'stop'
op|'('
op|')'
name|'and'
name|'x'
name|'or'
name|'x'
op|')'
newline|'\n'
nl|'\n'
name|'publisher'
op|'='
name|'TopicPublisher'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast
dedent|''
name|'def'
name|'cast'
op|'('
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_log'
op|'.'
name|'debug'
op|'('
string|'"Making asynchronous cast..."'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'publisher'
op|'='
name|'TopicPublisher'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generic_response
dedent|''
name|'def'
name|'generic_response'
op|'('
name|'message_data'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'response %s'"
op|','
name|'message_data'
op|')'
newline|'\n'
name|'message'
op|'.'
name|'ack'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|send_message
dedent|''
name|'def'
name|'send_message'
op|'('
name|'topic'
op|','
name|'message'
op|','
name|'wait'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'message'
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
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'topic is %s'"
op|','
name|'topic'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'message %s'"
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'wait'
op|':'
newline|'\n'
indent|'        '
name|'consumer'
op|'='
name|'messaging'
op|'.'
name|'Consumer'
op|'('
name|'connection'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
op|','
nl|'\n'
name|'queue'
op|'='
name|'msg_id'
op|','
nl|'\n'
name|'exchange'
op|'='
name|'msg_id'
op|','
nl|'\n'
name|'auto_delete'
op|'='
name|'True'
op|','
nl|'\n'
name|'exchange_type'
op|'='
string|'"direct"'
op|','
nl|'\n'
name|'routing_key'
op|'='
name|'msg_id'
op|')'
newline|'\n'
name|'consumer'
op|'.'
name|'register_callback'
op|'('
name|'generic_response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'publisher'
op|'='
name|'messaging'
op|'.'
name|'Publisher'
op|'('
name|'connection'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
op|','
nl|'\n'
name|'exchange'
op|'='
string|'"nova"'
op|','
nl|'\n'
name|'exchange_type'
op|'='
string|'"topic"'
op|','
nl|'\n'
name|'routing_key'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'message'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'wait'
op|':'
newline|'\n'
indent|'        '
name|'consumer'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO: Replace with a docstring test'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'send_message'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|']'
op|','
name|'json'
op|'.'
name|'loads'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
