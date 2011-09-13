begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
string|'"""\nThe BaseScheduler is the base class Scheduler for creating instances\nacross zones. There are two expansion points to this class for:\n1. Assigning Weights to hosts for requested instances\n2. Filtering Hosts based on required instance capabilities\n"""'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'abstract_scheduler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'host_filter'
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
name|'DEFINE_boolean'
op|'('
string|"'spread_first'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Use a spread-first zone scheduler strategy'"
op|')'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.base_scheduler'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseScheduler
name|'class'
name|'BaseScheduler'
op|'('
name|'abstract_scheduler'
op|'.'
name|'AbstractScheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for creating Schedulers that can work across any nova\n    deployment, from simple designs to multiply-nested zones.\n    """'
newline|'\n'
DECL|member|filter_hosts
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'hosts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter the full host list (from the ZoneManager)"""'
newline|'\n'
name|'filter_name'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'filter'"
op|','
name|'None'
op|')'
newline|'\n'
comment|'# Make sure that the requested filter is legitimate.'
nl|'\n'
name|'selected_filter'
op|'='
name|'host_filter'
op|'.'
name|'choose_host_filter'
op|'('
name|'filter_name'
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(sandy): We're only using InstanceType-based specs"
nl|'\n'
comment|"# currently. Later we'll need to snoop for more detailed"
nl|'\n'
comment|'# host filter requests.'
nl|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|'"instance_type"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'instance_type'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# No way to select; return the specified hosts'
nl|'\n'
indent|'            '
name|'return'
name|'hosts'
name|'or'
op|'['
op|']'
newline|'\n'
dedent|''
name|'name'
op|','
name|'query'
op|'='
name|'selected_filter'
op|'.'
name|'instance_type_to_filter'
op|'('
name|'instance_type'
op|')'
newline|'\n'
name|'return'
name|'selected_filter'
op|'.'
name|'filter_hosts'
op|'('
name|'self'
op|'.'
name|'zone_manager'
op|','
name|'query'
op|')'
newline|'\n'
nl|'\n'
DECL|member|weigh_hosts
dedent|''
name|'def'
name|'weigh_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Derived classes may override this to provide more sophisticated\n        scheduling objectives\n        """'
newline|'\n'
comment|'# NOTE(sirp): The default logic is the same as the NoopCostFunction'
nl|'\n'
name|'hosts'
op|'='
op|'['
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'hostname'
op|'='
name|'hostname'
op|','
name|'capabilities'
op|'='
name|'capabilities'
op|')'
nl|'\n'
name|'for'
name|'hostname'
op|','
name|'capabilities'
name|'in'
name|'hosts'
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(Vek): What we actually need to return is enough hosts'
nl|'\n'
comment|'#            for all the instances!'
nl|'\n'
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
name|'while'
name|'num_instances'
op|'>'
name|'len'
op|'('
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instances'
op|'.'
name|'extend'
op|'('
name|'hosts'
op|')'
newline|'\n'
name|'num_instances'
op|'-='
name|'len'
op|'('
name|'hosts'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'num_instances'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'instances'
op|'.'
name|'extend'
op|'('
name|'hosts'
op|'['
op|':'
name|'num_instances'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Adjust the weights for a spread-first strategy'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'spread_first'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'i'
op|','
name|'host'
name|'in'
name|'enumerate'
op|'('
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'host'
op|'['
string|"'weight'"
op|']'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'instances'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
