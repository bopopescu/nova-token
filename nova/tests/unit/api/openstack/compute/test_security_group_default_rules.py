begin_unit
comment|'# Copyright 2013 Metacloud, Inc'
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
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'security_group_default_rules'
name|'as'
name|'security_group_default_rules_v2'
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
name|'security_group_default_rules'
name|'as'
name|'security_group_default_rules_v21'
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
DECL|function|security_group_default_rule_template
dedent|''
dedent|''
name|'def'
name|'security_group_default_rule_template'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'rule'
op|'='
name|'kwargs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'rule'
op|'.'
name|'setdefault'
op|'('
string|"'ip_protocol'"
op|','
string|"'TCP'"
op|')'
newline|'\n'
name|'rule'
op|'.'
name|'setdefault'
op|'('
string|"'from_port'"
op|','
number|'22'
op|')'
newline|'\n'
name|'rule'
op|'.'
name|'setdefault'
op|'('
string|"'to_port'"
op|','
number|'22'
op|')'
newline|'\n'
name|'rule'
op|'.'
name|'setdefault'
op|'('
string|"'cidr'"
op|','
string|"'10.10.10.0/24'"
op|')'
newline|'\n'
name|'return'
name|'rule'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|security_group_default_rule_db
dedent|''
name|'def'
name|'security_group_default_rule_db'
op|'('
name|'security_group_default_rule'
op|','
name|'id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'attrs'
op|'='
name|'security_group_default_rule'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'if'
name|'id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
dedent|''
name|'return'
name|'AttrDict'
op|'('
name|'attrs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSecurityGroupDefaultRulesNeutronV21
dedent|''
name|'class'
name|'TestSecurityGroupDefaultRulesNeutronV21'
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
op|'('
name|'security_group_default_rules_v21'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRulesController'
op|')'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'security_group_api'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'super'
op|'('
name|'TestSecurityGroupDefaultRulesNeutronV21'
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
name|'controller_cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_not_implemented_neutron
dedent|''
name|'def'
name|'test_create_security_group_default_rule_not_implemented_neutron'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
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
nl|'\n'
string|"'/v2/fake/os-security-group-default-rules'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
name|'HTTPNotImplemented'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_group_default_rules_list_not_implemented_neutron
dedent|''
name|'def'
name|'test_security_group_default_rules_list_not_implemented_neutron'
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
nl|'\n'
string|"'/v2/fake/os-security-group-default-rules'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
name|'HTTPNotImplemented'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_group_default_rules_show_not_implemented_neutron
dedent|''
name|'def'
name|'test_security_group_default_rules_show_not_implemented_neutron'
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
nl|'\n'
string|"'/v2/fake/os-security-group-default-rules'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
name|'HTTPNotImplemented'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
string|"'602ed77c-a076-4f9b-a617-f93b847b62c5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_group_default_rules_delete_not_implemented_neutron
dedent|''
name|'def'
name|'test_security_group_default_rules_delete_not_implemented_neutron'
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
nl|'\n'
string|"'/v2/fake/os-security-group-default-rules'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
name|'HTTPNotImplemented'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
string|"'602ed77c-a076-4f9b-a617-f93b847b62c5'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSecurityGroupDefaultRulesNeutronV2
dedent|''
dedent|''
name|'class'
name|'TestSecurityGroupDefaultRulesNeutronV2'
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
op|'('
name|'security_group_default_rules_v2'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRulesController'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSecurityGroupDefaultRulesV21
dedent|''
name|'class'
name|'TestSecurityGroupDefaultRulesV21'
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
op|'('
name|'security_group_default_rules_v21'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRulesController'
op|')'
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
name|'TestSecurityGroupDefaultRulesV21'
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
name|'controller_cls'
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
nl|'\n'
string|"'/v2/fake/os-security-group-default-rules'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule
dedent|''
name|'def'
name|'test_create_security_group_default_rule'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'sgr_dict'
op|'='
name|'dict'
op|'('
name|'security_group_default_rule'
op|'='
name|'sgr'
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
name|'sgr_dict'
op|')'
newline|'\n'
name|'security_group_default_rule'
op|'='
name|'res_dict'
op|'['
string|"'security_group_default_rule'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'ip_protocol'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'ip_protocol'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'from_port'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'from_port'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'to_port'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'to_port'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'ip_range'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_no_to_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_no_to_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
op|')'
newline|'\n'
name|'del'
name|'sgr'
op|'['
string|"'to_port'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_no_from_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_no_from_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
op|')'
newline|'\n'
name|'del'
name|'sgr'
op|'['
string|"'from_port'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_no_ip_protocol
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_no_ip_protocol'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
op|')'
newline|'\n'
name|'del'
name|'sgr'
op|'['
string|"'ip_protocol'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_no_cidr
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_no_cidr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
op|')'
newline|'\n'
name|'del'
name|'sgr'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
nl|'\n'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
name|'security_group_default_rule'
op|'='
name|'res_dict'
op|'['
string|"'security_group_default_rule'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'id'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'ip_range'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_blank_to_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_blank_to_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'to_port'
op|'='
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_blank_from_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_blank_from_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'from_port'
op|'='
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_blank_ip_protocol
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_blank_ip_protocol'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'ip_protocol'
op|'='
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_blank_cidr
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_blank_cidr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'cidr'
op|'='
string|"''"
op|')'
newline|'\n'
nl|'\n'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
name|'security_group_default_rule'
op|'='
name|'res_dict'
op|'['
string|"'security_group_default_rule'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'id'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'ip_range'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_non_numerical_to_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_non_numerical_to_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'to_port'
op|'='
string|"'invalid'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_non_numerical_from_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_non_numerical_from_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'from_port'
op|'='
string|"'invalid'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_invalid_ip_protocol
dedent|''
name|'def'
name|'test_create_security_group_default_rule_invalid_ip_protocol'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'ip_protocol'
op|'='
string|"'invalid'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_invalid_cidr
dedent|''
name|'def'
name|'test_create_security_group_default_rule_invalid_cidr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'cidr'
op|'='
string|"'10.10.2222.0/24'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_invalid_to_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_invalid_to_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'to_port'
op|'='
string|"'666666'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_invalid_from_port
dedent|''
name|'def'
name|'test_create_security_group_default_rule_invalid_from_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'from_port'
op|'='
string|"'666666'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rule_with_no_body
dedent|''
name|'def'
name|'test_create_security_group_default_rule_with_no_body'
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
name|'HTTPBadRequest'
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
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_duplicate_security_group_default_rule
dedent|''
name|'def'
name|'test_create_duplicate_security_group_default_rule'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
op|'{'
string|"'security_group_default_rule'"
op|':'
name|'sgr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_group_default_rules_list
dedent|''
name|'def'
name|'test_security_group_default_rules_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_create_security_group_default_rule'
op|'('
op|')'
newline|'\n'
name|'rules'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'TCP'"
op|','
nl|'\n'
name|'from_port'
op|'='
number|'22'
op|','
nl|'\n'
name|'to_port'
op|'='
number|'22'
op|','
nl|'\n'
name|'ip_range'
op|'='
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'10.10.10.0/24'"
op|')'
op|')'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'security_group_default_rules'"
op|':'
name|'rules'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.security_group_default_rule_list'"
op|','
nl|'\n'
name|'side_effect'
op|'='
op|'('
name|'exception'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRuleNotFound'
op|'('
string|'"Rule Not Found"'
op|')'
op|')'
op|')'
newline|'\n'
DECL|member|test_non_existing_security_group_default_rules_list
name|'def'
name|'test_non_existing_security_group_default_rules_list'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_sec_grp_rule'
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
name|'index'
op|','
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_security_group_default_rule_show
dedent|''
name|'def'
name|'test_default_security_group_default_rule_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'id'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'test_create_security_group_default_rule'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
name|'security_group_default_rule'
op|'='
name|'res_dict'
op|'['
string|"'security_group_default_rule'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'ip_protocol'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'ip_protocol'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'to_port'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'to_port'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'from_port'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'from_port'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'security_group_default_rule'
op|'['
string|"'ip_range'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
name|'sgr'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.security_group_default_rule_get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
op|'('
name|'exception'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRuleNotFound'
op|'('
string|'"Rule Not Found"'
op|')'
op|')'
op|')'
newline|'\n'
DECL|member|test_non_existing_security_group_default_rule_show
name|'def'
name|'test_non_existing_security_group_default_rule_show'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_sec_grp_rule'
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
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_security_group_default_rule
dedent|''
name|'def'
name|'test_delete_security_group_default_rule'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'id'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'test_create_security_group_default_rule'
op|'('
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
DECL|function|security_group_default_rule_destroy
name|'def'
name|'security_group_default_rule_destroy'
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
DECL|function|return_security_group_default_rule
dedent|''
name|'def'
name|'return_security_group_default_rule'
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
name|'assertEqual'
op|'('
name|'sgr'
op|'['
string|"'id'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'security_group_default_rule_db'
op|'('
name|'sgr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.security_group_default_rule_destroy'"
op|','
nl|'\n'
name|'security_group_default_rule_destroy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.security_group_default_rule_get'"
op|','
nl|'\n'
name|'return_security_group_default_rule'
op|')'
newline|'\n'
nl|'\n'
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
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
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
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.security_group_default_rule_destroy'"
op|','
nl|'\n'
name|'side_effect'
op|'='
op|'('
name|'exception'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRuleNotFound'
op|'('
string|'"Rule Not Found"'
op|')'
op|')'
op|')'
newline|'\n'
DECL|member|test_non_existing_security_group_default_rule_delete
name|'def'
name|'test_non_existing_security_group_default_rule_delete'
op|'('
nl|'\n'
name|'self'
op|','
name|'mock_sec_grp_rule'
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
name|'delete'
op|','
name|'self'
op|'.'
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_group_ensure_default
dedent|''
name|'def'
name|'test_security_group_ensure_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
name|'id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_create_security_group_default_rule'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'setattr'
op|'('
name|'ctxt'
op|','
string|"'project_id'"
op|','
string|"'new_project_id'"
op|')'
newline|'\n'
nl|'\n'
name|'sg'
op|'='
name|'nova'
op|'.'
name|'db'
op|'.'
name|'security_group_ensure_default'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'rules'
op|'='
name|'nova'
op|'.'
name|'db'
op|'.'
name|'security_group_rule_get_by_security_group'
op|'('
name|'ctxt'
op|','
name|'sg'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'security_group_rule'
op|'='
name|'rules'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sgr'
op|'['
string|"'id'"
op|']'
op|','
name|'security_group_rule'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sgr'
op|'['
string|"'ip_protocol'"
op|']'
op|','
name|'security_group_rule'
op|'.'
name|'protocol'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sgr'
op|'['
string|"'from_port'"
op|']'
op|','
name|'security_group_rule'
op|'.'
name|'from_port'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sgr'
op|'['
string|"'to_port'"
op|']'
op|','
name|'security_group_rule'
op|'.'
name|'to_port'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sgr'
op|'['
string|"'cidr'"
op|']'
op|','
name|'security_group_rule'
op|'.'
name|'cidr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSecurityGroupDefaultRulesV2
dedent|''
dedent|''
name|'class'
name|'TestSecurityGroupDefaultRulesV2'
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
op|'('
name|'security_group_default_rules_v2'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRulesController'
op|')'
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
name|'TestSecurityGroupDefaultRulesV2'
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-security-group-default-rules'"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'non_admin_req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-security-group-default-rules'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_security_group_default_rules_with_non_admin
dedent|''
name|'def'
name|'test_create_security_group_default_rules_with_non_admin'
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
name|'self'
op|'.'
name|'controller_cls'
op|'('
op|')'
newline|'\n'
name|'sgr'
op|'='
name|'security_group_default_rule_template'
op|'('
op|')'
newline|'\n'
name|'sgr_dict'
op|'='
name|'dict'
op|'('
name|'security_group_default_rule'
op|'='
name|'sgr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AdminRequired'
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
name|'non_admin_req'
op|','
name|'sgr_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_security_group_default_rules_with_non_admin
dedent|''
name|'def'
name|'test_delete_security_group_default_rules_with_non_admin'
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
name|'self'
op|'.'
name|'controller_cls'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AdminRequired'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'self'
op|'.'
name|'non_admin_req'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupDefaultRulesPolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'SecurityGroupDefaultRulesPolicyEnforcementV21'
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
name|'SecurityGroupDefaultRulesPolicyEnforcementV21'
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
op|'('
name|'security_group_default_rules_v21'
op|'.'
nl|'\n'
name|'SecurityGroupDefaultRulesController'
op|'('
op|')'
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
DECL|member|_common_policy_check
dedent|''
name|'def'
name|'_common_policy_check'
op|'('
name|'self'
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
name|'rule_name'
op|'='
string|'"os_compute_api:os-security-group-default-rules"'
newline|'\n'
name|'rule'
op|'='
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
newline|'\n'
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
name|'rule_name'
op|','
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_policy_failed
dedent|''
name|'def'
name|'test_create_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
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
op|'{'
op|'}'
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
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
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
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_policy_failed
dedent|''
name|'def'
name|'test_delete_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_policy_failed
dedent|''
name|'def'
name|'test_index_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
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
dedent|''
dedent|''
endmarker|''
end_unit
