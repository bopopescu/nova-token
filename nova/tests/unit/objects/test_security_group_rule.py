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
name|'import'
name|'mock'
newline|'\n'
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
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_security_group'
newline|'\n'
nl|'\n'
DECL|variable|fake_rule
name|'fake_rule'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'protocol'"
op|':'
string|"'tcp'"
op|','
nl|'\n'
string|"'from_port'"
op|':'
number|'22'
op|','
nl|'\n'
string|"'to_port'"
op|':'
number|'22'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'0.0.0.0/0'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestSecurityGroupRuleObject
name|'class'
name|'_TestSecurityGroupRuleObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_by_id
indent|'    '
name|'def'
name|'test_get_by_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'security_group_rule_get'"
op|')'
name|'as'
name|'sgrg'
op|':'
newline|'\n'
indent|'            '
name|'sgrg'
op|'.'
name|'return_value'
op|'='
name|'fake_rule'
newline|'\n'
name|'rule'
op|'='
name|'objects'
op|'.'
name|'SecurityGroupRule'
op|'.'
name|'get_by_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'fake_rule'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'field'
op|'=='
string|"'cidr'"
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_rule'
op|'['
name|'field'
op|']'
op|','
name|'str'
op|'('
name|'rule'
op|'['
name|'field'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_rule'
op|'['
name|'field'
op|']'
op|','
name|'rule'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'sgrg'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_security_group
dedent|''
dedent|''
name|'def'
name|'test_get_by_security_group'
op|'('
name|'self'
op|')'
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
name|'id'
op|'='
number|'123'
newline|'\n'
name|'rule'
op|'='
name|'dict'
op|'('
name|'fake_rule'
op|')'
newline|'\n'
name|'rule'
op|'['
string|"'grantee_group'"
op|']'
op|'='
name|'dict'
op|'('
name|'test_security_group'
op|'.'
name|'fake_secgroup'
op|','
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'stupid_method'
op|'='
string|"'security_group_rule_get_by_security_group'"
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
name|'stupid_method'
op|')'
name|'as'
name|'sgrgbsg'
op|':'
newline|'\n'
indent|'            '
name|'sgrgbsg'
op|'.'
name|'return_value'
op|'='
op|'['
name|'rule'
op|']'
newline|'\n'
name|'rules'
op|'='
op|'('
name|'objects'
op|'.'
name|'SecurityGroupRuleList'
op|'.'
nl|'\n'
name|'get_by_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'secgroup'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'rules'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'123'
op|','
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'grantee_group'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'security_group_rule_create'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fake_rule'
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'db_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
name|'objects'
op|'.'
name|'SecurityGroupRule'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'rule'
op|'.'
name|'protocol'
op|'='
string|"'tcp'"
newline|'\n'
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
name|'id'
op|'='
number|'123'
newline|'\n'
name|'parentgroup'
op|'='
name|'objects'
op|'.'
name|'SecurityGroup'
op|'('
op|')'
newline|'\n'
name|'parentgroup'
op|'.'
name|'id'
op|'='
number|'223'
newline|'\n'
name|'rule'
op|'.'
name|'grantee_group'
op|'='
name|'secgroup'
newline|'\n'
name|'rule'
op|'.'
name|'parent_group'
op|'='
name|'parentgroup'
newline|'\n'
name|'rule'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'updates'
op|'='
name|'db_mock'
op|'.'
name|'call_args'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_rule'
op|'['
string|"'id'"
op|']'
op|','
name|'rule'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'updates'
op|'['
string|"'group_id'"
op|']'
op|','
name|'rule'
op|'.'
name|'grantee_group'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'updates'
op|'['
string|"'parent_group_id'"
op|']'
op|','
name|'rule'
op|'.'
name|'parent_group'
op|'.'
name|'id'
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
name|'db'
op|','
string|"'security_group_rule_create'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fake_rule'
op|')'
newline|'\n'
DECL|member|test_set_id_failure
name|'def'
name|'test_set_id_failure'
op|'('
name|'self'
op|','
name|'db_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
name|'objects'
op|'.'
name|'SecurityGroupRule'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'rule'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ReadOnlyFieldError'
op|','
name|'setattr'
op|','
nl|'\n'
name|'rule'
op|','
string|"'id'"
op|','
number|'124'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestSecurityGroupRuleObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestSecurityGroupRuleObject
name|'_TestSecurityGroupRuleObject'
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
name|'TestSecurityGroupRuleObjectRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestSecurityGroupRuleObjectRemote
name|'_TestSecurityGroupRuleObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
