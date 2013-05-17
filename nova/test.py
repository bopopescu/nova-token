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
string|'"""Base classes for our unit tests.\n\nAllows overriding of flags for use of fakes, and some black magic for\ninline callbacks.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'eventlet'
op|'.'
name|'monkey_patch'
op|'('
name|'os'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'testtools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
name|'network'
name|'import'
name|'manager'
name|'as'
name|'network_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'session'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
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
name|'import'
name|'conf_fixture'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'policy_fixture'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|test_opts
name|'test_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sqlite_clean_db'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'clean.sqlite'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'File name of clean sqlite db'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
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
name|'test_opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'sql_connection'"
op|','
nl|'\n'
string|"'nova.openstack.common.db.sqlalchemy.session'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'sqlite_db'"
op|','
string|"'nova.openstack.common.db.sqlalchemy.session'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'use_stderr'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_DB_CACHE
name|'_DB_CACHE'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Database
name|'class'
name|'Database'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'db_session'
op|','
name|'db_migrate'
op|','
name|'sql_connection'
op|','
nl|'\n'
name|'sqlite_db'
op|','
name|'sqlite_clean_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'sql_connection'
op|'='
name|'sql_connection'
newline|'\n'
name|'self'
op|'.'
name|'sqlite_db'
op|'='
name|'sqlite_db'
newline|'\n'
name|'self'
op|'.'
name|'sqlite_clean_db'
op|'='
name|'sqlite_clean_db'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'engine'
op|'='
name|'db_session'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'if'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'db_migrate'
op|'.'
name|'db_version'
op|'('
op|')'
op|'>'
name|'db_migrate'
op|'.'
name|'INIT_VERSION'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'testdb'
op|'='
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'sqlite_db'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'testdb'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'db_migrate'
op|'.'
name|'db_sync'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'post_migrations'
op|'('
op|')'
newline|'\n'
name|'if'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'self'
op|'.'
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_DB'
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
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cleandb'
op|'='
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'sqlite_clean_db'
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'copyfile'
op|'('
name|'testdb'
op|','
name|'cleandb'
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
name|'Database'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_DB'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'engine'
op|'.'
name|'dispose'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'copyfile'
op|'('
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'self'
op|'.'
name|'sqlite_clean_db'
op|')'
op|','
nl|'\n'
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'self'
op|'.'
name|'sqlite_db'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_migrations
dedent|''
dedent|''
name|'def'
name|'post_migrations'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Any addition steps that are needed outside of the migrations."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'network'
op|'='
name|'network_manager'
op|'.'
name|'VlanManager'
op|'('
op|')'
newline|'\n'
name|'bridge_interface'
op|'='
name|'CONF'
op|'.'
name|'flat_interface'
name|'or'
name|'CONF'
op|'.'
name|'vlan_interface'
newline|'\n'
name|'network'
op|'.'
name|'create_networks'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'label'
op|'='
string|"'test'"
op|','
nl|'\n'
name|'cidr'
op|'='
name|'CONF'
op|'.'
name|'fixed_range'
op|','
nl|'\n'
name|'multi_host'
op|'='
name|'CONF'
op|'.'
name|'multi_host'
op|','
nl|'\n'
name|'num_networks'
op|'='
name|'CONF'
op|'.'
name|'num_networks'
op|','
nl|'\n'
name|'network_size'
op|'='
name|'CONF'
op|'.'
name|'network_size'
op|','
nl|'\n'
name|'cidr_v6'
op|'='
name|'CONF'
op|'.'
name|'fixed_range_v6'
op|','
nl|'\n'
name|'gateway'
op|'='
name|'CONF'
op|'.'
name|'gateway'
op|','
nl|'\n'
name|'gateway_v6'
op|'='
name|'CONF'
op|'.'
name|'gateway_v6'
op|','
nl|'\n'
name|'bridge'
op|'='
name|'CONF'
op|'.'
name|'flat_network_bridge'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
name|'bridge_interface'
op|','
nl|'\n'
name|'vpn_start'
op|'='
name|'CONF'
op|'.'
name|'vpn_start'
op|','
nl|'\n'
name|'vlan_start'
op|'='
name|'CONF'
op|'.'
name|'vlan_start'
op|','
nl|'\n'
name|'dns1'
op|'='
name|'CONF'
op|'.'
name|'flat_network_dns'
op|')'
newline|'\n'
name|'for'
name|'net'
name|'in'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'.'
name|'set_network_host'
op|'('
name|'ctxt'
op|','
name|'net'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ReplaceModule
dedent|''
dedent|''
dedent|''
name|'class'
name|'ReplaceModule'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Replace a module with a fake module."""'
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
name|'new_value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'new_value'
op|'='
name|'new_value'
newline|'\n'
nl|'\n'
DECL|member|_restore
dedent|''
name|'def'
name|'_restore'
op|'('
name|'self'
op|','
name|'old_value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'modules'
op|'['
name|'self'
op|'.'
name|'name'
op|']'
op|'='
name|'old_value'
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
name|'ReplaceModule'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'old_value'
op|'='
name|'sys'
op|'.'
name|'modules'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'modules'
op|'['
name|'self'
op|'.'
name|'name'
op|']'
op|'='
name|'self'
op|'.'
name|'new_value'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_restore'
op|','
name|'old_value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceFixture
dedent|''
dedent|''
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
name|'and'
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
DECL|class|MoxStubout
dedent|''
dedent|''
name|'class'
name|'MoxStubout'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deal with code around mox and stubout as a fixture."""'
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
name|'MoxStubout'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|"# emulate some of the mox stuff, we can't use the metaclass"
nl|'\n'
comment|'# because it screws with our generators'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'SmartUnsetAll'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestingException
dedent|''
dedent|''
name|'class'
name|'TestingException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCase
dedent|''
name|'class'
name|'TestCase'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case base class for all unit tests."""'
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
string|'"""Run before each test method to initialize test environment."""'
newline|'\n'
name|'super'
op|'('
name|'TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'test_timeout'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_TEST_TIMEOUT'"
op|','
number|'0'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'test_timeout'
op|'='
name|'int'
op|'('
name|'test_timeout'
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
name|'test_timeout'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'if'
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
name|'test_timeout'
op|','
name|'gentle'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'NestedTempfile'
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
name|'TempHomeDir'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDOUT_CAPTURE'"
op|')'
op|'=='
string|"'True'"
name|'or'
nl|'\n'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDOUT_CAPTURE'"
op|')'
op|'=='
string|"'1'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'stdout'
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
op|'.'
name|'stream'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'sys.stdout'"
op|','
name|'stdout'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDERR_CAPTURE'"
op|')'
op|'=='
string|"'True'"
name|'or'
nl|'\n'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDERR_CAPTURE'"
op|')'
op|'=='
string|"'1'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'stderr'
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
op|'.'
name|'stream'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'sys.stderr'"
op|','
name|'stderr'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'log_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'FakeLogger'
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
name|'CONF'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'global'
name|'_DB_CACHE'
newline|'\n'
name|'if'
name|'not'
name|'_DB_CACHE'
op|':'
newline|'\n'
indent|'            '
name|'_DB_CACHE'
op|'='
name|'Database'
op|'('
name|'session'
op|','
name|'migration'
op|','
nl|'\n'
name|'sql_connection'
op|'='
name|'CONF'
op|'.'
name|'sql_connection'
op|','
nl|'\n'
name|'sqlite_db'
op|'='
name|'CONF'
op|'.'
name|'sqlite_db'
op|','
nl|'\n'
name|'sqlite_clean_db'
op|'='
name|'CONF'
op|'.'
name|'sqlite_clean_db'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'_DB_CACHE'
op|')'
newline|'\n'
nl|'\n'
name|'mox_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'MoxStubout'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox_fixture'
op|'.'
name|'mox'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'mox_fixture'
op|'.'
name|'stubs'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_clear_attrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'http_proxy'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'policy_fixture'
op|'.'
name|'PolicyFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'fatal_exception_format_errors'"
op|','
name|'True'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'enabled'"
op|','
name|'True'
op|','
string|"'osapi_v3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_clear_attrs
dedent|''
name|'def'
name|'_clear_attrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Delete attributes that don't start with _ so they don't pin"
nl|'\n'
comment|'# memory around unnecessarily for the duration of the test'
nl|'\n'
comment|'# suite'
nl|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'__dict__'
op|'.'
name|'keys'
op|'('
op|')'
name|'if'
name|'k'
op|'['
number|'0'
op|']'
op|'!='
string|"'_'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'.'
name|'__dict__'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|member|flags
dedent|''
dedent|''
name|'def'
name|'flags'
op|'('
name|'self'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Override flag variables for a test."""'
newline|'\n'
name|'group'
op|'='
name|'kw'
op|'.'
name|'pop'
op|'('
string|"'group'"
op|','
name|'None'
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kw'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'CONF'
op|'.'
name|'set_override'
op|'('
name|'k'
op|','
name|'v'
op|','
name|'group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_service
dedent|''
dedent|''
name|'def'
name|'start_service'
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
name|'svc'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'ServiceFixture'
op|'('
name|'name'
op|','
name|'host'
op|','
op|'**'
name|'kwargs'
op|')'
op|')'
newline|'\n'
name|'return'
name|'svc'
op|'.'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APICoverage
dedent|''
dedent|''
name|'class'
name|'APICoverage'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|cover_api
indent|'    '
name|'cover_api'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|test_api_methods
name|'def'
name|'test_api_methods'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'cover_api'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'api_methods'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'dir'
op|'('
name|'self'
op|'.'
name|'cover_api'
op|')'
nl|'\n'
name|'if'
name|'not'
name|'x'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|']'
newline|'\n'
name|'test_methods'
op|'='
op|'['
name|'x'
op|'['
number|'5'
op|':'
op|']'
name|'for'
name|'x'
name|'in'
name|'dir'
op|'('
name|'self'
op|')'
nl|'\n'
name|'if'
name|'x'
op|'.'
name|'startswith'
op|'('
string|"'test_'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
nl|'\n'
name|'test_methods'
op|','
nl|'\n'
name|'testtools'
op|'.'
name|'matchers'
op|'.'
name|'ContainsAll'
op|'('
name|'api_methods'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TimeOverride
dedent|''
dedent|''
name|'class'
name|'TimeOverride'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fixture to start and remove time override."""'
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
name|'TimeOverride'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'timeutils'
op|'.'
name|'clear_time_override'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
