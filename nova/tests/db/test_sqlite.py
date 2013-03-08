begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""Test cases for sqlite-specific logic"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'create_engine'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
op|','
name|'BigInteger'
op|','
name|'String'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'ext'
op|'.'
name|'declarative'
name|'import'
name|'declarative_base'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSqlite
name|'class'
name|'TestSqlite'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests for sqlite-specific logic."""'
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
name|'TestSqlite'
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
name|'db_file'
op|'='
string|'"test_bigint.sqlite"'
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
name|'db_file'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
name|'self'
op|'.'
name|'db_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_big_int_mapping
dedent|''
dedent|''
name|'def'
name|'test_big_int_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_class'
op|'='
name|'declarative_base'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|User
name|'class'
name|'User'
op|'('
name|'base_class'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Dummy class with a BigInteger column for testing."""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|'"users"'
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'BigInteger'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
name|'Column'
op|'('
name|'String'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'get_schema_cmd'
op|'='
string|'"sqlite3 %s \'.schema\'"'
op|'%'
name|'self'
op|'.'
name|'db_file'
newline|'\n'
name|'engine'
op|'='
name|'create_engine'
op|'('
string|'"sqlite:///%s"'
op|'%'
name|'self'
op|'.'
name|'db_file'
op|')'
newline|'\n'
name|'base_class'
op|'.'
name|'metadata'
op|'.'
name|'create_all'
op|'('
name|'engine'
op|')'
newline|'\n'
name|'process'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'get_schema_cmd'
op|','
name|'shell'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|stdout
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|')'
newline|'\n'
name|'output'
op|','
name|'_'
op|'='
name|'process'
op|'.'
name|'communicate'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'BIGINT'"
name|'in'
name|'output'
op|','
name|'msg'
op|'='
string|'"column type BIGINT "'
nl|'\n'
string|'"not converted to INTEGER in schema"'
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
indent|'        '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'db_file'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
name|'self'
op|'.'
name|'db_file'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'TestSqlite'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
