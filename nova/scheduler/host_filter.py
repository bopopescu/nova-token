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
string|'"""\nThe Host Filter classes are a way to ensure that only hosts that are\nappropriate are considered when creating a new instance. Hosts that are\neither incompatible or insufficient to accept a newly-requested instance\nare removed by Host Filter classes from consideration. Those that pass\nthe filter are then passed on for weighting or other process for ordering.\n\nFilters are in the \'filters\' directory that is off the \'scheduler\'\ndirectory of nova. Additional filters can be created and added to that\ndirectory; be sure to add them to the filters/__init__.py file so that\nthey are part of the nova.schedulers.filters namespace.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'types'
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
name|'import'
name|'nova'
op|'.'
name|'scheduler'
newline|'\n'
nl|'\n'
comment|"# NOTE(Vek): Even though we don't use filters in here anywhere, we"
nl|'\n'
comment|'#            depend on default_host_filter being available in FLAGS,'
nl|'\n'
comment|'#            and that happens only when filters/abstract_filter.py is'
nl|'\n'
comment|'#            imported.'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_filters
name|'def'
name|'_get_filters'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Imported here to avoid circular imports'
nl|'\n'
indent|'    '
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
DECL|function|get_itm
name|'def'
name|'get_itm'
op|'('
name|'nm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'filters'
op|','
name|'nm'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'get_itm'
op|'('
name|'itm'
op|')'
name|'for'
name|'itm'
name|'in'
name|'dir'
op|'('
name|'filters'
op|')'
nl|'\n'
name|'if'
op|'('
name|'type'
op|'('
name|'get_itm'
op|'('
name|'itm'
op|')'
op|')'
name|'is'
name|'types'
op|'.'
name|'TypeType'
op|')'
nl|'\n'
name|'and'
name|'issubclass'
op|'('
name|'get_itm'
op|'('
name|'itm'
op|')'
op|','
name|'filters'
op|'.'
name|'AbstractHostFilter'
op|')'
nl|'\n'
name|'and'
name|'get_itm'
op|'('
name|'itm'
op|')'
name|'is'
name|'not'
name|'filters'
op|'.'
name|'AbstractHostFilter'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|choose_host_filter
dedent|''
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
string|'"""Since the caller may specify which filter to use we need\n    to have an authoritative list of what is permissible. This\n    function checks the filter name against a predefined set\n    of acceptable filters.\n    """'
newline|'\n'
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
name|'_get_filters'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'filter_class'
op|'.'
name|'__name__'
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
dedent|''
endmarker|''
end_unit
