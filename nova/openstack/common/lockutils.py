begin_unit
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
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'threading'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'weakref'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
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
op|','
name|'_LE'
op|','
name|'_LI'
newline|'\n'
nl|'\n'
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
DECL|variable|util_opts
name|'util_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'disable_process_locking'"
op|','
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Enables or disables inter-process locks.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'lock_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|'"NOVA_LOCK_PATH"'
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory to use for lock files.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'util_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_defaults
name|'def'
name|'set_defaults'
op|'('
name|'lock_path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'cfg'
op|'.'
name|'set_defaults'
op|'('
name|'util_opts'
op|','
name|'lock_path'
op|'='
name|'lock_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_FileLock
dedent|''
name|'class'
name|'_FileLock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Lock implementation which allows multiple locks, working around\n    issues like bugs.debian.org/cgi-bin/bugreport.cgi?bug=632857 and does\n    not require any cleanup. Since the lock is always held on a file\n    descriptor rather than outside of the process, the lock gets dropped\n    automatically if the process crashes, even if __exit__ is not executed.\n\n    There are no guarantees regarding usage by multiple green threads in a\n    single process here. This lock works only between processes. Exclusive\n    access between local threads should be achieved using the semaphores\n    in the @synchronized decorator.\n\n    Note these locks are released when the descriptor is closed, so it\'s not\n    safe to close the file descriptor while another green thread holds the\n    lock. Just opening and closing the lock file can break synchronisation,\n    so lock files must be accessed only using this abstraction.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'lockfile'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'fname'
op|'='
name|'name'
newline|'\n'
nl|'\n'
DECL|member|acquire
dedent|''
name|'def'
name|'acquire'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'basedir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'self'
op|'.'
name|'fname'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basedir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'basedir'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Created lock path: %s'"
op|')'
op|','
name|'basedir'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'lockfile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'fname'
op|','
string|"'w'"
op|')'
newline|'\n'
nl|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'# Using non-blocking locks since green threads are not'
nl|'\n'
comment|'# patched to deal with blocking locking calls.'
nl|'\n'
comment|'# Also upon reading the MSDN docs for locking(), it seems'
nl|'\n'
comment|'# to have a laughable 10 attempts "blocking" mechanism.'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'trylock'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Got file lock "%s"\''
op|','
name|'self'
op|'.'
name|'fname'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'e'
op|'.'
name|'errno'
name|'in'
op|'('
name|'errno'
op|'.'
name|'EACCES'
op|','
name|'errno'
op|'.'
name|'EAGAIN'
op|')'
op|':'
newline|'\n'
comment|'# external locks synchronise things like iptables'
nl|'\n'
comment|'# updates - give it some time to prevent busy spinning'
nl|'\n'
indent|'                    '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.01'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'threading'
op|'.'
name|'ThreadError'
op|'('
name|'_'
op|'('
string|'"Unable to acquire lock on"'
nl|'\n'
string|'" `%(filename)s` due to"'
nl|'\n'
string|'" %(exception)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'filename'"
op|':'
name|'self'
op|'.'
name|'fname'
op|','
nl|'\n'
string|"'exception'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'acquire'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|release
dedent|''
name|'def'
name|'release'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unlock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lockfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Released file lock "%s"\''
op|','
name|'self'
op|'.'
name|'fname'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Could not release the acquired lock `%s`"'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fname'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'exc_type'
op|','
name|'exc_val'
op|','
name|'exc_tb'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'release'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|exists
dedent|''
name|'def'
name|'exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'fname'
op|')'
newline|'\n'
nl|'\n'
DECL|member|trylock
dedent|''
name|'def'
name|'trylock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unlock
dedent|''
name|'def'
name|'unlock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_WindowsLock
dedent|''
dedent|''
name|'class'
name|'_WindowsLock'
op|'('
name|'_FileLock'
op|')'
op|':'
newline|'\n'
DECL|member|trylock
indent|'    '
name|'def'
name|'trylock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msvcrt'
op|'.'
name|'locking'
op|'('
name|'self'
op|'.'
name|'lockfile'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
name|'msvcrt'
op|'.'
name|'LK_NBLCK'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unlock
dedent|''
name|'def'
name|'unlock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msvcrt'
op|'.'
name|'locking'
op|'('
name|'self'
op|'.'
name|'lockfile'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
name|'msvcrt'
op|'.'
name|'LK_UNLCK'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_FcntlLock
dedent|''
dedent|''
name|'class'
name|'_FcntlLock'
op|'('
name|'_FileLock'
op|')'
op|':'
newline|'\n'
DECL|member|trylock
indent|'    '
name|'def'
name|'trylock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fcntl'
op|'.'
name|'lockf'
op|'('
name|'self'
op|'.'
name|'lockfile'
op|','
name|'fcntl'
op|'.'
name|'LOCK_EX'
op|'|'
name|'fcntl'
op|'.'
name|'LOCK_NB'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unlock
dedent|''
name|'def'
name|'unlock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fcntl'
op|'.'
name|'lockf'
op|'('
name|'self'
op|'.'
name|'lockfile'
op|','
name|'fcntl'
op|'.'
name|'LOCK_UN'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'os'
op|'.'
name|'name'
op|'=='
string|"'nt'"
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'msvcrt'
newline|'\n'
DECL|variable|InterProcessLock
name|'InterProcessLock'
op|'='
name|'_WindowsLock'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'fcntl'
newline|'\n'
DECL|variable|InterProcessLock
name|'InterProcessLock'
op|'='
name|'_FcntlLock'
newline|'\n'
nl|'\n'
DECL|variable|_semaphores
dedent|''
name|'_semaphores'
op|'='
name|'weakref'
op|'.'
name|'WeakValueDictionary'
op|'('
op|')'
newline|'\n'
DECL|variable|_semaphores_lock
name|'_semaphores_lock'
op|'='
name|'threading'
op|'.'
name|'Lock'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_lock_path
name|'def'
name|'_get_lock_path'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|','
name|'lock_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mikal): the lock name cannot contain directory'
nl|'\n'
comment|'# separators'
nl|'\n'
indent|'    '
name|'name'
op|'='
name|'name'
op|'.'
name|'replace'
op|'('
name|'os'
op|'.'
name|'sep'
op|','
string|"'_'"
op|')'
newline|'\n'
name|'if'
name|'lock_file_prefix'
op|':'
newline|'\n'
indent|'        '
name|'sep'
op|'='
string|"''"
name|'if'
name|'lock_file_prefix'
op|'.'
name|'endswith'
op|'('
string|"'-'"
op|')'
name|'else'
string|"'-'"
newline|'\n'
name|'name'
op|'='
string|"'%s%s%s'"
op|'%'
op|'('
name|'lock_file_prefix'
op|','
name|'sep'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'local_lock_path'
op|'='
name|'lock_path'
name|'or'
name|'CONF'
op|'.'
name|'lock_path'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'local_lock_path'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'cfg'
op|'.'
name|'RequiredOptError'
op|'('
string|"'lock_path'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'local_lock_path'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|external_lock
dedent|''
name|'def'
name|'external_lock'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|'='
name|'None'
op|','
name|'lock_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Attempting to grab external lock "%(lock)s"\''
op|','
nl|'\n'
op|'{'
string|"'lock'"
op|':'
name|'name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'lock_file_path'
op|'='
name|'_get_lock_path'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|','
name|'lock_path'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'InterProcessLock'
op|'('
name|'lock_file_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_external_lock_file
dedent|''
name|'def'
name|'remove_external_lock_file'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove an external lock file when it\'s not used anymore\n    This will be helpful when we have a lot of lock files\n    """'
newline|'\n'
name|'with'
name|'internal_lock'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lock_file_path'
op|'='
name|'_get_lock_path'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
name|'lock_file_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Failed to remove file %(file)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'file'"
op|':'
name|'lock_file_path'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|internal_lock
dedent|''
dedent|''
dedent|''
name|'def'
name|'internal_lock'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'with'
name|'_semaphores_lock'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sem'
op|'='
name|'_semaphores'
op|'['
name|'name'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Using existing semaphore "%s"\''
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'sem'
op|'='
name|'threading'
op|'.'
name|'Semaphore'
op|'('
op|')'
newline|'\n'
name|'_semaphores'
op|'['
name|'name'
op|']'
op|'='
name|'sem'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Created new semaphore "%s"\''
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'sem'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|function|lock
name|'def'
name|'lock'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|'='
name|'None'
op|','
name|'external'
op|'='
name|'False'
op|','
name|'lock_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Context based lock\n\n    This function yields a `threading.Semaphore` instance (if we don\'t use\n    eventlet.monkey_patch(), else `semaphore.Semaphore`) unless external is\n    True, in which case, it\'ll yield an InterProcessLock instance.\n\n    :param lock_file_prefix: The lock_file_prefix argument is used to provide\n      lock files on disk with a meaningful prefix.\n\n    :param external: The external keyword argument denotes whether this lock\n      should work across multiple processes. This means that if two different\n      workers both run a method decorated with @synchronized(\'mylock\',\n      external=True), only one of them will execute at a time.\n    """'
newline|'\n'
name|'int_lock'
op|'='
name|'internal_lock'
op|'('
name|'name'
op|')'
newline|'\n'
name|'with'
name|'int_lock'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Acquired semaphore "%(lock)s"\''
op|','
op|'{'
string|"'lock'"
op|':'
name|'name'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'external'
name|'and'
name|'not'
name|'CONF'
op|'.'
name|'disable_process_locking'
op|':'
newline|'\n'
indent|'            '
name|'ext_lock'
op|'='
name|'external_lock'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|','
name|'lock_path'
op|')'
newline|'\n'
name|'with'
name|'ext_lock'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'ext_lock'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'int_lock'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Releasing semaphore "%(lock)s"\''
op|','
op|'{'
string|"'lock'"
op|':'
name|'name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|synchronized
dedent|''
dedent|''
name|'def'
name|'synchronized'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|'='
name|'None'
op|','
name|'external'
op|'='
name|'False'
op|','
name|'lock_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Synchronization decorator.\n\n    Decorating a method like so::\n\n        @synchronized(\'mylock\')\n        def foo(self, *args):\n           ...\n\n    ensures that only one thread will execute the foo method at a time.\n\n    Different methods can share the same lock::\n\n        @synchronized(\'mylock\')\n        def foo(self, *args):\n           ...\n\n        @synchronized(\'mylock\')\n        def bar(self, *args):\n           ...\n\n    This way only one of either foo or bar can be executing at a time.\n    """'
newline|'\n'
nl|'\n'
DECL|function|wrap
name|'def'
name|'wrap'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'f'
op|')'
newline|'\n'
DECL|function|inner
name|'def'
name|'inner'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'lock'
op|'('
name|'name'
op|','
name|'lock_file_prefix'
op|','
name|'external'
op|','
name|'lock_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Got semaphore / lock "%(function)s"\''
op|','
nl|'\n'
op|'{'
string|"'function'"
op|':'
name|'f'
op|'.'
name|'__name__'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Semaphore / lock released "%(function)s"\''
op|','
nl|'\n'
op|'{'
string|"'function'"
op|':'
name|'f'
op|'.'
name|'__name__'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'inner'
newline|'\n'
dedent|''
name|'return'
name|'wrap'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|synchronized_with_prefix
dedent|''
name|'def'
name|'synchronized_with_prefix'
op|'('
name|'lock_file_prefix'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Partial object generator for the synchronization decorator.\n\n    Redefine @synchronized in each project like so::\n\n        (in oslo.utils.py)\n        from nova.openstack.common import lockutils\n\n        synchronized = lockutils.synchronized_with_prefix(\'nova-\')\n\n\n        (in nova/foo.py)\n        from nova import utils\n\n        @utils.synchronized(\'mylock\')\n        def bar(self, *args):\n           ...\n\n    The lock_file_prefix argument is used to provide lock files on disk with a\n    meaningful prefix.\n    """'
newline|'\n'
nl|'\n'
name|'return'
name|'functools'
op|'.'
name|'partial'
op|'('
name|'synchronized'
op|','
name|'lock_file_prefix'
op|'='
name|'lock_file_prefix'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
name|'def'
name|'main'
op|'('
name|'argv'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a dir for locks and pass it to command from arguments\n\n    If you run this:\n    python -m openstack.common.lockutils python setup.py testr <etc>\n\n    a temporary directory will be created for all your locks and passed to all\n    your tests in an environment variable. The temporary dir will be deleted\n    afterwards and the return value will be preserved.\n    """'
newline|'\n'
nl|'\n'
name|'lock_dir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'environ'
op|'['
string|'"NOVA_LOCK_PATH"'
op|']'
op|'='
name|'lock_dir'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ret_val'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'lock_dir'
op|','
name|'ignore_errors'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret_val'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'sys'
op|'.'
name|'exit'
op|'('
name|'main'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
