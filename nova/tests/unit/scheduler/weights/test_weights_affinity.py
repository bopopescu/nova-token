begin_unit
comment|'# Copyright (c) 2015 Ericsson AB'
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
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'weights'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'weights'
name|'import'
name|'affinity'
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
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SoftWeigherTestBase
name|'class'
name|'SoftWeigherTestBase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'SoftWeigherTestBase'
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
name|'weight_handler'
op|'='
name|'weights'
op|'.'
name|'HostWeightHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'weighers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_weighed_host
dedent|''
name|'def'
name|'_get_weighed_host'
op|'('
name|'self'
op|','
name|'hosts'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_spec'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'instance_group'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
nl|'\n'
name|'policies'
op|'='
op|'['
name|'policy'
op|']'
op|','
nl|'\n'
name|'members'
op|'='
op|'['
string|"'member1'"
op|','
nl|'\n'
string|"'member2'"
op|','
nl|'\n'
string|"'member3'"
op|','
nl|'\n'
string|"'member4'"
op|','
nl|'\n'
string|"'member5'"
op|','
nl|'\n'
string|"'member6'"
op|','
nl|'\n'
string|"'member7'"
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'weight_handler'
op|'.'
name|'get_weighed_objects'
op|'('
name|'self'
op|'.'
name|'weighers'
op|','
nl|'\n'
name|'hosts'
op|','
nl|'\n'
name|'request_spec'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_all_hosts
dedent|''
name|'def'
name|'_get_all_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_values'
op|'='
op|'['
nl|'\n'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
string|"'instances'"
op|':'
op|'{'
nl|'\n'
string|"'member1'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|','
nl|'\n'
string|"'instance13'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
nl|'\n'
op|'}'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
string|"'node2'"
op|','
op|'{'
string|"'instances'"
op|':'
op|'{'
nl|'\n'
string|"'member2'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|','
nl|'\n'
string|"'member3'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|','
nl|'\n'
string|"'member4'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|','
nl|'\n'
string|"'member5'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|','
nl|'\n'
string|"'instance14'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
nl|'\n'
op|'}'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'host3'"
op|','
string|"'node3'"
op|','
op|'{'
string|"'instances'"
op|':'
op|'{'
nl|'\n'
string|"'instance15'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
nl|'\n'
op|'}'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'host4'"
op|','
string|"'node4'"
op|','
op|'{'
string|"'instances'"
op|':'
op|'{'
nl|'\n'
string|"'member6'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|','
nl|'\n'
string|"'member7'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|','
nl|'\n'
string|"'instance16'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
nl|'\n'
op|'}'
op|'}'
op|')'
op|']'
newline|'\n'
name|'return'
op|'['
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
name|'host'
op|','
name|'node'
op|','
name|'values'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'node'
op|','
name|'values'
name|'in'
name|'host_values'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_do_test
dedent|''
name|'def'
name|'_do_test'
op|'('
name|'self'
op|','
name|'policy'
op|','
name|'expected_weight'
op|','
nl|'\n'
name|'expected_host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hostinfo_list'
op|'='
name|'self'
op|'.'
name|'_get_all_hosts'
op|'('
op|')'
newline|'\n'
name|'weighed_host'
op|'='
name|'self'
op|'.'
name|'_get_weighed_host'
op|'('
name|'hostinfo_list'
op|','
nl|'\n'
name|'policy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_weight'
op|','
name|'weighed_host'
op|'.'
name|'weight'
op|')'
newline|'\n'
name|'if'
name|'expected_host'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_host'
op|','
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SoftAffinityWeigherTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'SoftAffinityWeigherTestCase'
op|'('
name|'SoftWeigherTestBase'
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
name|'SoftAffinityWeigherTestCase'
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
name|'weighers'
op|'='
op|'['
name|'affinity'
op|'.'
name|'ServerGroupSoftAffinityWeigher'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_soft_affinity_weight_multiplier_by_default
dedent|''
name|'def'
name|'test_soft_affinity_weight_multiplier_by_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'1.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_soft_affinity_weight_multiplier_zero_value
dedent|''
name|'def'
name|'test_soft_affinity_weight_multiplier_zero_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# We do not know the host, all have same weight.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'soft_affinity_weight_multiplier'
op|'='
number|'0.0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'0.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_soft_affinity_weight_multiplier_positive_value
dedent|''
name|'def'
name|'test_soft_affinity_weight_multiplier_positive_value'
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
name|'soft_affinity_weight_multiplier'
op|'='
number|'2.0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'2.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host2'"
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
name|'affinity'
op|','
string|"'LOG'"
op|')'
newline|'\n'
DECL|member|test_soft_affinity_weight_multiplier_negative_value
name|'def'
name|'test_soft_affinity_weight_multiplier_negative_value'
op|'('
name|'self'
op|','
name|'mock_log'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'soft_affinity_weight_multiplier'
op|'='
op|'-'
number|'1.0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'0.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host3'"
op|')'
newline|'\n'
comment|'# call twice and assert that only one warning is emitted'
nl|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'0.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_log'
op|'.'
name|'warn'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SoftAntiAffinityWeigherTestCase
dedent|''
dedent|''
name|'class'
name|'SoftAntiAffinityWeigherTestCase'
op|'('
name|'SoftWeigherTestBase'
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
name|'SoftAntiAffinityWeigherTestCase'
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
name|'weighers'
op|'='
op|'['
name|'affinity'
op|'.'
name|'ServerGroupSoftAntiAffinityWeigher'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_soft_anti_affinity_weight_multiplier_by_default
dedent|''
name|'def'
name|'test_soft_anti_affinity_weight_multiplier_by_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-anti-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'1.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_soft_anti_affinity_weight_multiplier_zero_value
dedent|''
name|'def'
name|'test_soft_anti_affinity_weight_multiplier_zero_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# We do not know the host, all have same weight.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'soft_anti_affinity_weight_multiplier'
op|'='
number|'0.0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-anti-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'0.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_soft_anti_affinity_weight_multiplier_positive_value
dedent|''
name|'def'
name|'test_soft_anti_affinity_weight_multiplier_positive_value'
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
name|'soft_anti_affinity_weight_multiplier'
op|'='
number|'2.0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-anti-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'2.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host3'"
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
name|'affinity'
op|','
string|"'LOG'"
op|')'
newline|'\n'
DECL|member|test_soft_anti_affinity_weight_multiplier_negative_value
name|'def'
name|'test_soft_anti_affinity_weight_multiplier_negative_value'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_log'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'soft_anti_affinity_weight_multiplier'
op|'='
op|'-'
number|'1.0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-anti-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'0.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host2'"
op|')'
newline|'\n'
comment|'# call twice and assert that only one warning is emitted'
nl|'\n'
name|'self'
op|'.'
name|'_do_test'
op|'('
name|'policy'
op|'='
string|"'soft-anti-affinity'"
op|','
nl|'\n'
name|'expected_weight'
op|'='
number|'0.0'
op|','
nl|'\n'
name|'expected_host'
op|'='
string|"'host2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_log'
op|'.'
name|'warn'
op|'.'
name|'call_count'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
