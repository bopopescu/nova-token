begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (C) 2011 Midokura KK'
nl|'\n'
comment|'# Copyright (C) 2011 Nicira, Inc'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""VIF drivers for libvirt."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
op|'.'
name|'network'
name|'import'
name|'linux_net'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'vif'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
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
DECL|variable|libvirt_vif_opts
name|'libvirt_vif_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'libvirt_ovs_bridge'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'br-int'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of Integration Bridge used by Open vSwitch'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'libvirt_use_virtio_for_bridges'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use virtio for bridge interfaces'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'libvirt_vif_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtBridgeDriver
name|'class'
name|'LibvirtBridgeDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Linux bridge."""'
newline|'\n'
nl|'\n'
DECL|member|_get_configurations
name|'def'
name|'_get_configurations'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a dictionary of VIF configurations for bridge type."""'
newline|'\n'
nl|'\n'
name|'mac_id'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'network'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'libvirt_use_virtio_for_bridges'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
nl|'\n'
dedent|''
name|'conf'
op|'.'
name|'filtername'
op|'='
string|'"nova-instance-"'
op|'+'
name|'instance'
op|'['
string|"'name'"
op|']'
op|'+'
string|'"-"'
op|'+'
name|'mac_id'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"IP"'
op|','
name|'mapping'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"DHCPSERVER"'
op|','
name|'mapping'
op|'['
string|"'dhcp_server'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"RASERVER"'
op|','
nl|'\n'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'gateway_v6'"
op|')'
op|'+'
string|'"/128"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'allow_same_net_traffic'
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
name|'network'
op|'['
string|"'cidr'"
op|']'
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
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                '
name|'net_v6'
op|','
name|'prefixlen_v6'
op|'='
name|'netutils'
op|'.'
name|'get_net_and_prefixlen'
op|'('
nl|'\n'
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJNET6"'
op|','
name|'net_v6'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJMASK6"'
op|','
name|'prefixlen_v6'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that the bridge exists, and add VIF to it."""'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'network'
op|'.'
name|'get'
op|'('
string|"'multi_host'"
op|')'
name|'and'
nl|'\n'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'should_create_bridge'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'should_create_vlan'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'iface'
op|'='
name|'FLAGS'
op|'.'
name|'vlan_interface'
name|'or'
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ensuring vlan %(vlan)s and bridge %(bridge)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'vlan'"
op|':'
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'LinuxBridgeInterfaceDriver'
op|'.'
name|'ensure_vlan_bridge'
op|'('
nl|'\n'
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
nl|'\n'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'iface'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'iface'
op|'='
name|'FLAGS'
op|'.'
name|'flat_interface'
name|'or'
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Ensuring bridge %s"'
op|')'
op|','
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'LinuxBridgeInterfaceDriver'
op|'.'
name|'ensure_bridge'
op|'('
nl|'\n'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'iface'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_get_configurations'
op|'('
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
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
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No manual unplugging required."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtOpenVswitchDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtOpenVswitchDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch that uses type=\'ethernet\'\n       libvirt XML.  Used for libvirt versions that do not support\n       OVS virtual port XML (0.9.10 or earlier)."""'
newline|'\n'
nl|'\n'
DECL|member|get_dev_name
name|'def'
name|'get_dev_name'
op|'('
name|'_self'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"tap"'
op|'+'
name|'iface_id'
op|'['
number|'0'
op|':'
number|'11'
op|']'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'iface_id'
op|'='
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_dev_name'
op|'('
name|'iface_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'linux_net'
op|'.'
name|'_device_exists'
op|'('
name|'dev'
op|')'
op|':'
newline|'\n'
comment|"# Older version of the command 'ip' from the iproute2 package"
nl|'\n'
comment|"# don't have support for the tuntap option (lp:882568).  If it"
nl|'\n'
comment|"# turns out we're on an old version we work around this by using"
nl|'\n'
comment|'# tunctl.'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|"# First, try with 'ip'"
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'tuntap'"
op|','
string|"'add'"
op|','
name|'dev'
op|','
string|"'mode'"
op|','
string|"'tap'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
comment|'# Second option: tunctl'
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tunctl'"
op|','
string|"'-b'"
op|','
string|"'-t'"
op|','
name|'dev'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'set'"
op|','
name|'dev'
op|','
string|"'up'"
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ovs-vsctl'"
op|','
string|"'--'"
op|','
string|"'--may-exist'"
op|','
string|"'add-port'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'libvirt_ovs_bridge'
op|','
name|'dev'
op|','
nl|'\n'
string|"'--'"
op|','
string|"'set'"
op|','
string|"'Interface'"
op|','
name|'dev'
op|','
nl|'\n'
string|'"external-ids:iface-id=%s"'
op|'%'
name|'iface_id'
op|','
nl|'\n'
string|"'--'"
op|','
string|"'set'"
op|','
string|"'Interface'"
op|','
name|'dev'
op|','
nl|'\n'
string|'"external-ids:iface-status=active"'
op|','
nl|'\n'
string|"'--'"
op|','
string|"'set'"
op|','
string|"'Interface'"
op|','
name|'dev'
op|','
nl|'\n'
string|'"external-ids:attached-mac=%s"'
op|'%'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|','
nl|'\n'
string|"'--'"
op|','
string|"'set'"
op|','
string|"'Interface'"
op|','
name|'dev'
op|','
nl|'\n'
string|'"external-ids:vm-uuid=%s"'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
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
name|'dev'
newline|'\n'
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'conf'
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
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unplug the VIF from the network by deleting the port from\n        the bridge."""'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_dev_name'
op|'('
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ovs-vsctl'"
op|','
string|"'del-port'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'libvirt_ovs_bridge'
op|','
name|'dev'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'delete'"
op|','
name|'dev'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed while unplugging vif"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtOpenVswitchVirtualPortDriver
dedent|''
dedent|''
dedent|''
name|'class'
name|'LibvirtOpenVswitchVirtualPortDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch that uses integrated libvirt\n       OVS virtual port XML (introduced in libvirt 0.9.11)."""'
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
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Pass data required to create OVS virtual port element"""'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
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
name|'FLAGS'
op|'.'
name|'libvirt_ovs_bridge'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'libvirt_use_virtio_for_bridges'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
dedent|''
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
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'conf'
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
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No action needed.  Libvirt takes care of cleanup"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumLinuxBridgeVIFDriver
dedent|''
dedent|''
name|'class'
name|'QuantumLinuxBridgeVIFDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Linux Bridge when running Quantum."""'
newline|'\n'
nl|'\n'
DECL|member|get_dev_name
name|'def'
name|'get_dev_name'
op|'('
name|'self'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"tap"'
op|'+'
name|'iface_id'
op|'['
number|'0'
op|':'
number|'11'
op|']'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'iface_id'
op|'='
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_dev_name'
op|'('
name|'iface_id'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'QuantumLinuxBridgeInterfaceDriver'
op|'.'
name|'create_tap_dev'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
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
name|'dev'
newline|'\n'
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'conf'
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
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unplug the VIF from the network by deleting the port from\n        the bridge."""'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_dev_name'
op|'('
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'delete'"
op|','
name|'dev'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Failed while unplugging vif"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
