begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Rackspace'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'db'
name|'import'
name|'fakes'
name|'as'
name|'db_fakes'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkTestCase
name|'class'
name|'NetworkTestCase'
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
name|'NetworkTestCase'
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
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'fake_call'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_network'
op|'='
name|'True'
op|','
nl|'\n'
name|'network_manager'
op|'='
name|'self'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'netuser'"
op|','
nl|'\n'
string|"'netuser'"
op|','
nl|'\n'
string|"'netuser'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'projects'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'db_fakes'
op|'.'
name|'stub_out_db_network_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'project'
op|'='
name|'None'
op|','
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'reload'
op|'('
name|'db'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFuncs
dedent|''
dedent|''
name|'class'
name|'TestFuncs'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_compare_fields
indent|'    '
name|'def'
name|'_compare_fields'
op|'('
name|'self'
op|','
name|'dict1'
op|','
name|'dict2'
op|','
name|'fields'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dict1'
op|'['
name|'field'
op|']'
op|','
name|'dict2'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_network_hosts
dedent|''
dedent|''
name|'def'
name|'test_set_network_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'network'
op|'.'
name|'set_network_hosts'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_network_host
dedent|''
name|'def'
name|'test_set_network_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'network'
op|'.'
name|'set_network_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_for_instance
dedent|''
name|'def'
name|'test_allocate_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
number|'0'
newline|'\n'
name|'project_id'
op|'='
number|'0'
newline|'\n'
name|'type_id'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'set_network_hosts'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'nw'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_for_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'instance_type_id'
op|'='
name|'type_id'
op|')'
newline|'\n'
name|'static_info'
op|'='
op|'['
op|'('
op|'{'
string|"'bridge'"
op|':'
string|"'fa0'"
op|','
string|"'id'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'broadcast'"
op|':'
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'dns'"
op|':'
op|'['
string|"'192.168.0.1'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'gateway6'"
op|':'
string|"'dead:beef::1'"
op|','
nl|'\n'
string|"'ip6s'"
op|':'
op|'['
op|'{'
string|"'enabled'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'dead:beef::dcad:beff:feef:0'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'64'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
op|'{'
string|"'enabled'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'192.168.0.100'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'mac'"
op|':'
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\n'
string|"'rxtx_cap'"
op|':'
number|'3'
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_compare_fields'
op|'('
name|'nw'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|','
name|'static_info'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|','
op|'('
string|"'bridge'"
op|','
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare_fields'
op|'('
name|'nw'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|','
name|'static_info'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|','
op|'('
string|"'ips'"
op|','
nl|'\n'
string|"'broadcast'"
op|','
nl|'\n'
string|"'gateway'"
op|','
nl|'\n'
string|"'ip6s'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deallocate_for_instance
dedent|''
name|'def'
name|'test_deallocate_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
number|'0'
newline|'\n'
name|'network_id'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'set_network_hosts'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'add_fixed_ip_to_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'network_id'
op|'='
name|'network_id'
op|')'
newline|'\n'
name|'ips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ip'
op|'['
string|"'allocated'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_for_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|')'
newline|'\n'
name|'ips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'ips'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ip'
op|'['
string|"'allocated'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lease_release_fixed_ip
dedent|''
dedent|''
name|'def'
name|'test_lease_release_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
number|'0'
newline|'\n'
name|'project_id'
op|'='
number|'0'
newline|'\n'
name|'type_id'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'set_network_hosts'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'nw'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_for_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'instance_type_id'
op|'='
name|'type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'network_id'
op|'='
name|'nw'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'ips'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'vif'
op|'='
name|'db'
op|'.'
name|'virtual_interface_get_by_instance_and_network'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'network_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ips'
op|')'
newline|'\n'
name|'address'
op|'='
name|'ips'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'fixed_ip_associate'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|','
nl|'\n'
op|'{'
string|"'virtual_interface_id'"
op|':'
name|'vif'
op|'['
string|"'id'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'lease_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
name|'address'
op|')'
newline|'\n'
name|'ip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ip'
op|'['
string|"'leased'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'release_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
name|'address'
op|')'
newline|'\n'
name|'ip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ip'
op|'['
string|"'leased'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
