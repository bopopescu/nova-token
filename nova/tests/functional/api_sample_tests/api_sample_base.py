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
name|'import'
name|'testscenarios'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'API_V21_CORE_EXTENSIONS'
comment|'# noqa'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
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
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
comment|'# API samples heavily uses testscenarios. This allows us to use the'
nl|'\n'
comment|'# same tests, with slight variations in configuration to ensure our'
nl|'\n'
comment|'# various ways of calling the API are compatible. Testscenarios works'
nl|'\n'
comment|'# through the class level ``scenarios`` variable. It is an array of'
nl|'\n'
comment|'# tuples where the first value in each tuple is an arbitrary name for'
nl|'\n'
comment|'# the scenario (should be unique), and the second item is a dictionary'
nl|'\n'
comment|'# of attributes to change in the class for the test.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# By default we're running scenarios for 2 situations"
nl|'\n'
comment|'#'
nl|'\n'
comment|'# - Hitting the default /v2 endpoint with the v2.1 Compatibility stack'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# - Hitting the default /v2.1 endpoint'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Things we need to set:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# - api_major_version - what version of the API we should be hitting'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# - microversion - what API microversion should be used'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# - _additional_fixtures - any additional fixtures need'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# NOTE(sdague): if you want to build a test that only tests specific'
nl|'\n'
comment|'# microversions, then replace the ``scenarios`` class variable in that'
nl|'\n'
comment|'# test class with something like:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# [("v2_11", {\'api_major_version\': \'v2.1\', \'microversion\': \'2.11\'})]'
nl|'\n'
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
DECL|variable|api_major_version
indent|'    '
name|'api_major_version'
op|'='
string|"'v2'"
newline|'\n'
comment|'# any additional fixtures needed for this scenario'
nl|'\n'
DECL|variable|_additional_fixtures
name|'_additional_fixtures'
op|'='
op|'['
op|']'
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
DECL|variable|_project_id
name|'_project_id'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
nl|'\n'
comment|'# test v2 with the v2.1 compatibility stack'
nl|'\n'
op|'('
string|"'v2'"
op|','
op|'{'
nl|'\n'
string|"'api_major_version'"
op|':'
string|"'v2'"
op|'}'
op|')'
op|','
nl|'\n'
comment|'# test v2.1 base microversion'
nl|'\n'
op|'('
string|"'v2_1'"
op|','
op|'{'
nl|'\n'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|','
nl|'\n'
comment|'# test v2.18 code without project id'
nl|'\n'
op|'('
string|"'v2_1_noproject_id'"
op|','
op|'{'
nl|'\n'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|','
nl|'\n'
string|"'_project_id'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'_additional_fixtures'"
op|':'
op|'['
nl|'\n'
name|'api_paste_fixture'
op|'.'
name|'ApiPasteNoProjectId'
op|']'
op|'}'
op|')'
nl|'\n'
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
name|'API_V21_CORE_EXTENSIONS'
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
nl|'\n'
comment|'# load any additional fixtures specified by the scenario'
nl|'\n'
dedent|''
name|'for'
name|'fix'
name|'in'
name|'self'
op|'.'
name|'_additional_fixtures'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fix'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# super class call is delayed here so that we have the right'
nl|'\n'
comment|"# paste and conf before loading all the services, as we can't"
nl|'\n'
comment|'# change these later.'
nl|'\n'
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
nl|'\n'
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
nl|'\n'
comment|'# this is used to generate sample docs'
nl|'\n'
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
dedent|''
dedent|''
endmarker|''
end_unit
