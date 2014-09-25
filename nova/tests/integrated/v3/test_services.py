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
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'test_services'
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
DECL|class|ServicesJsonTest
name|'class'
name|'ServicesJsonTest'
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
string|'"os-services"'
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
name|'ServicesJsonTest'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"service_get_all"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_db_api_service_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'timeutils'
op|','
string|'"utcnow"'
op|','
name|'test_services'
op|'.'
name|'fake_utcnow'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'timeutils'
op|','
string|'"utcnow_ts"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_utcnow_ts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"service_get_by_args"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_service_get_by_host_binary'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"service_update"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_service_update'
op|')'
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
name|'ServicesJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'clear_time_override'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_services_list
dedent|''
name|'def'
name|'test_services_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of all agent builds."""'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-services'"
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'disabled'"
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'up'"
op|'}'
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
string|"'services-list-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_enable
dedent|''
name|'def'
name|'test_service_enable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Enable an existing agent build."""'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|'"host"'
op|':'
string|'"host1"'
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-services/enable'"
op|','
nl|'\n'
string|"'service-enable-put-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|'"host"'
op|':'
string|'"host1"'
op|','
nl|'\n'
string|'"binary"'
op|':'
string|'"nova-compute"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'service-enable-put-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_disable
dedent|''
name|'def'
name|'test_service_disable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disable an existing agent build."""'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|'"host"'
op|':'
string|'"host1"'
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-services/disable'"
op|','
nl|'\n'
string|"'service-disable-put-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|'"host"'
op|':'
string|'"host1"'
op|','
nl|'\n'
string|'"binary"'
op|':'
string|'"nova-compute"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'service-disable-put-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_disable_log_reason
dedent|''
name|'def'
name|'test_service_disable_log_reason'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disable an existing service and log the reason."""'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|'"host"'
op|':'
string|'"host1"'
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test2'"
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-services/disable-log-reason'"
op|','
nl|'\n'
string|"'service-disable-log-put-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'service-disable-log-put-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_delete
dedent|''
name|'def'
name|'test_service_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete an existing service."""'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-services/1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'204'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content'
op|','
string|'""'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
