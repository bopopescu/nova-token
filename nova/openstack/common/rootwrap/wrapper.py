begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack Foundation.'
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
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'logging'
op|'.'
name|'handlers'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
nl|'\n'
name|'from'
name|'six'
name|'import'
name|'moves'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rootwrap'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoFilterMatched
name|'class'
name|'NoFilterMatched'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This exception is raised when no filter matched."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FilterMatchNotExecutable
dedent|''
name|'class'
name|'FilterMatchNotExecutable'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Raised when a filter matched but no executable was found."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'match'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'match'
op|'='
name|'match'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RootwrapConfig
dedent|''
dedent|''
name|'class'
name|'RootwrapConfig'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'config'
op|')'
op|':'
newline|'\n'
comment|'# filters_path'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'filters_path'
op|'='
name|'config'
op|'.'
name|'get'
op|'('
string|'"DEFAULT"'
op|','
string|'"filters_path"'
op|')'
op|'.'
name|'split'
op|'('
string|'","'
op|')'
newline|'\n'
nl|'\n'
comment|'# exec_dirs'
nl|'\n'
name|'if'
name|'config'
op|'.'
name|'has_option'
op|'('
string|'"DEFAULT"'
op|','
string|'"exec_dirs"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'exec_dirs'
op|'='
name|'config'
op|'.'
name|'get'
op|'('
string|'"DEFAULT"'
op|','
string|'"exec_dirs"'
op|')'
op|'.'
name|'split'
op|'('
string|'","'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'exec_dirs'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# Use system PATH if exec_dirs is not specified'
nl|'\n'
name|'if'
string|'"PATH"'
name|'in'
name|'os'
op|'.'
name|'environ'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'exec_dirs'
op|'='
name|'os'
op|'.'
name|'environ'
op|'['
string|"'PATH'"
op|']'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
nl|'\n'
comment|'# syslog_log_facility'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'config'
op|'.'
name|'has_option'
op|'('
string|'"DEFAULT"'
op|','
string|'"syslog_log_facility"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'='
name|'config'
op|'.'
name|'get'
op|'('
string|'"DEFAULT"'
op|','
string|'"syslog_log_facility"'
op|')'
newline|'\n'
name|'facility_names'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'.'
name|'facility_names'
newline|'\n'
name|'self'
op|'.'
name|'syslog_log_facility'
op|'='
name|'getattr'
op|'('
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|','
nl|'\n'
name|'v'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'syslog_log_facility'
name|'is'
name|'None'
name|'and'
name|'v'
name|'in'
name|'facility_names'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'syslog_log_facility'
op|'='
name|'facility_names'
op|'.'
name|'get'
op|'('
name|'v'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'syslog_log_facility'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
string|"'Unexpected syslog_log_facility: %s'"
op|'%'
name|'v'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'default_facility'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'.'
name|'LOG_SYSLOG'
newline|'\n'
name|'self'
op|'.'
name|'syslog_log_facility'
op|'='
name|'default_facility'
newline|'\n'
nl|'\n'
comment|'# syslog_log_level'
nl|'\n'
dedent|''
name|'if'
name|'config'
op|'.'
name|'has_option'
op|'('
string|'"DEFAULT"'
op|','
string|'"syslog_log_level"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'='
name|'config'
op|'.'
name|'get'
op|'('
string|'"DEFAULT"'
op|','
string|'"syslog_log_level"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'syslog_log_level'
op|'='
name|'logging'
op|'.'
name|'getLevelName'
op|'('
name|'v'
op|'.'
name|'upper'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'syslog_log_level'
op|'=='
string|'"Level %s"'
op|'%'
name|'v'
op|'.'
name|'upper'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
string|"'Unexepected syslog_log_level: %s'"
op|'%'
name|'v'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'syslog_log_level'
op|'='
name|'logging'
op|'.'
name|'ERROR'
newline|'\n'
nl|'\n'
comment|'# use_syslog'
nl|'\n'
dedent|''
name|'if'
name|'config'
op|'.'
name|'has_option'
op|'('
string|'"DEFAULT"'
op|','
string|'"use_syslog"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'use_syslog'
op|'='
name|'config'
op|'.'
name|'getboolean'
op|'('
string|'"DEFAULT"'
op|','
string|'"use_syslog"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'use_syslog'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup_syslog
dedent|''
dedent|''
dedent|''
name|'def'
name|'setup_syslog'
op|'('
name|'execname'
op|','
name|'facility'
op|','
name|'level'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'rootwrap_logger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'rootwrap_logger'
op|'.'
name|'setLevel'
op|'('
name|'level'
op|')'
newline|'\n'
name|'handler'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'('
name|'address'
op|'='
string|"'/dev/log'"
op|','
nl|'\n'
name|'facility'
op|'='
name|'facility'
op|')'
newline|'\n'
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'logging'
op|'.'
name|'Formatter'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'execname'
op|')'
op|'+'
string|"': %(message)s'"
op|')'
op|')'
newline|'\n'
name|'rootwrap_logger'
op|'.'
name|'addHandler'
op|'('
name|'handler'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_filter
dedent|''
name|'def'
name|'build_filter'
op|'('
name|'class_name'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a filter object of class class_name."""'
newline|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'filters'
op|','
name|'class_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'warning'
op|'('
string|'"Skipping unknown filter class (%s) specified "'
nl|'\n'
string|'"in filter definitions"'
op|'%'
name|'class_name'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'filterclass'
op|'='
name|'getattr'
op|'('
name|'filters'
op|','
name|'class_name'
op|')'
newline|'\n'
name|'return'
name|'filterclass'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_filters
dedent|''
name|'def'
name|'load_filters'
op|'('
name|'filters_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Load filters from a list of directories."""'
newline|'\n'
name|'filterlist'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'filterdir'
name|'in'
name|'filters_path'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'filterdir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'for'
name|'filterfile'
name|'in'
name|'filter'
op|'('
name|'lambda'
name|'f'
op|':'
name|'not'
name|'f'
op|'.'
name|'startswith'
op|'('
string|"'.'"
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'filterdir'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'filterconfig'
op|'='
name|'moves'
op|'.'
name|'configparser'
op|'.'
name|'RawConfigParser'
op|'('
op|')'
newline|'\n'
name|'filterconfig'
op|'.'
name|'read'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'filterdir'
op|','
name|'filterfile'
op|')'
op|')'
newline|'\n'
name|'for'
op|'('
name|'name'
op|','
name|'value'
op|')'
name|'in'
name|'filterconfig'
op|'.'
name|'items'
op|'('
string|'"Filters"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'filterdefinition'
op|'='
op|'['
name|'string'
op|'.'
name|'strip'
op|'('
name|'s'
op|')'
name|'for'
name|'s'
name|'in'
name|'value'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|']'
newline|'\n'
name|'newfilter'
op|'='
name|'build_filter'
op|'('
op|'*'
name|'filterdefinition'
op|')'
newline|'\n'
name|'if'
name|'newfilter'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'newfilter'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'filterlist'
op|'.'
name|'append'
op|'('
name|'newfilter'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'filterlist'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|match_filter
dedent|''
name|'def'
name|'match_filter'
op|'('
name|'filter_list'
op|','
name|'userargs'
op|','
name|'exec_dirs'
op|'='
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks user command and arguments through command filters.\n\n    Returns the first matching filter.\n\n    Raises NoFilterMatched if no filter matched.\n    Raises FilterMatchNotExecutable if no executable was found for the\n    best filter match.\n    """'
newline|'\n'
name|'first_not_executable_filter'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'for'
name|'f'
name|'in'
name|'filter_list'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'f'
op|'.'
name|'match'
op|'('
name|'userargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'f'
op|','
name|'filters'
op|'.'
name|'ChainingFilter'
op|')'
op|':'
newline|'\n'
comment|'# This command calls exec verify that remaining args'
nl|'\n'
comment|'# matches another filter.'
nl|'\n'
DECL|function|non_chain_filter
indent|'                '
name|'def'
name|'non_chain_filter'
op|'('
name|'fltr'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
op|'('
name|'fltr'
op|'.'
name|'run_as'
op|'=='
name|'f'
op|'.'
name|'run_as'
nl|'\n'
name|'and'
name|'not'
name|'isinstance'
op|'('
name|'fltr'
op|','
name|'filters'
op|'.'
name|'ChainingFilter'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'leaf_filters'
op|'='
op|'['
name|'fltr'
name|'for'
name|'fltr'
name|'in'
name|'filter_list'
nl|'\n'
name|'if'
name|'non_chain_filter'
op|'('
name|'fltr'
op|')'
op|']'
newline|'\n'
name|'args'
op|'='
name|'f'
op|'.'
name|'exec_args'
op|'('
name|'userargs'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'args'
name|'or'
name|'not'
name|'match_filter'
op|'('
name|'leaf_filters'
op|','
nl|'\n'
name|'args'
op|','
name|'exec_dirs'
op|'='
name|'exec_dirs'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Try other filters if executable is absent'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'f'
op|'.'
name|'get_exec'
op|'('
name|'exec_dirs'
op|'='
name|'exec_dirs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'first_not_executable_filter'
op|':'
newline|'\n'
indent|'                    '
name|'first_not_executable_filter'
op|'='
name|'f'
newline|'\n'
dedent|''
name|'continue'
newline|'\n'
comment|'# Otherwise return matching filter for execution'
nl|'\n'
dedent|''
name|'return'
name|'f'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'first_not_executable_filter'
op|':'
newline|'\n'
comment|'# A filter matched, but no executable was found for it'
nl|'\n'
indent|'        '
name|'raise'
name|'FilterMatchNotExecutable'
op|'('
name|'match'
op|'='
name|'first_not_executable_filter'
op|')'
newline|'\n'
nl|'\n'
comment|'# No filter matched'
nl|'\n'
dedent|''
name|'raise'
name|'NoFilterMatched'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
