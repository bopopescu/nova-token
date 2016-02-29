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
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'uuidutils'
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
name|'instance_mapping'
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
name|'test_cell_mapping'
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
nl|'\n'
nl|'\n'
DECL|function|get_db_mapping
name|'def'
name|'get_db_mapping'
op|'('
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'db_mapping'
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
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
op|','
nl|'\n'
string|"'cell_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake-project'"
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
newline|'\n'
name|'db_mapping'
op|'['
string|'"cell_mapping"'
op|']'
op|'='
name|'test_cell_mapping'
op|'.'
name|'get_db_mapping'
op|'('
name|'id'
op|'='
number|'42'
op|')'
newline|'\n'
name|'db_mapping'
op|'['
string|"'cell_id'"
op|']'
op|'='
name|'db_mapping'
op|'['
string|'"cell_mapping"'
op|']'
op|'['
string|'"id"'
op|']'
newline|'\n'
name|'db_mapping'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'return'
name|'db_mapping'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceMappingObject
dedent|''
name|'class'
name|'_TestInstanceMappingObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_check_cell_map_value
indent|'    '
name|'def'
name|'_check_cell_map_value'
op|'('
name|'self'
op|','
name|'db_val'
op|','
name|'cell_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'db_val'
op|','
name|'cell_obj'
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
name|'instance_mapping'
op|'.'
name|'InstanceMapping'
op|','
nl|'\n'
string|"'_get_by_instance_uuid_from_db'"
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid
name|'def'
name|'test_get_by_instance_uuid'
op|'('
name|'self'
op|','
name|'uuid_from_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mapping'
op|'='
name|'get_db_mapping'
op|'('
op|')'
newline|'\n'
name|'uuid_from_db'
op|'.'
name|'return_value'
op|'='
name|'db_mapping'
newline|'\n'
nl|'\n'
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMapping'
op|'('
op|')'
op|'.'
name|'get_by_instance_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
name|'uuid_from_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mapping_obj'
op|','
name|'db_mapping'
op|','
nl|'\n'
name|'subs'
op|'='
op|'{'
string|"'cell_mapping'"
op|':'
string|"'cell_id'"
op|'}'
op|','
nl|'\n'
name|'comparators'
op|'='
op|'{'
nl|'\n'
string|"'cell_mapping'"
op|':'
name|'self'
op|'.'
name|'_check_cell_map_value'
op|'}'
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
name|'instance_mapping'
op|'.'
name|'InstanceMapping'
op|','
nl|'\n'
string|"'_get_by_instance_uuid_from_db'"
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid_cell_mapping_none
name|'def'
name|'test_get_by_instance_uuid_cell_mapping_none'
op|'('
name|'self'
op|','
name|'uuid_from_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mapping'
op|'='
name|'get_db_mapping'
op|'('
name|'cell_mapping'
op|'='
name|'None'
op|','
name|'cell_id'
op|'='
name|'None'
op|')'
newline|'\n'
name|'uuid_from_db'
op|'.'
name|'return_value'
op|'='
name|'db_mapping'
newline|'\n'
nl|'\n'
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMapping'
op|'('
op|')'
op|'.'
name|'get_by_instance_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
name|'uuid_from_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mapping_obj'
op|','
name|'db_mapping'
op|','
nl|'\n'
name|'subs'
op|'='
op|'{'
string|"'cell_mapping'"
op|':'
string|"'cell_id'"
op|'}'
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
name|'instance_mapping'
op|'.'
name|'InstanceMapping'
op|','
string|"'_create_in_db'"
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'create_in_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mapping'
op|'='
name|'get_db_mapping'
op|'('
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
name|'create_in_db'
op|'.'
name|'return_value'
op|'='
name|'db_mapping'
newline|'\n'
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMapping'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'instance_uuid'
op|'='
name|'uuid'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'cell_mapping'
op|'='
name|'objects'
op|'.'
name|'CellMapping'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'id'
op|'='
name|'db_mapping'
op|'['
string|"'cell_mapping'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'project_id'
op|'='
name|'db_mapping'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
nl|'\n'
name|'mapping_obj'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'create_in_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'instance_uuid'"
op|':'
name|'uuid'
op|','
nl|'\n'
string|"'cell_id'"
op|':'
name|'db_mapping'
op|'['
string|"'cell_mapping'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'db_mapping'
op|'['
string|"'project_id'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mapping_obj'
op|','
name|'db_mapping'
op|','
nl|'\n'
name|'subs'
op|'='
op|'{'
string|"'cell_mapping'"
op|':'
string|"'cell_id'"
op|'}'
op|','
nl|'\n'
name|'comparators'
op|'='
op|'{'
nl|'\n'
string|"'cell_mapping'"
op|':'
name|'self'
op|'.'
name|'_check_cell_map_value'
op|'}'
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
name|'instance_mapping'
op|'.'
name|'InstanceMapping'
op|','
string|"'_create_in_db'"
op|')'
newline|'\n'
DECL|member|test_create_cell_mapping_none
name|'def'
name|'test_create_cell_mapping_none'
op|'('
name|'self'
op|','
name|'create_in_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mapping'
op|'='
name|'get_db_mapping'
op|'('
name|'cell_mapping'
op|'='
name|'None'
op|','
name|'cell_id'
op|'='
name|'None'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
name|'create_in_db'
op|'.'
name|'return_value'
op|'='
name|'db_mapping'
newline|'\n'
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMapping'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'instance_uuid'
op|'='
name|'uuid'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'cell_mapping'
op|'='
name|'None'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'project_id'
op|'='
name|'db_mapping'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
nl|'\n'
name|'mapping_obj'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'create_in_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'instance_uuid'"
op|':'
name|'uuid'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'db_mapping'
op|'['
string|"'project_id'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mapping_obj'
op|','
name|'db_mapping'
op|','
nl|'\n'
name|'subs'
op|'='
op|'{'
string|"'cell_mapping'"
op|':'
string|"'cell_id'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'mapping_obj'
op|'.'
name|'cell_mapping'
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
name|'instance_mapping'
op|'.'
name|'InstanceMapping'
op|','
string|"'_save_in_db'"
op|')'
newline|'\n'
DECL|member|test_save
name|'def'
name|'test_save'
op|'('
name|'self'
op|','
name|'save_in_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mapping'
op|'='
name|'get_db_mapping'
op|'('
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
name|'save_in_db'
op|'.'
name|'return_value'
op|'='
name|'db_mapping'
newline|'\n'
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMapping'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'instance_uuid'
op|'='
name|'uuid'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'cell_mapping'
op|'='
name|'objects'
op|'.'
name|'CellMapping'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'id'
op|'='
number|'42'
op|')'
newline|'\n'
nl|'\n'
name|'mapping_obj'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'save_in_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_mapping'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'cell_id'"
op|':'
name|'mapping_obj'
op|'.'
name|'cell_mapping'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'uuid'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mapping_obj'
op|','
name|'db_mapping'
op|','
nl|'\n'
name|'subs'
op|'='
op|'{'
string|"'cell_mapping'"
op|':'
string|"'cell_id'"
op|'}'
op|','
nl|'\n'
name|'comparators'
op|'='
op|'{'
nl|'\n'
string|"'cell_mapping'"
op|':'
name|'self'
op|'.'
name|'_check_cell_map_value'
op|'}'
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
name|'instance_mapping'
op|'.'
name|'InstanceMapping'
op|','
string|"'_destroy_in_db'"
op|')'
newline|'\n'
DECL|member|test_destroy
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|','
name|'destroy_in_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMapping'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'mapping_obj'
op|'.'
name|'instance_uuid'
op|'='
name|'uuid'
newline|'\n'
nl|'\n'
name|'mapping_obj'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'destroy_in_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cell_mapping_nullable
dedent|''
name|'def'
name|'test_cell_mapping_nullable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMapping'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
comment|"# Just ensure this doesn't raise an exception"
nl|'\n'
name|'mapping_obj'
op|'.'
name|'cell_mapping'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceMappingObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceMappingObject
name|'_TestInstanceMappingObject'
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
name|'TestRemoteInstanceMappingObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceMappingObject
name|'_TestInstanceMappingObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceMappingListObject
dedent|''
name|'class'
name|'_TestInstanceMappingListObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_check_cell_map_value
indent|'    '
name|'def'
name|'_check_cell_map_value'
op|'('
name|'self'
op|','
name|'db_val'
op|','
name|'cell_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'db_val'
op|','
name|'cell_obj'
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
name|'instance_mapping'
op|'.'
name|'InstanceMappingList'
op|','
nl|'\n'
string|"'_get_by_project_id_from_db'"
op|')'
newline|'\n'
DECL|member|test_get_by_project_id
name|'def'
name|'test_get_by_project_id'
op|'('
name|'self'
op|','
name|'project_id_from_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mapping'
op|'='
name|'get_db_mapping'
op|'('
op|')'
newline|'\n'
name|'project_id_from_db'
op|'.'
name|'return_value'
op|'='
op|'['
name|'db_mapping'
op|']'
newline|'\n'
nl|'\n'
name|'mapping_obj'
op|'='
name|'objects'
op|'.'
name|'InstanceMappingList'
op|'('
op|')'
op|'.'
name|'get_by_project_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'db_mapping'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'project_id_from_db'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_mapping'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'mapping_obj'
op|'.'
name|'objects'
op|'['
number|'0'
op|']'
op|','
name|'db_mapping'
op|','
nl|'\n'
name|'subs'
op|'='
op|'{'
string|"'cell_mapping'"
op|':'
string|"'cell_id'"
op|'}'
op|','
nl|'\n'
name|'comparators'
op|'='
op|'{'
nl|'\n'
string|"'cell_mapping'"
op|':'
name|'self'
op|'.'
name|'_check_cell_map_value'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceMappingListObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceMappingListObject
name|'_TestInstanceMappingListObject'
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
name|'TestRemoteInstanceMappingListObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceMappingListObject
name|'_TestInstanceMappingListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
