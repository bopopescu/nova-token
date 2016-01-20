begin_unit
comment|'# Copyright (c) 2013 NTT DOCOMO, INC.'
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
nl|'\n'
name|'from'
name|'ironicclient'
name|'import'
name|'exc'
name|'as'
name|'ironic_exc'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
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
name|'import'
name|'baremetal_nodes'
name|'as'
name|'b_nodes_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'baremetal_nodes'
name|'as'
name|'b_nodes_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'ironic'
name|'import'
name|'utils'
name|'as'
name|'ironic_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_node
dedent|''
dedent|''
name|'def'
name|'fake_node'
op|'('
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'node'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'service_host'"
op|':'
string|'"host"'
op|','
nl|'\n'
string|"'cpus'"
op|':'
number|'8'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'8192'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'pm_address'"
op|':'
string|'"10.1.2.3"'
op|','
nl|'\n'
string|"'pm_user'"
op|':'
string|'"pm_user"'
op|','
nl|'\n'
string|"'pm_password'"
op|':'
string|'"pm_pass"'
op|','
nl|'\n'
string|"'terminal_port'"
op|':'
number|'8000'
op|','
nl|'\n'
string|"'interfaces'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-instance-uuid'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'        '
name|'node'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'node'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_node_ext_status
dedent|''
name|'def'
name|'fake_node_ext_status'
op|'('
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'node'
op|'='
name|'fake_node'
op|'('
name|'uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'task_state'
op|'='
string|"'fake-task-state'"
op|','
nl|'\n'
name|'updated_at'
op|'='
string|"'fake-updated-at'"
op|','
nl|'\n'
name|'pxe_config_path'
op|'='
string|"'fake-pxe-config-path'"
op|')'
newline|'\n'
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'        '
name|'node'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'node'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_IRONIC_CLIENT
dedent|''
name|'FAKE_IRONIC_CLIENT'
op|'='
name|'ironic_utils'
op|'.'
name|'FakeClient'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'b_nodes_v21'
op|','
string|"'_get_ironic_client'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'_'
op|':'
name|'FAKE_IRONIC_CLIENT'
op|')'
newline|'\n'
DECL|class|BareMetalNodesTestV21
name|'class'
name|'BareMetalNodesTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|mod
indent|'    '
name|'mod'
op|'='
name|'b_nodes_v21'
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
name|'BareMetalNodesTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_setup'
op|'('
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'request'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup
dedent|''
name|'def'
name|'_setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'b_nodes_v21'
op|'.'
name|'BareMetalNodeController'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'list'"
op|')'
newline|'\n'
DECL|member|test_index_ironic
name|'def'
name|'test_index_ironic'
op|'('
name|'self'
op|','
name|'mock_list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'='
op|'{'
string|"'cpus'"
op|':'
number|'2'
op|','
string|"'memory_mb'"
op|':'
number|'1024'
op|','
string|"'local_gb'"
op|':'
number|'20'
op|'}'
newline|'\n'
name|'node'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_node'
op|'('
name|'properties'
op|'='
name|'properties'
op|')'
newline|'\n'
name|'mock_list'
op|'.'
name|'return_value'
op|'='
op|'['
name|'node'
op|']'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'request'
op|')'
newline|'\n'
name|'expected_output'
op|'='
op|'{'
string|"'nodes'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'memory_mb'"
op|':'
name|'properties'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'IRONIC MANAGED'"
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'properties'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
string|"'interfaces'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'node'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'cpus'"
op|':'
name|'properties'
op|'['
string|"'cpus'"
op|']'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'res_dict'
op|')'
newline|'\n'
name|'mock_list'
op|'.'
name|'assert_called_once_with'
op|'('
name|'detail'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'list'"
op|')'
newline|'\n'
DECL|member|test_index_ironic_missing_properties
name|'def'
name|'test_index_ironic_missing_properties'
op|'('
name|'self'
op|','
name|'mock_list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'='
op|'{'
string|"'cpus'"
op|':'
number|'2'
op|'}'
newline|'\n'
name|'node'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_node'
op|'('
name|'properties'
op|'='
name|'properties'
op|')'
newline|'\n'
name|'mock_list'
op|'.'
name|'return_value'
op|'='
op|'['
name|'node'
op|']'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'request'
op|')'
newline|'\n'
name|'expected_output'
op|'='
op|'{'
string|"'nodes'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'memory_mb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'IRONIC MANAGED'"
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'interfaces'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'node'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'cpus'"
op|':'
name|'properties'
op|'['
string|"'cpus'"
op|']'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'res_dict'
op|')'
newline|'\n'
name|'mock_list'
op|'.'
name|'assert_called_once_with'
op|'('
name|'detail'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_ironic_not_implemented
dedent|''
name|'def'
name|'test_index_ironic_not_implemented'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'mod'
op|','
string|"'ironic_client'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'list_ports'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'get'"
op|')'
newline|'\n'
DECL|member|test_show_ironic
name|'def'
name|'test_show_ironic'
op|'('
name|'self'
op|','
name|'mock_get'
op|','
name|'mock_list_ports'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'='
op|'{'
string|"'cpus'"
op|':'
number|'1'
op|','
string|"'memory_mb'"
op|':'
number|'512'
op|','
string|"'local_gb'"
op|':'
number|'10'
op|'}'
newline|'\n'
name|'node'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_node'
op|'('
name|'properties'
op|'='
name|'properties'
op|')'
newline|'\n'
name|'port'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_port'
op|'('
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'node'
newline|'\n'
name|'mock_list_ports'
op|'.'
name|'return_value'
op|'='
op|'['
name|'port'
op|']'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'request'
op|','
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'expected_output'
op|'='
op|'{'
string|"'node'"
op|':'
nl|'\n'
op|'{'
string|"'memory_mb'"
op|':'
name|'properties'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'IRONIC MANAGED'"
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'properties'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
string|"'interfaces'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
name|'port'
op|'.'
name|'address'
op|'}'
op|']'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'node'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'cpus'"
op|':'
name|'properties'
op|'['
string|"'cpus'"
op|']'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'res_dict'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'mock_list_ports'
op|'.'
name|'assert_called_once_with'
op|'('
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'list_ports'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'get'"
op|')'
newline|'\n'
DECL|member|test_show_ironic_no_properties
name|'def'
name|'test_show_ironic_no_properties'
op|'('
name|'self'
op|','
name|'mock_get'
op|','
name|'mock_list_ports'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'node'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_node'
op|'('
name|'properties'
op|'='
name|'properties'
op|')'
newline|'\n'
name|'port'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_port'
op|'('
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'node'
newline|'\n'
name|'mock_list_ports'
op|'.'
name|'return_value'
op|'='
op|'['
name|'port'
op|']'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'request'
op|','
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'expected_output'
op|'='
op|'{'
string|"'node'"
op|':'
nl|'\n'
op|'{'
string|"'memory_mb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'IRONIC MANAGED'"
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'interfaces'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
name|'port'
op|'.'
name|'address'
op|'}'
op|']'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'node'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'cpus'"
op|':'
number|'0'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'res_dict'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'mock_list_ports'
op|'.'
name|'assert_called_once_with'
op|'('
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'list_ports'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'get'"
op|')'
newline|'\n'
DECL|member|test_show_ironic_no_interfaces
name|'def'
name|'test_show_ironic_no_interfaces'
op|'('
name|'self'
op|','
name|'mock_get'
op|','
name|'mock_list_ports'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'='
op|'{'
string|"'cpus'"
op|':'
number|'1'
op|','
string|"'memory_mb'"
op|':'
number|'512'
op|','
string|"'local_gb'"
op|':'
number|'10'
op|'}'
newline|'\n'
name|'node'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_node'
op|'('
name|'properties'
op|'='
name|'properties'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'node'
newline|'\n'
name|'mock_list_ports'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'request'
op|','
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'res_dict'
op|'['
string|"'node'"
op|']'
op|'['
string|"'interfaces'"
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'mock_list_ports'
op|'.'
name|'assert_called_once_with'
op|'('
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'FAKE_IRONIC_CLIENT'
op|'.'
name|'node'
op|','
string|"'get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'ironic_exc'
op|'.'
name|'NotFound'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_show_ironic_node_not_found
name|'def'
name|'test_show_ironic_node_not_found'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'error'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'fake-uuid'"
op|','
name|'six'
op|'.'
name|'text_type'
op|'('
name|'error'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_ironic_not_implemented
dedent|''
name|'def'
name|'test_show_ironic_not_implemented'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'mod'
op|','
string|"'ironic_client'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'properties'
op|'='
op|'{'
string|"'cpus'"
op|':'
number|'1'
op|','
string|"'memory_mb'"
op|':'
number|'512'
op|','
string|"'local_gb'"
op|':'
number|'10'
op|'}'
newline|'\n'
name|'node'
op|'='
name|'ironic_utils'
op|'.'
name|'get_test_node'
op|'('
name|'properties'
op|'='
name|'properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
name|'node'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_ironic_not_supported
dedent|''
dedent|''
name|'def'
name|'test_create_ironic_not_supported'
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
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
op|'{'
string|"'node'"
op|':'
name|'object'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_ironic_not_supported
dedent|''
name|'def'
name|'test_delete_ironic_not_supported'
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
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
string|"'fake-id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_interface_ironic_not_supported
dedent|''
name|'def'
name|'test_add_interface_ironic_not_supported'
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
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_add_interface'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
string|"'fake-id'"
op|','
string|"'fake-body'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_interface_ironic_not_supported
dedent|''
name|'def'
name|'test_remove_interface_ironic_not_supported'
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
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_remove_interface'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
string|"'fake-id'"
op|','
string|"'fake-body'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'b_nodes_v2'
op|','
string|"'_get_ironic_client'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'_'
op|':'
name|'FAKE_IRONIC_CLIENT'
op|')'
newline|'\n'
DECL|class|BareMetalNodesTestV2
name|'class'
name|'BareMetalNodesTestV2'
op|'('
name|'BareMetalNodesTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|mod
indent|'    '
name|'mod'
op|'='
name|'b_nodes_v2'
newline|'\n'
nl|'\n'
DECL|member|_setup
name|'def'
name|'_setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'extensions'
op|'.'
name|'ExtensionManager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'b_nodes_v2'
op|'.'
name|'BareMetalNodeController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
