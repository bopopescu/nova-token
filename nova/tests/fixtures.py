begin_unit
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
string|'"""Fixtures for Nova tests."""'
newline|'\n'
name|'from'
name|'__future__'
name|'import'
name|'absolute_import'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
name|'as'
name|'std_logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
name|'import'
name|'warnings'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_messaging'
name|'import'
name|'conffixture'
name|'as'
name|'messaging_conffixture'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'migration'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'session'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api'
name|'import'
name|'client'
newline|'\n'
nl|'\n'
DECL|variable|_TRUE_VALUES
name|'_TRUE_VALUES'
op|'='
op|'('
string|"'True'"
op|','
string|"'true'"
op|','
string|"'1'"
op|','
string|"'yes'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|DB_SCHEMA
name|'DB_SCHEMA'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceFixture
name|'class'
name|'ServiceFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Run a service as a test fixture."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'host'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
name|'name'
newline|'\n'
name|'host'
op|'='
name|'host'
name|'or'
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'host'"
op|','
name|'host'
op|')'
newline|'\n'
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'binary'"
op|','
string|"'nova-%s'"
op|'%'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'kwargs'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ServiceFixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
op|'**'
name|'self'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'kill'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NullHandler
dedent|''
dedent|''
name|'class'
name|'NullHandler'
op|'('
name|'std_logging'
op|'.'
name|'Handler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""custom default NullHandler to attempt to format the record.\n\n    Used in conjunction with\n    log_fixture.get_logging_handle_error_fixture to detect formatting errors in\n    debug level logs without saving the logs.\n    """'
newline|'\n'
DECL|member|handle
name|'def'
name|'handle'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'format'
op|'('
name|'record'
op|')'
newline|'\n'
nl|'\n'
DECL|member|emit
dedent|''
name|'def'
name|'emit'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|createLock
dedent|''
name|'def'
name|'createLock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'lock'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StandardLogging
dedent|''
dedent|''
name|'class'
name|'StandardLogging'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Setup Logging redirection for tests.\n\n    There are a number of things we want to handle with logging in tests:\n\n    * Redirect the logging to somewhere that we can test or dump it later.\n\n    * Ensure that as many DEBUG messages as possible are actually\n       executed, to ensure they are actually syntactically valid (they\n       often have not been).\n\n    * Ensure that we create useful output for tests that doesn\'t\n      overwhelm the testing system (which means we can\'t capture the\n      100 MB of debug logging on every run).\n\n    To do this we create a logger fixture at the root level, which\n    defaults to INFO and create a Null Logger at DEBUG which lets\n    us execute log messages at DEBUG but not keep the output.\n\n    To support local debugging OS_DEBUG=True can be set in the\n    environment, which will print out the full debug logging.\n\n    There are also a set of overrides for particularly verbose\n    modules to be even less than INFO.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'StandardLogging'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# set root logger to debug'
nl|'\n'
name|'root'
op|'='
name|'std_logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'root'
op|'.'
name|'setLevel'
op|'('
name|'std_logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
comment|'# supports collecting debug level for local runs'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_DEBUG'"
op|')'
name|'in'
name|'_TRUE_VALUES'
op|':'
newline|'\n'
indent|'            '
name|'level'
op|'='
name|'std_logging'
op|'.'
name|'DEBUG'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'level'
op|'='
name|'std_logging'
op|'.'
name|'INFO'
newline|'\n'
nl|'\n'
comment|'# Collect logs'
nl|'\n'
dedent|''
name|'fs'
op|'='
string|"'%(asctime)s %(levelname)s [%(name)s] %(message)s'"
newline|'\n'
name|'self'
op|'.'
name|'logger'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'fixtures'
op|'.'
name|'FakeLogger'
op|'('
name|'format'
op|'='
name|'fs'
op|','
name|'level'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
comment|"# TODO(sdague): why can't we send level through the fake"
nl|'\n'
comment|"# logger? Tests prove that it breaks, but it's worth getting"
nl|'\n'
comment|'# to the bottom of.'
nl|'\n'
name|'root'
op|'.'
name|'handlers'
op|'['
number|'0'
op|']'
op|'.'
name|'setLevel'
op|'('
name|'level'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'level'
op|'>'
name|'std_logging'
op|'.'
name|'DEBUG'
op|':'
newline|'\n'
comment|"# Just attempt to format debug level logs, but don't save them"
nl|'\n'
indent|'            '
name|'handler'
op|'='
name|'NullHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'LogHandler'
op|'('
name|'handler'
op|','
name|'nuke_handlers'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
name|'handler'
op|'.'
name|'setLevel'
op|'('
name|'std_logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
comment|"# Don't log every single DB migration step"
nl|'\n'
name|'std_logging'
op|'.'
name|'getLogger'
op|'('
nl|'\n'
string|"'migrate.versioning.api'"
op|')'
op|'.'
name|'setLevel'
op|'('
name|'std_logging'
op|'.'
name|'WARNING'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OutputStreamCapture
dedent|''
dedent|''
dedent|''
name|'class'
name|'OutputStreamCapture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Capture output streams during tests.\n\n    This fixture captures errant printing to stderr / stdout during\n    the tests and lets us see those streams at the end of the test\n    runs instead. Useful to see what was happening during failed\n    tests.\n    """'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'OutputStreamCapture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDOUT_CAPTURE'"
op|')'
name|'in'
name|'_TRUE_VALUES'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'out'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StringStream'
op|'('
string|"'stdout'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'sys.stdout'"
op|','
name|'self'
op|'.'
name|'out'
op|'.'
name|'stream'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDERR_CAPTURE'"
op|')'
name|'in'
name|'_TRUE_VALUES'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'err'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StringStream'
op|'('
string|"'stderr'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'sys.stderr'"
op|','
name|'self'
op|'.'
name|'err'
op|'.'
name|'stream'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|stderr
name|'def'
name|'stderr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'err'
op|'.'
name|'_details'
op|'['
string|'"stderr"'
op|']'
op|'.'
name|'as_text'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|stdout
name|'def'
name|'stdout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'out'
op|'.'
name|'_details'
op|'['
string|'"stdout"'
op|']'
op|'.'
name|'as_text'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Timeout
dedent|''
dedent|''
name|'class'
name|'Timeout'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Setup per test timeouts.\n\n    In order to avoid test deadlocks we support setting up a test\n    timeout parameter read from the environment. In almost all\n    cases where the timeout is reached this means a deadlock.\n\n    A class level TIMEOUT_SCALING_FACTOR also exists, which allows\n    extremely long tests to specify they need more time.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'timeout'
op|','
name|'scaling'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Timeout'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'test_timeout'
op|'='
name|'int'
op|'('
name|'timeout'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|'# If timeout value is invalid do not set a timeout.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'test_timeout'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'if'
name|'scaling'
op|'>='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'test_timeout'
op|'*='
name|'scaling'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
string|"'scaling value must be >= 1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Timeout'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'test_timeout'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
name|'self'
op|'.'
name|'test_timeout'
op|','
name|'gentle'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Database
dedent|''
dedent|''
dedent|''
name|'class'
name|'Database'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
DECL|member|_cache_schema
indent|'    '
name|'def'
name|'_cache_schema'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'DB_SCHEMA'
newline|'\n'
name|'if'
name|'not'
name|'DB_SCHEMA'
op|':'
newline|'\n'
indent|'            '
name|'engine'
op|'='
name|'session'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'='
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'migration'
op|'.'
name|'db_sync'
op|'('
op|')'
newline|'\n'
name|'DB_SCHEMA'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'line'
name|'for'
name|'line'
name|'in'
name|'conn'
op|'.'
name|'connection'
op|'.'
name|'iterdump'
op|'('
op|')'
op|')'
newline|'\n'
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset
dedent|''
dedent|''
name|'def'
name|'reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_cache_schema'
op|'('
op|')'
newline|'\n'
name|'engine'
op|'='
name|'session'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'='
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'connection'
op|'.'
name|'executescript'
op|'('
name|'DB_SCHEMA'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Database'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RPCFixture
dedent|''
dedent|''
name|'class'
name|'RPCFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
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
op|'*'
name|'exmods'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'RPCFixture'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'exmods'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'exmods'
op|'.'
name|'extend'
op|'('
name|'exmods'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'RPCFixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'rpc'
op|'.'
name|'cleanup'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'add_extra_exmods'
op|'('
op|'*'
name|'self'
op|'.'
name|'exmods'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'rpc'
op|'.'
name|'clear_extra_exmods'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'messaging_conf'
op|'='
name|'messaging_conffixture'
op|'.'
name|'ConfFixture'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'messaging_conf'
op|'.'
name|'transport_driver'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'self'
op|'.'
name|'messaging_conf'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'init'
op|'('
name|'CONF'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WarningsFixture
dedent|''
dedent|''
name|'class'
name|'WarningsFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filters out warnings during test runs."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'WarningsFixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(sdague): Make deprecation warnings only happen once. Otherwise'
nl|'\n'
comment|'# this gets kind of crazy given the way that upstream python libs use'
nl|'\n'
comment|'# this.'
nl|'\n'
name|'warnings'
op|'.'
name|'simplefilter'
op|'('
string|'"once"'
op|','
name|'DeprecationWarning'
op|')'
newline|'\n'
name|'warnings'
op|'.'
name|'filterwarnings'
op|'('
string|"'ignore'"
op|','
nl|'\n'
name|'message'
op|'='
string|"'With-statements now directly support'"
nl|'\n'
string|"' multiple context managers'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'warnings'
op|'.'
name|'resetwarnings'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfPatcher
dedent|''
dedent|''
name|'class'
name|'ConfPatcher'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fixture to patch and restore global CONF.\n\n    This also resets overrides for everything that is patched during\n    it\'s teardown.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructor\n\n        :params group: if specified all config options apply to that group.\n\n        :params **kwargs: the rest of the kwargs are processed as a\n        set of key/value pairs to be set as configuration override.\n\n        """'
newline|'\n'
name|'super'
op|'('
name|'ConfPatcher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'group'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'group'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'args'
op|'='
name|'kwargs'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConfPatcher'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'args'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'CONF'
op|'.'
name|'clear_override'
op|','
name|'k'
op|','
name|'self'
op|'.'
name|'group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
name|'k'
op|','
name|'v'
op|','
name|'self'
op|'.'
name|'group'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OSAPIFixture
dedent|''
dedent|''
dedent|''
name|'class'
name|'OSAPIFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create an OS API server as a fixture.\n\n    This spawns an OS API server as a fixture in a new greenthread in\n    the current test. The fixture has a .api paramenter with is a\n    simple rest client that can communicate with it.\n\n    This fixture is extremely useful for testing REST responses\n    through the WSGI stack easily in functional tests.\n\n    Usage:\n\n        api = self.useFixture(fixtures.OSAPIFixture()).api\n        resp = api.api_request(\'/someurl\')\n        self.assertEqual(200, resp.status_code)\n        resp = api.api_request(\'/otherurl\', method=\'POST\', body=\'{foo}\')\n\n    The resp is a requests library response. Common attributes that\n    you\'ll want to use are:\n\n    - resp.status_code - integer HTTP status code returned by the request\n    - resp.content - the body of the response\n    - resp.headers - dictionary of HTTP headers returned\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'api_version'
op|'='
string|"'v2'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructor\n\n        :param api_version: the API version that we\'re interested in\n        using. Currently this expects \'v2\' or \'v2.1\' as possible\n        options.\n\n        """'
newline|'\n'
name|'super'
op|'('
name|'OSAPIFixture'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api_version'
op|'='
name|'api_version'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'OSAPIFixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# in order to run these in tests we need to bind only to local'
nl|'\n'
comment|'# host, and dynamically allocate ports'
nl|'\n'
name|'conf_overrides'
op|'='
op|'{'
nl|'\n'
string|"'ec2_listen'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'osapi_compute_listen'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'metadata_listen'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'ec2_listen_port'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'osapi_compute_listen_port'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'metadata_listen_port'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'verbose'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'debug'"
op|':'
name|'True'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'ConfPatcher'
op|'('
op|'**'
name|'conf_overrides'
op|')'
op|')'
newline|'\n'
name|'osapi'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"osapi_compute"'
op|')'
newline|'\n'
name|'osapi'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'osapi'
op|'.'
name|'stop'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth_url'
op|'='
string|"'http://%(host)s:%(port)s/%(api_version)s'"
op|'%'
op|'('
op|'{'
nl|'\n'
string|"'host'"
op|':'
name|'osapi'
op|'.'
name|'host'
op|','
string|"'port'"
op|':'
name|'osapi'
op|'.'
name|'port'
op|','
nl|'\n'
string|"'api_version'"
op|':'
name|'self'
op|'.'
name|'api_version'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'client'
op|'.'
name|'TestOpenStackClient'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'self'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PoisonFunctions
dedent|''
dedent|''
name|'class'
name|'PoisonFunctions'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Poison functions so they explode if we touch them.\n\n    When running under a non full stack test harness there are parts\n    of the code that you don\'t want to go anywhere near. These include\n    things like code that spins up extra threads, which just\n    introduces races.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PoisonFunctions'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# The nova libvirt driver starts an event thread which only'
nl|'\n'
comment|"# causes trouble in tests. Make sure that if tests don't"
nl|'\n'
comment|'# properly patch it the test explodes.'
nl|'\n'
nl|'\n'
comment|"# explicit import because MonkeyPatch doesn't magic import"
nl|'\n'
comment|'# correctly if we are patching a method on a class in a'
nl|'\n'
comment|'# module.'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'host'
comment|'# noqa'
newline|'\n'
nl|'\n'
DECL|function|evloop
name|'def'
name|'evloop'
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
name|'import'
name|'sys'
newline|'\n'
name|'warnings'
op|'.'
name|'warn'
op|'('
string|'"Forgot to disable libvirt event thread"'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.libvirt.host.Host._init_events'"
op|','
nl|'\n'
name|'evloop'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
