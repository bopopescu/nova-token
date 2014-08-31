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
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'tasks'
name|'import'
name|'live_migrate'
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
name|'scheduler'
name|'import'
name|'utils'
name|'as'
name|'scheduler_utils'
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
name|'fake_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LiveMigrationTaskTestCase
name|'class'
name|'LiveMigrationTaskTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
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
name|'LiveMigrationTaskTestCase'
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
name|'context'
op|'='
string|'"context"'
newline|'\n'
name|'self'
op|'.'
name|'instance_host'
op|'='
string|'"host"'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
string|'"uuid"'
newline|'\n'
name|'self'
op|'.'
name|'instance_image'
op|'='
string|'"image_ref"'
newline|'\n'
name|'db_instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'instance_host'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'power_state'
op|'='
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'image_ref'
op|'='
name|'self'
op|'.'
name|'instance_image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'objects'
op|'.'
name|'Instance'
op|'('
op|')'
op|','
name|'db_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'destination'
op|'='
string|'"destination"'
newline|'\n'
name|'self'
op|'.'
name|'block_migration'
op|'='
string|'"bm"'
newline|'\n'
name|'self'
op|'.'
name|'disk_over_commit'
op|'='
string|'"doc"'
newline|'\n'
name|'self'
op|'.'
name|'_generate_task'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_generate_task
dedent|''
name|'def'
name|'_generate_task'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'task'
op|'='
name|'live_migrate'
op|'.'
name|'LiveMigrationTask'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'destination'
op|','
name|'self'
op|'.'
name|'block_migration'
op|','
nl|'\n'
name|'self'
op|'.'
name|'disk_over_commit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_execute_with_destination
dedent|''
name|'def'
name|'test_execute_with_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_check_host_is_up'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_check_requested_destination'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'compute_rpcapi'
op|','
string|"'live_migration'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_host_is_up'
op|'('
name|'self'
op|'.'
name|'instance_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_requested_destination'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'live_migration'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'instance_host'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'dest'
op|'='
name|'self'
op|'.'
name|'destination'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'self'
op|'.'
name|'block_migration'
op|','
nl|'\n'
name|'migrate_data'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"bob"'
op|')'
newline|'\n'
nl|'\n'
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
string|'"bob"'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'execute'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_execute_without_destination
dedent|''
name|'def'
name|'test_execute_without_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'destination'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_generate_task'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'destination'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_check_host_is_up'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_find_destination'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'compute_rpcapi'
op|','
string|"'live_migration'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_host_is_up'
op|'('
name|'self'
op|'.'
name|'instance_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_find_destination'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"found_host"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'live_migration'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'instance_host'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'dest'
op|'='
string|'"found_host"'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'self'
op|'.'
name|'block_migration'
op|','
nl|'\n'
name|'migrate_data'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"bob"'
op|')'
newline|'\n'
nl|'\n'
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
string|'"bob"'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'execute'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_instance_is_running_passes
dedent|''
name|'def'
name|'test_check_instance_is_running_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_instance_is_running'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_instance_is_running_fails_when_shutdown
dedent|''
name|'def'
name|'test_check_instance_is_running_fails_when_shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'task'
op|'.'
name|'instance'
op|'['
string|"'power_state'"
op|']'
op|'='
name|'power_state'
op|'.'
name|'SHUTDOWN'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceNotRunning'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_instance_is_running'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_instance_host_is_up
dedent|''
name|'def'
name|'test_check_instance_host_is_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'servicegroup_api'
op|','
string|"'service_is_up'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|'"host"'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"service"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
string|'"service"'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
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
name|'task'
op|'.'
name|'_check_host_is_up'
op|'('
string|'"host"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_instance_host_is_up_fails_if_not_up
dedent|''
name|'def'
name|'test_check_instance_host_is_up_fails_if_not_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'servicegroup_api'
op|','
string|"'service_is_up'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|'"host"'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"service"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
string|'"service"'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_host_is_up'
op|','
string|'"host"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_instance_host_is_up_fails_if_not_found
dedent|''
name|'def'
name|'test_check_instance_host_is_up_fails_if_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|'"host"'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_host_is_up'
op|','
string|'"host"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_requested_destination
dedent|''
name|'def'
name|'test_check_requested_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_get_compute_info'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'servicegroup_api'
op|','
string|"'service_is_up'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'compute_rpcapi'
op|','
nl|'\n'
string|"'check_can_live_migrate_destination'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'destination'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"service"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
string|'"service"'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'hypervisor_details'
op|'='
op|'{'
nl|'\n'
string|'"hypervisor_type"'
op|':'
string|'"a"'
op|','
nl|'\n'
string|'"hypervisor_version"'
op|':'
number|'6.1'
op|','
nl|'\n'
string|'"free_ram_mb"'
op|':'
number|'513'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'hypervisor_details'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'instance_host'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'hypervisor_details'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'hypervisor_details'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'check_can_live_migrate_destination'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'destination'
op|','
nl|'\n'
name|'self'
op|'.'
name|'block_migration'
op|','
name|'self'
op|'.'
name|'disk_over_commit'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|'"migrate_data"'
op|')'
newline|'\n'
nl|'\n'
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
name|'task'
op|'.'
name|'_check_requested_destination'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"migrate_data"'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'migrate_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_requested_destination_fails_with_same_dest
dedent|''
name|'def'
name|'test_check_requested_destination_fails_with_same_dest'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'task'
op|'.'
name|'destination'
op|'='
string|'"same"'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'source'
op|'='
string|'"same"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'UnableToMigrateToSelf'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_requested_destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_requested_destination_fails_when_destination_is_up
dedent|''
name|'def'
name|'test_check_requested_destination_fails_when_destination_is_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'destination'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_requested_destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_requested_destination_fails_with_not_enough_memory
dedent|''
name|'def'
name|'test_check_requested_destination_fails_with_not_enough_memory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_check_host_is_up'"
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
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_host_is_up'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'destination'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
nl|'\n'
string|'"compute_node"'
op|':'
op|'['
op|'{'
string|'"free_ram_mb"'
op|':'
number|'511'
op|'}'
op|']'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'MigrationPreCheckError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_requested_destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_requested_destination_fails_with_hypervisor_diff
dedent|''
name|'def'
name|'test_check_requested_destination_fails_with_hypervisor_diff'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_check_host_is_up'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
nl|'\n'
string|"'_check_destination_has_enough_memory'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_get_compute_info'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_host_is_up'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_destination_has_enough_memory'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'instance_host'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
nl|'\n'
string|'"hypervisor_type"'
op|':'
string|'"b"'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
nl|'\n'
string|'"hypervisor_type"'
op|':'
string|'"a"'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidHypervisorType'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_requested_destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_requested_destination_fails_with_hypervisor_too_old
dedent|''
name|'def'
name|'test_check_requested_destination_fails_with_hypervisor_too_old'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_check_host_is_up'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
nl|'\n'
string|"'_check_destination_has_enough_memory'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_get_compute_info'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_host_is_up'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_destination_has_enough_memory'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'instance_host'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
nl|'\n'
string|'"hypervisor_type"'
op|':'
string|'"a"'
op|','
nl|'\n'
string|'"hypervisor_version"'
op|':'
number|'7'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_get_compute_info'
op|'('
name|'self'
op|'.'
name|'destination'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
nl|'\n'
string|'"hypervisor_type"'
op|':'
string|'"a"'
op|','
nl|'\n'
string|'"hypervisor_version"'
op|':'
number|'6'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_requested_destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_destination_works
dedent|''
name|'def'
name|'test_find_destination_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_utils'
op|','
string|"'get_image_metadata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'scheduler_utils'
op|','
string|"'build_request_spec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|','
nl|'\n'
string|"'select_destinations'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
nl|'\n'
string|"'_check_compatible_with_source_hypervisor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_call_livem_checks_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_utils'
op|'.'
name|'get_image_metadata'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'image_api'
op|','
name|'self'
op|'.'
name|'instance_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"image"'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
string|'"host1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_call_livem_checks_on_host'
op|'('
string|'"host1"'
op|')'
newline|'\n'
nl|'\n'
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
string|'"host1"'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'_find_destination'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_destination_no_image_works
dedent|''
name|'def'
name|'test_find_destination_no_image_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|'='
string|"''"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'scheduler_utils'
op|','
string|"'build_request_spec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|','
nl|'\n'
string|"'select_destinations'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
nl|'\n'
string|"'_check_compatible_with_source_hypervisor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_call_livem_checks_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'None'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
string|'"host1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_call_livem_checks_on_host'
op|'('
string|'"host1"'
op|')'
newline|'\n'
nl|'\n'
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
string|'"host1"'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'_find_destination'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_find_destination_retry_hypervisor_raises
dedent|''
name|'def'
name|'_test_find_destination_retry_hypervisor_raises'
op|'('
name|'self'
op|','
name|'error'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_utils'
op|','
string|"'get_image_metadata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'scheduler_utils'
op|','
string|"'build_request_spec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|','
nl|'\n'
string|"'select_destinations'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
nl|'\n'
string|"'_check_compatible_with_source_hypervisor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_call_livem_checks_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_utils'
op|'.'
name|'get_image_metadata'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'image_api'
op|','
name|'self'
op|'.'
name|'instance_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"image"'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
string|'"host1"'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'error'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'host'"
op|':'
string|"'host2'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
string|'"host2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_call_livem_checks_on_host'
op|'('
string|'"host2"'
op|')'
newline|'\n'
nl|'\n'
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
string|'"host2"'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'_find_destination'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_destination_retry_with_old_hypervisor
dedent|''
name|'def'
name|'test_find_destination_retry_with_old_hypervisor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_find_destination_retry_hypervisor_raises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_destination_retry_with_invalid_hypervisor_type
dedent|''
name|'def'
name|'test_find_destination_retry_with_invalid_hypervisor_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_find_destination_retry_hypervisor_raises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InvalidHypervisorType'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_destination_retry_with_invalid_livem_checks
dedent|''
name|'def'
name|'test_find_destination_retry_with_invalid_livem_checks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'migrate_max_retries'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_utils'
op|','
string|"'get_image_metadata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'scheduler_utils'
op|','
string|"'build_request_spec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|','
nl|'\n'
string|"'select_destinations'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
nl|'\n'
string|"'_check_compatible_with_source_hypervisor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
string|"'_call_livem_checks_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_utils'
op|'.'
name|'get_image_metadata'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'image_api'
op|','
name|'self'
op|'.'
name|'instance_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"image"'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
string|'"host1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_call_livem_checks_on_host'
op|'('
string|'"host1"'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'host'"
op|':'
string|"'host2'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
string|'"host2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_call_livem_checks_on_host'
op|'('
string|'"host2"'
op|')'
newline|'\n'
nl|'\n'
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
string|'"host2"'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'_find_destination'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_destination_retry_exceeds_max
dedent|''
name|'def'
name|'test_find_destination_retry_exceeds_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'migrate_max_retries'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_utils'
op|','
string|"'get_image_metadata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'scheduler_utils'
op|','
string|"'build_request_spec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|','
nl|'\n'
string|"'select_destinations'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|','
nl|'\n'
string|"'_check_compatible_with_source_hypervisor'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_utils'
op|'.'
name|'get_image_metadata'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'image_api'
op|','
name|'self'
op|'.'
name|'instance_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"image"'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'_check_compatible_with_source_hypervisor'
op|'('
string|'"host1"'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'_find_destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_destination_when_runs_out_of_hosts
dedent|''
name|'def'
name|'test_find_destination_when_runs_out_of_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_utils'
op|','
string|"'get_image_metadata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'scheduler_utils'
op|','
string|"'build_request_spec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|','
nl|'\n'
string|"'select_destinations'"
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'get_image_metadata'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'image_api'
op|','
name|'self'
op|'.'
name|'instance_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"image"'
op|')'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'task'
op|'.'
name|'scheduler_client'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'_find_destination'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_implemented_rollback
dedent|''
name|'def'
name|'test_not_implemented_rollback'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
name|'self'
op|'.'
name|'task'
op|'.'
name|'rollback'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
