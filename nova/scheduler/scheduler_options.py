begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
string|'"""\nSchedulerOptions monitors a local .json file for changes and loads\nit if needed. This file is converted to a data structure and passed\ninto the filtering and weighing functions which can use it for\ndynamic configuration.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
nl|'\n'
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
DECL|class|SchedulerOptions
name|'class'
name|'SchedulerOptions'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""SchedulerOptions monitors a local .json file for changes and loads it\n    if needed. This file is converted to a data structure and passed into\n    the filtering and weighing functions which can use it for dynamic\n    configuration.\n    """'
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
name|'super'
op|'('
name|'SchedulerOptions'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'last_modified'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'last_checked'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_file_handle
dedent|''
name|'def'
name|'_get_file_handle'
op|'('
name|'self'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get file handle. Broken out for testing."""'
newline|'\n'
name|'return'
name|'open'
op|'('
name|'filename'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_file_timestamp
dedent|''
name|'def'
name|'_get_file_timestamp'
op|'('
name|'self'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the last modified datetime. Broken out for testing."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'getmtime'
op|'('
name|'filename'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'os'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Could not stat scheduler options file "'
nl|'\n'
string|'"%(filename)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'filename'"
op|':'
name|'filename'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_file
dedent|''
dedent|''
dedent|''
name|'def'
name|'_load_file'
op|'('
name|'self'
op|','
name|'handle'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Decode the JSON file. Broken out for testing."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'jsonutils'
op|'.'
name|'load'
op|'('
name|'handle'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Could not decode scheduler options"'
op|')'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_time_now
dedent|''
dedent|''
name|'def'
name|'_get_time_now'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get current UTC. Broken out for testing."""'
newline|'\n'
name|'return'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_configuration
dedent|''
name|'def'
name|'get_configuration'
op|'('
name|'self'
op|','
name|'filename'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check the json file for changes and load it if needed."""'
newline|'\n'
name|'if'
name|'not'
name|'filename'
op|':'
newline|'\n'
indent|'            '
name|'filename'
op|'='
name|'CONF'
op|'.'
name|'scheduler_json_config_location'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'filename'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'data'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'last_checked'
op|':'
newline|'\n'
indent|'            '
name|'now'
op|'='
name|'self'
op|'.'
name|'_get_time_now'
op|'('
op|')'
newline|'\n'
name|'if'
name|'now'
op|'-'
name|'self'
op|'.'
name|'last_checked'
op|'<'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'minutes'
op|'='
number|'5'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'last_modified'
op|'='
name|'self'
op|'.'
name|'_get_file_timestamp'
op|'('
name|'filename'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'last_modified'
name|'or'
name|'not'
name|'self'
op|'.'
name|'last_modified'
name|'or'
nl|'\n'
name|'last_modified'
op|'>'
name|'self'
op|'.'
name|'last_modified'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'='
name|'self'
op|'.'
name|'_load_file'
op|'('
name|'self'
op|'.'
name|'_get_file_handle'
op|'('
name|'filename'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'last_modified'
op|'='
name|'last_modified'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
