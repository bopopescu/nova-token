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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'netutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vif'
name|'import'
name|'VIFDriver'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.virt.libvirt.vif'"
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
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_ovs_bridge'"
op|','
string|"'br-int'"
op|','
nl|'\n'
string|"'Name of Integration Bridge used by Open vSwitch'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtBridgeDriver
name|'class'
name|'LibvirtBridgeDriver'
op|'('
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
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a dictionary of VIF configurations for bridge type."""'
newline|'\n'
comment|'# Assume that the gateway also acts as the dhcp server.'
nl|'\n'
name|'gateway_v6'
op|'='
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'gateway_v6'"
op|')'
newline|'\n'
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
name|'if'
name|'FLAGS'
op|'.'
name|'allow_same_net_traffic'
op|':'
newline|'\n'
indent|'            '
name|'template'
op|'='
string|'"<parameter name=\\"%s\\"value=\\"%s\\" />\\n"'
newline|'\n'
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
name|'values'
op|'='
op|'['
op|'('
string|'"PROJNET"'
op|','
name|'net'
op|')'
op|','
op|'('
string|'"PROJMASK"'
op|','
name|'mask'
op|')'
op|']'
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
name|'values'
op|'.'
name|'extend'
op|'('
op|'['
op|'('
string|'"PROJNETV6"'
op|','
name|'net_v6'
op|')'
op|','
nl|'\n'
op|'('
string|'"PROJMASKV6"'
op|','
name|'prefixlen_v6'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'extra_params'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
op|'['
name|'template'
op|'%'
name|'value'
name|'for'
name|'value'
name|'in'
name|'values'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'extra_params'
op|'='
string|'"\\n"'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'mac_id'
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|','
nl|'\n'
string|"'ip_address'"
op|':'
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
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'mapping'
op|'['
string|"'dhcp_server'"
op|']'
op|','
nl|'\n'
string|"'extra_params'"
op|':'
name|'extra_params'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'gateway_v6'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'['
string|"'gateway_v6'"
op|']'
op|'='
name|'gateway_v6'
op|'+'
string|'"/128"'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
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
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
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
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
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
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch."""'
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
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
op|'{'
nl|'\n'
string|"'script'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'name'"
op|':'
name|'dev'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'result'
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
name|'warning'
op|'('
name|'_'
op|'('
string|'"Failed while unplugging vif of instance \'%s\'"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
