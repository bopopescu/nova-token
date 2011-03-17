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
name|'import'
name|'novaclient'
op|'.'
name|'client'
name|'as'
name|'client'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
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
nl|'\n'
DECL|function|_wrap_method
dedent|''
dedent|''
name|'def'
name|'_wrap_method'
op|'('
name|'function'
op|','
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrap method to supply \'self\'."""'
newline|'\n'
DECL|function|_wrap
name|'def'
name|'_wrap'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'function'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_wrap'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_process
dedent|''
name|'def'
name|'_process'
op|'('
name|'self'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Worker stub for green thread pool"""'
newline|'\n'
name|'nova'
op|'='
name|'client'
op|'.'
name|'OpenStackClient'
op|'('
name|'zone'
op|'.'
name|'username'
op|','
name|'zone'
op|'.'
name|'password'
op|','
nl|'\n'
name|'zone'
op|'.'
name|'api_url'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'authenticate'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'process'
op|'('
name|'nova'
op|','
name|'zone'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ChildZoneHelper
dedent|''
name|'class'
name|'ChildZoneHelper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delegate a call to a set of Child Zones and wait for their\n       responses. Could be used for Zone Redirect or by the Scheduler\n       plug-ins to query the children."""'
newline|'\n'
nl|'\n'
DECL|member|start
name|'def'
name|'start'
op|'('
name|'self'
op|','
name|'zone_list'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Spawn a green thread for each child zone, calling the\n        derived classes process() method as the worker. Returns\n        a list of HTTP Responses. 1 per child."""'
newline|'\n'
name|'self'
op|'.'
name|'green_pool'
op|'='
name|'greenpool'
op|'.'
name|'GreenPool'
op|'('
op|')'
newline|'\n'
name|'return'
op|'['
name|'result'
name|'for'
name|'result'
name|'in'
name|'self'
op|'.'
name|'green_pool'
op|'.'
name|'imap'
op|'('
nl|'\n'
name|'_wrap_method'
op|'('
name|'_process'
op|','
name|'self'
op|')'
op|','
name|'zone_list'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|process
dedent|''
name|'def'
name|'process'
op|'('
name|'self'
op|','
name|'client'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Worker Method. Derived class must override."""'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
