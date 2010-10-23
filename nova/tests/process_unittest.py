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
name|'import'
name|'logging'
newline|'\n'
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
name|'reactor'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'etree'
name|'import'
name|'ElementTree'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'process'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessTestCase
name|'class'
name|'ProcessTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ProcessTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_execute_stdout
dedent|''
name|'def'
name|'test_execute_stdout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool'
op|'='
name|'process'
op|'.'
name|'ProcessPool'
op|'('
number|'2'
op|')'
newline|'\n'
name|'d'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'echo test'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_check
name|'def'
name|'_check'
op|'('
name|'rv'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
number|'0'
op|']'
op|','
string|"'test\\n'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
number|'1'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'_check'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addErrback'
op|'('
name|'self'
op|'.'
name|'fail'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|test_execute_stderr
dedent|''
name|'def'
name|'test_execute_stderr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool'
op|'='
name|'process'
op|'.'
name|'ProcessPool'
op|'('
number|'2'
op|')'
newline|'\n'
name|'d'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'cat BAD_FILE'"
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_check
name|'def'
name|'_check'
op|'('
name|'rv'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
number|'0'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
string|"'No such file'"
name|'in'
name|'rv'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'_check'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addErrback'
op|'('
name|'self'
op|'.'
name|'fail'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|test_execute_unexpected_stderr
dedent|''
name|'def'
name|'test_execute_unexpected_stderr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool'
op|'='
name|'process'
op|'.'
name|'ProcessPool'
op|'('
number|'2'
op|')'
newline|'\n'
name|'d'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'cat BAD_FILE'"
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'x'
op|':'
name|'self'
op|'.'
name|'fail'
op|'('
string|"'should have raised an error'"
op|')'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addErrback'
op|'('
name|'lambda'
name|'failure'
op|':'
name|'failure'
op|'.'
name|'trap'
op|'('
name|'IOError'
op|')'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|test_max_processes
dedent|''
name|'def'
name|'test_max_processes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool'
op|'='
name|'process'
op|'.'
name|'ProcessPool'
op|'('
number|'2'
op|')'
newline|'\n'
name|'d1'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 0.01'"
op|')'
newline|'\n'
name|'d2'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 0.01'"
op|')'
newline|'\n'
name|'d3'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 0.005'"
op|')'
newline|'\n'
name|'d4'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 0.005'"
op|')'
newline|'\n'
nl|'\n'
name|'called'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|_called
name|'def'
name|'_called'
op|'('
name|'rv'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'called'
op|'.'
name|'append'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'d1'
op|'.'
name|'addCallback'
op|'('
name|'_called'
op|','
string|"'d1'"
op|')'
newline|'\n'
name|'d2'
op|'.'
name|'addCallback'
op|'('
name|'_called'
op|','
string|"'d2'"
op|')'
newline|'\n'
name|'d3'
op|'.'
name|'addCallback'
op|'('
name|'_called'
op|','
string|"'d3'"
op|')'
newline|'\n'
name|'d4'
op|'.'
name|'addCallback'
op|'('
name|'_called'
op|','
string|"'d4'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure that d3 and d4 had to wait on the other two and were called'
nl|'\n'
comment|'# in order'
nl|'\n'
comment|'# NOTE(termie): there may be a race condition in this test if for some'
nl|'\n'
comment|'#               reason one of the sleeps takes longer to complete'
nl|'\n'
comment|'#               than it should'
nl|'\n'
name|'d4'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'x'
op|':'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'called'
op|'['
number|'2'
op|']'
op|','
string|"'d3'"
op|')'
op|')'
newline|'\n'
name|'d4'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'x'
op|':'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'called'
op|'['
number|'3'
op|']'
op|','
string|"'d4'"
op|')'
op|')'
newline|'\n'
name|'d4'
op|'.'
name|'addErrback'
op|'('
name|'self'
op|'.'
name|'fail'
op|')'
newline|'\n'
name|'return'
name|'d4'
newline|'\n'
nl|'\n'
DECL|member|test_kill_long_process
dedent|''
name|'def'
name|'test_kill_long_process'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool'
op|'='
name|'process'
op|'.'
name|'ProcessPool'
op|'('
number|'2'
op|')'
newline|'\n'
nl|'\n'
name|'d1'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 1'"
op|')'
newline|'\n'
name|'d2'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 0.005'"
op|')'
newline|'\n'
nl|'\n'
name|'timeout'
op|'='
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'0.1'
op|','
name|'self'
op|'.'
name|'fail'
op|','
string|"'should have been killed'"
op|')'
newline|'\n'
nl|'\n'
comment|'# kill d1 and wait on it to end then cancel the timeout'
nl|'\n'
name|'d2'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'_'
op|':'
name|'d1'
op|'.'
name|'process'
op|'.'
name|'signalProcess'
op|'('
string|"'KILL'"
op|')'
op|')'
newline|'\n'
name|'d2'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'_'
op|':'
name|'d1'
op|')'
newline|'\n'
name|'d2'
op|'.'
name|'addBoth'
op|'('
name|'lambda'
name|'_'
op|':'
name|'timeout'
op|'.'
name|'active'
op|'('
op|')'
name|'and'
name|'timeout'
op|'.'
name|'cancel'
op|'('
op|')'
op|')'
newline|'\n'
name|'d2'
op|'.'
name|'addErrback'
op|'('
name|'self'
op|'.'
name|'fail'
op|')'
newline|'\n'
name|'return'
name|'d2'
newline|'\n'
nl|'\n'
DECL|member|test_process_exit_is_contained
dedent|''
name|'def'
name|'test_process_exit_is_contained'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool'
op|'='
name|'process'
op|'.'
name|'ProcessPool'
op|'('
number|'2'
op|')'
newline|'\n'
nl|'\n'
name|'d1'
op|'='
name|'pool'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 1'"
op|')'
newline|'\n'
name|'d1'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'x'
op|':'
name|'self'
op|'.'
name|'fail'
op|'('
string|"'should have errbacked'"
op|')'
op|')'
newline|'\n'
name|'d1'
op|'.'
name|'addErrback'
op|'('
name|'lambda'
name|'fail'
op|':'
name|'fail'
op|'.'
name|'trap'
op|'('
name|'IOError'
op|')'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'0.05'
op|','
name|'d1'
op|'.'
name|'process'
op|'.'
name|'signalProcess'
op|','
string|"'KILL'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'d1'
newline|'\n'
nl|'\n'
DECL|member|test_shared_pool_is_singleton
dedent|''
name|'def'
name|'test_shared_pool_is_singleton'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool1'
op|'='
name|'process'
op|'.'
name|'SharedPool'
op|'('
op|')'
newline|'\n'
name|'pool2'
op|'='
name|'process'
op|'.'
name|'SharedPool'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'id'
op|'('
name|'pool1'
op|'.'
name|'_instance'
op|')'
op|','
name|'id'
op|'('
name|'pool2'
op|'.'
name|'_instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shared_pool_works_as_singleton
dedent|''
name|'def'
name|'test_shared_pool_works_as_singleton'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d1'
op|'='
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 1'"
op|')'
newline|'\n'
name|'d2'
op|'='
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'sleep 0.005'"
op|')'
newline|'\n'
comment|'# lp609749: would have failed with'
nl|'\n'
comment|'# exceptions.AssertionError: Someone released me too many times:'
nl|'\n'
comment|'# too many tokens!'
nl|'\n'
name|'return'
name|'d1'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
