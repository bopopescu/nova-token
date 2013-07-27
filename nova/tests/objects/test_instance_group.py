begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 OpenStack Foundation'
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
name|'context'
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
name|'objects'
name|'import'
name|'instance_group'
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
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceGroupObjects
name|'class'
name|'_TestInstanceGroupObjects'
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
name|'_TestInstanceGroupObjects'
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
name|'user_id'
op|'='
string|"'fake_user'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake_project'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_default_values
dedent|''
name|'def'
name|'_get_default_values'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'name'"
op|':'
string|"'fake_name'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project_id'
op|'}'
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
name|'values'
op|','
name|'policies'
op|'='
name|'None'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'None'
op|','
name|'members'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'instance_group_create'
op|'('
name|'context'
op|','
name|'values'
op|','
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|','
name|'members'
op|'='
name|'members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_uuid
dedent|''
name|'def'
name|'test_get_by_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'metadata'
op|'='
op|'{'
string|"'key11'"
op|':'
string|"'value1'"
op|','
nl|'\n'
string|"'key12'"
op|':'
string|"'value2'"
op|'}'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'policy1'"
op|','
string|"'policy2'"
op|']'
newline|'\n'
name|'members'
op|'='
op|'['
string|"'instance_id1'"
op|','
string|"'instance_id2'"
op|']'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
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
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'metadetails'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'members'
op|','
name|'members'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'policies'
op|','
name|'policies'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh
dedent|''
name|'def'
name|'test_refresh'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'name'
op|','
string|"'fake_name'"
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'new_name'"
op|','
string|"'user_id'"
op|':'
string|"'new_user'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'new_project'"
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_group_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'name'
op|','
string|"'new_name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
name|'obj_result'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_simple
dedent|''
name|'def'
name|'test_save_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'name'
op|','
string|"'fake_name'"
op|')'
newline|'\n'
name|'obj_result'
op|'.'
name|'name'
op|'='
string|"'new_name'"
newline|'\n'
name|'obj_result'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'name'"
op|']'
op|','
string|"'new_name'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_policies
dedent|''
name|'def'
name|'test_save_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'policy1'"
op|','
string|"'policy2'"
op|']'
newline|'\n'
name|'obj_result'
op|'.'
name|'policies'
op|'='
name|'policies'
newline|'\n'
name|'obj_result'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'policies'"
op|']'
op|','
name|'policies'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_members
dedent|''
name|'def'
name|'test_save_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'members'
op|'='
op|'['
string|"'instance1'"
op|','
string|"'instance2'"
op|']'
newline|'\n'
name|'obj_result'
op|'.'
name|'members'
op|'='
name|'members'
newline|'\n'
name|'obj_result'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'members'"
op|']'
op|','
name|'members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_metadata
dedent|''
name|'def'
name|'test_save_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'metadata'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
name|'obj_result'
op|'.'
name|'metadetails'
op|'='
name|'metadata'
newline|'\n'
name|'obj_result'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'metadata1'
op|'='
name|'db'
op|'.'
name|'instance_group_metadata_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'metadata'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'metadata'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group1'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group1'
op|'.'
name|'uuid'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'group1'
op|'.'
name|'name'
op|'='
string|"'fake-name'"
newline|'\n'
name|'group1'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group2'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'group2'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'uuid'
op|','
name|'group2'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'name'
op|','
name|'group2'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'result'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'uuid'
op|','
name|'result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'name'
op|','
name|'result'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_policies
dedent|''
name|'def'
name|'test_create_with_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group1'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group1'
op|'.'
name|'policies'
op|'='
op|'['
string|"'policy1'"
op|','
string|"'policy2'"
op|']'
newline|'\n'
name|'group1'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group2'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'group2'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'policies'
op|','
name|'group2'
op|'.'
name|'policies'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_members
dedent|''
name|'def'
name|'test_create_with_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group1'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group1'
op|'.'
name|'members'
op|'='
op|'['
string|"'instance1'"
op|','
string|"'instance2'"
op|']'
newline|'\n'
name|'group1'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group2'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'group2'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'members'
op|','
name|'group2'
op|'.'
name|'members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_metadata
dedent|''
name|'def'
name|'test_create_with_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group1'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'metadata'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
name|'group1'
op|'.'
name|'metadetails'
op|'='
name|'metadata'
newline|'\n'
name|'group1'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group2'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'group2'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'metadata'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'group2'
op|'.'
name|'metadetails'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_recreate_fails
dedent|''
dedent|''
name|'def'
name|'test_recreate_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'group'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy
dedent|''
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'id'
op|'='
name|'result'
op|'.'
name|'id'
newline|'\n'
name|'group'
op|'.'
name|'uuid'
op|'='
name|'result'
op|'.'
name|'uuid'
newline|'\n'
name|'group'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceGroupNotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'instance_group_get'
op|','
name|'self'
op|'.'
name|'context'
op|','
name|'result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_populate_instances
dedent|''
name|'def'
name|'_populate_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
op|'['
op|'('
string|"'f1'"
op|','
string|"'p1'"
op|')'
op|','
op|'('
string|"'f2'"
op|','
string|"'p1'"
op|')'
op|','
nl|'\n'
op|'('
string|"'f3'"
op|','
string|"'p2'"
op|')'
op|','
op|'('
string|"'f4'"
op|','
string|"'p2'"
op|')'
op|']'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'values'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'instance'
op|'['
number|'0'
op|']'
newline|'\n'
name|'values'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'instance'
op|'['
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_all
dedent|''
dedent|''
name|'def'
name|'test_list_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_populate_instances'
op|'('
op|')'
newline|'\n'
name|'inst_list'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'groups'
op|'='
name|'db'
op|'.'
name|'instance_group_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
name|'len'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
number|'4'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'groups'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'groups'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_by_project_id
dedent|''
dedent|''
name|'def'
name|'test_list_by_project_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_populate_instances'
op|'('
op|')'
newline|'\n'
name|'project_ids'
op|'='
op|'['
string|"'p1'"
op|','
string|"'p2'"
op|']'
newline|'\n'
name|'for'
name|'id'
name|'in'
name|'project_ids'
op|':'
newline|'\n'
indent|'            '
name|'il'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_by_project_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'groups'
op|'='
name|'db'
op|'.'
name|'instance_group_get_all_by_project_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
name|'len'
op|'('
name|'il'
op|'.'
name|'objects'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'groups'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'il'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'il'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'groups'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'il'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'project_id'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestInstanceGroupObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceGroupObject
name|'_TestInstanceGroupObjects'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteInstanceGroupObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceGroupObject
name|'_TestInstanceGroupObjects'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
