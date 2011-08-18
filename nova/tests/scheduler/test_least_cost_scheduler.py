begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nTests For Least Cost Scheduler\n"""'
newline|'\n'
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'least_cost'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'scheduler'
name|'import'
name|'test_abstract_scheduler'
newline|'\n'
nl|'\n'
DECL|variable|MB
name|'MB'
op|'='
number|'1024'
op|'*'
number|'1024'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHost
name|'class'
name|'FakeHost'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host_id'
op|','
name|'free_ram'
op|','
name|'io'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'id'
op|'='
name|'host_id'
newline|'\n'
name|'self'
op|'.'
name|'free_ram'
op|'='
name|'free_ram'
newline|'\n'
name|'self'
op|'.'
name|'io'
op|'='
name|'io'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WeightedSumTestCase
dedent|''
dedent|''
name|'class'
name|'WeightedSumTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_empty_domain
indent|'    '
name|'def'
name|'test_empty_domain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
op|'['
op|']'
newline|'\n'
name|'weighted_fns'
op|'='
op|'['
op|']'
newline|'\n'
name|'result'
op|'='
name|'least_cost'
op|'.'
name|'weighted_sum'
op|'('
name|'domain'
op|','
name|'weighted_fns'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_basic_costing
dedent|''
name|'def'
name|'test_basic_costing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hosts'
op|'='
op|'['
nl|'\n'
name|'FakeHost'
op|'('
number|'1'
op|','
number|'512'
op|'*'
name|'MB'
op|','
number|'100'
op|')'
op|','
nl|'\n'
name|'FakeHost'
op|'('
number|'2'
op|','
number|'256'
op|'*'
name|'MB'
op|','
number|'400'
op|')'
op|','
nl|'\n'
name|'FakeHost'
op|'('
number|'3'
op|','
number|'512'
op|'*'
name|'MB'
op|','
number|'100'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'weighted_fns'
op|'='
op|'['
nl|'\n'
op|'('
number|'1'
op|','
name|'lambda'
name|'h'
op|':'
name|'h'
op|'.'
name|'free_ram'
op|')'
op|','
comment|'# Fill-first, free_ram is a *cost*'
nl|'\n'
op|'('
number|'2'
op|','
name|'lambda'
name|'h'
op|':'
name|'h'
op|'.'
name|'io'
op|')'
op|','
comment|'# Avoid high I/O'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'costs'
op|'='
name|'least_cost'
op|'.'
name|'weighted_sum'
op|'('
nl|'\n'
name|'domain'
op|'='
name|'hosts'
op|','
name|'weighted_fns'
op|'='
name|'weighted_fns'
op|')'
newline|'\n'
nl|'\n'
comment|'# Each 256 MB unit of free-ram contributes 0.5 points by way of:'
nl|'\n'
comment|'#   cost = weight * (score/max_score) = 1 * (256/512) = 0.5'
nl|'\n'
comment|'# Each 100 iops of IO adds 0.5 points by way of:'
nl|'\n'
comment|'#   cost = 2 * (100/400) = 2 * 0.25 = 0.5'
nl|'\n'
name|'expected'
op|'='
op|'['
number|'1.5'
op|','
number|'2.5'
op|','
number|'1.5'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'costs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LeastCostSchedulerTestCase
dedent|''
dedent|''
name|'class'
name|'LeastCostSchedulerTestCase'
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
name|'LeastCostSchedulerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeZoneManager
name|'class'
name|'FakeZoneManager'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'zone_manager'
op|'='
name|'FakeZoneManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'states'
op|'='
name|'test_abstract_scheduler'
op|'.'
name|'fake_zone_manager_service_states'
op|'('
nl|'\n'
DECL|variable|num_hosts
name|'num_hosts'
op|'='
number|'10'
op|')'
newline|'\n'
name|'zone_manager'
op|'.'
name|'service_states'
op|'='
name|'states'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'sched'
op|'='
name|'least_cost'
op|'.'
name|'LeastCostScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sched'
op|'.'
name|'zone_manager'
op|'='
name|'zone_manager'
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
name|'LeastCostSchedulerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertWeights
dedent|''
name|'def'
name|'assertWeights'
op|'('
name|'self'
op|','
name|'expected'
op|','
name|'num'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'weighted'
op|'='
name|'self'
op|'.'
name|'sched'
op|'.'
name|'weigh_hosts'
op|'('
string|'"compute"'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDictListMatch'
op|'('
name|'weighted'
op|','
name|'expected'
op|','
name|'approx_equal'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_hosts
dedent|''
name|'def'
name|'test_no_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'num'
op|'='
number|'1'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertWeights'
op|'('
name|'expected'
op|','
name|'num'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_noop_cost_fn
dedent|''
name|'def'
name|'test_noop_cost_fn'
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
name|'least_cost_scheduler_cost_functions'
op|'='
op|'['
nl|'\n'
string|"'nova.scheduler.least_cost.noop_cost_fn'"
op|']'
op|','
nl|'\n'
name|'noop_cost_fn_weight'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'num'
op|'='
number|'1'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'sched'
op|'.'
name|'filter_hosts'
op|'('
name|'num'
op|','
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'hostname'
op|'='
name|'hostname'
op|')'
nl|'\n'
name|'for'
name|'hostname'
op|','
name|'caps'
name|'in'
name|'hosts'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertWeights'
op|'('
name|'expected'
op|','
name|'num'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cost_fn_weights
dedent|''
name|'def'
name|'test_cost_fn_weights'
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
name|'least_cost_scheduler_cost_functions'
op|'='
op|'['
nl|'\n'
string|"'nova.scheduler.least_cost.noop_cost_fn'"
op|']'
op|','
nl|'\n'
name|'noop_cost_fn_weight'
op|'='
number|'2'
op|')'
newline|'\n'
nl|'\n'
name|'num'
op|'='
number|'1'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'sched'
op|'.'
name|'filter_hosts'
op|'('
name|'num'
op|','
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'dict'
op|'('
name|'weight'
op|'='
number|'2'
op|','
name|'hostname'
op|'='
name|'hostname'
op|')'
nl|'\n'
name|'for'
name|'hostname'
op|','
name|'caps'
name|'in'
name|'hosts'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertWeights'
op|'('
name|'expected'
op|','
name|'num'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_compute_fill_first_cost_fn
dedent|''
name|'def'
name|'test_compute_fill_first_cost_fn'
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
name|'least_cost_scheduler_cost_functions'
op|'='
op|'['
nl|'\n'
string|"'nova.scheduler.least_cost.compute_fill_first_cost_fn'"
op|']'
op|','
nl|'\n'
name|'compute_fill_first_cost_fn_weight'
op|'='
number|'1'
op|')'
newline|'\n'
name|'num'
op|'='
number|'1'
newline|'\n'
name|'instance_type'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'1024'
op|'}'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'instance_type'"
op|':'
name|'instance_type'
op|'}'
newline|'\n'
name|'svc_states'
op|'='
name|'self'
op|'.'
name|'sched'
op|'.'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'iteritems'
op|'('
op|')'
newline|'\n'
name|'all_hosts'
op|'='
op|'['
op|'('
name|'host'
op|','
name|'services'
op|'['
string|'"compute"'
op|']'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'svc_states'
nl|'\n'
name|'if'
string|'"compute"'
name|'in'
name|'services'
op|']'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'sched'
op|'.'
name|'filter_hosts'
op|'('
string|"'compute'"
op|','
name|'request_spec'
op|','
name|'all_hosts'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'idx'
op|','
op|'('
name|'hostname'
op|','
name|'services'
op|')'
name|'in'
name|'enumerate'
op|'('
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'caps'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'services'
op|'['
string|'"compute"'
op|']'
op|')'
newline|'\n'
comment|'# Costs are normalized so over 10 hosts, each host with increasing'
nl|'\n'
comment|'# free ram will cost 1/N more. Since the lowest cost host has some'
nl|'\n'
comment|'# free ram, we add in the 1/N for the base_cost'
nl|'\n'
name|'weight'
op|'='
number|'0.1'
op|'+'
op|'('
number|'0.1'
op|'*'
name|'idx'
op|')'
newline|'\n'
name|'wtd_dict'
op|'='
name|'dict'
op|'('
name|'hostname'
op|'='
name|'hostname'
op|','
name|'weight'
op|'='
name|'weight'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'caps'
op|')'
newline|'\n'
name|'expected'
op|'.'
name|'append'
op|'('
name|'wtd_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertWeights'
op|'('
name|'expected'
op|','
name|'num'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
