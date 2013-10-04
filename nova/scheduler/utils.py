begin_unit
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
string|'"""Utility methods for scheduling."""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifier'
name|'as'
name|'notify'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_request_spec
name|'def'
name|'build_request_spec'
op|'('
name|'ctxt'
op|','
name|'image'
op|','
name|'instances'
op|','
name|'instance_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build a request_spec for the scheduler.\n\n    The request_spec assumes that all instances to be scheduled are the same\n    type.\n    """'
newline|'\n'
name|'instance'
op|'='
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'instance_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'instance'
op|')'
newline|'\n'
comment|'# NOTE(comstud): This is a bit ugly, but will get cleaned up when'
nl|'\n'
comment|"# we're passing an InstanceType internal object."
nl|'\n'
dedent|''
name|'extra_specs'
op|'='
name|'db'
op|'.'
name|'flavor_extra_specs_get'
op|'('
name|'ctxt'
op|','
name|'instance_type'
op|'['
string|"'flavorid'"
op|']'
op|')'
newline|'\n'
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|'='
name|'extra_specs'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
nl|'\n'
string|"'image'"
op|':'
name|'image'
name|'or'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
name|'instance'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'num_instances'"
op|':'
name|'len'
op|'('
name|'instances'
op|')'
op|','
nl|'\n'
comment|'# NOTE(alaski): This should be removed as logic moves from the'
nl|'\n'
comment|'# scheduler to conductor.  Provides backwards compatibility now.'
nl|'\n'
string|"'instance_uuids'"
op|':'
op|'['
name|'inst'
op|'['
string|"'uuid'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'instances'
op|']'
op|'}'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vm_state_and_notify
dedent|''
name|'def'
name|'set_vm_state_and_notify'
op|'('
name|'context'
op|','
name|'service'
op|','
name|'method'
op|','
name|'updates'
op|','
name|'ex'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'db'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""changes VM state and notifies."""'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Failed to %(service)s_%(method)s: %(ex)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'service'"
op|':'
name|'service'
op|','
string|"'method'"
op|':'
name|'method'
op|','
string|"'ex'"
op|':'
name|'ex'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'vm_state'
op|'='
name|'updates'
op|'['
string|"'vm_state'"
op|']'
newline|'\n'
name|'properties'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
comment|"# NOTE(vish): We shouldn't get here unless we have a catastrophic"
nl|'\n'
comment|'#             failure, so just set all instances to error. if uuid'
nl|'\n'
comment|'#             is not set, instance_uuids will be set to [None], this'
nl|'\n'
comment|'#             is solely to preserve existing behavior and can'
nl|'\n'
comment|"#             be removed along with the 'if instance_uuid:' if we can"
nl|'\n'
comment|'#             verify that uuid is always set.'
nl|'\n'
name|'uuids'
op|'='
op|'['
name|'properties'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|']'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'api'
name|'as'
name|'conductor_api'
newline|'\n'
name|'conductor'
op|'='
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|'('
op|')'
newline|'\n'
name|'notifier'
op|'='
name|'notify'
op|'.'
name|'get_notifier'
op|'('
name|'service'
op|')'
newline|'\n'
name|'for'
name|'instance_uuid'
name|'in'
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_uuids'"
op|')'
name|'or'
name|'uuids'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'            '
name|'state'
op|'='
name|'vm_state'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Setting instance to %s state.'"
op|')'
op|','
name|'state'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|'# update instance state and notify on the transition'
nl|'\n'
op|'('
name|'old_ref'
op|','
name|'new_ref'
op|')'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuid'
op|','
name|'updates'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_ref'
op|','
name|'new_ref'
op|','
nl|'\n'
name|'service'
op|'='
name|'service'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'add_instance_fault_from_exc'
op|'('
name|'context'
op|','
nl|'\n'
name|'conductor'
op|','
nl|'\n'
name|'new_ref'
op|','
name|'ex'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'payload'
op|'='
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'instance_properties'
op|'='
name|'properties'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'state'
op|'='
name|'vm_state'
op|','
nl|'\n'
name|'method'
op|'='
name|'method'
op|','
nl|'\n'
name|'reason'
op|'='
name|'ex'
op|')'
newline|'\n'
nl|'\n'
name|'event_type'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'service'
op|','
name|'method'
op|')'
newline|'\n'
name|'notifier'
op|'.'
name|'error'
op|'('
name|'context'
op|','
name|'event_type'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|populate_filter_properties
dedent|''
dedent|''
name|'def'
name|'populate_filter_properties'
op|'('
name|'filter_properties'
op|','
name|'host_state'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add additional information to the filter properties after a node has\n    been selected by the scheduling process.\n    """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'host_state'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'host_state'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'nodename'
op|'='
name|'host_state'
op|'['
string|"'nodename'"
op|']'
newline|'\n'
name|'limits'
op|'='
name|'host_state'
op|'['
string|"'limits'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'host_state'
op|'.'
name|'host'
newline|'\n'
name|'nodename'
op|'='
name|'host_state'
op|'.'
name|'nodename'
newline|'\n'
name|'limits'
op|'='
name|'host_state'
op|'.'
name|'limits'
newline|'\n'
nl|'\n'
comment|'# Adds a retry entry for the selected compute host and node:'
nl|'\n'
dedent|''
name|'_add_retry_host'
op|'('
name|'filter_properties'
op|','
name|'host'
op|','
name|'nodename'
op|')'
newline|'\n'
nl|'\n'
comment|'# Adds oversubscription policy'
nl|'\n'
name|'if'
name|'not'
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'force_hosts'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'['
string|"'limits'"
op|']'
op|'='
name|'limits'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_add_retry_host
dedent|''
dedent|''
name|'def'
name|'_add_retry_host'
op|'('
name|'filter_properties'
op|','
name|'host'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add a retry entry for the selected compute node. In the event that\n    the request gets re-scheduled, this entry will signal that the given\n    node has already been tried.\n    """'
newline|'\n'
name|'retry'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'retry'"
op|','
name|'None'
op|')'
newline|'\n'
name|'force_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'force_hosts'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'force_nodes'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'force_nodes'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'retry'
name|'or'
name|'force_hosts'
name|'or'
name|'force_nodes'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'hosts'
op|'='
name|'retry'
op|'['
string|"'hosts'"
op|']'
newline|'\n'
name|'hosts'
op|'.'
name|'append'
op|'('
op|'['
name|'host'
op|','
name|'node'
op|']'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
