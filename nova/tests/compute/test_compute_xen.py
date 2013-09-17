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
string|'"""Tests for expectations of behaviour from the Xen driver."""'
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
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
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
string|"'compute_manager'"
op|','
string|"'nova.service'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'compute_driver'"
op|','
string|"'nova.virt.driver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeXenTestCase
name|'class'
name|'ComputeXenTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBase'
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
name|'ComputeXenTestCase'
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
name|'compute_driver'
op|'='
string|"'xenapi.XenAPIDriver'"
op|','
nl|'\n'
name|'xenapi_connection_url'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'xenapi_connection_password'
op|'='
string|"'test_pass'"
op|')'
newline|'\n'
nl|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVMTests'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'CONF'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_sync_power_states_instance_not_found
dedent|''
name|'def'
name|'test_sync_power_states_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'instance_list'
op|'='
name|'instance_obj'
op|'.'
name|'_make_instance_list'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance_obj'
op|'.'
name|'InstanceList'
op|'('
op|')'
op|','
op|'['
name|'db_instance'
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'instance_list'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'instance_obj'
op|'.'
name|'InstanceList'
op|','
string|"'get_by_host'"
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
string|"'get_num_instances'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'lookup'"
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
string|"'_sync_instance_power_state'"
op|')'
newline|'\n'
nl|'\n'
name|'instance_obj'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_host'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'get_num_instances'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'1'
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'_session'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_sync_instance_power_state'
op|'('
name|'ctxt'
op|','
name|'instance'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
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
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_sync_power_states'
op|'('
name|'ctxt'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
