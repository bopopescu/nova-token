begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
comment|'#'
nl|'\n'
comment|'# XenAPI plugin for reading/writing information to xenstore'
nl|'\n'
comment|'#'
nl|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'json'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'simplejson'
name|'as'
name|'json'
newline|'\n'
nl|'\n'
dedent|''
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
nl|'\n'
name|'import'
name|'XenAPIPlugin'
newline|'\n'
nl|'\n'
name|'import'
name|'pluginlib_nova'
name|'as'
name|'pluginlib'
newline|'\n'
name|'pluginlib'
op|'.'
name|'configure_logging'
op|'('
string|'"xenstore"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenstoreError
name|'class'
name|'XenstoreError'
op|'('
name|'pluginlib'
op|'.'
name|'PluginError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Errors that occur when calling xenstore-* through subprocesses."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cmd'
op|','
name|'return_code'
op|','
name|'stderr'
op|','
name|'stdout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
string|'"cmd: %s; returncode: %d; stderr: %s; stdout: %s"'
newline|'\n'
name|'msg'
op|'='
name|'msg'
op|'%'
op|'('
name|'cmd'
op|','
name|'return_code'
op|','
name|'stderr'
op|','
name|'stdout'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cmd'
op|'='
name|'cmd'
newline|'\n'
name|'self'
op|'.'
name|'return_code'
op|'='
name|'return_code'
newline|'\n'
name|'self'
op|'.'
name|'stderr'
op|'='
name|'stderr'
newline|'\n'
name|'self'
op|'.'
name|'stdout'
op|'='
name|'stdout'
newline|'\n'
name|'pluginlib'
op|'.'
name|'PluginError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|jsonify
dedent|''
dedent|''
name|'def'
name|'jsonify'
op|'('
name|'fnc'
op|')'
op|':'
newline|'\n'
DECL|function|wrapper
indent|'    '
name|'def'
name|'wrapper'
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
name|'ret'
op|'='
name|'fnc'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'json'
op|'.'
name|'loads'
op|'('
name|'ret'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|'# Value should already be JSON-encoded, but some operations'
nl|'\n'
comment|'# may write raw sting values; this will catch those and'
nl|'\n'
comment|'# properly encode them.'
nl|'\n'
indent|'            '
name|'ret'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'ret'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_record_exists
dedent|''
name|'def'
name|'_record_exists'
op|'('
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns whether or not the given record exists. The record path\n    is determined from the given path and dom_id in the arg_dict."""'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|'"xenstore-exists"'
op|','
string|'"/local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|','
name|'result'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenstoreError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'stderr'
op|'=='
string|"''"
op|':'
newline|'\n'
comment|'# if stderr was empty, this just means the path did not exist'
nl|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
comment|'# otherwise there was a real problem'
nl|'\n'
dedent|''
name|'raise'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|read_record
name|'def'
name|'read_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the value stored at the given path for the given dom_id.\n    These must be encoded as key/value pairs in arg_dict. You can\n    optinally include a key \'ignore_missing_path\'; if this is present\n    and boolean True, attempting to read a non-existent path will return\n    the string \'None\' instead of raising an exception.\n    """'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|'"xenstore-read"'
op|','
string|'"/local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|','
name|'result'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'result'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenstoreError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'arg_dict'
op|'.'
name|'get'
op|'('
string|'"ignore_missing_path"'
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'_record_exists'
op|'('
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"None"'
newline|'\n'
comment|'# Just try again in case the agent write won the race against'
nl|'\n'
comment|'# the record_exists check. If this fails again, it will likely raise'
nl|'\n'
comment|'# an equally meaningful XenstoreError as the one we just caught'
nl|'\n'
dedent|''
name|'ret'
op|','
name|'result'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'result'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|write_record
name|'def'
name|'write_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Writes to xenstore at the specified path. If there is information\n    already stored in that location, it is overwritten. As in read_record,\n    the dom_id and path must be specified in the arg_dict; additionally,\n    you must specify a \'value\' key, whose value must be a string. Typically,\n    you can json-ify more complex values and store the json output.\n    """'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|'"xenstore-write"'
op|','
nl|'\n'
string|'"/local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
op|','
nl|'\n'
name|'arg_dict'
op|'['
string|'"value"'
op|']'
op|']'
newline|'\n'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'arg_dict'
op|'['
string|'"value"'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|list_records
name|'def'
name|'list_records'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns all the stored data at or below the given path for the\n    given dom_id. The data is returned as a json-ified dict, with the\n    path as the key and the stored value as the value. If the path\n    doesn\'t exist, an empty dict is returned.\n    """'
newline|'\n'
name|'dirpath'
op|'='
string|'"/local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|'"xenstore-ls"'
op|','
name|'dirpath'
op|'.'
name|'rstrip'
op|'('
string|'"/"'
op|')'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|','
name|'recs'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenstoreError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'_record_exists'
op|'('
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
comment|'# Just try again in case the path was created in between'
nl|'\n'
comment|'# the "ls" and the existence check. If this fails again, it will'
nl|'\n'
comment|'# likely raise an equally meaningful XenstoreError'
nl|'\n'
dedent|''
name|'ret'
op|','
name|'recs'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'base_path'
op|'='
name|'arg_dict'
op|'['
string|'"path"'
op|']'
newline|'\n'
name|'paths'
op|'='
name|'_paths_from_ls'
op|'('
name|'recs'
op|')'
newline|'\n'
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'path'
name|'in'
name|'paths'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'base_path'
op|':'
newline|'\n'
indent|'            '
name|'arg_dict'
op|'['
string|'"path"'
op|']'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'base_path'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'arg_dict'
op|'['
string|'"path"'
op|']'
op|'='
name|'path'
newline|'\n'
dedent|''
name|'rec'
op|'='
name|'read_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'rec'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'rec'
newline|'\n'
dedent|''
name|'ret'
op|'['
name|'path'
op|']'
op|'='
name|'val'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|delete_record
name|'def'
name|'delete_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Just like it sounds: it removes the record for the specified\n    VM and the specified path from xenstore.\n    """'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|'"xenstore-rm"'
op|','
string|'"/local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
op|']'
newline|'\n'
name|'ret'
op|','
name|'result'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_paths_from_ls
dedent|''
name|'def'
name|'_paths_from_ls'
op|'('
name|'recs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The xenstore-ls command returns a listing that isn\'t terribly\n    useful. This method cleans that up into a dict with each path\n    as the key, and the associated string as the value.\n    """'
newline|'\n'
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'last_nm'
op|'='
string|'""'
newline|'\n'
name|'level'
op|'='
number|'0'
newline|'\n'
name|'path'
op|'='
op|'['
op|']'
newline|'\n'
name|'ret'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ln'
name|'in'
name|'recs'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nm'
op|','
name|'val'
op|'='
name|'ln'
op|'.'
name|'rstrip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|'" = "'
op|')'
newline|'\n'
name|'barename'
op|'='
name|'nm'
op|'.'
name|'lstrip'
op|'('
op|')'
newline|'\n'
name|'this_level'
op|'='
name|'len'
op|'('
name|'nm'
op|')'
op|'-'
name|'len'
op|'('
name|'barename'
op|')'
newline|'\n'
name|'if'
name|'this_level'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'.'
name|'append'
op|'('
name|'barename'
op|')'
newline|'\n'
name|'level'
op|'='
number|'0'
newline|'\n'
name|'path'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'this_level'
op|'=='
name|'level'
op|':'
newline|'\n'
comment|'# child of same parent'
nl|'\n'
indent|'            '
name|'ret'
op|'.'
name|'append'
op|'('
string|'"%s/%s"'
op|'%'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path'
op|')'
op|','
name|'barename'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'this_level'
op|'>'
name|'level'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'.'
name|'append'
op|'('
name|'last_nm'
op|')'
newline|'\n'
name|'ret'
op|'.'
name|'append'
op|'('
string|'"%s/%s"'
op|'%'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path'
op|')'
op|','
name|'barename'
op|')'
op|')'
newline|'\n'
name|'level'
op|'='
name|'this_level'
newline|'\n'
dedent|''
name|'elif'
name|'this_level'
op|'<'
name|'level'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'path'
op|'['
op|':'
name|'this_level'
op|']'
newline|'\n'
name|'ret'
op|'.'
name|'append'
op|'('
string|'"%s/%s"'
op|'%'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path'
op|')'
op|','
name|'barename'
op|')'
op|')'
newline|'\n'
name|'level'
op|'='
name|'this_level'
newline|'\n'
dedent|''
name|'last_nm'
op|'='
name|'barename'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_run_command
dedent|''
name|'def'
name|'_run_command'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstracts out the basics of issuing system commands. If the command\n    returns anything in stderr, a PluginError is raised with that information.\n    Otherwise, a tuple of (return code, stdout data) is returned.\n    """'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'pipe'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
newline|'\n'
name|'proc'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
name|'stdin'
op|'='
name|'pipe'
op|','
name|'stdout'
op|'='
name|'pipe'
op|','
name|'stderr'
op|'='
name|'pipe'
op|','
nl|'\n'
name|'close_fds'
op|'='
name|'True'
op|')'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'proc'
op|'.'
name|'communicate'
op|'('
op|')'
newline|'\n'
name|'if'
name|'proc'
op|'.'
name|'returncode'
name|'is'
name|'not'
name|'os'
op|'.'
name|'EX_OK'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'XenstoreError'
op|'('
name|'cmd'
op|','
name|'proc'
op|'.'
name|'returncode'
op|','
name|'err'
op|','
name|'out'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'proc'
op|'.'
name|'returncode'
op|','
name|'out'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'XenAPIPlugin'
op|'.'
name|'dispatch'
op|'('
nl|'\n'
op|'{'
string|'"read_record"'
op|':'
name|'read_record'
op|','
nl|'\n'
string|'"write_record"'
op|':'
name|'write_record'
op|','
nl|'\n'
string|'"list_records"'
op|':'
name|'list_records'
op|','
nl|'\n'
string|'"delete_record"'
op|':'
name|'delete_record'
op|'}'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
