begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Openstack, LLC.'
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
string|'"""\nChance (Random) Scheduler implementation\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ChanceScheduler
name|'class'
name|'ChanceScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements Scheduler as a random node selector."""'
newline|'\n'
nl|'\n'
DECL|member|_filter_hosts
name|'def'
name|'_filter_hosts'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter a list of hosts based on request_spec."""'
newline|'\n'
nl|'\n'
comment|'# Filter out excluded host'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'request_spec'
op|'['
string|"'avoid_original_host'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'original_host'
op|'='
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'hosts'
op|'='
op|'['
name|'host'
name|'for'
name|'host'
name|'in'
name|'hosts'
name|'if'
name|'host'
op|'!='
name|'original_host'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'hosts'
newline|'\n'
nl|'\n'
DECL|member|_schedule
dedent|''
name|'def'
name|'_schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Picks a host that is up at random."""'
newline|'\n'
nl|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'hosts_up'
op|'('
name|'elevated'
op|','
name|'topic'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Is the appropriate service running?"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'hosts'
op|'='
name|'self'
op|'.'
name|'_filter_hosts'
op|'('
name|'request_spec'
op|','
name|'hosts'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Could not find another compute"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'hosts'
op|'['
name|'int'
op|'('
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'*'
name|'len'
op|'('
name|'hosts'
op|')'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|schedule
dedent|''
name|'def'
name|'schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'method'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Picks a host that is up at random."""'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'cast_to_host'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'host'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create and run an instance or instances"""'
newline|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'num_instances'"
op|','
number|'1'
op|')'
newline|'\n'
name|'instances'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'xrange'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance_db_entry'
op|'('
name|'elevated'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'cast_to_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|','
nl|'\n'
string|"'run_instance'"
op|','
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'instances'
op|'.'
name|'append'
op|'('
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
comment|'# So if we loop around, create_instance_db_entry will actually'
nl|'\n'
comment|"# create a new entry, instead of assume it's been created"
nl|'\n'
comment|'# already'
nl|'\n'
name|'del'
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'instances'
newline|'\n'
nl|'\n'
DECL|member|schedule_prep_resize
dedent|''
name|'def'
name|'schedule_prep_resize'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
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
string|'"""Select a target for resize."""'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'cast_to_host'
op|'('
name|'context'
op|','
string|"'compute'"
op|','
name|'host'
op|','
string|"'prep_resize'"
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
