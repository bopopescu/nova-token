begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright (C) 2011 Nicira, Inc'
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
string|'"""VIF drivers for XenAPI."""'
newline|'\n'
nl|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'vif'
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
name|'vm_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|xenapi_ovs_integration_bridge_opt
name|'xenapi_ovs_integration_bridge_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'xenapi_ovs_integration_bridge'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'xapi1'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of Integration Bridge used by Open vSwitch'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opt'
op|'('
name|'xenapi_ovs_integration_bridge_opt'
op|')'
newline|'\n'
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
DECL|class|XenVIFDriver
name|'class'
name|'XenVIFDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'xenapi_session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'xenapi_session'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIBridgeDriver
dedent|''
dedent|''
name|'class'
name|'XenAPIBridgeDriver'
op|'('
name|'XenVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF Driver for XenAPI that uses XenAPI to create Networks."""'
newline|'\n'
nl|'\n'
DECL|member|plug
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|','
name|'vm_ref'
op|'='
name|'None'
op|','
name|'device'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'vm_ref'
op|':'
newline|'\n'
indent|'            '
name|'vm_ref'
op|'='
name|'vm_utils'
op|'.'
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'device'
op|'='
number|'0'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'.'
name|'get_meta'
op|'('
string|"'should_create_vlan'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'_ensure_vlan_bridge'
op|'('
name|'vif'
op|'['
string|"'network'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'network_ref'
op|'='
name|'network_utils'
op|'.'
name|'NetworkHelper'
op|'.'
name|'find_network_with_bridge'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'bridge'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'vif_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'device'"
op|']'
op|'='
name|'str'
op|'('
name|'device'
op|')'
newline|'\n'
name|'vif_rec'
op|'['
string|"'network'"
op|']'
op|'='
name|'network_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MAC'"
op|']'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MTU'"
op|']'
op|'='
string|"'1500'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'vif'
op|'.'
name|'get_meta'
op|'('
string|"'rxtx_cap'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vif_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"'ratelimit'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
string|"'kbps'"
op|':'
nl|'\n'
name|'str'
op|'('
name|'int'
op|'('
name|'vif'
op|'.'
name|'get_meta'
op|'('
string|"'rxtx_cap'"
op|')'
op|')'
op|'*'
number|'1024'
op|')'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'vif_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'vif_rec'
newline|'\n'
nl|'\n'
DECL|member|_ensure_vlan_bridge
dedent|''
name|'def'
name|'_ensure_vlan_bridge'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that a VLAN bridge exists"""'
newline|'\n'
nl|'\n'
name|'vlan_num'
op|'='
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'vlan'"
op|')'
newline|'\n'
name|'bridge'
op|'='
name|'network'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'bridge_interface'
op|'='
op|'('
name|'FLAGS'
op|'.'
name|'vlan_interface'
name|'or'
nl|'\n'
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'bridge_interface'"
op|')'
op|')'
newline|'\n'
comment|'# Check whether bridge already exists'
nl|'\n'
comment|'# Retrieve network whose name_label is "bridge"'
nl|'\n'
name|'network_ref'
op|'='
name|'network_utils'
op|'.'
name|'NetworkHelper'
op|'.'
name|'find_network_with_name_label'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'bridge'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# If bridge does not exists'
nl|'\n'
comment|'# 1 - create network'
nl|'\n'
indent|'            '
name|'description'
op|'='
string|"'network for nova bridge %s'"
op|'%'
name|'bridge'
newline|'\n'
name|'network_rec'
op|'='
op|'{'
string|"'name_label'"
op|':'
name|'bridge'
op|','
nl|'\n'
string|"'name_description'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'network.create'"
op|','
nl|'\n'
name|'network_rec'
op|')'
newline|'\n'
comment|'# 2 - find PIF for VLAN NOTE(salvatore-orlando): using double'
nl|'\n'
comment|'# quotes inside single quotes as xapi filter only support'
nl|'\n'
comment|'# tokens in double quotes'
nl|'\n'
name|'expr'
op|'='
op|'('
string|'\'field "device" = "%s" and field "VLAN" = "-1"\''
op|'%'
nl|'\n'
name|'bridge_interface'
op|')'
newline|'\n'
name|'pifs'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'PIF.get_all_records_where'"
op|','
nl|'\n'
name|'expr'
op|')'
newline|'\n'
name|'pif_ref'
op|'='
name|'None'
newline|'\n'
comment|'# Multiple PIF are ok: we are dealing with a pool'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'pifs'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Found no PIF for device %s'"
op|')'
op|'%'
nl|'\n'
name|'bridge_interface'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'pif_ref'
name|'in'
name|'pifs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VLAN.create'"
op|','
nl|'\n'
name|'pif_ref'
op|','
nl|'\n'
name|'str'
op|'('
name|'vlan_num'
op|')'
op|','
nl|'\n'
name|'network_ref'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Check VLAN tag is appropriate'
nl|'\n'
indent|'            '
name|'network_rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'network.get_record'"
op|','
nl|'\n'
name|'network_ref'
op|')'
newline|'\n'
comment|'# Retrieve PIFs from network'
nl|'\n'
name|'for'
name|'pif_ref'
name|'in'
name|'network_rec'
op|'['
string|"'PIFs'"
op|']'
op|':'
newline|'\n'
comment|'# Retrieve VLAN from PIF'
nl|'\n'
indent|'                '
name|'pif_rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'PIF.get_record'"
op|','
nl|'\n'
name|'pif_ref'
op|')'
newline|'\n'
name|'pif_vlan'
op|'='
name|'int'
op|'('
name|'pif_rec'
op|'['
string|"'VLAN'"
op|']'
op|')'
newline|'\n'
comment|'# Raise an exception if VLAN != vlan_num'
nl|'\n'
name|'if'
name|'pif_vlan'
op|'!='
name|'vlan_num'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
nl|'\n'
string|'"PIF %(pif_rec[\'uuid\'])s for network "'
nl|'\n'
string|'"%(bridge)s has VLAN id %(pif_vlan)d. "'
nl|'\n'
string|'"Expected %(vlan_num)d"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIOpenVswitchDriver
dedent|''
dedent|''
name|'class'
name|'XenAPIOpenVswitchDriver'
op|'('
name|'XenVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch with XenAPI."""'
newline|'\n'
nl|'\n'
DECL|member|plug
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|','
name|'vm_ref'
op|'='
name|'None'
op|','
name|'device'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'vm_ref'
op|':'
newline|'\n'
indent|'            '
name|'vm_ref'
op|'='
name|'vm_utils'
op|'.'
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'device'
op|'='
number|'0'
newline|'\n'
nl|'\n'
comment|'# with OVS model, always plug into an OVS integration bridge'
nl|'\n'
comment|'# that is already created'
nl|'\n'
dedent|''
name|'network_ref'
op|'='
name|'network_utils'
op|'.'
name|'NetworkHelper'
op|'.'
name|'find_network_with_bridge'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'FLAGS'
op|'.'
name|'xenapi_ovs_integration_bridge'
op|')'
newline|'\n'
name|'vif_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'device'"
op|']'
op|'='
name|'str'
op|'('
name|'device'
op|')'
newline|'\n'
name|'vif_rec'
op|'['
string|"'network'"
op|']'
op|'='
name|'network_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MAC'"
op|']'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MTU'"
op|']'
op|'='
string|"'1500'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|'# OVS on the hypervisor monitors this key and uses it to'
nl|'\n'
comment|'# set the iface-id attribute'
nl|'\n'
name|'vif_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
string|"'nicira-iface-id'"
op|':'
name|'vif'
op|'['
string|"'id'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'vif_rec'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
