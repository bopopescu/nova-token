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
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
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
name|'task'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'service'
newline|'\n'
nl|'\n'
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
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
string|"'seconds between nodes reporting state to cloud'"
op|','
nl|'\n'
DECL|variable|lower_bound
name|'lower_bound'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Service
name|'class'
name|'Service'
op|'('
name|'object'
op|','
name|'service'
op|'.'
name|'Service'
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
name|'manager'
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
name|'manager'
op|'='
name|'manager'
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
name|'print'
string|"'getattr'"
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'super'
op|'('
name|'Service'
op|','
name|'self'
op|')'
op|'.'
name|'__getattr__'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'__getattr__'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'report_interval'
op|'='
name|'None'
op|','
nl|'\n'
name|'bin_name'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Instantiates class and passes back application object.\n\n        Args:\n            report_interval, defaults to flag\n            bin_name, defaults to basename of executable\n            topic, defaults to bin_name - "nova-" part\n            manager, defaults to FLAGS.<topic>_manager\n        """'
newline|'\n'
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
nl|'\n'
comment|'# NOTE(vish): magic to automatically determine bin_name and topic'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'bin_name'
op|':'
newline|'\n'
indent|'            '
name|'bin_name'
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
name|'bin_name'
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
name|'manager_ref'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'manager'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"Starting %s node"'
op|'%'
name|'topic'
op|')'
newline|'\n'
name|'service_ref'
op|'='
name|'cls'
op|'('
name|'manager_ref'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'consumer_all'
op|'='
name|'rpc'
op|'.'
name|'AdapterConsumer'
op|'('
nl|'\n'
name|'connection'
op|'='
name|'conn'
op|','
nl|'\n'
name|'topic'
op|'='
string|"'%s'"
op|'%'
name|'topic'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'service_ref'
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
name|'conn'
op|','
nl|'\n'
name|'topic'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'topic'
op|','
name|'FLAGS'
op|'.'
name|'node_name'
op|')'
op|','
nl|'\n'
name|'proxy'
op|'='
name|'service_ref'
op|')'
newline|'\n'
nl|'\n'
name|'pulse'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'service_ref'
op|'.'
name|'report_state'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'node_name'
op|','
nl|'\n'
name|'bin_name'
op|')'
newline|'\n'
name|'pulse'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
name|'report_interval'
op|','
name|'now'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'consumer_all'
op|'.'
name|'attach_to_twisted'
op|'('
op|')'
newline|'\n'
name|'consumer_node'
op|'.'
name|'attach_to_twisted'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# This is the parent service that twistd will be looking for when it'
nl|'\n'
comment|'# parses this file, return it so that we can get it into globals.'
nl|'\n'
name|'application'
op|'='
name|'service'
op|'.'
name|'Application'
op|'('
name|'bin_name'
op|')'
newline|'\n'
name|'service_ref'
op|'.'
name|'setServiceParent'
op|'('
name|'application'
op|')'
newline|'\n'
name|'return'
name|'application'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|report_state
name|'def'
name|'report_state'
op|'('
name|'self'
op|','
name|'node_name'
op|','
name|'binary'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the state of this daemon in the datastore."""'
newline|'\n'
name|'print'
string|"'report_state'"
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'daemon_ref'
op|'='
name|'db'
op|'.'
name|'daemon_get_by_args'
op|'('
name|'context'
op|','
name|'node_name'
op|','
name|'binary'
op|')'
newline|'\n'
name|'daemon_id'
op|'='
name|'daemon_ref'
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
indent|'                '
name|'daemon_id'
op|'='
name|'db'
op|'.'
name|'daemon_create'
op|'('
name|'context'
op|','
op|'{'
string|"'node_name'"
op|':'
name|'node_name'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
name|'daemon_ref'
op|'='
name|'db'
op|'.'
name|'daemon_get'
op|'('
name|'context'
op|','
name|'daemon_id'
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'daemon_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'daemon_id'
op|','
nl|'\n'
op|'{'
string|"'report_count'"
op|':'
name|'daemon_ref'
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
string|'"Recovered model server connection!"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'ex'
op|':'
comment|'#FIXME this should only be connection error'
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
string|'"model server went away"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'yield'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
