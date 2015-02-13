begin_unit
comment|'# Copyright 2012 Red Hat, Inc.'
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
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'threading'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'loopingcall'
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
DECL|function|_thread_done
name|'def'
name|'_thread_done'
op|'('
name|'gt'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Callback function to be passed to GreenThread.link() when we spawn()\n    Calls the :class:`ThreadGroup` to notify if.\n\n    """'
newline|'\n'
name|'kwargs'
op|'['
string|"'group'"
op|']'
op|'.'
name|'thread_done'
op|'('
name|'kwargs'
op|'['
string|"'thread'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Thread
dedent|''
name|'class'
name|'Thread'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around a greenthread, that holds a reference to the\n    :class:`ThreadGroup`. The Thread will notify the :class:`ThreadGroup` when\n    it has done so it can be removed from the threads list.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'thread'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'thread'
op|'='
name|'thread'
newline|'\n'
name|'self'
op|'.'
name|'thread'
op|'.'
name|'link'
op|'('
name|'_thread_done'
op|','
name|'group'
op|'='
name|'group'
op|','
name|'thread'
op|'='
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'thread'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'thread'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|link
dedent|''
name|'def'
name|'link'
op|'('
name|'self'
op|','
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'thread'
op|'.'
name|'link'
op|'('
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ThreadGroup
dedent|''
dedent|''
name|'class'
name|'ThreadGroup'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The point of the ThreadGroup class is to:\n\n    * keep track of timers and greenthreads (making it easier to stop them\n      when need be).\n    * provide an easy API to add timers.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'thread_pool_size'
op|'='
number|'10'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pool'
op|'='
name|'greenpool'
op|'.'
name|'GreenPool'
op|'('
name|'thread_pool_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'threads'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'timers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|add_dynamic_timer
dedent|''
name|'def'
name|'add_dynamic_timer'
op|'('
name|'self'
op|','
name|'callback'
op|','
name|'initial_delay'
op|'='
name|'None'
op|','
nl|'\n'
name|'periodic_interval_max'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timer'
op|'='
name|'loopingcall'
op|'.'
name|'DynamicLoopingCall'
op|'('
name|'callback'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'initial_delay'
op|'='
name|'initial_delay'
op|','
nl|'\n'
name|'periodic_interval_max'
op|'='
name|'periodic_interval_max'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'timers'
op|'.'
name|'append'
op|'('
name|'timer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_timer
dedent|''
name|'def'
name|'add_timer'
op|'('
name|'self'
op|','
name|'interval'
op|','
name|'callback'
op|','
name|'initial_delay'
op|'='
name|'None'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pulse'
op|'='
name|'loopingcall'
op|'.'
name|'FixedIntervalLoopingCall'
op|'('
name|'callback'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'pulse'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
name|'interval'
op|','
nl|'\n'
name|'initial_delay'
op|'='
name|'initial_delay'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'timers'
op|'.'
name|'append'
op|'('
name|'pulse'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_thread
dedent|''
name|'def'
name|'add_thread'
op|'('
name|'self'
op|','
name|'callback'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'gt'
op|'='
name|'self'
op|'.'
name|'pool'
op|'.'
name|'spawn'
op|'('
name|'callback'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'th'
op|'='
name|'Thread'
op|'('
name|'gt'
op|','
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'threads'
op|'.'
name|'append'
op|'('
name|'th'
op|')'
newline|'\n'
name|'return'
name|'th'
newline|'\n'
nl|'\n'
DECL|member|thread_done
dedent|''
name|'def'
name|'thread_done'
op|'('
name|'self'
op|','
name|'thread'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'threads'
op|'.'
name|'remove'
op|'('
name|'thread'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stop_threads
dedent|''
name|'def'
name|'_stop_threads'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current'
op|'='
name|'threading'
op|'.'
name|'current_thread'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# Iterate over a copy of self.threads so thread_done doesn't"
nl|'\n'
comment|"# modify the list while we're iterating"
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'threads'
op|'['
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
name|'is'
name|'current'
op|':'
newline|'\n'
comment|"# don't kill the current thread."
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'x'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'eventlet'
op|'.'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_timers
dedent|''
dedent|''
dedent|''
name|'def'
name|'stop_timers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'timers'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'x'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'timers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|','
name|'graceful'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""stop function has the option of graceful=True/False.\n\n        * In case of graceful=True, wait for all threads to be finished.\n          Never kill threads.\n        * In case of graceful=False, kill threads immediately.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'stop_timers'
op|'('
op|')'
newline|'\n'
name|'if'
name|'graceful'
op|':'
newline|'\n'
comment|'# In case of graceful=True, wait for all threads to be'
nl|'\n'
comment|'# finished, never kill threads'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# In case of graceful=False(Default), kill threads'
nl|'\n'
comment|'# immediately'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_stop_threads'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'timers'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'x'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'eventlet'
op|'.'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'current'
op|'='
name|'threading'
op|'.'
name|'current_thread'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# Iterate over a copy of self.threads so thread_done doesn't"
nl|'\n'
comment|"# modify the list while we're iterating"
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'threads'
op|'['
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'x'
name|'is'
name|'current'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'x'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'eventlet'
op|'.'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
