begin_unit
comment|'# Copyright (c) 2014 Cisco Systems, Inc.'
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
name|'oslo_utils'
name|'import'
name|'uuidutils'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'import'
name|'uuidsentinel'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID1
name|'FAKE_UUID1'
op|'='
string|"'a47ae74e-ab08-447f-8eee-ffd43fc46c16'"
newline|'\n'
DECL|variable|FAKE_UUID2
name|'FAKE_UUID2'
op|'='
string|"'c6e6430a-6563-4efa-9542-5e93c9e97d18'"
newline|'\n'
DECL|variable|FAKE_UUID3
name|'FAKE_UUID3'
op|'='
string|"'b8713410-9ba3-e913-901b-13410ca90121'"
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
DECL|function|server_group_resp_template
dedent|''
name|'def'
name|'server_group_resp_template'
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
name|'sgroup'
op|'.'
name|'setdefault'
op|'('
string|"'policies'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'sgroup'
op|'.'
name|'setdefault'
op|'('
string|"'members'"
op|','
op|'['
op|']'
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
name|'fakes'
op|'.'
name|'FAKE_USER_ID'
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
name|'fakes'
op|'.'
name|'FAKE_PROJECT_ID'
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
DECL|class|ServerGroupTestV21
dedent|''
name|'class'
name|'ServerGroupTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|validation_error
indent|'    '
name|'validation_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'ServerGroupTestV21'
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
DECL|member|test_create_server_group_with_no_policies
dedent|''
name|'def'
name|'test_create_server_group_with_no_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
DECL|member|_create_server_group_normal
dedent|''
name|'def'
name|'_create_server_group_normal'
op|'('
name|'self'
op|','
name|'policies'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
op|')'
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
DECL|member|test_create_server_group
dedent|''
name|'def'
name|'test_create_server_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'policies'
op|'='
op|'['
string|"'affinity'"
op|','
string|"'anti-affinity'"
op|']'
newline|'\n'
name|'for'
name|'policy'
name|'in'
name|'policies'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_create_server_group_normal'
op|'('
op|'['
name|'policy'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'image_ref'
op|'='
name|'uuidsentinel'
op|'.'
name|'fake_image_ref'
op|','
nl|'\n'
name|'node'
op|'='
string|"'node1'"
op|','
name|'reservation_id'
op|'='
string|"'a'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host1'"
op|','
name|'project_id'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'vm_state'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'system_metadata'
op|'='
op|'{'
string|"'key'"
op|':'
string|"'value'"
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|_create_instance_group
dedent|''
name|'def'
name|'_create_instance_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'members'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ig'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'name'
op|'='
string|"'fake_name'"
op|','
nl|'\n'
name|'user_id'
op|'='
string|"'fake_user'"
op|','
name|'project_id'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|')'
newline|'\n'
name|'ig'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'ig'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|_create_groups_and_instances
dedent|''
name|'def'
name|'_create_groups_and_instances'
op|'('
name|'self'
op|','
name|'ctx'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
op|'['
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'ctx'
op|')'
op|','
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'ctx'
op|')'
op|']'
newline|'\n'
name|'members'
op|'='
op|'['
name|'instance'
op|'.'
name|'uuid'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|']'
newline|'\n'
name|'ig_uuid'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'ctx'
op|','
name|'members'
op|')'
newline|'\n'
name|'return'
op|'('
name|'ig_uuid'
op|','
name|'instances'
op|','
name|'members'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_group_get_all_by_project_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_group_get_all'"
op|')'
newline|'\n'
DECL|member|_test_list_server_group_all
name|'def'
name|'_test_list_server_group_all'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_get_all'
op|','
nl|'\n'
name|'mock_get_by_project'
op|','
nl|'\n'
name|'api_version'
op|'='
string|"'2.1'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'policies'
op|'='
op|'['
string|"'anti-affinity'"
op|']'
newline|'\n'
name|'members'
op|'='
op|'['
op|']'
newline|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
comment|'# always empty'
newline|'\n'
name|'names'
op|'='
op|'['
string|"'default-x'"
op|','
string|"'test'"
op|']'
newline|'\n'
name|'p_id'
op|'='
name|'fakes'
op|'.'
name|'FAKE_PROJECT_ID'
newline|'\n'
name|'u_id'
op|'='
name|'fakes'
op|'.'
name|'FAKE_USER_ID'
newline|'\n'
name|'if'
name|'api_version'
op|'>='
string|"'2.13'"
op|':'
newline|'\n'
indent|'            '
name|'sg1'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg1_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'p_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'u_id'
op|')'
newline|'\n'
name|'sg2'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg2_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'p_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'u_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'sg1'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg1_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
name|'sg2'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg2_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'tenant_groups'
op|'='
op|'['
name|'sg2'
op|']'
newline|'\n'
name|'all_groups'
op|'='
op|'['
name|'sg1'
op|','
name|'sg2'
op|']'
newline|'\n'
nl|'\n'
name|'all'
op|'='
op|'{'
string|"'server_groups'"
op|':'
name|'all_groups'
op|'}'
newline|'\n'
name|'tenant_specific'
op|'='
op|'{'
string|"'server_groups'"
op|':'
name|'tenant_groups'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|return_all_server_groups
name|'def'
name|'return_all_server_groups'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'server_group_db'
op|'('
name|'sg'
op|')'
name|'for'
name|'sg'
name|'in'
name|'all_groups'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_get_all'
op|'.'
name|'return_value'
op|'='
name|'return_all_server_groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|return_tenant_server_groups
name|'def'
name|'return_tenant_server_groups'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'server_group_db'
op|'('
name|'sg'
op|')'
name|'for'
name|'sg'
name|'in'
name|'tenant_groups'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_get_by_project'
op|'.'
name|'return_value'
op|'='
name|'return_tenant_server_groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'path'
op|'='
string|"'/os-server-groups?all_projects=True'"
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'path'
op|','
name|'use_admin_context'
op|'='
name|'True'
op|','
nl|'\n'
name|'version'
op|'='
name|'api_version'
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
name|'all'
op|','
name|'res_dict'
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
name|'path'
op|','
nl|'\n'
name|'version'
op|'='
name|'api_version'
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
name|'tenant_specific'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_group_get_all_by_project_id'"
op|')'
newline|'\n'
DECL|member|_test_list_server_group_by_tenant
name|'def'
name|'_test_list_server_group_by_tenant'
op|'('
name|'self'
op|','
name|'mock_get_by_project'
op|','
nl|'\n'
name|'api_version'
op|'='
string|"'2.1'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'policies'
op|'='
op|'['
string|"'anti-affinity'"
op|']'
newline|'\n'
name|'members'
op|'='
op|'['
op|']'
newline|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
comment|'# always empty'
newline|'\n'
name|'names'
op|'='
op|'['
string|"'default-x'"
op|','
string|"'test'"
op|']'
newline|'\n'
name|'p_id'
op|'='
name|'fakes'
op|'.'
name|'FAKE_PROJECT_ID'
newline|'\n'
name|'u_id'
op|'='
name|'fakes'
op|'.'
name|'FAKE_USER_ID'
newline|'\n'
name|'if'
name|'api_version'
op|'>='
string|"'2.13'"
op|':'
newline|'\n'
indent|'            '
name|'sg1'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg1_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'p_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'u_id'
op|')'
newline|'\n'
name|'sg2'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg2_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'p_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'u_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'sg1'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg1_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
name|'sg2'
op|'='
name|'server_group_resp_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg2_id'
op|','
nl|'\n'
name|'name'
op|'='
name|'names'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'groups'
op|'='
op|'['
name|'sg1'
op|','
name|'sg2'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'server_groups'"
op|':'
name|'groups'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|return_server_groups
name|'def'
name|'return_server_groups'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'server_group_db'
op|'('
name|'sg'
op|')'
name|'for'
name|'sg'
name|'in'
name|'groups'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return_get_by_project'
op|'='
name|'return_server_groups'
op|'('
op|')'
newline|'\n'
name|'mock_get_by_project'
op|'.'
name|'return_value'
op|'='
name|'return_get_by_project'
newline|'\n'
name|'path'
op|'='
string|"'/os-server-groups'"
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
name|'path'
op|','
nl|'\n'
name|'version'
op|'='
name|'api_version'
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
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_display_members
dedent|''
name|'def'
name|'test_display_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake'"
op|')'
newline|'\n'
op|'('
name|'ig_uuid'
op|','
name|'instances'
op|','
name|'members'
op|')'
op|'='
name|'self'
op|'.'
name|'_create_groups_and_instances'
op|'('
name|'ctx'
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
name|'self'
op|'.'
name|'req'
op|','
name|'ig_uuid'
op|')'
newline|'\n'
name|'result_members'
op|'='
name|'res_dict'
op|'['
string|"'server_group'"
op|']'
op|'['
string|"'members'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'result_members'
op|')'
op|')'
newline|'\n'
name|'for'
name|'member'
name|'in'
name|'members'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'member'
op|','
name|'result_members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_display_members_with_nonexistent_group
dedent|''
dedent|''
name|'def'
name|'test_display_members_with_nonexistent_group'
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
name|'HTTPNotFound'
op|','
nl|'\n'
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
name|'uuidsentinel'
op|'.'
name|'group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_display_active_members_only
dedent|''
name|'def'
name|'test_display_active_members_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake'"
op|')'
newline|'\n'
op|'('
name|'ig_uuid'
op|','
name|'instances'
op|','
name|'members'
op|')'
op|'='
name|'self'
op|'.'
name|'_create_groups_and_instances'
op|'('
name|'ctx'
op|')'
newline|'\n'
nl|'\n'
comment|'# delete an instance'
nl|'\n'
name|'instances'
op|'['
number|'1'
op|']'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
comment|'# check that the instance does not exist'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|','
nl|'\n'
name|'ctx'
op|','
name|'instances'
op|'['
number|'1'
op|']'
op|'.'
name|'uuid'
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
name|'self'
op|'.'
name|'req'
op|','
name|'ig_uuid'
op|')'
newline|'\n'
name|'result_members'
op|'='
name|'res_dict'
op|'['
string|"'server_group'"
op|']'
op|'['
string|"'members'"
op|']'
newline|'\n'
comment|'# check that only the active instance is displayed'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'result_members'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'uuid'
op|','
name|'result_members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_group_with_non_alphanumeric_in_name
dedent|''
name|'def'
name|'test_create_server_group_with_non_alphanumeric_in_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# The fix for bug #1434335 expanded the allowable character set'
nl|'\n'
comment|'# for server group names to include non-alphanumeric characters'
nl|'\n'
comment|'# if they are printable.'
nl|'\n'
nl|'\n'
indent|'        '
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'good* $%name'"
op|','
nl|'\n'
name|'policies'
op|'='
op|'['
string|"'affinity'"
op|']'
op|')'
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
string|"'good* $%name'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_group_with_illegal_name
dedent|''
name|'def'
name|'test_create_server_group_with_illegal_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# blank name'
nl|'\n'
indent|'        '
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"''"
op|','
name|'policies'
op|'='
op|'['
string|"'test_policy'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# name with length 256'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'1234567890'"
op|'*'
number|'26'
op|','
nl|'\n'
name|'policies'
op|'='
op|'['
string|"'test_policy'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# non-string name'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
number|'12'
op|','
name|'policies'
op|'='
op|'['
string|"'test_policy'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# name with leading spaces'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'  leading spaces'"
op|','
nl|'\n'
name|'policies'
op|'='
op|'['
string|"'test_policy'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# name with trailing spaces'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'trailing space '"
op|','
nl|'\n'
name|'policies'
op|'='
op|'['
string|"'test_policy'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# name with all spaces'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'    '"
op|','
nl|'\n'
name|'policies'
op|'='
op|'['
string|"'test_policy'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# name with unprintable character'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'bad\\x00name'"
op|','
nl|'\n'
name|'policies'
op|'='
op|'['
string|"'test_policy'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# name with out of range char U0001F4A9'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|'u"\\U0001F4A9"'
op|','
nl|'\n'
name|'policies'
op|'='
op|'['
string|"'affinity'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
DECL|member|test_create_server_group_with_illegal_policies
dedent|''
name|'def'
name|'test_create_server_group_with_illegal_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# blank policy'
nl|'\n'
indent|'        '
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'fake-name'"
op|','
name|'policies'
op|'='
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# policy as integer'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'fake-name'"
op|','
name|'policies'
op|'='
number|'7'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# policy as string'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'fake-name'"
op|','
name|'policies'
op|'='
string|"'invalid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
comment|'# policy as None'
nl|'\n'
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
name|'name'
op|'='
string|"'fake-name'"
op|','
name|'policies'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
DECL|member|test_create_server_group_conflicting_policies
dedent|''
name|'def'
name|'test_create_server_group_conflicting_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|','
string|"'affinity'"
op|']'
newline|'\n'
name|'sgroup'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
DECL|member|test_create_server_group_with_duplicate_policies
dedent|''
name|'def'
name|'test_create_server_group_with_duplicate_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'affinity'"
op|','
string|"'affinity'"
op|']'
newline|'\n'
name|'sgroup'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
DECL|member|test_create_server_group_not_supported
dedent|''
name|'def'
name|'test_create_server_group_not_supported'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgroup'
op|'='
name|'server_group_template'
op|'('
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'storage-affinity'"
op|','
string|"'anti-affinity'"
op|','
string|"'rack-affinity'"
op|']'
newline|'\n'
name|'sgroup'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
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
DECL|member|test_create_server_group_with_no_body
dedent|''
name|'def'
name|'test_create_server_group_with_no_body'
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
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_group_with_no_server_group
dedent|''
name|'def'
name|'test_create_server_group_with_no_server_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'no-instanceGroup'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_server_group_by_tenant
dedent|''
name|'def'
name|'test_list_server_group_by_tenant'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_server_group_by_tenant'
op|'('
name|'api_version'
op|'='
string|"'2.1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_server_group_all
dedent|''
name|'def'
name|'test_list_server_group_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_server_group_all'
op|'('
name|'api_version'
op|'='
string|"'2.1'"
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
name|'sg'
op|'='
name|'server_group_template'
op|'('
name|'id'
op|'='
name|'uuidsentinel'
op|'.'
name|'sg1_id'
op|')'
newline|'\n'
nl|'\n'
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
name|'stub_out'
op|'('
string|"'nova.db.instance_group_delete'"
op|','
nl|'\n'
name|'server_group_delete'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_group_get'"
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
name|'uuidsentinel'
op|'.'
name|'sg1_id'
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
DECL|member|test_delete_non_existing_server_group
dedent|''
name|'def'
name|'test_delete_non_existing_server_group'
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
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'invalid'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupTestV2
dedent|''
dedent|''
name|'class'
name|'ServerGroupTestV2'
op|'('
name|'ServerGroupTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|validation_error
indent|'    '
name|'validation_error'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
nl|'\n'
DECL|member|_setup_controller
name|'def'
name|'_setup_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_mgr'
op|'='
name|'extensions'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'server_groups'
op|'.'
name|'ServerGroupController'
op|'('
name|'ext_mgr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupTestV213
dedent|''
dedent|''
name|'class'
name|'ServerGroupTestV213'
op|'('
name|'ServerGroupTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|wsgi_api_version
indent|'    '
name|'wsgi_api_version'
op|'='
string|"'2.13'"
newline|'\n'
nl|'\n'
DECL|member|_setup_controller
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
DECL|member|test_list_server_group_all
dedent|''
name|'def'
name|'test_list_server_group_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_server_group_all'
op|'('
name|'api_version'
op|'='
string|"'2.13'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_server_group_by_tenant
dedent|''
name|'def'
name|'test_list_server_group_by_tenant'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_server_group_by_tenant'
op|'('
name|'api_version'
op|'='
string|"'2.13'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
