begin_unit
comment|'# Copyright (C) 2014, Red Hat, Inc.'
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
name|'ec2'
name|'as'
name|'ec2_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_map
name|'fake_map'
op|'='
op|'{'
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
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake-uuid-2'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestEC2InstanceMapping
name|'class'
name|'_TestEC2InstanceMapping'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_compare
name|'def'
name|'_compare'
op|'('
name|'test'
op|','
name|'db'
op|','
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
op|','
name|'value'
name|'in'
name|'db'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'test'
op|'.'
name|'assertEqual'
op|'('
name|'db'
op|'['
name|'field'
op|']'
op|','
name|'obj'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'imap'
op|'='
name|'ec2_obj'
op|'.'
name|'EC2InstanceMapping'
op|'('
op|')'
newline|'\n'
name|'imap'
op|'.'
name|'uuid'
op|'='
string|"'fake-uuid-2'"
newline|'\n'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'ec2_instance_create'"
op|')'
name|'as'
name|'create'
op|':'
newline|'\n'
indent|'            '
name|'create'
op|'.'
name|'return_value'
op|'='
name|'fake_map'
newline|'\n'
name|'imap'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'imap'
op|'.'
name|'_context'
op|')'
newline|'\n'
name|'imap'
op|'.'
name|'_context'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'fake_map'
op|','
name|'imap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_uuid
dedent|''
name|'def'
name|'test_get_by_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'ec2_instance_get_by_uuid'"
op|')'
name|'as'
name|'get'
op|':'
newline|'\n'
indent|'            '
name|'get'
op|'.'
name|'return_value'
op|'='
name|'fake_map'
newline|'\n'
name|'imap'
op|'='
name|'ec2_obj'
op|'.'
name|'EC2InstanceMapping'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'fake-uuid-2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'fake_map'
op|','
name|'imap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_ec2_id
dedent|''
dedent|''
name|'def'
name|'test_get_by_ec2_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'ec2_instance_get_by_id'"
op|')'
name|'as'
name|'get'
op|':'
newline|'\n'
indent|'            '
name|'get'
op|'.'
name|'return_value'
op|'='
name|'fake_map'
newline|'\n'
name|'imap'
op|'='
name|'ec2_obj'
op|'.'
name|'EC2InstanceMapping'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'fake_map'
op|','
name|'imap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestEC2InstanceMapping
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestEC2InstanceMapping'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
name|'_TestEC2InstanceMapping'
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
name|'TestRemoteEC2InstanceMapping'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteEC2InstanceMapping
name|'_TestEC2InstanceMapping'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestVolumeMapping
dedent|''
name|'class'
name|'_TestVolumeMapping'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_compare
name|'def'
name|'_compare'
op|'('
name|'test'
op|','
name|'db'
op|','
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
op|','
name|'value'
name|'in'
name|'db'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'test'
op|'.'
name|'assertEqual'
op|'('
name|'db'
op|'['
name|'field'
op|']'
op|','
name|'obj'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmap'
op|'='
name|'ec2_obj'
op|'.'
name|'VolumeMapping'
op|'('
op|')'
newline|'\n'
name|'vmap'
op|'.'
name|'uuid'
op|'='
string|"'fake-uuid-2'"
newline|'\n'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'ec2_volume_create'"
op|')'
name|'as'
name|'create'
op|':'
newline|'\n'
indent|'            '
name|'create'
op|'.'
name|'return_value'
op|'='
name|'fake_map'
newline|'\n'
name|'vmap'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vmap'
op|'.'
name|'_context'
op|')'
newline|'\n'
name|'vmap'
op|'.'
name|'_context'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'fake_map'
op|','
name|'vmap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_uuid
dedent|''
name|'def'
name|'test_get_by_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'ec2_volume_get_by_uuid'"
op|')'
name|'as'
name|'get'
op|':'
newline|'\n'
indent|'            '
name|'get'
op|'.'
name|'return_value'
op|'='
name|'fake_map'
newline|'\n'
name|'vmap'
op|'='
name|'ec2_obj'
op|'.'
name|'VolumeMapping'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'fake-uuid-2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'fake_map'
op|','
name|'vmap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_ec2_id
dedent|''
dedent|''
name|'def'
name|'test_get_by_ec2_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'ec2_volume_get_by_id'"
op|')'
name|'as'
name|'get'
op|':'
newline|'\n'
indent|'            '
name|'get'
op|'.'
name|'return_value'
op|'='
name|'fake_map'
newline|'\n'
name|'vmap'
op|'='
name|'ec2_obj'
op|'.'
name|'VolumeMapping'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'fake_map'
op|','
name|'vmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestVolumeMapping
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestVolumeMapping'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
name|'_TestVolumeMapping'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestRemoteVolumeMapping
dedent|''
name|'class'
name|'TestRemoteVolumeMapping'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
name|'_TestVolumeMapping'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
