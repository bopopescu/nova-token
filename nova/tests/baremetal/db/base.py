begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""Bare-metal DB test base class."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'migration'
name|'as'
name|'bm_migration'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'session'
name|'as'
name|'bm_session'
newline|'\n'
nl|'\n'
DECL|variable|_DB_CACHE
name|'_DB_CACHE'
op|'='
name|'None'
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
name|'import_opt'
op|'('
string|"'sql_connection'"
op|','
nl|'\n'
string|"'nova.virt.baremetal.db.sqlalchemy.session'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Database
name|'class'
name|'Database'
op|'('
name|'test'
op|'.'
name|'Database'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|post_migrations
indent|'    '
name|'def'
name|'post_migrations'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BMDBTestCase
dedent|''
dedent|''
name|'class'
name|'BMDBTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'super'
op|'('
name|'BMDBTestCase'
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
name|'flags'
op|'('
name|'sql_connection'
op|'='
string|"'sqlite://'"
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
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
name|'bm_session'
op|','
name|'bm_migration'
op|','
nl|'\n'
name|'sql_connection'
op|'='
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'sql_connection'
op|','
nl|'\n'
name|'sqlite_db'
op|'='
name|'None'
op|','
nl|'\n'
name|'sqlite_clean_db'
op|'='
name|'None'
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
name|'self'
op|'.'
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
