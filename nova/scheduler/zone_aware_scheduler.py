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
string|'"""\nThe Zone Aware Scheduler is a base class Scheduler for creating instances\nacross zones. There are two expansion points to this class for:\n1. Assigning Weights to hosts for requested instances\n2. Filtering Hosts based on required instance capabilities\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'operator'
newline|'\n'
nl|'\n'
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
name|'scheduler'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.zone_aware_scheduler'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneAwareScheduler
name|'class'
name|'ZoneAwareScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for creating Zone Aware Schedulers."""'
newline|'\n'
nl|'\n'
DECL|member|_call_zone_method
name|'def'
name|'_call_zone_method'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call novaclient zone method. Broken out for testing."""'
newline|'\n'
name|'return'
name|'api'
op|'.'
name|'call_zone_method'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|'='
name|'specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|select
dedent|''
name|'def'
name|'select'
op|'('
name|'self'
op|','
name|'context'
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
string|'"""Select returns a list of weights and zone/host information\n        corresponding to the best hosts to service the request. Any\n        child zone information has been encrypted so as not to reveal\n        anything about the children."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
string|'"compute"'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The schedule() contract requires we return the one\n        best-suited host for this request.\n        """'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'topic'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# TODO(sirp): should this be a host object rather than a weight-dict?'
nl|'\n'
name|'if'
name|'not'
name|'res'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
name|'_'
op|'('
string|"'No hosts were available'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'res'
op|'['
number|'0'
op|']'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of hosts that meet the required specs,\n        ordered by their fitness.\n        """'
newline|'\n'
nl|'\n'
comment|'#TODO(sandy): extract these from args.'
nl|'\n'
name|'num_instances'
op|'='
number|'1'
newline|'\n'
name|'specs'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Filter local hosts based on requirements ...'
nl|'\n'
name|'host_list'
op|'='
name|'self'
op|'.'
name|'filter_hosts'
op|'('
name|'num_instances'
op|','
name|'specs'
op|')'
newline|'\n'
nl|'\n'
comment|'# then weigh the selected hosts.'
nl|'\n'
comment|'# weighted = [{weight=weight, name=hostname}, ...]'
nl|'\n'
name|'weighted'
op|'='
name|'self'
op|'.'
name|'weigh_hosts'
op|'('
name|'num_instances'
op|','
name|'specs'
op|','
name|'host_list'
op|')'
newline|'\n'
nl|'\n'
comment|'# Next, tack on the best weights from the child zones ...'
nl|'\n'
name|'child_results'
op|'='
name|'self'
op|'.'
name|'_call_zone_method'
op|'('
name|'context'
op|','
string|'"select"'
op|','
nl|'\n'
name|'specs'
op|'='
name|'specs'
op|')'
newline|'\n'
name|'for'
name|'child_zone'
op|','
name|'result'
name|'in'
name|'child_results'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'weighting'
name|'in'
name|'result'
op|':'
newline|'\n'
comment|'# Remember the child_zone so we can get back to'
nl|'\n'
comment|'# it later if needed. This implicitly builds a zone'
nl|'\n'
comment|'# path structure.'
nl|'\n'
indent|'                '
name|'host_dict'
op|'='
op|'{'
nl|'\n'
string|'"weight"'
op|':'
name|'weighting'
op|'['
string|'"weight"'
op|']'
op|','
nl|'\n'
string|'"child_zone"'
op|':'
name|'child_zone'
op|','
nl|'\n'
string|'"child_blob"'
op|':'
name|'weighting'
op|'['
string|'"blob"'
op|']'
op|'}'
newline|'\n'
name|'weighted'
op|'.'
name|'append'
op|'('
name|'host_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'weighted'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'operator'
op|'.'
name|'itemgetter'
op|'('
string|"'weight'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'weighted'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'num'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Derived classes must override this method and return\n           a list of hosts in [(hostname, capability_dict)] format."""'
newline|'\n'
name|'raise'
name|'NotImplemented'
op|'('
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
name|'num'
op|','
name|'specs'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Derived classes must override this method and return\n           a lists of hosts in [(weight, hostname)] format."""'
newline|'\n'
name|'raise'
name|'NotImplemented'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
