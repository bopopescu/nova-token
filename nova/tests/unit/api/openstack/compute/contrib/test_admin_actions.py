begin_unit
comment|'#   Copyright 2011 OpenStack Foundation'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'admin_actions'
name|'as'
name|'admin_actions_v2'
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
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'admin_actions'
name|'as'
name|'admin_actions_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'admin_only_action_common'
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
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminActionsTestV21
name|'class'
name|'AdminActionsTestV21'
op|'('
name|'admin_only_action_common'
op|'.'
name|'CommonTests'
op|')'
op|':'
newline|'\n'
DECL|variable|admin_actions
indent|'    '
name|'admin_actions'
op|'='
name|'admin_actions_v21'
newline|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'2.1'"
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
name|'AdminActionsTestV21'
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
name|'controller'
op|'='
name|'self'
op|'.'
name|'admin_actions'
op|'.'
name|'AdminActionsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
newline|'\n'
nl|'\n'
DECL|function|_fake_controller
name|'def'
name|'_fake_controller'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'controller'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'admin_actions'
op|','
string|"'AdminActionsController'"
op|','
nl|'\n'
name|'_fake_controller'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'get'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_actions
dedent|''
name|'def'
name|'test_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'actions'
op|'='
op|'['
string|"'_reset_network'"
op|','
string|"'_inject_network_info'"
op|']'
newline|'\n'
name|'method_translations'
op|'='
op|'{'
string|"'_reset_network'"
op|':'
string|"'reset_network'"
op|','
nl|'\n'
string|"'_inject_network_info'"
op|':'
string|"'inject_network_info'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_test_actions'
op|'('
name|'actions'
op|','
name|'method_translations'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_actions_with_non_existed_instance
dedent|''
name|'def'
name|'test_actions_with_non_existed_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'actions'
op|'='
op|'['
string|"'_reset_network'"
op|','
string|"'_inject_network_info'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_test_actions_with_non_existed_instance'
op|'('
name|'actions'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_actions_with_locked_instance
dedent|''
name|'def'
name|'test_actions_with_locked_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'actions'
op|'='
op|'['
string|"'_reset_network'"
op|','
string|"'_inject_network_info'"
op|']'
newline|'\n'
name|'method_translations'
op|'='
op|'{'
string|"'_reset_network'"
op|':'
string|"'reset_network'"
op|','
nl|'\n'
string|"'_inject_network_info'"
op|':'
string|"'inject_network_info'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_test_actions_with_locked_instance'
op|'('
name|'actions'
op|','
nl|'\n'
name|'method_translations'
op|'='
name|'method_translations'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminActionsTestV2
dedent|''
dedent|''
name|'class'
name|'AdminActionsTestV2'
op|'('
name|'AdminActionsTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|admin_actions
indent|'    '
name|'admin_actions'
op|'='
name|'admin_actions_v2'
newline|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'2'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminActionsPolicyEnforcementV21
dedent|''
name|'class'
name|'AdminActionsPolicyEnforcementV21'
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
name|'AdminActionsPolicyEnforcementV21'
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
name|'controller'
op|'='
name|'admin_actions_v21'
op|'.'
name|'AdminActionsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_id'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
nl|'\n'
DECL|member|common_policy_check
dedent|''
name|'def'
name|'common_policy_check'
op|'('
name|'self'
op|','
name|'rule'
op|','
name|'fun_name'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwarg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rule'
op|')'
newline|'\n'
name|'func'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
name|'fun_name'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'func'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwarg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
nl|'\n'
name|'rule'
op|'.'
name|'popitem'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|','
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_network_policy_failed
dedent|''
name|'def'
name|'test_reset_network_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
op|'{'
string|'"os_compute_api:os-admin-actions:reset_network"'
op|':'
nl|'\n'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'common_policy_check'
op|'('
nl|'\n'
name|'rule'
op|','
string|'"_reset_network"'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'self'
op|'.'
name|'fake_id'
op|','
name|'body'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_network_info_policy_failed
dedent|''
name|'def'
name|'test_inject_network_info_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
op|'{'
string|'"os_compute_api:os-admin-actions:inject_network_info"'
op|':'
nl|'\n'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'common_policy_check'
op|'('
nl|'\n'
name|'rule'
op|','
string|'"_inject_network_info"'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'self'
op|'.'
name|'fake_id'
op|','
name|'body'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_state_policy_failed
dedent|''
name|'def'
name|'test_reset_state_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
op|'{'
string|'"os_compute_api:os-admin-actions:reset_state"'
op|':'
nl|'\n'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'common_policy_check'
op|'('
nl|'\n'
name|'rule'
op|','
string|'"_reset_state"'
op|','
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_id'
op|','
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
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
