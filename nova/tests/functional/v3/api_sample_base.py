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
name|'import'
name|'testtools'
newline|'\n'
nl|'\n'
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
name|'api_samples_test_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'v3'
name|'import'
name|'api_paste_fixture'
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
name|'ApiSampleTestBaseV3'
op|'('
name|'testscenarios'
op|'.'
name|'WithScenarios'
op|','
nl|'\n'
DECL|class|ApiSampleTestBaseV3
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
string|"'v3'"
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
comment|'# TODO(gmann): Below condition is to skip the tests which running'
nl|'\n'
comment|"# for 'v2' and have not been merged yet. Once all tests are merged"
nl|'\n'
comment|'# this condition needs to be removed.'
nl|'\n'
indent|'        '
name|'if'
op|'('
name|'hasattr'
op|'('
name|'self'
op|','
string|"'_test'"
op|')'
name|'and'
nl|'\n'
op|'('
name|'self'
op|'.'
name|'_test'
op|'=='
string|"'v2'"
op|')'
name|'and'
nl|'\n'
op|'('
name|'self'
op|'.'
name|'_api_version'
op|'=='
string|"'v3'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'testtools'
op|'.'
name|'TestCase'
op|'.'
name|'skipException'
op|'('
string|"'tests are not merged yet'"
op|')'
newline|'\n'
dedent|''
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
string|"'osapi_v3'"
op|')'
newline|'\n'
comment|'# TODO(gmann): Currently redirecting only merged tests'
nl|'\n'
comment|'# after merging all tests, second condition needs to be removed.'
nl|'\n'
dedent|''
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
nl|'\n'
op|'('
op|'('
name|'self'
op|'.'
name|'_test'
op|'=='
string|"'v2.1'"
op|')'
name|'and'
op|'('
name|'self'
op|'.'
name|'_api_version'
op|'=='
string|"'v2'"
op|')'
op|')'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(gmann)For v2.1 API testing, override /v2 endpoint with v2.1'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'api_paste_fixture'
op|'.'
name|'ApiPasteFixture'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'ApiSampleTestBaseV3'
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
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_sample_path
name|'def'
name|'_get_sample_path'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'dirname'
op|','
name|'suffix'
op|'='
string|"''"
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parts'
op|'='
op|'['
name|'dirname'
op|']'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
string|"'api_samples'"
op|')'
newline|'\n'
name|'if'
name|'cls'
op|'.'
name|'all_extensions'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
string|"'all_extensions'"
op|')'
newline|'\n'
comment|'# Note(gmann): if _use_common_server_api_samples is set to True'
nl|'\n'
comment|"# then common server sample files present in 'servers' directory"
nl|'\n'
comment|'# will be used.'
nl|'\n'
dedent|''
name|'elif'
name|'cls'
op|'.'
name|'_use_common_server_api_samples'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
string|"'servers'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'cls'
op|'.'
name|'sample_dir'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
name|'cls'
op|'.'
name|'sample_dir'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'cls'
op|'.'
name|'extension_name'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
name|'cls'
op|'.'
name|'extension_name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'api_version'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
string|"'v'"
op|'+'
name|'api_version'
op|')'
newline|'\n'
dedent|''
name|'parts'
op|'.'
name|'append'
op|'('
name|'name'
op|'+'
string|'"."'
op|'+'
name|'cls'
op|'.'
name|'ctype'
op|'+'
name|'suffix'
op|')'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
op|'*'
name|'parts'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_sample
name|'def'
name|'_get_sample'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
newline|'\n'
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'dirname'
op|','
nl|'\n'
string|'"../../../../doc/v3"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_get_sample_path'
op|'('
name|'name'
op|','
name|'dirname'
op|','
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_template
name|'def'
name|'_get_template'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_get_sample_path'
op|'('
name|'name'
op|','
name|'dirname'
op|','
name|'suffix'
op|'='
string|"'.tpl'"
op|','
nl|'\n'
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
