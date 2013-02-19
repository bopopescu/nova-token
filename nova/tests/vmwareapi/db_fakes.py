begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nStubouts, mocks and fixtures for the test suite\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_db_instance_api
name|'def'
name|'stub_out_db_instance_api'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out the db API for creating Instances."""'
newline|'\n'
nl|'\n'
name|'INSTANCE_TYPES'
op|'='
op|'{'
nl|'\n'
string|"'m1.tiny'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'root_gb'
op|'='
number|'0'
op|','
name|'flavorid'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'m1.small'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'root_gb'
op|'='
number|'20'
op|','
name|'flavorid'
op|'='
number|'2'
op|')'
op|','
nl|'\n'
string|"'m1.medium'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'2'
op|','
name|'root_gb'
op|'='
number|'40'
op|','
name|'flavorid'
op|'='
number|'3'
op|')'
op|','
nl|'\n'
string|"'m1.large'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'8192'
op|','
name|'vcpus'
op|'='
number|'4'
op|','
name|'root_gb'
op|'='
number|'80'
op|','
name|'flavorid'
op|'='
number|'4'
op|')'
op|','
nl|'\n'
string|"'m1.xlarge'"
op|':'
nl|'\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'16384'
op|','
name|'vcpus'
op|'='
number|'8'
op|','
name|'root_gb'
op|'='
number|'160'
op|','
name|'flavorid'
op|'='
number|'5'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|FakeModel
name|'class'
name|'FakeModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stubs out for model."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'values'
op|'='
name|'values'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'values'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_create
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stubs out the db.instance_create method."""'
newline|'\n'
nl|'\n'
name|'type_data'
op|'='
name|'INSTANCE_TYPES'
op|'['
name|'values'
op|'['
string|"'instance_type'"
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'base_options'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'values'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'values'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'values'
op|'['
string|"'image_ref'"
op|']'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
name|'values'
op|'['
string|"'kernel_id'"
op|']'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'values'
op|'['
string|"'ramdisk_id'"
op|']'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'task_states'
op|'.'
name|'SCHEDULING'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'values'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'values'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'launch_time'"
op|':'
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'values'
op|'['
string|"'instance_type'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'type_data'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'mac_addresses'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
name|'values'
op|'['
string|"'mac_address'"
op|']'
op|'}'
op|']'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
name|'type_data'
op|'['
string|"'root_gb'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'FakeModel'
op|'('
name|'base_options'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_all
dedent|''
name|'def'
name|'fake_instance_type_get_all'
op|'('
name|'context'
op|','
name|'inactive'
op|'='
number|'0'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_by_name
dedent|''
name|'def'
name|'fake_instance_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_create'"
op|','
name|'fake_instance_create'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get_all'"
op|','
name|'fake_instance_type_get_all'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get_by_name'"
op|','
name|'fake_instance_type_get_by_name'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
