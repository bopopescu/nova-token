begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""\nBare-Metal DB testcase for BareMetalNode\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalNodesTestCase
name|'class'
name|'BareMetalNodesTestCase'
op|'('
name|'base'
op|'.'
name|'BMDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_create_nodes
indent|'    '
name|'def'
name|'_create_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nodes'
op|'='
op|'['
nl|'\n'
name|'utils'
op|'.'
name|'new_bm_node'
op|'('
name|'pm_address'
op|'='
string|"'0'"
op|','
name|'service_host'
op|'='
string|'"host1"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'100000'
op|','
name|'cpus'
op|'='
number|'100'
op|','
name|'local_gb'
op|'='
number|'10000'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'new_bm_node'
op|'('
name|'pm_address'
op|'='
string|"'1'"
op|','
name|'service_host'
op|'='
string|'"host2"'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'A'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'100000'
op|','
name|'cpus'
op|'='
number|'100'
op|','
name|'local_gb'
op|'='
number|'10000'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'new_bm_node'
op|'('
name|'pm_address'
op|'='
string|"'2'"
op|','
name|'service_host'
op|'='
string|'"host2"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'1000'
op|','
name|'cpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'new_bm_node'
op|'('
name|'pm_address'
op|'='
string|"'3'"
op|','
name|'service_host'
op|'='
string|'"host2"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'1000'
op|','
name|'cpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'new_bm_node'
op|'('
name|'pm_address'
op|'='
string|"'4'"
op|','
name|'service_host'
op|'='
string|'"host2"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2000'
op|','
name|'cpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'new_bm_node'
op|'('
name|'pm_address'
op|'='
string|"'5'"
op|','
name|'service_host'
op|'='
string|'"host2"'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2000'
op|','
name|'cpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'n'
name|'in'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'ref'
op|'='
name|'db'
op|'.'
name|'bm_node_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ids'
op|'.'
name|'append'
op|'('
name|'ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all
dedent|''
dedent|''
name|'def'
name|'test_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'r'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_create_nodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get
dedent|''
name|'def'
name|'test_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'r'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'0'"
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'r'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NodeNotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_node_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_service_host
dedent|''
name|'def'
name|'test_get_by_service_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service_host'
op|'='
string|'"host1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'r'
op|'['
number|'0'
op|']'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'0'"
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service_host'
op|'='
string|'"host2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
name|'pmaddrs'
op|'='
op|'['
name|'x'
op|'['
string|"'pm_address'"
op|']'
name|'for'
name|'x'
name|'in'
name|'r'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'1'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'2'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'3'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'4'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'5'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service_host'
op|'='
string|'"host3"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'r'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_associated
dedent|''
name|'def'
name|'test_get_associated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_associated'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'r'
op|'['
number|'0'
op|']'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_unassociated'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
name|'pmaddrs'
op|'='
op|'['
name|'x'
op|'['
string|"'pm_address'"
op|']'
name|'for'
name|'x'
name|'in'
name|'r'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'0'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'2'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'3'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'4'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'5'"
op|','
name|'pmaddrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy
dedent|''
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'bm_node_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NodeNotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_node_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_with_interfaces
dedent|''
name|'def'
name|'test_destroy_with_interfaces'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if_a_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'aa:aa:aa:aa:aa:aa'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'if_b_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'bb:bb:bb:bb:bb:bb'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'if_x_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
string|"'11:22:33:44:55:66'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'bm_node_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_interface_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'if_a_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_interface_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'if_b_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# Another node's interface is not affected"
nl|'\n'
name|'if_x'
op|'='
name|'db'
op|'.'
name|'bm_interface_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'if_x_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ids'
op|'['
number|'1'
op|']'
op|','
name|'if_x'
op|'['
string|"'bm_node_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NodeNotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_node_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'r'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'r'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_free
dedent|''
name|'def'
name|'test_find_free'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_nodes'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fn'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'2'"
op|')'
newline|'\n'
nl|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'500'
op|','
name|'cpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'100'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fn'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'3'"
op|')'
newline|'\n'
nl|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'1001'
op|','
name|'cpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fn'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'4'"
op|')'
newline|'\n'
nl|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2000'
op|','
name|'cpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fn'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'4'"
op|')'
newline|'\n'
nl|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2000'
op|','
name|'cpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fn'
op|'['
string|"'pm_address'"
op|']'
op|','
string|"'5'"
op|')'
newline|'\n'
nl|'\n'
comment|'# check memory_mb'
nl|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2001'
op|','
name|'cpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'fn'
op|')'
newline|'\n'
nl|'\n'
comment|'# check cpus'
nl|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2000'
op|','
name|'cpus'
op|'='
number|'3'
op|','
name|'local_gb'
op|'='
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'fn'
op|')'
newline|'\n'
nl|'\n'
comment|'# check local_gb'
nl|'\n'
name|'fn'
op|'='
name|'db'
op|'.'
name|'bm_node_find_free'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2000'
op|','
name|'cpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'1001'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'fn'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
