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
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'opts'
name|'as'
name|'cells_opts'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'rpcapi'
name|'as'
name|'cells_rpcapi'
newline|'\n'
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
name|'i18n'
name|'import'
name|'_LE'
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
nl|'\n'
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
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
name|'class'
name|'InstanceFault'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|InstanceFault
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: String attributes updated to support unicode'
nl|'\n'
comment|'# Version 1.2: Added create()'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
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
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'code'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'message'"
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
string|"'details'"
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
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'fault'
op|','
name|'db_fault'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): These are identical right now'
nl|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'fault'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'fault'
op|'['
name|'key'
op|']'
op|'='
name|'db_fault'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'fault'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'fault'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'fault'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_latest_for_instance
name|'def'
name|'get_latest_for_instance'
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
name|'db_faults'
op|'='
name|'db'
op|'.'
name|'instance_fault_get_by_instance_uuids'
op|'('
name|'context'
op|','
nl|'\n'
op|'['
name|'instance_uuid'
op|']'
op|')'
newline|'\n'
name|'if'
name|'instance_uuid'
name|'in'
name|'db_faults'
name|'and'
name|'db_faults'
op|'['
name|'instance_uuid'
op|']'
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
op|')'
op|','
nl|'\n'
name|'db_faults'
op|'['
name|'instance_uuid'
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
op|','
name|'context'
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
name|'values'
op|'='
op|'{'
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
string|"'code'"
op|':'
name|'self'
op|'.'
name|'code'
op|','
nl|'\n'
string|"'message'"
op|':'
name|'self'
op|'.'
name|'message'
op|','
nl|'\n'
string|"'details'"
op|':'
name|'self'
op|'.'
name|'details'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'db_fault'
op|'='
name|'db'
op|'.'
name|'instance_fault_create'
op|'('
name|'context'
op|','
name|'values'
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
name|'db_fault'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
comment|'# Cells should only try sending a message over to nova-cells'
nl|'\n'
comment|"# if cells is enabled and we're not the API cell. Otherwise,"
nl|'\n'
comment|'# if the API cell is calling this, we could end up with'
nl|'\n'
comment|'# infinite recursion.'
nl|'\n'
name|'if'
name|'cells_opts'
op|'.'
name|'get_cell_type'
op|'('
op|')'
op|'=='
string|"'compute'"
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|'('
op|')'
op|'.'
name|'instance_fault_create_at_top'
op|'('
nl|'\n'
name|'context'
op|','
name|'db_fault'
op|')'
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
name|'_LE'
op|'('
string|'"Failed to notify cells of instance fault"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceFaultList
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'InstanceFaultList'
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
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'#              InstanceFault <= version 1.1'
nl|'\n'
comment|'# Version 1.1: InstanceFault version 1.2'
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
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'InstanceFault'"
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
string|"'1.1'"
op|','
nl|'\n'
comment|'# NOTE(danms): InstanceFault was at 1.1 before we added this'
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.2'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuids
name|'def'
name|'get_by_instance_uuids'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_faultdict'
op|'='
name|'db'
op|'.'
name|'instance_fault_get_by_instance_uuids'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuids'
op|')'
newline|'\n'
name|'db_faultlist'
op|'='
name|'itertools'
op|'.'
name|'chain'
op|'('
op|'*'
name|'db_faultdict'
op|'.'
name|'values'
op|'('
op|')'
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
name|'objects'
op|'.'
name|'InstanceFault'
op|','
nl|'\n'
name|'db_faultlist'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
