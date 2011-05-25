begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
nl|'\n'
comment|'# All Rights Reserved.'
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
string|'"""Generic Node baseclass for all workers that run on hosts."""'
newline|'\n'
nl|'\n'
name|'import'
name|'greenlet'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
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
name|'db'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
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
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'report_interval'"
op|','
number|'10'
op|','
nl|'\n'
string|"'seconds between nodes reporting state to datastore'"
op|','
nl|'\n'
DECL|variable|lower_bound
name|'lower_bound'
op|'='
number|'1'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'periodic_interval'"
op|','
number|'60'
op|','
nl|'\n'
string|"'seconds between running periodic tasks'"
op|','
nl|'\n'
DECL|variable|lower_bound
name|'lower_bound'
op|'='
number|'1'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ec2_listen'"
op|','
string|'"0.0.0.0"'
op|','
nl|'\n'
string|"'IP address for EC2 API to listen'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'ec2_listen_port'"
op|','
number|'8773'
op|','
string|"'port for ec2 api to listen'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'osapi_listen'"
op|','
string|'"0.0.0.0"'
op|','
nl|'\n'
string|"'IP address for OpenStack API to listen'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'osapi_listen_port'"
op|','
number|'8774'
op|','
string|"'port for os api to listen'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'api_paste_config'"
op|','
string|'"api-paste.ini"'
op|','
nl|'\n'
string|"'File name for the paste.deploy config for nova-api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Service
name|'class'
name|'Service'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for workers that run on hosts."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'binary'
op|','
name|'topic'
op|','
name|'manager'
op|','
name|'report_interval'
op|'='
name|'None'
op|','
nl|'\n'
name|'periodic_interval'
op|'='
name|'None'
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
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'binary'
op|'='
name|'binary'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'manager_class_name'
op|'='
name|'manager'
newline|'\n'
name|'manager_class'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'self'
op|'.'
name|'manager_class_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager_class'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'report_interval'
op|'='
name|'report_interval'
newline|'\n'
name|'self'
op|'.'
name|'periodic_interval'
op|'='
name|'periodic_interval'
newline|'\n'
name|'super'
op|'('
name|'Service'
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
name|'self'
op|'.'
name|'saved_args'
op|','
name|'self'
op|'.'
name|'saved_kwargs'
op|'='
name|'args'
op|','
name|'kwargs'
newline|'\n'
name|'self'
op|'.'
name|'timers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vcs_string'
op|'='
name|'version'
op|'.'
name|'version_string_with_vcs'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Starting %(topic)s node (version %(vcs_string)s)'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'topic'"
op|':'
name|'self'
op|'.'
name|'topic'
op|','
string|"'vcs_string'"
op|':'
name|'vcs_string'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'model_disconnected'
op|'='
name|'False'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'binary'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service_id'
op|'='
name|'service_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_create_service_ref'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'nova-compute'"
op|'=='
name|'self'
op|'.'
name|'binary'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'update_available_resource'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'conn1'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
name|'conn2'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
name|'conn3'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Creating Consumer connection for Service %s"'
op|'%'
name|'self'
op|'.'
name|'topic'
op|')'
newline|'\n'
nl|'\n'
comment|'# Share this same connection for these Consumers'
nl|'\n'
name|'consumer_all'
op|'='
name|'rpc'
op|'.'
name|'TopicAdapterConsumer'
op|'('
nl|'\n'
name|'connection'
op|'='
name|'conn1'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'self'
op|')'
newline|'\n'
name|'consumer_node'
op|'='
name|'rpc'
op|'.'
name|'TopicAdapterConsumer'
op|'('
nl|'\n'
name|'connection'
op|'='
name|'conn1'
op|','
nl|'\n'
name|'topic'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'topic'
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'self'
op|')'
newline|'\n'
name|'fanout'
op|'='
name|'rpc'
op|'.'
name|'FanoutAdapterConsumer'
op|'('
nl|'\n'
name|'connection'
op|'='
name|'conn1'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'self'
op|')'
newline|'\n'
nl|'\n'
name|'cset'
op|'='
name|'rpc'
op|'.'
name|'ConsumerSet'
op|'('
name|'conn1'
op|','
op|'['
name|'consumer_all'
op|','
nl|'\n'
name|'consumer_node'
op|','
nl|'\n'
name|'fanout'
op|']'
op|')'
newline|'\n'
comment|'# Wait forever, processing these consumers'
nl|'\n'
DECL|function|_wait
name|'def'
name|'_wait'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cset'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'cset'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'csetthread'
op|'='
name|'greenthread'
op|'.'
name|'spawn'
op|'('
name|'_wait'
op|')'
newline|'\n'
nl|'\n'
comment|'#self.timers.append(consumer_all.attach_to_eventlet())'
nl|'\n'
comment|'#self.timers.append(consumer_node.attach_to_eventlet())'
nl|'\n'
comment|'#self.timers.append(fanout.attach_to_eventlet())'
nl|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'report_interval'
op|':'
newline|'\n'
indent|'            '
name|'pulse'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'report_state'
op|')'
newline|'\n'
name|'pulse'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
name|'self'
op|'.'
name|'report_interval'
op|','
name|'now'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'timers'
op|'.'
name|'append'
op|'('
name|'pulse'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'periodic_interval'
op|':'
newline|'\n'
indent|'            '
name|'periodic'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'periodic_tasks'
op|')'
newline|'\n'
name|'periodic'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
name|'self'
op|'.'
name|'periodic_interval'
op|','
name|'now'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'timers'
op|'.'
name|'append'
op|'('
name|'periodic'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_service_ref
dedent|''
dedent|''
name|'def'
name|'_create_service_ref'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zone'
op|'='
name|'FLAGS'
op|'.'
name|'node_availability_zone'
newline|'\n'
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'context'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
string|"'topic'"
op|':'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'zone'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service_id'
op|'='
name|'service_ref'
op|'['
string|"'id'"
op|']'
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
name|'manager'
op|'='
name|'self'
op|'.'
name|'__dict__'
op|'.'
name|'get'
op|'('
string|"'manager'"
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'manager'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'cls'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'binary'
op|'='
name|'None'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'manager'
op|'='
name|'None'
op|','
nl|'\n'
name|'report_interval'
op|'='
name|'None'
op|','
name|'periodic_interval'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Instantiates class and passes back application object.\n\n        :param host: defaults to FLAGS.host\n        :param binary: defaults to basename of executable\n        :param topic: defaults to bin_name - \'nova-\' part\n        :param manager: defaults to FLAGS.<topic>_manager\n        :param report_interval: defaults to FLAGS.report_interval\n        :param periodic_interval: defaults to FLAGS.periodic_interval\n\n        """'
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'binary'
op|':'
newline|'\n'
indent|'            '
name|'binary'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'inspect'
op|'.'
name|'stack'
op|'('
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'topic'
op|':'
newline|'\n'
indent|'            '
name|'topic'
op|'='
name|'binary'
op|'.'
name|'rpartition'
op|'('
string|"'nova-'"
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'manager'
op|':'
newline|'\n'
indent|'            '
name|'manager'
op|'='
name|'FLAGS'
op|'.'
name|'get'
op|'('
string|"'%s_manager'"
op|'%'
name|'topic'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'report_interval'
op|':'
newline|'\n'
indent|'            '
name|'report_interval'
op|'='
name|'FLAGS'
op|'.'
name|'report_interval'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'periodic_interval'
op|':'
newline|'\n'
indent|'            '
name|'periodic_interval'
op|'='
name|'FLAGS'
op|'.'
name|'periodic_interval'
newline|'\n'
dedent|''
name|'service_obj'
op|'='
name|'cls'
op|'('
name|'host'
op|','
name|'binary'
op|','
name|'topic'
op|','
name|'manager'
op|','
nl|'\n'
name|'report_interval'
op|','
name|'periodic_interval'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'service_obj'
newline|'\n'
nl|'\n'
DECL|member|kill
dedent|''
name|'def'
name|'kill'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy the service object in the datastore."""'
newline|'\n'
name|'self'
op|'.'
name|'csetthread'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'csetthread'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'service_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Service killed that has no database entry'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'timers'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'x'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'timers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'timers'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'x'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|periodic_tasks
dedent|''
dedent|''
dedent|''
name|'def'
name|'periodic_tasks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval."""'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'periodic_tasks'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|report_state
dedent|''
name|'def'
name|'report_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the state of this service in the datastore."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'service_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'The service database object disappeared, '"
nl|'\n'
string|"'Recreating it.'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_service_ref'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'service_ref'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'service_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'db'
op|'.'
name|'service_update'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'service_id'
op|','
nl|'\n'
op|'{'
string|"'report_count'"
op|':'
name|'service_ref'
op|'['
string|"'report_count'"
op|']'
op|'+'
number|'1'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(termie): make this pattern be more elegant.'
nl|'\n'
name|'if'
name|'getattr'
op|'('
name|'self'
op|','
string|"'model_disconnected'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'model_disconnected'
op|'='
name|'False'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Recovered model server connection!'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): this should probably only catch connection errors'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
comment|'# pylint: disable=W0702'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'getattr'
op|'('
name|'self'
op|','
string|"'model_disconnected'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'logging'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'model server went away'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WsgiService
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'WsgiService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for WSGI based services.\n\n    For each api you define, you must also define these flags:\n    :<api>_listen: The address on which to listen\n    :<api>_listen_port: The port on which to listen\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'conf'
op|','
name|'apis'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conf'
op|'='
name|'conf'
newline|'\n'
name|'self'
op|'.'
name|'apis'
op|'='
name|'apis'
newline|'\n'
name|'self'
op|'.'
name|'wsgi_app'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'wsgi_app'
op|'='
name|'_run_wsgi'
op|'('
name|'self'
op|'.'
name|'conf'
op|','
name|'self'
op|'.'
name|'apis'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'wsgi_app'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_socket_info
dedent|''
name|'def'
name|'get_socket_info'
op|'('
name|'self'
op|','
name|'api_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the (host, port) that an API was started on."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'wsgi_app'
op|'.'
name|'socket_info'
op|'['
name|'api_name'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiService
dedent|''
dedent|''
name|'class'
name|'ApiService'
op|'('
name|'WsgiService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class for our nova-api service."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'cls'
op|','
name|'conf'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'conf'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'='
name|'wsgi'
op|'.'
name|'paste_config_file'
op|'('
name|'FLAGS'
op|'.'
name|'api_paste_config'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'conf'
op|':'
newline|'\n'
indent|'                '
name|'message'
op|'='
op|'('
name|'_'
op|'('
string|"'No paste configuration found for: %s'"
op|')'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'api_paste_config'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'message'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'api_endpoints'
op|'='
op|'['
string|"'ec2'"
op|','
string|"'osapi'"
op|']'
newline|'\n'
name|'service'
op|'='
name|'cls'
op|'('
name|'conf'
op|','
name|'api_endpoints'
op|')'
newline|'\n'
name|'return'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serve
dedent|''
dedent|''
name|'def'
name|'serve'
op|'('
op|'*'
name|'services'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
op|'['
name|'Service'
op|'.'
name|'create'
op|'('
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'in Service.create()'"
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|"# After we've loaded up all our dynamic bits, check"
nl|'\n'
comment|'# whether we should print help'
nl|'\n'
indent|'        '
name|'flags'
op|'.'
name|'DEFINE_flag'
op|'('
name|'flags'
op|'.'
name|'HelpFlag'
op|'('
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_flag'
op|'('
name|'flags'
op|'.'
name|'HelpshortFlag'
op|'('
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_flag'
op|'('
name|'flags'
op|'.'
name|'HelpXMLFlag'
op|'('
op|')'
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'ParseNewFlags'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'name'
op|'='
string|"'_'"
op|'.'
name|'join'
op|'('
name|'x'
op|'.'
name|'binary'
name|'for'
name|'x'
name|'in'
name|'services'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Serving %s'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Full set of FLAGS:'"
op|')'
op|')'
newline|'\n'
name|'for'
name|'flag'
name|'in'
name|'FLAGS'
op|':'
newline|'\n'
indent|'        '
name|'flag_get'
op|'='
name|'FLAGS'
op|'.'
name|'get'
op|'('
name|'flag'
op|','
name|'None'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'%(flag)s : %(flag_get)s'"
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'x'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wait
dedent|''
dedent|''
name|'def'
name|'wait'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'5'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serve_wsgi
dedent|''
dedent|''
name|'def'
name|'serve_wsgi'
op|'('
name|'cls'
op|','
name|'conf'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'='
name|'cls'
op|'.'
name|'create'
op|'('
name|'conf'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'in WsgiService.create()'"
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|"# After we've loaded up all our dynamic bits, check"
nl|'\n'
comment|'# whether we should print help'
nl|'\n'
indent|'        '
name|'flags'
op|'.'
name|'DEFINE_flag'
op|'('
name|'flags'
op|'.'
name|'HelpFlag'
op|'('
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_flag'
op|'('
name|'flags'
op|'.'
name|'HelpshortFlag'
op|'('
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_flag'
op|'('
name|'flags'
op|'.'
name|'HelpXMLFlag'
op|'('
op|')'
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'ParseNewFlags'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_run_wsgi
dedent|''
name|'def'
name|'_run_wsgi'
op|'('
name|'paste_config_file'
op|','
name|'apis'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Using paste.deploy config at: %s'"
op|')'
op|','
name|'paste_config_file'
op|')'
newline|'\n'
name|'apps'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'api'
name|'in'
name|'apis'
op|':'
newline|'\n'
indent|'        '
name|'config'
op|'='
name|'wsgi'
op|'.'
name|'load_paste_configuration'
op|'('
name|'paste_config_file'
op|','
name|'api'
op|')'
newline|'\n'
name|'if'
name|'config'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'No paste configuration for app: %s'"
op|')'
op|','
name|'api'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'App Config: %(api)s\\n%(config)r'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Running %s API'"
op|')'
op|','
name|'api'
op|')'
newline|'\n'
name|'app'
op|'='
name|'wsgi'
op|'.'
name|'load_paste_app'
op|'('
name|'paste_config_file'
op|','
name|'api'
op|')'
newline|'\n'
name|'apps'
op|'.'
name|'append'
op|'('
op|'('
name|'app'
op|','
nl|'\n'
name|'getattr'
op|'('
name|'FLAGS'
op|','
string|"'%s_listen_port'"
op|'%'
name|'api'
op|')'
op|','
nl|'\n'
name|'getattr'
op|'('
name|'FLAGS'
op|','
string|"'%s_listen'"
op|'%'
name|'api'
op|')'
op|','
nl|'\n'
name|'api'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'apps'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'No known API applications configured in %s.'"
op|')'
op|','
nl|'\n'
name|'paste_config_file'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'server'
op|'='
name|'wsgi'
op|'.'
name|'Server'
op|'('
op|')'
newline|'\n'
name|'for'
name|'app'
name|'in'
name|'apps'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'.'
name|'start'
op|'('
op|'*'
name|'app'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
dedent|''
endmarker|''
end_unit
