begin_unit
comment|'# Copyright (c) 2011-2012 OpenStack Foundation'
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
string|'"""\nFilter support\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'loadables'
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
DECL|class|BaseFilter
name|'class'
name|'BaseFilter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all filter classes."""'
newline|'\n'
DECL|member|_filter_one
name|'def'
name|'_filter_one'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if it passes the filter, False otherwise.\n        Override this in a subclass.\n        """'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|filter_all
dedent|''
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'filter_obj_list'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Yield objects that pass the filter.\n\n        Can be overridden in a subclass, if you need to base filtering\n        decisions on all objects.  Otherwise, one can just override\n        _filter_one() to filter a single object.\n        """'
newline|'\n'
name|'for'
name|'obj'
name|'in'
name|'filter_obj_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_filter_one'
op|'('
name|'obj'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'obj'
newline|'\n'
nl|'\n'
comment|'# Set to true in a subclass if a filter only needs to be run once'
nl|'\n'
comment|'# for each request rather than for each instance'
nl|'\n'
DECL|variable|run_filter_once_per_request
dedent|''
dedent|''
dedent|''
name|'run_filter_once_per_request'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|run_filter_for_index
name|'def'
name|'run_filter_for_index'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if the filter needs to be run for the "index-th"\n        instance in a request.  Only need to override this if a filter\n        needs anything other than "first only" or "all" behaviour.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'run_filter_once_per_request'
name|'and'
name|'index'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseFilterHandler
dedent|''
dedent|''
dedent|''
name|'class'
name|'BaseFilterHandler'
op|'('
name|'loadables'
op|'.'
name|'BaseLoader'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class to handle loading filter classes.\n\n    This class should be subclassed where one needs to use filters.\n    """'
newline|'\n'
nl|'\n'
DECL|member|get_filtered_objects
name|'def'
name|'get_filtered_objects'
op|'('
name|'self'
op|','
name|'filters'
op|','
name|'objs'
op|','
name|'filter_properties'
op|','
name|'index'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'list_objs'
op|'='
name|'list'
op|'('
name|'objs'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Starting with %d host(s)"'
op|','
name|'len'
op|'('
name|'list_objs'
op|')'
op|')'
newline|'\n'
comment|"# Track the hosts as they are removed. The 'full_filter_results' list"
nl|'\n'
comment|'# contains the host/nodename info for every host that passes each'
nl|'\n'
comment|"# filter, while the 'part_filter_results' list just tracks the number"
nl|'\n'
comment|'# removed by each filter, unless the filter returns zero hosts, in'
nl|'\n'
comment|'# which case it records the host/nodename for the last batch that was'
nl|'\n'
comment|'# removed. Since the full_filter_results can be very large, it is only'
nl|'\n'
comment|'# recorded if the LOG level is set to debug.'
nl|'\n'
name|'part_filter_results'
op|'='
op|'['
op|']'
newline|'\n'
name|'full_filter_results'
op|'='
op|'['
op|']'
newline|'\n'
name|'log_msg'
op|'='
string|'"%(cls_name)s: (start: %(start)s, end: %(end)s)"'
newline|'\n'
name|'for'
name|'filter_'
name|'in'
name|'filters'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'filter_'
op|'.'
name|'run_filter_for_index'
op|'('
name|'index'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'cls_name'
op|'='
name|'filter_'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'start_count'
op|'='
name|'len'
op|'('
name|'list_objs'
op|')'
newline|'\n'
name|'objs'
op|'='
name|'filter_'
op|'.'
name|'filter_all'
op|'('
name|'list_objs'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'if'
name|'objs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Filter %s says to stop filtering"'
op|','
name|'cls_name'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'list_objs'
op|'='
name|'list'
op|'('
name|'objs'
op|')'
newline|'\n'
name|'end_count'
op|'='
name|'len'
op|'('
name|'list_objs'
op|')'
newline|'\n'
name|'part_filter_results'
op|'.'
name|'append'
op|'('
name|'log_msg'
op|'%'
op|'{'
string|'"cls_name"'
op|':'
name|'cls_name'
op|','
nl|'\n'
string|'"start"'
op|':'
name|'start_count'
op|','
string|'"end"'
op|':'
name|'end_count'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'list_objs'
op|':'
newline|'\n'
indent|'                    '
name|'remaining'
op|'='
op|'['
op|'('
name|'getattr'
op|'('
name|'obj'
op|','
string|'"host"'
op|','
name|'obj'
op|')'
op|','
nl|'\n'
name|'getattr'
op|'('
name|'obj'
op|','
string|'"nodename"'
op|','
string|'""'
op|')'
op|')'
nl|'\n'
name|'for'
name|'obj'
name|'in'
name|'list_objs'
op|']'
newline|'\n'
name|'full_filter_results'
op|'.'
name|'append'
op|'('
op|'('
name|'cls_name'
op|','
name|'remaining'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Filter %s returned 0 hosts"'
op|')'
op|','
name|'cls_name'
op|')'
newline|'\n'
name|'full_filter_results'
op|'.'
name|'append'
op|'('
op|'('
name|'cls_name'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Filter %(cls_name)s returned "'
nl|'\n'
string|'"%(obj_len)d host(s)"'
op|','
nl|'\n'
op|'{'
string|"'cls_name'"
op|':'
name|'cls_name'
op|','
string|"'obj_len'"
op|':'
name|'len'
op|'('
name|'list_objs'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'list_objs'
op|':'
newline|'\n'
comment|'# Log the filtration history'
nl|'\n'
indent|'            '
name|'rspec'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|'"request_spec"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'inst_props'
op|'='
name|'rspec'
op|'.'
name|'get'
op|'('
string|'"instance_properties"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'msg_dict'
op|'='
op|'{'
string|'"res_id"'
op|':'
name|'inst_props'
op|'.'
name|'get'
op|'('
string|'"reservation_id"'
op|','
string|'""'
op|')'
op|','
nl|'\n'
string|'"inst_uuid"'
op|':'
name|'inst_props'
op|'.'
name|'get'
op|'('
string|'"uuid"'
op|','
string|'""'
op|')'
op|','
nl|'\n'
string|'"str_results"'
op|':'
name|'str'
op|'('
name|'full_filter_results'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'full_msg'
op|'='
op|'('
string|'"Filtering removed all hosts for the request with "'
nl|'\n'
string|'"reservation ID \'%(res_id)s\' and instance ID "'
nl|'\n'
string|'"\'%(inst_uuid)s\'. Filter results: %(str_results)s"'
nl|'\n'
op|')'
op|'%'
name|'msg_dict'
newline|'\n'
name|'msg_dict'
op|'['
string|'"str_results"'
op|']'
op|'='
name|'str'
op|'('
name|'part_filter_results'
op|')'
newline|'\n'
name|'part_msg'
op|'='
name|'_LI'
op|'('
string|'"Filtering removed all hosts for the request with "'
nl|'\n'
string|'"reservation ID \'%(res_id)s\' and instance ID "'
nl|'\n'
string|'"\'%(inst_uuid)s\'. Filter results: %(str_results)s"'
nl|'\n'
op|')'
op|'%'
name|'msg_dict'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'full_msg'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'part_msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'list_objs'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
