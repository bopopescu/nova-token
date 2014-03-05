begin_unit
comment|'# Copyright (c) 2013 dotCloud, Inc.'
nl|'\n'
comment|'# All Rights Reserved.'
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
name|'contextlib'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'units'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'mock_client'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'test_virt_drivers'
name|'import'
name|'_VirtDriverTestCase'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
name|'import'
name|'hostinfo'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
name|'import'
name|'network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DockerDriverTestCase
name|'class'
name|'DockerDriverTestCase'
op|'('
name|'_VirtDriverTestCase'
op|','
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|driver_module
indent|'    '
name|'driver_module'
op|'='
string|"'nova.virt.docker.DockerDriver'"
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
name|'DockerDriverTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_client'
op|'='
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'mock_client'
op|'.'
name|'MockClient'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'driver'
op|'.'
name|'DockerDriver'
op|','
string|"'docker'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'mock_client'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_setup_network
name|'def'
name|'fake_setup_network'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'driver'
op|'.'
name|'DockerDriver'
op|','
nl|'\n'
string|"'_setup_network'"
op|','
nl|'\n'
name|'fake_setup_network'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get_registry_port
name|'def'
name|'fake_get_registry_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'5042'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'driver'
op|'.'
name|'DockerDriver'
op|','
nl|'\n'
string|"'_get_registry_port'"
op|','
nl|'\n'
name|'fake_get_registry_port'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note: using mock.object.path on class throws'
nl|'\n'
comment|'# errors in test_virt_drivers'
nl|'\n'
DECL|function|fake_teardown_network
name|'def'
name|'fake_teardown_network'
op|'('
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network'
op|','
string|"'teardown_network'"
op|','
name|'fake_teardown_network'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_driver_capabilities
dedent|''
name|'def'
name|'test_driver_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'connection'
op|'.'
name|'capabilities'
op|'['
string|"'has_imagecache'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'connection'
op|'.'
name|'capabilities'
op|'['
string|"'supports_recreate'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'#NOTE(bcwaldon): This exists only because _get_running_instance on the'
nl|'\n'
comment|'# base class will not let us set a custom disk/container_format.'
nl|'\n'
DECL|member|_get_running_instance
dedent|''
name|'def'
name|'_get_running_instance'
op|'('
name|'self'
op|','
name|'obj'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ref'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
name|'obj'
op|'='
name|'obj'
op|')'
newline|'\n'
name|'network_info'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
newline|'\n'
name|'network_info'
op|'['
number|'0'
op|']'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'dhcp_server'"
op|']'
op|'='
string|"'1.1.1.1'"
newline|'\n'
name|'image_info'
op|'='
name|'utils'
op|'.'
name|'get_test_image_info'
op|'('
name|'None'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'image_info'
op|'['
string|"'disk_format'"
op|']'
op|'='
string|"'raw'"
newline|'\n'
name|'image_info'
op|'['
string|"'container_format'"
op|']'
op|'='
string|"'docker'"
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance_ref'
op|')'
op|','
nl|'\n'
name|'image_info'
op|','
op|'['
op|']'
op|','
string|"'herp'"
op|','
name|'network_info'
op|'='
name|'network_info'
op|')'
newline|'\n'
name|'return'
name|'instance_ref'
op|','
name|'network_info'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_stats
dedent|''
name|'def'
name|'test_get_host_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'socket'
op|','
string|"'gethostname'"
op|')'
newline|'\n'
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_host_stats'
op|'('
op|')'
op|'['
string|"'host_hostname'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_host_stats'
op|'('
op|')'
op|'['
string|"'host_hostname'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_available_resource
dedent|''
name|'def'
name|'test_get_available_resource'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'memory'
op|'='
op|'{'
nl|'\n'
string|"'total'"
op|':'
number|'4'
op|'*'
name|'units'
op|'.'
name|'Mi'
op|','
nl|'\n'
string|"'free'"
op|':'
number|'3'
op|'*'
name|'units'
op|'.'
name|'Mi'
op|','
nl|'\n'
string|"'used'"
op|':'
number|'1'
op|'*'
name|'units'
op|'.'
name|'Mi'
nl|'\n'
op|'}'
newline|'\n'
name|'disk'
op|'='
op|'{'
nl|'\n'
string|"'total'"
op|':'
number|'50'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
nl|'\n'
string|"'available'"
op|':'
number|'25'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
nl|'\n'
string|"'used'"
op|':'
number|'25'
op|'*'
name|'units'
op|'.'
name|'Gi'
nl|'\n'
op|'}'
newline|'\n'
comment|'# create the mocks'
nl|'\n'
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'hostinfo'
op|','
string|"'get_memory_usage'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'memory'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'hostinfo'
op|','
string|"'get_disk_usage'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'disk'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
nl|'\n'
name|'get_memory_usage'
op|','
nl|'\n'
name|'get_disk_usage'
nl|'\n'
op|')'
op|':'
newline|'\n'
comment|'# run the code'
nl|'\n'
indent|'            '
name|'stats'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_available_resource'
op|'('
name|'nodename'
op|'='
string|"'test'"
op|')'
newline|'\n'
comment|'# make our assertions'
nl|'\n'
name|'get_memory_usage'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'get_disk_usage'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'expected_stats'
op|'='
op|'{'
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'50L'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
number|'25L'
op|','
nl|'\n'
string|"'disk_available_least'"
op|':'
number|'25L'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|"'docker'"
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
string|"'?'"
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
op|'('
string|'\'[["i686", "docker", "lxc"],\''
nl|'\n'
string|'\' ["x86_64", "docker", "lxc"]]\''
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_stats'
op|','
name|'stats'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_plug_vifs
dedent|''
dedent|''
name|'def'
name|'test_plug_vifs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Check to make sure the method raises NotImplementedError.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'plug_vifs'
op|','
nl|'\n'
name|'instance'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unplug_vifs
dedent|''
name|'def'
name|'test_unplug_vifs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Check to make sure the method raises NotImplementedError.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'unplug_vifs'
op|','
nl|'\n'
name|'instance'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_container
dedent|''
name|'def'
name|'test_create_container'
op|'('
name|'self'
op|','
name|'image_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_href'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
newline|'\n'
name|'if'
name|'image_info'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'image_info'
op|'='
name|'utils'
op|'.'
name|'get_test_image_info'
op|'('
name|'None'
op|','
name|'instance_href'
op|')'
newline|'\n'
name|'image_info'
op|'['
string|"'disk_format'"
op|']'
op|'='
string|"'raw'"
newline|'\n'
name|'image_info'
op|'['
string|"'container_format'"
op|']'
op|'='
string|"'docker'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'connection'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_href'
op|','
name|'image_info'
op|','
nl|'\n'
string|"'fake_files'"
op|','
string|"'fake_password'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assert_cpu_shares'
op|'('
name|'instance_href'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'mock_client'
op|'.'
name|'name'
op|','
string|'"nova-{0}"'
op|'.'
name|'format'
op|'('
nl|'\n'
name|'instance_href'
op|'['
string|"'uuid'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_container_vcpus_2
dedent|''
name|'def'
name|'test_create_container_vcpus_2'
op|'('
name|'self'
op|','
name|'image_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'utils'
op|'.'
name|'get_test_flavor'
op|'('
name|'options'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'vcpu_2'"
op|','
nl|'\n'
string|"'flavorid'"
op|':'
string|"'vcpu_2'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'instance_href'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
name|'flavor'
op|'='
name|'flavor'
op|')'
newline|'\n'
name|'if'
name|'image_info'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'image_info'
op|'='
name|'utils'
op|'.'
name|'get_test_image_info'
op|'('
name|'None'
op|','
name|'instance_href'
op|')'
newline|'\n'
name|'image_info'
op|'['
string|"'disk_format'"
op|']'
op|'='
string|"'raw'"
newline|'\n'
name|'image_info'
op|'['
string|"'container_format'"
op|']'
op|'='
string|"'docker'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'connection'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_href'
op|','
name|'image_info'
op|','
nl|'\n'
string|"'fake_files'"
op|','
string|"'fake_password'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assert_cpu_shares'
op|'('
name|'instance_href'
op|','
name|'vcpus'
op|'='
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'mock_client'
op|'.'
name|'name'
op|','
string|'"nova-{0}"'
op|'.'
name|'format'
op|'('
nl|'\n'
name|'instance_href'
op|'['
string|"'uuid'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assert_cpu_shares
dedent|''
name|'def'
name|'_assert_cpu_shares'
op|'('
name|'self'
op|','
name|'instance_href'
op|','
name|'vcpus'
op|'='
number|'4'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_id'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'_find_container_by_name'
op|'('
nl|'\n'
name|'instance_href'
op|'['
string|"'name'"
op|']'
op|')'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'container_info'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'docker'
op|'.'
name|'inspect_container'
op|'('
name|'container_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vcpus'
op|'*'
number|'1024'
op|','
name|'container_info'
op|'['
string|"'Config'"
op|']'
op|'['
string|"'CpuShares'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.docker.driver.DockerDriver._setup_network'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'Exception'
op|')'
newline|'\n'
DECL|member|test_create_container_net_setup_fails
name|'def'
name|'test_create_container_net_setup_fails'
op|'('
name|'self'
op|','
name|'mock_setup_network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|','
nl|'\n'
name|'self'
op|'.'
name|'test_create_container'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'mock_client'
op|'.'
name|'list_containers'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_container_wrong_image
dedent|''
name|'def'
name|'test_create_container_wrong_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_href'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
newline|'\n'
name|'image_info'
op|'='
name|'utils'
op|'.'
name|'get_test_image_info'
op|'('
name|'None'
op|','
name|'instance_href'
op|')'
newline|'\n'
name|'image_info'
op|'['
string|"'disk_format'"
op|']'
op|'='
string|"'raw'"
newline|'\n'
name|'image_info'
op|'['
string|"'container_format'"
op|']'
op|'='
string|"'invalid_format'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|','
nl|'\n'
name|'self'
op|'.'
name|'test_create_container'
op|','
nl|'\n'
name|'image_info'
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
name|'network'
op|','
string|"'teardown_network'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'driver'
op|'.'
name|'DockerDriver'
op|','
nl|'\n'
string|"'_find_container_by_name'"
op|','
name|'return_value'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake_id'"
op|'}'
op|')'
newline|'\n'
DECL|member|test_destroy_container
name|'def'
name|'test_destroy_container'
op|'('
name|'self'
op|','
name|'byname_mock'
op|','
name|'teardown_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'fake_networkinfo'"
op|')'
newline|'\n'
name|'byname_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'teardown_mock'
op|'.'
name|'assert_called_with'
op|'('
string|"'fake_id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_memory_limit_from_sys_meta_in_object
dedent|''
name|'def'
name|'test_get_memory_limit_from_sys_meta_in_object'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'limit'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'_get_memory_limit_bytes'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2048'
op|'*'
name|'units'
op|'.'
name|'Mi'
op|','
name|'limit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_memory_limit_from_sys_meta_in_db_instance
dedent|''
name|'def'
name|'test_get_memory_limit_from_sys_meta_in_db_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
name|'obj'
op|'='
name|'False'
op|')'
newline|'\n'
name|'limit'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'_get_memory_limit_bytes'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2048'
op|'*'
name|'units'
op|'.'
name|'Mi'
op|','
name|'limit'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
