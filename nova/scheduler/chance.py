begin_unit
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
name|'oslo_config'
name|'import'
name|'cfg'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
DECL|member|_filter_hosts
name|'def'
name|'_filter_hosts'
op|'('
name|'self'
op|','
name|'hosts'
op|','
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter a list of hosts based on RequestSpec."""'
newline|'\n'
nl|'\n'
name|'ignore_hosts'
op|'='
name|'spec_obj'
op|'.'
name|'ignore_hosts'
name|'or'
op|'['
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
name|'spec_obj'
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
name|'hosts'
op|','
name|'spec_obj'
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
comment|'# TODO(sbauza): Change the select_destinations method to accept a'
nl|'\n'
comment|'# RequestSpec object directly (and add a new RPC API method for passing'
nl|'\n'
comment|'# a RequestSpec object over the wire)'
nl|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'.'
name|'from_primitives'
op|'('
name|'context'
op|','
nl|'\n'
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'spec_obj'
op|'.'
name|'num_instances'
newline|'\n'
comment|"# NOTE(timello): Returns a list of dicts with 'host', 'nodename' and"
nl|'\n'
comment|"# 'limits' as keys for compatibility with filter_scheduler."
nl|'\n'
name|'dests'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
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
name|'CONF'
op|'.'
name|'compute_topic'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'host_state'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
name|'host'
op|','
name|'nodename'
op|'='
name|'None'
op|','
name|'limits'
op|'='
name|'None'
op|')'
newline|'\n'
name|'dests'
op|'.'
name|'append'
op|'('
name|'host_state'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'reason'
op|'='
name|'_'
op|'('
string|"'There are not enough hosts available.'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dests'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
