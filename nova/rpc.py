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
DECL|variable|__all__
name|'__all__'
op|'='
op|'['
nl|'\n'
string|"'init'"
op|','
nl|'\n'
string|"'cleanup'"
op|','
nl|'\n'
string|"'set_defaults'"
op|','
nl|'\n'
string|"'add_extra_exmods'"
op|','
nl|'\n'
string|"'clear_extra_exmods'"
op|','
nl|'\n'
string|"'get_allowed_exmods'"
op|','
nl|'\n'
string|"'RequestContextSerializer'"
op|','
nl|'\n'
string|"'get_client'"
op|','
nl|'\n'
string|"'get_server'"
op|','
nl|'\n'
string|"'get_notifier'"
op|','
nl|'\n'
string|"'TRANSPORT_ALIASES'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|TRANSPORT
name|'TRANSPORT'
op|'='
name|'None'
newline|'\n'
DECL|variable|NOTIFIER
name|'NOTIFIER'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|ALLOWED_EXMODS
name|'ALLOWED_EXMODS'
op|'='
op|'['
nl|'\n'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'__name__'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|EXTRA_EXMODS
name|'EXTRA_EXMODS'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(markmc): The nova.openstack.common.rpc entries are for backwards compat'
nl|'\n'
comment|'# with Havana rpc_backend configuration values. The nova.rpc entries are for'
nl|'\n'
comment|'# compat with Essex values.'
nl|'\n'
DECL|variable|TRANSPORT_ALIASES
name|'TRANSPORT_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'nova.openstack.common.rpc.impl_kombu'"
op|':'
string|"'rabbit'"
op|','
nl|'\n'
string|"'nova.openstack.common.rpc.impl_qpid'"
op|':'
string|"'qpid'"
op|','
nl|'\n'
string|"'nova.openstack.common.rpc.impl_zmq'"
op|':'
string|"'zmq'"
op|','
nl|'\n'
string|"'nova.rpc.impl_kombu'"
op|':'
string|"'rabbit'"
op|','
nl|'\n'
string|"'nova.rpc.impl_qpid'"
op|':'
string|"'qpid'"
op|','
nl|'\n'
string|"'nova.rpc.impl_zmq'"
op|':'
string|"'zmq'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init
name|'def'
name|'init'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'TRANSPORT'
op|','
name|'NOTIFIER'
newline|'\n'
name|'exmods'
op|'='
name|'get_allowed_exmods'
op|'('
op|')'
newline|'\n'
name|'TRANSPORT'
op|'='
name|'messaging'
op|'.'
name|'get_transport'
op|'('
name|'conf'
op|','
nl|'\n'
name|'allowed_remote_exmods'
op|'='
name|'exmods'
op|','
nl|'\n'
name|'aliases'
op|'='
name|'TRANSPORT_ALIASES'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'RequestContextSerializer'
op|'('
name|'JsonPayloadSerializer'
op|'('
op|')'
op|')'
newline|'\n'
name|'NOTIFIER'
op|'='
name|'messaging'
op|'.'
name|'Notifier'
op|'('
name|'TRANSPORT'
op|','
name|'serializer'
op|'='
name|'serializer'
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
name|'global'
name|'TRANSPORT'
op|','
name|'NOTIFIER'
newline|'\n'
name|'assert'
name|'TRANSPORT'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'assert'
name|'NOTIFIER'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'TRANSPORT'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
name|'TRANSPORT'
op|'='
name|'NOTIFIER'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_defaults
dedent|''
name|'def'
name|'set_defaults'
op|'('
name|'control_exchange'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'messaging'
op|'.'
name|'set_transport_defaults'
op|'('
name|'control_exchange'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_extra_exmods
dedent|''
name|'def'
name|'add_extra_exmods'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'EXTRA_EXMODS'
op|'.'
name|'extend'
op|'('
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|clear_extra_exmods
dedent|''
name|'def'
name|'clear_extra_exmods'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'del'
name|'EXTRA_EXMODS'
op|'['
op|':'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_allowed_exmods
dedent|''
name|'def'
name|'get_allowed_exmods'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'ALLOWED_EXMODS'
op|'+'
name|'EXTRA_EXMODS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JsonPayloadSerializer
dedent|''
name|'class'
name|'JsonPayloadSerializer'
op|'('
name|'messaging'
op|'.'
name|'NoOpSerializer'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|serialize_entity
name|'def'
name|'serialize_entity'
op|'('
name|'context'
op|','
name|'entity'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'entity'
op|','
name|'convert_instances'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestContextSerializer
dedent|''
dedent|''
name|'class'
name|'RequestContextSerializer'
op|'('
name|'messaging'
op|'.'
name|'Serializer'
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
name|'base'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_base'
op|'='
name|'base'
newline|'\n'
nl|'\n'
DECL|member|serialize_entity
dedent|''
name|'def'
name|'serialize_entity'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'entity'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_base'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'entity'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_base'
op|'.'
name|'serialize_entity'
op|'('
name|'context'
op|','
name|'entity'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize_entity
dedent|''
name|'def'
name|'deserialize_entity'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'entity'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_base'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'entity'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_base'
op|'.'
name|'deserialize_entity'
op|'('
name|'context'
op|','
name|'entity'
op|')'
newline|'\n'
nl|'\n'
DECL|member|serialize_context
dedent|''
name|'def'
name|'serialize_context'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize_context
dedent|''
name|'def'
name|'deserialize_context'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'context'
op|'.'
name|'RequestContext'
op|'.'
name|'from_dict'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_transport_url
dedent|''
dedent|''
name|'def'
name|'get_transport_url'
op|'('
name|'url_str'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'messaging'
op|'.'
name|'TransportURL'
op|'.'
name|'parse'
op|'('
name|'CONF'
op|','
name|'url_str'
op|','
name|'TRANSPORT_ALIASES'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_client
dedent|''
name|'def'
name|'get_client'
op|'('
name|'target'
op|','
name|'version_cap'
op|'='
name|'None'
op|','
name|'serializer'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'assert'
name|'TRANSPORT'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'serializer'
op|'='
name|'RequestContextSerializer'
op|'('
name|'serializer'
op|')'
newline|'\n'
name|'return'
name|'messaging'
op|'.'
name|'RPCClient'
op|'('
name|'TRANSPORT'
op|','
nl|'\n'
name|'target'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'version_cap'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_server
dedent|''
name|'def'
name|'get_server'
op|'('
name|'target'
op|','
name|'endpoints'
op|','
name|'serializer'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'assert'
name|'TRANSPORT'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'serializer'
op|'='
name|'RequestContextSerializer'
op|'('
name|'serializer'
op|')'
newline|'\n'
name|'return'
name|'messaging'
op|'.'
name|'get_rpc_server'
op|'('
name|'TRANSPORT'
op|','
nl|'\n'
name|'target'
op|','
nl|'\n'
name|'endpoints'
op|','
nl|'\n'
name|'executor'
op|'='
string|"'eventlet'"
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_notifier
dedent|''
name|'def'
name|'get_notifier'
op|'('
name|'service'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'publisher_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'assert'
name|'NOTIFIER'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'if'
name|'not'
name|'publisher_id'
op|':'
newline|'\n'
indent|'        '
name|'publisher_id'
op|'='
string|'"%s.%s"'
op|'%'
op|'('
name|'service'
op|','
name|'host'
name|'or'
name|'CONF'
op|'.'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'NOTIFIER'
op|'.'
name|'prepare'
op|'('
name|'publisher_id'
op|'='
name|'publisher_id'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
