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
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'select'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExceptionTestCase
name|'class'
name|'ExceptionTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_raise_exc
name|'def'
name|'_raise_exc'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exceptions_raise
dedent|''
name|'def'
name|'test_exceptions_raise'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'name'
name|'in'
name|'dir'
op|'('
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'exc'
op|'='
name|'getattr'
op|'('
name|'exception'
op|','
name|'name'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'exc'
op|','
name|'type'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|','
name|'self'
op|'.'
name|'_raise_exc'
op|','
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectTestCase
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'ProjectTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_all_migrations_have_downgrade
indent|'    '
name|'def'
name|'test_all_migrations_have_downgrade'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'topdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|'+'
string|"'/../../'"
op|')'
newline|'\n'
name|'py_glob'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'topdir'
op|','
string|'"nova"'
op|','
string|'"db"'
op|','
string|'"sqlalchemy"'
op|','
nl|'\n'
string|'"migrate_repo"'
op|','
string|'"versions"'
op|','
string|'"*.py"'
op|')'
newline|'\n'
name|'missing_downgrade'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'path'
name|'in'
name|'glob'
op|'.'
name|'iglob'
op|'('
name|'py_glob'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'has_upgrade'
op|'='
name|'False'
newline|'\n'
name|'has_downgrade'
op|'='
name|'False'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|'"r"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'line'
name|'in'
name|'f'
op|':'
newline|'\n'
indent|'                    '
name|'if'
string|"'def upgrade('"
name|'in'
name|'line'
op|':'
newline|'\n'
indent|'                        '
name|'has_upgrade'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
string|"'def downgrade('"
name|'in'
name|'line'
op|':'
newline|'\n'
indent|'                        '
name|'has_downgrade'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'has_upgrade'
name|'and'
name|'not'
name|'has_downgrade'
op|':'
newline|'\n'
indent|'                    '
name|'fname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'path'
op|')'
newline|'\n'
name|'missing_downgrade'
op|'.'
name|'append'
op|'('
name|'fname'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'helpful_msg'
op|'='
op|'('
name|'_'
op|'('
string|'"The following migrations are missing a downgrade:"'
nl|'\n'
string|'"\\n\\t%s"'
op|')'
op|'%'
string|"'\\n\\t'"
op|'.'
name|'join'
op|'('
name|'sorted'
op|'('
name|'missing_downgrade'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'missing_downgrade'
op|','
name|'helpful_msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LockTestCase
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
DECL|member|test_synchronized_wrapped_function_metadata
indent|'    '
name|'def'
name|'test_synchronized_wrapped_function_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'whatever'"
op|')'
newline|'\n'
DECL|function|foo
name|'def'
name|'foo'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Bar"""'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'foo'
op|'.'
name|'__doc__'
op|','
string|"'Bar'"
op|','
string|'"Wrapped function\'s docstring "'
nl|'\n'
string|'"got lost"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'foo'
op|'.'
name|'__name__'
op|','
string|"'foo'"
op|','
string|'"Wrapped function\'s name "'
nl|'\n'
string|'"got mangled"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_synchronized_internally
dedent|''
name|'def'
name|'test_synchronized_internally'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We can lock across multiple green threads"""'
newline|'\n'
name|'saved_sem_num'
op|'='
name|'len'
op|'('
name|'utils'
op|'.'
name|'_semaphores'
op|')'
newline|'\n'
name|'seen_threads'
op|'='
name|'list'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'testlock2'"
op|','
name|'external'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'seen_threads'
op|'.'
name|'append'
op|'('
name|'id'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'threads'
op|'='
op|'['
op|']'
newline|'\n'
name|'pool'
op|'='
name|'greenpool'
op|'.'
name|'GreenPool'
op|'('
number|'10'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'threads'
op|'.'
name|'append'
op|'('
name|'pool'
op|'.'
name|'spawn'
op|'('
name|'f'
op|','
name|'i'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'thread'
name|'in'
name|'threads'
op|':'
newline|'\n'
indent|'            '
name|'thread'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'seen_threads'
op|')'
op|','
number|'100'
op|')'
newline|'\n'
comment|'# Looking at the seen threads, split it into chunks of 10, and verify'
nl|'\n'
comment|'# that the last 9 match the first in each chunk.'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'j'
name|'in'
name|'range'
op|'('
number|'9'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'seen_threads'
op|'['
name|'i'
op|'*'
number|'10'
op|']'
op|','
nl|'\n'
name|'seen_threads'
op|'['
name|'i'
op|'*'
number|'10'
op|'+'
number|'1'
op|'+'
name|'j'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'saved_sem_num'
op|','
name|'len'
op|'('
name|'utils'
op|'.'
name|'_semaphores'
op|')'
op|','
nl|'\n'
string|'"Semaphore leak detected"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nested_external_works
dedent|''
name|'def'
name|'test_nested_external_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We can nest external syncs"""'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tempdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'lock_path'
op|'='
name|'tempdir'
op|')'
newline|'\n'
name|'sentinel'
op|'='
name|'object'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'testlock1'"
op|','
name|'external'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|function|outer_lock
name|'def'
name|'outer_lock'
op|'('
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'                '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'testlock2'"
op|','
name|'external'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|function|inner_lock
name|'def'
name|'inner_lock'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'sentinel'
newline|'\n'
dedent|''
name|'return'
name|'inner_lock'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sentinel'
op|','
name|'outer_lock'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_synchronized_externally
dedent|''
dedent|''
name|'def'
name|'test_synchronized_externally'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We can lock across multiple processes"""'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tempdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'lock_path'
op|'='
name|'tempdir'
op|')'
newline|'\n'
name|'rpipe1'
op|','
name|'wpipe1'
op|'='
name|'os'
op|'.'
name|'pipe'
op|'('
op|')'
newline|'\n'
name|'rpipe2'
op|','
name|'wpipe2'
op|'='
name|'os'
op|'.'
name|'pipe'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'testlock1'"
op|','
name|'external'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
name|'rpipe'
op|','
name|'wpipe'
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
nl|'\n'
dedent|''
name|'rfds'
op|','
name|'_wfds'
op|','
name|'_efds'
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
indent|'                '
name|'os'
op|'.'
name|'close'
op|'('
name|'wpipe1'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'rpipe2'
op|')'
newline|'\n'
nl|'\n'
name|'f'
op|'('
name|'rpipe1'
op|','
name|'wpipe2'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'close'
op|'('
name|'rpipe1'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'wpipe2'
op|')'
newline|'\n'
nl|'\n'
name|'f'
op|'('
name|'rpipe2'
op|','
name|'wpipe1'
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
dedent|''
endmarker|''
end_unit
