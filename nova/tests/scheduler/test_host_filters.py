begin_unit
comment|'# Copyright 2011 OpenStack Foundation  # All Rights Reserved.'
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
string|'"""\nTests For Scheduler Host Filters.\n"""'
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
name|'scheduler'
name|'import'
name|'filters'
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
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostFiltersTestCase
name|'class'
name|'HostFiltersTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for host filters."""'
newline|'\n'
comment|'# FIXME(sirp): These tests still require DB access until we can separate'
nl|'\n'
comment|'# the testing of the DB API code from the host-filter code.'
nl|'\n'
DECL|variable|USES_DB
name|'USES_DB'
op|'='
name|'True'
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
name|'HostFiltersTestCase'
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
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'HostFilterHandler'
op|'('
op|')'
newline|'\n'
name|'classes'
op|'='
name|'filter_handler'
op|'.'
name|'get_matching_classes'
op|'('
nl|'\n'
op|'['
string|"'nova.scheduler.filters.all_filters'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'class_map'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'cls'
name|'in'
name|'classes'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'class_map'
op|'['
name|'cls'
op|'.'
name|'__name__'
op|']'
op|'='
name|'cls'
newline|'\n'
nl|'\n'
DECL|member|test_all_filters
dedent|''
dedent|''
name|'def'
name|'test_all_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Double check at least a couple of known filters exist'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'AllHostsFilter'"
op|','
name|'self'
op|'.'
name|'class_map'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'ComputeFilter'"
op|','
name|'self'
op|'.'
name|'class_map'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_all_host_filter
dedent|''
name|'def'
name|'test_all_host_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'self'
op|'.'
name|'class_map'
op|'['
string|"'AllHostsFilter'"
op|']'
op|'('
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
op|'{'
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
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_group_anti_affinity_filter_passes
dedent|''
name|'def'
name|'_test_group_anti_affinity_filter_passes'
op|'('
name|'self'
op|','
name|'cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'self'
op|'.'
name|'class_map'
op|'['
name|'cls'
op|']'
op|'('
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
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
string|"'affinity'"
op|']'
op|'}'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
name|'policy'
op|']'
op|'}'
newline|'\n'
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|'='
op|'['
op|']'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|'='
op|'['
string|"'host2'"
op|']'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_passes
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_passes'
op|'('
nl|'\n'
string|"'ServerGroupAntiAffinityFilter'"
op|','
string|"'anti-affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_passes_legacy
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_passes_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_passes'
op|'('
nl|'\n'
string|"'GroupAntiAffinityFilter'"
op|','
string|"'legacy'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_group_anti_affinity_filter_fails
dedent|''
name|'def'
name|'_test_group_anti_affinity_filter_fails'
op|'('
name|'self'
op|','
name|'cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'self'
op|'.'
name|'class_map'
op|'['
name|'cls'
op|']'
op|'('
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
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
name|'policy'
op|']'
op|','
nl|'\n'
string|"'group_hosts'"
op|':'
op|'['
string|"'host1'"
op|']'
op|'}'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_fails
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_fails'
op|'('
nl|'\n'
string|"'ServerGroupAntiAffinityFilter'"
op|','
string|"'anti-affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_fails_legacy
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_fails_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_fails'
op|'('
nl|'\n'
string|"'GroupAntiAffinityFilter'"
op|','
string|"'legacy'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_group_affinity_filter_passes
dedent|''
name|'def'
name|'_test_group_affinity_filter_passes'
op|'('
name|'self'
op|','
name|'cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'self'
op|'.'
name|'class_map'
op|'['
string|"'ServerGroupAffinityFilter'"
op|']'
op|'('
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
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
string|"'anti-affinity'"
op|']'
op|'}'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
string|"'affinity'"
op|']'
op|','
nl|'\n'
string|"'group_hosts'"
op|':'
op|'['
string|"'host1'"
op|']'
op|'}'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_passes
dedent|''
name|'def'
name|'test_group_affinity_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_passes'
op|'('
nl|'\n'
string|"'ServerGroupAffinityFilter'"
op|','
string|"'affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_passes_legacy
dedent|''
name|'def'
name|'test_group_affinity_filter_passes_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_passes'
op|'('
nl|'\n'
string|"'GroupAffinityFilter'"
op|','
string|"'legacy'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_group_affinity_filter_fails
dedent|''
name|'def'
name|'_test_group_affinity_filter_fails'
op|'('
name|'self'
op|','
name|'cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filt_cls'
op|'='
name|'self'
op|'.'
name|'class_map'
op|'['
name|'cls'
op|']'
op|'('
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
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
name|'policy'
op|']'
op|','
nl|'\n'
string|"'group_hosts'"
op|':'
op|'['
string|"'host2'"
op|']'
op|'}'
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
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_fails
dedent|''
name|'def'
name|'test_group_affinity_filter_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_fails'
op|'('
nl|'\n'
string|"'ServerGroupAffinityFilter'"
op|','
string|"'affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_fails_legacy
dedent|''
name|'def'
name|'test_group_affinity_filter_fails_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_fails'
op|'('
nl|'\n'
string|"'GroupAffinityFilter'"
op|','
string|"'legacy'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
