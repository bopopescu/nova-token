begin_unit
comment|'# Copyright 2013 Red Hat, Inc.'
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
name|'collections'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
name|'import'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
DECL|variable|NOTIFICATIONS
name|'NOTIFICATIONS'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset
name|'def'
name|'reset'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'del'
name|'NOTIFICATIONS'
op|'['
op|':'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FakeMessage
dedent|''
name|'FakeMessage'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'Message'"
op|','
nl|'\n'
op|'['
string|"'publisher_id'"
op|','
string|"'priority'"
op|','
nl|'\n'
string|"'event_type'"
op|','
string|"'payload'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeNotifier
name|'class'
name|'FakeNotifier'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'transport'
op|','
name|'publisher_id'
op|','
name|'serializer'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'transport'
op|'='
name|'transport'
newline|'\n'
name|'self'
op|'.'
name|'publisher_id'
op|'='
name|'publisher_id'
newline|'\n'
name|'self'
op|'.'
name|'_serializer'
op|'='
name|'serializer'
name|'or'
name|'messaging'
op|'.'
name|'serializer'
op|'.'
name|'NoOpSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'priority'
name|'in'
op|'['
string|"'debug'"
op|','
string|"'info'"
op|','
string|"'warn'"
op|','
string|"'error'"
op|','
string|"'critical'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'priority'
op|','
nl|'\n'
name|'functools'
op|'.'
name|'partial'
op|'('
name|'self'
op|'.'
name|'_notify'
op|','
name|'priority'
op|'.'
name|'upper'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|prepare
dedent|''
dedent|''
name|'def'
name|'prepare'
op|'('
name|'self'
op|','
name|'publisher_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'publisher_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'publisher_id'
op|'='
name|'self'
op|'.'
name|'publisher_id'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'__class__'
op|'('
name|'self'
op|'.'
name|'transport'
op|','
name|'publisher_id'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'self'
op|'.'
name|'_serializer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_notify
dedent|''
name|'def'
name|'_notify'
op|'('
name|'self'
op|','
name|'priority'
op|','
name|'ctxt'
op|','
name|'event_type'
op|','
name|'payload'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'payload'
op|'='
name|'self'
op|'.'
name|'_serializer'
op|'.'
name|'serialize_entity'
op|'('
name|'ctxt'
op|','
name|'payload'
op|')'
newline|'\n'
comment|'# NOTE(sileht): simulate the kombu serializer'
nl|'\n'
comment|'# this permit to raise an exception if something have not'
nl|'\n'
comment|'# been serialized correctly'
nl|'\n'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'payload'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'FakeMessage'
op|'('
name|'self'
op|'.'
name|'publisher_id'
op|','
name|'priority'
op|','
name|'event_type'
op|','
name|'payload'
op|')'
newline|'\n'
name|'NOTIFICATIONS'
op|'.'
name|'append'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_notifier
dedent|''
dedent|''
name|'def'
name|'stub_notifier'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'messaging'
op|','
string|"'Notifier'"
op|','
name|'FakeNotifier'
op|')'
newline|'\n'
name|'if'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|':'
newline|'\n'
indent|'        '
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'NOTIFIER'"
op|','
nl|'\n'
name|'FakeNotifier'
op|'('
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'.'
name|'transport'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'NOTIFIER'
op|'.'
name|'publisher_id'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'getattr'
op|'('
name|'rpc'
op|'.'
name|'NOTIFIER'
op|','
string|"'_serializer'"
op|','
nl|'\n'
name|'None'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
