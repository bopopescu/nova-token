begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'v3'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HypervisorsSampleJsonTests
name|'class'
name|'HypervisorsSampleJsonTests'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-hypervisors"'
newline|'\n'
nl|'\n'
DECL|member|test_hypervisors_list
name|'def'
name|'test_hypervisors_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-list-resp'"
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
DECL|member|test_hypervisors_search
dedent|''
name|'def'
name|'test_hypervisors_search'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/search?query=fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-search-resp'"
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
DECL|member|test_hypervisors_servers
dedent|''
name|'def'
name|'test_hypervisors_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/1/servers'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-servers-resp'"
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
DECL|member|test_hypervisors_detail
dedent|''
name|'def'
name|'test_hypervisors_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hypervisor_id'
op|'='
number|'1'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'hypervisor_id'"
op|':'
name|'hypervisor_id'
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/detail'"
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-detail-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hypervisors_show
dedent|''
name|'def'
name|'test_hypervisors_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hypervisor_id'
op|'='
number|'1'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'hypervisor_id'"
op|':'
name|'hypervisor_id'
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/%s'"
op|'%'
name|'hypervisor_id'
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-show-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hypervisors_statistics
dedent|''
name|'def'
name|'test_hypervisors_statistics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/statistics'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-statistics-resp'"
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
DECL|member|test_hypervisors_uptime
dedent|''
name|'def'
name|'test_hypervisors_uptime'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_host_uptime
indent|'        '
name|'def'
name|'fake_get_host_uptime'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'hyp'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|'" 08:32:11 up 93 days, 18:25, 12 users,  load average:"'
nl|'\n'
string|'" 0.20, 0.12, 0.14"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'HostAPI'
op|','
nl|'\n'
string|"'get_host_uptime'"
op|','
name|'fake_get_host_uptime'
op|')'
newline|'\n'
name|'hypervisor_id'
op|'='
number|'1'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-hypervisors/%s/uptime'"
op|'%'
name|'hypervisor_id'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'hypervisor_id'"
op|':'
name|'hypervisor_id'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'hypervisors-uptime-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HypervisorsSampleXmlTests
dedent|''
dedent|''
name|'class'
name|'HypervisorsSampleXmlTests'
op|'('
name|'HypervisorsSampleJsonTests'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|'"xml"'
newline|'\n'
dedent|''
endmarker|''
end_unit
