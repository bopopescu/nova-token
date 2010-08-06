begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Openstack, LLC.'
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
string|'"""\nScheduler Service\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
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
name|'service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'scheduler'
newline|'\n'
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
name|'DEFINE_string'
op|'('
string|"'scheduler_type'"
op|','
nl|'\n'
string|"'random'"
op|','
nl|'\n'
string|"'the scheduler to use'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|scheduler_classes
name|'scheduler_classes'
op|'='
op|'{'
nl|'\n'
string|"'random'"
op|':'
name|'scheduler'
op|'.'
name|'RandomScheduler'
op|','
nl|'\n'
string|"'bestfit'"
op|':'
name|'scheduler'
op|'.'
name|'BestFitScheduler'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|SchedulerService
name|'class'
name|'SchedulerService'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Manages the running instances.\n    """'
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
name|'super'
op|'('
name|'SchedulerService'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'if'
op|'('
name|'FLAGS'
op|'.'
name|'scheduler_type'
name|'not'
name|'in'
name|'scheduler_classes'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Scheduler \'%s\' does not exist"'
op|'%'
name|'FLAGS'
op|'.'
name|'scheduler_type'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_scheduler_class'
op|'='
name|'scheduler_classes'
op|'['
name|'FLAGS'
op|'.'
name|'scheduler_type'
op|']'
newline|'\n'
nl|'\n'
DECL|member|noop
dedent|''
name|'def'
name|'noop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" simple test of an AMQP message call """'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
string|"'PONG'"
op|')'
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
name|'nodename'
op|','
name|'daemon'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): make this pattern be more elegant. -todd'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'record'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
name|'nodename'
op|','
name|'daemon'
op|')'
newline|'\n'
name|'record'
op|'.'
name|'heartbeat'
op|'('
op|')'
newline|'\n'
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
name|'model'
op|'.'
name|'ConnectionError'
op|','
name|'ex'
op|':'
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
nl|'\n'
DECL|member|pick_node
dedent|''
name|'def'
name|'pick_node'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_scheduler_class'
op|'('
op|')'
op|'.'
name|'pick_node'
op|'('
name|'instance_id'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|run_instance
name|'def'
name|'run_instance'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node'
op|'='
name|'self'
op|'.'
name|'pick_node'
op|'('
name|'instance_id'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
string|"'%s.%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'node'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"run_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance_id'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Casting to node %s for instance %s"'
op|'%'
nl|'\n'
op|'('
name|'node'
op|','
name|'instance_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
