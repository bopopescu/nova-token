begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""\nManage hosts in the current zone.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'UserDict'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|host_manager_opts
name|'host_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'reserved_host_disk_mb'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Amount of disk in MB to reserve for host/dom0'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'reserved_host_memory_mb'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'512'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Amount of memory in MB to reserve for host/dom0'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'scheduler_available_filters'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.scheduler.filters.standard_filters'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Filter classes available to the scheduler which may '"
nl|'\n'
string|"'be specified more than once.  An entry of '"
nl|'\n'
string|'\'"nova.scheduler.filters.standard_filters" \''
nl|'\n'
string|"'maps to all filters included with nova.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'scheduler_default_filters'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'AvailabilityZoneFilter'"
op|','
nl|'\n'
string|"'RamFilter'"
op|','
nl|'\n'
string|"'ComputeFilter'"
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Which filter class names to use for filtering hosts '"
nl|'\n'
string|"'when not specified in the request.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'host_manager_opts'
op|')'
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
DECL|class|ReadOnlyDict
name|'class'
name|'ReadOnlyDict'
op|'('
name|'UserDict'
op|'.'
name|'IterableUserDict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A read-only dict."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'source'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'update'
op|'('
name|'source'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|clear
dedent|''
name|'def'
name|'clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|pop
dedent|''
name|'def'
name|'pop'
op|'('
name|'self'
op|','
name|'key'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|popitem
dedent|''
name|'def'
name|'popitem'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'source'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'source'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'source'
op|','
name|'UserDict'
op|'.'
name|'UserDict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'='
name|'source'
op|'.'
name|'data'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'source'
op|','
name|'type'
op|'('
op|'{'
op|'}'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'='
name|'source'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostState
dedent|''
dedent|''
dedent|''
name|'class'
name|'HostState'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mutable and immutable information tracked for a host.\n    This is an attempt to remove the ad-hoc data structures\n    previously used and lock down access.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'topic'
op|','
name|'capabilities'
op|'='
name|'None'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
name|'topic'
newline|'\n'
nl|'\n'
comment|'# Read-only capability dicts'
nl|'\n'
nl|'\n'
name|'if'
name|'capabilities'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'capabilities'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'capabilities'
op|'='
name|'ReadOnlyDict'
op|'('
name|'capabilities'
op|'.'
name|'get'
op|'('
name|'topic'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'if'
name|'service'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'service'
op|'='
name|'ReadOnlyDict'
op|'('
name|'service'
op|')'
newline|'\n'
comment|'# Mutable available resources.'
nl|'\n'
comment|'# These will change as resources are virtually "consumed".'
nl|'\n'
name|'self'
op|'.'
name|'free_ram_mb'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_total'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_used'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|update_from_compute_node
dedent|''
name|'def'
name|'update_from_compute_node'
op|'('
name|'self'
op|','
name|'compute'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update information about a host from its compute_node info."""'
newline|'\n'
name|'all_disk_mb'
op|'='
name|'compute'
op|'['
string|"'local_gb'"
op|']'
op|'*'
number|'1024'
newline|'\n'
name|'all_ram_mb'
op|'='
name|'compute'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'vcpus_total'
op|'='
name|'compute'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'reserved_host_disk_mb'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'all_disk_mb'
op|'-='
name|'FLAGS'
op|'.'
name|'reserved_host_disk_mb'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'reserved_host_memory_mb'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'all_ram_mb'
op|'-='
name|'FLAGS'
op|'.'
name|'reserved_host_memory_mb'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'free_ram_mb'
op|'='
name|'all_ram_mb'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'='
name|'all_disk_mb'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_total'
op|'='
name|'vcpus_total'
newline|'\n'
nl|'\n'
DECL|member|consume_from_instance
dedent|''
name|'def'
name|'consume_from_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update information about a host from instance info."""'
newline|'\n'
name|'disk_mb'
op|'='
op|'('
name|'instance'
op|'['
string|"'root_gb'"
op|']'
op|'+'
name|'instance'
op|'['
string|"'ephemeral_gb'"
op|']'
op|')'
op|'*'
number|'1024'
newline|'\n'
name|'ram_mb'
op|'='
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'vcpus'
op|'='
name|'instance'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'free_ram_mb'
op|'-='
name|'ram_mb'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'-='
name|'disk_mb'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_used'
op|'+='
name|'vcpus'
newline|'\n'
nl|'\n'
DECL|member|passes_filters
dedent|''
name|'def'
name|'passes_filters'
op|'('
name|'self'
op|','
name|'filter_fns'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return whether or not this host passes filters."""'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'host'
name|'in'
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'ignore_hosts'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Host filter fails for ignored host %(host)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
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
name|'if'
name|'force_hosts'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'host'
name|'in'
name|'force_hosts'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Host filter fails for non-forced host %(host)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'host'
name|'in'
name|'force_hosts'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'filter_fn'
name|'in'
name|'filter_fns'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'filter_fn'
op|'('
name|'self'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Host filter function %(func)s failed for '"
nl|'\n'
string|"'%(host)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'func'"
op|':'
name|'repr'
op|'('
name|'filter_fn'
op|')'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Host filter passes for %(host)s'"
op|')'
op|','
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"host \'%s\': free_ram_mb:%s free_disk_mb:%s"'
op|'%'
nl|'\n'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'free_ram_mb'
op|','
name|'self'
op|'.'
name|'free_disk_mb'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostManager
dedent|''
dedent|''
name|'class'
name|'HostManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base HostManager class."""'
newline|'\n'
nl|'\n'
comment|'# Can be overriden in a subclass'
nl|'\n'
DECL|variable|host_state_cls
name|'host_state_cls'
op|'='
name|'HostState'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service_states'
op|'='
op|'{'
op|'}'
comment|'# { <host> : { <service> : { cap k : v }}}'
newline|'\n'
name|'self'
op|'.'
name|'filter_classes'
op|'='
name|'filters'
op|'.'
name|'get_filter_classes'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'scheduler_available_filters'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_choose_host_filters
dedent|''
name|'def'
name|'_choose_host_filters'
op|'('
name|'self'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Since the caller may specify which filters to use we need\n        to have an authoritative list of what is permissible. This\n        function checks the filter names against a predefined set\n        of acceptable filters.\n        """'
newline|'\n'
name|'if'
name|'filters'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'='
name|'FLAGS'
op|'.'
name|'scheduler_default_filters'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'filters'
op|','
op|'('
name|'list'
op|','
name|'tuple'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'='
op|'['
name|'filters'
op|']'
newline|'\n'
dedent|''
name|'good_filters'
op|'='
op|'['
op|']'
newline|'\n'
name|'bad_filters'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'filter_name'
name|'in'
name|'filters'
op|':'
newline|'\n'
indent|'            '
name|'found_class'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'cls'
name|'in'
name|'self'
op|'.'
name|'filter_classes'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'cls'
op|'.'
name|'__name__'
op|'=='
name|'filter_name'
op|':'
newline|'\n'
indent|'                    '
name|'found_class'
op|'='
name|'True'
newline|'\n'
name|'filter_instance'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
comment|'# Get the filter function'
nl|'\n'
name|'filter_func'
op|'='
name|'getattr'
op|'('
name|'filter_instance'
op|','
nl|'\n'
string|"'host_passes'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'filter_func'
op|':'
newline|'\n'
indent|'                        '
name|'good_filters'
op|'.'
name|'append'
op|'('
name|'filter_func'
op|')'
newline|'\n'
dedent|''
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'found_class'
op|':'
newline|'\n'
indent|'                '
name|'bad_filters'
op|'.'
name|'append'
op|'('
name|'filter_name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'bad_filters'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
string|'", "'
op|'.'
name|'join'
op|'('
name|'bad_filters'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'SchedulerHostFilterNotFound'
op|'('
name|'filter_name'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'good_filters'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'hosts'
op|','
name|'filter_properties'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter hosts and return only ones passing all filters"""'
newline|'\n'
name|'filtered_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'filter_fns'
op|'='
name|'self'
op|'.'
name|'_choose_host_filters'
op|'('
name|'filters'
op|')'
newline|'\n'
name|'for'
name|'host'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'host'
op|'.'
name|'passes_filters'
op|'('
name|'filter_fns'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'filtered_hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'filtered_hosts'
newline|'\n'
nl|'\n'
DECL|member|get_host_list
dedent|''
name|'def'
name|'get_host_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of dicts for each host that the Zone Manager\n        knows about. Each dict contains the host_name and the service\n        for that host.\n        """'
newline|'\n'
name|'all_hosts'
op|'='
name|'self'
op|'.'
name|'service_states'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'ret'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'host'
name|'in'
name|'self'
op|'.'
name|'service_states'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'svc'
name|'in'
name|'self'
op|'.'
name|'service_states'
op|'['
name|'host'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|'.'
name|'append'
op|'('
op|'{'
string|'"service"'
op|':'
name|'svc'
op|','
string|'"host_name"'
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|get_service_capabilities
dedent|''
name|'def'
name|'get_service_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Roll up all the individual host info to generic \'service\'\n           capabilities. Each capability is aggregated into\n           <cap>_min and <cap>_max values."""'
newline|'\n'
name|'hosts_dict'
op|'='
name|'self'
op|'.'
name|'service_states'
newline|'\n'
nl|'\n'
comment|'# TODO(sandy) - be smarter about fabricating this structure.'
nl|'\n'
comment|"# But it's likely to change once we understand what the Best-Match"
nl|'\n'
comment|'# code will need better.'
nl|'\n'
name|'combined'
op|'='
op|'{'
op|'}'
comment|'# { <service>_<cap> : (min, max), ... }'
newline|'\n'
name|'stale_host_services'
op|'='
op|'{'
op|'}'
comment|'# { host1 : [svc1, svc2], host2 :[svc1]}'
newline|'\n'
name|'for'
name|'host'
op|','
name|'host_dict'
name|'in'
name|'hosts_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'service_name'
op|','
name|'service_dict'
name|'in'
name|'host_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'service_dict'
op|'.'
name|'get'
op|'('
string|'"enabled"'
op|','
name|'True'
op|')'
op|':'
newline|'\n'
comment|'# Service is disabled; do no include it'
nl|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Check if the service capabilities became stale'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'host_service_caps_stale'
op|'('
name|'host'
op|','
name|'service_name'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'host'
name|'not'
name|'in'
name|'stale_host_services'
op|':'
newline|'\n'
indent|'                        '
name|'stale_host_services'
op|'['
name|'host'
op|']'
op|'='
op|'['
op|']'
comment|'# Adding host key once'
newline|'\n'
dedent|''
name|'stale_host_services'
op|'['
name|'host'
op|']'
op|'.'
name|'append'
op|'('
name|'service_name'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'for'
name|'cap'
op|','
name|'value'
name|'in'
name|'service_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'cap'
op|'=='
string|'"timestamp"'
op|':'
comment|'# Timestamp is not needed'
newline|'\n'
indent|'                        '
name|'continue'
newline|'\n'
dedent|''
name|'key'
op|'='
string|'"%s_%s"'
op|'%'
op|'('
name|'service_name'
op|','
name|'cap'
op|')'
newline|'\n'
name|'min_value'
op|','
name|'max_value'
op|'='
name|'combined'
op|'.'
name|'get'
op|'('
name|'key'
op|','
op|'('
name|'value'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
name|'min_value'
op|'='
name|'min'
op|'('
name|'min_value'
op|','
name|'value'
op|')'
newline|'\n'
name|'max_value'
op|'='
name|'max'
op|'('
name|'max_value'
op|','
name|'value'
op|')'
newline|'\n'
name|'combined'
op|'['
name|'key'
op|']'
op|'='
op|'('
name|'min_value'
op|','
name|'max_value'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the expired host services'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'delete_expired_host_services'
op|'('
name|'stale_host_services'
op|')'
newline|'\n'
name|'return'
name|'combined'
newline|'\n'
nl|'\n'
DECL|member|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'self'
op|','
name|'service_name'
op|','
name|'host'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the per-service capabilities based on this notification."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Received %(service_name)s service update from "'
nl|'\n'
string|'"%(host)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'service_caps'
op|'='
name|'self'
op|'.'
name|'service_states'
op|'.'
name|'get'
op|'('
name|'host'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
comment|"# Copy the capabilities, so we don't modify the original dict"
nl|'\n'
name|'capab_copy'
op|'='
name|'dict'
op|'('
name|'capabilities'
op|')'
newline|'\n'
name|'capab_copy'
op|'['
string|'"timestamp"'
op|']'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
comment|'# Reported time'
newline|'\n'
name|'service_caps'
op|'['
name|'service_name'
op|']'
op|'='
name|'capab_copy'
newline|'\n'
name|'self'
op|'.'
name|'service_states'
op|'['
name|'host'
op|']'
op|'='
name|'service_caps'
newline|'\n'
nl|'\n'
DECL|member|host_service_caps_stale
dedent|''
name|'def'
name|'host_service_caps_stale'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if host service capabilites are not recent enough."""'
newline|'\n'
name|'allowed_time_diff'
op|'='
name|'FLAGS'
op|'.'
name|'periodic_interval'
op|'*'
number|'3'
newline|'\n'
name|'caps'
op|'='
name|'self'
op|'.'
name|'service_states'
op|'['
name|'host'
op|']'
op|'['
name|'service'
op|']'
newline|'\n'
name|'if'
op|'('
op|'('
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'caps'
op|'['
string|'"timestamp"'
op|']'
op|')'
op|'<='
nl|'\n'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'allowed_time_diff'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|delete_expired_host_services
dedent|''
name|'def'
name|'delete_expired_host_services'
op|'('
name|'self'
op|','
name|'host_services_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete all the inactive host services information."""'
newline|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'host_services_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'service_caps'
op|'='
name|'self'
op|'.'
name|'service_states'
op|'['
name|'host'
op|']'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'service_caps'
op|'['
name|'service'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'service_caps'
op|')'
op|'=='
number|'0'
op|':'
comment|'# Delete host if no services'
newline|'\n'
indent|'                    '
name|'del'
name|'self'
op|'.'
name|'service_states'
op|'['
name|'host'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_all_host_states
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_all_host_states'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a dict of all the hosts the HostManager\n        knows about. Also, each of the consumable resources in HostState\n        are pre-populated and adjusted based on data in the db.\n\n        For example:\n        {\'192.168.1.100\': HostState(), ...}\n\n        Note: this can be very slow with a lot of instances.\n        InstanceType table isn\'t required since a copy is stored\n        with the instance (in case the InstanceType changed since the\n        instance was created)."""'
newline|'\n'
nl|'\n'
name|'if'
name|'topic'
op|'!='
string|"'compute'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
nl|'\n'
string|'"host_manager only implemented for \'compute\'"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'host_state_map'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Make a compute node dict with the bare essential metrics.'
nl|'\n'
name|'compute_nodes'
op|'='
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'for'
name|'compute'
name|'in'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'compute'
op|'['
string|"'service'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'service'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"No service for compute ID %s"'
op|')'
op|'%'
name|'compute'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'service'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'capabilities'
op|'='
name|'self'
op|'.'
name|'service_states'
op|'.'
name|'get'
op|'('
name|'host'
op|','
name|'None'
op|')'
newline|'\n'
name|'host_state'
op|'='
name|'self'
op|'.'
name|'host_state_cls'
op|'('
name|'host'
op|','
name|'topic'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'capabilities'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'service'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'host_state'
op|'.'
name|'update_from_compute_node'
op|'('
name|'compute'
op|')'
newline|'\n'
name|'host_state_map'
op|'['
name|'host'
op|']'
op|'='
name|'host_state'
newline|'\n'
nl|'\n'
comment|'# "Consume" resources from the host the instance resides on.'
nl|'\n'
dedent|''
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'host_state'
op|'='
name|'host_state_map'
op|'.'
name|'get'
op|'('
name|'host'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'host_state'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'host_state'
op|'.'
name|'consume_from_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'host_state_map'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
