begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (C) 2013 Red Hat, Inc.'
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
string|'"""\nPolicy based configuration of libvirt objects\n\nThis module provides helper APIs for populating the config.py\nclasses based on common operational needs / policies\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_guest_frontend_config
name|'def'
name|'set_vif_guest_frontend_config'
op|'('
name|'conf'
op|','
name|'mac'
op|','
name|'model'
op|','
name|'driver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with guest frontend details"""'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mac'
newline|'\n'
name|'if'
name|'model'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'model'
op|'='
name|'model'
newline|'\n'
dedent|''
name|'if'
name|'driver'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'driver_name'
op|'='
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_bridge_config
dedent|''
dedent|''
name|'def'
name|'set_vif_host_backend_bridge_config'
op|'('
name|'conf'
op|','
name|'brname'
op|','
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for a software bridge"""'
newline|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'brname'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
dedent|''
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_ethernet_config
dedent|''
name|'def'
name|'set_vif_host_backend_ethernet_config'
op|'('
name|'conf'
op|','
name|'tapname'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an externally configured\n    host device.\n\n    NB use of this configuration is discouraged by\n    libvirt project and will mark domains as \'tainted\'"""'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"ethernet"'
newline|'\n'
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_ovs_config
dedent|''
name|'def'
name|'set_vif_host_backend_ovs_config'
op|'('
name|'conf'
op|','
name|'brname'
op|','
name|'interfaceid'
op|','
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an OpenVSwitch bridge"""'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'brname'
newline|'\n'
name|'conf'
op|'.'
name|'vporttype'
op|'='
string|'"openvswitch"'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"interfaceid"'
op|','
name|'interfaceid'
op|')'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
dedent|''
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_802qbg_config
dedent|''
name|'def'
name|'set_vif_host_backend_802qbg_config'
op|'('
name|'conf'
op|','
name|'devname'
op|','
name|'managerid'
op|','
nl|'\n'
name|'typeid'
op|','
name|'typeidversion'
op|','
nl|'\n'
name|'instanceid'
op|','
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an 802.1qbg device"""'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"direct"'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'devname'
newline|'\n'
name|'conf'
op|'.'
name|'source_mode'
op|'='
string|'"vepa"'
newline|'\n'
name|'conf'
op|'.'
name|'vporttype'
op|'='
string|'"802.1Qbg"'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"managerid"'
op|','
name|'managerid'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"typeid"'
op|','
name|'typeid'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"typeidversion"'
op|','
name|'typeidversion'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"instanceid"'
op|','
name|'instanceid'
op|')'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_802qbh_config
dedent|''
dedent|''
name|'def'
name|'set_vif_host_backend_802qbh_config'
op|'('
name|'conf'
op|','
name|'devname'
op|','
name|'profileid'
op|','
nl|'\n'
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an 802.1qbh device"""'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"direct"'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'devname'
newline|'\n'
name|'conf'
op|'.'
name|'source_mode'
op|'='
string|'"vepa"'
newline|'\n'
name|'conf'
op|'.'
name|'vporttype'
op|'='
string|'"802.1Qbh"'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"profileid"'
op|','
name|'profileid'
op|')'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_filter_config
dedent|''
dedent|''
name|'def'
name|'set_vif_host_backend_filter_config'
op|'('
name|'conf'
op|','
name|'name'
op|','
nl|'\n'
name|'primary_addr'
op|','
nl|'\n'
name|'dhcp_server'
op|'='
name|'None'
op|','
nl|'\n'
name|'ra_server'
op|'='
name|'None'
op|','
nl|'\n'
name|'allow_same_net'
op|'='
name|'False'
op|','
nl|'\n'
name|'ipv4_cidr'
op|'='
name|'None'
op|','
nl|'\n'
name|'ipv6_cidr'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for traffic filtering"""'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'filtername'
op|'='
name|'name'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"IP"'
op|','
name|'primary_addr'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'dhcp_server'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"DHCPSERVER"'
op|','
name|'dhcp_server'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ra_server'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"RASERVER"'
op|','
name|'ra_server'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'allow_same_net'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ipv4_cidr'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|','
name|'mask'
op|'='
name|'netutils'
op|'.'
name|'get_net_and_mask'
op|'('
name|'ipv4_cidr'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJNET"'
op|','
name|'net'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJMASK"'
op|','
name|'mask'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ipv6_cidr'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|','
name|'prefix'
op|'='
name|'netutils'
op|'.'
name|'get_net_and_prefixlen'
op|'('
name|'ipv6_cidr'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJNET6"'
op|','
name|'net'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJMASK6"'
op|','
name|'prefix'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
