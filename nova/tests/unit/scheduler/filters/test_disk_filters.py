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
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'disk_filter'
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
DECL|class|TestDiskFilter
name|'class'
name|'TestDiskFilter'
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
name|'TestDiskFilter'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_filter_passes
dedent|''
name|'def'
name|'test_disk_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'disk_filter'
op|'.'
name|'DiskFilter'
op|'('
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'root_gb'
op|'='
number|'1'
op|','
name|'ephemeral_gb'
op|'='
number|'1'
op|','
name|'swap'
op|'='
number|'512'
op|')'
op|')'
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
string|"'free_disk_mb'"
op|':'
number|'11'
op|'*'
number|'1024'
op|','
string|"'total_usable_disk_gb'"
op|':'
number|'13'
op|','
nl|'\n'
string|"'disk_allocation_ratio'"
op|':'
number|'1.0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_filter_fails
dedent|''
name|'def'
name|'test_disk_filter_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'disk_filter'
op|'.'
name|'DiskFilter'
op|'('
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
nl|'\n'
name|'root_gb'
op|'='
number|'10'
op|','
name|'ephemeral_gb'
op|'='
number|'1'
op|','
name|'swap'
op|'='
number|'1024'
op|')'
op|')'
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
string|"'free_disk_mb'"
op|':'
number|'11'
op|'*'
number|'1024'
op|','
string|"'total_usable_disk_gb'"
op|':'
number|'13'
op|','
nl|'\n'
string|"'disk_allocation_ratio'"
op|':'
number|'1.0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_filter_oversubscribe
dedent|''
name|'def'
name|'test_disk_filter_oversubscribe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'disk_filter'
op|'.'
name|'DiskFilter'
op|'('
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
nl|'\n'
name|'root_gb'
op|'='
number|'100'
op|','
name|'ephemeral_gb'
op|'='
number|'18'
op|','
name|'swap'
op|'='
number|'1024'
op|')'
op|')'
newline|'\n'
comment|'# 1GB used... so 119GB allowed...'
nl|'\n'
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
string|"'free_disk_mb'"
op|':'
number|'11'
op|'*'
number|'1024'
op|','
string|"'total_usable_disk_gb'"
op|':'
number|'12'
op|','
nl|'\n'
string|"'disk_allocation_ratio'"
op|':'
number|'10.0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'12'
op|'*'
number|'10.0'
op|','
name|'host'
op|'.'
name|'limits'
op|'['
string|"'disk_gb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_filter_oversubscribe_fail
dedent|''
name|'def'
name|'test_disk_filter_oversubscribe_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'disk_filter'
op|'.'
name|'DiskFilter'
op|'('
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
nl|'\n'
name|'root_gb'
op|'='
number|'100'
op|','
name|'ephemeral_gb'
op|'='
number|'19'
op|','
name|'swap'
op|'='
number|'1024'
op|')'
op|')'
newline|'\n'
comment|'# 1GB used... so 119GB allowed...'
nl|'\n'
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
string|"'free_disk_mb'"
op|':'
number|'11'
op|'*'
number|'1024'
op|','
string|"'total_usable_disk_gb'"
op|':'
number|'12'
op|','
nl|'\n'
string|"'disk_allocation_ratio'"
op|':'
number|'10.0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
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
DECL|member|test_aggregate_disk_filter_value_error
name|'def'
name|'test_aggregate_disk_filter_value_error'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'disk_filter'
op|'.'
name|'AggregateDiskFilter'
op|'('
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
nl|'\n'
name|'root_gb'
op|'='
number|'1'
op|','
name|'ephemeral_gb'
op|'='
number|'1'
op|','
name|'swap'
op|'='
number|'1024'
op|')'
op|')'
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
string|"'free_disk_mb'"
op|':'
number|'3'
op|'*'
number|'1024'
op|','
nl|'\n'
string|"'total_usable_disk_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disk_allocation_ratio'"
op|':'
number|'1.0'
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
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
name|'agg_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'host'
op|','
string|"'disk_allocation_ratio'"
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
DECL|member|test_aggregate_disk_filter_default_value
name|'def'
name|'test_aggregate_disk_filter_default_value'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'disk_filter'
op|'.'
name|'AggregateDiskFilter'
op|'('
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
nl|'\n'
name|'root_gb'
op|'='
number|'2'
op|','
name|'ephemeral_gb'
op|'='
number|'1'
op|','
name|'swap'
op|'='
number|'1024'
op|')'
op|')'
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
string|"'free_disk_mb'"
op|':'
number|'3'
op|'*'
number|'1024'
op|','
nl|'\n'
string|"'total_usable_disk_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disk_allocation_ratio'"
op|':'
number|'1.0'
op|'}'
op|')'
newline|'\n'
comment|'# Uses global conf.'
nl|'\n'
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
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
name|'agg_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'host'
op|','
string|"'disk_allocation_ratio'"
op|')'
newline|'\n'
nl|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
string|"'2'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
