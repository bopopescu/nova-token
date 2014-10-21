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
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'isolated_hosts_filter'
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
DECL|class|TestIsolatedHostsFilter
name|'class'
name|'TestIsolatedHostsFilter'
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
name|'TestIsolatedHostsFilter'
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
name|'isolated_hosts_filter'
op|'.'
name|'IsolatedHostsFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_test_isolated_hosts
dedent|''
name|'def'
name|'_do_test_isolated_hosts'
op|'('
name|'self'
op|','
name|'host_in_list'
op|','
name|'image_in_list'
op|','
nl|'\n'
name|'set_flags'
op|'='
name|'True'
op|','
nl|'\n'
name|'restrict_isolated_hosts_to_isolated_images'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'set_flags'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'isolated_images'
op|'='
op|'['
string|"'isolated_image'"
op|']'
op|','
nl|'\n'
name|'isolated_hosts'
op|'='
op|'['
string|"'isolated_host'"
op|']'
op|','
nl|'\n'
name|'restrict_isolated_hosts_to_isolated_images'
op|'='
nl|'\n'
name|'restrict_isolated_hosts_to_isolated_images'
op|')'
newline|'\n'
dedent|''
name|'host_name'
op|'='
string|"'isolated_host'"
name|'if'
name|'host_in_list'
name|'else'
string|"'free_host'"
newline|'\n'
name|'image_ref'
op|'='
string|"'isolated_image'"
name|'if'
name|'image_in_list'
name|'else'
string|"'free_image'"
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
nl|'\n'
string|"'request_spec'"
op|':'
op|'{'
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
string|"'image_ref'"
op|':'
name|'image_ref'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
name|'host_name'
op|','
string|"'node'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
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
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_fails_isolated_on_non_isolated
dedent|''
name|'def'
name|'test_isolated_hosts_fails_isolated_on_non_isolated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_fails_non_isolated_on_isolated
dedent|''
name|'def'
name|'test_isolated_hosts_fails_non_isolated_on_isolated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_passes_isolated_on_isolated
dedent|''
name|'def'
name|'test_isolated_hosts_passes_isolated_on_isolated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_passes_non_isolated_on_non_isolated
dedent|''
name|'def'
name|'test_isolated_hosts_passes_non_isolated_on_non_isolated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_no_config
dedent|''
name|'def'
name|'test_isolated_hosts_no_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# If there are no hosts nor isolated images in the config, it should'
nl|'\n'
comment|'# not filter at all. This is the default config.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'False'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'False'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_no_hosts_config
dedent|''
name|'def'
name|'test_isolated_hosts_no_hosts_config'
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
name|'isolated_images'
op|'='
op|'['
string|"'isolated_image'"
op|']'
op|')'
newline|'\n'
comment|'# If there are no hosts in the config, it should only filter out'
nl|'\n'
comment|'# images that are listed'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'False'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'False'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_no_images_config
dedent|''
name|'def'
name|'test_isolated_hosts_no_images_config'
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
name|'isolated_hosts'
op|'='
op|'['
string|"'isolated_host'"
op|']'
op|')'
newline|'\n'
comment|'# If there are no images in the config, it should only filter out'
nl|'\n'
comment|'# isolated_hosts'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'False'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'False'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_isolated_hosts_less_restrictive
dedent|''
name|'def'
name|'test_isolated_hosts_less_restrictive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# If there are isolated hosts and non isolated images'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'False'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
comment|'# If there are isolated hosts and isolated images'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'True'
op|','
name|'True'
op|','
name|'True'
op|','
name|'False'
op|')'
op|')'
newline|'\n'
comment|'# If there are non isolated hosts and non isolated images'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'False'
op|','
name|'True'
op|','
nl|'\n'
name|'False'
op|')'
op|')'
newline|'\n'
comment|'# If there are non isolated hosts and isolated images'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'_do_test_isolated_hosts'
op|'('
name|'False'
op|','
name|'True'
op|','
name|'True'
op|','
nl|'\n'
name|'False'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
