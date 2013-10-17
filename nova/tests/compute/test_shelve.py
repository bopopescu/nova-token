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
name|'iso8601'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
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
op|'.'
name|'compute'
name|'import'
name|'task_states'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
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
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'compute'
name|'import'
name|'test_compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
name|'import'
name|'fake'
name|'as'
name|'fake_image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShelveComputeManagerTestCase
name|'class'
name|'ShelveComputeManagerTestCase'
op|'('
name|'test_compute'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_shelve
indent|'    '
name|'def'
name|'test_shelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'db_instance'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'db_instance'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'db_instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
name|'image_id'
op|'='
string|"'fake_image_id'"
newline|'\n'
name|'host'
op|'='
string|"'fake-mini'"
newline|'\n'
name|'cur_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'cur_time'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'SHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'dict'
op|'('
name|'instance'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'cur_time'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_host'"
op|']'
op|'='
name|'host'
newline|'\n'
name|'db_instance'
op|'['
string|"'system_metadata'"
op|']'
op|'='
name|'utils'
op|'.'
name|'dict_to_metadata'
op|'('
name|'sys_meta'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'snapshot'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'power_off'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve.start'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'snapshot'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'fake_image_id'"
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'power_state'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'SHELVED'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'expected_task_state'"
op|':'
op|'['
name|'task_states'
op|'.'
name|'SHELVING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'SHELVING_IMAGE_UPLOADING'
op|']'
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'False'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
op|','
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'db_instance'
op|','
nl|'\n'
name|'db_instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
string|"'shelve.end'"
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
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'shelve_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_volume_backed
dedent|''
name|'def'
name|'test_shelve_volume_backed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_instance'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'db_instance'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'db_instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'SHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'host'
op|'='
string|"'fake-mini'"
newline|'\n'
name|'cur_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'cur_time'
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'dict'
op|'('
name|'instance'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'cur_time'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_image_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_host'"
op|']'
op|'='
name|'host'
newline|'\n'
name|'db_instance'
op|'['
string|"'system_metadata'"
op|']'
op|'='
name|'utils'
op|'.'
name|'dict_to_metadata'
op|'('
name|'sys_meta'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'power_off'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve_offload.start'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'power_state'"
op|':'
number|'123'
op|','
string|"'host'"
op|':'
name|'None'
op|','
string|"'node'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'SHELVED_OFFLOADED'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'expected_task_state'"
op|':'
op|'['
name|'task_states'
op|'.'
name|'SHELVING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'SHELVING_OFFLOADING'
op|']'
op|'}'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'False'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
op|','
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'db_instance'
op|','
name|'db_instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve_offload.end'"
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
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'shelve_offload_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve
dedent|''
name|'def'
name|'test_unshelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_instance'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'db_instance'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'db_instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'UNSHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'image'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake_id'"
op|'}'
newline|'\n'
name|'host'
op|'='
string|"'fake-mini'"
newline|'\n'
name|'cur_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'cur_time_tz'
op|'='
name|'cur_time'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'cur_time'
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'dict'
op|'('
name|'instance'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'cur_time'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_image_id'"
op|']'
op|'='
name|'image'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_host'"
op|']'
op|'='
name|'host'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|','
string|"'_prep_block_device'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'spawn'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'deleted_image_id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|fake_delete
name|'def'
name|'fake_delete'
op|'('
name|'self2'
op|','
name|'ctxt'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'deleted_image_id'
op|'='
name|'image_id'
newline|'\n'
nl|'\n'
dedent|''
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake_image'
op|'.'
name|'_FakeImageService'
op|','
string|"'delete'"
op|','
name|'fake_delete'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.start'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'task_states'
op|'.'
name|'SPAWNING'
op|'}'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'False'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
op|','
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'db_instance'
op|','
name|'db_instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_prep_block_device'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake_bdm'"
op|')'
newline|'\n'
name|'db_instance'
op|'['
string|"'key_data'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'db_instance'
op|'['
string|"'auto_disk_config'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'image'
op|','
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
nl|'\n'
name|'network_info'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'block_device_info'
op|'='
string|"'fake_bdm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'power_state'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'key_data'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'auto_disk_config'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'expected_task_state'"
op|':'
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
string|"'launched_at'"
op|':'
name|'cur_time_tz'
op|'}'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'False'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'db_instance'
op|','
name|'db_instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.end'"
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
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'unshelve_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'image'
op|'='
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'['
string|"'id'"
op|']'
op|','
name|'self'
op|'.'
name|'deleted_image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve_volume_backed
dedent|''
name|'def'
name|'test_unshelve_volume_backed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_instance'
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
name|'host'
op|'='
string|"'fake-mini'"
newline|'\n'
name|'cur_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'cur_time_tz'
op|'='
name|'cur_time'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'cur_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'db_instance'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'db_instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'UNSHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'dict'
op|'('
name|'instance'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'cur_time'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_image_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_host'"
op|']'
op|'='
name|'host'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|','
string|"'_prep_block_device'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'spawn'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
string|"'instance_update_and_get_original'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.start'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'task_states'
op|'.'
name|'SPAWNING'
op|'}'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'False'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'db_instance'
op|','
name|'db_instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_prep_block_device'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
op|'['
op|']'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake_bdm'"
op|')'
newline|'\n'
name|'db_instance'
op|'['
string|"'key_data'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'db_instance'
op|'['
string|"'auto_disk_config'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'None'
op|','
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
nl|'\n'
name|'network_info'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'block_device_info'
op|'='
string|"'fake_bdm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'power_state'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'key_data'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'auto_disk_config'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'expected_task_state'"
op|':'
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
nl|'\n'
string|"'launched_at'"
op|':'
name|'cur_time_tz'
op|'}'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'False'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'db_instance'
op|','
name|'db_instance'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.end'"
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
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'unshelve_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'image'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelved_poll_none_exist
dedent|''
name|'def'
name|'test_shelved_poll_none_exist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'destroy'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'timeutils'
op|','
string|"'is_older_than'"
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_poll_shelved_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelved_poll_not_timedout
dedent|''
name|'def'
name|'test_shelved_poll_not_timedout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'metadata_to_dict'
op|'('
name|'instance'
op|'['
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
name|'shelved_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'shelved_time'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'shelved_time'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'SHELVED'
op|','
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'destroy'"
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_poll_shelved_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelved_poll_timedout
dedent|''
name|'def'
name|'test_shelved_poll_timedout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'active_instance'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'active_instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'metadata_to_dict'
op|'('
name|'instance'
op|'['
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
name|'shelved_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'shelved_time'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'shelved_time'
op|')'
newline|'\n'
op|'('
name|'old'
op|','
name|'instance'
op|')'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'SHELVED'
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_destroy
name|'def'
name|'fake_destroy'
op|'('
name|'inst'
op|','
name|'nw_info'
op|','
name|'bdm'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(alaski) There are too many differences between an instance'
nl|'\n'
comment|'# as returned by instance_update_and_get_original and'
nl|'\n'
comment|'# instance_get_all_by_filters so just compare the uuid.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'inst'
op|'['
string|"'uuid'"
op|']'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|','
string|"'destroy'"
op|','
name|'fake_destroy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_poll_shelved_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShelveComputeAPITestCase
dedent|''
dedent|''
name|'class'
name|'ShelveComputeAPITestCase'
op|'('
name|'test_compute'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_shelve
indent|'    '
name|'def'
name|'test_shelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure instance can be shelved.'
nl|'\n'
indent|'        '
name|'fake_instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|'{'
string|"'display_name'"
op|':'
string|"'vm01'"
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'fake_instance'
op|')'
newline|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'['
string|"'task_state'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_init
name|'def'
name|'fake_init'
op|'('
name|'self2'
op|')'
op|':'
newline|'\n'
comment|'# In original _FakeImageService.__init__(), some fake images are'
nl|'\n'
comment|'# created. To verify the snapshot name of this test only, here'
nl|'\n'
comment|'# sets a fake method.'
nl|'\n'
indent|'            '
name|'self2'
op|'.'
name|'images'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_create
dedent|''
name|'def'
name|'fake_create'
op|'('
name|'self2'
op|','
name|'ctxt'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|'['
string|"'name'"
op|']'
op|','
string|"'vm01-shelved'"
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'id'"
op|']'
op|'='
string|"'8b24ed3f-ee57-43bc-bc2e-fb2e9482bc42'"
newline|'\n'
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
dedent|''
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake_image'
op|'.'
name|'_FakeImageService'
op|','
string|"'__init__'"
op|','
name|'fake_init'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake_image'
op|'.'
name|'_FakeImageService'
op|','
string|"'create'"
op|','
name|'fake_create'
op|')'
newline|'\n'
nl|'\n'
name|'inst_obj'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'shelve'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst_obj'
op|')'
newline|'\n'
nl|'\n'
name|'inst_obj'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_obj'
op|'.'
name|'task_state'
op|','
name|'task_states'
op|'.'
name|'SHELVING'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_destroy'
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
nl|'\n'
DECL|member|test_unshelve
dedent|''
name|'def'
name|'test_unshelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure instance can be unshelved.'
nl|'\n'
indent|'        '
name|'instance'
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
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'['
string|"'task_state'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'inst_obj'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'shelve'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst_obj'
op|')'
newline|'\n'
nl|'\n'
name|'inst_obj'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
name|'inst_obj'
op|'.'
name|'task_state'
op|'='
name|'None'
newline|'\n'
name|'inst_obj'
op|'.'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'SHELVED'
newline|'\n'
name|'inst_obj'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'unshelve'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst_obj'
op|')'
newline|'\n'
nl|'\n'
name|'inst_obj'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_obj'
op|'.'
name|'task_state'
op|','
name|'task_states'
op|'.'
name|'UNSHELVING'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_destroy'
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
dedent|''
dedent|''
endmarker|''
end_unit
