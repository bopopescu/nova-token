begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
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
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeHostAPITestCase
name|'class'
name|'ComputeHostAPITestCase'
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
name|'ComputeHostAPITestCase'
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
name|'host_api'
op|'='
name|'compute'
op|'.'
name|'HostAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_mock_rpc_call
dedent|''
name|'def'
name|'_mock_rpc_call'
op|'('
name|'self'
op|','
name|'expected_message'
op|','
name|'result'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'result'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
string|"'fake-result'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpc'
op|','
string|"'call'"
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'compute.fake_host'"
op|','
nl|'\n'
name|'expected_message'
op|','
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_mock_assert_host_exists
dedent|''
name|'def'
name|'_mock_assert_host_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets it so that the host API always thinks that \'fake_host\'\n        exists.\n        """'
newline|'\n'
DECL|function|fake_assert_host_exists
name|'def'
name|'fake_assert_host_exists'
op|'('
name|'context'
op|','
name|'host_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'fake_host'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'host_api'
op|','
string|"'_assert_host_exists'"
op|','
nl|'\n'
name|'fake_assert_host_exists'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_host_enabled
dedent|''
name|'def'
name|'test_set_host_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_assert_host_exists'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mock_rpc_call'
op|'('
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'set_host_enabled'"
op|','
nl|'\n'
string|"'namespace'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'enabled'"
op|':'
string|"'fake_enabled'"
op|'}'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'BASE_RPC_API_VERSION'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'set_host_enabled'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake_host'"
op|','
nl|'\n'
string|"'fake_enabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-result'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_name_from_assert_hosts_exists
dedent|''
name|'def'
name|'test_host_name_from_assert_hosts_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_assert_host_exists'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mock_rpc_call'
op|'('
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'set_host_enabled'"
op|','
nl|'\n'
string|"'namespace'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'enabled'"
op|':'
string|"'fake_enabled'"
op|'}'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'BASE_RPC_API_VERSION'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'set_host_enabled'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake_hosT'"
op|','
nl|'\n'
string|"'fake_enabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-result'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_uptime
dedent|''
name|'def'
name|'test_get_host_uptime'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_assert_host_exists'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mock_rpc_call'
op|'('
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'get_host_uptime'"
op|','
nl|'\n'
string|"'namespace'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'BASE_RPC_API_VERSION'
op|'}'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'get_host_uptime'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake_host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-result'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_power_action
dedent|''
name|'def'
name|'test_host_power_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_assert_host_exists'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mock_rpc_call'
op|'('
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'host_power_action'"
op|','
nl|'\n'
string|"'namespace'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'action'"
op|':'
string|"'fake_action'"
op|'}'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'BASE_RPC_API_VERSION'
op|'}'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'host_power_action'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake_host'"
op|','
nl|'\n'
string|"'fake_action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-result'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_host_maintenance
dedent|''
name|'def'
name|'test_set_host_maintenance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_assert_host_exists'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mock_rpc_call'
op|'('
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'host_maintenance_mode'"
op|','
nl|'\n'
string|"'namespace'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'host'"
op|':'
string|"'fake_host'"
op|','
string|"'mode'"
op|':'
string|"'fake_mode'"
op|'}'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'.'
name|'BASE_RPC_API_VERSION'
op|'}'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'set_host_maintenance'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake_host'"
op|','
nl|'\n'
string|"'fake_mode'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-result'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_get_all_no_zones
dedent|''
name|'def'
name|'test_service_get_all_no_zones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'services'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'key1'
op|'='
string|"'val1'"
op|','
name|'key2'
op|'='
string|"'val2'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'key1'
op|'='
string|"'val2'"
op|','
name|'key3'
op|'='
string|"'val3'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host2'"
op|')'
op|']'
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
name|'host_api'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'service_get_all'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Test no filters'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
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
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test no filters #2'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'filters'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test w/ filter'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'dict'
op|'('
name|'key1'
op|'='
string|"'val2'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'services'
op|'['
number|'1'
op|']'
op|']'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_get_all
dedent|''
name|'def'
name|'test_service_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'services'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'key1'
op|'='
string|"'val1'"
op|','
name|'key2'
op|'='
string|"'val2'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'key1'
op|'='
string|"'val2'"
op|','
name|'key3'
op|'='
string|"'val3'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host2'"
op|')'
op|']'
newline|'\n'
name|'exp_services'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'exp_service'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'exp_service'
op|'.'
name|'update'
op|'('
name|'availability_zone'
op|'='
string|"'nova'"
op|','
op|'**'
name|'service'
op|')'
newline|'\n'
name|'exp_services'
op|'.'
name|'append'
op|'('
name|'exp_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'service_get_all'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Test no filters'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'set_zones'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test no filters #2'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'filters'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'set_zones'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test w/ filter'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'dict'
op|'('
name|'key1'
op|'='
string|"'val2'"
op|')'
op|','
nl|'\n'
name|'set_zones'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'exp_services'
op|'['
number|'1'
op|']'
op|']'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test w/ zone filter but no set_zones arg.'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'filters'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
string|"'nova'"
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_get_by_compute_host
dedent|''
name|'def'
name|'test_service_get_by_compute_host'
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
name|'host_api'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-host'"
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-response'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_update
dedent|''
name|'def'
name|'test_service_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_name'
op|'='
string|"'fake-host'"
newline|'\n'
name|'binary'
op|'='
string|"'nova-compute'"
newline|'\n'
name|'params_to_update'
op|'='
name|'dict'
op|'('
name|'disabled'
op|'='
name|'True'
op|')'
newline|'\n'
name|'service_id'
op|'='
number|'42'
newline|'\n'
name|'expected_result'
op|'='
op|'{'
string|"'id'"
op|':'
name|'service_id'
op|'}'
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
name|'host_api'
op|'.'
name|'db'
op|','
string|"'service_get_by_args'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'host_name'
op|','
name|'binary'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
string|"'id'"
op|':'
name|'service_id'
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
name|'host_api'
op|'.'
name|'db'
op|','
string|"'service_update'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'service_update'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'service_id'
op|','
name|'params_to_update'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'expected_result'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_update'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'host_name'
op|','
name|'binary'
op|','
name|'params_to_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_result'
op|','
name|'result'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'instance_get_all_by_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-host'"
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|"'fake-responses'"
op|']'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'fake-responses'"
op|']'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_task_log_get_all
dedent|''
name|'def'
name|'test_task_log_get_all'
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
name|'host_api'
op|'.'
name|'db'
op|','
string|"'task_log_get_all'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'task_log_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-name'"
op|','
string|"'fake-begin'"
op|','
string|"'fake-end'"
op|','
name|'host'
op|'='
string|"'fake-host'"
op|','
nl|'\n'
name|'state'
op|'='
string|"'fake-state'"
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'task_log_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake-name'"
op|','
nl|'\n'
string|"'fake-begin'"
op|','
string|"'fake-end'"
op|','
name|'host'
op|'='
string|"'fake-host'"
op|','
nl|'\n'
name|'state'
op|'='
string|"'fake-state'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-response'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeHostAPICellsTestCase
dedent|''
dedent|''
name|'class'
name|'ComputeHostAPICellsTestCase'
op|'('
name|'ComputeHostAPITestCase'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'cell_type'
op|'='
string|"'api'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'super'
op|'('
name|'ComputeHostAPICellsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_mock_rpc_call
dedent|''
name|'def'
name|'_mock_rpc_call'
op|'('
name|'self'
op|','
name|'expected_message'
op|','
name|'result'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'result'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
string|"'fake-result'"
newline|'\n'
comment|'# Wrapped with cells call'
nl|'\n'
dedent|''
name|'expected_message'
op|'='
op|'{'
string|"'method'"
op|':'
string|"'proxy_rpc_to_manager'"
op|','
nl|'\n'
string|"'namespace'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'topic'"
op|':'
string|"'compute.fake_host'"
op|','
nl|'\n'
string|"'rpc_message'"
op|':'
name|'expected_message'
op|','
nl|'\n'
string|"'call'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'timeout'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'1.2'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpc'
op|','
string|"'call'"
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'cells'"
op|','
name|'expected_message'
op|','
nl|'\n'
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_get_all_no_zones
dedent|''
name|'def'
name|'test_service_get_all_no_zones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'services'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'key1'
op|'='
string|"'val1'"
op|','
name|'key2'
op|'='
string|"'val2'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'key1'
op|'='
string|"'val2'"
op|','
name|'key3'
op|'='
string|"'val3'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host2'"
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'fake_filters'
op|'='
op|'{'
string|"'key1'"
op|':'
string|"'val1'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|','
nl|'\n'
string|"'service_get_all'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'fake_filters'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'fake_filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_get_all
dedent|''
name|'def'
name|'test_service_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'services'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'key1'
op|'='
string|"'val1'"
op|','
name|'key2'
op|'='
string|"'val2'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'key1'
op|'='
string|"'val2'"
op|','
name|'key3'
op|'='
string|"'val3'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host2'"
op|')'
op|']'
newline|'\n'
name|'exp_services'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'exp_service'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'exp_service'
op|'.'
name|'update'
op|'('
name|'availability_zone'
op|'='
string|"'nova'"
op|','
op|'**'
name|'service'
op|')'
newline|'\n'
name|'exp_services'
op|'.'
name|'append'
op|'('
name|'exp_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'fake_filters'
op|'='
op|'{'
string|"'key1'"
op|':'
string|"'val1'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|','
nl|'\n'
string|"'service_get_all'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'fake_filters'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'fake_filters'
op|','
nl|'\n'
name|'set_zones'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test w/ zone filter but no set_zones arg.'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
name|'fake_filters'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
string|"'nova'"
op|'}'
newline|'\n'
comment|'# Zone filter is done client-size, so should be stripped'
nl|'\n'
comment|'# from this call.'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
op|'{'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'services'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'filters'
op|'='
name|'fake_filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_services'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_get_by_compute_host
dedent|''
name|'def'
name|'test_service_get_by_compute_host'
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
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|','
nl|'\n'
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-host'"
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-response'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_update
dedent|''
name|'def'
name|'test_service_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_name'
op|'='
string|"'fake-host'"
newline|'\n'
name|'binary'
op|'='
string|"'nova-compute'"
newline|'\n'
name|'params_to_update'
op|'='
name|'dict'
op|'('
name|'disabled'
op|'='
name|'True'
op|')'
newline|'\n'
name|'service_id'
op|'='
number|'42'
newline|'\n'
name|'expected_result'
op|'='
op|'{'
string|"'id'"
op|':'
name|'service_id'
op|'}'
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
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|','
string|"'service_update'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'service_update'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'host_name'
op|','
nl|'\n'
name|'binary'
op|','
name|'params_to_update'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'expected_result'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_update'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'host_name'
op|','
name|'binary'
op|','
name|'params_to_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_result'
op|','
name|'result'
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
name|'instances'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cell_name'
op|'='
string|"'cell1'"
op|','
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'cell_name'
op|'='
string|"'cell2'"
op|','
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'3'
op|','
name|'cell_name'
op|'='
string|"'cell1'"
op|','
name|'host'
op|'='
string|"'host2'"
op|')'
op|']'
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
name|'host_api'
op|'.'
name|'db'
op|','
nl|'\n'
string|"'instance_get_all_by_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-host'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instances'
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
name|'expected_result'
op|'='
op|'['
name|'instances'
op|'['
number|'0'
op|']'
op|','
name|'instances'
op|'['
number|'2'
op|']'
op|']'
newline|'\n'
name|'cell_and_host'
op|'='
name|'cells_utils'
op|'.'
name|'cell_with_item'
op|'('
string|"'cell1'"
op|','
string|"'fake-host'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'cell_and_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_result'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_task_log_get_all
dedent|''
name|'def'
name|'test_task_log_get_all'
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
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|','
nl|'\n'
string|"'task_log_get_all'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'task_log_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'fake-name'"
op|','
string|"'fake-begin'"
op|','
string|"'fake-end'"
op|','
name|'host'
op|'='
string|"'fake-host'"
op|','
nl|'\n'
name|'state'
op|'='
string|"'fake-state'"
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
name|'result'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'task_log_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake-name'"
op|','
nl|'\n'
string|"'fake-begin'"
op|','
string|"'fake-end'"
op|','
name|'host'
op|'='
string|"'fake-host'"
op|','
nl|'\n'
name|'state'
op|'='
string|"'fake-state'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-response'"
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
