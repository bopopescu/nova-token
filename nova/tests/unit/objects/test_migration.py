begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
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
op|'.'
name|'objects'
name|'import'
name|'migration'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'uuidsentinel'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|NOW
name|'NOW'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
name|'microsecond'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_db_migration
name|'def'
name|'fake_db_migration'
op|'('
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'db_instance'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'compute-source'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'compute-dest'"
op|','
nl|'\n'
string|"'source_node'"
op|':'
string|"'node-source'"
op|','
nl|'\n'
string|"'dest_node'"
op|':'
string|"'node-dest'"
op|','
nl|'\n'
string|"'dest_host'"
op|':'
string|"'host-dest'"
op|','
nl|'\n'
string|"'old_instance_type_id'"
op|':'
number|'42'
op|','
nl|'\n'
string|"'new_instance_type_id'"
op|':'
number|'84'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'migrating'"
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'resize'"
op|','
nl|'\n'
string|"'hidden'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_total'"
op|':'
number|'123456'
op|','
nl|'\n'
string|"'memory_processed'"
op|':'
number|'12345'
op|','
nl|'\n'
string|"'memory_remaining'"
op|':'
number|'120000'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'234567'
op|','
nl|'\n'
string|"'disk_processed'"
op|':'
number|'23456'
op|','
nl|'\n'
string|"'disk_remaining'"
op|':'
number|'230000'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'        '
name|'db_instance'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'db_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestMigrationObject
dedent|''
name|'class'
name|'_TestMigrationObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_by_id
indent|'    '
name|'def'
name|'test_get_by_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'migration_get'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'migration_get'
op|'('
name|'ctxt'
op|','
name|'fake_migration'
op|'['
string|"'id'"
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_migration'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'mig'
op|'='
name|'migration'
op|'.'
name|'Migration'
op|'.'
name|'get_by_id'
op|'('
name|'ctxt'
op|','
name|'fake_migration'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mig'
op|','
name|'fake_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_instance_and_status
dedent|''
name|'def'
name|'test_get_by_instance_and_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'migration_get_by_instance_and_status'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'migration_get_by_instance_and_status'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'fake_migration'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'migrating'"
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_migration'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'mig'
op|'='
name|'migration'
op|'.'
name|'Migration'
op|'.'
name|'get_by_instance_and_status'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'fake_migration'
op|'['
string|"'id'"
op|']'
op|','
string|"'migrating'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mig'
op|','
name|'fake_migration'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.migration_get_in_progress_by_instance'"
op|')'
newline|'\n'
DECL|member|test_get_in_progress_by_instance
name|'def'
name|'test_get_in_progress_by_instance'
op|'('
name|'self'
op|','
name|'m_get_mig'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'db_migrations'
op|'='
op|'['
name|'fake_migration'
op|','
name|'dict'
op|'('
name|'fake_migration'
op|','
name|'id'
op|'='
number|'456'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'m_get_mig'
op|'.'
name|'return_value'
op|'='
name|'db_migrations'
newline|'\n'
name|'migrations'
op|'='
name|'migration'
op|'.'
name|'MigrationList'
op|'.'
name|'get_in_progress_by_instance'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'fake_migration'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'migrations'
op|')'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'db_migration'
name|'in'
name|'enumerate'
op|'('
name|'db_migrations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'migrations'
op|'['
name|'index'
op|']'
op|','
name|'db_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'migration_create'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'migration_create'
op|'('
name|'ctxt'
op|','
op|'{'
string|"'source_compute'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'resize'"
op|'}'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_migration'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'mig'
op|'='
name|'migration'
op|'.'
name|'Migration'
op|'('
name|'context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'mig'
op|'.'
name|'source_compute'
op|'='
string|"'foo'"
newline|'\n'
name|'mig'
op|'.'
name|'migration_type'
op|'='
string|"'resize'"
newline|'\n'
name|'mig'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_migration'
op|'['
string|"'dest_compute'"
op|']'
op|','
name|'mig'
op|'.'
name|'dest_compute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_recreate_fails
dedent|''
name|'def'
name|'test_recreate_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'migration_create'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'migration_create'
op|'('
name|'ctxt'
op|','
op|'{'
string|"'source_compute'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'resize'"
op|'}'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_migration'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'mig'
op|'='
name|'migration'
op|'.'
name|'Migration'
op|'('
name|'context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'mig'
op|'.'
name|'source_compute'
op|'='
string|"'foo'"
newline|'\n'
name|'mig'
op|'.'
name|'migration_type'
op|'='
string|"'resize'"
newline|'\n'
name|'mig'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'mig'
op|'.'
name|'create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_fails_migration_type
dedent|''
name|'def'
name|'test_create_fails_migration_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'migration_create'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'mig'
op|'='
name|'migration'
op|'.'
name|'Migration'
op|'('
name|'context'
op|'='
name|'ctxt'
op|','
nl|'\n'
name|'old_instance_type_id'
op|'='
number|'42'
op|','
nl|'\n'
name|'new_instance_type_id'
op|'='
number|'84'
op|')'
newline|'\n'
name|'mig'
op|'.'
name|'source_compute'
op|'='
string|"'foo'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'mig'
op|'.'
name|'create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save
dedent|''
name|'def'
name|'test_save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'migration_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'migration_update'
op|'('
name|'ctxt'
op|','
number|'123'
op|','
op|'{'
string|"'source_compute'"
op|':'
string|"'foo'"
op|'}'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_migration'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'mig'
op|'='
name|'migration'
op|'.'
name|'Migration'
op|'('
name|'context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'mig'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'mig'
op|'.'
name|'source_compute'
op|'='
string|"'foo'"
newline|'\n'
name|'mig'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_migration'
op|'['
string|"'dest_compute'"
op|']'
op|','
name|'mig'
op|'.'
name|'dest_compute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance
dedent|''
name|'def'
name|'test_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'fake_inst'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'fake_migration'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'info_cache'"
op|','
nl|'\n'
string|"'security_groups'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_inst'
op|')'
newline|'\n'
name|'mig'
op|'='
name|'migration'
op|'.'
name|'Migration'
op|'.'
name|'_from_db_object'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'migration'
op|'.'
name|'Migration'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_migration'
op|')'
newline|'\n'
name|'mig'
op|'.'
name|'_context'
op|'='
name|'ctxt'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mig'
op|'.'
name|'instance'
op|'.'
name|'host'
op|','
name|'fake_inst'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_setter
dedent|''
name|'def'
name|'test_instance_setter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migration'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'('
name|'instance_uuid'
op|'='
name|'uuidsentinel'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'uuid'
op|'='
name|'uuidsentinel'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Instance.get_by_uuid'"
op|')'
name|'as'
name|'mock_get'
op|':'
newline|'\n'
indent|'            '
name|'migration'
op|'.'
name|'instance'
op|'='
name|'inst'
newline|'\n'
name|'migration'
op|'.'
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_get'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|','
name|'migration'
op|'.'
name|'_cached_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst'
op|','
name|'migration'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_unconfirmed_by_dest_compute
dedent|''
name|'def'
name|'test_get_unconfirmed_by_dest_compute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'db_migrations'
op|'='
op|'['
name|'fake_migration'
op|','
name|'dict'
op|'('
name|'fake_migration'
op|','
name|'id'
op|'='
number|'456'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'db'
op|','
string|"'migration_get_unconfirmed_by_dest_compute'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'migration_get_unconfirmed_by_dest_compute'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'window'"
op|','
string|"'foo'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'db_migrations'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'migrations'
op|'='
op|'('
nl|'\n'
name|'migration'
op|'.'
name|'MigrationList'
op|'.'
name|'get_unconfirmed_by_dest_compute'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'window'"
op|','
string|"'foo'"
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'migrations'
op|')'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'db_migration'
name|'in'
name|'enumerate'
op|'('
name|'db_migrations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'migrations'
op|'['
name|'index'
op|']'
op|','
name|'db_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_in_progress_by_host_and_node
dedent|''
dedent|''
name|'def'
name|'test_get_in_progress_by_host_and_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'db_migrations'
op|'='
op|'['
name|'fake_migration'
op|','
name|'dict'
op|'('
name|'fake_migration'
op|','
name|'id'
op|'='
number|'456'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'db'
op|','
string|"'migration_get_in_progress_by_host_and_node'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'migration_get_in_progress_by_host_and_node'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'host'"
op|','
string|"'node'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'db_migrations'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'migrations'
op|'='
op|'('
nl|'\n'
name|'migration'
op|'.'
name|'MigrationList'
op|'.'
name|'get_in_progress_by_host_and_node'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'host'"
op|','
string|"'node'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'migrations'
op|')'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'db_migration'
name|'in'
name|'enumerate'
op|'('
name|'db_migrations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'migrations'
op|'['
name|'index'
op|']'
op|','
name|'db_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_filters
dedent|''
dedent|''
name|'def'
name|'test_get_by_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'db_migrations'
op|'='
op|'['
name|'fake_migration'
op|','
name|'dict'
op|'('
name|'fake_migration'
op|','
name|'id'
op|'='
number|'456'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'db'
op|','
string|"'migration_get_all_by_filters'"
op|')'
newline|'\n'
name|'filters'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'migration_get_all_by_filters'
op|'('
name|'ctxt'
op|','
name|'filters'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'db_migrations'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'migrations'
op|'='
name|'migration'
op|'.'
name|'MigrationList'
op|'.'
name|'get_by_filters'
op|'('
name|'ctxt'
op|','
name|'filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'migrations'
op|')'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'db_migration'
name|'in'
name|'enumerate'
op|'('
name|'db_migrations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'migrations'
op|'['
name|'index'
op|']'
op|','
name|'db_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_old_resize_record
dedent|''
dedent|''
name|'def'
name|'test_migrate_old_resize_record'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_migration'
op|'='
name|'dict'
op|'('
name|'fake_db_migration'
op|'('
op|')'
op|','
name|'migration_type'
op|'='
name|'None'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.migration_get'"
op|')'
name|'as'
name|'fake_get'
op|':'
newline|'\n'
indent|'            '
name|'fake_get'
op|'.'
name|'return_value'
op|'='
name|'db_migration'
newline|'\n'
name|'mig'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mig'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'migration_type'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'resize'"
op|','
name|'mig'
op|'.'
name|'migration_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_old_migration_record
dedent|''
name|'def'
name|'test_migrate_old_migration_record'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_migration'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'fake_db_migration'
op|'('
op|')'
op|','
name|'migration_type'
op|'='
name|'None'
op|','
nl|'\n'
name|'old_instance_type_id'
op|'='
number|'1'
op|','
name|'new_instance_type_id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.migration_get'"
op|')'
name|'as'
name|'fake_get'
op|':'
newline|'\n'
indent|'            '
name|'fake_get'
op|'.'
name|'return_value'
op|'='
name|'db_migration'
newline|'\n'
name|'mig'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mig'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'migration_type'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'migration'"
op|','
name|'mig'
op|'.'
name|'migration_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_unset_type_resize
dedent|''
name|'def'
name|'test_migrate_unset_type_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mig'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'('
name|'old_instance_type_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'new_instance_type_id'
op|'='
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'resize'"
op|','
name|'mig'
op|'.'
name|'migration_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mig'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'migration_type'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_unset_type_migration
dedent|''
name|'def'
name|'test_migrate_unset_type_migration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mig'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'('
name|'old_instance_type_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'new_instance_type_id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'migration'"
op|','
name|'mig'
op|'.'
name|'migration_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mig'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'migration_type'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.migration_get_by_id_and_instance'"
op|')'
newline|'\n'
DECL|member|test_get_by_id_and_instance
name|'def'
name|'test_get_by_id_and_instance'
op|'('
name|'self'
op|','
name|'fake_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake_migration'
op|'='
name|'fake_db_migration'
op|'('
op|')'
newline|'\n'
name|'fake_get'
op|'.'
name|'return_value'
op|'='
name|'fake_migration'
newline|'\n'
name|'migration'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'.'
name|'get_by_id_and_instance'
op|'('
name|'ctxt'
op|','
string|"'1'"
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'migration'
op|','
name|'fake_migration'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestMigrationObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestMigrationObject
name|'_TestMigrationObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteMigrationObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteMigrationObject
name|'_TestMigrationObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
