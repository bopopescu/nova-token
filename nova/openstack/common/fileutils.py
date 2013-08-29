begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation.'
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
name|'contextlib'
newline|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
comment|'# noqa'
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
DECL|variable|_FILE_CACHE
name|'_FILE_CACHE'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_tree
name|'def'
name|'ensure_tree'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a directory (and any ancestor directories required)\n\n    :param path: Directory to create\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'exc'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'EEXIST'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|read_cached_file
dedent|''
dedent|''
dedent|''
name|'def'
name|'read_cached_file'
op|'('
name|'filename'
op|','
name|'force_reload'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Read from a file if it has been modified.\n\n    :param force_reload: Whether to reload the file.\n    :returns: A tuple with a boolean specifying if the data is fresh\n              or not.\n    """'
newline|'\n'
name|'global'
name|'_FILE_CACHE'
newline|'\n'
nl|'\n'
name|'if'
name|'force_reload'
name|'and'
name|'filename'
name|'in'
name|'_FILE_CACHE'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'_FILE_CACHE'
op|'['
name|'filename'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'reloaded'
op|'='
name|'False'
newline|'\n'
name|'mtime'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'getmtime'
op|'('
name|'filename'
op|')'
newline|'\n'
name|'cache_info'
op|'='
name|'_FILE_CACHE'
op|'.'
name|'setdefault'
op|'('
name|'filename'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'cache_info'
name|'or'
name|'mtime'
op|'>'
name|'cache_info'
op|'.'
name|'get'
op|'('
string|"'mtime'"
op|','
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reloading cached file %s"'
op|')'
op|'%'
name|'filename'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'filename'
op|')'
name|'as'
name|'fap'
op|':'
newline|'\n'
indent|'            '
name|'cache_info'
op|'['
string|"'data'"
op|']'
op|'='
name|'fap'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'cache_info'
op|'['
string|"'mtime'"
op|']'
op|'='
name|'mtime'
newline|'\n'
name|'reloaded'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'return'
op|'('
name|'reloaded'
op|','
name|'cache_info'
op|'['
string|"'data'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_if_exists
dedent|''
name|'def'
name|'delete_if_exists'
op|'('
name|'path'
op|','
name|'remove'
op|'='
name|'os'
op|'.'
name|'unlink'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete a file, but ignore file not found error.\n\n    :param path: File to delete\n    :param remove: Optional function to remove passed path\n    """'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'remove'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'!='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|function|remove_path_on_error
name|'def'
name|'remove_path_on_error'
op|'('
name|'path'
op|','
name|'remove'
op|'='
name|'delete_if_exists'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Protect code that wants to operate on PATH atomically.\n    Any exception will cause PATH to be removed.\n\n    :param path: File to work with\n    :param remove: Optional function to remove passed path\n    """'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'yield'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'remove'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_open
dedent|''
dedent|''
dedent|''
name|'def'
name|'file_open'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Open file\n\n    see built-in file() documentation for more details\n\n    Note: The reason this is kept in a separate module is to easily\n    be able to provide a stub module that doesn\'t alter system\n    state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'file'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
