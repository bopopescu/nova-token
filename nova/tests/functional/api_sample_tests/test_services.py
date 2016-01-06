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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'test_services'
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
DECL|class|ServicesJsonTest
name|'class'
name|'ServicesJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-services"'
newline|'\n'
DECL|variable|microversion
name|'microversion'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'ServicesJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.services.Services'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.extended_services_delete.'"
nl|'\n'
string|"'Extended_services_delete'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.extended_services.Extended_services'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'stub_out'
op|'('
string|'"nova.db.service_get_all"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_db_api_service_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"oslo_utils.timeutils.utcnow"'
op|','
name|'test_services'
op|'.'
name|'fake_utcnow'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"oslo_utils.timeutils.utcnow_ts"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_utcnow_ts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.db.service_get_by_host_and_binary"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_service_get_by_host_binary'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.db.service_update"'
op|','
nl|'\n'
name|'test_services'
op|'.'
name|'fake_service_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'timeutils'
op|'.'
name|'clear_time_override'
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
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
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
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
op|')'
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
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
op|')'
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
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
op|')'
newline|'\n'
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
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'204'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'""'
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServicesV211JsonTest
dedent|''
dedent|''
name|'class'
name|'ServicesV211JsonTest'
op|'('
name|'ServicesJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|microversion
indent|'    '
name|'microversion'
op|'='
string|"'2.11'"
newline|'\n'
comment|'# NOTE(gryf): There is no need to run those tests on v2 API. Only'
nl|'\n'
comment|'# scenarios for v2_11 will be run.'
nl|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_11'"
op|','
op|'{'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_services_list
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
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
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
string|"'forced_down'"
op|':'
string|"'false'"
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
DECL|member|test_force_down
dedent|''
name|'def'
name|'test_force_down'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set forced_down flag"""'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|'"host"'
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'forced_down'"
op|':'
string|"'true'"
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-services/force-down'"
op|','
nl|'\n'
string|"'service-force-down-put-req'"
op|','
name|'subs'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'service-force-down-put-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
