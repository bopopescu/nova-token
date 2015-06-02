begin_unit
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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'InstancePCIRequest'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|InstancePCIRequest
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Add request_id'
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
string|"'count'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'spec'"
op|':'
name|'fields'
op|'.'
name|'ListOfDictOfNullableStringsField'
op|'('
op|')'
op|','
nl|'\n'
string|"'alias_name'"
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
comment|'# A stashed request related to a resize, not current'
nl|'\n'
string|"'is_new'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'request_id'"
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
op|'}'
newline|'\n'
nl|'\n'
DECL|member|obj_load_attr
name|'def'
name|'obj_load_attr'
op|'('
name|'self'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'setattr'
op|'('
name|'self'
op|','
name|'attr'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(danms): The dict that this object replaces uses a key of 'new'"
nl|'\n'
comment|"# so we translate it here to our more appropropriately-named 'is_new'."
nl|'\n'
comment|'# This is not something that affects the obect version, so we could'
nl|'\n'
comment|'# remove this later when all dependent code is fixed.'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|new
name|'def'
name|'new'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'is_new'
newline|'\n'
nl|'\n'
DECL|member|obj_make_compatible
dedent|''
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
number|'1'
op|')'
name|'and'
string|"'request_id'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'primitive'
op|'['
string|"'request_id'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
name|'class'
name|'InstancePCIRequests'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|InstancePCIRequests
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: InstancePCIRequest 1.1'
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
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'requests'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'InstancePCIRequest'"
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
string|"'requests'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|','
op|'('
string|"'1.1'"
op|','
string|"'1.1'"
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
number|'1'
op|')'
name|'and'
string|"'requests'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'index'
op|','
name|'request'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'requests'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'request'
op|'.'
name|'obj_make_compatible'
op|'('
nl|'\n'
name|'primitive'
op|'['
string|"'requests'"
op|']'
op|'['
name|'index'
op|']'
op|'['
string|"'nova_object.data'"
op|']'
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'primitive'
op|'['
string|"'requests'"
op|']'
op|'['
name|'index'
op|']'
op|'['
string|"'nova_object.version'"
op|']'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_from_db
name|'def'
name|'obj_from_db'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'db_requests'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'='
name|'cls'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'requests'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
name|'if'
name|'db_requests'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'requests'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'db_requests'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'requests'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'request_obj'
op|'='
name|'InstancePCIRequest'
op|'('
nl|'\n'
name|'count'
op|'='
name|'request'
op|'['
string|"'count'"
op|']'
op|','
name|'spec'
op|'='
name|'request'
op|'['
string|"'spec'"
op|']'
op|','
nl|'\n'
name|'alias_name'
op|'='
name|'request'
op|'['
string|"'alias_name'"
op|']'
op|','
name|'is_new'
op|'='
name|'request'
op|'['
string|"'is_new'"
op|']'
op|','
nl|'\n'
name|'request_id'
op|'='
name|'request'
op|'['
string|"'request_id'"
op|']'
op|')'
newline|'\n'
name|'request_obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'requests'
op|'.'
name|'append'
op|'('
name|'request_obj'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
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
name|'db_pci_requests'
op|'='
name|'db'
op|'.'
name|'instance_extra_get_by_instance_uuid'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuid'
op|','
name|'columns'
op|'='
op|'['
string|"'pci_requests'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'db_pci_requests'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'db_pci_requests'
op|'='
name|'db_pci_requests'
op|'['
string|"'pci_requests'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'obj_from_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'db_pci_requests'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid_and_newness
name|'def'
name|'get_by_instance_uuid_and_newness'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'is_new'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'requests'
op|'='
name|'cls'
op|'.'
name|'get_by_instance_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'requests'
op|'.'
name|'requests'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'requests'
op|'.'
name|'requests'
nl|'\n'
name|'if'
name|'x'
op|'.'
name|'new'
op|'=='
name|'is_new'
op|']'
newline|'\n'
name|'return'
name|'requests'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_load_legacy_requests
name|'def'
name|'_load_legacy_requests'
op|'('
name|'sysmeta_value'
op|','
name|'is_new'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'sysmeta_value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'requests'
op|'='
op|'['
op|']'
newline|'\n'
name|'db_requests'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'sysmeta_value'
op|')'
newline|'\n'
name|'for'
name|'db_request'
name|'in'
name|'db_requests'
op|':'
newline|'\n'
indent|'            '
name|'request'
op|'='
name|'InstancePCIRequest'
op|'('
nl|'\n'
name|'count'
op|'='
name|'db_request'
op|'['
string|"'count'"
op|']'
op|','
name|'spec'
op|'='
name|'db_request'
op|'['
string|"'spec'"
op|']'
op|','
nl|'\n'
name|'alias_name'
op|'='
name|'db_request'
op|'['
string|"'alias_name'"
op|']'
op|','
name|'is_new'
op|'='
name|'is_new'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'requests'
op|'.'
name|'append'
op|'('
name|'request'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'requests'
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
comment|'# NOTE (baoli): not all callers are passing instance as object yet.'
nl|'\n'
comment|'# Therefore, use the dict syntax in this routine'
nl|'\n'
indent|'        '
name|'if'
string|"'pci_requests'"
name|'in'
name|'instance'
op|'['
string|"'system_metadata'"
op|']'
op|':'
newline|'\n'
comment|"# NOTE(danms): This instance hasn't been converted to use"
nl|'\n'
comment|'# instance_extra yet, so extract the data from sysmeta'
nl|'\n'
indent|'            '
name|'sysmeta'
op|'='
name|'instance'
op|'['
string|"'system_metadata'"
op|']'
newline|'\n'
name|'_requests'
op|'='
op|'('
nl|'\n'
name|'cls'
op|'.'
name|'_load_legacy_requests'
op|'('
name|'sysmeta'
op|'['
string|"'pci_requests'"
op|']'
op|')'
op|'+'
nl|'\n'
name|'cls'
op|'.'
name|'_load_legacy_requests'
op|'('
name|'sysmeta'
op|'.'
name|'get'
op|'('
string|"'new_pci_requests'"
op|')'
op|','
nl|'\n'
name|'is_new'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
name|'requests'
op|'='
name|'cls'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'requests'
op|'='
name|'_requests'
op|')'
newline|'\n'
name|'requests'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'requests'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'get_by_instance_uuid'
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
DECL|member|to_json
dedent|''
dedent|''
name|'def'
name|'to_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'blob'
op|'='
op|'['
op|'{'
string|"'count'"
op|':'
name|'x'
op|'.'
name|'count'
op|','
nl|'\n'
string|"'spec'"
op|':'
name|'x'
op|'.'
name|'spec'
op|','
nl|'\n'
string|"'alias_name'"
op|':'
name|'x'
op|'.'
name|'alias_name'
op|','
nl|'\n'
string|"'is_new'"
op|':'
name|'x'
op|'.'
name|'is_new'
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'x'
op|'.'
name|'request_id'
op|'}'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'requests'
op|']'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'blob'
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
name|'blob'
op|'='
name|'self'
op|'.'
name|'to_json'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_extra_update_by_uuid'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
op|'{'
string|"'pci_requests'"
op|':'
name|'blob'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_request_spec_instance_props
name|'def'
name|'from_request_spec_instance_props'
op|'('
name|'cls'
op|','
name|'pci_requests'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'objs'
op|'='
op|'['
name|'InstancePCIRequest'
op|'('
op|'**'
name|'request'
op|')'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'pci_requests'
op|'['
string|"'requests'"
op|']'
op|']'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'requests'
op|'='
name|'objs'
op|','
name|'instance_uuid'
op|'='
name|'pci_requests'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
