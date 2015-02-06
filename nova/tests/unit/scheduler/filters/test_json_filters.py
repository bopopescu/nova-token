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
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'json_filter'
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
DECL|class|TestJsonFilter
name|'class'
name|'TestJsonFilter'
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
name|'TestJsonFilter'
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
name|'filt_cls'
op|'='
name|'json_filter'
op|'.'
name|'JsonFilter'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'json_query'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
nl|'\n'
op|'['
string|"'and'"
op|','
op|'['
string|"'>='"
op|','
string|"'$free_ram_mb'"
op|','
number|'1024'
op|']'
op|','
nl|'\n'
op|'['
string|"'>='"
op|','
string|"'$free_disk_mb'"
op|','
number|'200'
op|'*'
number|'1024'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_json_filter_passes
dedent|''
name|'def'
name|'test_json_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'query'"
op|':'
name|'self'
op|'.'
name|'json_query'
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
string|"'free_ram_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'200'
op|'*'
number|'1024'
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
DECL|member|test_json_filter_passes_with_no_query
dedent|''
name|'def'
name|'test_json_filter_passes_with_no_query'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
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
string|"'free_ram_mb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'0'
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
DECL|member|test_json_filter_fails_on_memory
dedent|''
name|'def'
name|'test_json_filter_fails_on_memory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'query'"
op|':'
name|'self'
op|'.'
name|'json_query'
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
string|"'free_ram_mb'"
op|':'
number|'1023'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'200'
op|'*'
number|'1024'
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
DECL|member|test_json_filter_fails_on_disk
dedent|''
name|'def'
name|'test_json_filter_fails_on_disk'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'query'"
op|':'
name|'self'
op|'.'
name|'json_query'
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
string|"'free_ram_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
op|'('
number|'200'
op|'*'
number|'1024'
op|')'
op|'-'
number|'1'
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
DECL|member|test_json_filter_fails_on_service_disabled
dedent|''
name|'def'
name|'test_json_filter_fails_on_service_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'json_query'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
nl|'\n'
op|'['
string|"'and'"
op|','
op|'['
string|"'>='"
op|','
string|"'$free_ram_mb'"
op|','
number|'1024'
op|']'
op|','
nl|'\n'
op|'['
string|"'>='"
op|','
string|"'$free_disk_mb'"
op|','
number|'200'
op|'*'
number|'1024'
op|']'
op|','
nl|'\n'
op|'['
string|"'not'"
op|','
string|"'$service.disabled'"
op|']'
op|']'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'200'
op|'}'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
string|"'query'"
op|':'
name|'json_query'
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
string|"'free_ram_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'200'
op|'*'
number|'1024'
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
DECL|member|test_json_filter_happy_day
dedent|''
name|'def'
name|'test_json_filter_happy_day'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test json filter more thoroughly.'
nl|'\n'
indent|'        '
name|'raw'
op|'='
op|'['
string|"'and'"
op|','
nl|'\n'
string|"'$capabilities.enabled'"
op|','
nl|'\n'
op|'['
string|"'='"
op|','
string|"'$capabilities.opt1'"
op|','
string|"'match'"
op|']'
op|','
nl|'\n'
op|'['
string|"'or'"
op|','
nl|'\n'
op|'['
string|"'and'"
op|','
nl|'\n'
op|'['
string|"'<'"
op|','
string|"'$free_ram_mb'"
op|','
number|'30'
op|']'
op|','
nl|'\n'
op|'['
string|"'<'"
op|','
string|"'$free_disk_mb'"
op|','
number|'300'
op|']'
op|']'
op|','
nl|'\n'
op|'['
string|"'and'"
op|','
nl|'\n'
op|'['
string|"'>'"
op|','
string|"'$free_ram_mb'"
op|','
number|'30'
op|']'
op|','
nl|'\n'
op|'['
string|"'>'"
op|','
string|"'$free_disk_mb'"
op|','
number|'300'
op|']'
op|']'
op|']'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Passes'
nl|'\n'
name|'capabilities'
op|'='
op|'{'
string|"'opt1'"
op|':'
string|"'match'"
op|'}'
newline|'\n'
name|'service'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'False'
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
string|"'free_ram_mb'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'200'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'capabilities'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
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
comment|'# Passes'
nl|'\n'
name|'capabilities'
op|'='
op|'{'
string|"'opt1'"
op|':'
string|"'match'"
op|'}'
newline|'\n'
name|'service'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'False'
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
string|"'free_ram_mb'"
op|':'
number|'40'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'400'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'capabilities'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
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
comment|'# Fails due to capabilities being disabled'
nl|'\n'
name|'capabilities'
op|'='
op|'{'
string|"'enabled'"
op|':'
name|'False'
op|','
string|"'opt1'"
op|':'
string|"'match'"
op|'}'
newline|'\n'
name|'service'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'False'
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
string|"'free_ram_mb'"
op|':'
number|'40'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'400'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'capabilities'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
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
comment|"# Fails due to being exact memory/disk we don't want"
nl|'\n'
name|'capabilities'
op|'='
op|'{'
string|"'enabled'"
op|':'
name|'True'
op|','
string|"'opt1'"
op|':'
string|"'match'"
op|'}'
newline|'\n'
name|'service'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'False'
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
string|"'free_ram_mb'"
op|':'
number|'30'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'300'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'capabilities'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
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
comment|'# Fails due to memory lower but disk higher'
nl|'\n'
name|'capabilities'
op|'='
op|'{'
string|"'enabled'"
op|':'
name|'True'
op|','
string|"'opt1'"
op|':'
string|"'match'"
op|'}'
newline|'\n'
name|'service'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'False'
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
string|"'free_ram_mb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'400'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'capabilities'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
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
comment|"# Fails due to capabilities 'opt1' not equal"
nl|'\n'
name|'capabilities'
op|'='
op|'{'
string|"'enabled'"
op|':'
name|'True'
op|','
string|"'opt1'"
op|':'
string|"'no-match'"
op|'}'
newline|'\n'
name|'service'
op|'='
op|'{'
string|"'enabled'"
op|':'
name|'True'
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
string|"'free_ram_mb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'free_disk_mb'"
op|':'
number|'400'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'capabilities'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
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
DECL|member|test_json_filter_basic_operators
dedent|''
name|'def'
name|'test_json_filter_basic_operators'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
comment|'# (operator, arguments, expected_result)'
nl|'\n'
name|'ops_to_test'
op|'='
op|'['
nl|'\n'
op|'['
string|"'='"
op|','
op|'['
number|'1'
op|','
number|'1'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'='"
op|','
op|'['
number|'1'
op|','
number|'2'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'<'"
op|','
op|'['
number|'1'
op|','
number|'2'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'<'"
op|','
op|'['
number|'1'
op|','
number|'1'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'<'"
op|','
op|'['
number|'2'
op|','
number|'1'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'>'"
op|','
op|'['
number|'2'
op|','
number|'1'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'>'"
op|','
op|'['
number|'2'
op|','
number|'2'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'>'"
op|','
op|'['
number|'2'
op|','
number|'3'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'<='"
op|','
op|'['
number|'1'
op|','
number|'2'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'<='"
op|','
op|'['
number|'1'
op|','
number|'1'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'<='"
op|','
op|'['
number|'2'
op|','
number|'1'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'>='"
op|','
op|'['
number|'2'
op|','
number|'1'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'>='"
op|','
op|'['
number|'2'
op|','
number|'2'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'>='"
op|','
op|'['
number|'2'
op|','
number|'3'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'in'"
op|','
op|'['
number|'1'
op|','
number|'1'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'in'"
op|','
op|'['
number|'1'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'in'"
op|','
op|'['
number|'4'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'not'"
op|','
op|'['
name|'True'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'not'"
op|','
op|'['
name|'False'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'or'"
op|','
op|'['
name|'True'
op|','
name|'False'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'or'"
op|','
op|'['
name|'False'
op|','
name|'False'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'and'"
op|','
op|'['
name|'True'
op|','
name|'True'
op|']'
op|','
name|'True'
op|']'
op|','
nl|'\n'
op|'['
string|"'and'"
op|','
op|'['
name|'False'
op|','
name|'False'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
op|'['
string|"'and'"
op|','
op|'['
name|'True'
op|','
name|'False'
op|']'
op|','
name|'False'
op|']'
op|','
nl|'\n'
comment|'# Nested ((True or False) and (2 > 1)) == Passes'
nl|'\n'
op|'['
string|"'and'"
op|','
op|'['
op|'['
string|"'or'"
op|','
name|'True'
op|','
name|'False'
op|']'
op|','
op|'['
string|"'>'"
op|','
number|'2'
op|','
number|'1'
op|']'
op|']'
op|','
name|'True'
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'op'
op|','
name|'args'
op|','
name|'expected'
op|')'
name|'in'
name|'ops_to_test'
op|':'
newline|'\n'
indent|'            '
name|'raw'
op|'='
op|'['
name|'op'
op|']'
op|'+'
name|'args'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
nl|'\n'
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
comment|'# This results in [False, True, False, True] and if any are True'
nl|'\n'
comment|'# then it passes...'
nl|'\n'
dedent|''
name|'raw'
op|'='
op|'['
string|"'not'"
op|','
name|'True'
op|','
name|'False'
op|','
name|'True'
op|','
name|'False'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
comment|'# This results in [False, False, False] and if any are True'
nl|'\n'
comment|"# then it passes...which this doesn't"
nl|'\n'
name|'raw'
op|'='
op|'['
string|"'not'"
op|','
name|'True'
op|','
name|'True'
op|','
name|'True'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
DECL|member|test_json_filter_unknown_operator_raises
dedent|''
name|'def'
name|'test_json_filter_unknown_operator_raises'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raw'
op|'='
op|'['
string|"'!='"
op|','
number|'1'
op|','
number|'2'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
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
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'KeyError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|','
name|'host'
op|','
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_json_filter_empty_filters_pass
dedent|''
name|'def'
name|'test_json_filter_empty_filters_pass'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'raw'
op|'='
op|'['
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
name|'raw'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
DECL|member|test_json_filter_invalid_num_arguments_fails
dedent|''
name|'def'
name|'test_json_filter_invalid_num_arguments_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'raw'
op|'='
op|'['
string|"'>'"
op|','
op|'['
string|"'and'"
op|','
op|'['
string|"'or'"
op|','
op|'['
string|"'not'"
op|','
op|'['
string|"'<'"
op|','
op|'['
string|"'>='"
op|','
op|'['
string|"'<='"
op|','
op|'['
string|"'in'"
op|','
op|']'
op|']'
op|']'
op|']'
op|']'
op|']'
op|']'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
name|'raw'
op|'='
op|'['
string|"'>'"
op|','
number|'1'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
DECL|member|test_json_filter_unknown_variable_ignored
dedent|''
name|'def'
name|'test_json_filter_unknown_variable_ignored'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'raw'
op|'='
op|'['
string|"'='"
op|','
string|"'$........'"
op|','
number|'1'
op|','
number|'1'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
name|'raw'
op|'='
op|'['
string|"'='"
op|','
string|"'$foo'"
op|','
number|'2'
op|','
number|'2'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'query'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'raw'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
dedent|''
dedent|''
endmarker|''
end_unit
