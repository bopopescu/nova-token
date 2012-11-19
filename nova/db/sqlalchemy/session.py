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
string|'"""Session Handling for SQLAlchemy backend.\n\nRecommended ways to use sessions within this framework:\n\n* Don\'t use them explicitly; this is like running with AUTOCOMMIT=1.\n  model_query() will implicitly use a session when called without one\n  supplied. This is the ideal situation because it will allow queries\n  to be automatically retried if the database connection is interrupted.\n\n    Note: Automatic retry will be enabled in a future patch.\n\n  It is generally fine to issue several queries in a row like this. Even though\n  they may be run in separate transactions and/or separate sessions, each one\n  will see the data from the prior calls. If needed, undo- or rollback-like\n  functionality should be handled at a logical level. For an example, look at\n  the code around quotas and reservation_rollback().\n\n  Examples:\n\n    def get_foo(context, foo):\n        return model_query(context, models.Foo).\\\n                filter_by(foo=foo).\\\n                first()\n\n    def update_foo(context, id, newfoo):\n        model_query(context, models.Foo).\\\n                filter_by(id=id).\\\n                update({\'foo\': newfoo})\n\n    def create_foo(context, values):\n        foo_ref = models.Foo()\n        foo_ref.update(values)\n        foo_ref.save()\n        return foo_ref\n\n\n* Within the scope of a single method, keeping all the reads and writes within\n  the context managed by a single session. In this way, the session\'s __exit__\n  handler will take care of calling flush() and commit() for you.\n  If using this approach, you should not explicitly call flush() or commit().\n  Any error within the context of the session will cause the session to emit\n  a ROLLBACK. If the connection is dropped before this is possible, the\n  database will implicitly rollback the transaction.\n\n     Note: statements in the session scope will not be automatically retried.\n\n  If you create models within the session, they need to be added, but you\n  do not need to call model.save()\n\n    def create_many_foo(context, foos):\n        session = get_session()\n        with session.begin():\n            for foo in foos:\n                foo_ref = models.Foo()\n                foo_ref.update(foo)\n                session.add(foo_ref)\n\n    def update_bar(context, foo_id, newbar):\n        session = get_session()\n        with session.begin():\n            foo_ref = model_query(context, models.Foo, session).\\\n                        filter_by(id=foo_id).\\\n                        first()\n            model_query(context, models.Bar, session).\\\n                        filter_by(id=foo_ref[\'bar_id\']).\\\n                        update({\'bar\': newbar})\n\n  Note: update_bar is a trivially simple example of using "with session.begin".\n  Whereas create_many_foo is a good example of when a transaction is needed,\n  it is always best to use as few queries as possible. The two queries in\n  update_bar can be better expressed using a single query which avoids\n  the need for an explicit transaction. It can be expressed like so:\n\n    def update_bar(context, foo_id, newbar):\n        subq = model_query(context, models.Foo.id).\\\n                filter_by(id=foo_id).\\\n                limit(1).\\\n                subquery()\n        model_query(context, models.Bar).\\\n                filter_by(id=subq.as_scalar()).\\\n                update({\'bar\': newbar})\n\n  For reference, this emits approximagely the following SQL statement:\n\n    UPDATE bar SET bar = ${newbar}\n        WHERE id=(SELECT bar_id FROM foo WHERE id = ${foo_id} LIMIT 1);\n\n* Passing an active session between methods. Sessions should only be passed\n  to private methods. The private method must use a subtransaction; otherwise\n  SQLAlchemy will throw an error when you call session.begin() on an existing\n  transaction. Public methods should not accept a session parameter and should\n  not be involved in sessions within the caller\'s scope.\n\n  Note that this incurs more overhead in SQLAlchemy than the above means\n  due to nesting transactions, and it is not possible to implicitly retry\n  failed database operations when using this approach.\n\n  This also makes code somewhat more difficult to read and debug, because a\n  single database transaction spans more than one method. Error handling\n  becomes less clear in this situation. When this is needed for code clarity,\n  it should be clearly documented.\n\n    def myfunc(foo):\n        session = get_session()\n        with session.begin():\n            # do some database things\n            bar = _private_func(foo, session)\n        return bar\n\n    def _private_func(foo, session=None):\n        if not session:\n            session = get_session()\n        with session.begin(subtransaction=True):\n            # do some other database things\n        return bar\n\n\nThere are some things which it is best to avoid:\n\n* Don\'t keep a transaction open any longer than necessary.\n\n  This means that your "with session.begin()" block should be as short\n  as possible, while still containing all the related calls for that\n  transaction.\n\n* Avoid "with_lockmode(\'UPDATE\')" when possible.\n\n  In MySQL/InnoDB, when a "SELECT ... FOR UPDATE" query does not match\n  any rows, it will take a gap-lock. This is a form of write-lock on the\n  "gap" where no rows exist, and prevents any other writes to that space.\n  This can effectively prevent any INSERT into a table by locking the gap\n  at the end of the index. Similar problems will occur if the SELECT FOR UPDATE\n  has an overly broad WHERE clause, or doesn\'t properly use an index.\n\n  One idea proposed at ODS Fall \'12 was to use a normal SELECT to test the\n  number of rows matching a query, and if only one row is returned,\n  then issue the SELECT FOR UPDATE.\n\n  The better long-term solution is to use INSERT .. ON DUPLICATE KEY UPDATE.\n  However, this can not be done until the "deleted" columns are removed and\n  proper UNIQUE constraints are added to the tables.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'exc'
name|'import'
name|'DisconnectionError'
op|','
name|'OperationalError'
newline|'\n'
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
name|'pool'
name|'import'
name|'NullPool'
op|','
name|'StaticPool'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
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
op|'='
name|'wrap_session'
op|'('
name|'session'
op|')'
newline|'\n'
name|'return'
name|'session'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_session
dedent|''
name|'def'
name|'wrap_session'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a session whose exceptions are wrapped."""'
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
DECL|function|get_engine
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
name|'_ENGINE'
op|'='
name|'create_engine'
op|'('
name|'CONF'
op|'.'
name|'sql_connection'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_ENGINE'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|synchronous_switch_listener
dedent|''
name|'def'
name|'synchronous_switch_listener'
op|'('
name|'dbapi_conn'
op|','
name|'connection_rec'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Switch sqlite connections to non-synchronous mode"""'
newline|'\n'
name|'dbapi_conn'
op|'.'
name|'execute'
op|'('
string|'"PRAGMA synchronous = OFF"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_regexp_listener
dedent|''
name|'def'
name|'add_regexp_listener'
op|'('
name|'dbapi_con'
op|','
name|'con_record'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add REGEXP function to sqlite connections."""'
newline|'\n'
nl|'\n'
DECL|function|regexp
name|'def'
name|'regexp'
op|'('
name|'expr'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'reg'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
name|'expr'
op|')'
newline|'\n'
name|'return'
name|'reg'
op|'.'
name|'search'
op|'('
name|'unicode'
op|'('
name|'item'
op|')'
op|')'
name|'is'
name|'not'
name|'None'
newline|'\n'
dedent|''
name|'dbapi_con'
op|'.'
name|'create_function'
op|'('
string|"'regexp'"
op|','
number|'2'
op|','
name|'regexp'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|greenthread_yield
dedent|''
name|'def'
name|'greenthread_yield'
op|'('
name|'dbapi_con'
op|','
name|'con_record'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Ensure other greenthreads get a chance to execute by forcing a context\n    switch. With common database backends (eg MySQLdb and sqlite), there is\n    no implicit yield caused by network I/O since they are implemented by\n    C libraries that eventlet cannot monkey patch.\n    """'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ping_listener
dedent|''
name|'def'
name|'ping_listener'
op|'('
name|'dbapi_conn'
op|','
name|'connection_rec'
op|','
name|'connection_proxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Ensures that MySQL connections checked out of the\n    pool are alive.\n\n    Borrowed from:\n    http://groups.google.com/group/sqlalchemy/msg/a4ce563d802c929f\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'dbapi_conn'
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
name|'dbapi_conn'
op|'.'
name|'OperationalError'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'        '
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
indent|'            '
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
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_db_connection_error
dedent|''
dedent|''
dedent|''
name|'def'
name|'is_db_connection_error'
op|'('
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return True if error in connecting to db."""'
newline|'\n'
comment|'# NOTE(adam_g): This is currently MySQL specific and needs to be extended'
nl|'\n'
comment|'#               to support Postgres and others.'
nl|'\n'
name|'conn_err_codes'
op|'='
op|'('
string|"'2002'"
op|','
string|"'2003'"
op|','
string|"'2006'"
op|')'
newline|'\n'
name|'for'
name|'err_code'
name|'in'
name|'conn_err_codes'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'args'
op|'.'
name|'find'
op|'('
name|'err_code'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_engine
dedent|''
name|'def'
name|'create_engine'
op|'('
name|'sql_connection'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a new SQLAlchemy engine."""'
newline|'\n'
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
name|'CONF'
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
name|'if'
name|'CONF'
op|'.'
name|'sql_pool_size'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'engine_args'
op|'['
string|"'pool_size'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'sql_pool_size'
newline|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'sql_max_overflow'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'engine_args'
op|'['
string|"'max_overflow'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'sql_max_overflow'
newline|'\n'
nl|'\n'
comment|"# Map our SQL debug level to SQLAlchemy's options"
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'sql_connection_debug'
op|'>='
number|'100'
op|':'
newline|'\n'
indent|'        '
name|'engine_args'
op|'['
string|"'echo'"
op|']'
op|'='
string|"'debug'"
newline|'\n'
dedent|''
name|'elif'
name|'CONF'
op|'.'
name|'sql_connection_debug'
op|'>='
number|'50'
op|':'
newline|'\n'
indent|'        '
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
indent|'        '
name|'engine_args'
op|'['
string|'"poolclass"'
op|']'
op|'='
name|'NullPool'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'            '
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
dedent|''
name|'engine'
op|'='
name|'sqlalchemy'
op|'.'
name|'create_engine'
op|'('
name|'sql_connection'
op|','
op|'**'
name|'engine_args'
op|')'
newline|'\n'
nl|'\n'
name|'sqlalchemy'
op|'.'
name|'event'
op|'.'
name|'listen'
op|'('
name|'engine'
op|','
string|"'checkin'"
op|','
name|'greenthread_yield'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'mysql'"
name|'in'
name|'connection_dict'
op|'.'
name|'drivername'
op|':'
newline|'\n'
indent|'        '
name|'sqlalchemy'
op|'.'
name|'event'
op|'.'
name|'listen'
op|'('
name|'engine'
op|','
string|"'checkout'"
op|','
name|'ping_listener'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'sqlite'"
name|'in'
name|'connection_dict'
op|'.'
name|'drivername'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'sqlite_synchronous'
op|':'
newline|'\n'
indent|'            '
name|'sqlalchemy'
op|'.'
name|'event'
op|'.'
name|'listen'
op|'('
name|'engine'
op|','
string|"'connect'"
op|','
nl|'\n'
name|'synchronous_switch_listener'
op|')'
newline|'\n'
dedent|''
name|'sqlalchemy'
op|'.'
name|'event'
op|'.'
name|'listen'
op|'('
name|'engine'
op|','
string|"'connect'"
op|','
name|'add_regexp_listener'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'CONF'
op|'.'
name|'sql_connection_trace'
name|'and'
nl|'\n'
name|'engine'
op|'.'
name|'dialect'
op|'.'
name|'dbapi'
op|'.'
name|'__name__'
op|'=='
string|"'MySQLdb'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'import'
name|'MySQLdb'
op|'.'
name|'cursors'
newline|'\n'
name|'_do_query'
op|'='
name|'debug_mysql_do_query'
op|'('
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'MySQLdb'
op|'.'
name|'cursors'
op|'.'
name|'BaseCursor'
op|','
string|"'_do_query'"
op|','
name|'_do_query'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OperationalError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'is_db_connection_error'
op|'('
name|'e'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'remaining'
op|'='
name|'CONF'
op|'.'
name|'sql_max_retries'
newline|'\n'
name|'if'
name|'remaining'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'remaining'
op|'='
string|"'infinite'"
newline|'\n'
dedent|''
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'SQL connection failed. %s attempts left.'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'msg'
op|'%'
name|'remaining'
op|')'
newline|'\n'
name|'if'
name|'remaining'
op|'!='
string|"'infinite'"
op|':'
newline|'\n'
indent|'                '
name|'remaining'
op|'-='
number|'1'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'sql_retry_interval'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'OperationalError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
op|'('
name|'remaining'
op|'!='
string|"'infinite'"
name|'and'
name|'remaining'
op|'=='
number|'0'
op|')'
name|'or'
name|'not'
name|'is_db_connection_error'
op|'('
name|'e'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'engine'
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
nl|'\n'
nl|'\n'
DECL|function|debug_mysql_do_query
dedent|''
name|'def'
name|'debug_mysql_do_query'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a debug version of MySQLdb.cursors._do_query"""'
newline|'\n'
name|'import'
name|'MySQLdb'
op|'.'
name|'cursors'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'old_mysql_do_query'
op|'='
name|'MySQLdb'
op|'.'
name|'cursors'
op|'.'
name|'BaseCursor'
op|'.'
name|'_do_query'
newline|'\n'
nl|'\n'
DECL|function|_do_query
name|'def'
name|'_do_query'
op|'('
name|'self'
op|','
name|'q'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stack'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'file'
op|','
name|'line'
op|','
name|'method'
op|','
name|'function'
name|'in'
name|'traceback'
op|'.'
name|'extract_stack'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# exclude various common things from trace'
nl|'\n'
indent|'            '
name|'if'
name|'file'
op|'.'
name|'endswith'
op|'('
string|"'session.py'"
op|')'
name|'and'
name|'method'
op|'=='
string|"'_do_query'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'file'
op|'.'
name|'endswith'
op|'('
string|"'api.py'"
op|')'
name|'and'
name|'method'
op|'=='
string|"'wrapper'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'file'
op|'.'
name|'endswith'
op|'('
string|"'utils.py'"
op|')'
name|'and'
name|'method'
op|'=='
string|"'_inner'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'file'
op|'.'
name|'endswith'
op|'('
string|"'exception.py'"
op|')'
name|'and'
name|'method'
op|'=='
string|"'_wrap'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
comment|'# nova/db/api is just a wrapper around nova/db/sqlalchemy/api'
nl|'\n'
dedent|''
name|'if'
name|'file'
op|'.'
name|'endswith'
op|'('
string|"'nova/db/api.py'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
comment|'# only trace inside nova'
nl|'\n'
dedent|''
name|'index'
op|'='
name|'file'
op|'.'
name|'rfind'
op|'('
string|"'nova'"
op|')'
newline|'\n'
name|'if'
name|'index'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'stack'
op|'+='
string|'"File:%s:%s Method:%s() Line:%s | "'
op|'%'
op|'('
name|'file'
op|'['
name|'index'
op|':'
op|']'
op|','
name|'line'
op|','
name|'method'
op|','
name|'function'
op|')'
newline|'\n'
nl|'\n'
comment|'# strip trailing " | " from stack'
nl|'\n'
dedent|''
name|'if'
name|'stack'
op|':'
newline|'\n'
indent|'            '
name|'stack'
op|'='
name|'stack'
op|'['
op|':'
op|'-'
number|'3'
op|']'
newline|'\n'
name|'qq'
op|'='
string|'"%s /* %s */"'
op|'%'
op|'('
name|'q'
op|','
name|'stack'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'qq'
op|'='
name|'q'
newline|'\n'
dedent|''
name|'old_mysql_do_query'
op|'('
name|'self'
op|','
name|'qq'
op|')'
newline|'\n'
nl|'\n'
comment|'# return the new _do_query method'
nl|'\n'
dedent|''
name|'return'
name|'_do_query'
newline|'\n'
dedent|''
endmarker|''
end_unit
