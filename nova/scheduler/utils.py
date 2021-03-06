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
name|'collections'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_serialization'
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
name|'import'
name|'nova'
op|'.'
name|'conf'
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
name|'_LE'
op|','
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'obj_instance'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|GroupDetails
name|'GroupDetails'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'GroupDetails'"
op|','
op|'['
string|"'hosts'"
op|','
string|"'policies'"
op|','
nl|'\n'
string|"'members'"
op|']'
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
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'obj_instance'
op|'.'
name|'Instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_type'
op|'='
name|'instance'
op|'.'
name|'get_flavor'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'instance_type'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'obj_instance'
op|'.'
name|'Instance'
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
comment|"# obj_to_primitive doesn't copy this enough, so be sure"
nl|'\n'
comment|'# to detach our metadata blob because we modify it below.'
nl|'\n'
name|'instance'
op|'['
string|"'system_metadata'"
op|']'
op|'='
name|'dict'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|"'system_metadata'"
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'instance_type'
op|','
name|'objects'
op|'.'
name|'Flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'obj_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'instance_type'
op|')'
newline|'\n'
comment|'# NOTE(danms): Replicate this old behavior because the'
nl|'\n'
comment|'# scheduler RPC interface technically expects it to be'
nl|'\n'
comment|'# there. Remove this when we bump the scheduler RPC API to'
nl|'\n'
comment|'# v5.0'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|"'system_metadata'"
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|"# If the flavor isn't complete (which is legit with a"
nl|'\n'
comment|"# flavor object, just don't put it in the request spec"
nl|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
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
name|'instance_uuid'
op|','
name|'service'
op|','
name|'method'
op|','
name|'updates'
op|','
nl|'\n'
name|'ex'
op|','
name|'request_spec'
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
comment|'#             failure, so just set the instance to its internal state'
nl|'\n'
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
name|'service'
op|')'
newline|'\n'
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
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
op|'**'
name|'updates'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'add_instance_fault_from_exc'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
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
DECL|function|build_filter_properties
dedent|''
name|'def'
name|'build_filter_properties'
op|'('
name|'scheduler_hints'
op|','
name|'forced_host'
op|','
nl|'\n'
name|'forced_node'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build the filter_properties dict from data in the boot request."""'
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'scheduler_hints'
op|'='
name|'scheduler_hints'
op|')'
newline|'\n'
name|'filter_properties'
op|'['
string|"'instance_type'"
op|']'
op|'='
name|'instance_type'
newline|'\n'
comment|"# TODO(alaski): It doesn't seem necessary that these are conditionally"
nl|'\n'
comment|"# added.  Let's just add empty lists if not forced_host/node."
nl|'\n'
name|'if'
name|'forced_host'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'['
string|"'force_hosts'"
op|']'
op|'='
op|'['
name|'forced_host'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'forced_node'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'['
string|"'force_nodes'"
op|']'
op|'='
op|'['
name|'forced_node'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'filter_properties'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|populate_filter_properties
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
name|'CONF'
op|'.'
name|'scheduler_max_attempts'
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
comment|'# In the case of multiple force hosts/nodes, scheduler should not'
nl|'\n'
comment|'# disable retry filter but traverse all force hosts/nodes one by'
nl|'\n'
comment|'# one till scheduler gets a valid target host.'
nl|'\n'
name|'if'
op|'('
name|'max_attempts'
op|'=='
number|'1'
name|'or'
name|'len'
op|'('
name|'force_hosts'
op|')'
op|'=='
number|'1'
nl|'\n'
name|'or'
name|'len'
op|'('
name|'force_nodes'
op|')'
op|'=='
number|'1'
op|')'
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
name|'exc_reason'
op|'='
name|'retry'
op|'.'
name|'pop'
op|'('
string|"'exc_reason'"
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
string|"'Last exception: %(exc_reason)s'"
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
string|"'exc_reason'"
op|':'
name|'exc_reason'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MaxRetriesExceeded'
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
name|'_LE'
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
string|'"""Parse a list of options, each in the format of <key><sep><value>. Also\n    use the converter to convert the value into desired type.\n\n    :params opts: list of options, e.g. from oslo_config.cfg.ListOpt\n    :params sep: the separator\n    :params converter: callable object to convert the value, should raise\n                       ValueError for conversion failure\n    :params name: name of the option\n\n    :returns: a lists of tuple of values (key, converted_value)\n    """'
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
name|'warning'
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
nl|'\n'
nl|'\n'
DECL|function|validate_weigher
dedent|''
name|'def'
name|'validate_weigher'
op|'('
name|'weigher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates that the weigher is configured in the default weighers."""'
newline|'\n'
name|'if'
string|"'nova.scheduler.weights.all_weighers'"
name|'in'
name|'CONF'
op|'.'
name|'scheduler_weight_classes'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'weigher'
name|'in'
name|'CONF'
op|'.'
name|'scheduler_weight_classes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_SUPPORTS_AFFINITY
dedent|''
name|'_SUPPORTS_AFFINITY'
op|'='
name|'None'
newline|'\n'
DECL|variable|_SUPPORTS_ANTI_AFFINITY
name|'_SUPPORTS_ANTI_AFFINITY'
op|'='
name|'None'
newline|'\n'
DECL|variable|_SUPPORTS_SOFT_AFFINITY
name|'_SUPPORTS_SOFT_AFFINITY'
op|'='
name|'None'
newline|'\n'
DECL|variable|_SUPPORTS_SOFT_ANTI_AFFINITY
name|'_SUPPORTS_SOFT_ANTI_AFFINITY'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_group_details
name|'def'
name|'_get_group_details'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'user_group_hosts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provide group_hosts and group_policies sets related to instances if\n    those instances are belonging to a group and if corresponding filters are\n    enabled.\n\n    :param instance_uuid: UUID of the instance to check\n    :param user_group_hosts: Hosts from the group or empty set\n\n    :returns: None or namedtuple GroupDetails\n    """'
newline|'\n'
name|'global'
name|'_SUPPORTS_AFFINITY'
newline|'\n'
name|'if'
name|'_SUPPORTS_AFFINITY'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_SUPPORTS_AFFINITY'
op|'='
name|'validate_filter'
op|'('
nl|'\n'
string|"'ServerGroupAffinityFilter'"
op|')'
newline|'\n'
dedent|''
name|'global'
name|'_SUPPORTS_ANTI_AFFINITY'
newline|'\n'
name|'if'
name|'_SUPPORTS_ANTI_AFFINITY'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_SUPPORTS_ANTI_AFFINITY'
op|'='
name|'validate_filter'
op|'('
nl|'\n'
string|"'ServerGroupAntiAffinityFilter'"
op|')'
newline|'\n'
dedent|''
name|'global'
name|'_SUPPORTS_SOFT_AFFINITY'
newline|'\n'
name|'if'
name|'_SUPPORTS_SOFT_AFFINITY'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_SUPPORTS_SOFT_AFFINITY'
op|'='
name|'validate_weigher'
op|'('
nl|'\n'
string|"'nova.scheduler.weights.affinity.ServerGroupSoftAffinityWeigher'"
op|')'
newline|'\n'
dedent|''
name|'global'
name|'_SUPPORTS_SOFT_ANTI_AFFINITY'
newline|'\n'
name|'if'
name|'_SUPPORTS_SOFT_ANTI_AFFINITY'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_SUPPORTS_SOFT_ANTI_AFFINITY'
op|'='
name|'validate_weigher'
op|'('
nl|'\n'
string|"'nova.scheduler.weights.affinity.'"
nl|'\n'
string|"'ServerGroupSoftAntiAffinityWeigher'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_instance_uuid'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceGroupNotFound'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'policies'
op|'='
name|'set'
op|'('
op|'('
string|"'anti-affinity'"
op|','
string|"'affinity'"
op|','
string|"'soft-affinity'"
op|','
nl|'\n'
string|"'soft-anti-affinity'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'any'
op|'('
op|'('
name|'policy'
name|'in'
name|'policies'
op|')'
name|'for'
name|'policy'
name|'in'
name|'group'
op|'.'
name|'policies'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'_SUPPORTS_AFFINITY'
name|'and'
string|"'affinity'"
name|'in'
name|'group'
op|'.'
name|'policies'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"ServerGroupAffinityFilter not configured"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'UnsupportedPolicyException'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'_SUPPORTS_ANTI_AFFINITY'
name|'and'
string|"'anti-affinity'"
name|'in'
name|'group'
op|'.'
name|'policies'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"ServerGroupAntiAffinityFilter not configured"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'UnsupportedPolicyException'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'not'
name|'_SUPPORTS_SOFT_AFFINITY'
nl|'\n'
name|'and'
string|"'soft-affinity'"
name|'in'
name|'group'
op|'.'
name|'policies'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"ServerGroupSoftAffinityWeigher not configured"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'UnsupportedPolicyException'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'not'
name|'_SUPPORTS_SOFT_ANTI_AFFINITY'
nl|'\n'
name|'and'
string|"'soft-anti-affinity'"
name|'in'
name|'group'
op|'.'
name|'policies'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"ServerGroupSoftAntiAffinityWeigher not configured"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'UnsupportedPolicyException'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'group_hosts'
op|'='
name|'set'
op|'('
name|'group'
op|'.'
name|'get_hosts'
op|'('
op|')'
op|')'
newline|'\n'
name|'user_hosts'
op|'='
name|'set'
op|'('
name|'user_group_hosts'
op|')'
name|'if'
name|'user_group_hosts'
name|'else'
name|'set'
op|'('
op|')'
newline|'\n'
name|'return'
name|'GroupDetails'
op|'('
name|'hosts'
op|'='
name|'user_hosts'
op|'|'
name|'group_hosts'
op|','
nl|'\n'
name|'policies'
op|'='
name|'group'
op|'.'
name|'policies'
op|','
name|'members'
op|'='
name|'group'
op|'.'
name|'members'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup_instance_group
dedent|''
dedent|''
name|'def'
name|'setup_instance_group'
op|'('
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add group_hosts and group_policies fields to filter_properties dict\n    based on instance uuids provided in request_spec, if those instances are\n    belonging to a group.\n\n    :param request_spec: Request spec\n    :param filter_properties: Filter properties\n    """'
newline|'\n'
name|'group_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'group_hosts'"
op|')'
newline|'\n'
comment|"# NOTE(sbauza) If there are multiple instance UUIDs, it's a boot"
nl|'\n'
comment|"# request and they will all be in the same group, so it's safe to"
nl|'\n'
comment|'# only check the first one.'
nl|'\n'
name|'instance_uuid'
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
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
name|'group_info'
op|'='
name|'_get_group_details'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'group_hosts'
op|')'
newline|'\n'
name|'if'
name|'group_info'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'['
string|"'group_updated'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|'='
name|'group_info'
op|'.'
name|'hosts'
newline|'\n'
name|'filter_properties'
op|'['
string|"'group_policies'"
op|']'
op|'='
name|'group_info'
op|'.'
name|'policies'
newline|'\n'
name|'filter_properties'
op|'['
string|"'group_members'"
op|']'
op|'='
name|'group_info'
op|'.'
name|'members'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|retry_on_timeout
dedent|''
dedent|''
name|'def'
name|'retry_on_timeout'
op|'('
name|'retries'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retry the call in case a MessagingTimeout is raised.\n\n    A decorator for retrying calls when a service dies mid-request.\n\n    :param retries: Number of retries\n    :returns: Decorator\n    """'
newline|'\n'
DECL|function|outer
name|'def'
name|'outer'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'func'
op|')'
newline|'\n'
DECL|function|wrapped
name|'def'
name|'wrapped'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'attempt'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'messaging'
op|'.'
name|'MessagingTimeout'
op|':'
newline|'\n'
indent|'                    '
name|'attempt'
op|'+='
number|'1'
newline|'\n'
name|'if'
name|'attempt'
op|'<='
name|'retries'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
nl|'\n'
string|'"Retrying %(name)s after a MessagingTimeout, "'
nl|'\n'
string|'"attempt %(attempt)s of %(retries)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'attempt'"
op|':'
name|'attempt'
op|','
string|"'retries'"
op|':'
name|'retries'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'func'
op|'.'
name|'__name__'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
dedent|''
name|'return'
name|'outer'
newline|'\n'
nl|'\n'
DECL|variable|retry_select_destinations
dedent|''
name|'retry_select_destinations'
op|'='
name|'retry_on_timeout'
op|'('
name|'CONF'
op|'.'
name|'scheduler_max_attempts'
op|'-'
number|'1'
op|')'
newline|'\n'
endmarker|''
end_unit
