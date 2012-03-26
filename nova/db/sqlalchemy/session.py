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
string|'"""Session Handling for SQLAlchemy backend."""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'sqlalchemy'
op|'.'
name|'interfaces'
newline|'\n'
name|'import'
name|'sqlalchemy'
op|'.'
name|'orm'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'exc'
name|'import'
name|'DisconnectionError'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'pool'
name|'import'
name|'NullPool'
op|','
name|'StaticPool'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'flags'
name|'as'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'log'
name|'as'
name|'logging'
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
DECL|variable|_ENGINE
name|'_ENGINE'
op|'='
name|'None'
newline|'\n'
DECL|variable|_MAKER
name|'_MAKER'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_session
name|'def'
name|'get_session'
op|'('
name|'autocommit'
op|'='
name|'True'
op|','
name|'expire_on_commit'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a SQLAlchemy session."""'
newline|'\n'
name|'global'
name|'_MAKER'
newline|'\n'
nl|'\n'
name|'if'
name|'_MAKER'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'engine'
op|'='
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'_MAKER'
op|'='
name|'get_maker'
op|'('
name|'engine'
op|','
name|'autocommit'
op|','
name|'expire_on_commit'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'session'
op|'='
name|'_MAKER'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'query'
op|'='
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'wrap_db_error'
op|'('
name|'session'
op|'.'
name|'query'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'flush'
op|'='
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'wrap_db_error'
op|'('
name|'session'
op|'.'
name|'flush'
op|')'
newline|'\n'
name|'return'
name|'session'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SynchronousSwitchListener
dedent|''
name|'class'
name|'SynchronousSwitchListener'
op|'('
name|'sqlalchemy'
op|'.'
name|'interfaces'
op|'.'
name|'PoolListener'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Switch sqlite connections to non-synchronous mode"""'
newline|'\n'
nl|'\n'
DECL|member|connect
name|'def'
name|'connect'
op|'('
name|'self'
op|','
name|'dbapi_con'
op|','
name|'con_record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dbapi_con'
op|'.'
name|'execute'
op|'('
string|'"PRAGMA synchronous = OFF"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MySQLPingListener
dedent|''
dedent|''
name|'class'
name|'MySQLPingListener'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""\n    Ensures that MySQL connections checked out of the\n    pool are alive.\n\n    Borrowed from:\n    http://groups.google.com/group/sqlalchemy/msg/a4ce563d802c929f\n    """'
newline|'\n'
nl|'\n'
DECL|member|checkout
name|'def'
name|'checkout'
op|'('
name|'self'
op|','
name|'dbapi_con'
op|','
name|'con_record'
op|','
name|'con_proxy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'dbapi_con'
op|'.'
name|'cursor'
op|'('
op|')'
op|'.'
name|'execute'
op|'('
string|"'select 1'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'dbapi_con'
op|'.'
name|'OperationalError'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ex'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
name|'in'
op|'('
number|'2006'
op|','
number|'2013'
op|','
number|'2014'
op|','
number|'2045'
op|','
number|'2055'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
string|"'Got mysql server has gone away: %s'"
op|','
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'DisconnectionError'
op|'('
string|'"Database server went away"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_engine
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_engine'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a SQLAlchemy engine."""'
newline|'\n'
name|'global'
name|'_ENGINE'
newline|'\n'
name|'if'
name|'_ENGINE'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'connection_dict'
op|'='
name|'sqlalchemy'
op|'.'
name|'engine'
op|'.'
name|'url'
op|'.'
name|'make_url'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|')'
newline|'\n'
nl|'\n'
name|'engine_args'
op|'='
op|'{'
nl|'\n'
string|'"pool_recycle"'
op|':'
name|'FLAGS'
op|'.'
name|'sql_idle_timeout'
op|','
nl|'\n'
string|'"echo"'
op|':'
name|'False'
op|','
nl|'\n'
string|"'convert_unicode'"
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|"# Map our SQL debug level to SQLAlchemy's options"
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'sql_connection_debug'
op|'>='
number|'100'
op|':'
newline|'\n'
indent|'            '
name|'engine_args'
op|'['
string|"'echo'"
op|']'
op|'='
string|"'debug'"
newline|'\n'
dedent|''
name|'elif'
name|'FLAGS'
op|'.'
name|'sql_connection_debug'
op|'>='
number|'50'
op|':'
newline|'\n'
indent|'            '
name|'engine_args'
op|'['
string|"'echo'"
op|']'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|'"sqlite"'
name|'in'
name|'connection_dict'
op|'.'
name|'drivername'
op|':'
newline|'\n'
indent|'            '
name|'engine_args'
op|'['
string|'"poolclass"'
op|']'
op|'='
name|'NullPool'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'                '
name|'engine_args'
op|'['
string|'"poolclass"'
op|']'
op|'='
name|'StaticPool'
newline|'\n'
name|'engine_args'
op|'['
string|'"connect_args"'
op|']'
op|'='
op|'{'
string|"'check_same_thread'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'sqlite_synchronous'
op|':'
newline|'\n'
indent|'                '
name|'engine_args'
op|'['
string|'"listeners"'
op|']'
op|'='
op|'['
name|'SynchronousSwitchListener'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'mysql'"
name|'in'
name|'connection_dict'
op|'.'
name|'drivername'
op|':'
newline|'\n'
indent|'            '
name|'engine_args'
op|'['
string|"'listeners'"
op|']'
op|'='
op|'['
name|'MySQLPingListener'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'_ENGINE'
op|'='
name|'sqlalchemy'
op|'.'
name|'create_engine'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
op|'**'
name|'engine_args'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_ENGINE'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_maker
dedent|''
name|'def'
name|'get_maker'
op|'('
name|'engine'
op|','
name|'autocommit'
op|'='
name|'True'
op|','
name|'expire_on_commit'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a SQLAlchemy sessionmaker using the given engine."""'
newline|'\n'
name|'return'
name|'sqlalchemy'
op|'.'
name|'orm'
op|'.'
name|'sessionmaker'
op|'('
name|'bind'
op|'='
name|'engine'
op|','
nl|'\n'
name|'autocommit'
op|'='
name|'autocommit'
op|','
nl|'\n'
name|'expire_on_commit'
op|'='
name|'expire_on_commit'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
