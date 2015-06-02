begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
name|'class'
name|'SecurityGroup'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|SecurityGroup
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: String attributes updated to support unicode'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'secgroup'
op|','
name|'db_secgroup'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): These are identical right now'
nl|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'secgroup'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'secgroup'
op|'['
name|'field'
op|']'
op|'='
name|'db_secgroup'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'secgroup'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'secgroup'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'secgroup'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'secgroup_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_secgroup'
op|'='
name|'db'
op|'.'
name|'security_group_get'
op|'('
name|'context'
op|','
name|'secgroup_id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_secgroup'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_name
name|'def'
name|'get_by_name'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_secgroup'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
name|'context'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'group_name'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_secgroup'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|in_use
name|'def'
name|'in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'security_group_in_use'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'db_secgroup'
op|'='
name|'db'
op|'.'
name|'security_group_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
nl|'\n'
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_secgroup'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|refresh
name|'def'
name|'refresh'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
nl|'\n'
name|'db'
op|'.'
name|'security_group_get'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|SecurityGroupList
name|'class'
name|'SecurityGroupList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'#              SecurityGroup <= version 1.1'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'SecurityGroup'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|child_versions
name|'child_versions'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
comment|'# NOTE(danms): SecurityGroup was at 1.1 before we added this'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'SecurityGroupList'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'groups'
op|'='
name|'db'
op|'.'
name|'security_group_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'SecurityGroup'
op|','
name|'groups'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_project
name|'def'
name|'get_by_project'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'groups'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'SecurityGroup'
op|','
name|'groups'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance
name|'def'
name|'get_by_instance'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'groups'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'context'
op|','
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'SecurityGroup'
op|','
name|'groups'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_secgroup_list
dedent|''
dedent|''
name|'def'
name|'make_secgroup_list'
op|'('
name|'security_groups'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A helper to make security group objects from a list of names.\n\n    Note that this does not make them save-able or have the rest of the\n    attributes they would normally have, but provides a quick way to fill,\n    for example, an instance object during create.\n    """'
newline|'\n'
name|'secgroups'
op|'='
name|'objects'
op|'.'
name|'SecurityGroupList'
op|'('
op|')'
newline|'\n'
name|'secgroups'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'security_groups'
op|':'
newline|'\n'
indent|'        '
name|'secgroup'
op|'='
name|'objects'
op|'.'
name|'SecurityGroup'
op|'('
op|')'
newline|'\n'
name|'secgroup'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'secgroups'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'secgroup'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'secgroups'
newline|'\n'
dedent|''
endmarker|''
end_unit
