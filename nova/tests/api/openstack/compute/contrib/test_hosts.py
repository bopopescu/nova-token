begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'hosts'
name|'as'
name|'os_hosts'
newline|'\n'
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
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
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
name|'import'
name|'test'
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
DECL|variable|HOST_LIST
name|'HOST_LIST'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_c1"'
op|','
string|'"service"'
op|':'
string|'"compute"'
op|','
string|'"zone"'
op|':'
string|'"nova"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_c2"'
op|','
string|'"service"'
op|':'
string|'"compute"'
op|','
string|'"zone"'
op|':'
string|'"nonova"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_v1"'
op|','
string|'"service"'
op|':'
string|'"volume"'
op|','
string|'"zone"'
op|':'
string|'"nova"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_v2"'
op|','
string|'"service"'
op|':'
string|'"volume"'
op|','
string|'"zone"'
op|':'
string|'"nonova"'
op|'}'
op|']'
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|HOST_LIST_NOVA_ZONE
name|'HOST_LIST_NOVA_ZONE'
op|'='
op|'['
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_c1"'
op|','
string|'"service"'
op|':'
string|'"compute"'
op|','
string|'"zone"'
op|':'
string|'"nova"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_v1"'
op|','
string|'"service"'
op|':'
string|'"volume"'
op|','
string|'"zone"'
op|':'
string|'"nova"'
op|'}'
op|']'
newline|'\n'
DECL|variable|SERVICES_LIST
name|'SERVICES_LIST'
op|'='
op|'['
nl|'\n'
op|'{'
string|'"host"'
op|':'
string|'"host_c1"'
op|','
string|'"topic"'
op|':'
string|'"compute"'
op|','
string|'"availability_zone"'
op|':'
string|'"nova"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host"'
op|':'
string|'"host_c2"'
op|','
string|'"topic"'
op|':'
string|'"compute"'
op|','
string|'"availability_zone"'
op|':'
string|'"nonova"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host"'
op|':'
string|'"host_v1"'
op|','
string|'"topic"'
op|':'
string|'"volume"'
op|','
string|'"availability_zone"'
op|':'
string|'"nova"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host"'
op|':'
string|'"host_v2"'
op|','
string|'"topic"'
op|':'
string|'"volume"'
op|','
string|'"availability_zone"'
op|':'
string|'"nonova"'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_service_get_all
name|'def'
name|'stub_service_get_all'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'SERVICES_LIST'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_set_host_enabled
dedent|''
name|'def'
name|'stub_set_host_enabled'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'enabled'
op|')'
op|':'
newline|'\n'
comment|"# We'll simulate success and failure by assuming"
nl|'\n'
comment|"# that 'host_c1' always succeeds, and 'host_c2'"
nl|'\n'
comment|'# always fails'
nl|'\n'
indent|'    '
name|'fail'
op|'='
op|'('
name|'host'
op|'=='
string|'"host_c2"'
op|')'
newline|'\n'
name|'status'
op|'='
string|'"enabled"'
name|'if'
op|'('
name|'enabled'
op|'!='
name|'fail'
op|')'
name|'else'
string|'"disabled"'
newline|'\n'
name|'return'
name|'status'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_set_host_maintenance
dedent|''
name|'def'
name|'stub_set_host_maintenance'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
comment|"# We'll simulate success and failure by assuming"
nl|'\n'
comment|"# that 'host_c1' always succeeds, and 'host_c2'"
nl|'\n'
comment|'# always fails'
nl|'\n'
indent|'    '
name|'fail'
op|'='
op|'('
name|'host'
op|'=='
string|'"host_c2"'
op|')'
newline|'\n'
name|'maintenance'
op|'='
string|'"on_maintenance"'
name|'if'
op|'('
name|'mode'
op|'!='
name|'fail'
op|')'
name|'else'
string|'"off_maintenance"'
newline|'\n'
name|'return'
name|'maintenance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_host_power_action
dedent|''
name|'def'
name|'stub_host_power_action'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'action'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a test instance"""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'ctxt'
op|','
name|'_create_instance_dict'
op|'('
op|'**'
name|'kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_instance_dict
dedent|''
name|'def'
name|'_create_instance_dict'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a dictionary for a test instance"""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_ref'"
op|']'
op|'='
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
string|"'admin'"
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
string|"'1'"
newline|'\n'
name|'if'
string|"'host'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'['
string|"'host'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'host'"
op|')'
newline|'\n'
dedent|''
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'vcpus'"
op|','
number|'1'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'memory_mb'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'memory_mb'"
op|','
number|'20'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'root_gb'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'root_gb'"
op|','
number|'30'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ephemeral_gb'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'ephemeral_gb'"
op|','
number|'30'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'vm_state'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'vm_state'"
op|','
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'power_state'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'power_state'"
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'task_state'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'task_state'"
op|','
name|'None'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|','
name|'None'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'launched_on'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'launched_on'"
op|','
string|"'dummy'"
op|')'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
dedent|''
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequestWithNovaZone
dedent|''
name|'class'
name|'FakeRequestWithNovaZone'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
string|'"zone"'
op|':'
string|'"nova"'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostTestCase
dedent|''
name|'class'
name|'HostTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Case for hosts."""'
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
name|'HostTestCase'
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
name|'controller'
op|'='
name|'os_hosts'
op|'.'
name|'HostController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'service_get_all'"
op|','
nl|'\n'
name|'stub_service_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'api'
op|','
string|"'set_host_enabled'"
op|','
nl|'\n'
name|'stub_set_host_enabled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'api'
op|','
string|"'set_host_maintenance'"
op|','
nl|'\n'
name|'stub_set_host_maintenance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'api'
op|','
string|"'host_power_action'"
op|','
nl|'\n'
name|'stub_host_power_action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_host_update
dedent|''
name|'def'
name|'_test_host_update'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'key'
op|','
name|'val'
op|','
name|'expected_value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
name|'key'
op|':'
name|'val'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'host'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
name|'key'
op|']'
op|','
name|'expected_value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_hosts
dedent|''
name|'def'
name|'test_list_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Verify that the compute hosts are returned."""'
newline|'\n'
name|'hosts'
op|'='
name|'os_hosts'
op|'.'
name|'_list_hosts'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'hosts'
op|','
name|'HOST_LIST'
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'compute_hosts'
op|'='
name|'os_hosts'
op|'.'
name|'_list_hosts'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"compute"'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'host'
name|'for'
name|'host'
name|'in'
name|'HOST_LIST'
op|'['
string|"'hosts'"
op|']'
nl|'\n'
name|'if'
name|'host'
op|'['
string|'"service"'
op|']'
op|'=='
string|'"compute"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'compute_hosts'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_hosts_with_zone
dedent|''
name|'def'
name|'test_list_hosts_with_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequestWithNovaZone'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'os_hosts'
op|'.'
name|'_list_hosts'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'hosts'
op|','
name|'HOST_LIST_NOVA_ZONE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disable_host
dedent|''
name|'def'
name|'test_disable_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_host_update'
op|'('
string|"'host_c1'"
op|','
string|"'status'"
op|','
string|"'disable'"
op|','
string|"'disabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_host_update'
op|'('
string|"'host_c2'"
op|','
string|"'status'"
op|','
string|"'disable'"
op|','
string|"'enabled'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enable_host
dedent|''
name|'def'
name|'test_enable_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_host_update'
op|'('
string|"'host_c1'"
op|','
string|"'status'"
op|','
string|"'enable'"
op|','
string|"'enabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_host_update'
op|'('
string|"'host_c2'"
op|','
string|"'status'"
op|','
string|"'enable'"
op|','
string|"'disabled'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enable_maintenance
dedent|''
name|'def'
name|'test_enable_maintenance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_host_update'
op|'('
string|"'host_c1'"
op|','
string|"'maintenance_mode'"
op|','
nl|'\n'
string|"'enable'"
op|','
string|"'on_maintenance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disable_maintenance
dedent|''
name|'def'
name|'test_disable_maintenance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_host_update'
op|'('
string|"'host_c1'"
op|','
string|"'maintenance_mode'"
op|','
nl|'\n'
string|"'disable'"
op|','
string|"'off_maintenance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_startup
dedent|''
name|'def'
name|'test_host_startup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'startup'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"power_action"'
op|']'
op|','
string|'"startup"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_shutdown
dedent|''
name|'def'
name|'test_host_shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'shutdown'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"power_action"'
op|']'
op|','
string|'"shutdown"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_reboot
dedent|''
name|'def'
name|'test_host_reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'reboot'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"power_action"'
op|']'
op|','
string|'"reboot"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_status_value
dedent|''
name|'def'
name|'test_bad_status_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"bad"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'bad_body'
op|')'
newline|'\n'
name|'bad_body2'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"disablabc"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'bad_body2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_update_key
dedent|''
name|'def'
name|'test_bad_update_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_body'
op|'='
op|'{'
string|'"crazy"'
op|':'
string|'"bad"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'bad_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_update_key_and_correct_udpate_key
dedent|''
name|'def'
name|'test_bad_update_key_and_correct_udpate_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"disable"'
op|','
string|'"crazy"'
op|':'
string|'"bad"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'bad_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_good_udpate_keys
dedent|''
name|'def'
name|'test_good_udpate_keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"disable"'
op|','
string|'"maintenance_mode"'
op|':'
string|'"enable"'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|"'host_c1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"host"'
op|']'
op|','
string|'"host_c1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"status"'
op|']'
op|','
string|'"disabled"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"maintenance_mode"'
op|']'
op|','
string|'"on_maintenance"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_host
dedent|''
name|'def'
name|'test_bad_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"bogus_host_name"'
op|','
name|'body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"disable"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_forbidden
dedent|''
name|'def'
name|'test_show_forbidden'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'is_admin'
op|'='
name|'False'
newline|'\n'
name|'dest'
op|'='
string|"'dummydest'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'dest'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|test_show_host_not_exist
dedent|''
name|'def'
name|'test_show_host_not_exist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""A host given as an argument does not exists."""'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
name|'dest'
op|'='
string|"'dummydest'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_compute_service
dedent|''
name|'def'
name|'_create_compute_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create compute-manager(ComputeNode and Service record)."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'dic'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'dummy'"
op|','
string|"'binary'"
op|':'
string|"'nova-compute'"
op|','
string|"'topic'"
op|':'
string|"'compute'"
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
string|"'availability_zone'"
op|':'
string|"'dummyzone'"
op|'}'
newline|'\n'
name|'s_ref'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'ctxt'
op|','
name|'dic'
op|')'
newline|'\n'
nl|'\n'
name|'dic'
op|'='
op|'{'
string|"'service_id'"
op|':'
name|'s_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'16'
op|','
string|"'memory_mb'"
op|':'
number|'32'
op|','
string|"'local_gb'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'16'
op|','
string|"'memory_mb_used'"
op|':'
number|'32'
op|','
string|"'local_gb_used'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|"'qemu'"
op|','
string|"'hypervisor_version'"
op|':'
number|'12003'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
string|"''"
op|','
string|"'stats'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_create'
op|'('
name|'ctxt'
op|','
name|'dic'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'db'
op|'.'
name|'service_get'
op|'('
name|'ctxt'
op|','
name|'s_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_no_project
dedent|''
name|'def'
name|'test_show_no_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No instance are running on the given host."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'s_ref'
op|'='
name|'self'
op|'.'
name|'_create_compute_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'s_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'proj'
op|'='
op|'['
string|"'(total)'"
op|','
string|"'(used_now)'"
op|','
string|"'(used_max)'"
op|']'
newline|'\n'
name|'column'
op|'='
op|'['
string|"'host'"
op|','
string|"'project'"
op|','
string|"'cpu'"
op|','
string|"'memory_mb'"
op|','
string|"'disk_gb'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'host'"
op|']'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'for'
name|'resource'
name|'in'
name|'result'
op|'['
string|"'host'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'resource'
op|'['
string|"'resource'"
op|']'
op|'['
string|"'project'"
op|']'
name|'in'
name|'proj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'resource'
op|'['
string|"'resource'"
op|']'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'set'
op|'('
name|'resource'
op|'['
string|"'resource'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'=='
name|'set'
op|'('
name|'column'
op|')'
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'ctxt'
op|','
name|'s_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_works_correctly
dedent|''
name|'def'
name|'test_show_works_correctly'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""show() works correctly as expected."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'s_ref'
op|'='
name|'self'
op|'.'
name|'_create_compute_service'
op|'('
op|')'
newline|'\n'
name|'i_ref1'
op|'='
name|'_create_instance'
op|'('
name|'project_id'
op|'='
string|"'p-01'"
op|','
name|'host'
op|'='
name|'s_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'i_ref2'
op|'='
name|'_create_instance'
op|'('
name|'project_id'
op|'='
string|"'p-02'"
op|','
name|'vcpus'
op|'='
number|'3'
op|','
nl|'\n'
name|'host'
op|'='
name|'s_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'s_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'proj'
op|'='
op|'['
string|"'(total)'"
op|','
string|"'(used_now)'"
op|','
string|"'(used_max)'"
op|','
string|"'p-01'"
op|','
string|"'p-02'"
op|']'
newline|'\n'
name|'column'
op|'='
op|'['
string|"'host'"
op|','
string|"'project'"
op|','
string|"'cpu'"
op|','
string|"'memory_mb'"
op|','
string|"'disk_gb'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'['
string|"'host'"
op|']'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
name|'for'
name|'resource'
name|'in'
name|'result'
op|'['
string|"'host'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'resource'
op|'['
string|"'resource'"
op|']'
op|'['
string|"'project'"
op|']'
name|'in'
name|'proj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'resource'
op|'['
string|"'resource'"
op|']'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'set'
op|'('
name|'resource'
op|'['
string|"'resource'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'=='
name|'set'
op|'('
name|'column'
op|')'
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'ctxt'
op|','
name|'s_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'ctxt'
op|','
name|'i_ref1'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'ctxt'
op|','
name|'i_ref2'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostSerializerTest
dedent|''
dedent|''
name|'class'
name|'HostSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'HostSerializerTest'
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
name|'deserializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostUpdateDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_serializer
dedent|''
name|'def'
name|'test_index_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostIndexTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'HOST_LIST'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'hosts'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'HOST_LIST'
op|'['
string|"'hosts'"
op|']'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'HOST_LIST'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'['
name|'i'
op|']'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'HOST_LIST'
op|'['
string|"'hosts'"
op|']'
op|'['
name|'i'
op|']'
op|'['
string|"'host_name'"
op|']'
op|','
nl|'\n'
name|'tree'
op|'['
name|'i'
op|']'
op|'.'
name|'get'
op|'('
string|"'host_name'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'HOST_LIST'
op|'['
string|"'hosts'"
op|']'
op|'['
name|'i'
op|']'
op|'['
string|"'service'"
op|']'
op|','
nl|'\n'
name|'tree'
op|'['
name|'i'
op|']'
op|'.'
name|'get'
op|'('
string|"'service'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_serializer_with_status
dedent|''
dedent|''
name|'def'
name|'test_update_serializer_with_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
name|'status'
op|'='
string|"'enabled'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostUpdateTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_serializer_with_maintainance_mode
dedent|''
dedent|''
name|'def'
name|'test_update_serializer_with_maintainance_mode'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
name|'maintenance_mode'
op|'='
string|"'enabled'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostUpdateTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_serializer_with_maintainance_mode_and_status
dedent|''
dedent|''
name|'def'
name|'test_update_serializer_with_maintainance_mode_and_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
nl|'\n'
name|'maintenance_mode'
op|'='
string|"'enabled'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'enabled'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostUpdateTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_action_serializer
dedent|''
dedent|''
name|'def'
name|'test_action_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
name|'power_action'
op|'='
string|"'reboot'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostActionTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_deserializer
dedent|''
dedent|''
name|'def'
name|'test_update_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'status'
op|'='
string|"'enabled'"
op|','
name|'maintenance_mode'
op|'='
string|"'disable'"
op|')'
newline|'\n'
name|'intext'
op|'='
string|'"""<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n    <updates>\n        <status>enabled</status>\n        <maintenance_mode>disable</maintenance_mode>\n    </updates>"""'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'intext'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dict'
op|'('
name|'body'
op|'='
name|'exemplar'
op|')'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
