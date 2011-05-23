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
string|'"""\nHost Filter is a mechanism for requesting instance resources.\nThree filters are included: AllHosts, Flavor & JSON. AllHosts just\nreturns the full, unfiltered list of hosts. Flavor is a hard coded\nmatching mechanism based on flavor criteria and JSON is an ad-hoc\nfilter grammar.\n\nWhy JSON? The requests for instances may come in through the\nREST interface from a user or a parent Zone.\nCurrently Flavors and/or InstanceTypes are used for\nspecifing the type of instance desired. Specific Nova users have\nnoted a need for a more expressive way of specifying instances.\nSince we don\'t want to get into building full DSL this is a simple\nform as an example of how this could be done. In reality, most\nconsumers will use the more rigid filters such as FlavorFilter.\n\nNote: These are "required" capability filters. These capabilities\nused must be present or the host will be excluded. The hosts\nreturned are then weighed by the Weighted Scheduler. Weights\ncan take the more esoteric factors into consideration (such as\nserver affinity and customer separation).\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
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
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'zone_aware_scheduler'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.host_filter'"
op|')'
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
name|'DEFINE_string'
op|'('
string|"'default_host_filter'"
op|','
nl|'\n'
string|"'nova.scheduler.host_filter.AllHostsFilter'"
op|','
nl|'\n'
string|"'Which filter to use for filtering hosts.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostFilter
name|'class'
name|'HostFilter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for host filters."""'
newline|'\n'
nl|'\n'
DECL|member|instance_type_to_filter
name|'def'
name|'instance_type_to_filter'
op|'('
name|'self'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert instance_type into a filter for most common use-case."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'zone_manager'
op|','
name|'query'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of hosts that fulfill the filter."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_full_name
dedent|''
name|'def'
name|'_full_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""module.classname of the filter."""'
newline|'\n'
name|'return'
string|'"%s.%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__module__'
op|','
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AllHostsFilter
dedent|''
dedent|''
name|'class'
name|'AllHostsFilter'
op|'('
name|'HostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""NOP host filter. Returns all hosts in ZoneManager.\n    This essentially does what the old Scheduler+Chance used\n    to give us."""'
newline|'\n'
nl|'\n'
DECL|member|instance_type_to_filter
name|'def'
name|'instance_type_to_filter'
op|'('
name|'self'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return anything to prevent base-class from raising\n        exception."""'
newline|'\n'
name|'return'
op|'('
name|'self'
op|'.'
name|'_full_name'
op|'('
op|')'
op|','
name|'instance_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'zone_manager'
op|','
name|'query'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of hosts from ZoneManager list."""'
newline|'\n'
name|'return'
op|'['
op|'('
name|'host'
op|','
name|'services'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTypeFilter
dedent|''
dedent|''
name|'class'
name|'InstanceTypeFilter'
op|'('
name|'HostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""HostFilter hard-coded to work with InstanceType records."""'
newline|'\n'
nl|'\n'
DECL|member|instance_type_to_filter
name|'def'
name|'instance_type_to_filter'
op|'('
name|'self'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Use instance_type to filter hosts."""'
newline|'\n'
name|'return'
op|'('
name|'self'
op|'.'
name|'_full_name'
op|'('
op|')'
op|','
name|'instance_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'zone_manager'
op|','
name|'query'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of hosts that can create instance_type."""'
newline|'\n'
name|'instance_type'
op|'='
name|'query'
newline|'\n'
name|'selected_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'capabilities'
op|'='
name|'services'
op|'.'
name|'get'
op|'('
string|"'compute'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'host_ram_mb'
op|'='
name|'capabilities'
op|'['
string|"'host_memory_free'"
op|']'
newline|'\n'
name|'disk_bytes'
op|'='
name|'capabilities'
op|'['
string|"'disk_available'"
op|']'
newline|'\n'
name|'spec_ram'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'spec_disk'
op|'='
name|'instance_type'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'if'
name|'host_ram_mb'
op|'>='
name|'spec_ram'
name|'and'
name|'disk_bytes'
op|'>='
name|'spec_disk'
op|':'
newline|'\n'
indent|'                '
name|'selected_hosts'
op|'.'
name|'append'
op|'('
op|'('
name|'host'
op|','
name|'capabilities'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'selected_hosts'
newline|'\n'
nl|'\n'
comment|'#host entries (currently) are like:'
nl|'\n'
comment|"#    {'host_name-description': 'Default install of XenServer',"
nl|'\n'
comment|"#    'host_hostname': 'xs-mini',"
nl|'\n'
comment|"#    'host_memory_total': 8244539392,"
nl|'\n'
comment|"#    'host_memory_overhead': 184225792,"
nl|'\n'
comment|"#    'host_memory_free': 3868327936,"
nl|'\n'
comment|"#    'host_memory_free_computed': 3840843776,"
nl|'\n'
comment|"#    'host_other_config': {},"
nl|'\n'
comment|"#    'host_ip_address': '192.168.1.109',"
nl|'\n'
comment|"#    'host_cpu_info': {},"
nl|'\n'
comment|"#    'disk_available': 32954957824,"
nl|'\n'
comment|"#    'disk_total': 50394562560,"
nl|'\n'
comment|"#    'disk_used': 17439604736,"
nl|'\n'
comment|"#    'host_uuid': 'cedb9b39-9388-41df-8891-c5c9a0c0fe5f',"
nl|'\n'
comment|"#    'host_name_label': 'xs-mini'}"
nl|'\n'
nl|'\n'
comment|'# instance_type table has:'
nl|'\n'
comment|'#name = Column(String(255), unique=True)'
nl|'\n'
comment|'#memory_mb = Column(Integer)'
nl|'\n'
comment|'#vcpus = Column(Integer)'
nl|'\n'
comment|'#local_gb = Column(Integer)'
nl|'\n'
comment|'#flavorid = Column(Integer, unique=True)'
nl|'\n'
comment|'#swap = Column(Integer, nullable=False, default=0)'
nl|'\n'
comment|'#rxtx_quota = Column(Integer, nullable=False, default=0)'
nl|'\n'
comment|'#rxtx_cap = Column(Integer, nullable=False, default=0)'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|JsonFilter
dedent|''
dedent|''
name|'class'
name|'JsonFilter'
op|'('
name|'HostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Host Filter to allow simple JSON-based grammar for\n       selecting hosts."""'
newline|'\n'
nl|'\n'
DECL|member|_equals
name|'def'
name|'_equals'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is == all the other terms."""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'<'
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'lhs'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'rhs'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'lhs'
op|'!='
name|'rhs'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_less_than
dedent|''
name|'def'
name|'_less_than'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is < all the other terms."""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'<'
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'lhs'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'rhs'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'lhs'
op|'>='
name|'rhs'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_greater_than
dedent|''
name|'def'
name|'_greater_than'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is > all the other terms."""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'<'
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'lhs'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'rhs'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'lhs'
op|'<='
name|'rhs'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_in
dedent|''
name|'def'
name|'_in'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is in set of remaining terms"""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'<'
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'args'
op|'['
number|'0'
op|']'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_less_than_equal
dedent|''
name|'def'
name|'_less_than_equal'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is <= all the other terms."""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'<'
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'lhs'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'rhs'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'lhs'
op|'>'
name|'rhs'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_greater_than_equal
dedent|''
name|'def'
name|'_greater_than_equal'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""First term is >= all the other terms."""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'<'
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'lhs'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'for'
name|'rhs'
name|'in'
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'lhs'
op|'<'
name|'rhs'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_not
dedent|''
name|'def'
name|'_not'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Flip each of the arguments."""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
op|'['
name|'not'
name|'arg'
name|'for'
name|'arg'
name|'in'
name|'args'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_or
dedent|''
name|'def'
name|'_or'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""True if any arg is True."""'
newline|'\n'
name|'return'
name|'True'
name|'in'
name|'args'
newline|'\n'
nl|'\n'
DECL|member|_and
dedent|''
name|'def'
name|'_and'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""True if all args are True."""'
newline|'\n'
name|'return'
name|'False'
name|'not'
name|'in'
name|'args'
newline|'\n'
nl|'\n'
DECL|variable|commands
dedent|''
name|'commands'
op|'='
op|'{'
nl|'\n'
string|"'='"
op|':'
name|'_equals'
op|','
nl|'\n'
string|"'<'"
op|':'
name|'_less_than'
op|','
nl|'\n'
string|"'>'"
op|':'
name|'_greater_than'
op|','
nl|'\n'
string|"'in'"
op|':'
name|'_in'
op|','
nl|'\n'
string|"'<='"
op|':'
name|'_less_than_equal'
op|','
nl|'\n'
string|"'>='"
op|':'
name|'_greater_than_equal'
op|','
nl|'\n'
string|"'not'"
op|':'
name|'_not'
op|','
nl|'\n'
string|"'or'"
op|':'
name|'_or'
op|','
nl|'\n'
string|"'and'"
op|':'
name|'_and'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|instance_type_to_filter
name|'def'
name|'instance_type_to_filter'
op|'('
name|'self'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert instance_type into JSON filter object."""'
newline|'\n'
name|'required_ram'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'required_disk'
op|'='
name|'instance_type'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'query'
op|'='
op|'['
string|"'and'"
op|','
nl|'\n'
op|'['
string|"'>='"
op|','
string|"'$compute.host_memory_free'"
op|','
name|'required_ram'
op|']'
op|','
nl|'\n'
op|'['
string|"'>='"
op|','
string|"'$compute.disk_available'"
op|','
name|'required_disk'
op|']'
nl|'\n'
op|']'
newline|'\n'
name|'return'
op|'('
name|'self'
op|'.'
name|'_full_name'
op|'('
op|')'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'query'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parse_string
dedent|''
name|'def'
name|'_parse_string'
op|'('
name|'self'
op|','
name|'string'
op|','
name|'host'
op|','
name|'services'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Strings prefixed with $ are capability lookups in the\n        form \'$service.capability[.subcap*]\'"""'
newline|'\n'
name|'if'
name|'not'
name|'string'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'string'
op|'['
number|'0'
op|']'
op|'!='
string|"'$'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'string'
newline|'\n'
nl|'\n'
dedent|''
name|'path'
op|'='
name|'string'
op|'['
number|'1'
op|':'
op|']'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'path'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
name|'services'
op|'.'
name|'get'
op|'('
name|'item'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'services'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'services'
newline|'\n'
nl|'\n'
DECL|member|_process_filter
dedent|''
name|'def'
name|'_process_filter'
op|'('
name|'self'
op|','
name|'zone_manager'
op|','
name|'query'
op|','
name|'host'
op|','
name|'services'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Recursively parse the query structure."""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'query'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'cmd'
op|'='
name|'query'
op|'['
number|'0'
op|']'
newline|'\n'
name|'method'
op|'='
name|'self'
op|'.'
name|'commands'
op|'['
name|'cmd'
op|']'
comment|'# Let exception fly.'
newline|'\n'
name|'cooked_args'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'arg'
name|'in'
name|'query'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'arg'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'arg'
op|'='
name|'self'
op|'.'
name|'_process_filter'
op|'('
name|'zone_manager'
op|','
name|'arg'
op|','
name|'host'
op|','
name|'services'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'arg'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'arg'
op|'='
name|'self'
op|'.'
name|'_parse_string'
op|'('
name|'arg'
op|','
name|'host'
op|','
name|'services'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'arg'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'cooked_args'
op|'.'
name|'append'
op|'('
name|'arg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'result'
op|'='
name|'method'
op|'('
name|'self'
op|','
name|'cooked_args'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'zone_manager'
op|','
name|'query'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of hosts that can fulfill filter."""'
newline|'\n'
name|'expanded'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'query'
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'r'
op|'='
name|'self'
op|'.'
name|'_process_filter'
op|'('
name|'zone_manager'
op|','
name|'expanded'
op|','
name|'host'
op|','
name|'services'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'r'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'r'
op|'='
name|'True'
name|'in'
name|'r'
newline|'\n'
dedent|''
name|'if'
name|'r'
op|':'
newline|'\n'
indent|'                '
name|'hosts'
op|'.'
name|'append'
op|'('
op|'('
name|'host'
op|','
name|'services'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'hosts'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FILTERS
dedent|''
dedent|''
name|'FILTERS'
op|'='
op|'['
name|'AllHostsFilter'
op|','
name|'InstanceTypeFilter'
op|','
name|'JsonFilter'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|choose_host_filter
name|'def'
name|'choose_host_filter'
op|'('
name|'filter_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Since the caller may specify which filter to use we need\n       to have an authoritative list of what is permissible. This\n       function checks the filter name against a predefined set\n       of acceptable filters."""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'filter_name'
op|':'
newline|'\n'
indent|'        '
name|'filter_name'
op|'='
name|'FLAGS'
op|'.'
name|'default_host_filter'
newline|'\n'
dedent|''
name|'for'
name|'filter_class'
name|'in'
name|'FILTERS'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|'"%s.%s"'
op|'%'
op|'('
name|'filter_class'
op|'.'
name|'__module__'
op|','
name|'filter_class'
op|'.'
name|'__name__'
op|')'
op|'=='
name|'filter_name'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'filter_class'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'SchedulerHostFilterNotFound'
op|'('
name|'filter_name'
op|'='
name|'filter_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostFilterScheduler
dedent|''
name|'class'
name|'HostFilterScheduler'
op|'('
name|'zone_aware_scheduler'
op|'.'
name|'ZoneAwareScheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The HostFilterScheduler uses the HostFilter to filter\n    hosts for weighing. The particular filter used may be passed in\n    as an argument or the default will be used.\n\n    request_spec = {\'filter_name\': <Filter name>,\n                    \'instance_type\': <InstanceType dict>}\n    """'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'num'
op|','
name|'request_spec'
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
string|"'filter_name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'host_filter'
op|'='
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
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'name'
op|','
name|'query'
op|'='
name|'host_filter'
op|'.'
name|'instance_type_to_filter'
op|'('
name|'instance_type'
op|')'
newline|'\n'
name|'return'
name|'host_filter'
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
name|'num'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Derived classes must override this method and return\n           a lists of hosts in [{weight, hostname}] format."""'
newline|'\n'
name|'return'
op|'['
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'hostname'
op|'='
name|'host'
op|')'
name|'for'
name|'host'
op|','
name|'caps'
name|'in'
name|'hosts'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
