begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'network_util'
newline|'\n'
nl|'\n'
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
string|"'vmwareapi_vlan_interface'"
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
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'vmwareapi_vif_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan_bridge
name|'def'
name|'ensure_vlan_bridge'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'vif'
op|','
name|'cluster'
op|'='
name|'None'
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
name|'vmwareapi_vlan_interface'
newline|'\n'
nl|'\n'
comment|'# Check if the vlan_interface physical network adapter exists on the'
nl|'\n'
comment|'# host.'
nl|'\n'
name|'if'
name|'not'
name|'network_util'
op|'.'
name|'check_if_vlan_interface_exists'
op|'('
name|'session'
op|','
nl|'\n'
name|'vlan_interface'
op|','
nl|'\n'
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
name|'vlan_interface'
op|')'
newline|'\n'
nl|'\n'
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
name|'vlan_interface'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'if'
name|'vswitch_associated'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'SwitchNotFoundForNetworkAdapter'
op|'('
nl|'\n'
name|'adapter'
op|'='
name|'vlan_interface'
op|')'
newline|'\n'
comment|'# Check whether bridge already exists and retrieve the the ref of the'
nl|'\n'
comment|'# network whose name_label is "bridge"'
nl|'\n'
dedent|''
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
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# Create a port group on the vSwitch associated with the'
nl|'\n'
comment|'# vlan_interface corresponding physical network adapter on the ESX'
nl|'\n'
comment|'# host.'
nl|'\n'
indent|'        '
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
name|'vlan_num'
op|','
nl|'\n'
name|'cluster'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Get the vlan id and vswitch corresponding to the port group'
nl|'\n'
indent|'        '
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
dedent|''
endmarker|''
end_unit
