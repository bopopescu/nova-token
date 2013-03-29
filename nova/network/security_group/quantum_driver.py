begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Nicira, Inc.'
nl|'\n'
comment|'# All Rights Reserved'
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
comment|'#'
nl|'\n'
comment|'# @author: Aaron Rosen, Nicira Networks, Inc.'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'quantumclient'
op|'.'
name|'common'
name|'import'
name|'exceptions'
name|'as'
name|'q_exc'
newline|'\n'
name|'from'
name|'quantumclient'
op|'.'
name|'quantum'
name|'import'
name|'v2_0'
name|'as'
name|'quantumv20'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'quantumv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'security_group'
name|'import'
name|'security_group_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|wrap_check_security_groups_policy
name|'wrap_check_security_groups_policy'
op|'='
name|'compute_api'
op|'.'
name|'policy_decorator'
op|'('
nl|'\n'
DECL|variable|scope
name|'scope'
op|'='
string|"'compute:security_groups'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupAPI
name|'class'
name|'SecurityGroupAPI'
op|'('
name|'security_group_base'
op|'.'
name|'SecurityGroupBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|id_is_uuid
indent|'    '
name|'id_is_uuid'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|create_security_group
name|'def'
name|'create_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'_make_quantum_security_group_dict'
op|'('
name|'name'
op|','
name|'description'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'security_group'
op|'='
name|'quantum'
op|'.'
name|'create_security_group'
op|'('
nl|'\n'
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'security_group'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error creating security group %s"'
op|')'
op|','
nl|'\n'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'401'
op|':'
newline|'\n'
comment|'# TODO(arosen) Cannot raise generic response from quantum here'
nl|'\n'
comment|'# as this error code could be related to bad input or over'
nl|'\n'
comment|'# quota'
nl|'\n'
indent|'                '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'e'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_convert_to_nova_security_group_format'
op|'('
name|'security_group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_convert_to_nova_security_group_format
dedent|''
name|'def'
name|'_convert_to_nova_security_group_format'
op|'('
name|'self'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nova_group'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'nova_group'
op|'['
string|"'id'"
op|']'
op|'='
name|'security_group'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'nova_group'
op|'['
string|"'description'"
op|']'
op|'='
name|'security_group'
op|'['
string|"'description'"
op|']'
newline|'\n'
name|'nova_group'
op|'['
string|"'name'"
op|']'
op|'='
name|'security_group'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'nova_group'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'security_group'
op|'['
string|"'tenant_id'"
op|']'
newline|'\n'
name|'nova_group'
op|'['
string|"'rules'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'security_group'
op|'.'
name|'get'
op|'('
string|"'security_group_rules'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'rule'
op|'['
string|"'direction'"
op|']'
op|'=='
string|"'ingress'"
op|':'
newline|'\n'
indent|'                '
name|'nova_group'
op|'['
string|"'rules'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_convert_to_nova_security_group_rule_format'
op|'('
name|'rule'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'nova_group'
newline|'\n'
nl|'\n'
DECL|member|_convert_to_nova_security_group_rule_format
dedent|''
name|'def'
name|'_convert_to_nova_security_group_rule_format'
op|'('
name|'self'
op|','
name|'rule'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nova_rule'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'nova_rule'
op|'['
string|"'id'"
op|']'
op|'='
name|'rule'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'nova_rule'
op|'['
string|"'parent_group_id'"
op|']'
op|'='
name|'rule'
op|'['
string|"'security_group_id'"
op|']'
newline|'\n'
name|'nova_rule'
op|'['
string|"'protocol'"
op|']'
op|'='
name|'rule'
op|'['
string|"'protocol'"
op|']'
newline|'\n'
name|'if'
name|'rule'
op|'['
string|"'port_range_min'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'nova_rule'
op|'['
string|"'from_port'"
op|']'
op|'='
op|'-'
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'nova_rule'
op|'['
string|"'from_port'"
op|']'
op|'='
name|'rule'
op|'['
string|"'port_range_min'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'rule'
op|'['
string|"'port_range_max'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'nova_rule'
op|'['
string|"'to_port'"
op|']'
op|'='
op|'-'
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'nova_rule'
op|'['
string|"'to_port'"
op|']'
op|'='
name|'rule'
op|'['
string|"'port_range_max'"
op|']'
newline|'\n'
dedent|''
name|'nova_rule'
op|'['
string|"'group_id'"
op|']'
op|'='
name|'rule'
op|'['
string|"'remote_group_id'"
op|']'
newline|'\n'
name|'nova_rule'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'rule'
op|'['
string|"'remote_ip_prefix'"
op|']'
newline|'\n'
name|'return'
name|'nova_rule'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|'='
name|'None'
op|','
name|'id'
op|'='
name|'None'
op|','
name|'map_exception'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'id'
name|'and'
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'id'
op|'='
name|'quantumv20'
op|'.'
name|'find_resourceid_by_name_or_id'
op|'('
nl|'\n'
name|'quantum'
op|','
string|"'security_group'"
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'group'
op|'='
name|'quantum'
op|'.'
name|'show_security_group'
op|'('
name|'id'
op|')'
op|'.'
name|'get'
op|'('
string|"'security_group'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'404'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error getting security group %s"'
op|')'
op|','
nl|'\n'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Quantum Error: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_convert_to_nova_security_group_format'
op|'('
name|'group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list
dedent|''
name|'def'
name|'list'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'names'
op|'='
name|'None'
op|','
name|'ids'
op|'='
name|'None'
op|','
name|'project'
op|'='
name|'None'
op|','
nl|'\n'
name|'search_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns list of security group rules owned by tenant."""'
newline|'\n'
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'search_opts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'names'
op|':'
newline|'\n'
indent|'            '
name|'search_opts'
op|'['
string|"'name'"
op|']'
op|'='
name|'names'
newline|'\n'
dedent|''
name|'if'
name|'ids'
op|':'
newline|'\n'
indent|'            '
name|'search_opts'
op|'['
string|"'id'"
op|']'
op|'='
name|'ids'
newline|'\n'
dedent|''
name|'if'
name|'project'
op|':'
newline|'\n'
indent|'            '
name|'search_opts'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'project'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'security_groups'
op|'='
name|'quantum'
op|'.'
name|'list_security_groups'
op|'('
op|'**'
name|'search_opts'
op|')'
op|'.'
name|'get'
op|'('
nl|'\n'
string|"'security_groups'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error getting security groups"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
name|'converted_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'security_group'
name|'in'
name|'security_groups'
op|':'
newline|'\n'
indent|'            '
name|'converted_rules'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_convert_to_nova_security_group_format'
op|'('
name|'security_group'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'converted_rules'
newline|'\n'
nl|'\n'
DECL|member|validate_id
dedent|''
name|'def'
name|'validate_id'
op|'('
name|'self'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Security group id should be uuid"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_invalid_property'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This function deletes a security group."""'
newline|'\n'
nl|'\n'
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'quantum'
op|'.'
name|'delete_security_group'
op|'('
name|'security_group'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'404'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'409'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'raise_invalid_property'
op|'('
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Quantum Error: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
DECL|member|add_rules
dedent|''
dedent|''
dedent|''
name|'def'
name|'add_rules'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|','
name|'name'
op|','
name|'vals'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add security group rule(s) to security group.\n\n        Note: the Nova security group API doesn\'t support adding muliple\n        security group rules at once but the EC2 one does. Therefore,\n        this function is writen to support both. Multiple rules are\n        installed to a security group in quantum using bulk support."""'
newline|'\n'
nl|'\n'
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'body'
op|'='
name|'self'
op|'.'
name|'_make_quantum_security_group_rules_list'
op|'('
name|'vals'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rules'
op|'='
name|'quantum'
op|'.'
name|'create_security_group_rule'
op|'('
nl|'\n'
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'security_group_rules'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'409'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error getting security group %s"'
op|')'
op|','
nl|'\n'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error:"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
name|'converted_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'rules'
op|':'
newline|'\n'
indent|'            '
name|'converted_rules'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_convert_to_nova_security_group_rule_format'
op|'('
name|'rule'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'converted_rules'
newline|'\n'
nl|'\n'
DECL|member|_make_quantum_security_group_dict
dedent|''
name|'def'
name|'_make_quantum_security_group_dict'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'security_group'"
op|':'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'description'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_make_quantum_security_group_rules_list
dedent|''
name|'def'
name|'_make_quantum_security_group_rules_list'
op|'('
name|'self'
op|','
name|'rules'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'new_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'rules'
op|':'
newline|'\n'
indent|'            '
name|'new_rule'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|'# nova only supports ingress rules so all rules are ingress.'
nl|'\n'
name|'new_rule'
op|'['
string|"'direction'"
op|']'
op|'='
string|'"ingress"'
newline|'\n'
name|'new_rule'
op|'['
string|"'protocol'"
op|']'
op|'='
name|'rule'
op|'.'
name|'get'
op|'('
string|"'protocol'"
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME(arosen) Nova does not expose ethertype on security group'
nl|'\n'
comment|'# rules. Therefore, in the case of self referential rules we'
nl|'\n'
comment|'# should probably assume they want to allow both IPv4 and IPv6.'
nl|'\n'
comment|'# Unfortunately, this would require adding two rules in quantum.'
nl|'\n'
comment|'# The reason we do not do this is because when the user using the'
nl|'\n'
comment|"# nova api wants to remove the rule we'd have to have some way to"
nl|'\n'
comment|'# know that we should delete both of these rules in quantum.'
nl|'\n'
comment|'# For now, self referential rules only support IPv4.'
nl|'\n'
name|'if'
name|'not'
name|'rule'
op|'.'
name|'get'
op|'('
string|"'cidr'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'new_rule'
op|'['
string|"'ethertype'"
op|']'
op|'='
string|"'IPv4'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'new_rule'
op|'['
string|"'ethertype'"
op|']'
op|'='
name|'utils'
op|'.'
name|'get_ip_version'
op|'('
name|'rule'
op|'.'
name|'get'
op|'('
string|"'cidr'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'new_rule'
op|'['
string|"'remote_ip_prefix'"
op|']'
op|'='
name|'rule'
op|'.'
name|'get'
op|'('
string|"'cidr'"
op|')'
newline|'\n'
name|'new_rule'
op|'['
string|"'security_group_id'"
op|']'
op|'='
name|'rule'
op|'.'
name|'get'
op|'('
string|"'parent_group_id'"
op|')'
newline|'\n'
name|'new_rule'
op|'['
string|"'remote_group_id'"
op|']'
op|'='
name|'rule'
op|'.'
name|'get'
op|'('
string|"'group_id'"
op|')'
newline|'\n'
name|'if'
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'new_rule'
op|'['
string|"'port_range_min'"
op|']'
op|'='
name|'rule'
op|'['
string|"'from_port'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'rule'
op|'['
string|"'to_port'"
op|']'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'new_rule'
op|'['
string|"'port_range_max'"
op|']'
op|'='
name|'rule'
op|'['
string|"'to_port'"
op|']'
newline|'\n'
dedent|''
name|'new_rules'
op|'.'
name|'append'
op|'('
name|'new_rule'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'security_group_rules'"
op|':'
name|'new_rules'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|remove_rules
dedent|''
name|'def'
name|'remove_rules'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_group'
op|','
name|'rule_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'rule_ids'
op|'='
name|'set'
op|'('
name|'rule_ids'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# The ec2 api allows one to delete multiple security group rules'
nl|'\n'
comment|'# at once. Since there is no bulk delete for quantum the best'
nl|'\n'
comment|'# thing we can do is delete the rules one by one and hope this'
nl|'\n'
comment|'# works.... :/'
nl|'\n'
indent|'            '
name|'for'
name|'rule_id'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'rule_ids'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'quantum'
op|'.'
name|'delete_security_group_rule'
op|'('
name|'rule_ids'
op|'.'
name|'pop'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error unable to delete %s"'
op|')'
op|','
nl|'\n'
name|'rule_ids'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
DECL|member|get_rule
dedent|''
dedent|''
name|'def'
name|'get_rule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rule'
op|'='
name|'quantum'
op|'.'
name|'show_security_group_rule'
op|'('
nl|'\n'
name|'id'
op|')'
op|'.'
name|'get'
op|'('
string|"'security_group_rule'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'404'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error getting security group rule "'
nl|'\n'
string|'"%s."'
op|')'
op|'%'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Quantum Error: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_convert_to_nova_security_group_rule_format'
op|'('
name|'rule'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_security_groups
dedent|''
name|'def'
name|'get_instance_security_groups'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'None'
op|','
name|'detailed'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the security groups that are associated with an instance.\n        If detailed is True then it also returns the full details of the\n        security groups associated with an instance.\n        """'
newline|'\n'
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'instance_uuid'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
string|"'device_id'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
string|"'device_id'"
op|':'
name|'instance_id'
op|'}'
newline|'\n'
dedent|''
name|'ports'
op|'='
name|'quantum'
op|'.'
name|'list_ports'
op|'('
op|'**'
name|'params'
op|')'
newline|'\n'
name|'security_groups'
op|'='
name|'quantum'
op|'.'
name|'list_security_groups'
op|'('
op|')'
op|'.'
name|'get'
op|'('
string|"'security_groups'"
op|')'
newline|'\n'
nl|'\n'
name|'security_group_lookup'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'security_group'
name|'in'
name|'security_groups'
op|':'
newline|'\n'
indent|'            '
name|'security_group_lookup'
op|'['
name|'security_group'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'security_group'
newline|'\n'
nl|'\n'
dedent|''
name|'ret'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'port'
name|'in'
name|'ports'
op|'['
string|"'ports'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'security_group'
name|'in'
name|'port'
op|'.'
name|'get'
op|'('
string|"'security_groups'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'                        '
name|'ret'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_convert_to_nova_security_group_format'
op|'('
nl|'\n'
name|'security_group_lookup'
op|'['
name|'security_group'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'name'
op|'='
name|'security_group_lookup'
op|'['
name|'security_group'
op|']'
op|'.'
name|'get'
op|'('
nl|'\n'
string|"'name'"
op|')'
newline|'\n'
comment|'# Since the name is optional for'
nl|'\n'
comment|'# quantum security groups'
nl|'\n'
name|'if'
name|'not'
name|'name'
op|':'
newline|'\n'
indent|'                            '
name|'name'
op|'='
name|'security_group'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'ret'
op|'.'
name|'append'
op|'('
op|'{'
string|"'name'"
op|':'
name|'name'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|'# If this should only happen due to a race condition'
nl|'\n'
comment|'# if the security group on a port was deleted after the'
nl|'\n'
comment|'# ports were returned. We pass since this security'
nl|'\n'
comment|'# group is no longer on the port.'
nl|'\n'
indent|'                    '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|_has_security_group_requirements
dedent|''
name|'def'
name|'_has_security_group_requirements'
op|'('
name|'self'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'port_security_enabled'
op|'='
name|'port'
op|'.'
name|'get'
op|'('
string|"'port_security_enabled'"
op|')'
newline|'\n'
name|'has_ip'
op|'='
name|'port'
op|'.'
name|'get'
op|'('
string|"'fixed_ips'"
op|')'
newline|'\n'
name|'if'
name|'port_security_enabled'
name|'and'
name|'has_ip'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wrap_check_security_groups_policy'
newline|'\n'
DECL|member|add_to_instance
name|'def'
name|'add_to_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'security_group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add security group to the instance."""'
newline|'\n'
nl|'\n'
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'security_group_id'
op|'='
name|'quantumv20'
op|'.'
name|'find_resourceid_by_name_or_id'
op|'('
nl|'\n'
name|'quantum'
op|','
string|"'security_group'"
op|','
name|'security_group_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'404'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
string|'"Security group %s is not found for project %s"'
op|'%'
nl|'\n'
op|'('
name|'security_group_name'
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error:"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
name|'params'
op|'='
op|'{'
string|"'device_id'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ports'
op|'='
name|'quantum'
op|'.'
name|'list_ports'
op|'('
op|'**'
name|'params'
op|')'
op|'.'
name|'get'
op|'('
string|"'ports'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error:"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'ports'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
string|'"instance_id %s could not be found as device id on"'
nl|'\n'
string|'" any ports"'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'port'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_has_security_group_requirements'
op|'('
name|'port'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Cannot add security group %(name)s to %(instance)s"'
nl|'\n'
string|'" since the port %(port_id)s does not meet security"'
nl|'\n'
string|'" requirements"'
op|')'
op|','
op|'{'
string|"'name'"
op|':'
name|'security_group_name'
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
string|"'port_id'"
op|':'
name|'port'
op|'['
string|"'id'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'SecurityGroupCannotBeApplied'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'security_groups'"
name|'not'
name|'in'
name|'port'
op|':'
newline|'\n'
indent|'                '
name|'port'
op|'['
string|"'security_groups'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'port'
op|'['
string|"'security_groups'"
op|']'
op|'.'
name|'append'
op|'('
name|'security_group_id'
op|')'
newline|'\n'
name|'updated_port'
op|'='
op|'{'
string|"'security_groups'"
op|':'
name|'port'
op|'['
string|"'security_groups'"
op|']'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Adding security group %(security_group_id)s to "'
nl|'\n'
string|'"port %(port_id)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'security_group_id'"
op|':'
name|'security_group_id'
op|','
nl|'\n'
string|"'port_id'"
op|':'
name|'port'
op|'['
string|"'id'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'quantum'
op|'.'
name|'update_port'
op|'('
name|'port'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'port'"
op|':'
name|'updated_port'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error:"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
op|'@'
name|'wrap_check_security_groups_policy'
newline|'\n'
DECL|member|remove_from_instance
name|'def'
name|'remove_from_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'security_group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove the security group associated with the instance."""'
newline|'\n'
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'security_group_id'
op|'='
name|'quantumv20'
op|'.'
name|'find_resourceid_by_name_or_id'
op|'('
nl|'\n'
name|'quantum'
op|','
string|"'security_group'"
op|','
name|'security_group_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'status_code'
op|'=='
number|'404'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
string|'"Security group %s is not found for project %s"'
op|'%'
nl|'\n'
op|'('
name|'security_group_name'
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error:"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
name|'params'
op|'='
op|'{'
string|"'device_id'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ports'
op|'='
name|'quantum'
op|'.'
name|'list_ports'
op|'('
op|'**'
name|'params'
op|')'
op|'.'
name|'get'
op|'('
string|"'ports'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'q_exc'
op|'.'
name|'QuantumClientException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error:"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'ports'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
string|'"instance_id %s could not be found as device id on"'
nl|'\n'
string|'" any ports"'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'found_security_group'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'port'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'port'
op|'.'
name|'get'
op|'('
string|"'security_groups'"
op|','
op|'['
op|']'
op|')'
op|'.'
name|'remove'
op|'('
name|'security_group_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|'# When removing a security group from an instance the security'
nl|'\n'
comment|'# group should be on both ports since it was added this way if'
nl|'\n'
comment|'# done through the nova api. In case it is not a 404 is only'
nl|'\n'
comment|'# raised if the security group is not found on any of the'
nl|'\n'
comment|'# ports on the instance.'
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'updated_port'
op|'='
op|'{'
string|"'security_groups'"
op|':'
name|'port'
op|'['
string|"'security_groups'"
op|']'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Adding security group %(security_group_id)s to "'
nl|'\n'
string|'"port %(port_id)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'security_group_id'"
op|':'
name|'security_group_id'
op|','
nl|'\n'
string|"'port_id'"
op|':'
name|'port'
op|'['
string|"'id'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'quantum'
op|'.'
name|'update_port'
op|'('
name|'port'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'port'"
op|':'
name|'updated_port'
op|'}'
op|')'
newline|'\n'
name|'found_security_group'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Quantum Error:"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'found_security_group'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Security group %(security_group_name)s not assocaited "'
nl|'\n'
string|'"with the instance %(instance)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'security_group_name'"
op|':'
name|'security_group_name'
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_not_found'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|populate_security_groups
dedent|''
dedent|''
name|'def'
name|'populate_security_groups'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'security_groups'
op|')'
op|':'
newline|'\n'
comment|'# Setting to emply list since we do not want to populate this field'
nl|'\n'
comment|'# in the nova database if using the quantum driver'
nl|'\n'
indent|'        '
name|'instance'
op|'['
string|"'security_groups'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
