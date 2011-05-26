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
string|'"""Database setup and migration commands."""'
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
name|'utils'
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
name|'DECLARE'
op|'('
string|"'db_backend'"
op|','
string|"'nova.db.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|IMPL
name|'IMPL'
op|'='
name|'utils'
op|'.'
name|'LazyPluggable'
op|'('
name|'FLAGS'
op|'['
string|"'db_backend'"
op|']'
op|','
nl|'\n'
DECL|variable|sqlalchemy
name|'sqlalchemy'
op|'='
string|"'nova.db.sqlalchemy.migration'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_sync
name|'def'
name|'db_sync'
op|'('
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Migrate the database to `version` or the most recent version."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'db_sync'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_version
dedent|''
name|'def'
name|'db_version'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Display the current database version."""'
newline|'\n'
name|'return'
name|'IMPL'
op|'.'
name|'db_version'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
