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
name|'errno'
newline|'\n'
name|'import'
name|'os'
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
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
