begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 Openstack Foundation'
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
string|'"""\nTests For Compute admin api w/ Cells\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'admin_actions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'cells_api'
name|'as'
name|'compute_cells_api'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'uuidutils'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|INSTANCE_IDS
name|'INSTANCE_IDS'
op|'='
op|'{'
string|"'inst_id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsAdminAPITestCase
name|'class'
name|'CellsAdminAPITestCase'
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
name|'CellsAdminAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fake_cell_read_only
name|'def'
name|'_fake_cell_read_only'
op|'('
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
name|'False'
newline|'\n'
nl|'\n'
DECL|function|_fake_validate_cell
dedent|''
name|'def'
name|'_fake_validate_cell'
op|'('
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
newline|'\n'
nl|'\n'
DECL|function|_fake_compute_api_get
dedent|''
name|'def'
name|'_fake_compute_api_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'uuid'"
op|':'
name|'instance_id'
op|','
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
string|"'cell_name'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_fake_instance_update_and_get_original
dedent|''
name|'def'
name|'_fake_instance_update_and_get_original'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'INSTANCE_IDS'
op|'.'
name|'get'
op|'('
name|'instance_uuid'
op|')'
op|','
nl|'\n'
name|'name'
op|'='
name|'values'
op|'.'
name|'get'
op|'('
string|"'display_name'"
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'inst'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_cast_to_cells
dedent|''
name|'def'
name|'fake_cast_to_cells'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'method'
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
string|'"""\n            Makes sure that the cells receive the cast to update\n            the cell state\n            """'
newline|'\n'
name|'self'
op|'.'
name|'cells_received_kwargs'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'admin_api'
op|'='
name|'admin_actions'
op|'.'
name|'AdminActionsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'compute_api'
op|'='
name|'compute_cells_api'
op|'.'
name|'ComputeCellsAPI'
op|'('
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
name|'admin_api'
op|'.'
name|'compute_api'
op|','
string|"'_cell_read_only'"
op|','
nl|'\n'
name|'_fake_cell_read_only'
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
name|'admin_api'
op|'.'
name|'compute_api'
op|','
string|"'_validate_cell'"
op|','
nl|'\n'
name|'_fake_validate_cell'
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
name|'admin_api'
op|'.'
name|'compute_api'
op|','
string|"'get'"
op|','
nl|'\n'
name|'_fake_compute_api_get'
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
name|'admin_api'
op|'.'
name|'compute_api'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'instance_update_and_get_original'"
op|','
nl|'\n'
name|'_fake_instance_update_and_get_original'
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
name|'admin_api'
op|'.'
name|'compute_api'
op|','
string|"'_cast_to_cells'"
op|','
nl|'\n'
name|'fake_cast_to_cells'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'url'
op|'='
string|"'/fake/servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cells_received_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_reset_active
dedent|''
name|'def'
name|'test_reset_active'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"error"'
op|'}'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|'('
name|'self'
op|'.'
name|'request'
op|','
string|"'inst_id'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
comment|'# Make sure the cells received the update'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'cells_received_kwargs'
op|','
nl|'\n'
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
