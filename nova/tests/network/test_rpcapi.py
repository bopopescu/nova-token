begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""\nUnit Tests for nova.network.rpcapi\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'collections'
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
name|'import'
name|'context'
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
name|'import'
name|'test'
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
DECL|class|NetworkRpcAPITestCase
name|'class'
name|'NetworkRpcAPITestCase'
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
name|'NetworkRpcAPITestCase'
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
name|'multi_host'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Used to specify the default value expected if no real value is passed'
nl|'\n'
DECL|variable|DefaultArg
dedent|''
name|'DefaultArg'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'DefaultArg'"
op|','
op|'['
string|"'value'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_network_api
name|'def'
name|'_test_network_api'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'rpc_method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
nl|'\n'
name|'rpcapi'
op|'='
name|'network_rpcapi'
op|'.'
name|'NetworkAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|'.'
name|'target'
op|'.'
name|'topic'
op|','
name|'CONF'
op|'.'
name|'network_topic'
op|')'
newline|'\n'
nl|'\n'
name|'expected_retval'
op|'='
string|"'foo'"
name|'if'
name|'method'
op|'=='
string|"'call'"
name|'else'
name|'None'
newline|'\n'
name|'expected_version'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'None'
op|')'
newline|'\n'
name|'expected_fanout'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'fanout'"
op|','
name|'None'
op|')'
newline|'\n'
name|'expected_kwargs'
op|'='
name|'kwargs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'expected_kwargs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'v'
op|','
name|'self'
op|'.'
name|'DefaultArg'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'expected_kwargs'
op|'['
name|'k'
op|']'
op|'='
name|'v'
op|'.'
name|'value'
newline|'\n'
name|'kwargs'
op|'.'
name|'pop'
op|'('
name|'k'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'prepare_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'expected_version'
op|':'
newline|'\n'
indent|'            '
name|'prepare_kwargs'
op|'['
string|"'version'"
op|']'
op|'='
name|'expected_version'
newline|'\n'
dedent|''
name|'if'
name|'expected_fanout'
op|':'
newline|'\n'
indent|'            '
name|'prepare_kwargs'
op|'['
string|"'fanout'"
op|']'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'source_compute'"
name|'in'
name|'expected_kwargs'
op|':'
newline|'\n'
comment|'# Fix up for migrate_instance_* calls.'
nl|'\n'
indent|'            '
name|'expected_kwargs'
op|'['
string|"'source'"
op|']'
op|'='
name|'expected_kwargs'
op|'.'
name|'pop'
op|'('
string|"'source_compute'"
op|')'
newline|'\n'
name|'expected_kwargs'
op|'['
string|"'dest'"
op|']'
op|'='
name|'expected_kwargs'
op|'.'
name|'pop'
op|'('
string|"'dest_compute'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'targeted_methods'
op|'='
op|'['
nl|'\n'
string|"'lease_fixed_ip'"
op|','
string|"'release_fixed_ip'"
op|','
string|"'rpc_setup_network_on_host'"
op|','
nl|'\n'
string|"'_rpc_allocate_fixed_ip'"
op|','
string|"'deallocate_fixed_ip'"
op|','
string|"'update_dns'"
op|','
nl|'\n'
string|"'_associate_floating_ip'"
op|','
string|"'_disassociate_floating_ip'"
op|','
nl|'\n'
string|"'lease_fixed_ip'"
op|','
string|"'release_fixed_ip'"
op|','
string|"'migrate_instance_start'"
op|','
nl|'\n'
string|"'migrate_instance_finish'"
op|','
nl|'\n'
string|"'allocate_for_instance'"
op|','
string|"'deallocate_for_instance'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'if'
name|'method'
name|'in'
name|'targeted_methods'
name|'and'
string|"'host'"
name|'in'
name|'expected_kwargs'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'expected_kwargs'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'method'
name|'not'
name|'in'
op|'['
string|"'allocate_for_instance'"
op|','
nl|'\n'
string|"'deallocate_for_instance'"
op|','
nl|'\n'
string|"'deallocate_fixed_ip'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'expected_kwargs'
op|'.'
name|'pop'
op|'('
string|"'host'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'multi_host'
op|':'
newline|'\n'
indent|'                '
name|'prepare_kwargs'
op|'['
string|"'server'"
op|']'
op|'='
name|'host'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpcapi'
op|','
string|"'client'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'prepare_kwargs'
op|':'
newline|'\n'
indent|'            '
name|'rpcapi'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|'**'
name|'prepare_kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc_method'
op|'='
name|'getattr'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|','
name|'rpc_method'
op|')'
newline|'\n'
name|'rpc_method'
op|'('
name|'ctxt'
op|','
name|'method'
op|','
op|'**'
name|'expected_kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'expected_retval'
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
name|'retval'
op|'='
name|'getattr'
op|'('
name|'rpcapi'
op|','
name|'method'
op|')'
op|'('
name|'ctxt'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'retval'
op|','
name|'expected_retval'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_networks
dedent|''
name|'def'
name|'test_create_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'create_networks'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'arg1'
op|'='
string|"'arg'"
op|','
name|'arg2'
op|'='
string|"'arg'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_network
dedent|''
name|'def'
name|'test_delete_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'delete_network'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'uuid'
op|'='
string|"'fake_uuid'"
op|','
name|'fixed_range'
op|'='
string|"'range'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_network
dedent|''
name|'def'
name|'test_disassociate_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'disassociate_network'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'network_uuid'
op|'='
string|"'fake_uuid'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_host_and_project
dedent|''
name|'def'
name|'test_associate_host_and_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'associate'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'network_uuid'
op|'='
string|"'fake_uuid'"
op|','
nl|'\n'
name|'associations'
op|'='
op|'{'
string|"'host'"
op|':'
string|'"testHost"'
op|','
nl|'\n'
string|"'project'"
op|':'
string|"'testProject'"
op|'}'
op|','
nl|'\n'
name|'version'
op|'='
string|'"1.5"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_fixed_ip
dedent|''
name|'def'
name|'test_get_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_fixed_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
name|'id'
op|'='
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_fixed_ip_by_address
dedent|''
name|'def'
name|'test_get_fixed_ip_by_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_fixed_ip_by_address'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'a.b.c.d'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_floating_ip
dedent|''
name|'def'
name|'test_get_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
name|'id'
op|'='
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_floating_ip_pools
dedent|''
name|'def'
name|'test_get_floating_ip_pools'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_floating_ip_pools'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'version'
op|'='
string|'"1.7"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_floating_ip_by_address
dedent|''
name|'def'
name|'test_get_floating_ip_by_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_floating_ip_by_address'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'a.b.c.d'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_floating_ips_by_project
dedent|''
name|'def'
name|'test_get_floating_ips_by_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_floating_ips_by_project'"
op|','
nl|'\n'
name|'rpc_method'
op|'='
string|"'call'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_floating_ips_by_fixed_address
dedent|''
name|'def'
name|'test_get_floating_ips_by_fixed_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_floating_ips_by_fixed_address'"
op|','
nl|'\n'
name|'rpc_method'
op|'='
string|"'call'"
op|','
name|'fixed_address'
op|'='
string|"'w.x.y.z'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_id_by_floating_address
dedent|''
name|'def'
name|'test_get_instance_id_by_floating_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_instance_id_by_floating_address'"
op|','
nl|'\n'
name|'rpc_method'
op|'='
string|"'call'"
op|','
name|'address'
op|'='
string|"'w.x.y.z'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_floating_ip
dedent|''
name|'def'
name|'test_allocate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'allocate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake_id'"
op|','
name|'pool'
op|'='
string|"'fake_pool'"
op|','
name|'auto_assigned'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deallocate_floating_ip
dedent|''
name|'def'
name|'test_deallocate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'deallocate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'addr'"
op|','
name|'affect_auto_assigned'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_floating_ip_no_multi
dedent|''
name|'def'
name|'test_allocate_floating_ip_no_multi'
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
name|'multi_host'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'allocate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake_id'"
op|','
name|'pool'
op|'='
string|"'fake_pool'"
op|','
name|'auto_assigned'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deallocate_floating_ip_no_multi
dedent|''
name|'def'
name|'test_deallocate_floating_ip_no_multi'
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
name|'multi_host'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'deallocate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'addr'"
op|','
name|'affect_auto_assigned'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_floating_ip
dedent|''
name|'def'
name|'test_associate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'associate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'floating_address'
op|'='
string|"'blah'"
op|','
name|'fixed_address'
op|'='
string|"'foo'"
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_floating_ip
dedent|''
name|'def'
name|'test_disassociate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'disassociate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'addr'"
op|','
name|'affect_auto_assigned'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_for_instance
dedent|''
name|'def'
name|'test_allocate_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'allocate_for_instance'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
name|'project_id'
op|'='
string|"'fake_id'"
op|','
name|'host'
op|'='
string|"'fake_host'"
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
name|'vpn'
op|'='
name|'False'
op|','
name|'requested_networks'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'macs'
op|'='
op|'['
op|']'
op|','
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deallocate_for_instance
dedent|''
name|'def'
name|'test_deallocate_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'deallocate_for_instance'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
name|'project_id'
op|'='
string|"'fake_id'"
op|','
name|'host'
op|'='
string|"'fake_host'"
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'self'
op|'.'
name|'DefaultArg'
op|'('
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deallocate_for_instance_with_expected_networks
dedent|''
name|'def'
name|'test_deallocate_for_instance_with_expected_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'deallocate_for_instance'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
name|'project_id'
op|'='
string|"'fake_id'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'requested_networks'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip_to_instance
dedent|''
name|'def'
name|'test_add_fixed_ip_to_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'add_fixed_ip_to_instance'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'network_id'
op|'='
string|"'fake_id'"
op|','
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_from_instance
dedent|''
name|'def'
name|'test_remove_fixed_ip_from_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'remove_fixed_ip_from_instance'"
op|','
nl|'\n'
name|'rpc_method'
op|'='
string|"'call'"
op|','
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
name|'host'
op|'='
string|"'fake_host'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'fake_address'"
op|','
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_network_to_project
dedent|''
name|'def'
name|'test_add_network_to_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'add_network_to_project'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake_id'"
op|','
name|'network_uuid'
op|'='
string|"'fake_uuid'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_nw_info
dedent|''
name|'def'
name|'test_get_instance_nw_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_instance_nw_info'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'project_id'
op|'='
string|"'fake_id'"
op|','
name|'version'
op|'='
string|"'1.9'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate_networks
dedent|''
name|'def'
name|'test_validate_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'validate_networks'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'networks'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_uuids_by_ip_filter
dedent|''
name|'def'
name|'test_get_instance_uuids_by_ip_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_instance_uuids_by_ip_filter'"
op|','
nl|'\n'
name|'rpc_method'
op|'='
string|"'call'"
op|','
name|'filters'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dns_domains
dedent|''
name|'def'
name|'test_get_dns_domains'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_dns_domains'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_dns_entry
dedent|''
name|'def'
name|'test_add_dns_entry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'add_dns_entry'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'addr'"
op|','
name|'name'
op|'='
string|"'name'"
op|','
name|'dns_type'
op|'='
string|"'foo'"
op|','
name|'domain'
op|'='
string|"'domain'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_modify_dns_entry
dedent|''
name|'def'
name|'test_modify_dns_entry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'modify_dns_entry'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'addr'"
op|','
name|'name'
op|'='
string|"'name'"
op|','
name|'domain'
op|'='
string|"'domain'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_dns_entry
dedent|''
name|'def'
name|'test_delete_dns_entry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'delete_dns_entry'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'name'"
op|','
name|'domain'
op|'='
string|"'domain'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_dns_domain
dedent|''
name|'def'
name|'test_delete_dns_domain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'delete_dns_domain'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'domain'
op|'='
string|"'fake_domain'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dns_entries_by_address
dedent|''
name|'def'
name|'test_get_dns_entries_by_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_dns_entries_by_address'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'fake_address'"
op|','
name|'domain'
op|'='
string|"'fake_domain'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dns_entries_by_name
dedent|''
name|'def'
name|'test_get_dns_entries_by_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'get_dns_entries_by_name'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'fake_name'"
op|','
name|'domain'
op|'='
string|"'fake_domain'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_private_dns_domain
dedent|''
name|'def'
name|'test_create_private_dns_domain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'create_private_dns_domain'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'domain'
op|'='
string|"'fake_domain'"
op|','
name|'av_zone'
op|'='
string|"'fake_zone'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_public_dns_domain
dedent|''
name|'def'
name|'test_create_public_dns_domain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'create_public_dns_domain'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'domain'
op|'='
string|"'fake_domain'"
op|','
name|'project'
op|'='
string|"'fake_project'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setup_networks_on_host
dedent|''
name|'def'
name|'test_setup_networks_on_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'setup_networks_on_host'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'teardown'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lease_fixed_ip
dedent|''
name|'def'
name|'test_lease_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'lease_fixed_ip'"
op|','
name|'rpc_method'
op|'='
string|"'cast'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'address'
op|'='
string|"'fake_addr'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_release_fixed_ip
dedent|''
name|'def'
name|'test_release_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'release_fixed_ip'"
op|','
name|'rpc_method'
op|'='
string|"'cast'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'address'
op|'='
string|"'fake_addr'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_network_host
dedent|''
name|'def'
name|'test_set_network_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'set_network_host'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'network_ref'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rpc_setup_network_on_host
dedent|''
name|'def'
name|'test_rpc_setup_network_on_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'rpc_setup_network_on_host'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'network_id'
op|'='
string|"'fake_id'"
op|','
name|'teardown'
op|'='
name|'False'
op|','
name|'host'
op|'='
string|"'fake_host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rpc_allocate_fixed_ip
dedent|''
name|'def'
name|'test_rpc_allocate_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'_rpc_allocate_fixed_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'fake_id'"
op|','
name|'network_id'
op|'='
string|"'fake_id'"
op|','
name|'address'
op|'='
string|"'addr'"
op|','
nl|'\n'
name|'vpn'
op|'='
name|'True'
op|','
name|'host'
op|'='
string|"'fake_host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deallocate_fixed_ip
dedent|''
name|'def'
name|'test_deallocate_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'deallocate_fixed_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'fake_addr'"
op|','
name|'host'
op|'='
string|"'fake_host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_dns
dedent|''
name|'def'
name|'test_update_dns'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'update_dns'"
op|','
name|'rpc_method'
op|'='
string|"'cast'"
op|','
name|'fanout'
op|'='
name|'True'
op|','
nl|'\n'
name|'network_ids'
op|'='
string|"'fake_id'"
op|','
name|'version'
op|'='
string|"'1.3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__associate_floating_ip
dedent|''
name|'def'
name|'test__associate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'_associate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'floating_address'
op|'='
string|"'fake_addr'"
op|','
name|'fixed_address'
op|'='
string|"'fixed_address'"
op|','
nl|'\n'
name|'interface'
op|'='
string|"'fake_interface'"
op|','
name|'host'
op|'='
string|"'fake_host'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake_uuid'"
op|','
name|'version'
op|'='
string|"'1.6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__disassociate_floating_ip
dedent|''
name|'def'
name|'test__disassociate_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'_disassociate_floating_ip'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'address'
op|'='
string|"'fake_addr'"
op|','
name|'interface'
op|'='
string|"'fake_interface'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'instance_uuid'
op|'='
string|"'fake_uuid'"
op|','
name|'version'
op|'='
string|"'1.6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_start
dedent|''
name|'def'
name|'test_migrate_instance_start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'migrate_instance_start'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake_instance_uuid'"
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake_project'"
op|','
nl|'\n'
name|'source_compute'
op|'='
string|"'fake_src_compute'"
op|','
nl|'\n'
name|'dest_compute'
op|'='
string|"'fake_dest_compute'"
op|','
nl|'\n'
name|'floating_addresses'
op|'='
string|"'fake_floating_addresses'"
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'DefaultArg'
op|'('
name|'None'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_start_multi_host
dedent|''
name|'def'
name|'test_migrate_instance_start_multi_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'migrate_instance_start'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake_instance_uuid'"
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake_project'"
op|','
nl|'\n'
name|'source_compute'
op|'='
string|"'fake_src_compute'"
op|','
nl|'\n'
name|'dest_compute'
op|'='
string|"'fake_dest_compute'"
op|','
nl|'\n'
name|'floating_addresses'
op|'='
string|"'fake_floating_addresses'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_finish
dedent|''
name|'def'
name|'test_migrate_instance_finish'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'migrate_instance_finish'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake_instance_uuid'"
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake_project'"
op|','
nl|'\n'
name|'source_compute'
op|'='
string|"'fake_src_compute'"
op|','
nl|'\n'
name|'dest_compute'
op|'='
string|"'fake_dest_compute'"
op|','
nl|'\n'
name|'floating_addresses'
op|'='
string|"'fake_floating_addresses'"
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'DefaultArg'
op|'('
name|'None'
op|')'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_finish_multi_host
dedent|''
name|'def'
name|'test_migrate_instance_finish_multi_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_api'
op|'('
string|"'migrate_instance_finish'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake_instance_uuid'"
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
string|"'fake_factor'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake_project'"
op|','
nl|'\n'
name|'source_compute'
op|'='
string|"'fake_src_compute'"
op|','
nl|'\n'
name|'dest_compute'
op|'='
string|"'fake_dest_compute'"
op|','
nl|'\n'
name|'floating_addresses'
op|'='
string|"'fake_floating_addresses'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
