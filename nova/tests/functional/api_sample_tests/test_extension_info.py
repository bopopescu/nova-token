begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
name|'as'
name|'api_extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
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
nl|'\n'
DECL|function|fake_soft_extension_authorizer
name|'def'
name|'fake_soft_extension_authorizer'
op|'('
name|'extension_name'
op|','
name|'core'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
DECL|function|authorize
indent|'    '
name|'def'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'authorize'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionInfoAllSamplesJsonTest
dedent|''
name|'class'
name|'ExtensionInfoAllSamplesJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'api_extensions'
op|','
string|"'os_compute_soft_authorizer'"
op|')'
newline|'\n'
DECL|member|test_list_extensions
name|'def'
name|'test_list_extensions'
op|'('
name|'self'
op|','
name|'soft_auth'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'soft_auth'
op|'.'
name|'side_effect'
op|'='
name|'fake_soft_extension_authorizer'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'extensions'"
op|')'
newline|'\n'
comment|'# The full extension list is one of the places that things are'
nl|'\n'
comment|'# different between the API versions and the legacy vs. new'
nl|'\n'
comment|'# stack. We default to the v2.1 case.'
nl|'\n'
name|'template'
op|'='
string|"'extensions-list-resp'"
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'api_major_version'
op|'=='
string|"'v2'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_legacy_v2_code'
op|':'
newline|'\n'
indent|'                '
name|'template'
op|'='
string|"'extensions-list-resp-v2'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'template'
op|'='
string|"'extensions-list-resp-v21-compatible'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_verify_response'
op|'('
name|'template'
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionInfoSamplesJsonTest
dedent|''
dedent|''
name|'class'
name|'ExtensionInfoSamplesJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|'"extension-info"'
newline|'\n'
DECL|variable|all_extensions
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'api_extensions'
op|','
string|"'os_compute_soft_authorizer'"
op|')'
newline|'\n'
DECL|member|test_get_extensions
name|'def'
name|'test_get_extensions'
op|'('
name|'self'
op|','
name|'soft_auth'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'soft_auth'
op|'.'
name|'side_effect'
op|'='
name|'fake_soft_extension_authorizer'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'extensions/os-agents'"
op|')'
newline|'\n'
comment|'# The extension details info are different between legacy v2 and v2.1'
nl|'\n'
comment|'# stack. namespace link and updated date are different. So keep both'
nl|'\n'
comment|'# version for testing and default to v2.1'
nl|'\n'
name|'template'
op|'='
string|"'extensions-get-resp'"
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_legacy_v2_code'
op|':'
newline|'\n'
indent|'            '
name|'template'
op|'='
string|"'extensions-get-resp-v2'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_verify_response'
op|'('
name|'template'
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
