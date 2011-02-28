begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2010 OpenStack LLC'
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
name|'from'
name|'datetime'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'select'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'utils'
name|'import'
name|'parse_mailmap'
op|','
name|'str_dict_replace'
op|','
name|'synchronized'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectTestCase
name|'class'
name|'ProjectTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_authors_up_to_date
indent|'    '
name|'def'
name|'test_authors_up_to_date'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|"'.bzr'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'contributors'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mailmap'
op|'='
name|'parse_mailmap'
op|'('
string|"'.mailmap'"
op|')'
newline|'\n'
nl|'\n'
name|'import'
name|'bzrlib'
op|'.'
name|'workingtree'
newline|'\n'
name|'tree'
op|'='
name|'bzrlib'
op|'.'
name|'workingtree'
op|'.'
name|'WorkingTree'
op|'.'
name|'open'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'tree'
op|'.'
name|'lock_read'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'parents'
op|'='
name|'tree'
op|'.'
name|'get_parent_ids'
op|'('
op|')'
newline|'\n'
name|'g'
op|'='
name|'tree'
op|'.'
name|'branch'
op|'.'
name|'repository'
op|'.'
name|'get_graph'
op|'('
op|')'
newline|'\n'
name|'for'
name|'p'
name|'in'
name|'parents'
op|'['
number|'1'
op|':'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'rev_ids'
op|'='
op|'['
name|'r'
name|'for'
name|'r'
op|','
name|'_'
name|'in'
name|'g'
op|'.'
name|'iter_ancestry'
op|'('
name|'parents'
op|')'
nl|'\n'
name|'if'
name|'r'
op|'!='
string|'"null:"'
op|']'
newline|'\n'
name|'revs'
op|'='
name|'tree'
op|'.'
name|'branch'
op|'.'
name|'repository'
op|'.'
name|'get_revisions'
op|'('
name|'rev_ids'
op|')'
newline|'\n'
name|'for'
name|'r'
name|'in'
name|'revs'
op|':'
newline|'\n'
indent|'                        '
name|'for'
name|'author'
name|'in'
name|'r'
op|'.'
name|'get_apparent_authors'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                            '
name|'email'
op|'='
name|'author'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'contributors'
op|'.'
name|'add'
op|'('
name|'str_dict_replace'
op|'('
name|'email'
op|','
name|'mailmap'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'authors_file'
op|'='
name|'open'
op|'('
string|"'Authors'"
op|','
string|"'r'"
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'missing'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'contributor'
name|'in'
name|'contributors'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'contributor'
op|'=='
string|"'nova-core'"
op|':'
newline|'\n'
indent|'                        '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'contributor'
name|'in'
name|'authors_file'
op|':'
newline|'\n'
indent|'                        '
name|'missing'
op|'.'
name|'add'
op|'('
name|'contributor'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'missing'
op|')'
op|'=='
number|'0'
op|','
nl|'\n'
string|"'%r not listed in Authors'"
op|'%'
name|'missing'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'                '
name|'tree'
op|'.'
name|'unlock'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LockTestCase
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'LockTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_synchronized
indent|'    '
name|'def'
name|'test_synchronized'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpipe'
op|','
name|'wpipe'
op|'='
name|'os'
op|'.'
name|'pipe'
op|'('
op|')'
newline|'\n'
name|'pid'
op|'='
name|'os'
op|'.'
name|'fork'
op|'('
op|')'
newline|'\n'
name|'if'
name|'pid'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'close'
op|'('
name|'wpipe'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'synchronized'
op|'('
string|"'testlock'"
op|')'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'rfds'
op|','
name|'_'
op|','
name|'__'
op|'='
name|'select'
op|'.'
name|'select'
op|'('
op|'['
name|'rpipe'
op|']'
op|','
op|'['
op|']'
op|','
op|'['
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'rfds'
op|')'
op|','
number|'0'
op|','
string|'"The other process, which was"'
nl|'\n'
string|'" supposed to be locked, "'
nl|'\n'
string|'"wrote on its end of the "'
nl|'\n'
string|'"pipe"'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'rpipe'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'f'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'close'
op|'('
name|'rpipe'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'synchronized'
op|'('
string|"'testlock'"
op|')'
newline|'\n'
DECL|function|g
name|'def'
name|'g'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'write'
op|'('
name|'wpipe'
op|','
string|'"foo"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'e'
op|'.'
name|'errno'
op|','
name|'errno'
op|'.'
name|'EPIPE'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'g'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'_exit'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
