begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nImplements vlans, bridges, and iptables rules using linux utilities.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
comment|'# todo(ja): does the definition of network_path belong here?'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
string|"'dhcpbridge_flagfile'"
op|','
nl|'\n'
string|"'/etc/nova/nova-dhcpbridge.conf'"
op|','
nl|'\n'
string|"'location of flagfile for dhcpbridge'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
name|'def'
name|'execute'
op|'('
name|'cmd'
op|','
name|'addl_env'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around utils.execute for fake_network"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_network'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"FAKE NET: %s"'
op|','
name|'cmd'
op|')'
newline|'\n'
name|'return'
string|'"fake"'
op|','
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|','
name|'addl_env'
op|'='
name|'addl_env'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|runthis
dedent|''
dedent|''
name|'def'
name|'runthis'
op|'('
name|'desc'
op|','
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around utils.runthis for fake_network"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_network'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'execute'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'runthis'
op|'('
name|'desc'
op|','
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|device_exists
dedent|''
dedent|''
name|'def'
name|'device_exists'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if ethernet device exists"""'
newline|'\n'
op|'('
name|'_out'
op|','
name|'err'
op|')'
op|'='
name|'execute'
op|'('
string|'"ifconfig %s"'
op|'%'
name|'device'
op|')'
newline|'\n'
name|'return'
name|'not'
name|'err'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|confirm_rule
dedent|''
name|'def'
name|'confirm_rule'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete and re-add iptables rule"""'
newline|'\n'
name|'execute'
op|'('
string|'"sudo iptables --delete %s"'
op|'%'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo iptables -I %s"'
op|'%'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_rule
dedent|''
name|'def'
name|'remove_rule'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove iptables rule"""'
newline|'\n'
name|'execute'
op|'('
string|'"sudo iptables --delete %s"'
op|'%'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bind_public_ip
dedent|''
name|'def'
name|'bind_public_ip'
op|'('
name|'public_ip'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Bind ip to an interface"""'
newline|'\n'
name|'runthis'
op|'('
string|'"Binding IP to interface: %s"'
op|','
nl|'\n'
string|'"sudo ip addr add %s dev %s"'
op|'%'
op|'('
name|'public_ip'
op|','
name|'interface'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unbind_public_ip
dedent|''
name|'def'
name|'unbind_public_ip'
op|'('
name|'public_ip'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unbind a public ip from an interface"""'
newline|'\n'
name|'runthis'
op|'('
string|'"Binding IP to interface: %s"'
op|','
nl|'\n'
string|'"sudo ip addr del %s dev %s"'
op|'%'
op|'('
name|'public_ip'
op|','
name|'interface'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vlan_create
dedent|''
name|'def'
name|'vlan_create'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a vlan on on a bridge device unless vlan already exists"""'
newline|'\n'
name|'if'
name|'not'
name|'device_exists'
op|'('
string|'"vlan%s"'
op|'%'
name|'net'
op|'['
string|"'vlan'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Starting VLAN inteface for %s network"'
op|','
op|'('
name|'net'
op|'['
string|"'vlan'"
op|']'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo vconfig set_name_type VLAN_PLUS_VID_NO_PAD"'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo vconfig add %s %s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'bridge_dev'
op|','
name|'net'
op|'['
string|"'vlan'"
op|']'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo ifconfig vlan%s up"'
op|'%'
op|'('
name|'net'
op|'['
string|"'vlan'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bridge_create
dedent|''
dedent|''
name|'def'
name|'bridge_create'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a bridge on a vlan unless it already exists"""'
newline|'\n'
name|'if'
name|'not'
name|'device_exists'
op|'('
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Starting Bridge inteface for %s network"'
op|','
op|'('
name|'net'
op|'['
string|"'vlan'"
op|']'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo brctl addbr %s"'
op|'%'
op|'('
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo brctl setfd %s 0"'
op|'%'
op|'('
name|'net'
op|'.'
name|'bridge_name'
op|')'
op|')'
newline|'\n'
comment|'# execute("sudo brctl setageing %s 10" % (net.bridge_name))'
nl|'\n'
name|'execute'
op|'('
string|'"sudo brctl stp %s off"'
op|'%'
op|'('
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo brctl addif %s vlan%s"'
op|'%'
op|'('
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|','
nl|'\n'
name|'net'
op|'['
string|"'vlan'"
op|']'
op|')'
op|')'
newline|'\n'
name|'if'
name|'net'
op|'.'
name|'bridge_gets_ip'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'('
string|'"sudo ifconfig %s %s broadcast %s netmask %s up"'
op|'%'
op|'('
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|','
name|'net'
op|'.'
name|'gateway'
op|','
name|'net'
op|'.'
name|'broadcast'
op|','
name|'net'
op|'.'
name|'netmask'
op|')'
op|')'
newline|'\n'
name|'confirm_rule'
op|'('
string|'"FORWARD --in-interface %s -j ACCEPT"'
op|'%'
nl|'\n'
op|'('
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'('
string|'"sudo ifconfig %s up"'
op|'%'
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_dnsmasq_cmd
dedent|''
dedent|''
dedent|''
name|'def'
name|'_dnsmasq_cmd'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds dnsmasq command"""'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|"'sudo -E dnsmasq'"
op|','
nl|'\n'
string|"' --strict-order'"
op|','
nl|'\n'
string|"' --bind-interfaces'"
op|','
nl|'\n'
string|"' --conf-file='"
op|','
nl|'\n'
string|"' --pid-file=%s'"
op|'%'
name|'dhcp_file'
op|'('
name|'net'
op|'['
string|"'vlan'"
op|']'
op|','
string|"'pid'"
op|')'
op|','
nl|'\n'
string|"' --listen-address=%s'"
op|'%'
name|'net'
op|'.'
name|'dhcp_listen_address'
op|','
nl|'\n'
string|"' --except-interface=lo'"
op|','
nl|'\n'
string|"' --dhcp-range=%s,static,600s'"
op|'%'
op|'('
name|'net'
op|'.'
name|'dhcp_range_start'
op|')'
op|','
nl|'\n'
string|"' --dhcp-hostsfile=%s'"
op|'%'
name|'dhcp_file'
op|'('
name|'net'
op|'['
string|"'vlan'"
op|']'
op|','
string|"'conf'"
op|')'
op|','
nl|'\n'
string|"' --dhcp-script=%s'"
op|'%'
name|'bin_file'
op|'('
string|"'nova-dhcpbridge'"
op|')'
op|','
nl|'\n'
string|"' --leasefile-ro'"
op|']'
newline|'\n'
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|host_dhcp
dedent|''
name|'def'
name|'host_dhcp'
op|'('
name|'network'
op|','
name|'host'
op|','
name|'mac'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a host string for a network, host, and mac"""'
newline|'\n'
comment|"# Logically, the idx of instances they've launched in this net"
nl|'\n'
name|'idx'
op|'='
name|'host'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'return'
string|'"%s,%s-%s-%s.novalocal,%s"'
op|'%'
op|'('
name|'mac'
op|','
name|'network'
op|'['
string|"'user_id'"
op|']'
op|','
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
name|'idx'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(ja): if the system has restarted or pid numbers have wrapped'
nl|'\n'
comment|'#           then you cannot be certain that the pid refers to the'
nl|'\n'
comment|'#           dnsmasq.  As well, sending a HUP only reloads the hostfile,'
nl|'\n'
comment|'#           so any configuration options (like dchp-range, vlan, ...)'
nl|'\n'
comment|"#           aren't reloaded"
nl|'\n'
DECL|function|start_dnsmasq
dedent|''
name|'def'
name|'start_dnsmasq'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""(Re)starts a dnsmasq server for a given network\n\n    if a dnsmasq instance is already running then send a HUP\n    signal causing it to reload, otherwise spawn a new instance\n    """'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'dhcp_file'
op|'('
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
string|"'conf'"
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'host_name'
name|'in'
name|'network'
op|'.'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
string|'"%s\\n"'
op|'%'
name|'host_dhcp'
op|'('
name|'network'
op|','
nl|'\n'
name|'host_name'
op|','
nl|'\n'
name|'network'
op|'.'
name|'hosts'
op|'['
name|'host_name'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'pid'
op|'='
name|'dnsmasq_pid_for'
op|'('
name|'network'
op|')'
newline|'\n'
nl|'\n'
comment|'# if dnsmasq is already running, then tell it to reload'
nl|'\n'
name|'if'
name|'pid'
op|':'
newline|'\n'
comment|'# TODO(ja): use "/proc/%d/cmdline" % (pid) to determine if pid refers'
nl|'\n'
comment|'#           correct dnsmasq process'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGHUP'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
comment|'# pylint: disable-msg=W0703'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Hupping dnsmasq threw %s"'
op|','
name|'exc'
op|')'
newline|'\n'
nl|'\n'
comment|'# otherwise delete the existing leases file and start dnsmasq'
nl|'\n'
dedent|''
dedent|''
name|'lease_file'
op|'='
name|'dhcp_file'
op|'('
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
string|"'leases'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'lease_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'lease_file'
op|')'
newline|'\n'
nl|'\n'
comment|'# FLAGFILE and DNSMASQ_INTERFACE in env'
nl|'\n'
dedent|''
name|'env'
op|'='
op|'{'
string|"'FLAGFILE'"
op|':'
name|'FLAGS'
op|'.'
name|'dhcpbridge_flagfile'
op|','
nl|'\n'
string|"'DNSMASQ_INTERFACE'"
op|':'
name|'network'
op|'['
string|"'bridge_name'"
op|']'
op|'}'
newline|'\n'
name|'execute'
op|'('
name|'_dnsmasq_cmd'
op|'('
name|'network'
op|')'
op|','
name|'addl_env'
op|'='
name|'env'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stop_dnsmasq
dedent|''
name|'def'
name|'stop_dnsmasq'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stops the dnsmasq instance for a given network"""'
newline|'\n'
name|'pid'
op|'='
name|'dnsmasq_pid_for'
op|'('
name|'network'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'pid'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGTERM'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
comment|'# pylint: disable-msg=W0703'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Killing dnsmasq threw %s"'
op|','
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|dhcp_file
dedent|''
dedent|''
dedent|''
name|'def'
name|'dhcp_file'
op|'('
name|'vlan'
op|','
name|'kind'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return path to a pid, leases or conf file for a vlan"""'
newline|'\n'
nl|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
string|'"%s/nova-%s.%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'networks_path'
op|','
name|'vlan'
op|','
name|'kind'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bin_file
dedent|''
name|'def'
name|'bin_file'
op|'('
name|'script'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the absolute path to scipt in the bin directory"""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'__file__'
op|','
string|'"../../../bin"'
op|','
name|'script'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|dnsmasq_pid_for
dedent|''
name|'def'
name|'dnsmasq_pid_for'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns he pid for prior dnsmasq instance for a vlan\n\n    Returns None if no pid file exists\n\n    If machine has rebooted pid might be incorrect (caller should check)\n    """'
newline|'\n'
nl|'\n'
name|'pid_file'
op|'='
name|'dhcp_file'
op|'('
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
string|"'pid'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pid_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'pid_file'
op|','
string|"'r'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
