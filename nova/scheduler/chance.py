begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack, LLC.'
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
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
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
string|'"""Create and run an instance or instances"""'
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
name|'FLAGS'
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
name|'FLAGS'
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
nl|'\n'
DECL|member|schedule_create_volume
dedent|''
name|'def'
name|'schedule_create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'snapshot_id'
op|','
nl|'\n'
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Picks a host that is up at random."""'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'None'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'cast_to_host'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|','
string|"'create_volume'"
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|','
name|'snapshot_id'
op|'='
name|'snapshot_id'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
