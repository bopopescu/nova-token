begin_unit
comment|'# Copyright 2014 Hewlett-Packard Development Company, L.P'
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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
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
op|'.'
name|'contrib'
name|'import'
name|'server_groups'
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
name|'server_groups'
name|'as'
name|'sg_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'uuidutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
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
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AttrDict
name|'class'
name|'AttrDict'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
DECL|member|__getattr__
indent|'    '
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'k'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'['
name|'k'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|server_group_template
dedent|''
dedent|''
name|'def'
name|'server_group_template'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'sgroup'
op|'='
name|'kwargs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'sgroup'
op|'.'
name|'setdefault'
op|'('
string|"'name'"
op|','
string|"'test'"
op|')'
newline|'\n'
name|'return'
name|'sgroup'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|server_group_db
dedent|''
name|'def'
name|'server_group_db'
op|'('
name|'sg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'attrs'
op|'='
name|'sg'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'if'
string|"'id'"
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'attrs'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'policies'"
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'        '
name|'policies'
op|'='
name|'attrs'
op|'.'
name|'pop'
op|'('
string|"'policies'"
op|')'
newline|'\n'
name|'attrs'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'policies'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'members'"
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'        '
name|'members'
op|'='
name|'attrs'
op|'.'
name|'pop'
op|'('
string|"'members'"
op|')'
newline|'\n'
name|'attrs'
op|'['
string|"'members'"
op|']'
op|'='
name|'members'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'members'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'metadata'"
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'metadetails'"
op|']'
op|'='
name|'attrs'
op|'.'
name|'pop'
op|'('
string|"'metadata'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'metadetails'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'attrs'
op|'['
string|"'deleted'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'attrs'
op|'['
string|"'deleted_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'attrs'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'attrs'
op|'['
string|"'updated_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'if'
string|"'user_id'"
name|'not'
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'user_id'"
newline|'\n'
dedent|''
name|'if'
string|"'project_id'"
name|'not'
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'project_id'"
newline|'\n'
dedent|''
name|'attrs'
op|'['
string|"'id'"
op|']'
op|'='
number|'7'
newline|'\n'
nl|'\n'
name|'return'
name|'AttrDict'
op|'('
name|'attrs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupQuotasTestV21
dedent|''
name|'class'
name|'ServerGroupQuotasTestV21'
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
name|'ServerGroupQuotasTestV21'
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
name|'_setup_controller'
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
DECL|member|_setup_controller
dedent|''
name|'def'
name|'_setup_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'sg_v21'
op|'.'
name|'ServerGroupController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_quotas
dedent|''
name|'def'
name|'_setup_quotas'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_assert_server_groups_in_use
dedent|''
name|'def'
name|'_assert_server_groups_in_use'
op|'('
name|'self'
op|','
name|'project_id'
op|','
name|'user_id'
op|','
name|'in_use'
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
name|'result'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
op|'.'
name|'get_user_quotas'
op|'('
name|'ctxt'
op|','
name|'project_id'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'server_groups'"
op|']'
op|'['
string|"'in_use'"
op|']'
op|','
name|'in_use'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_group_normal
dedent|''
name|'def'
name|'test_create_server_group_normal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_setup_quotas'
op|'('
op|')'
newline|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'anti-affinity'"
op|']'
newline|'\n'
name|'sgroup'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'server_group'"
op|':'
name|'sgroup'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'server_group'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'res_dict'
op|'['
string|"'server_group'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'server_group'"
op|']'
op|'['
string|"'policies'"
op|']'
op|','
name|'policies'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_group_quota_limit
dedent|''
name|'def'
name|'test_create_server_group_quota_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_setup_quotas'
op|'('
op|')'
newline|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'anti-affinity'"
op|']'
newline|'\n'
name|'sgroup'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
newline|'\n'
comment|"# Start by creating as many server groups as we're allowed to."
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'CONF'
op|'.'
name|'quota_server_groups'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
op|'{'
string|"'server_group'"
op|':'
name|'sgroup'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Then, creating a server group should fail.'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
op|'{'
string|"'server_group'"
op|':'
name|'sgroup'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_server_group_by_admin
dedent|''
name|'def'
name|'test_delete_server_group_by_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_setup_quotas'
op|'('
op|')'
newline|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'anti-affinity'"
op|']'
newline|'\n'
name|'sgroup'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
op|'{'
string|"'server_group'"
op|':'
name|'sgroup'
op|'}'
op|')'
newline|'\n'
name|'sg_id'
op|'='
name|'res'
op|'['
string|"'server_group'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_assert_server_groups_in_use'
op|'('
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'context'
op|'.'
name|'user_id'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|"# Delete the server group we've just created."
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
name|'sg_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure the quota in use has been released.'
nl|'\n'
name|'self'
op|'.'
name|'_assert_server_groups_in_use'
op|'('
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'context'
op|'.'
name|'user_id'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_server_group_by_id
dedent|''
name|'def'
name|'test_delete_server_group_by_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_setup_quotas'
op|'('
op|')'
newline|'\n'
name|'sg'
op|'='
name|'server_group_template'
op|'('
name|'id'
op|'='
string|"'123'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|server_group_delete
name|'def'
name|'server_group_delete'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|function|return_server_group
dedent|''
name|'def'
name|'return_server_group'
op|'('
name|'context'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sg'
op|'['
string|"'id'"
op|']'
op|','
name|'group_id'
op|')'
newline|'\n'
name|'return'
name|'server_group_db'
op|'('
name|'sg'
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
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_group_delete'"
op|','
nl|'\n'
name|'server_group_delete'
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
name|'db'
op|','
string|"'instance_group_get'"
op|','
nl|'\n'
name|'return_server_group'
op|')'
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|"'123'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE: on v2.1, http status code is set as wsgi_code of API'
nl|'\n'
comment|'# method instead of status_int in a response object.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
name|'sg_v21'
op|'.'
name|'ServerGroupController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'.'
name|'wsgi_code'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'resp'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'204'
op|','
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupQuotasTestV2
dedent|''
dedent|''
name|'class'
name|'ServerGroupQuotasTestV2'
op|'('
name|'ServerGroupQuotasTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_setup_controller
indent|'    '
name|'def'
name|'_setup_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'extensions'
op|'.'
name|'ExtensionManager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'server_groups'
op|'.'
name|'ServerGroupController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_quotas
dedent|''
name|'def'
name|'_setup_quotas'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-server-group-quotas'"
op|')'
op|'.'
name|'MultipleTimes'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
