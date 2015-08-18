begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'testscenarios'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'API_V3_CORE_EXTENSIONS'
comment|'# noqa'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'compute'
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
name|'functional'
name|'import'
name|'api_paste_fixture'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
name|'import'
name|'api_samples_test_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_utils'
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
name|'class'
name|'ApiSampleTestBaseV21'
op|'('
name|'testscenarios'
op|'.'
name|'WithScenarios'
op|','
nl|'\n'
DECL|class|ApiSampleTestBaseV21
name|'api_samples_test_base'
op|'.'
name|'ApiSampleTestBase'
op|')'
op|':'
newline|'\n'
DECL|variable|_api_version
indent|'    '
name|'_api_version'
op|'='
string|"'v2'"
newline|'\n'
DECL|variable|sample_dir
name|'sample_dir'
op|'='
name|'None'
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
name|'None'
newline|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2'"
op|','
op|'{'
string|"'_test'"
op|':'
string|"'v2'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'v2_1'"
op|','
op|'{'
string|"'_test'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'v2_1_compatible'"
op|','
op|'{'
string|"'_test'"
op|':'
string|"'v2.1_compatible'"
op|'}'
op|')'
op|']'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_ipv6'
op|'='
name|'False'
op|','
nl|'\n'
name|'osapi_compute_link_prefix'
op|'='
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|','
nl|'\n'
name|'osapi_glance_link_prefix'
op|'='
name|'self'
op|'.'
name|'_get_glance_host'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'all_extensions'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'osapi_compute_extension'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
comment|'# Set the whitelist to ensure only the extensions we are'
nl|'\n'
comment|"# interested in are loaded so the api samples don't include"
nl|'\n'
comment|'# data from extensions we are not interested in'
nl|'\n'
name|'whitelist'
op|'='
name|'API_V3_CORE_EXTENSIONS'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'extension_name'
op|':'
newline|'\n'
indent|'                '
name|'whitelist'
op|'.'
name|'add'
op|'('
name|'self'
op|'.'
name|'extension_name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'extra_extensions_to_load'
op|':'
newline|'\n'
indent|'                '
name|'whitelist'
op|'.'
name|'update'
op|'('
name|'set'
op|'('
name|'self'
op|'.'
name|'extra_extensions_to_load'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_whitelist'"
op|','
name|'whitelist'
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
dedent|''
name|'expected_middleware'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'hasattr'
op|'('
name|'self'
op|','
string|"'_test'"
op|')'
name|'or'
op|'('
name|'self'
op|'.'
name|'_test'
op|'=='
string|"'v2.1'"
op|')'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(gmann): we should run v21 tests on /v2.1 but then we need'
nl|'\n'
comment|'# two sets of sample files as api version (v2 or v2.1) is being'
nl|'\n'
comment|"# added in response's link/namespace etc"
nl|'\n'
comment|'# override /v2 in compatibility mode with v2.1'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'api_paste_fixture'
op|'.'
name|'ApiPasteV21Fixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'expected_middleware'
op|'='
op|'['
name|'compute'
op|'.'
name|'APIRouterV21'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'_test'
op|'=='
string|"'v2.1_compatible'"
op|':'
newline|'\n'
indent|'            '
name|'expected_middleware'
op|'='
op|'['
name|'openstack'
op|'.'
name|'LegacyV2CompatibleWrapper'
op|','
nl|'\n'
name|'compute'
op|'.'
name|'APIRouterV21'
op|']'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'self'
op|'.'
name|'_test'
op|'=='
string|"'v2'"
name|'and'
name|'self'
op|'.'
name|'_api_version'
op|'=='
string|"'v2'"
op|')'
op|':'
newline|'\n'
comment|'# override /v2 in compatibility mode with v2 legacy'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'api_paste_fixture'
op|'.'
name|'ApiPasteLegacyV2Fixture'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'ApiSampleTestBaseV21'
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
name|'useFixture'
op|'('
name|'test'
op|'.'
name|'SampleNetworks'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
name|'fake_network'
op|'.'
name|'stub_compute_with_ips'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fake_utils'
op|'.'
name|'stub_out_utils_spawn_n'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'generate_samples'
op|'='
name|'os'
op|'.'
name|'getenv'
op|'('
string|"'GENERATE_SAMPLES'"
op|')'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'if'
name|'expected_middleware'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_api_endpoint'
op|'('
string|"'/v2'"
op|','
name|'expected_middleware'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
