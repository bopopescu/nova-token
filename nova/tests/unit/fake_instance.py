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
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
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
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_db_secgroups
name|'def'
name|'fake_db_secgroups'
op|'('
name|'instance'
op|','
name|'names'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'secgroups'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
op|','
name|'name'
name|'in'
name|'enumerate'
op|'('
name|'names'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group_name'
op|'='
string|"'secgroup-%i'"
op|'%'
name|'i'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'name'
op|','
name|'dict'
op|')'
name|'and'
name|'name'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'group_name'
op|'='
name|'name'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
dedent|''
name|'secgroups'
op|'.'
name|'append'
op|'('
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'i'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'group_name'
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'Fake secgroup'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
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
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'secgroups'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_db_instance
dedent|''
name|'def'
name|'fake_db_instance'
op|'('
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
string|"'instance_type'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'updates'
op|'['
string|"'instance_type'"
op|']'
op|','
name|'objects'
op|'.'
name|'Flavor'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'='
name|'updates'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
op|'**'
name|'updates'
op|'['
string|"'instance_type'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'flavorinfo'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
nl|'\n'
string|"'cur'"
op|':'
name|'flavor'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
nl|'\n'
string|"'old'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'new'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'flavorinfo'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'db_instance'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake-user'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake-project'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake-host'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1955'
op|','
number|'11'
op|','
number|'5'
op|')'
op|','
nl|'\n'
string|"'pci_devices'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'extra'"
op|':'
op|'{'
string|"'pci_requests'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'flavor'"
op|':'
name|'flavorinfo'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vcpu_model'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'tags'"
op|':'
op|'['
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'name'
op|','
name|'field'
name|'in'
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'fields'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'in'
name|'db_instance'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'field'
op|'.'
name|'nullable'
op|':'
newline|'\n'
indent|'            '
name|'db_instance'
op|'['
name|'name'
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'.'
name|'default'
op|'!='
name|'fields'
op|'.'
name|'UnspecifiedDefault'
op|':'
newline|'\n'
indent|'            '
name|'db_instance'
op|'['
name|'name'
op|']'
op|'='
name|'field'
op|'.'
name|'default'
newline|'\n'
dedent|''
name|'elif'
name|'name'
name|'in'
op|'['
string|"'flavor'"
op|','
string|"'ec2_ids'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'fake_db_instance needs help with %s'"
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'        '
name|'db_instance'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'db_instance'
op|'.'
name|'get'
op|'('
string|"'security_groups'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_instance'
op|'['
string|"'security_groups'"
op|']'
op|'='
name|'fake_db_secgroups'
op|'('
nl|'\n'
name|'db_instance'
op|','
name|'db_instance'
op|'['
string|"'security_groups'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_obj
dedent|''
name|'def'
name|'fake_instance_obj'
op|'('
name|'context'
op|','
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'expected_attrs'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'expected_attrs'"
op|','
name|'None'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'flavor'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'flavor'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'name'
op|'='
string|"'flavor1'"
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'256'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'root_gb'
op|'='
number|'1'
op|','
name|'ephemeral_gb'
op|'='
number|'1'
op|','
nl|'\n'
name|'flavorid'
op|'='
string|"'1'"
op|','
nl|'\n'
name|'swap'
op|'='
number|'0'
op|','
name|'rxtx_factor'
op|'='
number|'1.0'
op|','
nl|'\n'
name|'vcpu_weight'
op|'='
number|'1'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
name|'is_public'
op|'='
name|'True'
op|','
nl|'\n'
name|'extra_specs'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'projects'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
dedent|''
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Instance'
op|'('
op|')'
op|','
name|'fake_db_instance'
op|'('
op|'**'
name|'updates'
op|')'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'expected_attrs'
op|')'
newline|'\n'
name|'if'
name|'flavor'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'.'
name|'flavor'
op|'='
name|'flavor'
newline|'\n'
dedent|''
name|'inst'
op|'.'
name|'old_flavor'
op|'='
name|'None'
newline|'\n'
name|'inst'
op|'.'
name|'new_flavor'
op|'='
name|'None'
newline|'\n'
name|'inst'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_fault_obj
dedent|''
name|'def'
name|'fake_fault_obj'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'code'
op|'='
number|'404'
op|','
nl|'\n'
name|'message'
op|'='
string|"'HTTPNotFound'"
op|','
nl|'\n'
name|'details'
op|'='
string|"'Stock details for test'"
op|','
nl|'\n'
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fault'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'code'"
op|':'
name|'code'
op|','
nl|'\n'
string|"'message'"
op|':'
name|'message'
op|','
nl|'\n'
string|"'details'"
op|':'
name|'details'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
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
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'        '
name|'fault'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'objects'
op|'.'
name|'InstanceFault'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceFault'
op|'('
op|')'
op|','
nl|'\n'
name|'fault'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
