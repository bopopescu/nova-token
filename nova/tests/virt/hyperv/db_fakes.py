begin_unit
comment|'#  Copyright 2012 Cloudbase Solutions Srl'
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
DECL|function|get_fake_instance_data
name|'def'
name|'get_fake_instance_data'
op|'('
name|'name'
op|','
name|'project_id'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
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
string|"'project_id'"
op|':'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'user_id'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|'"de:ad:be:ef:be:ef"'
op|','
nl|'\n'
string|"'flavor'"
op|':'
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'m1.tiny'"
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'1'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fake_image_data
dedent|''
name|'def'
name|'get_fake_image_data'
op|'('
name|'project_id'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'user_id'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|'"1"'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|'"de:ad:be:ef:be:ef"'
op|','
nl|'\n'
string|"'flavor'"
op|':'
string|"'m1.tiny'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fake_volume_info_data
dedent|''
name|'def'
name|'get_fake_volume_info_data'
op|'('
name|'target_portal'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
string|"'iqn.2010-10.org.openstack:volume-'"
op|'+'
name|'volume_id'
op|','
nl|'\n'
string|"'target_portal'"
op|':'
name|'target_portal'
op|','
nl|'\n'
string|"'target_lun'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'auth_method'"
op|':'
string|"'CHAP'"
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fake_block_device_info
dedent|''
name|'def'
name|'get_fake_block_device_info'
op|'('
name|'target_portal'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'block_device_mapping'"
op|':'
op|'['
op|'{'
string|"'connection_info'"
op|':'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
string|"'target_lun'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume_id'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
nl|'\n'
string|"'iqn.2010-10.org.openstack:volume-'"
op|'+'
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
string|"'target_portal'"
op|':'
name|'target_portal'
op|','
nl|'\n'
string|"'target_discovered'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
string|"'mount_device'"
op|':'
string|"'vda'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|']'
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'ephemerals'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'None'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_db_instance_api
dedent|''
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
name|'FLAVORS'
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
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
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
name|'return'
name|'default'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
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
name|'return'
name|'self'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_create
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
name|'if'
string|"'flavor'"
name|'not'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'flavor'
op|'='
name|'values'
op|'['
string|"'flavor'"
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
string|"'flavor'"
op|':'
name|'flavor'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'flavor'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'flavor'
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
name|'flavor'
op|'['
string|"'root_gb'"
op|']'
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
op|'{'
string|"'image_shutdown_timeout'"
op|':'
number|'0'
op|'}'
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
DECL|function|fake_flavor_get_all
dedent|''
name|'def'
name|'fake_flavor_get_all'
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
name|'FLAVORS'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_flavor_get_by_name
dedent|''
name|'def'
name|'fake_flavor_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAVORS'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_block_device_mapping_get_all_by_instance
dedent|''
name|'def'
name|'fake_block_device_mapping_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
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
string|"'flavor_get_all'"
op|','
name|'fake_flavor_get_all'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'flavor_get_by_name'"
op|','
name|'fake_flavor_get_by_name'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'block_device_mapping_get_all_by_instance'"
op|','
nl|'\n'
name|'fake_block_device_mapping_get_all_by_instance'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
