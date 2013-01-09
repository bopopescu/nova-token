begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nTests For CellsManager\n"""'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'messaging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'utils'
name|'as'
name|'cells_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'cells'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsManagerClassTestCase
name|'class'
name|'CellsManagerClassTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for CellsManager class."""'
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
name|'CellsManagerClassTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'init'
op|'('
name|'self'
op|')'
newline|'\n'
comment|'# pick a child cell to use for tests.'
nl|'\n'
name|'self'
op|'.'
name|'our_cell'
op|'='
string|"'grandchild-cell1'"
newline|'\n'
name|'self'
op|'.'
name|'cells_manager'
op|'='
name|'fakes'
op|'.'
name|'get_cells_manager'
op|'('
name|'self'
op|'.'
name|'our_cell'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'='
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'msg_runner'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'ctxt'
op|'='
string|"'fake_context'"
newline|'\n'
nl|'\n'
DECL|member|test_post_start_hook_child_cell
dedent|''
name|'def'
name|'test_post_start_hook_child_cell'
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
name|'driver'
op|','
string|"'start_consumers'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'context'
op|','
string|"'get_admin_context'"
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
name|'cells_manager'
op|','
string|"'_update_our_parents'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'start_consumers'
op|'('
name|'self'
op|'.'
name|'msg_runner'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'_update_our_parents'
op|'('
name|'self'
op|'.'
name|'ctxt'
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
name|'cells_manager'
op|'.'
name|'post_start_hook'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_start_hook_middle_cell
dedent|''
name|'def'
name|'test_post_start_hook_middle_cell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells_manager'
op|'='
name|'fakes'
op|'.'
name|'get_cells_manager'
op|'('
string|"'child-cell2'"
op|')'
newline|'\n'
name|'msg_runner'
op|'='
name|'cells_manager'
op|'.'
name|'msg_runner'
newline|'\n'
name|'driver'
op|'='
name|'cells_manager'
op|'.'
name|'driver'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'driver'
op|','
string|"'start_consumers'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'context'
op|','
string|"'get_admin_context'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'msg_runner'
op|','
nl|'\n'
string|"'ask_children_for_capabilities'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'msg_runner'
op|','
nl|'\n'
string|"'ask_children_for_capacities'"
op|')'
newline|'\n'
nl|'\n'
name|'driver'
op|'.'
name|'start_consumers'
op|'('
name|'msg_runner'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'msg_runner'
op|'.'
name|'ask_children_for_capabilities'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'msg_runner'
op|'.'
name|'ask_children_for_capacities'
op|'('
name|'self'
op|'.'
name|'ctxt'
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
name|'cells_manager'
op|'.'
name|'post_start_hook'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_our_parents
dedent|''
name|'def'
name|'test_update_our_parents'
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
name|'msg_runner'
op|','
nl|'\n'
string|"'tell_parents_our_capabilities'"
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
name|'msg_runner'
op|','
nl|'\n'
string|"'tell_parents_our_capacities'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'tell_parents_our_capabilities'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'tell_parents_our_capacities'
op|'('
name|'self'
op|'.'
name|'ctxt'
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
name|'cells_manager'
op|'.'
name|'_update_our_parents'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_schedule_run_instance
dedent|''
name|'def'
name|'test_schedule_run_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_sched_kwargs'
op|'='
string|"'fake_host_sched_kwargs_silently_passed'"
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'msg_runner'
op|','
string|"'schedule_run_instance'"
op|')'
newline|'\n'
name|'our_cell'
op|'='
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'schedule_run_instance'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'our_cell'
op|','
nl|'\n'
name|'host_sched_kwargs'
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
name|'cells_manager'
op|'.'
name|'schedule_run_instance'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'host_sched_kwargs'
op|'='
name|'host_sched_kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_compute_api_method
dedent|''
name|'def'
name|'test_run_compute_api_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Args should just be silently passed through'
nl|'\n'
indent|'        '
name|'cell_name'
op|'='
string|"'fake-cell-name'"
newline|'\n'
name|'method_info'
op|'='
string|"'fake-method-info'"
newline|'\n'
nl|'\n'
name|'fake_response'
op|'='
name|'messaging'
op|'.'
name|'Response'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'False'
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
name|'msg_runner'
op|','
nl|'\n'
string|"'run_compute_api_method'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'fake_response'
op|','
nl|'\n'
string|"'value_or_raise'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'run_compute_api_method'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'cell_name'
op|','
nl|'\n'
name|'method_info'
op|','
nl|'\n'
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_response'
op|')'
newline|'\n'
name|'fake_response'
op|'.'
name|'value_or_raise'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake-response'"
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
name|'response'
op|'='
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'run_compute_api_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'cell_name'
op|'='
name|'cell_name'
op|','
name|'method_info'
op|'='
name|'method_info'
op|','
nl|'\n'
name|'call'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-response'"
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_update_at_top
dedent|''
name|'def'
name|'test_instance_update_at_top'
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
name|'msg_runner'
op|','
string|"'instance_update_at_top'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_update_at_top'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake-instance'"
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
name|'cells_manager'
op|'.'
name|'instance_update_at_top'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|'='
string|"'fake-instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_destroy_at_top
dedent|''
name|'def'
name|'test_instance_destroy_at_top'
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
name|'msg_runner'
op|','
string|"'instance_destroy_at_top'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_destroy_at_top'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake-instance'"
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
name|'cells_manager'
op|'.'
name|'instance_destroy_at_top'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|'='
string|"'fake-instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_delete_everywhere
dedent|''
name|'def'
name|'test_instance_delete_everywhere'
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
name|'msg_runner'
op|','
nl|'\n'
string|"'instance_delete_everywhere'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_delete_everywhere'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'fake-type'"
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
name|'cells_manager'
op|'.'
name|'instance_delete_everywhere'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'instance'
op|'='
string|"'fake-instance'"
op|','
nl|'\n'
name|'delete_type'
op|'='
string|"'fake-type'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_fault_create_at_top
dedent|''
name|'def'
name|'test_instance_fault_create_at_top'
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
name|'msg_runner'
op|','
nl|'\n'
string|"'instance_fault_create_at_top'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_fault_create_at_top'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-fault'"
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
name|'cells_manager'
op|'.'
name|'instance_fault_create_at_top'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'instance_fault'
op|'='
string|"'fake-fault'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bw_usage_update_at_top
dedent|''
name|'def'
name|'test_bw_usage_update_at_top'
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
name|'msg_runner'
op|','
nl|'\n'
string|"'bw_usage_update_at_top'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'bw_usage_update_at_top'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-bw-info'"
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
name|'cells_manager'
op|'.'
name|'bw_usage_update_at_top'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'bw_update_info'
op|'='
string|"'fake-bw-info'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_heal_instances
dedent|''
name|'def'
name|'test_heal_instances'
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
name|'instance_updated_at_threshold'
op|'='
number|'1000'
op|','
nl|'\n'
name|'instance_update_num_instances'
op|'='
number|'2'
op|','
nl|'\n'
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'stalled_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'updated_since'
op|'='
name|'stalled_time'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
number|'1000'
op|')'
newline|'\n'
nl|'\n'
DECL|function|utcnow
name|'def'
name|'utcnow'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'stalled_time'
newline|'\n'
nl|'\n'
dedent|''
name|'call_info'
op|'='
op|'{'
string|"'get_instances'"
op|':'
number|'0'
op|','
string|"'sync_instances'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
op|'['
string|"'instance1'"
op|','
string|"'instance2'"
op|','
string|"'instance3'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_instances_to_sync
name|'def'
name|'get_instances_to_sync'
op|'('
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'context'
op|','
name|'fake_context'
op|')'
newline|'\n'
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'shuffle'"
op|')'
newline|'\n'
name|'call_info'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|')'
newline|'\n'
name|'call_info'
op|'['
string|"'updated_since'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'updated_since'"
op|')'
newline|'\n'
name|'call_info'
op|'['
string|"'get_instances'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'return'
name|'iter'
op|'('
name|'instances'
op|')'
newline|'\n'
nl|'\n'
DECL|function|instance_get_by_uuid
dedent|''
name|'def'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instances'
op|'['
name|'int'
op|'('
name|'uuid'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
DECL|function|sync_instance
dedent|''
name|'def'
name|'sync_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'context'
op|','
name|'fake_context'
op|')'
newline|'\n'
name|'call_info'
op|'['
string|"'sync_instances'"
op|']'
op|'.'
name|'append'
op|'('
name|'instance'
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
name|'cells_utils'
op|','
string|"'get_instances_to_sync'"
op|','
nl|'\n'
name|'get_instances_to_sync'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'instance_get_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'cells_manager'
op|','
string|"'_sync_instance'"
op|','
nl|'\n'
name|'sync_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'timeutils'
op|','
string|"'utcnow'"
op|','
name|'utcnow'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'_heal_instances'
op|'('
name|'fake_context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'project_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'updated_since'"
op|']'
op|','
name|'updated_since'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'get_instances'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
comment|'# Only first 2'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'sync_instances'"
op|']'
op|','
nl|'\n'
name|'instances'
op|'['
op|':'
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'call_info'
op|'['
string|"'sync_instances'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'cells_manager'
op|'.'
name|'_heal_instances'
op|'('
name|'fake_context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'shuffle'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'project_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'updated_since'"
op|']'
op|','
name|'updated_since'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'get_instances'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
comment|'# Now the last 1 and the first 1'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'call_info'
op|'['
string|"'sync_instances'"
op|']'
op|','
nl|'\n'
op|'['
name|'instances'
op|'['
op|'-'
number|'1'
op|']'
op|','
name|'instances'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
