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
string|'"""Generic Node base class for all workers that run on hosts."""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'greenlet'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.service'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|service_opts
name|'service_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'report_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'seconds between nodes reporting state to datastore'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'periodic_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'seconds between running periodic tasks'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ec2_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address for EC2 API to listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'ec2_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8773'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'port for ec2 api to listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'osapi_compute_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address for OpenStack API to listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'osapi_compute_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8774'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'list port for osapi compute'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'metadata_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.api.manager.MetadataManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'OpenStack metadata service manager'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'metadata_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address for metadata api to listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'metadata_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8775'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'port for metadata api to listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'osapi_volume_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address for OpenStack Volume API to listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'osapi_volume_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8776'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'port for os volume api to listen'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'add_options'
op|'('
name|'service_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Launcher
name|'class'
name|'Launcher'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Launch one or more services and wait for them to complete."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize the service launcher.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_services'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|run_server
name|'def'
name|'run_server'
op|'('
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start and wait for a server to finish.\n\n        :param service: Server to run and wait for.\n        :returns: None\n\n        """'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|launch_server
dedent|''
name|'def'
name|'launch_server'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Load and start the given server.\n\n        :param server: The server you would like to start.\n        :returns: None\n\n        """'
newline|'\n'
name|'gt'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'run_server'
op|','
name|'server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_services'
op|'.'
name|'append'
op|'('
name|'gt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop all services which are currently running.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'_services'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Waits until all services have been stopped, and then returns.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'_services'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'service'
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
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Service
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Service'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Service object for binaries running on hosts.\n\n    A service takes a manager and enables rpc by listening to queues based\n    on topic. It also periodically runs tasks on the manager and reports\n    it state to the database services table."""'
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
name|'LOG'
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
name|'self'
op|'.'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Creating Consumer connection for Service %s"'
op|')'
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|')'
newline|'\n'
nl|'\n'
comment|'# Share this same connection for these Consumers'
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_consumer'
op|'('
name|'self'
op|'.'
name|'topic'
op|','
name|'self'
op|','
name|'fanout'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'node_topic'
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
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_consumer'
op|'('
name|'node_topic'
op|','
name|'self'
op|','
name|'fanout'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_consumer'
op|'('
name|'self'
op|'.'
name|'topic'
op|','
name|'self'
op|','
name|'fanout'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Consume from all consumers in a thread'
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'consume_in_thread'
op|'('
op|')'
newline|'\n'
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
name|'LOG'
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
comment|'# Try to shut the connection down, but if we get any sort of'
nl|'\n'
comment|"# errors, go ahead and ignore them.. as we're shutting down anyway"
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
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
op|','
name|'raise_on_error'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'periodic_tasks'
op|'('
name|'ctxt'
op|','
name|'raise_on_error'
op|'='
name|'raise_on_error'
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
name|'zone'
op|'='
name|'FLAGS'
op|'.'
name|'node_availability_zone'
newline|'\n'
name|'state_catalog'
op|'='
op|'{'
op|'}'
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
name|'LOG'
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
name|'state_catalog'
op|'['
string|"'report_count'"
op|']'
op|'='
name|'service_ref'
op|'['
string|"'report_count'"
op|']'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'zone'
op|'!='
name|'service_ref'
op|'['
string|"'availability_zone'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'state_catalog'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'zone'
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
name|'state_catalog'
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
name|'LOG'
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
name|'LOG'
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
DECL|class|WSGIService
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'WSGIService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provides ability to launch API from a \'paste\' configuration."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'loader'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize, but do not start the WSGI server.\n\n        :param name: The name of the WSGI server given to the loader.\n        :param loader: Loads the WSGI application using the given name.\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'self'
op|'.'
name|'_get_manager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loader'
op|'='
name|'loader'
name|'or'
name|'wsgi'
op|'.'
name|'Loader'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'self'
op|'.'
name|'loader'
op|'.'
name|'load_app'
op|'('
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
string|"'%s_listen'"
op|'%'
name|'name'
op|','
string|'"0.0.0.0"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
string|"'%s_listen_port'"
op|'%'
name|'name'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'='
name|'wsgi'
op|'.'
name|'Server'
op|'('
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'app'
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'port'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_manager
dedent|''
name|'def'
name|'_get_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize a Manager object appropriate for this service.\n\n        Use the service name to look up a Manager subclass from the\n        configuration and initialize an instance. If no class name\n        is configured, just return None.\n\n        :returns: a Manager instance, or None.\n\n        """'
newline|'\n'
name|'fl'
op|'='
string|"'%s_manager'"
op|'%'
name|'self'
op|'.'
name|'name'
newline|'\n'
name|'if'
name|'not'
name|'fl'
name|'in'
name|'FLAGS'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'manager_class_name'
op|'='
name|'FLAGS'
op|'.'
name|'get'
op|'('
name|'fl'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'manager_class_name'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'manager_class'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'manager_class_name'
op|')'
newline|'\n'
name|'return'
name|'manager_class'
op|'('
op|')'
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
string|'"""Start serving this service using loaded configuration.\n\n        Also, retrieve updated port number in case \'0\' was passed in, which\n        indicates a random port should be used.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'manager'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'self'
op|'.'
name|'server'
op|'.'
name|'port'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop serving this API.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'.'
name|'stop'
op|'('
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
string|'"""Wait for the service to stop serving this API.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(vish): the global launcher is to maintain the existing'
nl|'\n'
comment|'#             functionality of calling service.serve +'
nl|'\n'
comment|'#             service.wait'
nl|'\n'
DECL|variable|_launcher
dedent|''
dedent|''
name|'_launcher'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serve
name|'def'
name|'serve'
op|'('
op|'*'
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_launcher'
newline|'\n'
name|'if'
name|'not'
name|'_launcher'
op|':'
newline|'\n'
indent|'        '
name|'_launcher'
op|'='
name|'Launcher'
op|'('
op|')'
newline|'\n'
dedent|''
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'        '
name|'_launcher'
op|'.'
name|'launch_server'
op|'('
name|'server'
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
name|'LOG'
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
comment|'# hide flag contents from log if contains a password'
nl|'\n'
comment|'# should use secret flag when switch over to openstack-common'
nl|'\n'
name|'if'
op|'('
string|'"_password"'
name|'in'
name|'flag'
name|'or'
string|'"_key"'
name|'in'
name|'flag'
name|'or'
nl|'\n'
op|'('
name|'flag'
op|'=='
string|'"sql_connection"'
name|'and'
string|'"mysql:"'
name|'in'
name|'flag_get'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%(flag)s : FLAG SET '"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
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
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'_launcher'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyboardInterrupt'
op|':'
newline|'\n'
indent|'        '
name|'_launcher'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'rpc'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
