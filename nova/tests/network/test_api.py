begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
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
string|'"""Tests for network API."""'
newline|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
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
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'rpcapi'
name|'as'
name|'network_rpcapi'
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
name|'policy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'a47ae74e-ab08-547f-9eee-ffd23fc46c16'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkPolicyTestCase
name|'class'
name|'NetworkPolicyTestCase'
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
name|'NetworkPolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NetworkPolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_policy
dedent|''
name|'def'
name|'test_check_policy'
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
name|'policy'
op|','
string|"'enforce'"
op|')'
newline|'\n'
name|'target'
op|'='
op|'{'
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'network:get_all'"
op|','
name|'target'
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
name|'api'
op|'.'
name|'check_policy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'get_all'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiTestCase
dedent|''
dedent|''
name|'class'
name|'ApiTestCase'
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
name|'ApiTestCase'
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
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake-user'"
op|','
nl|'\n'
string|"'fake-project'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_for_instance_handles_macs_passed
dedent|''
name|'def'
name|'test_allocate_for_instance_handles_macs_passed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# If a macs argument is supplied to the 'nova-network' API, it is just"
nl|'\n'
comment|'# ignored. This test checks that the call down to the rpcapi layer'
nl|'\n'
comment|"# doesn't pass macs down: nova-network doesn't support hypervisor"
nl|'\n'
comment|'# mac address limits (today anyhow).'
nl|'\n'
indent|'        '
name|'macs'
op|'='
name|'set'
op|'('
op|'['
string|"'ab:cd:ef:01:23:34'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'network_rpcapi'
op|','
string|'"allocate_for_instance"'
op|')'
newline|'\n'
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'zip'
op|'('
op|'['
string|"'host'"
op|','
string|"'instance_id'"
op|','
string|"'instance_uuid'"
op|','
nl|'\n'
string|"'project_id'"
op|','
string|"'requested_networks'"
op|','
string|"'rxtx_factor'"
op|','
string|"'vpn'"
op|']'
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'repeat'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'network_rpcapi'
op|'.'
name|'allocate_for_instance'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
op|'**'
name|'kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
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
name|'instance'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
string|"'id'"
op|','
name|'uuid'
op|'='
string|"'uuid'"
op|','
name|'project_id'
op|'='
string|"'project_id'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host'"
op|','
name|'instance_type'
op|'='
op|'{'
string|"'rxtx_factor'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'allocate_for_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'vpn'"
op|','
string|"'requested_networks'"
op|','
name|'macs'
op|'='
name|'macs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_test_associate_floating_ip
dedent|''
name|'def'
name|'_do_test_associate_floating_ip'
op|'('
name|'self'
op|','
name|'orig_instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test post-association logic."""'
newline|'\n'
nl|'\n'
name|'new_instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'new-uuid'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_rpc_call
name|'def'
name|'fake_rpc_call'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'orig_instance_uuid'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'call'"
op|','
name|'fake_rpc_call'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_by_uuid
name|'def'
name|'fake_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
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
name|'network_api'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get_nw_info
name|'def'
name|'fake_get_nw_info'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNWInfo
indent|'            '
name|'class'
name|'FakeNWInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|json
indent|'                '
name|'def'
name|'json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'FakeNWInfo'
op|'('
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
name|'network_api'
op|','
string|"'_get_instance_nw_info'"
op|','
nl|'\n'
name|'fake_get_nw_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'orig_instance_uuid'
op|':'
newline|'\n'
indent|'            '
name|'expected_updated_instances'
op|'='
op|'['
name|'new_instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'orig_instance_uuid'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'expected_updated_instances'
op|'='
op|'['
name|'new_instance'
op|'['
string|"'uuid'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_info_cache_update
dedent|''
name|'def'
name|'fake_instance_info_cache_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'cache'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instance_uuid'
op|','
nl|'\n'
name|'expected_updated_instances'
op|'.'
name|'pop'
op|'('
op|')'
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
name|'network_api'
op|'.'
name|'db'
op|','
string|"'instance_info_cache_update'"
op|','
nl|'\n'
name|'fake_instance_info_cache_update'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'associate_floating_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'new_instance'
op|','
nl|'\n'
string|"'172.24.4.225'"
op|','
nl|'\n'
string|"'10.0.0.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_preassociated_floating_ip
dedent|''
name|'def'
name|'test_associate_preassociated_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_associate_floating_ip'
op|'('
string|"'orig-uuid'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_unassociated_floating_ip
dedent|''
name|'def'
name|'test_associate_unassociated_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_associate_floating_ip'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_migrate_instance_calls
dedent|''
name|'def'
name|'_stub_migrate_instance_calls'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'multi_host'
op|','
name|'info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_instance_type'
op|'='
op|'{'
string|"'rxtx_factor'"
op|':'
string|"'fake_factor'"
op|'}'
newline|'\n'
name|'fake_instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake_uuid'"
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'fake_instance_type'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project_id'"
op|'}'
newline|'\n'
name|'fake_migration'
op|'='
op|'{'
string|"'source_compute'"
op|':'
string|"'fake_compute_source'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'fake_compute_dest'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_mig_inst_method
name|'def'
name|'fake_mig_inst_method'
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
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|'='
name|'kwargs'
newline|'\n'
nl|'\n'
DECL|function|fake_is_multi_host
dedent|''
name|'def'
name|'fake_is_multi_host'
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
name|'multi_host'
newline|'\n'
nl|'\n'
DECL|function|fake_get_floaters
dedent|''
name|'def'
name|'fake_get_floaters'
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
op|'['
string|"'fake_float1'"
op|','
string|"'fake_float2'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_rpcapi'
op|'.'
name|'NetworkAPI'
op|','
name|'method'
op|','
nl|'\n'
name|'fake_mig_inst_method'
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
name|'network_api'
op|','
string|"'_is_multi_host'"
op|','
nl|'\n'
name|'fake_is_multi_host'
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
name|'network_api'
op|','
string|"'_get_floating_ip_addresses'"
op|','
nl|'\n'
name|'fake_get_floaters'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'instance_uuid'"
op|':'
string|"'fake_uuid'"
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'fake_compute_source'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'fake_compute_dest'"
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
string|"'fake_factor'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project_id'"
op|','
nl|'\n'
string|"'floating_addresses'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'if'
name|'multi_host'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'['
string|"'floating_addresses'"
op|']'
op|'='
op|'['
string|"'fake_float1'"
op|','
string|"'fake_float2'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'fake_instance'
op|','
name|'fake_migration'
op|','
name|'expected'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_start_with_multhost
dedent|''
name|'def'
name|'test_migrate_instance_start_with_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_start'"
op|','
name|'True'
op|','
name|'info'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'host'"
op|']'
op|'='
string|"'fake_compute_source'"
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_start'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_start_without_multhost
dedent|''
name|'def'
name|'test_migrate_instance_start_without_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_start'"
op|','
name|'False'
op|','
name|'info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_start'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_finish_with_multhost
dedent|''
name|'def'
name|'test_migrate_instance_finish_with_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_finish'"
op|','
name|'True'
op|','
name|'info'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'host'"
op|']'
op|'='
string|"'fake_compute_dest'"
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_finish'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_finish_without_multhost
dedent|''
name|'def'
name|'test_migrate_instance_finish_without_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_finish'"
op|','
name|'False'
op|','
name|'info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_finish'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_multi_host_instance_has_no_fixed_ip
dedent|''
name|'def'
name|'test_is_multi_host_instance_has_no_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_fixed_ip_get_by_instance
indent|'        '
name|'def'
name|'fake_fixed_ip_get_by_instance'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FixedIpNotFoundForInstance'
op|'('
name|'instance_uuid'
op|'='
name|'uuid'
op|')'
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
name|'network_api'
op|'.'
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_instance'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'_is_multi_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_multi_host_network_has_no_project_id
dedent|''
name|'def'
name|'test_is_multi_host_network_has_no_project_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'is_multi_host'
op|'='
name|'random'
op|'.'
name|'choice'
op|'('
op|'['
name|'True'
op|','
name|'False'
op|']'
op|')'
newline|'\n'
name|'network'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'is_multi_host'
op|','
op|'}'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|'.'
name|'network_create_safe'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_by_instance
name|'def'
name|'fake_fixed_ip_get_by_instance'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
op|'['
op|'{'
string|"'network_id'"
op|':'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'FAKE_UUID'
op|','
op|'}'
op|']'
newline|'\n'
name|'return'
name|'fixed_ip'
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
name|'network_api'
op|'.'
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'_is_multi_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'is_multi_host'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_multi_host_network_has_project_id
dedent|''
name|'def'
name|'test_is_multi_host_network_has_project_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'is_multi_host'
op|'='
name|'random'
op|'.'
name|'choice'
op|'('
op|'['
name|'True'
op|','
name|'False'
op|']'
op|')'
newline|'\n'
name|'network'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'is_multi_host'
op|','
op|'}'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|'.'
name|'network_create_safe'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_by_instance
name|'def'
name|'fake_fixed_ip_get_by_instance'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
op|'['
op|'{'
string|"'network_id'"
op|':'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'FAKE_UUID'
op|','
op|'}'
op|']'
newline|'\n'
name|'return'
name|'fixed_ip'
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
name|'network_api'
op|'.'
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'_is_multi_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'is_multi_host'
op|','
name|'result'
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
name|'ctxt'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'backdoor_port'
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
name|'network_api'
op|'.'
name|'network_rpcapi'
op|','
string|"'get_backdoor_port'"
op|','
nl|'\n'
name|'fake_get_backdoor_port'
op|')'
newline|'\n'
nl|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'network_api'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'port'
op|','
name|'backdoor_port'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
