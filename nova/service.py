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
string|'"""\nGeneric Node baseclass for all workers that run on hosts\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
newline|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'exc'
name|'import'
name|'OperationalError'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
nl|'\n'
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
nl|'\n'
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
name|'self'
op|'.'
name|'saved_args'
op|','
nl|'\n'
op|'**'
name|'self'
op|'.'
name|'saved_kwargs'
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
name|'if'
name|'self'
op|'.'
name|'report_interval'
op|':'
newline|'\n'
indent|'            '
name|'consumer_all'
op|'='
name|'rpc'
op|'.'
name|'AdapterConsumer'
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
name|'AdapterConsumer'
op|'('
nl|'\n'
name|'connection'
op|'='
name|'conn2'
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
nl|'\n'
name|'self'
op|'.'
name|'timers'
op|'.'
name|'append'
op|'('
name|'consumer_all'
op|'.'
name|'attach_to_eventlet'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'timers'
op|'.'
name|'append'
op|'('
name|'consumer_node'
op|'.'
name|'attach_to_eventlet'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'host'
op|'='
name|'None'
op|','
nl|'\n'
name|'binary'
op|'='
name|'None'
op|','
nl|'\n'
name|'topic'
op|'='
name|'None'
op|','
nl|'\n'
name|'manager'
op|'='
name|'None'
op|','
nl|'\n'
name|'report_interval'
op|'='
name|'None'
op|','
nl|'\n'
name|'periodic_interval'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Instantiates class and passes back application object.\n\n        Args:\n            host, defaults to FLAGS.host\n            binary, defaults to basename of executable\n            topic, defaults to bin_name - "nova-" part\n            manager, defaults to FLAGS.<topic>_manager\n            report_interval, defaults to FLAGS.report_interval\n            periodic_interval, defaults to FLAGS.periodic_interval\n        """'
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
string|'"nova-"'
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
string|'"Starting %(topic)s node (version %(vcs_string)s)"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
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
string|'"""Destroy the service object in the datastore"""'
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
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Service killed that has no database entry"'
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
DECL|member|periodic_tasks
dedent|''
name|'def'
name|'periodic_tasks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval"""'
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
string|'"The service database object disappeared, "'
nl|'\n'
string|'"Recreating it."'
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
string|'"model_disconnected"'
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
string|'"Recovered model server connection!"'
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
comment|'# pylint: disable-msg=W0702'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'getattr'
op|'('
name|'self'
op|','
string|'"model_disconnected"'
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
string|'"model server went away"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serve
dedent|''
dedent|''
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
name|'FLAGS'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'basicConfig'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'services'
op|':'
newline|'\n'
indent|'        '
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
string|'"Serving %s"'
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
string|'"Full set of FLAGS:"'
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
string|'"%(flag)s : %(flag_get)s"'
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
dedent|''
dedent|''
endmarker|''
end_unit
