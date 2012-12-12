begin_unit
comment|'#    Copyright 2012 IBM Corp.'
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
string|'"""Tests for the conductor service"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'api'
name|'as'
name|'conductor_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'manager'
name|'as'
name|'conductor_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'rpcapi'
name|'as'
name|'conductor_rpcapi'
newline|'\n'
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
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
name|'as'
name|'exc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_IMAGE_REF
name|'FAKE_IMAGE_REF'
op|'='
string|"'fake-image-ref'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_BaseTestCase
name|'class'
name|'_BaseTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'_BaseTestCase'
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
name|'db'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stub_out_client_exceptions
dedent|''
name|'def'
name|'stub_out_client_exceptions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|passthru
indent|'        '
name|'def'
name|'passthru'
op|'('
name|'exceptions'
op|','
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc_common'
op|','
string|"'catch_client_exception'"
op|','
name|'passthru'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_fake_instance
dedent|''
name|'def'
name|'_create_fake_instance'
op|'('
name|'self'
op|','
name|'params'
op|'='
name|'None'
op|','
name|'type_name'
op|'='
string|"'m1.tiny'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'vm_state'"
op|']'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'inst'
op|'['
string|"'image_ref'"
op|']'
op|'='
name|'FAKE_IMAGE_REF'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user_id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project_id'
newline|'\n'
name|'inst'
op|'['
string|"'host'"
op|']'
op|'='
string|"'fake_host'"
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
name|'type_name'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
name|'type_id'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'memory_mb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'root_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'ephemeral_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'architecture'"
op|']'
op|'='
string|"'x86_64'"
newline|'\n'
name|'inst'
op|'['
string|"'os_type'"
op|']'
op|'='
string|"'Linux'"
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_update
dedent|''
name|'def'
name|'_do_update'
op|'('
name|'self'
op|','
name|'instance_uuid'
op|','
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'instance_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_update
dedent|''
name|'def'
name|'test_instance_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'new_inst'
op|'='
name|'self'
op|'.'
name|'_do_update'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'STOPPED'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|','
name|'vm_states'
op|'.'
name|'STOPPED'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'new_inst'
op|'['
string|"'vm_state'"
op|']'
op|','
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_update_invalid_key
dedent|''
name|'def'
name|'test_instance_update_invalid_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): the real DB API call ignores invalid keys'
nl|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'db'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'KeyError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_do_update'
op|','
string|"'any-uuid'"
op|','
name|'foobar'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migration_get
dedent|''
dedent|''
name|'def'
name|'test_migration_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migration'
op|'='
name|'db'
op|'.'
name|'migration_create'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'migrating'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migration'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'migration_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'migration'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migration_update
dedent|''
name|'def'
name|'test_migration_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migration'
op|'='
name|'db'
op|'.'
name|'migration_create'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'migrating'"
op|'}'
op|')'
newline|'\n'
name|'migration_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migration'
op|')'
newline|'\n'
name|'migration'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'migration_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'migration_p'
op|','
nl|'\n'
string|"'finished'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'migration'
op|'['
string|"'status'"
op|']'
op|','
string|"'finished'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_get_by_uuid
dedent|''
name|'def'
name|'test_instance_get_by_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'orig_instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'copy_instance'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'instance_get_by_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'orig_instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'orig_instance'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'copy_instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_get_all_by_host
dedent|''
name|'def'
name|'test_instance_get_all_by_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'orig_instance'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
op|')'
newline|'\n'
name|'all_instances'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'instance_get_all_by_host'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'orig_instance'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'orig_instance'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'all_instances'
op|'['
number|'0'
op|']'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_aggregate_with_host
dedent|''
name|'def'
name|'_setup_aggregate_with_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_ref'
op|'='
name|'db'
op|'.'
name|'aggregate_create'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|','
string|"'availability_zone'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'aggregate_host_add'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'aggregate_ref'
op|','
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
name|'aggregate_ref'
op|'='
name|'db'
op|'.'
name|'aggregate_get'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'aggregate_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'aggregate_ref'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_host_add
dedent|''
name|'def'
name|'test_aggregate_host_add'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_ref'
op|'='
name|'self'
op|'.'
name|'_setup_aggregate_with_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'any'
op|'('
op|'['
name|'host'
op|'=='
string|"'bar'"
nl|'\n'
name|'for'
name|'host'
name|'in'
name|'aggregate_ref'
op|'['
string|"'hosts'"
op|']'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'aggregate_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'aggregate_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_host_delete
dedent|''
name|'def'
name|'test_aggregate_host_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_ref'
op|'='
name|'self'
op|'.'
name|'_setup_aggregate_with_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'aggregate_host_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'aggregate_ref'
op|','
nl|'\n'
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
name|'aggregate_ref'
op|'='
name|'db'
op|'.'
name|'aggregate_get'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'aggregate_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'any'
op|'('
op|'['
name|'host'
op|'=='
string|"'bar'"
nl|'\n'
name|'for'
name|'host'
name|'in'
name|'aggregate_ref'
op|'['
string|"'hosts'"
op|']'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'aggregate_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'aggregate_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bw_usage_update
dedent|''
name|'def'
name|'test_bw_usage_update'
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
string|"'bw_usage_update'"
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
string|"'bw_usage_get'"
op|')'
newline|'\n'
nl|'\n'
name|'update_args'
op|'='
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'uuid'"
op|','
string|"'mac'"
op|','
number|'0'
op|','
number|'10'
op|','
number|'20'
op|','
number|'5'
op|','
number|'10'
op|','
number|'20'
op|')'
newline|'\n'
name|'get_args'
op|'='
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'uuid'"
op|','
number|'0'
op|','
string|"'mac'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'bw_usage_update'
op|'('
op|'*'
name|'update_args'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'bw_usage_get'
op|'('
op|'*'
name|'get_args'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'foo'"
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
name|'result'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'bw_usage_update'
op|'('
op|'*'
name|'update_args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_backdoor_port
dedent|''
name|'def'
name|'test_get_backdoor_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'backdoor_port'
op|'='
number|'59697'
newline|'\n'
nl|'\n'
DECL|function|fake_get_backdoor_port
name|'def'
name|'fake_get_backdoor_port'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'backdoor_port'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'conductor'
op|','
name|'conductor_api'
op|'.'
name|'API'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'conductor_manager'
op|'.'
name|'ConductorManager'
op|','
nl|'\n'
string|"'get_backdoor_port'"
op|','
name|'fake_get_backdoor_port'
op|')'
newline|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'get_backdoor_port'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake_host'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'conductor'
op|','
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'get_backdoor_port'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake_host'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exc'
op|'.'
name|'InvalidRequest'
op|':'
newline|'\n'
indent|'                '
name|'port'
op|'='
name|'backdoor_port'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'conductor'
op|','
name|'conductor_rpcapi'
op|'.'
name|'ConductorAPI'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'conductor_manager'
op|'.'
name|'ConductorManager'
op|','
nl|'\n'
string|"'get_backdoor_port'"
op|','
name|'fake_get_backdoor_port'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'backdoor_port'
op|'='
name|'backdoor_port'
newline|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'get_backdoor_port'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'port'
op|','
name|'backdoor_port'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorTestCase
dedent|''
dedent|''
name|'class'
name|'ConductorTestCase'
op|'('
name|'_BaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Conductor Manager Tests"""'
newline|'\n'
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
name|'ConductorTestCase'
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
name|'conductor'
op|'='
name|'conductor_manager'
op|'.'
name|'ConductorManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out_client_exceptions'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorRPCAPITestCase
dedent|''
dedent|''
name|'class'
name|'ConductorRPCAPITestCase'
op|'('
name|'_BaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Conductor RPC API Tests"""'
newline|'\n'
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
name|'ConductorRPCAPITestCase'
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
name|'conductor_service'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
nl|'\n'
string|"'conductor'"
op|','
name|'manager'
op|'='
string|"'nova.conductor.manager.ConductorManager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conductor'
op|'='
name|'conductor_rpcapi'
op|'.'
name|'ConductorAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorAPITestCase
dedent|''
dedent|''
name|'class'
name|'ConductorAPITestCase'
op|'('
name|'_BaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Conductor API Tests"""'
newline|'\n'
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
name|'ConductorAPITestCase'
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
name|'conductor_service'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
nl|'\n'
string|"'conductor'"
op|','
name|'manager'
op|'='
string|"'nova.conductor.manager.ConductorManager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conductor'
op|'='
name|'conductor_api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_do_update
dedent|''
name|'def'
name|'_do_update'
op|'('
name|'self'
op|','
name|'instance_uuid'
op|','
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): the public API takes actual keyword arguments,'
nl|'\n'
comment|'# so override the base class here to make the call correctly'
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'instance_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
op|'**'
name|'updates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bw_usage_get
dedent|''
name|'def'
name|'test_bw_usage_get'
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
string|"'bw_usage_update'"
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
string|"'bw_usage_get'"
op|')'
newline|'\n'
nl|'\n'
name|'get_args'
op|'='
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'uuid'"
op|','
number|'0'
op|','
string|"'mac'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'bw_usage_get'
op|'('
op|'*'
name|'get_args'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'foo'"
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
name|'result'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'bw_usage_get'
op|'('
op|'*'
name|'get_args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorLocalAPITestCase
dedent|''
dedent|''
name|'class'
name|'ConductorLocalAPITestCase'
op|'('
name|'ConductorAPITestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Conductor LocalAPI Tests"""'
newline|'\n'
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
name|'ConductorLocalAPITestCase'
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
name|'conductor'
op|'='
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
name|'self'
op|'.'
name|'stub_out_client_exceptions'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_client_exceptions
dedent|''
name|'def'
name|'test_client_exceptions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(danms): The LocalAPI should not raise exceptions wrapped'
nl|'\n'
comment|'# in ClientException. KeyError should be raised if an invalid'
nl|'\n'
comment|'# update key is passed, so use that to validate.'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'KeyError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_do_update'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'foo'
op|'='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorImportTest
dedent|''
dedent|''
name|'class'
name|'ConductorImportTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_import_conductor_local
indent|'    '
name|'def'
name|'test_import_conductor_local'
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
name|'use_local'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'conductor'
op|'.'
name|'API'
op|'('
op|')'
op|','
nl|'\n'
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_import_conductor_rpc
dedent|''
name|'def'
name|'test_import_conductor_rpc'
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
name|'use_local'
op|'='
name|'False'
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'conductor'
op|'.'
name|'API'
op|'('
op|')'
op|','
nl|'\n'
name|'conductor_api'
op|'.'
name|'API'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorPolicyTest
dedent|''
dedent|''
name|'class'
name|'ConductorPolicyTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_all_allowed_keys
indent|'    '
name|'def'
name|'test_all_allowed_keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_db_instance_update
indent|'        '
name|'def'
name|'fake_db_instance_update'
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
indent|'            '
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_update_and_get_original'"
op|','
nl|'\n'
name|'fake_db_instance_update'
op|')'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake-user'"
op|','
string|"'fake-project'"
op|')'
newline|'\n'
name|'conductor'
op|'='
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|'('
op|')'
newline|'\n'
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'conductor_manager'
op|'.'
name|'allowed_updates'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'conductor_manager'
op|'.'
name|'datetime_fields'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
string|"'foo'"
newline|'\n'
dedent|''
dedent|''
name|'conductor'
op|'.'
name|'instance_update'
op|'('
name|'ctxt'
op|','
string|"'fake-instance'"
op|','
op|'**'
name|'updates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allowed_keys_are_real
dedent|''
name|'def'
name|'test_allowed_keys_are_real'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'keys'
op|'='
name|'list'
op|'('
name|'conductor_manager'
op|'.'
name|'allowed_updates'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): expected_task_state is a parameter that gets'
nl|'\n'
comment|'# passed to the db layer, but is not actually an instance attribute'
nl|'\n'
name|'del'
name|'keys'
op|'['
name|'keys'
op|'.'
name|'index'
op|'('
string|"'expected_task_state'"
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'instance'
op|','
name|'key'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
