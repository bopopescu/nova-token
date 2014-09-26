begin_unit
comment|'#    Copyright 2014 Red Hat, Inc.'
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
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|FLOATING_IP_OPTIONAL_ATTRS
name|'FLOATING_IP_OPTIONAL_ATTRS'
op|'='
op|'['
string|"'fixed_ip'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIP
name|'class'
name|'FloatingIP'
op|'('
name|'obj_base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added _get_addresses_by_instance_uuid()'
nl|'\n'
comment|'# Version 1.2: FixedIP <= version 1.2'
nl|'\n'
comment|'# Version 1.3: FixedIP <= version 1.3'
nl|'\n'
comment|'# Version 1.4: FixedIP <= version 1.4'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.4'"
newline|'\n'
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
string|"'address'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
op|')'
op|','
nl|'\n'
string|"'fixed_ip_id'"
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
string|"'project_id'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'host'"
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
string|"'auto_assigned'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'pool'"
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
string|"'interface'"
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
string|"'fixed_ip'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'FixedIP'"
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
DECL|member|obj_make_compatible
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'2'
op|')'
name|'and'
string|"'fixed_ip'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixed_ip'
op|'.'
name|'obj_make_compatible'
op|'('
nl|'\n'
name|'primitive'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'nova_object.data'"
op|']'
op|','
string|"'1.1'"
op|')'
newline|'\n'
name|'primitive'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'nova_object.version'"
op|']'
op|'='
string|"'1.1'"
newline|'\n'
dedent|''
name|'elif'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'3'
op|')'
name|'and'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'fixed_ip'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixed_ip'
op|'.'
name|'obj_make_compatible'
op|'('
nl|'\n'
name|'primitive'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'nova_object.data'"
op|']'
op|','
string|"'1.2'"
op|')'
newline|'\n'
name|'primitive'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'nova_object.version'"
op|']'
op|'='
string|"'1.2'"
newline|'\n'
dedent|''
name|'elif'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'4'
op|')'
name|'and'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'fixed_ip'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixed_ip'
op|'.'
name|'obj_make_compatible'
op|'('
nl|'\n'
name|'primitive'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'nova_object.data'"
op|']'
op|','
string|"'1.3'"
op|')'
newline|'\n'
name|'primitive'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'nova_object.version'"
op|']'
op|'='
string|"'1.3'"
newline|'\n'
nl|'\n'
dedent|''
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
name|'floatingip'
op|','
name|'db_floatingip'
op|','
nl|'\n'
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
name|'floatingip'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'not'
name|'in'
name|'FLOATING_IP_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'                '
name|'floatingip'
op|'['
name|'field'
op|']'
op|'='
name|'db_floatingip'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'if'
op|'('
string|"'fixed_ip'"
name|'in'
name|'expected_attrs'
name|'and'
nl|'\n'
name|'db_floatingip'
op|'['
string|"'fixed_ip'"
op|']'
name|'is'
name|'not'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'floatingip'
op|'.'
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'objects'
op|'.'
name|'FixedIP'
op|'('
name|'context'
op|')'
op|','
name|'db_floatingip'
op|'['
string|"'fixed_ip'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'floatingip'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'floatingip'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'floatingip'
newline|'\n'
nl|'\n'
DECL|member|obj_load_attr
dedent|''
name|'def'
name|'obj_load_attr'
op|'('
name|'self'
op|','
name|'attrname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'attrname'
name|'not'
name|'in'
name|'FLOATING_IP_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'obj_load_attr'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'attribute %s is not lazy-loadable'"
op|'%'
name|'attrname'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_context'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'OrphanedObjectError'
op|'('
name|'method'
op|'='
string|"'obj_load_attr'"
op|','
nl|'\n'
name|'objtype'
op|'='
name|'self'
op|'.'
name|'obj_name'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'fixed_ip_id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'.'
name|'get_by_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'fixed_ip_id'
op|','
name|'expected_attrs'
op|'='
op|'['
string|"'network'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixed_ip'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'obj_base'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_floatingip'
op|'='
name|'db'
op|'.'
name|'floating_ip_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
comment|'# XXX joins fixed.instance'
nl|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_floatingip'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'fixed_ip'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_address
name|'def'
name|'get_by_address'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_floatingip'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'str'
op|'('
name|'address'
op|')'
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
name|'context'
op|')'
op|','
name|'db_floatingip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_pool_names
name|'def'
name|'get_pool_names'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'x'
op|'['
string|"'name'"
op|']'
name|'for'
name|'x'
name|'in'
name|'db'
op|'.'
name|'floating_ip_get_pools'
op|'('
name|'context'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|allocate_address
name|'def'
name|'allocate_address'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'pool'
op|','
name|'auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'floating_ip_allocate_address'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'pool'
op|','
nl|'\n'
name|'auto_assigned'
op|'='
name|'auto_assigned'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|associate
name|'def'
name|'associate'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'floating_address'
op|','
name|'fixed_address'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixed'
op|'='
name|'db'
op|'.'
name|'floating_ip_fixed_ip_associate'
op|'('
name|'context'
op|','
nl|'\n'
name|'str'
op|'('
name|'floating_address'
op|')'
op|','
nl|'\n'
name|'str'
op|'('
name|'fixed_address'
op|')'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
name|'if'
name|'db_fixed'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'floating'
op|'='
name|'FloatingIP'
op|'('
nl|'\n'
name|'context'
op|'='
name|'context'
op|','
name|'address'
op|'='
name|'floating_address'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'fixed_ip_id'
op|'='
name|'db_fixed'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'objects'
op|'.'
name|'FixedIP'
op|'('
name|'context'
op|')'
op|','
name|'db_fixed'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'network'"
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'floating'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|deallocate
name|'def'
name|'deallocate'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'floating_ip_deallocate'
op|'('
name|'context'
op|','
name|'str'
op|'('
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'context'
op|','
name|'str'
op|'('
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|disassociate
name|'def'
name|'disassociate'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixed'
op|'='
name|'db'
op|'.'
name|'floating_ip_disassociate'
op|'('
name|'context'
op|','
name|'str'
op|'('
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'cls'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'address'
op|'='
name|'address'
op|','
nl|'\n'
name|'fixed_ip_id'
op|'='
name|'db_fixed'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'objects'
op|'.'
name|'FixedIP'
op|'('
name|'context'
op|')'
op|','
name|'db_fixed'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'network'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|_get_addresses_by_instance_uuid
name|'def'
name|'_get_addresses_by_instance_uuid'
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
name|'return'
name|'db'
op|'.'
name|'instance_floating_address_get_all'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_addresses_by_instance
name|'def'
name|'get_addresses_by_instance'
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
name|'_get_addresses_by_instance_uuid'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'context'
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
string|"'address'"
name|'in'
name|'updates'
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
string|"'save'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'address is not mutable'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'fixed_ip_id'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'='
string|"'fixed_ip_id is not mutable'"
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'save'"
op|','
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(danms): Make sure we don't pass the calculated fixed_ip"
nl|'\n'
comment|'# relationship to the DB update method'
nl|'\n'
dedent|''
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'fixed_ip'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'db_floatingip'
op|'='
name|'db'
op|'.'
name|'floating_ip_update'
op|'('
name|'context'
op|','
name|'str'
op|'('
name|'self'
op|'.'
name|'address'
op|')'
op|','
nl|'\n'
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_floatingip'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPList
dedent|''
dedent|''
name|'class'
name|'FloatingIPList'
op|'('
name|'obj_base'
op|'.'
name|'ObjectListBase'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.3: FloatingIP 1.2'
nl|'\n'
comment|'# Version 1.4: FloatingIP 1.3'
nl|'\n'
comment|'# Version 1.5: FloatingIP 1.4'
nl|'\n'
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
string|"'FloatingIP'"
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
string|"'1.0'"
op|','
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'1.2'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'1.3'"
op|':'
string|"'1.2'"
op|','
nl|'\n'
string|"'1.4'"
op|':'
string|"'1.3'"
op|','
nl|'\n'
string|"'1.5'"
op|':'
string|"'1.4'"
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|VERSION
name|'VERSION'
op|'='
string|"'1.5'"
newline|'\n'
nl|'\n'
op|'@'
name|'obj_base'
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
name|'db_floatingips'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
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
name|'FloatingIP'
op|','
name|'db_floatingips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host
name|'def'
name|'get_by_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_floatingips'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
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
name|'FloatingIP'
op|','
name|'db_floatingips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
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
name|'db_floatingips'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_all_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
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
name|'FloatingIP'
op|','
name|'db_floatingips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_fixed_address
name|'def'
name|'get_by_fixed_address'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_floatingips'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_by_fixed_address'
op|'('
nl|'\n'
name|'context'
op|','
name|'str'
op|'('
name|'fixed_address'
op|')'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
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
name|'FloatingIP'
op|','
name|'db_floatingips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_fixed_ip_id
name|'def'
name|'get_by_fixed_ip_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'fixed_ip_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_floatingips'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_by_fixed_ip_id'
op|'('
name|'context'
op|','
nl|'\n'
name|'fixed_ip_id'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'FloatingIP'
op|','
nl|'\n'
name|'db_floatingips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|make_ip_info
name|'def'
name|'make_ip_info'
op|'('
name|'address'
op|','
name|'pool'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'address'"
op|':'
name|'str'
op|'('
name|'address'
op|')'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'interface'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'ip_info'
op|','
name|'want_result'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_floatingips'
op|'='
name|'db'
op|'.'
name|'floating_ip_bulk_create'
op|'('
name|'context'
op|','
name|'ip_info'
op|')'
newline|'\n'
name|'if'
name|'want_result'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'obj_base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'FloatingIP'
op|','
nl|'\n'
name|'db_floatingips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'ips'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'floating_ip_bulk_destroy'
op|'('
name|'context'
op|','
name|'ips'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
