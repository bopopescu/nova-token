begin_unit
comment|'#   Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'admin_actions'
newline|'\n'
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
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'rpcapi'
name|'as'
name|'scheduler_rpcapi'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|INSTANCE
name|'INSTANCE'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"fake"'
op|','
nl|'\n'
string|'"display_name"'
op|':'
string|'"test_server"'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"abcd"'
op|','
nl|'\n'
string|'"user_id"'
op|':'
string|"'fake_user_id'"
op|','
nl|'\n'
string|'"tenant_id"'
op|':'
string|"'fake_tenant_id'"
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"security_groups"'
op|':'
op|'['
op|'{'
string|'"id"'
op|':'
number|'1'
op|','
string|'"name"'
op|':'
string|'"test"'
op|'}'
op|']'
op|','
nl|'\n'
string|'"progress"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"image_ref"'
op|':'
string|"'http://foo.com/123'"
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"instance_type"'
op|':'
op|'{'
string|'"flavorid"'
op|':'
string|"'124'"
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api
name|'def'
name|'fake_compute_api'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api_raises_invalid_state
dedent|''
name|'def'
name|'fake_compute_api_raises_invalid_state'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
name|'attr'
op|'='
string|"'fake_attr'"
op|','
nl|'\n'
name|'state'
op|'='
string|"'fake_state'"
op|','
name|'method'
op|'='
string|"'fake_method'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api_get
dedent|''
name|'def'
name|'fake_compute_api_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'uuid'"
op|':'
name|'instance_id'
op|','
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_scheduler_api_live_migration
dedent|''
name|'def'
name|'fake_scheduler_api_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
name|'False'
op|','
name|'instance'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'None'
op|','
name|'topic'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminActionsTest
dedent|''
name|'class'
name|'AdminActionsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_actions
indent|'    '
name|'_actions'
op|'='
op|'('
string|"'pause'"
op|','
string|"'unpause'"
op|','
string|"'suspend'"
op|','
string|"'resume'"
op|','
string|"'migrate'"
op|','
nl|'\n'
string|"'resetNetwork'"
op|','
string|"'injectNetworkInfo'"
op|','
string|"'lock'"
op|','
string|"'unlock'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_methods
name|'_methods'
op|'='
op|'('
string|"'pause'"
op|','
string|"'unpause'"
op|','
string|"'suspend'"
op|','
string|"'resume'"
op|','
string|"'resize'"
op|','
nl|'\n'
string|"'reset_network'"
op|','
string|"'inject_network_info'"
op|','
string|"'lock'"
op|','
string|"'unlock'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_actions_that_check_state
name|'_actions_that_check_state'
op|'='
op|'('
nl|'\n'
comment|'# action, method'
nl|'\n'
op|'('
string|"'pause'"
op|','
string|"'pause'"
op|')'
op|','
nl|'\n'
op|'('
string|"'unpause'"
op|','
string|"'unpause'"
op|')'
op|','
nl|'\n'
op|'('
string|"'suspend'"
op|','
string|"'suspend'"
op|')'
op|','
nl|'\n'
op|'('
string|"'resume'"
op|','
string|"'resume'"
op|')'
op|','
nl|'\n'
op|'('
string|"'migrate'"
op|','
string|"'resize'"
op|')'
op|')'
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
name|'AdminActionsTest'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_api_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'UUID'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
name|'for'
name|'_method'
name|'in'
name|'self'
op|'.'
name|'_methods'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
name|'_method'
op|','
name|'fake_compute_api'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'scheduler_rpcapi'
op|'.'
name|'SchedulerAPI'
op|','
nl|'\n'
string|"'live_migration'"
op|','
nl|'\n'
name|'fake_scheduler_api_live_migration'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Admin_actions'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_admin_api_actions
dedent|''
name|'def'
name|'test_admin_api_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
name|'for'
name|'_action'
name|'in'
name|'self'
op|'.'
name|'_actions'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/%s/action'"
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
name|'_action'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_admin_api_actions_raise_conflict_on_invalid_state
dedent|''
dedent|''
name|'def'
name|'test_admin_api_actions_raise_conflict_on_invalid_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'_action'
op|','
name|'_method'
name|'in'
name|'self'
op|'.'
name|'_actions_that_check_state'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
name|'_method'
op|','
nl|'\n'
name|'fake_compute_api_raises_invalid_state'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/%s/action'"
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
name|'_action'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'409'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"Cannot \\\'%(_action)s\\\' while instance"'
op|'%'
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_live_enabled
dedent|''
dedent|''
name|'def'
name|'test_migrate_live_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'ctxt'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'ctxt'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'fake_auth_context'
op|'='
name|'ctxt'
op|','
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
nl|'\n'
string|"'os-migrateLive'"
op|':'
op|'{'
nl|'\n'
string|"'host'"
op|':'
string|"'hostname'"
op|','
nl|'\n'
string|"'block_migration'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'disk_over_commit'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
DECL|function|fake_update
name|'def'
name|'fake_update'
op|'('
name|'inst'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'task_state'
op|','
name|'expected_task_state'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
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
name|'API'
op|','
string|"'update'"
op|','
name|'fake_update'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_live_missing_dict_param
dedent|''
name|'def'
name|'test_migrate_live_missing_dict_param'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'ctxt'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'ctxt'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'fake_auth_context'
op|'='
name|'ctxt'
op|','
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
nl|'\n'
string|"'os-migrateLive'"
op|':'
op|'{'
nl|'\n'
string|"'dummy'"
op|':'
string|"'hostname'"
op|','
nl|'\n'
string|"'block_migration'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'disk_over_commit'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateBackupTests
dedent|''
dedent|''
name|'class'
name|'CreateBackupTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'CreateBackupTests'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_api_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'backup_stubs'
op|'='
name|'fakes'
op|'.'
name|'stub_out_compute_api_backup'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouter'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_request
dedent|''
name|'def'
name|'_get_request'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'/fake/servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_with_metadata
dedent|''
name|'def'
name|'test_create_backup_with_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'123'"
op|':'
string|"'asdf'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'response'
op|'.'
name|'headers'
op|'['
string|"'Location'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_with_too_much_metadata
dedent|''
name|'def'
name|'test_create_backup_with_too_much_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'123'"
op|':'
string|"'asdf'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'range'
op|'('
name|'CONF'
op|'.'
name|'quota_metadata_items'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'['
string|"'createBackup'"
op|']'
op|'['
string|"'metadata'"
op|']'
op|'['
string|"'foo%i'"
op|'%'
name|'num'
op|']'
op|'='
string|'"bar"'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'413'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_no_name
dedent|''
name|'def'
name|'test_create_backup_no_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Name is required for backups"""'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_no_rotation
dedent|''
name|'def'
name|'test_create_backup_no_rotation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rotation is required for backup requests"""'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_negative_rotation
dedent|''
name|'def'
name|'test_create_backup_negative_rotation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rotation must be greater than or equal to zero\n        for backup requests\n        """'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_no_backup_type
dedent|''
name|'def'
name|'test_create_backup_no_backup_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Backup Type (daily or weekly) is required for backup requests"""'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_bad_entity
dedent|''
name|'def'
name|'test_create_backup_bad_entity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'createBackup'"
op|':'
string|"'go'"
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_rotation_is_zero
dedent|''
name|'def'
name|'test_create_backup_rotation_is_zero'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The happy path for creating backups if rotation is zero"""'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'0'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'Location'"
name|'in'
name|'response'
op|'.'
name|'headers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_rotation_is_positive
dedent|''
name|'def'
name|'test_create_backup_rotation_is_positive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The happy path for creating backups if rotation is positive"""'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'response'
op|'.'
name|'headers'
op|'['
string|"'Location'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_raises_conflict_on_invalid_state
dedent|''
name|'def'
name|'test_create_backup_raises_conflict_on_invalid_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'backup'"
op|','
nl|'\n'
name|'fake_compute_api_raises_invalid_state'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'409'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResetStateTests
dedent|''
dedent|''
name|'class'
name|'ResetStateTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'ResetStateTests'
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
name|'exists'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get
name|'def'
name|'fake_get'
op|'('
name|'inst'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'exists'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'uuid'
op|'='
name|'instance_id'
op|','
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_update
dedent|''
name|'def'
name|'fake_update'
op|'('
name|'inst'
op|','
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'kwargs'
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
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'update'"
op|','
name|'fake_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'='
name|'admin_actions'
op|'.'
name|'AdminActionsController'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|"'/fake/servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_state
dedent|''
name|'def'
name|'test_no_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
string|"'inst_id'"
op|','
nl|'\n'
op|'{'
string|'"os-resetState"'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_state
dedent|''
name|'def'
name|'test_bad_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
string|"'inst_id'"
op|','
nl|'\n'
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"spam"'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_instance
dedent|''
name|'def'
name|'test_no_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'exists'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|','
string|"'inst_id'"
op|','
nl|'\n'
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"active"'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_active
dedent|''
name|'def'
name|'test_reset_active'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"active"'
op|'}'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|'('
name|'self'
op|'.'
name|'request'
op|','
string|"'inst_id'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'kwargs'
op|','
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_error
dedent|''
name|'def'
name|'test_reset_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"os-resetState"'
op|':'
op|'{'
string|'"state"'
op|':'
string|'"error"'
op|'}'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'admin_api'
op|'.'
name|'_reset_state'
op|'('
name|'self'
op|'.'
name|'request'
op|','
string|"'inst_id'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'kwargs'
op|','
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
