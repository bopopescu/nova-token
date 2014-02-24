begin_unit
comment|'# Copyright 2010-2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2012-2013 IBM Corp.'
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
name|'functools'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
nl|'\n'
name|'import'
name|'lockfile'
newline|'\n'
name|'from'
name|'six'
name|'import'
name|'moves'
newline|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
name|'import'
name|'parse'
newline|'\n'
name|'import'
name|'sqlalchemy'
newline|'\n'
name|'import'
name|'sqlalchemy'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
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
name|'utils'
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
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'test'
newline|'\n'
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
DECL|function|_have_mysql
name|'def'
name|'_have_mysql'
op|'('
name|'user'
op|','
name|'passwd'
op|','
name|'database'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'present'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'TEST_MYSQL_PRESENT'"
op|')'
newline|'\n'
name|'if'
name|'present'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'is_backend_avail'
op|'('
name|'backend'
op|'='
string|"'mysql'"
op|','
nl|'\n'
name|'user'
op|'='
name|'user'
op|','
nl|'\n'
name|'passwd'
op|'='
name|'passwd'
op|','
nl|'\n'
name|'database'
op|'='
name|'database'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'present'
op|'.'
name|'lower'
op|'('
op|')'
name|'in'
op|'('
string|"''"
op|','
string|"'true'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_have_postgresql
dedent|''
name|'def'
name|'_have_postgresql'
op|'('
name|'user'
op|','
name|'passwd'
op|','
name|'database'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'present'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'TEST_POSTGRESQL_PRESENT'"
op|')'
newline|'\n'
name|'if'
name|'present'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'is_backend_avail'
op|'('
name|'backend'
op|'='
string|"'postgres'"
op|','
nl|'\n'
name|'user'
op|'='
name|'user'
op|','
nl|'\n'
name|'passwd'
op|'='
name|'passwd'
op|','
nl|'\n'
name|'database'
op|'='
name|'database'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'present'
op|'.'
name|'lower'
op|'('
op|')'
name|'in'
op|'('
string|"''"
op|','
string|"'true'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_set_db_lock
dedent|''
name|'def'
name|'_set_db_lock'
op|'('
name|'lock_path'
op|'='
name|'None'
op|','
name|'lock_prefix'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
DECL|function|decorator
indent|'    '
name|'def'
name|'decorator'
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
DECL|function|wrapper
name|'def'
name|'wrapper'
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
name|'path'
op|'='
name|'lock_path'
name|'or'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|'"NOVA_LOCK_PATH"'
op|')'
newline|'\n'
name|'lock'
op|'='
name|'lockfile'
op|'.'
name|'FileLock'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
name|'lock_prefix'
op|')'
op|')'
newline|'\n'
name|'with'
name|'lock'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'\'Got lock "%s"\''
op|'%'
name|'f'
op|'.'
name|'__name__'
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
string|'\'Lock released "%s"\''
op|'%'
name|'f'
op|'.'
name|'__name__'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
dedent|''
name|'return'
name|'decorator'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseMigrationTestCase
dedent|''
name|'class'
name|'BaseMigrationTestCase'
op|'('
name|'test'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class fort testing of migration utils."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'super'
op|'('
name|'BaseMigrationTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'DEFAULT_CONFIG_FILE'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
nl|'\n'
string|"'test_migrations.conf'"
op|')'
newline|'\n'
comment|'# Test machines can set the TEST_MIGRATIONS_CONF variable'
nl|'\n'
comment|'# to override the location of the config file for migration testing'
nl|'\n'
name|'self'
op|'.'
name|'CONFIG_FILE_PATH'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'TEST_MIGRATIONS_CONF'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'DEFAULT_CONFIG_FILE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_databases'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'migration_api'
op|'='
name|'None'
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
name|'BaseMigrationTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Load test databases from the config file. Only do this'
nl|'\n'
comment|'# once. No need to re-run this on each test...'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'config_path is %s'"
op|'%'
name|'self'
op|'.'
name|'CONFIG_FILE_PATH'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'CONFIG_FILE_PATH'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cp'
op|'='
name|'moves'
op|'.'
name|'configparser'
op|'.'
name|'RawConfigParser'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'cp'
op|'.'
name|'read'
op|'('
name|'self'
op|'.'
name|'CONFIG_FILE_PATH'
op|')'
newline|'\n'
name|'defaults'
op|'='
name|'cp'
op|'.'
name|'defaults'
op|'('
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'defaults'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'test_databases'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'moves'
op|'.'
name|'configparser'
op|'.'
name|'ParsingError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Failed to read test_migrations.conf config "'
nl|'\n'
string|'"file. Got error: %s"'
op|'%'
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Failed to find test_migrations.conf config "'
nl|'\n'
string|'"file."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'engines'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'self'
op|'.'
name|'test_databases'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'engines'
op|'['
name|'key'
op|']'
op|'='
name|'sqlalchemy'
op|'.'
name|'create_engine'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
comment|'# We start each test case with a completely blank slate.'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_reset_databases'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# We destroy the test data store between each test case,'
nl|'\n'
comment|'# and recreate it, which ensures that we have no side-effects'
nl|'\n'
comment|'# from the tests'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_reset_databases'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'BaseMigrationTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|execute_cmd
dedent|''
name|'def'
name|'execute_cmd'
op|'('
name|'self'
op|','
name|'cmd'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'process'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
name|'shell'
op|'='
name|'True'
op|','
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'subprocess'
op|'.'
name|'STDOUT'
op|')'
newline|'\n'
name|'output'
op|'='
name|'process'
op|'.'
name|'communicate'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'process'
op|'.'
name|'returncode'
op|','
nl|'\n'
string|'"Failed to run: %s\\n%s"'
op|'%'
op|'('
name|'cmd'
op|','
name|'output'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_reset_pg
dedent|''
name|'def'
name|'_reset_pg'
op|'('
name|'self'
op|','
name|'conn_pieces'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'user'
op|','
nl|'\n'
name|'password'
op|','
nl|'\n'
name|'database'
op|','
nl|'\n'
name|'host'
op|')'
op|'='
name|'utils'
op|'.'
name|'get_db_connection_info'
op|'('
name|'conn_pieces'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'environ'
op|'['
string|"'PGPASSWORD'"
op|']'
op|'='
name|'password'
newline|'\n'
name|'os'
op|'.'
name|'environ'
op|'['
string|"'PGUSER'"
op|']'
op|'='
name|'user'
newline|'\n'
comment|"# note(boris-42): We must create and drop database, we can't"
nl|'\n'
comment|'# drop database which we have connected to, so for such'
nl|'\n'
comment|'# operations there is a special database template1.'
nl|'\n'
name|'sqlcmd'
op|'='
op|'('
string|'"psql -w -U %(user)s -h %(host)s -c"'
nl|'\n'
string|'" \'%(sql)s\' -d template1"'
op|')'
newline|'\n'
nl|'\n'
name|'sql'
op|'='
op|'('
string|'"drop database if exists %s;"'
op|')'
op|'%'
name|'database'
newline|'\n'
name|'droptable'
op|'='
name|'sqlcmd'
op|'%'
op|'{'
string|"'user'"
op|':'
name|'user'
op|','
string|"'host'"
op|':'
name|'host'
op|','
string|"'sql'"
op|':'
name|'sql'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'execute_cmd'
op|'('
name|'droptable'
op|')'
newline|'\n'
nl|'\n'
name|'sql'
op|'='
op|'('
string|'"create database %s;"'
op|')'
op|'%'
name|'database'
newline|'\n'
name|'createtable'
op|'='
name|'sqlcmd'
op|'%'
op|'{'
string|"'user'"
op|':'
name|'user'
op|','
string|"'host'"
op|':'
name|'host'
op|','
string|"'sql'"
op|':'
name|'sql'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'execute_cmd'
op|'('
name|'createtable'
op|')'
newline|'\n'
nl|'\n'
name|'os'
op|'.'
name|'unsetenv'
op|'('
string|"'PGPASSWORD'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unsetenv'
op|'('
string|"'PGUSER'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'_set_db_lock'
op|'('
name|'lock_prefix'
op|'='
string|"'migration_tests-'"
op|')'
newline|'\n'
DECL|member|_reset_databases
name|'def'
name|'_reset_databases'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
op|','
name|'engine'
name|'in'
name|'self'
op|'.'
name|'engines'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'conn_string'
op|'='
name|'self'
op|'.'
name|'test_databases'
op|'['
name|'key'
op|']'
newline|'\n'
name|'conn_pieces'
op|'='
name|'parse'
op|'.'
name|'urlparse'
op|'('
name|'conn_string'
op|')'
newline|'\n'
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
name|'if'
name|'conn_string'
op|'.'
name|'startswith'
op|'('
string|"'sqlite'"
op|')'
op|':'
newline|'\n'
comment|'# We can just delete the SQLite database, which is'
nl|'\n'
comment|'# the easiest and cleanest solution'
nl|'\n'
indent|'                '
name|'db_path'
op|'='
name|'conn_pieces'
op|'.'
name|'path'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'db_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'db_path'
op|')'
newline|'\n'
comment|'# No need to recreate the SQLite DB. SQLite will'
nl|'\n'
comment|"# create it for us if it's not there..."
nl|'\n'
dedent|''
dedent|''
name|'elif'
name|'conn_string'
op|'.'
name|'startswith'
op|'('
string|"'mysql'"
op|')'
op|':'
newline|'\n'
comment|'# We can execute the MySQL client to destroy and re-create'
nl|'\n'
comment|'# the MYSQL database, which is easier and less error-prone'
nl|'\n'
comment|'# than using SQLAlchemy to do this via MetaData...trust me.'
nl|'\n'
indent|'                '
op|'('
name|'user'
op|','
name|'password'
op|','
name|'database'
op|','
name|'host'
op|')'
op|'='
name|'utils'
op|'.'
name|'get_db_connection_info'
op|'('
name|'conn_pieces'
op|')'
newline|'\n'
name|'sql'
op|'='
op|'('
string|'"drop database if exists %(db)s; "'
nl|'\n'
string|'"create database %(db)s;"'
op|')'
op|'%'
op|'{'
string|"'db'"
op|':'
name|'database'
op|'}'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|'"mysql -u \\"%(user)s\\" -p\\"%(password)s\\" -h %(host)s "'
nl|'\n'
string|'"-e \\"%(sql)s\\""'
op|')'
op|'%'
op|'{'
string|"'user'"
op|':'
name|'user'
op|','
string|"'password'"
op|':'
name|'password'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|','
string|"'sql'"
op|':'
name|'sql'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'execute_cmd'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'conn_string'
op|'.'
name|'startswith'
op|'('
string|"'postgresql'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_reset_pg'
op|'('
name|'conn_pieces'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WalkVersionsMixin
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'WalkVersionsMixin'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_walk_versions
indent|'    '
name|'def'
name|'_walk_versions'
op|'('
name|'self'
op|','
name|'engine'
op|'='
name|'None'
op|','
name|'snake_walk'
op|'='
name|'False'
op|','
name|'downgrade'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
comment|'# Determine latest version script from the repo, then'
nl|'\n'
comment|'# upgrade from 1 through to the latest, with no data'
nl|'\n'
comment|'# in the databases. This just checks that the schema itself'
nl|'\n'
comment|'# upgrades successfully.'
nl|'\n'
nl|'\n'
comment|'# Place the database under version control'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'migration_api'
op|'.'
name|'version_control'
op|'('
name|'engine'
op|','
name|'self'
op|'.'
name|'REPOSITORY'
op|','
nl|'\n'
name|'self'
op|'.'
name|'INIT_VERSION'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'INIT_VERSION'
op|','
nl|'\n'
name|'self'
op|'.'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'self'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'latest version is %s'"
op|'%'
name|'self'
op|'.'
name|'REPOSITORY'
op|'.'
name|'latest'
op|')'
newline|'\n'
name|'versions'
op|'='
name|'range'
op|'('
name|'self'
op|'.'
name|'INIT_VERSION'
op|'+'
number|'1'
op|','
name|'self'
op|'.'
name|'REPOSITORY'
op|'.'
name|'latest'
op|'+'
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'version'
name|'in'
name|'versions'
op|':'
newline|'\n'
comment|'# upgrade -> downgrade -> upgrade'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_migrate_up'
op|'('
name|'engine'
op|','
name|'version'
op|','
name|'with_data'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'snake_walk'
op|':'
newline|'\n'
indent|'                '
name|'downgraded'
op|'='
name|'self'
op|'.'
name|'_migrate_down'
op|'('
nl|'\n'
name|'engine'
op|','
name|'version'
op|'-'
number|'1'
op|','
name|'with_data'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'downgraded'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_migrate_up'
op|'('
name|'engine'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'downgrade'
op|':'
newline|'\n'
comment|'# Now walk it back down to 0 from the latest, testing'
nl|'\n'
comment|'# the downgrade paths.'
nl|'\n'
indent|'            '
name|'for'
name|'version'
name|'in'
name|'reversed'
op|'('
name|'versions'
op|')'
op|':'
newline|'\n'
comment|'# downgrade -> upgrade -> downgrade'
nl|'\n'
indent|'                '
name|'downgraded'
op|'='
name|'self'
op|'.'
name|'_migrate_down'
op|'('
name|'engine'
op|','
name|'version'
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'snake_walk'
name|'and'
name|'downgraded'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_migrate_up'
op|'('
name|'engine'
op|','
name|'version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_migrate_down'
op|'('
name|'engine'
op|','
name|'version'
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_migrate_down
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_migrate_down'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'version'
op|','
name|'with_data'
op|'='
name|'False'
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
name|'migration_api'
op|'.'
name|'downgrade'
op|'('
name|'engine'
op|','
name|'self'
op|'.'
name|'REPOSITORY'
op|','
name|'version'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NotImplementedError'
op|':'
newline|'\n'
comment|'# NOTE(sirp): some migrations, namely release-level'
nl|'\n'
comment|"# migrations, don't support a downgrade."
nl|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'version'
op|','
name|'self'
op|'.'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
name|'self'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(sirp): `version` is what we're downgrading to (i.e. the 'target'"
nl|'\n'
comment|'# version). So if we have any downgrade checks, they need to be run for'
nl|'\n'
comment|'# the previous (higher numbered) migration.'
nl|'\n'
name|'if'
name|'with_data'
op|':'
newline|'\n'
indent|'            '
name|'post_downgrade'
op|'='
name|'getattr'
op|'('
nl|'\n'
name|'self'
op|','
string|'"_post_downgrade_%03d"'
op|'%'
op|'('
name|'version'
op|'+'
number|'1'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'post_downgrade'
op|':'
newline|'\n'
indent|'                '
name|'post_downgrade'
op|'('
name|'engine'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_migrate_up
dedent|''
name|'def'
name|'_migrate_up'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'version'
op|','
name|'with_data'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""migrate up to a new version of the db.\n\n        We allow for data insertion and post checks at every\n        migration version with special _pre_upgrade_### and\n        _check_### functions in the main test.\n        """'
newline|'\n'
comment|"# NOTE(sdague): try block is here because it's impossible to debug"
nl|'\n'
comment|'# where a failed data migration happens otherwise'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'with_data'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'='
name|'None'
newline|'\n'
name|'pre_upgrade'
op|'='
name|'getattr'
op|'('
nl|'\n'
name|'self'
op|','
string|'"_pre_upgrade_%03d"'
op|'%'
name|'version'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'pre_upgrade'
op|':'
newline|'\n'
indent|'                    '
name|'data'
op|'='
name|'pre_upgrade'
op|'('
name|'engine'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'migration_api'
op|'.'
name|'upgrade'
op|'('
name|'engine'
op|','
name|'self'
op|'.'
name|'REPOSITORY'
op|','
name|'version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'version'
op|','
nl|'\n'
name|'self'
op|'.'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'self'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
name|'if'
name|'with_data'
op|':'
newline|'\n'
indent|'                '
name|'check'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|'"_check_%03d"'
op|'%'
name|'version'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'check'
op|':'
newline|'\n'
indent|'                    '
name|'check'
op|'('
name|'engine'
op|','
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Failed to migrate to version %s on engine %s"'
op|')'
op|'%'
nl|'\n'
op|'('
name|'version'
op|','
name|'engine'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
