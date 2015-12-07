begin_unit
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
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'network_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vif'
newline|'\n'
nl|'\n'
DECL|variable|fake_vif
name|'fake_vif'
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
string|"'123456789123'"
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'00:00:00:00:00:00'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
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
DECL|function|fake_call_xenapi
name|'def'
name|'fake_call_xenapi'
op|'('
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'method'
op|'=='
string|'"VM.get_VIFs"'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|'"fake_vif_ref"'
op|','
string|'"fake_vif_ref_A2"'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'method'
op|'=='
string|'"VIF.get_record"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"fake_vif_ref"'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'fake_vif'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'MAC'"
op|':'
name|'fake_vif'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'network'"
op|':'
string|"'fake_network'"
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
string|"'nicira-iface-id'"
op|':'
name|'fake_vif'
op|'['
string|"'id'"
op|']'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Exception'
op|'('
string|'"Failed get vif record"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'method'
op|'=='
string|'"VIF.unplug"'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'method'
op|'=='
string|'"VIF.destroy"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"fake_vif_ref"'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Exception'
op|'('
string|'"unplug vif failed"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'method'
op|'=='
string|'"VIF.create"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"fake_vif_rec"'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"fake_vif_ref"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Exception'
op|'('
string|'"VIF existed"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
string|'"Unexpected call_xenapi: %s.%s"'
op|'%'
op|'('
name|'method'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenVIFDriverTestBase
dedent|''
name|'class'
name|'XenVIFDriverTestBase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
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
name|'XenVIFDriverTestBase'
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
name|'_session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'.'
name|'side_effect'
op|'='
name|'fake_call_xenapi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenVIFDriverTestCase
dedent|''
dedent|''
name|'class'
name|'XenVIFDriverTestCase'
op|'('
name|'XenVIFDriverTestBase'
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
name|'XenVIFDriverTestCase'
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
name|'base_driver'
op|'='
name|'vif'
op|'.'
name|'XenVIFDriver'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vif_ref
dedent|''
name|'def'
name|'test_get_vif_ref'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'vif_ref'
op|'='
string|"'fake_vif_ref'"
newline|'\n'
name|'ret_vif_ref'
op|'='
name|'self'
op|'.'
name|'base_driver'
op|'.'
name|'_get_vif_ref'
op|'('
name|'fake_vif'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vif_ref'
op|','
name|'ret_vif_ref'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VM.get_VIFs'"
op|','
name|'vm_ref'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VIF.get_record'"
op|','
name|'vif_ref'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vif_ref_none_and_exception
dedent|''
name|'def'
name|'test_get_vif_ref_none_and_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'vif'
op|'='
op|'{'
string|"'address'"
op|':'
string|'"no_match_vif_address"'
op|'}'
newline|'\n'
name|'ret_vif_ref'
op|'='
name|'self'
op|'.'
name|'base_driver'
op|'.'
name|'_get_vif_ref'
op|'('
name|'vif'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'ret_vif_ref'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VM.get_VIFs'"
op|','
name|'vm_ref'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VIF.get_record'"
op|','
string|"'fake_vif_ref'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VIF.get_record'"
op|','
string|"'fake_vif_ref_A2'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vif
dedent|''
name|'def'
name|'test_create_vif'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif_rec'
op|'='
string|'"fake_vif_rec"'
newline|'\n'
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'ret_vif_ref'
op|'='
name|'self'
op|'.'
name|'base_driver'
op|'.'
name|'_create_vif'
op|'('
name|'fake_vif'
op|','
name|'vif_rec'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"fake_vif_ref"'
op|','
name|'ret_vif_ref'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VIF.create'"
op|','
name|'vif_rec'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_vif_exception
dedent|''
name|'def'
name|'test_create_vif_exception'
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
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'base_driver'
op|'.'
name|'_create_vif'
op|','
nl|'\n'
string|'"fake_vif"'
op|','
string|'"missing_vif_rec"'
op|','
string|'"fake_vm_ref"'
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
name|'vif'
op|'.'
name|'XenVIFDriver'
op|','
string|"'_get_vif_ref'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_vif_ref'"
op|')'
newline|'\n'
DECL|member|test_unplug
name|'def'
name|'test_unplug'
op|'('
name|'self'
op|','
name|'mock_get_vif_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|"'name'"
op|':'
string|'"fake_instance"'
op|'}'
newline|'\n'
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'self'
op|'.'
name|'base_driver'
op|'.'
name|'unplug'
op|'('
name|'instance'
op|','
name|'fake_vif'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VIF.destroy'"
op|','
string|"'fake_vif_ref'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'.'
name|'call_args_list'
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
name|'vif'
op|'.'
name|'XenVIFDriver'
op|','
string|"'_get_vif_ref'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'missing_vif_ref'"
op|')'
newline|'\n'
DECL|member|test_unplug_exception
name|'def'
name|'test_unplug_exception'
op|'('
name|'self'
op|','
name|'mock_get_vif_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
string|'"fake_instance"'
newline|'\n'
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'base_driver'
op|'.'
name|'unplug'
op|','
nl|'\n'
name|'instance'
op|','
name|'fake_vif'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIBridgeDriverTestCase
dedent|''
dedent|''
name|'class'
name|'XenAPIBridgeDriverTestCase'
op|'('
name|'XenVIFDriverTestBase'
op|','
name|'object'
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
name|'XenAPIBridgeDriverTestCase'
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
name|'bridge_driver'
op|'='
name|'vif'
op|'.'
name|'XenAPIBridgeDriver'
op|'('
name|'self'
op|'.'
name|'_session'
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
name|'vif'
op|'.'
name|'XenAPIBridgeDriver'
op|','
string|"'_ensure_vlan_bridge'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_network_ref'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vif'
op|'.'
name|'XenVIFDriver'
op|','
string|"'_create_vif'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_vif_ref'"
op|')'
newline|'\n'
DECL|member|test_plug_create_vlan
name|'def'
name|'test_plug_create_vlan'
op|'('
name|'self'
op|','
name|'mock_create_vif'
op|','
name|'mock_ensure_vlan_bridge'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|"'name'"
op|':'
string|'"fake_instance_name"'
op|'}'
newline|'\n'
name|'network'
op|'='
name|'model'
op|'.'
name|'Network'
op|'('
op|')'
newline|'\n'
name|'network'
op|'.'
name|'_set_meta'
op|'('
op|'{'
string|"'should_create_vlan'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
name|'vif'
op|'='
name|'model'
op|'.'
name|'VIF'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'.'
name|'_set_meta'
op|'('
op|'{'
string|"'rxtx_cap'"
op|':'
number|'1'
op|'}'
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'='
name|'network'
newline|'\n'
name|'vif'
op|'['
string|"'address'"
op|']'
op|'='
string|'"fake_address"'
newline|'\n'
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'device'
op|'='
number|'1'
newline|'\n'
name|'ret_vif_ref'
op|'='
name|'self'
op|'.'
name|'bridge_driver'
op|'.'
name|'plug'
op|'('
name|'instance'
op|','
name|'vif'
op|','
name|'vm_ref'
op|','
name|'device'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake_vif_ref'"
op|','
name|'ret_vif_ref'
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
name|'vif'
op|'.'
name|'XenVIFDriver'
op|','
string|"'_get_vif_ref'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_vif_ref'"
op|')'
newline|'\n'
DECL|member|test_unplug
name|'def'
name|'test_unplug'
op|'('
name|'self'
op|','
name|'mock_get_vif_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|"'name'"
op|':'
string|'"fake_instance"'
op|'}'
newline|'\n'
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'self'
op|'.'
name|'bridge_driver'
op|'.'
name|'unplug'
op|'('
name|'instance'
op|','
name|'fake_vif'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VIF.destroy'"
op|','
string|"'fake_vif_ref'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIOpenVswitchDriverTestCase
dedent|''
dedent|''
name|'class'
name|'XenAPIOpenVswitchDriverTestCase'
op|'('
name|'XenVIFDriverTestBase'
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
name|'XenAPIOpenVswitchDriverTestCase'
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
name|'ovs_driver'
op|'='
name|'vif'
op|'.'
name|'XenAPIOpenVswitchDriver'
op|'('
name|'self'
op|'.'
name|'_session'
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
name|'network_utils'
op|','
string|"'find_network_with_bridge'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_network_ref'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vif'
op|'.'
name|'XenVIFDriver'
op|','
string|"'_create_vif'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_vif_ref'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vif'
op|'.'
name|'XenVIFDriver'
op|','
string|"'_get_vif_ref'"
op|','
name|'return_value'
op|'='
name|'None'
op|')'
newline|'\n'
DECL|member|test_plug
name|'def'
name|'test_plug'
op|'('
name|'self'
op|','
name|'mock_get_vif_ref'
op|','
name|'mock_create_vif'
op|','
nl|'\n'
name|'mock_find_network_with_bridge'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|"'name'"
op|':'
string|'"fake_instance_name"'
op|'}'
newline|'\n'
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'device'
op|'='
number|'1'
newline|'\n'
name|'ret_vif_ref'
op|'='
name|'self'
op|'.'
name|'ovs_driver'
op|'.'
name|'plug'
op|'('
name|'instance'
op|','
name|'fake_vif'
op|','
name|'vm_ref'
op|','
name|'device'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake_vif_ref'"
op|','
name|'ret_vif_ref'
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
name|'vif'
op|'.'
name|'XenVIFDriver'
op|','
string|"'_get_vif_ref'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'fake_vif_ref'"
op|')'
newline|'\n'
DECL|member|test_unplug
name|'def'
name|'test_unplug'
op|'('
name|'self'
op|','
name|'mock_get_vif_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
string|"'name'"
op|':'
string|'"fake_instance"'
op|'}'
newline|'\n'
name|'vm_ref'
op|'='
string|'"fake_vm_ref"'
newline|'\n'
name|'self'
op|'.'
name|'ovs_driver'
op|'.'
name|'unplug'
op|'('
name|'instance'
op|','
name|'fake_vif'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'VIF.destroy'"
op|','
string|"'fake_vif_ref'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
