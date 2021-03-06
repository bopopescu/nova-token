begin_unit
comment|'#    Copyright 2013 Red Hat, Inc.'
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
name|'exception'
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
DECL|variable|OPTIONAL_ATTRS
name|'OPTIONAL_ATTRS'
op|'='
op|'['
string|"'parent_group'"
op|','
string|"'grantee_group'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|SecurityGroupRule
name|'class'
name|'SecurityGroupRule'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added create() and set id as read_only'
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
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'protocol'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'from_port'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'to_port'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'fields'
op|'.'
name|'IPNetworkField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'parent_group'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'SecurityGroup'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'grantee_group'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'SecurityGroup'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_subgroup
name|'def'
name|'_from_db_subgroup'
op|'('
name|'context'
op|','
name|'db_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'db_group'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'objects'
op|'.'
name|'SecurityGroup'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'objects'
op|'.'
name|'SecurityGroup'
op|'('
name|'context'
op|')'
op|','
name|'db_group'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'rule'
op|','
name|'db_rule'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'expected_attrs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'expected_attrs'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'for'
name|'field'
name|'in'
name|'rule'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'rule'
op|','
name|'field'
op|','
nl|'\n'
name|'rule'
op|'.'
name|'_from_db_subgroup'
op|'('
name|'context'
op|','
name|'db_rule'
op|'['
name|'field'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'field'
name|'not'
name|'in'
name|'OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'rule'
op|','
name|'field'
op|','
name|'db_rule'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'rule'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'rule'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'rule'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'parent_group'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'parent_group'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'parent_group'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'parent_group_id'"
op|']'
op|'='
name|'parent_group'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'grantee_group'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'grantee_group'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'grantee_group'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'group_id'"
op|']'
op|'='
name|'grantee_group'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'db_rule'
op|'='
name|'db'
op|'.'
name|'security_group_rule_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
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
name|'db_rule'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'rule_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_rule'
op|'='
name|'db'
op|'.'
name|'security_group_rule_get'
op|'('
name|'context'
op|','
name|'rule_id'
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
name|'db_rule'
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
DECL|class|SecurityGroupRuleList
name|'class'
name|'SecurityGroupRuleList'
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
DECL|variable|fields
indent|'    '
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
string|"'SecurityGroupRule'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|VERSION
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_security_group_id
name|'def'
name|'get_by_security_group_id'
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
name|'db_rules'
op|'='
name|'db'
op|'.'
name|'security_group_rule_get_by_security_group'
op|'('
nl|'\n'
name|'context'
op|','
name|'secgroup_id'
op|','
name|'columns_to_join'
op|'='
op|'['
string|"'grantee_group'"
op|']'
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
name|'SecurityGroupRule'
op|','
name|'db_rules'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'grantee_group'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_by_security_group
name|'def'
name|'get_by_security_group'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'get_by_security_group_id'
op|'('
name|'context'
op|','
name|'security_group'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid
name|'def'
name|'get_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_rules'
op|'='
name|'db'
op|'.'
name|'security_group_rule_get_by_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
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
name|'SecurityGroupRule'
op|','
name|'db_rules'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'grantee_group'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
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
name|'return'
name|'cls'
op|'.'
name|'get_by_instance_uuid'
op|'('
name|'context'
op|','
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
