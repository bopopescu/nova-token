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
string|'"""\nHandles all requests relating to schedulers.\n"""'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_call_scheduler
name|'def'
name|'_call_scheduler'
op|'('
name|'method'
op|','
name|'context'
op|','
name|'params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generic handler for RPC calls to the scheduler.\n\n    :param params: Optional dictionary of arguments to be passed to the\n                   scheduler worker\n\n    :retval: Result returned by scheduler worker\n    """'
newline|'\n'
name|'if'
name|'not'
name|'params'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'queue'
op|'='
name|'FLAGS'
op|'.'
name|'scheduler_topic'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'args'"
op|':'
name|'params'
op|'}'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'queue'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
dedent|''
name|'class'
name|'API'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the scheduler."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_is_current_zone
name|'def'
name|'_is_current_zone'
op|'('
name|'cls'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_zone_list
name|'def'
name|'get_zone_list'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of zones assoicated with this zone."""'
newline|'\n'
name|'items'
op|'='
name|'_call_scheduler'
op|'('
string|"'get_zone_list'"
op|','
name|'context'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'['
string|"'api_url'"
op|']'
op|'='
name|'item'
op|'['
string|"'api_url'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'\\\\/'"
op|','
string|"'/'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'items'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_zone_capabilities
name|'def'
name|'get_zone_capabilities'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a dict of key, value capabilities for this zone,\n           or for a particular class of services running in this zone."""'
newline|'\n'
name|'return'
name|'_call_scheduler'
op|'('
string|"'get_zone_capabilities'"
op|','
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'params'
op|'='
name|'dict'
op|'('
name|'service'
op|'='
name|'service'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|update_service_capabilities
name|'def'
name|'update_service_capabilities'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service_name'
op|','
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send an update to all the scheduler services informing them\n           of the capabilities of this service."""'
newline|'\n'
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'method'
op|'='
string|"'update_service_capabilities'"
op|','
nl|'\n'
name|'args'
op|'='
name|'dict'
op|'('
name|'service_name'
op|'='
name|'service_name'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'capabilities'
op|')'
op|')'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'fanout_cast'
op|'('
name|'context'
op|','
string|"'scheduler'"
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_instance_or_reroute
name|'def'
name|'get_instance_or_reroute'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance %(instance_id)s not found locally: \'%(e)s\'"'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Throw a reroute Exception for the middleware to pick up. '
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Firing ZoneRouteException"'
op|')'
newline|'\n'
name|'zones'
op|'='
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ZoneRouteException'
op|'('
name|'zones'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_queue_for_instance
name|'def'
name|'get_queue_for_instance'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'zone'
op|'='
name|'db'
op|'.'
name|'get_zone'
op|'('
name|'instance'
op|'.'
name|'zone'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'if'
name|'cls'
op|'.'
name|'_is_current_zone'
op|'('
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'service'
op|','
name|'instance'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Throw a reroute Exception for the middleware to pick up. '
nl|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'ZoneRouteException'
op|'('
name|'zone'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
