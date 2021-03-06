begin_unit
comment|'# All Rights Reserved.'
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
name|'oslo_utils'
name|'import'
name|'fixture'
name|'as'
name|'utils_fixture'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'notification_sample_tests'
name|'import'
name|'notification_sample_base'
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
nl|'\n'
name|'class'
name|'TestServiceUpdateNotificationSample'
op|'('
nl|'\n'
DECL|class|TestServiceUpdateNotificationSample
name|'notification_sample_base'
op|'.'
name|'NotificationSampleTestBase'
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
name|'TestServiceUpdateNotificationSample'
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
name|'useFixture'
op|'('
name|'utils_fixture'
op|'.'
name|'TimeFixture'
op|'('
name|'test_services'
op|'.'
name|'fake_utcnow'
op|'('
op|')'
op|')'
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
name|'body'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'api_put'
op|'('
string|"'os-services/enable'"
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_notification'
op|'('
string|"'service-update'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_disabled
dedent|''
name|'def'
name|'test_service_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|"'nova-compute'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'api_put'
op|'('
string|"'os-services/disable'"
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_notification'
op|'('
string|"'service-update'"
op|','
nl|'\n'
name|'replacements'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_disabled_log_reason
dedent|''
name|'def'
name|'test_service_disabled_log_reason'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
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
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'api_put'
op|'('
string|"'os-services/disable-log-reason'"
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_notification'
op|'('
string|"'service-update'"
op|','
nl|'\n'
name|'replacements'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test2'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_force_down
dedent|''
name|'def'
name|'test_service_force_down'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'host'"
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
name|'True'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'microversion'
op|'='
string|"'2.12'"
newline|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'api_put'
op|'('
string|"'os-services/force-down'"
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_notification'
op|'('
string|"'service-update'"
op|','
nl|'\n'
name|'replacements'
op|'='
op|'{'
string|"'forced_down'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
string|"'test2'"
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
