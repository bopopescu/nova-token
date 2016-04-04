begin_unit
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""VIF drivers for VMware."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'versionutils'
newline|'\n'
name|'from'
name|'oslo_vmware'
name|'import'
name|'vim_util'
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
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LI'
op|','
name|'_LW'
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
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'network_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vm_util'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|vmwareapi_vif_opts
name|'vmwareapi_vif_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vlan_interface'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'vmnic0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Physical ethernet adapter name for vlan networking'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'integration_bridge'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'This option should be configured only when using the '"
nl|'\n'
string|"'NSX-MH Neutron plugin. This is the name of the '"
nl|'\n'
string|"'integration bridge on the ESXi. This should not be set '"
nl|'\n'
string|"'for any other Neutron plugin. Hence the default value '"
nl|'\n'
string|"'is not set.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'vmwareapi_vif_opts'
op|','
string|"'vmware'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_associated_vswitch_for_interface
name|'def'
name|'_get_associated_vswitch_for_interface'
op|'('
name|'session'
op|','
name|'interface'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# Check if the physical network adapter exists on the host.'
nl|'\n'
indent|'    '
name|'if'
name|'not'
name|'network_util'
op|'.'
name|'check_if_vlan_interface_exists'
op|'('
name|'session'
op|','
nl|'\n'
name|'interface'
op|','
name|'cluster'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NetworkAdapterNotFound'
op|'('
name|'adapter'
op|'='
name|'interface'
op|')'
newline|'\n'
comment|'# Get the vSwitch associated with the Physical Adapter'
nl|'\n'
dedent|''
name|'vswitch_associated'
op|'='
name|'network_util'
op|'.'
name|'get_vswitch_for_vlan_interface'
op|'('
nl|'\n'
name|'session'
op|','
name|'interface'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'vswitch_associated'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'SwitchNotFoundForNetworkAdapter'
op|'('
name|'adapter'
op|'='
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'vswitch_associated'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan_bridge
dedent|''
name|'def'
name|'ensure_vlan_bridge'
op|'('
name|'session'
op|','
name|'vif'
op|','
name|'cluster'
op|'='
name|'None'
op|','
name|'create_vlan'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a vlan and bridge unless they already exist."""'
newline|'\n'
name|'vlan_num'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'.'
name|'get_meta'
op|'('
string|"'vlan'"
op|')'
newline|'\n'
name|'bridge'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'vlan_interface'
op|'='
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'vlan_interface'
newline|'\n'
nl|'\n'
name|'network_ref'
op|'='
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'session'
op|','
name|'bridge'
op|','
nl|'\n'
name|'cluster'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
name|'and'
name|'network_ref'
op|'['
string|"'type'"
op|']'
op|'=='
string|"'DistributedVirtualPortgroup'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'network_ref'
op|':'
newline|'\n'
comment|'# Create a port group on the vSwitch associated with the'
nl|'\n'
comment|'# vlan_interface corresponding physical network adapter on the ESX'
nl|'\n'
comment|'# host.'
nl|'\n'
indent|'        '
name|'vswitch_associated'
op|'='
name|'_get_associated_vswitch_for_interface'
op|'('
name|'session'
op|','
nl|'\n'
name|'vlan_interface'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'create_port_group'
op|'('
name|'session'
op|','
name|'bridge'
op|','
nl|'\n'
name|'vswitch_associated'
op|','
nl|'\n'
name|'vlan_num'
name|'if'
name|'create_vlan'
name|'else'
number|'0'
op|','
nl|'\n'
name|'cluster'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'session'
op|','
nl|'\n'
name|'bridge'
op|','
nl|'\n'
name|'cluster'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'create_vlan'
op|':'
newline|'\n'
comment|'# Get the vSwitch associated with the Physical Adapter'
nl|'\n'
indent|'        '
name|'vswitch_associated'
op|'='
name|'_get_associated_vswitch_for_interface'
op|'('
name|'session'
op|','
nl|'\n'
name|'vlan_interface'
op|','
name|'cluster'
op|')'
newline|'\n'
comment|'# Get the vlan id and vswitch corresponding to the port group'
nl|'\n'
name|'_get_pg_info'
op|'='
name|'network_util'
op|'.'
name|'get_vlanid_and_vswitch_for_portgroup'
newline|'\n'
name|'pg_vlanid'
op|','
name|'pg_vswitch'
op|'='
name|'_get_pg_info'
op|'('
name|'session'
op|','
name|'bridge'
op|','
name|'cluster'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if the vswitch associated is proper'
nl|'\n'
name|'if'
name|'pg_vswitch'
op|'!='
name|'vswitch_associated'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVLANPortGroup'
op|'('
nl|'\n'
name|'bridge'
op|'='
name|'bridge'
op|','
name|'expected'
op|'='
name|'vswitch_associated'
op|','
nl|'\n'
name|'actual'
op|'='
name|'pg_vswitch'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if the vlan id is proper for the port group'
nl|'\n'
dedent|''
name|'if'
name|'pg_vlanid'
op|'!='
name|'vlan_num'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVLANTag'
op|'('
name|'bridge'
op|'='
name|'bridge'
op|','
name|'tag'
op|'='
name|'vlan_num'
op|','
nl|'\n'
name|'pgroup'
op|'='
name|'pg_vlanid'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_check_ovs_supported_version
dedent|''
name|'def'
name|'_check_ovs_supported_version'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
comment|"# The port type 'ovs' is only support by the VC version 5.5 onwards"
nl|'\n'
indent|'    '
name|'min_version'
op|'='
name|'versionutils'
op|'.'
name|'convert_version_to_int'
op|'('
nl|'\n'
name|'constants'
op|'.'
name|'MIN_VC_OVS_VERSION'
op|')'
newline|'\n'
name|'vc_version'
op|'='
name|'versionutils'
op|'.'
name|'convert_version_to_int'
op|'('
nl|'\n'
name|'vim_util'
op|'.'
name|'get_vc_version'
op|'('
name|'session'
op|')'
op|')'
newline|'\n'
name|'if'
name|'vc_version'
op|'<'
name|'min_version'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'VMware vCenter version less than %(version)s '"
nl|'\n'
string|"'does not support the \\'ovs\\' port type.'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'version'"
op|':'
name|'constants'
op|'.'
name|'MIN_VC_OVS_VERSION'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_neutron_network
dedent|''
dedent|''
name|'def'
name|'_get_neutron_network'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'vif'
op|'['
string|"'type'"
op|']'
op|'=='
name|'model'
op|'.'
name|'VIF_TYPE_OVS'
op|':'
newline|'\n'
indent|'        '
name|'_check_ovs_supported_version'
op|'('
name|'session'
op|')'
newline|'\n'
comment|'# Check if this is the NSX-MH plugin is used'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'integration_bridge'
op|':'
newline|'\n'
indent|'            '
name|'net_id'
op|'='
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'integration_bridge'
newline|'\n'
name|'use_external_id'
op|'='
name|'False'
newline|'\n'
name|'network_type'
op|'='
string|"'opaque'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# The NSX|V3 plugin will pass the nsx-logical-switch-id as part'
nl|'\n'
comment|'# of the port details. This will enable the VC to connect to'
nl|'\n'
comment|'# that specific opaque network'
nl|'\n'
indent|'            '
name|'net_id'
op|'='
op|'('
name|'vif'
op|'.'
name|'get'
op|'('
string|"'details'"
op|')'
name|'and'
nl|'\n'
name|'vif'
op|'['
string|"'details'"
op|']'
op|'.'
name|'get'
op|'('
string|"'nsx-logical-switch-id'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'net_id'
op|':'
newline|'\n'
comment|'# Make use of the original one, in the event that the'
nl|'\n'
comment|'# plugin does not pass the aforementioned id'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'NSX Logical switch ID is not present. '"
nl|'\n'
string|"'Using network ID to attach to the '"
nl|'\n'
string|"'opaque network.'"
op|')'
op|')'
newline|'\n'
name|'net_id'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'use_external_id'
op|'='
name|'True'
newline|'\n'
name|'network_type'
op|'='
string|"'nsx.LogicalSwitch'"
newline|'\n'
dedent|''
name|'network_ref'
op|'='
op|'{'
string|"'type'"
op|':'
string|"'OpaqueNetwork'"
op|','
nl|'\n'
string|"'network-id'"
op|':'
name|'net_id'
op|','
nl|'\n'
string|"'network-type'"
op|':'
name|'network_type'
op|','
nl|'\n'
string|"'use-external-id'"
op|':'
name|'use_external_id'
op|'}'
newline|'\n'
dedent|''
name|'elif'
name|'vif'
op|'['
string|"'type'"
op|']'
op|'=='
name|'model'
op|'.'
name|'VIF_TYPE_DVS'
op|':'
newline|'\n'
comment|'# Port binding for DVS VIF types may pass the name'
nl|'\n'
comment|'# of the port group, so use it if present'
nl|'\n'
indent|'        '
name|'network_id'
op|'='
name|'vif'
op|'.'
name|'get'
op|'('
string|"'details'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'dvs_port_group_name'"
op|')'
newline|'\n'
name|'if'
name|'network_id'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# Make use of the original one, in the event that the'
nl|'\n'
comment|'# port binding does not provide this key in VIF details'
nl|'\n'
indent|'            '
name|'network_id'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
dedent|''
name|'network_ref'
op|'='
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
nl|'\n'
name|'session'
op|','
name|'network_id'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'network_ref'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFoundForBridge'
op|'('
name|'bridge'
op|'='
name|'network_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'vif'
op|'.'
name|'get'
op|'('
string|"'details'"
op|')'
name|'and'
name|'vif'
op|'['
string|"'details'"
op|']'
op|'.'
name|'get'
op|'('
string|"'dvs_port_key'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_ref'
op|'['
string|"'dvs_port_key'"
op|']'
op|'='
name|'vif'
op|'['
string|"'details'"
op|']'
op|'['
string|"'dvs_port_key'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'reason'
op|'='
name|'_'
op|'('
string|"'vif type %s not supported'"
op|')'
op|'%'
name|'vif'
op|'['
string|"'type'"
op|']'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_network_ref
dedent|''
name|'def'
name|'get_network_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'vif'
op|','
name|'is_neutron'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'is_neutron'
op|':'
newline|'\n'
indent|'        '
name|'network_ref'
op|'='
name|'_get_neutron_network'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'vif'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'create_vlan'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'.'
name|'get_meta'
op|'('
string|"'should_create_vlan'"
op|','
name|'False'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'ensure_vlan_bridge'
op|'('
name|'session'
op|','
name|'vif'
op|','
name|'cluster'
op|'='
name|'cluster'
op|','
nl|'\n'
name|'create_vlan'
op|'='
name|'create_vlan'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vif_dict
dedent|''
name|'def'
name|'get_vif_dict'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'vif_model'
op|','
name|'is_neutron'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'mac'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'name'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'bridge'"
op|']'
name|'or'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'integration_bridge'
newline|'\n'
name|'ref'
op|'='
name|'get_network_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'vif'
op|','
name|'is_neutron'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'network_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'mac'
op|','
nl|'\n'
string|"'network_ref'"
op|':'
name|'ref'
op|','
nl|'\n'
string|"'iface_id'"
op|':'
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'vif_model'"
op|':'
name|'vif_model'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vif_info
dedent|''
name|'def'
name|'get_vif_info'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'is_neutron'
op|','
name|'vif_model'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vif_infos'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'network_info'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'vif_infos'
newline|'\n'
dedent|''
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'        '
name|'vif_infos'
op|'.'
name|'append'
op|'('
name|'get_vif_dict'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'vif_model'
op|','
nl|'\n'
name|'is_neutron'
op|','
name|'vif'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'vif_infos'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_network_device
dedent|''
name|'def'
name|'get_network_device'
op|'('
name|'hardware_devices'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the network device with MAC \'mac_address\'."""'
newline|'\n'
name|'if'
name|'hardware_devices'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"ArrayOfVirtualDevice"'
op|':'
newline|'\n'
indent|'        '
name|'hardware_devices'
op|'='
name|'hardware_devices'
op|'.'
name|'VirtualDevice'
newline|'\n'
dedent|''
name|'for'
name|'device'
name|'in'
name|'hardware_devices'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
name|'in'
name|'vm_util'
op|'.'
name|'ALL_SUPPORTED_NETWORK_DEVICES'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'hasattr'
op|'('
name|'device'
op|','
string|"'macAddress'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'device'
op|'.'
name|'macAddress'
op|'=='
name|'mac_address'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'device'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
