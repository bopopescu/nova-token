begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vmops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareVMOpsTestCase
name|'class'
name|'VMwareVMOpsTestCase'
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
name|'VMwareVMOpsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'subnet_4'
op|'='
name|'network_model'
op|'.'
name|'Subnet'
op|'('
name|'cidr'
op|'='
string|"'192.168.0.1/24'"
op|','
nl|'\n'
name|'dns'
op|'='
op|'['
name|'network_model'
op|'.'
name|'IP'
op|'('
string|"'192.168.0.1'"
op|')'
op|']'
op|','
nl|'\n'
name|'gateway'
op|'='
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
string|"'192.168.0.1'"
op|')'
op|','
nl|'\n'
name|'ips'
op|'='
op|'['
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
string|"'192.168.0.100'"
op|')'
op|']'
op|','
nl|'\n'
name|'routes'
op|'='
name|'None'
op|')'
newline|'\n'
name|'subnet_6'
op|'='
name|'network_model'
op|'.'
name|'Subnet'
op|'('
name|'cidr'
op|'='
string|"'dead:beef::1/64'"
op|','
nl|'\n'
name|'dns'
op|'='
name|'None'
op|','
nl|'\n'
name|'gateway'
op|'='
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
string|"'dead:beef::1'"
op|')'
op|','
nl|'\n'
name|'ips'
op|'='
op|'['
name|'network_model'
op|'.'
name|'IP'
op|'('
nl|'\n'
string|"'dead:beef::dcad:beff:feef:0'"
op|')'
op|']'
op|','
nl|'\n'
name|'routes'
op|'='
name|'None'
op|')'
newline|'\n'
name|'network'
op|'='
name|'network_model'
op|'.'
name|'Network'
op|'('
name|'id'
op|'='
number|'0'
op|','
nl|'\n'
name|'bridge'
op|'='
string|"'fa0'"
op|','
nl|'\n'
name|'label'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'subnets'
op|'='
op|'['
name|'subnet_4'
op|','
name|'subnet_6'
op|']'
op|','
nl|'\n'
name|'vlan'
op|'='
name|'None'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
name|'None'
op|','
nl|'\n'
name|'injected'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
nl|'\n'
name|'network_model'
op|'.'
name|'VIF'
op|'('
name|'id'
op|'='
name|'None'
op|','
nl|'\n'
name|'address'
op|'='
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\n'
name|'network'
op|'='
name|'network'
op|','
nl|'\n'
name|'type'
op|'='
name|'None'
op|','
nl|'\n'
name|'devname'
op|'='
name|'None'
op|','
nl|'\n'
name|'ovs_interfaceid'
op|'='
name|'None'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
number|'3'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'reset_is_neutron'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_machine_id_str
dedent|''
name|'def'
name|'test_get_machine_id_str'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'.'
name|'_get_machine_id_str'
op|'('
name|'self'
op|'.'
name|'network_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
nl|'\n'
string|"'DE:AD:BE:EF:00:00;192.168.0.100;255.255.255.0;'"
nl|'\n'
string|"'192.168.0.1;192.168.0.255;192.168.0.1#'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_neutron_nova
dedent|''
name|'def'
name|'test_is_neutron_nova'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'network_api_class'
op|'='
string|"'nova.network.api.API'"
op|')'
newline|'\n'
name|'ops'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'('
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ops'
op|'.'
name|'_is_neutron'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_neutron_neutron
dedent|''
name|'def'
name|'test_is_neutron_neutron'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'network_api_class'
op|'='
string|"'nova.network.neutronv2.api.API'"
op|')'
newline|'\n'
name|'ops'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'('
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ops'
op|'.'
name|'_is_neutron'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_neutron_quantum
dedent|''
name|'def'
name|'test_is_neutron_quantum'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'network_api_class'
op|'='
string|"'nova.network.quantumv2.api.API'"
op|')'
newline|'\n'
name|'ops'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'('
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ops'
op|'.'
name|'_is_neutron'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_nf
dedent|''
name|'def'
name|'test_use_linked_clone_override_nf'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'.'
name|'decide_linked_clone'
op|'('
name|'None'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'value'
op|','
string|'"No overrides present but still overridden!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_nt
dedent|''
name|'def'
name|'test_use_linked_clone_override_nt'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'.'
name|'decide_linked_clone'
op|'('
name|'None'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'value'
op|','
string|'"No overrides present but still overridden!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_ny
dedent|''
name|'def'
name|'test_use_linked_clone_override_ny'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'.'
name|'decide_linked_clone'
op|'('
name|'None'
op|','
string|'"yes"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'value'
op|','
string|'"No overrides present but still overridden!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_ft
dedent|''
name|'def'
name|'test_use_linked_clone_override_ft'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'.'
name|'decide_linked_clone'
op|'('
name|'False'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'value'
op|','
nl|'\n'
string|'"image level metadata failed to override global"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_nt
dedent|''
name|'def'
name|'test_use_linked_clone_override_nt'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'.'
name|'decide_linked_clone'
op|'('
string|'"no"'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'value'
op|','
nl|'\n'
string|'"image level metadata failed to override global"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_yf
dedent|''
name|'def'
name|'test_use_linked_clone_override_yf'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'vmops'
op|'.'
name|'VMwareVMOps'
op|'.'
name|'decide_linked_clone'
op|'('
string|'"yes"'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'value'
op|','
nl|'\n'
string|'"image level metadata failed to override global"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
