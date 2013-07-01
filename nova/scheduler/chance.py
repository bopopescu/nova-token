begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack Foundation'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
newline|'\n'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'compute_topic'"
op|','
string|"'nova.compute.rpcapi'"
op|')'
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
name|'super'
op|'('
name|'ChanceScheduler'
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
name|'compute_rpcapi'
op|'='
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_filter_hosts
dedent|''
name|'def'
name|'_filter_hosts'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
name|'hosts'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter a list of hosts based on request_spec."""'
newline|'\n'
nl|'\n'
name|'ignore_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'ignore_hosts'"
op|','
op|'['
op|']'
op|')'
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
name|'not'
name|'in'
name|'ignore_hosts'
op|']'
newline|'\n'
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
name|'filter_properties'
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
op|','
name|'filter_properties'
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
name|'random'
op|'.'
name|'choice'
op|'('
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|select_hosts
dedent|''
name|'def'
name|'select_hosts'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Selects a set of random hosts."""'
newline|'\n'
name|'hosts'
op|'='
op|'['
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'CONF'
op|'.'
name|'compute_topic'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'filter_properties'
op|')'
nl|'\n'
name|'for'
name|'instance_uuid'
name|'in'
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_uuids'"
op|','
op|'['
op|']'
op|')'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|'""'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'hosts'
newline|'\n'
nl|'\n'
DECL|member|select_destinations
dedent|''
name|'def'
name|'select_destinations'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Selects random destinations."""'
newline|'\n'
name|'num_instances'
op|'='
name|'request_spec'
op|'['
string|"'num_instances'"
op|']'
newline|'\n'
comment|'# NOTE(alaski): Returns a list of tuples for compatibility with'
nl|'\n'
comment|'# filter_scheduler'
nl|'\n'
name|'dests'
op|'='
op|'['
op|'('
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'CONF'
op|'.'
name|'compute_topic'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
op|','
name|'None'
op|')'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'num_instances'
op|')'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'dests'
op|')'
op|'<'
name|'num_instances'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|"''"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dests'
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
nl|'\n'
name|'admin_password'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|','
name|'is_first_time'
op|','
nl|'\n'
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create and run an instance or instances."""'
newline|'\n'
name|'instance_uuids'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_uuids'"
op|')'
newline|'\n'
name|'for'
name|'num'
op|','
name|'instance_uuid'
name|'in'
name|'enumerate'
op|'('
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'launch_index'"
op|']'
op|'='
name|'num'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'host'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'CONF'
op|'.'
name|'compute_topic'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'updated_instance'
op|'='
name|'driver'
op|'.'
name|'instance_update_db'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'run_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'='
name|'updated_instance'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
name|'is_first_time'
op|'='
name|'is_first_time'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|"# NOTE(vish): we don't reraise the exception here to make sure"
nl|'\n'
comment|'#             that all instances in the request get set to'
nl|'\n'
comment|'#             error properly'
nl|'\n'
indent|'                '
name|'driver'
op|'.'
name|'handle_schedule_error'
op|'('
name|'context'
op|','
name|'ex'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_prep_resize
dedent|''
dedent|''
dedent|''
name|'def'
name|'schedule_prep_resize'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'instance'
op|','
name|'instance_type'
op|','
nl|'\n'
name|'reservations'
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
name|'CONF'
op|'.'
name|'compute_topic'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'prep_resize'
op|'('
name|'context'
op|','
name|'image'
op|','
name|'instance'
op|','
nl|'\n'
name|'instance_type'
op|','
name|'host'
op|','
name|'reservations'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
