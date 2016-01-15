begin_unit
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
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
name|'mock'
newline|'\n'
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
name|'import'
name|'fping'
name|'as'
name|'fping_v21'
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
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'fping'
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
name|'import'
name|'fakes'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
name|'def'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'""'
op|'.'
name|'join'
op|'('
op|'['
string|'"%s is alive"'
op|'%'
name|'ip'
name|'for'
name|'ip'
name|'in'
name|'cmd'
op|'['
number|'1'
op|':'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FpingTestV21
dedent|''
name|'class'
name|'FpingTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|controller_cls
indent|'    '
name|'controller_cls'
op|'='
name|'fping_v21'
op|'.'
name|'FpingController'
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
name|'FpingTestV21'
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
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|','
name|'use_ipv6'
op|'='
name|'False'
op|')'
newline|'\n'
name|'return_server'
op|'='
name|'fakes'
op|'.'
name|'fake_instance_get'
op|'('
op|')'
newline|'\n'
name|'return_servers'
op|'='
name|'fakes'
op|'.'
name|'fake_instance_get_all_by_filters'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.db.instance_get_all_by_filters"'
op|','
nl|'\n'
name|'return_servers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.db.instance_get_by_uuid"'
op|','
nl|'\n'
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'utils'
op|','
string|'"execute"'
op|','
nl|'\n'
name|'execute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller_cls'
op|','
string|'"check_fping"'
op|','
nl|'\n'
name|'lambda'
name|'self'
op|':'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'controller_cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_url
dedent|''
name|'def'
name|'_get_url'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"/v2/1234"'
newline|'\n'
nl|'\n'
DECL|member|test_fping_index
dedent|''
name|'def'
name|'test_fping_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|'"/os-fping"'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"servers"'
op|','
name|'res_dict'
op|')'
newline|'\n'
name|'for'
name|'srv'
name|'in'
name|'res_dict'
op|'['
string|'"servers"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
string|'"project_id"'
op|','
string|'"id"'
op|','
string|'"alive"'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'key'
op|','
name|'srv'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fping_index_policy
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_fping_index_policy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
nl|'\n'
string|'"os-fping?all_tenants=1"'
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
name|'index'
op|','
name|'req'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
nl|'\n'
string|'"/os-fping?all_tenants=1"'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"servers"'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fping_index_include
dedent|''
name|'def'
name|'test_fping_index_include'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|'"/os-fping"'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'ids'
op|'='
op|'['
name|'srv'
op|'['
string|'"id"'
op|']'
name|'for'
name|'srv'
name|'in'
name|'res_dict'
op|'['
string|'"servers"'
op|']'
op|']'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
nl|'\n'
string|'"/os-fping?include=%s"'
op|'%'
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|'"servers"'
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|'"servers"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"id"'
op|']'
op|','
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fping_index_exclude
dedent|''
name|'def'
name|'test_fping_index_exclude'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|'"/os-fping"'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'ids'
op|'='
op|'['
name|'srv'
op|'['
string|'"id"'
op|']'
name|'for'
name|'srv'
name|'in'
name|'res_dict'
op|'['
string|'"servers"'
op|']'
op|']'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
nl|'\n'
string|'"/os-fping?exclude=%s"'
op|'%'
nl|'\n'
string|'","'
op|'.'
name|'join'
op|'('
name|'ids'
op|'['
number|'1'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|'"servers"'
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|'"servers"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"id"'
op|']'
op|','
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fping_show
dedent|''
name|'def'
name|'test_fping_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
nl|'\n'
string|'"os-fping/%s"'
op|'%'
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"server"'
op|','
name|'res_dict'
op|')'
newline|'\n'
name|'srv'
op|'='
name|'res_dict'
op|'['
string|'"server"'
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
string|'"project_id"'
op|','
string|'"id"'
op|','
string|'"alive"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'key'
op|','
name|'srv'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_get_by_uuid'"
op|')'
newline|'\n'
DECL|member|test_fping_show_with_not_found
name|'def'
name|'test_fping_show_with_not_found'
op|'('
name|'self'
op|','
name|'mock_get_instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_instance'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
nl|'\n'
name|'instance_id'
op|'='
string|"''"
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
nl|'\n'
string|'"os-fping/%s"'
op|'%'
name|'FAKE_UUID'
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
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
name|'FAKE_UUID'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FpingTestV2
dedent|''
dedent|''
name|'class'
name|'FpingTestV2'
op|'('
name|'FpingTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|controller_cls
indent|'    '
name|'controller_cls'
op|'='
name|'fping'
op|'.'
name|'FpingController'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FpingPolicyEnforcementV21
dedent|''
name|'class'
name|'FpingPolicyEnforcementV21'
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
name|'FpingPolicyEnforcementV21'
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
name|'fping_v21'
op|'.'
name|'FpingController'
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
DECL|member|common_policy_check
dedent|''
name|'def'
name|'common_policy_check'
op|'('
name|'self'
op|','
name|'rule'
op|','
name|'func'
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
DECL|member|test_list_policy_failed
dedent|''
name|'def'
name|'test_list_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
op|'{'
string|'"os_compute_api:os-fping"'
op|':'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'common_policy_check'
op|'('
name|'rule'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'req'
op|'.'
name|'GET'
op|'.'
name|'update'
op|'('
op|'{'
string|'"all_tenants"'
op|':'
string|'"True"'
op|'}'
op|')'
newline|'\n'
name|'rule'
op|'='
op|'{'
string|'"os_compute_api:os-fping:all_tenants"'
op|':'
nl|'\n'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'common_policy_check'
op|'('
name|'rule'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_policy_failed
dedent|''
name|'def'
name|'test_show_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
op|'{'
string|'"os_compute_api:os-fping"'
op|':'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'FAKE_UUID'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
