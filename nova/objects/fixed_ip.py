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
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'network'
name|'as'
name|'network_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FIXED_IP_OPTIONAL_ATTRS
name|'FIXED_IP_OPTIONAL_ATTRS'
op|'='
op|'['
string|"'instance'"
op|','
string|"'network'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIP
name|'class'
name|'FixedIP'
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
name|'IPV4Address'
op|'('
op|')'
op|','
nl|'\n'
string|"'network_id'"
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
string|"'virtual_interface_id'"
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
string|"'instance_uuid'"
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
string|"'allocated'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'leased'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'reserved'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
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
string|"'instance'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'Instance'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'Network'"
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
name|'property'
newline|'\n'
DECL|member|floating_ips
name|'def'
name|'floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): avoid circular import'
nl|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'floating_ip'
newline|'\n'
name|'return'
name|'floating_ip'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_by_fixed_ip_id'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'id'
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
name|'fixedip'
op|','
name|'db_fixedip'
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
name|'fixedip'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'not'
name|'in'
name|'FIXED_IP_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'                '
name|'fixedip'
op|'['
name|'field'
op|']'
op|'='
name|'db_fixedip'
op|'['
name|'field'
op|']'
newline|'\n'
comment|'# NOTE(danms): Instance could be deleted, and thus None'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'instance'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'fixedip'
op|'.'
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'instance_obj'
op|'.'
name|'Instance'
op|'('
op|')'
op|','
nl|'\n'
name|'db_fixedip'
op|'['
string|"'instance'"
op|']'
op|')'
name|'if'
name|'db_fixedip'
op|'['
string|"'instance'"
op|']'
name|'else'
name|'None'
newline|'\n'
dedent|''
name|'if'
string|"'network'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'fixedip'
op|'.'
name|'network'
op|'='
name|'network_obj'
op|'.'
name|'Network'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'network_obj'
op|'.'
name|'Network'
op|'('
op|')'
op|','
name|'db_fixedip'
op|'['
string|"'network'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'fixedip'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'fixedip'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'fixedip'
newline|'\n'
nl|'\n'
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
name|'get_network'
op|'='
string|"'network'"
name|'in'
name|'expected_attrs'
newline|'\n'
name|'db_fixedip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'get_network'
op|'='
name|'get_network'
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
name|'db_fixedip'
op|','
name|'expected_attrs'
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
name|'db_fixedip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'str'
op|'('
name|'address'
op|')'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'expected_attrs'
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
name|'db_fixedip'
op|','
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_floating_address
name|'def'
name|'get_by_floating_address'
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
name|'db_fixedip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_floating_address'
op|'('
name|'context'
op|','
name|'address'
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
name|'db_fixedip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_network_and_host
name|'def'
name|'get_by_network_and_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network_id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixedip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_network_host'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'host'
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
name|'db_fixedip'
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
name|'address'
op|','
name|'instance_uuid'
op|','
name|'network_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'reserved'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixedip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_associate'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'network_id'
op|'='
name|'network_id'
op|','
nl|'\n'
name|'reserved'
op|'='
name|'reserved'
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
name|'db_fixedip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|associate_pool
name|'def'
name|'associate_pool'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network_id'
op|','
name|'instance_uuid'
op|'='
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixedip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_associate_pool'
op|'('
name|'context'
op|','
name|'network_id'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
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
name|'db_fixedip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|disassociate_by_address
name|'def'
name|'disassociate_by_address'
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
name|'fixed_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|_disassociate_all_by_timeout
name|'def'
name|'_disassociate_all_by_timeout'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'time_str'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'time'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'time_str'
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'fixed_ip_disassociate_all_by_timeout'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'time'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|disassociate_all_by_timeout
name|'def'
name|'disassociate_all_by_timeout'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'time'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'_disassociate_all_by_timeout'
op|'('
name|'context'
op|','
name|'host'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'time'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
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
string|"'id'"
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
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'address'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'address'"
op|']'
op|'='
name|'str'
op|'('
name|'updates'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'db_fixedip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_create'
op|'('
name|'context'
op|','
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
name|'db_fixedip'
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
name|'db'
op|'.'
name|'fixed_ip_update'
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
name|'updates'
op|')'
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
name|'obj_base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|disassociate
name|'def'
name|'disassociate'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'fixed_ip_disassociate'
op|'('
name|'context'
op|','
name|'str'
op|'('
name|'self'
op|'.'
name|'address'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'instance_uuid'"
op|','
string|"'instance'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIPList
dedent|''
dedent|''
name|'class'
name|'FixedIPList'
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
comment|'# Version 1.0: Initial version'
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
string|"'FixedIP'"
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
op|'}'
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
name|'db_fixedips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_all'
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
op|')'
op|','
name|'FixedIP'
op|','
name|'db_fixedips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
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
name|'db_fixedips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_instance'
op|'('
name|'context'
op|','
name|'instance_uuid'
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
name|'FixedIP'
op|','
name|'db_fixedips'
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
name|'db_fixedips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_host'
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
op|')'
op|','
name|'FixedIP'
op|','
name|'db_fixedips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_virtual_interface_id
name|'def'
name|'get_by_virtual_interface_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'vif_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixedips'
op|'='
name|'db'
op|'.'
name|'fixed_ips_by_virtual_interface'
op|'('
name|'context'
op|','
name|'vif_id'
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
name|'FixedIP'
op|','
name|'db_fixedips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|bulk_create
name|'def'
name|'bulk_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_ips'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'fixedip'
name|'in'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'='
name|'obj_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'fixedip'
op|')'
newline|'\n'
name|'if'
string|"'id'"
name|'in'
name|'ip'
op|':'
newline|'\n'
indent|'                '
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
name|'ips'
op|'.'
name|'append'
op|'('
name|'ip'
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'fixed_ip_bulk_create'
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
