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
name|'oslo_utils'
name|'import'
name|'timeutils'
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
nl|'\n'
DECL|variable|FIXED_IP_OPTIONAL_ATTRS
name|'FIXED_IP_OPTIONAL_ATTRS'
op|'='
op|'['
string|"'instance'"
op|','
string|"'network'"
op|','
string|"'virtual_interface'"
op|','
nl|'\n'
string|"'floating_ips'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
op|'@'
name|'obj_base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
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
op|','
nl|'\n'
DECL|class|FixedIP
name|'obj_base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added virtual_interface field'
nl|'\n'
comment|'# Version 1.2: Instance version 1.14'
nl|'\n'
comment|'# Version 1.3: Instance 1.15'
nl|'\n'
comment|'# Version 1.4: Added default_route field'
nl|'\n'
comment|'# Version 1.5: Added floating_ips field'
nl|'\n'
comment|'# Version 1.6: Instance 1.16'
nl|'\n'
comment|'# Version 1.7: Instance 1.17'
nl|'\n'
comment|'# Version 1.8: Instance 1.18'
nl|'\n'
comment|'# Version 1.9: Instance 1.19'
nl|'\n'
comment|'# Version 1.10: Instance 1.20'
nl|'\n'
comment|'# Version 1.11: Instance 1.21'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.11'"
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
name|'IPV4AndV6AddressField'
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
string|"'default_route'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
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
string|"'virtual_interface'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'VirtualInterface'"
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
comment|'# NOTE(danms): This should not ever be made lazy-loadable'
nl|'\n'
comment|'# because it would create a bit of a loop between FixedIP'
nl|'\n'
comment|'# and FloatingIP'
nl|'\n'
string|"'floating_ips'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'FloatingIPList'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'instance'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.13'"
op|')'
op|','
op|'('
string|"'1.2'"
op|','
string|"'1.14'"
op|')'
op|','
op|'('
string|"'1.3'"
op|','
string|"'1.15'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.6'"
op|','
string|"'1.16'"
op|')'
op|','
op|'('
string|"'1.7'"
op|','
string|"'1.17'"
op|')'
op|','
op|'('
string|"'1.8'"
op|','
string|"'1.18'"
op|')'
op|','
nl|'\n'
op|'('
string|"'1.9'"
op|','
string|"'1.19'"
op|')'
op|','
op|'('
string|"'1.10'"
op|','
string|"'1.20'"
op|')'
op|','
op|'('
string|"'1.11'"
op|','
string|"'1.21'"
op|')'
op|']'
op|','
nl|'\n'
string|"'network'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.2'"
op|')'
op|']'
op|','
nl|'\n'
string|"'virtual_interface'"
op|':'
op|'['
op|'('
string|"'1.1'"
op|','
string|"'1.0'"
op|')'
op|']'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
op|'('
string|"'1.5'"
op|','
string|"'1.7'"
op|')'
op|']'
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
name|'super'
op|'('
name|'FixedIP'
op|','
name|'self'
op|')'
op|'.'
name|'obj_make_compatible'
op|'('
name|'primitive'
op|','
name|'target_version'
op|')'
newline|'\n'
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
number|'4'
op|')'
name|'and'
string|"'default_route'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'default_route'"
op|']'
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
op|'=='
string|"'default_route'"
op|':'
newline|'\n'
comment|'# NOTE(danms): This field is only set when doing a'
nl|'\n'
comment|"# FixedIPList.get_by_network() because it's a relatively"
nl|'\n'
comment|'# special-case thing, so skip it here'
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
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
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
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
name|'objects'
op|'.'
name|'Network'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Network'
op|'('
name|'context'
op|')'
op|','
nl|'\n'
name|'db_fixedip'
op|'['
string|"'network'"
op|']'
op|')'
name|'if'
name|'db_fixedip'
op|'['
string|"'network'"
op|']'
name|'else'
name|'None'
newline|'\n'
dedent|''
name|'if'
string|"'virtual_interface'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'db_vif'
op|'='
name|'db_fixedip'
op|'['
string|"'virtual_interface'"
op|']'
newline|'\n'
name|'vif'
op|'='
name|'objects'
op|'.'
name|'VirtualInterface'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'VirtualInterface'
op|'('
name|'context'
op|')'
op|','
nl|'\n'
name|'db_fixedip'
op|'['
string|"'virtual_interface'"
op|']'
op|')'
name|'if'
name|'db_vif'
name|'else'
name|'None'
newline|'\n'
name|'fixedip'
op|'.'
name|'virtual_interface'
op|'='
name|'vif'
newline|'\n'
dedent|''
name|'if'
string|"'floating_ips'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'fixedip'
op|'.'
name|'floating_ips'
op|'='
name|'obj_base'
op|'.'
name|'obj_make_list'
op|'('
nl|'\n'
name|'context'
op|','
name|'objects'
op|'.'
name|'FloatingIPList'
op|'('
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'FloatingIP'
op|','
name|'db_fixedip'
op|'['
string|"'floating_ips'"
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
name|'context'
op|')'
op|','
name|'db_fixedip'
op|','
nl|'\n'
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
name|'context'
op|')'
op|','
name|'db_fixedip'
op|','
nl|'\n'
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
name|'str'
op|'('
name|'address'
op|')'
op|')'
newline|'\n'
name|'if'
name|'db_fixedip'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
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
name|'db_fixedip'
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
name|'context'
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
name|'context'
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
name|'context'
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
name|'self'
op|'.'
name|'_context'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'fixed_ip_disassociate'
op|'('
name|'self'
op|'.'
name|'_context'
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
dedent|''
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|FixedIPList
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
comment|'# Version 1.1: Added get_by_network()'
nl|'\n'
comment|'# Version 1.2: FixedIP <= version 1.2'
nl|'\n'
comment|'# Version 1.3: FixedIP <= version 1.3'
nl|'\n'
comment|'# Version 1.4: FixedIP <= version 1.4'
nl|'\n'
comment|'# Version 1.5: FixedIP <= version 1.5, added expected attrs to gets'
nl|'\n'
comment|'# Version 1.6: FixedIP <= version 1.6'
nl|'\n'
comment|'# Version 1.7: FixedIP <= version 1.7'
nl|'\n'
comment|'# Version 1.8: FixedIP <= version 1.8'
nl|'\n'
comment|'# Version 1.9: FixedIP <= version 1.9'
nl|'\n'
comment|'# Version 1.10: FixedIP <= version 1.10'
nl|'\n'
comment|'# Version 1.11: FixedIP <= version 1.11'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.11'"
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
string|"'1.1'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'1.2'"
op|':'
string|"'1.2'"
op|','
nl|'\n'
string|"'1.3'"
op|':'
string|"'1.3'"
op|','
nl|'\n'
string|"'1.4'"
op|':'
string|"'1.4'"
op|','
nl|'\n'
string|"'1.5'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'1.6'"
op|':'
string|"'1.6'"
op|','
nl|'\n'
string|"'1.7'"
op|':'
string|"'1.7'"
op|','
nl|'\n'
string|"'1.8'"
op|':'
string|"'1.8'"
op|','
nl|'\n'
string|"'1.9'"
op|':'
string|"'1.9'"
op|','
nl|'\n'
string|"'1.10'"
op|':'
string|"'1.10'"
op|','
nl|'\n'
string|"'1.11'"
op|':'
string|"'1.11'"
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
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
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
name|'expected_attrs'
op|'='
op|'['
string|"'network'"
op|','
string|"'virtual_interface'"
op|','
string|"'floating_ips'"
op|']'
newline|'\n'
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
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'FixedIP'
op|','
name|'db_fixedips'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
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
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
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
name|'expected_attrs'
op|'='
op|'['
string|"'network'"
op|','
string|"'floating_ips'"
op|']'
newline|'\n'
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
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'FixedIP'
op|','
name|'db_fixedips'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
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
DECL|member|get_by_network
name|'def'
name|'get_by_network'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ipinfo'
op|'='
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'context'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ipinfo'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'fips'
op|'='
name|'cls'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'objects'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'info'
name|'in'
name|'ipinfo'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'info'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
name|'hostname'
op|'='
name|'info'
op|'['
string|"'instance_hostname'"
op|']'
op|','
nl|'\n'
name|'created_at'
op|'='
name|'info'
op|'['
string|"'instance_created'"
op|']'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'info'
op|'['
string|"'instance_updated'"
op|']'
op|')'
newline|'\n'
name|'vif'
op|'='
name|'objects'
op|'.'
name|'VirtualInterface'
op|'('
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'id'
op|'='
name|'info'
op|'['
string|"'vif_id'"
op|']'
op|','
nl|'\n'
name|'address'
op|'='
name|'info'
op|'['
string|"'vif_address'"
op|']'
op|')'
newline|'\n'
name|'fip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'('
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'address'
op|'='
name|'info'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'info'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
name|'network_id'
op|'='
name|'info'
op|'['
string|"'network_id'"
op|']'
op|','
nl|'\n'
name|'virtual_interface_id'
op|'='
name|'info'
op|'['
string|"'vif_id'"
op|']'
op|','
nl|'\n'
name|'allocated'
op|'='
name|'info'
op|'['
string|"'allocated'"
op|']'
op|','
nl|'\n'
name|'leased'
op|'='
name|'info'
op|'['
string|"'leased'"
op|']'
op|','
nl|'\n'
name|'default_route'
op|'='
name|'info'
op|'['
string|"'default_route'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'='
name|'inst'
op|','
nl|'\n'
name|'virtual_interface'
op|'='
name|'vif'
op|')'
newline|'\n'
name|'fips'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'fip'
op|')'
newline|'\n'
dedent|''
name|'fips'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'fips'
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
