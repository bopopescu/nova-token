begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Nicira Networks, Inc'
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
string|'\'\'\'Implement Security Groups abstraction and API.\n\nThe nova security_group_handler flag specifies which class is to be used\nto implement the security group calls.\n\nThe NullSecurityGroupHandler provides a "no-op" plugin that is loaded\nby default and has no impact on current system behavior.  In the future,\nspecial purposes classes that inherit from SecurityGroupHandlerBase\nwill provide enhanced functionality and will be loadable via the\nsecurity_group_handler flag.\n\'\'\''
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupHandlerBase
name|'class'
name|'SecurityGroupHandlerBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_create_refresh
dedent|''
name|'def'
name|'trigger_security_group_create_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group is created\n\n        :param context: the security context.\n        :param group: the new group added. group is a dictionary that contains\n            the following: user_id, project_id, name, description).'''"
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_destroy_refresh
dedent|''
name|'def'
name|'trigger_security_group_destroy_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group is deleted\n\n        :param context: the security context.\n        :param security_group_id: the security group identifier.'''"
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_rule_create_refresh
dedent|''
name|'def'
name|'trigger_security_group_rule_create_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'rule_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a rule is added to a security_group.\n\n        :param context: the security context.\n        :param rule_ids: a list of rule ids that have been affected.'''"
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_rule_destroy_refresh
dedent|''
name|'def'
name|'trigger_security_group_rule_destroy_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'rule_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a rule is removed from a security_group.\n\n        :param context: the security context.\n        :param rule_ids: a list of rule ids that have been affected.'''"
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|trigger_instance_add_security_group_refresh
dedent|''
name|'def'
name|'trigger_instance_add_security_group_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group gains a new member.\n\n        :param context: the security context.\n        :param instance: the instance to be associated.\n        :param group_name: the name of the security group to be associated.'''"
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|trigger_instance_remove_security_group_refresh
dedent|''
name|'def'
name|'trigger_instance_remove_security_group_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group loses a member.\n\n        :param context: the security context.\n        :param instance: the instance to be associated.\n        :param group_name: the name of the security group to be associated.'''"
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_members_refresh
dedent|''
name|'def'
name|'trigger_security_group_members_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group gains or loses a member.\n\n        :param context: the security context.\n        :param group_ids: a list of security group identifiers.'''"
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NullSecurityGroupHandler
dedent|''
dedent|''
name|'class'
name|'NullSecurityGroupHandler'
op|'('
name|'SecurityGroupHandlerBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_create_refresh
dedent|''
name|'def'
name|'trigger_security_group_create_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a rule is added to a security_group.\n\n        :param context: the security context.\n        :param group: the new group added. group is a dictionary that contains\n            the following: user_id, project_id, name, description).'''"
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_destroy_refresh
dedent|''
name|'def'
name|'trigger_security_group_destroy_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a rule is added to a security_group.\n\n        :param context: the security context.\n        :param security_group_id: the security group identifier.'''"
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_rule_create_refresh
dedent|''
name|'def'
name|'trigger_security_group_rule_create_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'rule_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a rule is added to a security_group.\n\n        :param context: the security context.\n        :param rule_ids: a list of rule ids that have been affected.'''"
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_rule_destroy_refresh
dedent|''
name|'def'
name|'trigger_security_group_rule_destroy_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'rule_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a rule is removed from a security_group.\n\n        :param context: the security context.\n        :param rule_ids: a list of rule ids that have been affected.'''"
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_instance_add_security_group_refresh
dedent|''
name|'def'
name|'trigger_instance_add_security_group_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group gains a new member.\n\n        :param context: the security context.\n        :param instance: the instance to be associated.\n        :param group_name: the name of the security group to be associated.'''"
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_instance_remove_security_group_refresh
dedent|''
name|'def'
name|'trigger_instance_remove_security_group_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group loses a member.\n\n        :param context: the security context.\n        :param instance: the instance to be associated.\n        :param group_name: the name of the security group to be associated.'''"
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_security_group_members_refresh
dedent|''
name|'def'
name|'trigger_security_group_members_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Called when a security group gains or loses a member.\n\n        :param context: the security context.\n        :param group_ids: a list of security group identifiers.'''"
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
