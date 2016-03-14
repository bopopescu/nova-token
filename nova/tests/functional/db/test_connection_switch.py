begin_unit
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
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'uuidutils'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fixtures'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConnectionSwitchTestCase
name|'class'
name|'ConnectionSwitchTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|test_filename
indent|'    '
name|'test_filename'
op|'='
string|"'foo.db'"
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
name|'ConnectionSwitchTestCase'
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
name|'self'
op|'.'
name|'cleanup'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cleanup
dedent|''
name|'def'
name|'cleanup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
name|'self'
op|'.'
name|'test_filename'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_connection_switch
dedent|''
dedent|''
name|'def'
name|'test_connection_switch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Use a file-based sqlite database so data will persist across new'
nl|'\n'
comment|'# connections'
nl|'\n'
indent|'        '
name|'fake_conn'
op|'='
string|"'sqlite:///'"
op|'+'
name|'self'
op|'.'
name|'test_filename'
newline|'\n'
nl|'\n'
comment|"# The 'main' database connection will stay open, so in-memory is fine"
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
string|"'main'"
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
name|'connection'
op|'='
name|'fake_conn'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make a request context with a cell mapping'
nl|'\n'
name|'mapping'
op|'='
name|'objects'
op|'.'
name|'CellMapping'
op|'('
name|'database_connection'
op|'='
name|'fake_conn'
op|')'
newline|'\n'
comment|'# In the tests, the admin context is required in order to read'
nl|'\n'
comment|'# an Instance back after write, for some reason'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
comment|'# Create an instance in the cell database'
nl|'\n'
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'with'
name|'context'
op|'.'
name|'target_cell'
op|'('
name|'ctxt'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'ctxt'
op|','
name|'uuid'
op|'='
name|'uuid'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Verify the instance is found in the cell database'
nl|'\n'
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'uuid'
op|','
name|'inst'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
comment|"# Verify the instance isn't found in the main database"
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|','
name|'ctxt'
op|','
name|'uuid'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit