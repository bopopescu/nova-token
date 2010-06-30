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
string|'""" Based a bit on the carrot.backeds.queue backend... but a lot better """'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'Queue'
name|'as'
name|'queue'
newline|'\n'
nl|'\n'
name|'from'
name|'carrot'
op|'.'
name|'backends'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Message
name|'class'
name|'Message'
op|'('
name|'base'
op|'.'
name|'BaseMessage'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Exchange
dedent|''
name|'class'
name|'Exchange'
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
name|'name'
op|','
name|'exchange_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'exchange_type'
op|'='
name|'exchange_type'
newline|'\n'
name|'self'
op|'.'
name|'_queue'
op|'='
name|'queue'
op|'.'
name|'Queue'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_routes'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|publish
dedent|''
name|'def'
name|'publish'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'routing_key'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'(%s) publish (key: %s) %s'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'name'
op|','
name|'routing_key'
op|','
name|'message'
op|')'
newline|'\n'
name|'if'
name|'routing_key'
name|'in'
name|'self'
op|'.'
name|'_routes'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'_routes'
op|'['
name|'routing_key'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Publishing to route %s'"
op|','
name|'f'
op|')'
newline|'\n'
name|'f'
op|'('
name|'message'
op|','
name|'routing_key'
op|'='
name|'routing_key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|bind
dedent|''
dedent|''
dedent|''
name|'def'
name|'bind'
op|'('
name|'self'
op|','
name|'callback'
op|','
name|'routing_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_routes'
op|'.'
name|'setdefault'
op|'('
name|'routing_key'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_routes'
op|'['
name|'routing_key'
op|']'
op|'.'
name|'append'
op|'('
name|'callback'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Queue
dedent|''
dedent|''
name|'class'
name|'Queue'
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
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'_queue'
op|'='
name|'queue'
op|'.'
name|'Queue'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'<Queue: %s>'"
op|'%'
name|'self'
op|'.'
name|'name'
newline|'\n'
nl|'\n'
DECL|member|push
dedent|''
name|'def'
name|'push'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'routing_key'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_queue'
op|'.'
name|'put'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|size
dedent|''
name|'def'
name|'size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_queue'
op|'.'
name|'qsize'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|pop
dedent|''
name|'def'
name|'pop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_queue'
op|'.'
name|'get'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Backend
dedent|''
dedent|''
name|'class'
name|'Backend'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Singleton backend for testing """'
newline|'\n'
DECL|class|__impl
name|'class'
name|'__impl'
op|'('
name|'base'
op|'.'
name|'BaseBackend'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
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
comment|'#super(__impl, self).__init__(*args, **kwargs)'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_exchanges'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_queues'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_reset_all
dedent|''
name|'def'
name|'_reset_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_exchanges'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_queues'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|queue_declare
dedent|''
name|'def'
name|'queue_declare'
op|'('
name|'self'
op|','
name|'queue'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'queue'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_queues'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Declaring queue %s'"
op|','
name|'queue'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_queues'
op|'['
name|'queue'
op|']'
op|'='
name|'Queue'
op|'('
name|'queue'
op|')'
newline|'\n'
nl|'\n'
DECL|member|exchange_declare
dedent|''
dedent|''
name|'def'
name|'exchange_declare'
op|'('
name|'self'
op|','
name|'exchange'
op|','
name|'type'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'exchange'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_exchanges'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Declaring exchange %s'"
op|','
name|'exchange'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_exchanges'
op|'['
name|'exchange'
op|']'
op|'='
name|'Exchange'
op|'('
name|'exchange'
op|','
name|'type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|queue_bind
dedent|''
dedent|''
name|'def'
name|'queue_bind'
op|'('
name|'self'
op|','
name|'queue'
op|','
name|'exchange'
op|','
name|'routing_key'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Binding %s to %s with key %s'"
op|','
nl|'\n'
name|'queue'
op|','
name|'exchange'
op|','
name|'routing_key'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_exchanges'
op|'['
name|'exchange'
op|']'
op|'.'
name|'bind'
op|'('
name|'self'
op|'.'
name|'_queues'
op|'['
name|'queue'
op|']'
op|'.'
name|'push'
op|','
nl|'\n'
name|'routing_key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'queue'
op|','
name|'no_ack'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'queue'
name|'in'
name|'self'
op|'.'
name|'_queues'
name|'or'
name|'not'
name|'self'
op|'.'
name|'_queues'
op|'['
name|'queue'
op|']'
op|'.'
name|'size'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
dedent|''
op|'('
name|'message_data'
op|','
name|'content_type'
op|','
name|'content_encoding'
op|')'
op|'='
name|'self'
op|'.'
name|'_queues'
op|'['
name|'queue'
op|']'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'message'
op|'='
name|'Message'
op|'('
name|'backend'
op|'='
name|'self'
op|','
name|'body'
op|'='
name|'message_data'
op|','
nl|'\n'
name|'content_type'
op|'='
name|'content_type'
op|','
nl|'\n'
name|'content_encoding'
op|'='
name|'content_encoding'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Getting from %s: %s'"
op|','
name|'queue'
op|','
name|'message'
op|')'
newline|'\n'
name|'return'
name|'message'
newline|'\n'
nl|'\n'
DECL|member|prepare_message
dedent|''
name|'def'
name|'prepare_message'
op|'('
name|'self'
op|','
name|'message_data'
op|','
name|'delivery_mode'
op|','
nl|'\n'
name|'content_type'
op|','
name|'content_encoding'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Prepare message for sending."""'
newline|'\n'
name|'return'
op|'('
name|'message_data'
op|','
name|'content_type'
op|','
name|'content_encoding'
op|')'
newline|'\n'
nl|'\n'
DECL|member|publish
dedent|''
name|'def'
name|'publish'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'exchange'
op|','
name|'routing_key'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'exchange'
name|'in'
name|'self'
op|'.'
name|'_exchanges'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_exchanges'
op|'['
name|'exchange'
op|']'
op|'.'
name|'publish'
op|'('
nl|'\n'
name|'message'
op|','
name|'routing_key'
op|'='
name|'routing_key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|__instance
dedent|''
dedent|''
dedent|''
name|'__instance'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'Backend'
op|'.'
name|'__instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'Backend'
op|'.'
name|'__instance'
op|'='
name|'Backend'
op|'.'
name|'__impl'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'_Backend__instance'"
op|']'
op|'='
name|'Backend'
op|'.'
name|'__instance'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'__instance'
op|','
name|'attr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setattr__
dedent|''
name|'def'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'attr'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'setattr'
op|'('
name|'self'
op|'.'
name|'__instance'
op|','
name|'attr'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset_all
dedent|''
dedent|''
name|'def'
name|'reset_all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'Backend'
op|'('
op|')'
op|'.'
name|'_reset_all'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
