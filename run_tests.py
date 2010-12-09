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
string|'"""\nThis is our basic test running framework based on Twisted\'s Trial.\n\nUsage Examples:\n\n    # to run all the tests\n    python run_tests.py\n\n    # to run a specific test suite imported here\n    python run_tests.py NodeConnectionTestCase\n\n    # to run a specific test imported here\n    python run_tests.py NodeConnectionTestCase.test_reboot\n\n    # to run some test suites elsewhere\n    python run_tests.py nova.tests.node_unittest\n    python run_tests.py nova.tests.node_unittest.NodeConnectionTestCase\n\nDue to our use of multiprocessing it we frequently get some ignorable\n\'Interrupted system call\' exceptions after test completion.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'eventlet'
op|'.'
name|'monkey_patch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'import'
name|'__main__'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'scripts'
name|'import'
name|'trial'
name|'as'
name|'trial_script'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'twistd'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'access_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'auth_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'cloud_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'compute_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'flags_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'misc_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'network_unittest'
name|'import'
op|'*'
newline|'\n'
comment|'#from nova.tests.objectstore_unittest import *'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'quota_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'rpc_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'scheduler_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'service_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'twistd_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'validator_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt_unittest'
name|'import'
op|'*'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'volume_unittest'
name|'import'
op|'*'
newline|'\n'
nl|'\n'
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
name|'DEFINE_bool'
op|'('
string|"'flush_db'"
op|','
name|'True'
op|','
nl|'\n'
string|"'Flush the database before running fake tests'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'tests_stderr'"
op|','
string|"'run_tests.err.log'"
op|','
nl|'\n'
string|"'Path to where to pipe STDERR during test runs.'"
nl|'\n'
string|'\' Default = "run_tests.err.log"\''
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
DECL|variable|OptionsClass
indent|'    '
name|'OptionsClass'
op|'='
name|'twistd'
op|'.'
name|'WrapTwistedOptions'
op|'('
name|'trial_script'
op|'.'
name|'Options'
op|')'
newline|'\n'
DECL|variable|config
name|'config'
op|'='
name|'OptionsClass'
op|'('
op|')'
newline|'\n'
DECL|variable|argv
name|'argv'
op|'='
name|'config'
op|'.'
name|'parseOptions'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|argv
name|'argv'
op|'='
name|'FLAGS'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
nl|'\n'
name|'FLAGS'
op|'.'
name|'verbose'
op|'='
name|'True'
newline|'\n'
nl|'\n'
comment|'# TODO(termie): these should make a call instead of doing work on import'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'fake_flags'
name|'import'
op|'*'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'real_flags'
name|'import'
op|'*'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Establish redirect for STDERR'
nl|'\n'
dedent|''
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
DECL|variable|err
name|'err'
op|'='
name|'open'
op|'('
name|'FLAGS'
op|'.'
name|'tests_stderr'
op|','
string|"'w+'"
op|','
number|'0'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'dup2'
op|'('
name|'err'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'argv'
op|')'
op|'=='
number|'1'
name|'and'
name|'len'
op|'('
name|'config'
op|'['
string|"'tests'"
op|']'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
comment|'# If no tests were specified run the ones imported in this file'
nl|'\n'
comment|'# NOTE(termie): "tests" is not a flag, just some Trial related stuff'
nl|'\n'
indent|'        '
name|'config'
op|'['
string|"'tests'"
op|']'
op|'.'
name|'update'
op|'('
op|'['
string|"'__main__'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'config'
op|'['
string|"'tests'"
op|']'
op|')'
op|':'
newline|'\n'
comment|'# If we specified tests check first whether they are in __main__'
nl|'\n'
indent|'        '
name|'for'
name|'arg'
name|'in'
name|'config'
op|'['
string|"'tests'"
op|']'
op|':'
newline|'\n'
DECL|variable|key
indent|'            '
name|'key'
op|'='
name|'arg'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'__main__'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'config'
op|'['
string|"'tests'"
op|']'
op|'.'
name|'remove'
op|'('
name|'arg'
op|')'
newline|'\n'
name|'config'
op|'['
string|"'tests'"
op|']'
op|'.'
name|'add'
op|'('
string|"'__main__.%s'"
op|'%'
name|'arg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'trial_script'
op|'.'
name|'_initialDebugSetup'
op|'('
name|'config'
op|')'
newline|'\n'
DECL|variable|trialRunner
name|'trialRunner'
op|'='
name|'trial_script'
op|'.'
name|'_makeRunner'
op|'('
name|'config'
op|')'
newline|'\n'
DECL|variable|suite
name|'suite'
op|'='
name|'trial_script'
op|'.'
name|'_getSuite'
op|'('
name|'config'
op|')'
newline|'\n'
name|'if'
name|'config'
op|'['
string|"'until-failure'"
op|']'
op|':'
newline|'\n'
DECL|variable|test_result
indent|'        '
name|'test_result'
op|'='
name|'trialRunner'
op|'.'
name|'runUntilFailure'
op|'('
name|'suite'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|test_result
indent|'        '
name|'test_result'
op|'='
name|'trialRunner'
op|'.'
name|'run'
op|'('
name|'suite'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'config'
op|'.'
name|'tracer'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'settrace'
op|'('
name|'None'
op|')'
newline|'\n'
DECL|variable|results
name|'results'
op|'='
name|'config'
op|'.'
name|'tracer'
op|'.'
name|'results'
op|'('
op|')'
newline|'\n'
name|'results'
op|'.'
name|'write_results'
op|'('
name|'show_missing'
op|'='
number|'1'
op|','
name|'summary'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|coverdir
name|'coverdir'
op|'='
name|'config'
op|'.'
name|'coverdir'
op|')'
newline|'\n'
dedent|''
name|'sys'
op|'.'
name|'exit'
op|'('
name|'not'
name|'test_result'
op|'.'
name|'wasSuccessful'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
