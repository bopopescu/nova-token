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
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'conf'
newline|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
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
DECL|variable|TRANSPORT
name|'TRANSPORT'
op|'='
name|'None'
newline|'\n'
DECL|variable|LEGACY_NOTIFIER
name|'LEGACY_NOTIFIER'
op|'='
name|'None'
newline|'\n'
DECL|variable|NOTIFICATION_TRANSPORT
name|'NOTIFICATION_TRANSPORT'
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
name|'NOTIFICATION_TRANSPORT'
op|','
name|'LEGACY_NOTIFIER'
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
name|'NOTIFICATION_TRANSPORT'
op|'='
name|'messaging'
op|'.'
name|'get_notification_transport'
op|'('
nl|'\n'
name|'conf'
op|','
name|'allowed_remote_exmods'
op|'='
name|'exmods'
op|','
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
name|'if'
name|'conf'
op|'.'
name|'notification_format'
op|'=='
string|"'unversioned'"
op|':'
newline|'\n'
indent|'        '
name|'LEGACY_NOTIFIER'
op|'='
name|'messaging'
op|'.'
name|'Notifier'
op|'('
name|'NOTIFICATION_TRANSPORT'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
name|'NOTIFIER'
op|'='
name|'messaging'
op|'.'
name|'Notifier'
op|'('
name|'NOTIFICATION_TRANSPORT'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|','
name|'driver'
op|'='
string|"'noop'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'conf'
op|'.'
name|'notification_format'
op|'=='
string|"'both'"
op|':'
newline|'\n'
indent|'        '
name|'LEGACY_NOTIFIER'
op|'='
name|'messaging'
op|'.'
name|'Notifier'
op|'('
name|'NOTIFICATION_TRANSPORT'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
name|'NOTIFIER'
op|'='
name|'messaging'
op|'.'
name|'Notifier'
op|'('
name|'NOTIFICATION_TRANSPORT'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|','
nl|'\n'
name|'topics'
op|'='
op|'['
string|"'versioned_notifications'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LEGACY_NOTIFIER'
op|'='
name|'messaging'
op|'.'
name|'Notifier'
op|'('
name|'NOTIFICATION_TRANSPORT'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|','
nl|'\n'
name|'driver'
op|'='
string|"'noop'"
op|')'
newline|'\n'
name|'NOTIFIER'
op|'='
name|'messaging'
op|'.'
name|'Notifier'
op|'('
name|'NOTIFICATION_TRANSPORT'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|','
nl|'\n'
name|'topics'
op|'='
op|'['
string|"'versioned_notifications'"
op|']'
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
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'TRANSPORT'
op|','
name|'NOTIFICATION_TRANSPORT'
op|','
name|'LEGACY_NOTIFIER'
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
name|'NOTIFICATION_TRANSPORT'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'assert'
name|'LEGACY_NOTIFIER'
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
name|'NOTIFICATION_TRANSPORT'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
name|'TRANSPORT'
op|'='
name|'NOTIFICATION_TRANSPORT'
op|'='
name|'LEGACY_NOTIFIER'
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
name|'LEGACY_NOTIFIER'
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
name|'LegacyValidatingNotifier'
op|'('
nl|'\n'
name|'LEGACY_NOTIFIER'
op|'.'
name|'prepare'
op|'('
name|'publisher_id'
op|'='
name|'publisher_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_versioned_notifier
dedent|''
name|'def'
name|'get_versioned_notifier'
op|'('
name|'publisher_id'
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
nl|'\n'
nl|'\n'
DECL|class|LegacyValidatingNotifier
dedent|''
name|'class'
name|'LegacyValidatingNotifier'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps an oslo.messaging Notifier and checks for allowed event_types."""'
newline|'\n'
nl|'\n'
comment|'# If true an exception is thrown if the event_type is not allowed, if false'
nl|'\n'
comment|'# then only a WARNING is logged'
nl|'\n'
DECL|variable|fatal
name|'fatal'
op|'='
name|'False'
newline|'\n'
nl|'\n'
comment|'# This list contains the already existing therefore allowed legacy'
nl|'\n'
comment|'# notification event_types. New items shall not be added to the list as'
nl|'\n'
comment|'# Nova does not allow new legacy notifications any more. This list will be'
nl|'\n'
comment|'# removed when all the notification is transformed to versioned'
nl|'\n'
comment|'# notifications.'
nl|'\n'
DECL|variable|allowed_legacy_notification_event_types
name|'allowed_legacy_notification_event_types'
op|'='
op|'['
nl|'\n'
string|"'aggregate.addhost.end'"
op|','
nl|'\n'
string|"'aggregate.addhost.start'"
op|','
nl|'\n'
string|"'aggregate.create.end'"
op|','
nl|'\n'
string|"'aggregate.create.start'"
op|','
nl|'\n'
string|"'aggregate.delete.end'"
op|','
nl|'\n'
string|"'aggregate.delete.start'"
op|','
nl|'\n'
string|"'aggregate.removehost.end'"
op|','
nl|'\n'
string|"'aggregate.removehost.start'"
op|','
nl|'\n'
string|"'aggregate.updatemetadata.end'"
op|','
nl|'\n'
string|"'aggregate.updatemetadata.start'"
op|','
nl|'\n'
string|"'aggregate.updateprop.end'"
op|','
nl|'\n'
string|"'aggregate.updateprop.start'"
op|','
nl|'\n'
string|"'api.fault'"
op|','
nl|'\n'
string|"'compute.instance.create.end'"
op|','
nl|'\n'
string|"'compute.instance.create.error'"
op|','
nl|'\n'
string|"'compute.instance.create_ip.end'"
op|','
nl|'\n'
string|"'compute.instance.create_ip.start'"
op|','
nl|'\n'
string|"'compute.instance.create.start'"
op|','
nl|'\n'
string|"'compute.instance.delete.end'"
op|','
nl|'\n'
string|"'compute.instance.delete_ip.end'"
op|','
nl|'\n'
string|"'compute.instance.delete_ip.start'"
op|','
nl|'\n'
string|"'compute.instance.delete.start'"
op|','
nl|'\n'
string|"'compute.instance.evacuate'"
op|','
nl|'\n'
string|"'compute.instance.exists'"
op|','
nl|'\n'
string|"'compute.instance.finish_resize.end'"
op|','
nl|'\n'
string|"'compute.instance.finish_resize.start'"
op|','
nl|'\n'
string|"'compute.instance.live.migration.abort.start'"
op|','
nl|'\n'
string|"'compute.instance.live.migration.abort.end'"
op|','
nl|'\n'
string|"'compute.instance.live_migration.post.dest.end'"
op|','
nl|'\n'
string|"'compute.instance.live_migration.post.dest.start'"
op|','
nl|'\n'
string|"'compute.instance.live_migration._post.end'"
op|','
nl|'\n'
string|"'compute.instance.live_migration._post.start'"
op|','
nl|'\n'
string|"'compute.instance.live_migration.pre.end'"
op|','
nl|'\n'
string|"'compute.instance.live_migration.pre.start'"
op|','
nl|'\n'
string|"'compute.instance.live_migration.rollback.dest.end'"
op|','
nl|'\n'
string|"'compute.instance.live_migration.rollback.dest.start'"
op|','
nl|'\n'
string|"'compute.instance.live_migration._rollback.end'"
op|','
nl|'\n'
string|"'compute.instance.live_migration._rollback.start'"
op|','
nl|'\n'
string|"'compute.instance.pause.end'"
op|','
nl|'\n'
string|"'compute.instance.pause.start'"
op|','
nl|'\n'
string|"'compute.instance.power_off.end'"
op|','
nl|'\n'
string|"'compute.instance.power_off.start'"
op|','
nl|'\n'
string|"'compute.instance.power_on.end'"
op|','
nl|'\n'
string|"'compute.instance.power_on.start'"
op|','
nl|'\n'
string|"'compute.instance.reboot.end'"
op|','
nl|'\n'
string|"'compute.instance.reboot.start'"
op|','
nl|'\n'
string|"'compute.instance.rebuild.end'"
op|','
nl|'\n'
string|"'compute.instance.rebuild.error'"
op|','
nl|'\n'
string|"'compute.instance.rebuild.scheduled'"
op|','
nl|'\n'
string|"'compute.instance.rebuild.start'"
op|','
nl|'\n'
string|"'compute.instance.rescue.end'"
op|','
nl|'\n'
string|"'compute.instance.rescue.start'"
op|','
nl|'\n'
string|"'compute.instance.resize.confirm.end'"
op|','
nl|'\n'
string|"'compute.instance.resize.confirm.start'"
op|','
nl|'\n'
string|"'compute.instance.resize.end'"
op|','
nl|'\n'
string|"'compute.instance.resize.error'"
op|','
nl|'\n'
string|"'compute.instance.resize.prep.end'"
op|','
nl|'\n'
string|"'compute.instance.resize.prep.start'"
op|','
nl|'\n'
string|"'compute.instance.resize.revert.end'"
op|','
nl|'\n'
string|"'compute.instance.resize.revert.start'"
op|','
nl|'\n'
string|"'compute.instance.resize.start'"
op|','
nl|'\n'
string|"'compute.instance.restore.end'"
op|','
nl|'\n'
string|"'compute.instance.restore.start'"
op|','
nl|'\n'
string|"'compute.instance.resume.end'"
op|','
nl|'\n'
string|"'compute.instance.resume.start'"
op|','
nl|'\n'
string|"'compute.instance.shelve.end'"
op|','
nl|'\n'
string|"'compute.instance.shelve_offload.end'"
op|','
nl|'\n'
string|"'compute.instance.shelve_offload.start'"
op|','
nl|'\n'
string|"'compute.instance.shelve.start'"
op|','
nl|'\n'
string|"'compute.instance.shutdown.end'"
op|','
nl|'\n'
string|"'compute.instance.shutdown.start'"
op|','
nl|'\n'
string|"'compute.instance.snapshot.end'"
op|','
nl|'\n'
string|"'compute.instance.snapshot.start'"
op|','
nl|'\n'
string|"'compute.instance.soft_delete.end'"
op|','
nl|'\n'
string|"'compute.instance.soft_delete.start'"
op|','
nl|'\n'
string|"'compute.instance.suspend.end'"
op|','
nl|'\n'
string|"'compute.instance.suspend.start'"
op|','
nl|'\n'
string|"'compute.instance.trigger_crash_dump.end'"
op|','
nl|'\n'
string|"'compute.instance.trigger_crash_dump.start'"
op|','
nl|'\n'
string|"'compute.instance.unpause.end'"
op|','
nl|'\n'
string|"'compute.instance.unpause.start'"
op|','
nl|'\n'
string|"'compute.instance.unrescue.end'"
op|','
nl|'\n'
string|"'compute.instance.unrescue.start'"
op|','
nl|'\n'
string|"'compute.instance.unshelve.start'"
op|','
nl|'\n'
string|"'compute.instance.unshelve.end'"
op|','
nl|'\n'
string|"'compute.instance.update'"
op|','
nl|'\n'
string|"'compute.instance.volume.attach'"
op|','
nl|'\n'
string|"'compute.instance.volume.detach'"
op|','
nl|'\n'
string|"'compute.libvirt.error'"
op|','
nl|'\n'
string|"'compute_task.build_instances'"
op|','
nl|'\n'
string|"'compute_task.migrate_server'"
op|','
nl|'\n'
string|"'compute_task.rebuild_server'"
op|','
nl|'\n'
string|"'HostAPI.power_action.end'"
op|','
nl|'\n'
string|"'HostAPI.power_action.start'"
op|','
nl|'\n'
string|"'HostAPI.set_enabled.end'"
op|','
nl|'\n'
string|"'HostAPI.set_enabled.start'"
op|','
nl|'\n'
string|"'HostAPI.set_maintenance.end'"
op|','
nl|'\n'
string|"'HostAPI.set_maintenance.start'"
op|','
nl|'\n'
string|"'keypair.create.start'"
op|','
nl|'\n'
string|"'keypair.create.end'"
op|','
nl|'\n'
string|"'keypair.delete.start'"
op|','
nl|'\n'
string|"'keypair.delete.end'"
op|','
nl|'\n'
string|"'keypair.import.start'"
op|','
nl|'\n'
string|"'keypair.import.end'"
op|','
nl|'\n'
string|"'network.floating_ip.allocate'"
op|','
nl|'\n'
string|"'network.floating_ip.associate'"
op|','
nl|'\n'
string|"'network.floating_ip.deallocate'"
op|','
nl|'\n'
string|"'network.floating_ip.disassociate'"
op|','
nl|'\n'
string|"'scheduler.select_destinations.end'"
op|','
nl|'\n'
string|"'scheduler.select_destinations.start'"
op|','
nl|'\n'
string|"'servergroup.addmember'"
op|','
nl|'\n'
string|"'servergroup.create'"
op|','
nl|'\n'
string|"'servergroup.delete'"
op|','
nl|'\n'
string|"'volume.usage'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|message
name|'message'
op|'='
name|'_'
op|'('
string|"'%(event_type)s is not a versioned notification and not '"
nl|'\n'
string|"'whitelisted. See ./doc/source/notification.rst'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'notifier'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'notifier'
op|'='
name|'notifier'
newline|'\n'
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
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_is_wrap_exception_notification
dedent|''
dedent|''
name|'def'
name|'_is_wrap_exception_notification'
op|'('
name|'self'
op|','
name|'payload'
op|')'
op|':'
newline|'\n'
comment|'# nova.exception.wrap_exception decorator emits notification where the'
nl|'\n'
comment|'# event_type is the name of the decorated function. This is used in'
nl|'\n'
comment|'# many places but it will be converted to versioned notification in one'
nl|'\n'
comment|'# run by updating the decorator so it is pointless to white list all'
nl|'\n'
comment|'# the function names here we white list the notification itself'
nl|'\n'
comment|'# detected by the special payload keys.'
nl|'\n'
indent|'        '
name|'return'
op|'{'
string|"'exception'"
op|','
string|"'args'"
op|'}'
op|'=='
name|'set'
op|'('
name|'payload'
op|'.'
name|'keys'
op|'('
op|')'
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
name|'if'
op|'('
name|'event_type'
name|'not'
name|'in'
name|'self'
op|'.'
name|'allowed_legacy_notification_event_types'
name|'and'
nl|'\n'
name|'not'
name|'self'
op|'.'
name|'_is_wrap_exception_notification'
op|'('
name|'payload'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'fatal'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'AssertionError'
op|'('
name|'self'
op|'.'
name|'message'
op|'%'
op|'{'
string|"'event_type'"
op|':'
name|'event_type'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'self'
op|'.'
name|'message'
op|','
op|'{'
string|"'event_type'"
op|':'
name|'event_type'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'getattr'
op|'('
name|'self'
op|'.'
name|'notifier'
op|','
name|'priority'
op|')'
op|'('
name|'ctxt'
op|','
name|'event_type'
op|','
name|'payload'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
