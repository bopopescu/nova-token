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
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'shelve'
name|'as'
name|'shelve_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'shelve'
name|'as'
name|'shelve_v21'
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
name|'import'
name|'db'
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
name|'policy'
name|'as'
name|'common_policy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'policy'
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
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get_by_uuid
name|'def'
name|'fake_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'None'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
nl|'\n'
op|'**'
op|'{'
string|"'name'"
op|':'
string|"'fake'"
op|','
string|"'project_id'"
op|':'
string|"'%s_unequal'"
op|'%'
name|'context'
op|'.'
name|'project_id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShelvePolicyTestV21
dedent|''
name|'class'
name|'ShelvePolicyTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|plugin
indent|'    '
name|'plugin'
op|'='
name|'shelve_v21'
newline|'\n'
DECL|variable|prefix
name|'prefix'
op|'='
string|"'os_compute_api:os-shelve'"
newline|'\n'
DECL|variable|offload
name|'offload'
op|'='
string|"'shelve_offload'"
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
name|'ShelvePolicyTestV21'
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
name|'plugin'
op|'.'
name|'ShelveController'
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
nl|'\n'
DECL|member|test_shelve_restricted_by_role
dedent|''
name|'def'
name|'test_shelve_restricted_by_role'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
string|"'compute_extension:%sshelve'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"'role:admin'"
op|')'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_locked_server
dedent|''
name|'def'
name|'test_shelve_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
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
string|"'shelve'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_actions_to_locked_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve_restricted_by_role
dedent|''
name|'def'
name|'test_unshelve_restricted_by_role'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
string|"'compute_extension:%sunshelve'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"'role:admin'"
op|')'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unshelve'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve_locked_server
dedent|''
name|'def'
name|'test_unshelve_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
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
string|"'unshelve'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_actions_to_locked_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unshelve'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_offload_restricted_by_role
dedent|''
name|'def'
name|'test_shelve_offload_restricted_by_role'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
string|"'compute_extension:%s%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'prefix'
op|','
name|'self'
op|'.'
name|'offload'
op|')'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"'role:admin'"
op|')'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve_offload'
op|','
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_offload_locked_server
dedent|''
name|'def'
name|'test_shelve_offload_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
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
string|"'shelve_offload'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_actions_to_locked_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve_offload'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShelvePolicyTestV2
dedent|''
dedent|''
name|'class'
name|'ShelvePolicyTestV2'
op|'('
name|'ShelvePolicyTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|plugin
indent|'    '
name|'plugin'
op|'='
name|'shelve_v2'
newline|'\n'
DECL|variable|prefix
name|'prefix'
op|'='
string|"''"
newline|'\n'
DECL|variable|offload
name|'offload'
op|'='
string|"'shelveOffload'"
newline|'\n'
nl|'\n'
comment|'# These 3 cases are covered in ShelvePolicyEnforcementV21'
nl|'\n'
DECL|member|test_shelve_allowed
name|'def'
name|'test_shelve_allowed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
string|"'compute:get'"
op|':'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|','
nl|'\n'
string|"'compute_extension:%sshelve'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
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
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve_allowed
dedent|''
name|'def'
name|'test_unshelve_allowed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
string|"'compute:get'"
op|':'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|','
nl|'\n'
string|"'compute_extension:%sunshelve'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unshelve'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_offload_allowed
dedent|''
name|'def'
name|'test_shelve_offload_allowed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
string|"'compute:get'"
op|':'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|','
nl|'\n'
string|"'compute_extension:%s%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'prefix'
op|','
name|'self'
op|'.'
name|'offload'
op|')'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve_offload'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShelvePolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'ShelvePolicyEnforcementV21'
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
name|'ShelvePolicyEnforcementV21'
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
name|'shelve_v21'
op|'.'
name|'ShelveController'
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
nl|'\n'
DECL|member|test_shelve_policy_failed
dedent|''
name|'def'
name|'test_shelve_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-shelve:shelve"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
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
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'shelve'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_offload_policy_failed
dedent|''
name|'def'
name|'test_shelve_offload_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-shelve:shelve_offload"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
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
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_shelve_offload'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'shelve_offload'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve_policy_failed
dedent|''
name|'def'
name|'test_unshelve_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-shelve:unshelve"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
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
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unshelve'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'unshelve'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
