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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
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
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
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
DECL|variable|scheduler_opts
name|'scheduler_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_max_attempts'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum number of attempts to schedule an instance'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'scheduler_opts'
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
name|'isinstance'
op|'('
name|'instance'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'obj_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'_LW'
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
name|'notifier'
op|'='
name|'rpc'
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
name|'_LW'
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
DECL|function|populate_retry
dedent|''
dedent|''
name|'def'
name|'populate_retry'
op|'('
name|'filter_properties'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'max_attempts'
op|'='
name|'_max_attempts'
op|'('
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
nl|'\n'
name|'if'
name|'max_attempts'
op|'=='
number|'1'
name|'or'
name|'force_hosts'
name|'or'
name|'force_nodes'
op|':'
newline|'\n'
comment|'# re-scheduling is disabled.'
nl|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
comment|'# retry is enabled, update attempt count:'
nl|'\n'
dedent|''
name|'retry'
op|'='
name|'filter_properties'
op|'.'
name|'setdefault'
op|'('
nl|'\n'
string|"'retry'"
op|','
op|'{'
nl|'\n'
string|"'num_attempts'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'hosts'"
op|':'
op|'['
op|']'
comment|'# list of compute hosts tried'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'retry'
op|'['
string|"'num_attempts'"
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'_log_compute_error'
op|'('
name|'instance_uuid'
op|','
name|'retry'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'retry'
op|'.'
name|'pop'
op|'('
string|"'exc'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'retry'
op|'['
string|"'num_attempts'"
op|']'
op|'>'
name|'max_attempts'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|"'Exceeded max scheduling attempts %(max_attempts)d '"
nl|'\n'
string|"'for instance %(instance_uuid)s. '"
nl|'\n'
string|"'Last exception: %(exc)s'"
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'max_attempts'"
op|':'
name|'max_attempts'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'exc'"
op|':'
name|'exc'
op|'}'
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
nl|'\n'
DECL|function|_log_compute_error
dedent|''
dedent|''
name|'def'
name|'_log_compute_error'
op|'('
name|'instance_uuid'
op|','
name|'retry'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""If the request contained an exception from a previous compute\n    build/resize operation, log it to aid debugging\n    """'
newline|'\n'
name|'exc'
op|'='
name|'retry'
op|'.'
name|'get'
op|'('
string|"'exc'"
op|')'
comment|'# string-ified exception from compute'
newline|'\n'
name|'if'
name|'not'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'return'
comment|'# no exception info from a previous attempt, skip'
newline|'\n'
nl|'\n'
dedent|''
name|'hosts'
op|'='
name|'retry'
op|'.'
name|'get'
op|'('
string|"'hosts'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hosts'
op|':'
newline|'\n'
indent|'        '
name|'return'
comment|'# no previously attempted hosts, skip'
newline|'\n'
nl|'\n'
dedent|''
name|'last_host'
op|','
name|'last_node'
op|'='
name|'hosts'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Error from last host: %(last_host)s (node %(last_node)s):'"
nl|'\n'
string|"' %(exc)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'last_host'"
op|':'
name|'last_host'
op|','
nl|'\n'
string|"'last_node'"
op|':'
name|'last_node'
op|','
nl|'\n'
string|"'exc'"
op|':'
name|'exc'
op|'}'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_max_attempts
dedent|''
name|'def'
name|'_max_attempts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'max_attempts'
op|'='
name|'CONF'
op|'.'
name|'scheduler_max_attempts'
newline|'\n'
name|'if'
name|'max_attempts'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Invalid value for "'
nl|'\n'
string|'"\'scheduler_max_attempts\', must be >= 1"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'max_attempts'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_add_retry_host
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
name|'if'
name|'not'
name|'retry'
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
nl|'\n'
nl|'\n'
DECL|function|parse_options
dedent|''
name|'def'
name|'parse_options'
op|'('
name|'opts'
op|','
name|'sep'
op|'='
string|"'='"
op|','
name|'converter'
op|'='
name|'str'
op|','
name|'name'
op|'='
string|'""'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse a list of options, each in the format of <key><sep><value>. Also\n    use the converter to convert the value into desired type.\n\n    :params opts: list of options, e.g. from oslo.config.cfg.ListOpt\n    :params sep: the separator\n    :params converter: callable object to convert the value, should raise\n                       ValueError for conversion failure\n    :params name: name of the option\n\n    :returns: a lists of tuple of values (key, converted_value)\n    """'
newline|'\n'
name|'good'
op|'='
op|'['
op|']'
newline|'\n'
name|'bad'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'opt'
name|'in'
name|'opts'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|','
name|'seen_sep'
op|','
name|'value'
op|'='
name|'opt'
op|'.'
name|'partition'
op|'('
name|'sep'
op|')'
newline|'\n'
name|'value'
op|'='
name|'converter'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
name|'None'
newline|'\n'
name|'value'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'key'
name|'and'
name|'seen_sep'
name|'and'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'good'
op|'.'
name|'append'
op|'('
op|'('
name|'key'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'bad'
op|'.'
name|'append'
op|'('
name|'opt'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'bad'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"Ignoring the invalid elements of the option "'
nl|'\n'
string|'"%(name)s: %(options)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'options'"
op|':'
string|'", "'
op|'.'
name|'join'
op|'('
name|'bad'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'good'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_filter
dedent|''
name|'def'
name|'validate_filter'
op|'('
name|'filter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates that the filter is configured in the default filters."""'
newline|'\n'
name|'return'
name|'filter'
name|'in'
name|'CONF'
op|'.'
name|'scheduler_default_filters'
newline|'\n'
dedent|''
endmarker|''
end_unit
