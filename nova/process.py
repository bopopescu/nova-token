begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nProcess pool, still buggy right now.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'multiprocessing'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'error'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'process'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'threads'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'failure'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'process_pool_size'"
op|','
number|'4'
op|','
nl|'\n'
string|"'Number of processes to use in the process pool'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(termie): this is copied from twisted.internet.utils but since'
nl|'\n'
comment|"#               they don't export it I've copied and modified"
nl|'\n'
DECL|class|UnexpectedErrorOutput
name|'class'
name|'UnexpectedErrorOutput'
op|'('
name|'IOError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Standard error data was received where it was not expected.  This is a\n    subclass of L{IOError} to preserve backward compatibility with the previous\n    error behavior of L{getProcessOutput}.\n\n    @ivar processEnded: A L{Deferred} which will fire when the process which\n        produced the data on stderr has ended (exited and all file descriptors\n        closed).\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stdout'
op|'='
name|'None'
op|','
name|'stderr'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'IOError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
string|'"got stdout: %r\\nstderr: %r"'
op|'%'
op|'('
name|'stdout'
op|','
name|'stderr'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(termie): this too'
nl|'\n'
DECL|class|_BackRelay
dedent|''
dedent|''
name|'class'
name|'_BackRelay'
op|'('
name|'protocol'
op|'.'
name|'ProcessProtocol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Trivial protocol for communicating with a process and turning its output\n    into the result of a L{Deferred}.\n\n    @ivar deferred: A L{Deferred} which will be called back with all of stdout\n        and, if C{errortoo} is true, all of stderr as well (mixed together in\n        one string).  If C{errortoo} is false and any bytes are received over\n        stderr, this will fire with an L{_UnexpectedErrorOutput} instance and\n        the attribute will be set to C{None}.\n\n    @ivar onProcessEnded: If C{errortoo} is false and bytes are received over\n        stderr, this attribute will refer to a L{Deferred} which will be called\n        back when the process ends.  This C{Deferred} is also associated with\n        the L{_UnexpectedErrorOutput} which C{deferred} fires with earlier in\n        this case so that users can determine when the process has actually\n        ended, in addition to knowing when bytes have been received via stderr.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'deferred'
op|','
name|'errortoo'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'deferred'
op|'='
name|'deferred'
newline|'\n'
name|'self'
op|'.'
name|'s'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'if'
name|'errortoo'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'errReceived'
op|'='
name|'self'
op|'.'
name|'errReceivedIsGood'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'errReceived'
op|'='
name|'self'
op|'.'
name|'errReceivedIsBad'
newline|'\n'
nl|'\n'
DECL|member|errReceivedIsBad
dedent|''
dedent|''
name|'def'
name|'errReceivedIsBad'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'deferred'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'onProcessEnded'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'err'
op|'='
name|'UnexpectedErrorOutput'
op|'('
name|'text'
op|','
name|'self'
op|'.'
name|'onProcessEnded'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deferred'
op|'.'
name|'errback'
op|'('
name|'failure'
op|'.'
name|'Failure'
op|'('
name|'err'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deferred'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|errReceivedIsGood
dedent|''
dedent|''
name|'def'
name|'errReceivedIsGood'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'s'
op|'.'
name|'write'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|member|outReceived
dedent|''
name|'def'
name|'outReceived'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'s'
op|'.'
name|'write'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|member|processEnded
dedent|''
name|'def'
name|'processEnded'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'deferred'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'deferred'
op|'.'
name|'callback'
op|'('
name|'self'
op|'.'
name|'s'
op|'.'
name|'getvalue'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'onProcessEnded'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'onProcessEnded'
op|'.'
name|'errback'
op|'('
name|'reason'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BackRelayWithInput
dedent|''
dedent|''
dedent|''
name|'class'
name|'BackRelayWithInput'
op|'('
name|'_BackRelay'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'deferred'
op|','
name|'startedDeferred'
op|'='
name|'None'
op|','
name|'error_ok'
op|'='
number|'0'
op|','
nl|'\n'
name|'input'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|"# Twisted doesn't use new-style classes in most places :("
nl|'\n'
indent|'        '
name|'_BackRelay'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'deferred'
op|','
name|'errortoo'
op|'='
name|'error_ok'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'error_ok'
op|'='
name|'error_ok'
newline|'\n'
name|'self'
op|'.'
name|'input'
op|'='
name|'input'
newline|'\n'
name|'self'
op|'.'
name|'stderr'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'startedDeferred'
op|'='
name|'startedDeferred'
newline|'\n'
nl|'\n'
DECL|member|errReceivedIsBad
dedent|''
name|'def'
name|'errReceivedIsBad'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|errReceivedIsGood
dedent|''
name|'def'
name|'errReceivedIsGood'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|member|connectionMade
dedent|''
name|'def'
name|'connectionMade'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'startedDeferred'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'startedDeferred'
op|'.'
name|'callback'
op|'('
name|'self'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'input'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'input'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'transport'
op|'.'
name|'closeStdin'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|processEnded
dedent|''
name|'def'
name|'processEnded'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'deferred'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'stdout'
op|','
name|'stderr'
op|'='
name|'self'
op|'.'
name|'s'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'stderr'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(termie): current behavior means if error_ok is True'
nl|'\n'
comment|"#               we won't throw an error even if the process"
nl|'\n'
comment|"#               exited with a non-0 status, so you can't be"
nl|'\n'
comment|'#               okay with stderr output and not with bad exit'
nl|'\n'
comment|'#               codes.'
nl|'\n'
indent|'                '
name|'if'
name|'not'
name|'self'
op|'.'
name|'error_ok'
op|':'
newline|'\n'
indent|'                    '
name|'reason'
op|'.'
name|'trap'
op|'('
name|'error'
op|'.'
name|'ProcessDone'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'deferred'
op|'.'
name|'callback'
op|'('
op|'('
name|'stdout'
op|','
name|'stderr'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'deferred'
op|'.'
name|'errback'
op|'('
name|'UnexpectedErrorOutput'
op|'('
name|'stdout'
op|','
name|'stderr'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|getProcessOutput
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'getProcessOutput'
op|'('
name|'executable'
op|','
name|'args'
op|'='
name|'None'
op|','
name|'env'
op|'='
name|'None'
op|','
name|'path'
op|'='
name|'None'
op|','
name|'reactor'
op|'='
name|'None'
op|','
nl|'\n'
name|'error_ok'
op|'='
number|'0'
op|','
name|'input'
op|'='
name|'None'
op|','
name|'startedDeferred'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'reactor'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
dedent|''
name|'args'
op|'='
name|'args'
name|'and'
name|'args'
name|'or'
op|'('
op|')'
newline|'\n'
name|'env'
op|'='
name|'env'
name|'and'
name|'env'
name|'and'
op|'{'
op|'}'
newline|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'p'
op|'='
name|'BackRelayWithInput'
op|'('
nl|'\n'
name|'d'
op|','
name|'startedDeferred'
op|'='
name|'startedDeferred'
op|','
name|'error_ok'
op|'='
name|'error_ok'
op|','
name|'input'
op|'='
name|'input'
op|')'
newline|'\n'
comment|'# NOTE(vish): commands come in as unicode, but self.executes needs'
nl|'\n'
comment|'#             strings or process.spawn raises a deprecation warning'
nl|'\n'
name|'executable'
op|'='
name|'str'
op|'('
name|'executable'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'args'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
name|'str'
op|'('
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'args'
op|']'
newline|'\n'
dedent|''
name|'reactor'
op|'.'
name|'spawnProcess'
op|'('
name|'p'
op|','
name|'executable'
op|','
op|'('
name|'executable'
op|','
op|')'
op|'+'
name|'tuple'
op|'('
name|'args'
op|')'
op|','
name|'env'
op|','
name|'path'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessPool
dedent|''
name|'class'
name|'ProcessPool'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" A simple process pool implementation using Twisted\'s Process bits.\n\n    This is pretty basic right now, but hopefully the API will be the correct\n    one so that it can be optimized later.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'size'
op|'='
name|'size'
name|'and'
name|'size'
name|'or'
name|'FLAGS'
op|'.'
name|'process_pool_size'
newline|'\n'
name|'self'
op|'.'
name|'_pool'
op|'='
name|'defer'
op|'.'
name|'DeferredSemaphore'
op|'('
name|'self'
op|'.'
name|'size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|simple_execute
dedent|''
name|'def'
name|'simple_execute'
op|'('
name|'self'
op|','
name|'cmd'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Weak emulation of the old utils.execute() function.\n\n        This only exists as a way to quickly move old execute methods to\n        this new style of code.\n\n        NOTE(termie): This will break on args with spaces in them.\n        """'
newline|'\n'
name|'parsed'
op|'='
name|'cmd'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
newline|'\n'
name|'executable'
op|','
name|'args'
op|'='
name|'parsed'
op|'['
number|'0'
op|']'
op|','
name|'parsed'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'execute'
op|'('
name|'executable'
op|','
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
nl|'\n'
DECL|member|execute
dedent|''
name|'def'
name|'execute'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
name|'self'
op|'.'
name|'_pool'
op|'.'
name|'acquire'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_associateProcess
name|'def'
name|'_associateProcess'
op|'('
name|'proto'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'.'
name|'process'
op|'='
name|'proto'
op|'.'
name|'transport'
newline|'\n'
name|'return'
name|'proto'
op|'.'
name|'transport'
newline|'\n'
nl|'\n'
dedent|''
name|'started'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'started'
op|'.'
name|'addCallback'
op|'('
name|'_associateProcess'
op|')'
newline|'\n'
name|'kw'
op|'.'
name|'setdefault'
op|'('
string|"'startedDeferred'"
op|','
name|'started'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'.'
name|'process'
op|'='
name|'None'
newline|'\n'
name|'d'
op|'.'
name|'started'
op|'='
name|'started'
newline|'\n'
nl|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'_'
op|':'
name|'getProcessOutput'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addBoth'
op|'('
name|'self'
op|'.'
name|'_release'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|_release
dedent|''
name|'def'
name|'_release'
op|'('
name|'self'
op|','
name|'rv'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_pool'
op|'.'
name|'release'
op|'('
op|')'
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SharedPool
dedent|''
dedent|''
name|'class'
name|'SharedPool'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|_instance
indent|'    '
name|'_instance'
op|'='
name|'None'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'SharedPool'
op|'.'
name|'_instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_instance'
op|'='
name|'ProcessPool'
op|'('
op|')'
newline|'\n'
DECL|member|__getattr__
dedent|''
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_instance'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|simple_execute
dedent|''
dedent|''
name|'def'
name|'simple_execute'
op|'('
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'SharedPool'
op|'('
op|')'
op|'.'
name|'simple_execute'
op|'('
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
