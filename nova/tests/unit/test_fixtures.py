begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'sqlalchemy'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
name|'as'
name|'fx'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'uuidutils'
newline|'\n'
name|'import'
name|'testtools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'service'
name|'as'
name|'service_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fixtures'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'conf_fixture'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestConfFixture
name|'class'
name|'TestConfFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test the Conf fixtures in Nova.\n\n    This is a basic test that this fixture works like we expect.\n\n    Expectations:\n\n    1. before using the fixture, a default value (api_paste_config)\n       comes through untouched.\n\n    2. before using the fixture, a known default value that we\n       override is correct.\n\n    3. after using the fixture a known value that we override is the\n       new value.\n\n    4. after using the fixture we can set a default value to something\n       random, and it will be reset once we are done.\n\n    There are 2 copies of this test so that you can verify they do the\n    right thing with:\n\n       tox -e py27 test_fixtures -- --concurrency=1\n\n    As regardless of run order, their initial asserts would be\n    impacted if the reset behavior isn\'t working correctly.\n\n    """'
newline|'\n'
DECL|member|_test_override
name|'def'
name|'_test_override'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'api-paste.ini'"
op|','
name|'CONF'
op|'.'
name|'wsgi'
op|'.'
name|'api_paste_config'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'CONF'
op|'.'
name|'fake_network'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_default'
op|'('
string|"'api_paste_config'"
op|','
string|"'foo'"
op|','
name|'group'
op|'='
string|"'wsgi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'CONF'
op|'.'
name|'fake_network'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_override1
dedent|''
name|'def'
name|'test_override1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_override'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_override2
dedent|''
name|'def'
name|'test_override2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_override'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestOutputStream
dedent|''
dedent|''
name|'class'
name|'TestOutputStream'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure Output Stream capture works as expected.\n\n    This has the added benefit of providing a code example of how you\n    can manipulate the output stream in your own tests.\n    """'
newline|'\n'
DECL|member|test_output
name|'def'
name|'test_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fx'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'OS_STDOUT_CAPTURE'"
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fx'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'OS_STDERR_CAPTURE'"
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'out'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'OutputStreamCapture'
op|'('
op|')'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
string|'"foo"'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
string|'"bar"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"foo"'
op|','
name|'out'
op|'.'
name|'stdout'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"bar"'
op|','
name|'out'
op|'.'
name|'stderr'
op|')'
newline|'\n'
comment|"# TODO(sdague): nuke the out and err buffers so it doesn't"
nl|'\n'
comment|'# make it to testr'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLogging
dedent|''
dedent|''
name|'class'
name|'TestLogging'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_default_logging
indent|'    '
name|'def'
name|'test_default_logging'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stdlog'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StandardLogging'
op|'('
op|')'
op|')'
newline|'\n'
name|'root'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
comment|'# there should be a null handler as well at DEBUG'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'root'
op|'.'
name|'handlers'
op|')'
op|','
name|'root'
op|'.'
name|'handlers'
op|')'
newline|'\n'
name|'log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'info'
op|'('
string|'"at info"'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'debug'
op|'('
string|'"at debug"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"at info"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|'"at debug"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
nl|'\n'
comment|'# broken debug messages should still explode, even though we'
nl|'\n'
comment|"# aren't logging them in the regular handler"
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TypeError'
op|','
name|'log'
op|'.'
name|'debug'
op|','
string|'"this is broken %s %s"'
op|','
string|'"foo"'
op|')'
newline|'\n'
nl|'\n'
comment|"# and, ensure that one of the terrible log messages isn't"
nl|'\n'
comment|'# output at info'
nl|'\n'
name|'warn_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'migrate.versioning.api'"
op|')'
newline|'\n'
name|'warn_log'
op|'.'
name|'info'
op|'('
string|'"warn_log at info, should be skipped"'
op|')'
newline|'\n'
name|'warn_log'
op|'.'
name|'error'
op|'('
string|'"warn_log at error"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"warn_log at error"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|'"warn_log at info"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_debug_logging
dedent|''
name|'def'
name|'test_debug_logging'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fx'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'OS_DEBUG'"
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'stdlog'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StandardLogging'
op|'('
op|')'
op|')'
newline|'\n'
name|'root'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
comment|'# there should no longer be a null handler'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'root'
op|'.'
name|'handlers'
op|')'
op|','
name|'root'
op|'.'
name|'handlers'
op|')'
newline|'\n'
name|'log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'info'
op|'('
string|'"at info"'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'debug'
op|'('
string|'"at debug"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"at info"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"at debug"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestTimeout
dedent|''
dedent|''
name|'class'
name|'TestTimeout'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests for our timeout fixture.\n\n    Testing the actual timeout mechanism is beyond the scope of this\n    test, because it\'s a pretty clear pass through to fixtures\'\n    timeout fixture, which tested in their tree.\n\n    """'
newline|'\n'
DECL|member|test_scaling
name|'def'
name|'test_scaling'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# a bad scaling factor'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'fixtures'
op|'.'
name|'Timeout'
op|','
number|'1'
op|','
number|'0.5'
op|')'
newline|'\n'
nl|'\n'
comment|'# various things that should work.'
nl|'\n'
name|'timeout'
op|'='
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'10'
op|','
name|'timeout'
op|'.'
name|'test_timeout'
op|')'
newline|'\n'
name|'timeout'
op|'='
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
string|'"10"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'10'
op|','
name|'timeout'
op|'.'
name|'test_timeout'
op|')'
newline|'\n'
name|'timeout'
op|'='
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
string|'"10"'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'20'
op|','
name|'timeout'
op|'.'
name|'test_timeout'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestOSAPIFixture
dedent|''
dedent|''
name|'class'
name|'TestOSAPIFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service.get_by_host_and_binary'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service.create'"
op|')'
newline|'\n'
DECL|member|test_responds_to_version
name|'def'
name|'test_responds_to_version'
op|'('
name|'self'
op|','
name|'mock_service_create'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the OSAPI server responds to calls sensibly."""'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'OutputStreamCapture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StandardLogging'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'RPCFixture'
op|'('
string|"'nova.test'"
op|')'
op|')'
newline|'\n'
name|'api'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'OSAPIFixture'
op|'('
op|')'
op|')'
op|'.'
name|'api'
newline|'\n'
nl|'\n'
comment|'# request the API root, which provides us the versions of the API'
nl|'\n'
name|'resp'
op|'='
name|'api'
op|'.'
name|'api_request'
op|'('
string|"'/'"
op|','
name|'strip_version'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'resp'
op|'.'
name|'status_code'
op|','
name|'resp'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
comment|'# request a bad root url, should be a 404'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# NOTE(sdague): this currently fails, as it falls into the 300'
nl|'\n'
comment|'# dispatcher instead. This is a bug. The test case is left in'
nl|'\n'
comment|'# here, commented out until we can address it.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# resp = api.api_request('/foo', strip_version=True)"
nl|'\n'
comment|'# self.assertEqual(resp.status_code, 400, resp.content)'
nl|'\n'
nl|'\n'
comment|'# request a known bad url, and we should get a 404'
nl|'\n'
name|'resp'
op|'='
name|'api'
op|'.'
name|'api_request'
op|'('
string|"'/foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'resp'
op|'.'
name|'status_code'
op|','
name|'resp'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDatabaseFixture
dedent|''
dedent|''
name|'class'
name|'TestDatabaseFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_fixture_reset
indent|'    '
name|'def'
name|'test_fixture_reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# because this sets up reasonable db connection strings'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
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
name|'conn'
op|'='
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from instance_types"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
comment|'# insert a 6th instance type, column 5 below is an int id'
nl|'\n'
comment|'# which has a constraint on it, so if new standard instance'
nl|'\n'
comment|'# types are added you have to bump it.'
nl|'\n'
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"insert into instance_types VALUES "'
nl|'\n'
string|'"(NULL, NULL, NULL, \'t1.test\', 6, 4096, 2, 0, NULL, \'87\'"'
nl|'\n'
string|'", 1.0, 40, 0, 0, 1, 0)"'
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from instance_types"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
comment|'# reset by invoking the fixture again'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# NOTE(sdague): it's important to reestablish the db"
nl|'\n'
comment|'# connection because otherwise we have a reference to the old'
nl|'\n'
comment|'# in mem db.'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
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
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from instance_types"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_api_fixture_reset
dedent|''
name|'def'
name|'test_api_fixture_reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# This sets up reasonable db connection strings'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
op|')'
newline|'\n'
name|'engine'
op|'='
name|'session'
op|'.'
name|'get_api_engine'
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
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from cell_mappings"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"insert into cell_mappings (uuid, name) VALUES "'
nl|'\n'
string|'"(\'%s\', \'fake-cell\')"'
op|'%'
op|'('
name|'uuid'
op|','
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from cell_mappings"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
comment|'# reset by invoking the fixture again'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# NOTE(sdague): it's important to reestablish the db"
nl|'\n'
comment|'# connection because otherwise we have a reference to the old'
nl|'\n'
comment|'# in mem db.'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
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
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from cell_mappings"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixture_cleanup
dedent|''
name|'def'
name|'test_fixture_cleanup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# because this sets up reasonable db connection strings'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'fix'
op|'='
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fix'
op|')'
newline|'\n'
nl|'\n'
comment|'# manually do the cleanup that addCleanup will do'
nl|'\n'
name|'fix'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure the db contains nothing'
nl|'\n'
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
name|'schema'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'schema'
op|','
string|'"BEGIN TRANSACTION;COMMIT;"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_api_fixture_cleanup
dedent|''
name|'def'
name|'test_api_fixture_cleanup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# This sets up reasonable db connection strings'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'fix'
op|'='
name|'fixtures'
op|'.'
name|'Database'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fix'
op|')'
newline|'\n'
nl|'\n'
comment|'# No data inserted by migrations so we need to add a row'
nl|'\n'
name|'engine'
op|'='
name|'session'
op|'.'
name|'get_api_engine'
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
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"insert into cell_mappings (uuid, name) VALUES "'
nl|'\n'
string|'"(\'%s\', \'fake-cell\')"'
op|'%'
op|'('
name|'uuid'
op|','
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from cell_mappings"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
comment|'# Manually do the cleanup that addCleanup will do'
nl|'\n'
name|'fix'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Ensure the db contains nothing'
nl|'\n'
name|'engine'
op|'='
name|'session'
op|'.'
name|'get_api_engine'
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
name|'schema'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"BEGIN TRANSACTION;COMMIT;"'
op|','
name|'schema'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDatabaseAtVersionFixture
dedent|''
dedent|''
name|'class'
name|'TestDatabaseAtVersionFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_fixture_schema_version
indent|'    '
name|'def'
name|'test_fixture_schema_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# In/after 317 aggregates did have uuid'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'DatabaseAtVersion'
op|'('
number|'318'
op|')'
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
name|'connect'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'='
name|'sqlalchemy'
op|'.'
name|'MetaData'
op|'('
name|'engine'
op|')'
newline|'\n'
name|'aggregate'
op|'='
name|'sqlalchemy'
op|'.'
name|'Table'
op|'('
string|"'aggregates'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'aggregate'
op|'.'
name|'c'
op|','
string|"'uuid'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Before 317, aggregates had no uuid'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'DatabaseAtVersion'
op|'('
number|'316'
op|')'
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
name|'connect'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'='
name|'sqlalchemy'
op|'.'
name|'MetaData'
op|'('
name|'engine'
op|')'
newline|'\n'
name|'aggregate'
op|'='
name|'sqlalchemy'
op|'.'
name|'Table'
op|'('
string|"'aggregates'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'hasattr'
op|'('
name|'aggregate'
op|'.'
name|'c'
op|','
string|"'uuid'"
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
DECL|member|test_fixture_after_database_fixture
dedent|''
name|'def'
name|'test_fixture_after_database_fixture'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'DatabaseAtVersion'
op|'('
number|'318'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDefaultFlavorsFixture
dedent|''
dedent|''
name|'class'
name|'TestDefaultFlavorsFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_flavors
indent|'    '
name|'def'
name|'test_flavors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'engine'
op|'='
name|'session'
op|'.'
name|'get_api_engine'
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
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from flavors"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'DefaultFlavorsFixture'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from flavors"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'5'
op|','
name|'len'
op|'('
name|'rows'
op|')'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestIndirectionAPIFixture
dedent|''
dedent|''
name|'class'
name|'TestIndirectionAPIFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_indirection_api
indent|'    '
name|'def'
name|'test_indirection_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Should initially be None'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|')'
newline|'\n'
nl|'\n'
comment|'# make sure the fixture correctly sets the value'
nl|'\n'
name|'fix'
op|'='
name|'fixtures'
op|'.'
name|'IndirectionAPIFixture'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fix'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|')'
newline|'\n'
nl|'\n'
comment|'# manually do the cleanup that addCleanup will do'
nl|'\n'
name|'fix'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure the initial value is restored'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSpawnIsSynchronousFixture
dedent|''
dedent|''
name|'class'
name|'TestSpawnIsSynchronousFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_spawn_patch
indent|'    '
name|'def'
name|'test_spawn_patch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'orig_spawn'
op|'='
name|'utils'
op|'.'
name|'spawn_n'
newline|'\n'
nl|'\n'
name|'fix'
op|'='
name|'fixtures'
op|'.'
name|'SpawnIsSynchronousFixture'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fix'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'orig_spawn'
op|','
name|'utils'
op|'.'
name|'spawn_n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_passes_through
dedent|''
name|'def'
name|'test_spawn_passes_through'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'SpawnIsSynchronousFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'tester'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'tester'
op|'.'
name|'function'
op|','
string|"'foo'"
op|','
name|'bar'
op|'='
string|"'bar'"
op|')'
newline|'\n'
name|'tester'
op|'.'
name|'function'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'foo'"
op|','
name|'bar'
op|'='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_return_has_wait
dedent|''
name|'def'
name|'test_spawn_return_has_wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'SpawnIsSynchronousFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'gt'
op|'='
name|'utils'
op|'.'
name|'spawn'
op|'('
name|'lambda'
name|'x'
op|':'
string|"'%s'"
op|'%'
name|'x'
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'foo'
op|'='
name|'gt'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'foo'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_n_return_has_wait
dedent|''
name|'def'
name|'test_spawn_n_return_has_wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'SpawnIsSynchronousFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'gt'
op|'='
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'lambda'
name|'x'
op|':'
string|"'%s'"
op|'%'
name|'x'
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'foo'
op|'='
name|'gt'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'foo'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_has_link
dedent|''
name|'def'
name|'test_spawn_has_link'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'SpawnIsSynchronousFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'gt'
op|'='
name|'utils'
op|'.'
name|'spawn'
op|'('
name|'mock'
op|'.'
name|'MagicMock'
op|')'
newline|'\n'
name|'passed_arg'
op|'='
string|"'test'"
newline|'\n'
name|'call_count'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake
name|'def'
name|'fake'
op|'('
name|'thread'
op|','
name|'param'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'gt'
op|','
name|'thread'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'passed_arg'
op|','
name|'param'
op|')'
newline|'\n'
name|'call_count'
op|'.'
name|'append'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'gt'
op|'.'
name|'link'
op|'('
name|'fake'
op|','
name|'passed_arg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'call_count'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_n_has_link
dedent|''
name|'def'
name|'test_spawn_n_has_link'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'SpawnIsSynchronousFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'gt'
op|'='
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'mock'
op|'.'
name|'MagicMock'
op|')'
newline|'\n'
name|'passed_arg'
op|'='
string|"'test'"
newline|'\n'
name|'call_count'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake
name|'def'
name|'fake'
op|'('
name|'thread'
op|','
name|'param'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'gt'
op|','
name|'thread'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'passed_arg'
op|','
name|'param'
op|')'
newline|'\n'
name|'call_count'
op|'.'
name|'append'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'gt'
op|'.'
name|'link'
op|'('
name|'fake'
op|','
name|'passed_arg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'call_count'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestBannedDBSchemaOperations
dedent|''
dedent|''
name|'class'
name|'TestBannedDBSchemaOperations'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_column
indent|'    '
name|'def'
name|'test_column'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'column'
op|'='
name|'sqlalchemy'
op|'.'
name|'Column'
op|'('
op|')'
newline|'\n'
name|'with'
name|'fixtures'
op|'.'
name|'BannedDBSchemaOperations'
op|'('
op|'['
string|"'Column'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DBNotAllowed'
op|','
nl|'\n'
name|'column'
op|'.'
name|'drop'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DBNotAllowed'
op|','
nl|'\n'
name|'column'
op|'.'
name|'alter'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_table
dedent|''
dedent|''
name|'def'
name|'test_table'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'='
name|'sqlalchemy'
op|'.'
name|'Table'
op|'('
op|')'
newline|'\n'
name|'with'
name|'fixtures'
op|'.'
name|'BannedDBSchemaOperations'
op|'('
op|'['
string|"'Table'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DBNotAllowed'
op|','
nl|'\n'
name|'table'
op|'.'
name|'drop'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DBNotAllowed'
op|','
nl|'\n'
name|'table'
op|'.'
name|'alter'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestStableObjectJsonFixture
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestStableObjectJsonFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_changes_sort
indent|'    '
name|'def'
name|'test_changes_sort'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|TestObject
indent|'        '
name|'class'
name|'TestObject'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|member|obj_what_changed
indent|'            '
name|'def'
name|'obj_what_changed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'['
string|"'z'"
op|','
string|"'a'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'obj'
op|'='
name|'TestObject'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'z'"
op|','
string|"'a'"
op|']'
op|','
nl|'\n'
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|'['
string|"'nova_object.changes'"
op|']'
op|')'
newline|'\n'
name|'with'
name|'fixtures'
op|'.'
name|'StableObjectJsonFixture'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'a'"
op|','
string|"'z'"
op|']'
op|','
nl|'\n'
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|'['
string|"'nova_object.changes'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestAllServicesCurrentFixture
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestAllServicesCurrentFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service._db_service_get_minimum_version'"
op|')'
newline|'\n'
DECL|member|test_services_current
name|'def'
name|'test_services_current'
op|'('
name|'self'
op|','
name|'mock_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'nova-compute'"
op|':'
number|'123'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'123'
op|','
name|'service_obj'
op|'.'
name|'Service'
op|'.'
name|'get_minimum_version'
op|'('
nl|'\n'
name|'None'
op|','
string|"'nova-compute'"
op|')'
op|')'
newline|'\n'
name|'mock_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'None'
op|','
op|'['
string|"'nova-compute'"
op|']'
op|','
nl|'\n'
name|'use_slave'
op|'='
name|'False'
op|')'
newline|'\n'
name|'mock_db'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'compute_rpcapi'
op|'.'
name|'LAST_VERSION'
op|'='
number|'123'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'AllServicesCurrent'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'compute_rpcapi'
op|'.'
name|'LAST_VERSION'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'service_obj'
op|'.'
name|'SERVICE_VERSION'
op|','
nl|'\n'
name|'service_obj'
op|'.'
name|'Service'
op|'.'
name|'get_minimum_version'
op|'('
nl|'\n'
name|'None'
op|','
string|"'nova-compute'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_db'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
