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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'core_filter'
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
DECL|class|TestCoreFilter
name|'class'
name|'TestCoreFilter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_core_filter_passes
indent|'    '
name|'def'
name|'test_core_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'core_filter'
op|'.'
name|'CoreFilter'
op|'('
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'vcpus'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'vcpus_total'"
op|':'
number|'4'
op|','
string|"'vcpus_used'"
op|':'
number|'7'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'2'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_core_filter_fails_safe
dedent|''
name|'def'
name|'test_core_filter_fails_safe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'core_filter'
op|'.'
name|'CoreFilter'
op|'('
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'vcpus'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_core_filter_fails
dedent|''
name|'def'
name|'test_core_filter_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'core_filter'
op|'.'
name|'CoreFilter'
op|'('
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'vcpus'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'vcpus_total'"
op|':'
number|'4'
op|','
string|"'vcpus_used'"
op|':'
number|'8'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'2'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_core_filter_single_instance_overcommit_fails
dedent|''
name|'def'
name|'test_core_filter_single_instance_overcommit_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'core_filter'
op|'.'
name|'CoreFilter'
op|'('
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'vcpus'"
op|':'
number|'2'
op|'}'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'vcpus_total'"
op|':'
number|'1'
op|','
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'2'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.scheduler.filters.utils.aggregate_values_from_key'"
op|')'
newline|'\n'
DECL|member|test_aggregate_core_filter_value_error
name|'def'
name|'test_aggregate_core_filter_value_error'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'core_filter'
op|'.'
name|'AggregateCoreFilter'
op|'('
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
string|"'vcpus'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'vcpus_total'"
op|':'
number|'4'
op|','
string|"'vcpus_used'"
op|':'
number|'7'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'2'
op|'}'
op|')'
newline|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
string|"'XXX'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'agg_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'host'
op|','
string|"'cpu_allocation_ratio'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|'*'
number|'2'
op|','
name|'host'
op|'.'
name|'limits'
op|'['
string|"'vcpu'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.scheduler.filters.utils.aggregate_values_from_key'"
op|')'
newline|'\n'
DECL|member|test_aggregate_core_filter_default_value
name|'def'
name|'test_aggregate_core_filter_default_value'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'core_filter'
op|'.'
name|'AggregateCoreFilter'
op|'('
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
string|"'vcpus'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'vcpus_total'"
op|':'
number|'4'
op|','
string|"'vcpus_used'"
op|':'
number|'8'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'2'
op|'}'
op|')'
newline|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
comment|'# False: fallback to default flag w/o aggregates'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'agg_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'host'
op|','
string|"'cpu_allocation_ratio'"
op|')'
newline|'\n'
comment|'# True: use ratio from aggregates'
nl|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
string|"'3'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|'*'
number|'3'
op|','
name|'host'
op|'.'
name|'limits'
op|'['
string|"'vcpu'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.scheduler.filters.utils.aggregate_values_from_key'"
op|')'
newline|'\n'
DECL|member|test_aggregate_core_filter_conflict_values
name|'def'
name|'test_aggregate_core_filter_conflict_values'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'core_filter'
op|'.'
name|'AggregateCoreFilter'
op|'('
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
string|"'vcpus'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'vcpus_total'"
op|':'
number|'4'
op|','
string|"'vcpus_used'"
op|':'
number|'8'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'1'
op|'}'
op|')'
newline|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
string|"'2'"
op|','
string|"'3'"
op|']'
op|')'
newline|'\n'
comment|'# use the minimum ratio from aggregates'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|'*'
number|'2'
op|','
name|'host'
op|'.'
name|'limits'
op|'['
string|"'vcpu'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
