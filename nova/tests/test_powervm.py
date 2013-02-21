begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM'
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
string|'"""\nTest suite for PowerVMDriver.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_network_cache_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'blockdev'
name|'as'
name|'powervm_blockdev'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'driver'
name|'as'
name|'powervm_driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'lpar'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'operator'
newline|'\n'
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
DECL|function|fake_lpar
name|'def'
name|'fake_lpar'
op|'('
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'lpar'
op|'.'
name|'LPAR'
op|'('
name|'name'
op|'='
name|'instance_name'
op|','
nl|'\n'
name|'lpar_id'
op|'='
number|'1'
op|','
name|'desired_mem'
op|'='
number|'1024'
op|','
nl|'\n'
name|'max_mem'
op|'='
number|'2048'
op|','
name|'max_procs'
op|'='
number|'2'
op|','
nl|'\n'
name|'uptime'
op|'='
number|'939395'
op|','
name|'state'
op|'='
string|"'Running'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeIVMOperator
dedent|''
name|'class'
name|'FakeIVMOperator'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|get_lpar
indent|'    '
name|'def'
name|'get_lpar'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'resource_type'
op|'='
string|"'lpar'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake_lpar'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_lpar_instances
dedent|''
name|'def'
name|'list_lpar_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|"'instance-00000001'"
op|','
string|"'instance-00000002'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|create_lpar
dedent|''
name|'def'
name|'create_lpar'
op|'('
name|'self'
op|','
name|'lpar'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|start_lpar
dedent|''
name|'def'
name|'start_lpar'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|stop_lpar
dedent|''
name|'def'
name|'stop_lpar'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|remove_lpar
dedent|''
name|'def'
name|'remove_lpar'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_vhost_by_instance_id
dedent|''
name|'def'
name|'get_vhost_by_instance_id'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'vhostfake'"
newline|'\n'
nl|'\n'
DECL|member|get_virtual_eth_adapter_id
dedent|''
name|'def'
name|'get_virtual_eth_adapter_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_disk_name_by_vhost
dedent|''
name|'def'
name|'get_disk_name_by_vhost'
op|'('
name|'self'
op|','
name|'vhost'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'lvfake01'"
newline|'\n'
nl|'\n'
DECL|member|remove_disk
dedent|''
name|'def'
name|'remove_disk'
op|'('
name|'self'
op|','
name|'disk_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|run_cfg_dev
dedent|''
name|'def'
name|'run_cfg_dev'
op|'('
name|'self'
op|','
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|attach_disk_to_vhost
dedent|''
name|'def'
name|'attach_disk_to_vhost'
op|'('
name|'self'
op|','
name|'disk'
op|','
name|'vhost'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_memory_info
dedent|''
name|'def'
name|'get_memory_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'total_mem'"
op|':'
number|'65536'
op|','
string|"'avail_mem'"
op|':'
number|'46336'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_cpu_info
dedent|''
name|'def'
name|'get_cpu_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'total_procs'"
op|':'
number|'8.0'
op|','
string|"'avail_procs'"
op|':'
number|'6.3'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_disk_info
dedent|''
name|'def'
name|'get_disk_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'disk_total'"
op|':'
number|'10168'
op|','
nl|'\n'
string|"'disk_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_avail'"
op|':'
number|'10168'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_hostname
dedent|''
name|'def'
name|'get_hostname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'fake-powervm'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeBlockAdapter
dedent|''
dedent|''
name|'class'
name|'FakeBlockAdapter'
op|'('
name|'powervm_blockdev'
op|'.'
name|'PowerVMLocalVolumeAdapter'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_create_logical_volume
dedent|''
name|'def'
name|'_create_logical_volume'
op|'('
name|'self'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'lvfake01'"
newline|'\n'
nl|'\n'
DECL|member|_remove_logical_volume
dedent|''
name|'def'
name|'_remove_logical_volume'
op|'('
name|'self'
op|','
name|'lv_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_copy_file_to_device
dedent|''
name|'def'
name|'_copy_file_to_device'
op|'('
name|'self'
op|','
name|'sourcePath'
op|','
name|'device'
op|','
name|'decrompress'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_copy_image_file
dedent|''
name|'def'
name|'_copy_image_file'
op|'('
name|'self'
op|','
name|'sourcePath'
op|','
name|'remotePath'
op|','
name|'decompress'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'finalPath'
op|'='
string|"'/home/images/rhel62.raw.7e358754160433febd6f3318b7c9e335'"
newline|'\n'
name|'size'
op|'='
number|'4294967296'
newline|'\n'
name|'return'
name|'finalPath'
op|','
name|'size'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_powervm_operator
dedent|''
dedent|''
name|'def'
name|'fake_get_powervm_operator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FakeIVMOperator'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMDriverTestCase
dedent|''
name|'class'
name|'PowerVMDriverTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for PowerVM connection calls."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PowerVMDriverTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'operator'
op|','
string|"'get_powervm_operator'"
op|','
nl|'\n'
name|'fake_get_powervm_operator'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'operator'
op|','
string|"'get_powervm_disk_adapter'"
op|','
nl|'\n'
name|'lambda'
op|':'
name|'FakeBlockAdapter'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'powervm_connection'
op|'='
name|'powervm_driver'
op|'.'
name|'PowerVMDriver'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_instances
dedent|''
name|'def'
name|'test_list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'instance-00000001'"
name|'in'
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'instance-00000002'"
name|'in'
name|'instances'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_exists
dedent|''
name|'def'
name|'test_instance_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'instance_exists'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn
dedent|''
name|'def'
name|'test_spawn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_image_fetch
indent|'        '
name|'def'
name|'fake_image_fetch'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'file_path'
op|','
nl|'\n'
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'flags'
op|'('
name|'powervm_img_local_path'
op|'='
string|"'/images/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'images'
op|','
string|"'fetch'"
op|','
name|'fake_image_fetch'
op|')'
newline|'\n'
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_meta'
op|'['
string|"'id'"
op|']'
op|'='
string|"'666'"
newline|'\n'
name|'fake_net_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'spawn'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
name|'image_meta'
op|','
op|'['
op|']'
op|','
string|"'s3cr3t'"
op|','
nl|'\n'
name|'fake_net_info'
op|')'
newline|'\n'
name|'state'
op|'='
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'get_info'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|'['
string|"'state'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_spawn_cleanup_on_fail
dedent|''
name|'def'
name|'test_spawn_cleanup_on_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Verify on a failed spawn, we get the original exception raised.'
nl|'\n'
comment|'# helper function'
nl|'\n'
DECL|function|raise_
indent|'        '
name|'def'
name|'raise_'
op|'('
name|'ex'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ex'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'flags'
op|'('
name|'powervm_img_local_path'
op|'='
string|"'/images/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'images'
op|','
string|"'fetch'"
op|','
name|'lambda'
op|'*'
name|'x'
op|','
op|'**'
name|'y'
op|':'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'_powervm'
op|'.'
name|'_disk_adapter'
op|','
nl|'\n'
string|"'create_volume_from_image'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'x'
op|','
op|'**'
name|'y'
op|':'
name|'raise_'
op|'('
name|'exception'
op|'.'
name|'PowerVMImageCreationFailed'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'_powervm'
op|','
string|"'_cleanup'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'x'
op|','
op|'**'
name|'y'
op|':'
name|'raise_'
op|'('
name|'Exception'
op|'('
string|"'This should be logged.'"
op|')'
op|')'
op|')'
newline|'\n'
name|'fake_net_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PowerVMImageCreationFailed'
op|','
nl|'\n'
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'spawn'
op|','
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'ANY_ID'"
op|'}'
op|','
op|'['
op|']'
op|','
string|"'s3cr3t'"
op|','
name|'fake_net_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy
dedent|''
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'FakeIVMOperator'
op|','
string|"'get_lpar'"
op|','
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'None'
op|')'
newline|'\n'
name|'name'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'instance_exists'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_info
dedent|''
name|'def'
name|'test_get_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
name|'self'
op|'.'
name|'powervm_connection'
op|'.'
name|'get_info'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'state'"
op|']'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'max_mem'"
op|']'
op|','
number|'2048'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'mem'"
op|']'
op|','
number|'1024'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'num_cpu'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'cpu_time'"
op|']'
op|','
number|'939395'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remote_utility_1
dedent|''
name|'def'
name|'test_remote_utility_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path_one'
op|'='
string|"'/some/file/'"
newline|'\n'
name|'path_two'
op|'='
string|"'/path/filename'"
newline|'\n'
name|'joined_path'
op|'='
name|'common'
op|'.'
name|'aix_path_join'
op|'('
name|'path_one'
op|','
name|'path_two'
op|')'
newline|'\n'
name|'expected_path'
op|'='
string|"'/some/file/path/filename'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'joined_path'
op|','
name|'expected_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remote_utility_2
dedent|''
name|'def'
name|'test_remote_utility_2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path_one'
op|'='
string|"'/some/file/'"
newline|'\n'
name|'path_two'
op|'='
string|"'path/filename'"
newline|'\n'
name|'joined_path'
op|'='
name|'common'
op|'.'
name|'aix_path_join'
op|'('
name|'path_one'
op|','
name|'path_two'
op|')'
newline|'\n'
name|'expected_path'
op|'='
string|"'/some/file/path/filename'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'joined_path'
op|','
name|'expected_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remote_utility_3
dedent|''
name|'def'
name|'test_remote_utility_3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path_one'
op|'='
string|"'/some/file'"
newline|'\n'
name|'path_two'
op|'='
string|"'/path/filename'"
newline|'\n'
name|'joined_path'
op|'='
name|'common'
op|'.'
name|'aix_path_join'
op|'('
name|'path_one'
op|','
name|'path_two'
op|')'
newline|'\n'
name|'expected_path'
op|'='
string|"'/some/file/path/filename'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'joined_path'
op|','
name|'expected_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remote_utility_4
dedent|''
name|'def'
name|'test_remote_utility_4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path_one'
op|'='
string|"'/some/file'"
newline|'\n'
name|'path_two'
op|'='
string|"'path/filename'"
newline|'\n'
name|'joined_path'
op|'='
name|'common'
op|'.'
name|'aix_path_join'
op|'('
name|'path_one'
op|','
name|'path_two'
op|')'
newline|'\n'
name|'expected_path'
op|'='
string|"'/some/file/path/filename'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'joined_path'
op|','
name|'expected_path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
