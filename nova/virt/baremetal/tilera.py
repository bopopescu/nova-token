begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 University of Southern California'
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
string|'"""\nTilera back-end for bare-metal compute node provisioning\n\nThe details of this implementation are specific to ISI\'s testbed. This code\nis provided here as an example of how to implement a backend.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
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
DECL|variable|tilera_opts
name|'tilera_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'tile_monitor'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/usr/local/TileraMDE/bin/tile-monitor'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Tilera command line program for Bare-metal driver'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'tilera_opts'
op|')'
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
nl|'\n'
DECL|function|get_baremetal_nodes
name|'def'
name|'get_baremetal_nodes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'BareMetalNodes'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalNodes
dedent|''
name|'class'
name|'BareMetalNodes'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This manages node information and implements singleton.\n\n    BareMetalNodes class handles machine architectures of interest to\n    technical computing users have either poor or non-existent support\n    for virtualization.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_instance
name|'_instance'
op|'='
name|'None'
newline|'\n'
DECL|variable|_is_init
name|'_is_init'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|__new__
name|'def'
name|'__new__'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns the BareMetalNodes singleton.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'cls'
op|'.'
name|'_instance'
name|'or'
op|'('
string|"'new'"
name|'in'
name|'kwargs'
name|'and'
name|'kwargs'
op|'['
string|"'new'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'super'
op|'('
name|'BareMetalNodes'
op|','
name|'cls'
op|')'
op|'.'
name|'__new__'
op|'('
name|'cls'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'file_name'
op|'='
string|'"/tftpboot/tilera_boards"'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Only call __init__ the first time object is instantiated.\n\n        From the bare-metal node list file: /tftpboot/tilera_boards,\n        reads each item of each node such as node ID, IP address,\n        MAC address, vcpus, memory, hdd, hypervisor type/version, and cpu\n        and appends each node information into nodes list.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_is_init'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_is_init'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'nodes'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'BOARD_ID'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'IP_ADDR'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'MAC_ADDR'
op|'='
number|'2'
newline|'\n'
name|'self'
op|'.'
name|'VCPUS'
op|'='
number|'3'
newline|'\n'
name|'self'
op|'.'
name|'MEMORY_MB'
op|'='
number|'4'
newline|'\n'
name|'self'
op|'.'
name|'LOCAL_GB'
op|'='
number|'5'
newline|'\n'
name|'self'
op|'.'
name|'MEMORY_MB_USED'
op|'='
number|'6'
newline|'\n'
name|'self'
op|'.'
name|'LOCAL_GB_USED'
op|'='
number|'7'
newline|'\n'
name|'self'
op|'.'
name|'HYPERVISOR_TYPE'
op|'='
number|'8'
newline|'\n'
name|'self'
op|'.'
name|'HYPERVISOR_VER'
op|'='
number|'9'
newline|'\n'
name|'self'
op|'.'
name|'CPU_INFO'
op|'='
number|'10'
newline|'\n'
nl|'\n'
name|'fp'
op|'='
name|'open'
op|'('
name|'file_name'
op|','
string|'"r"'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'fp'
op|':'
newline|'\n'
indent|'            '
name|'l'
op|'='
name|'item'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'if'
name|'l'
op|'['
number|'0'
op|']'
op|'=='
string|"'#'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'l_d'
op|'='
op|'{'
string|"'node_id'"
op|':'
name|'int'
op|'('
name|'l'
op|'['
name|'self'
op|'.'
name|'BOARD_ID'
op|']'
op|')'
op|','
nl|'\n'
string|"'ip_addr'"
op|':'
name|'l'
op|'['
name|'self'
op|'.'
name|'IP_ADDR'
op|']'
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
name|'l'
op|'['
name|'self'
op|'.'
name|'MAC_ADDR'
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'int'
op|'('
name|'l'
op|'['
name|'self'
op|'.'
name|'VCPUS'
op|']'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'int'
op|'('
name|'l'
op|'['
name|'self'
op|'.'
name|'MEMORY_MB'
op|']'
op|')'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'int'
op|'('
name|'l'
op|'['
name|'self'
op|'.'
name|'LOCAL_GB'
op|']'
op|')'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'int'
op|'('
name|'l'
op|'['
name|'self'
op|'.'
name|'MEMORY_MB_USED'
op|']'
op|')'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'int'
op|'('
name|'l'
op|'['
name|'self'
op|'.'
name|'LOCAL_GB_USED'
op|']'
op|')'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
name|'l'
op|'['
name|'self'
op|'.'
name|'HYPERVISOR_TYPE'
op|']'
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'int'
op|'('
name|'l'
op|'['
name|'self'
op|'.'
name|'HYPERVISOR_VER'
op|']'
op|')'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
name|'l'
op|'['
name|'self'
op|'.'
name|'CPU_INFO'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'nodes'
op|'.'
name|'append'
op|'('
name|'l_d'
op|')'
newline|'\n'
dedent|''
name|'fp'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_hw_info
dedent|''
name|'def'
name|'get_hw_info'
op|'('
name|'self'
op|','
name|'field'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns hardware information of bare-metal node by the given field.\n\n        Given field can be vcpus, memory_mb, local_gb, memory_mb_used,\n        local_gb_used, hypervisor_type, hypervisor_version, and cpu_info.\n        """'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'self'
op|'.'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'node'
op|'['
string|"'node_id'"
op|']'
op|'=='
number|'9'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'field'
op|'=='
string|"'vcpus'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'memory_mb'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'local_gb'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'memory_mb_used'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'memory_mb_used'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'local_gb_used'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'local_gb_used'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'hypervisor_type'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'hypervisor_version'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'cpu_info'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'node'
op|'['
string|"'cpu_info'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|set_status
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'set_status'
op|'('
name|'self'
op|','
name|'node_id'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets status of the given node by the given status.\n\n        Returns 1 if the node is in the nodes list.\n        """'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'self'
op|'.'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'node'
op|'['
string|"'node_id'"
op|']'
op|'=='
name|'node_id'
op|':'
newline|'\n'
indent|'                '
name|'node'
op|'['
string|"'status'"
op|']'
op|'='
name|'status'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|get_status
dedent|''
name|'def'
name|'get_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Gets status of the given node.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_idle_node
dedent|''
name|'def'
name|'get_idle_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Gets an idle node, sets the status as 1 (RUNNING) and Returns node ID.\n        """'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'self'
op|'.'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|'['
string|"'status'"
op|']'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'['
string|"'status'"
op|']'
op|'='
number|'1'
comment|'# make status RUNNING'
newline|'\n'
name|'return'
name|'item'
op|'['
string|"'node_id'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"No free nodes available"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_ip_by_id
dedent|''
name|'def'
name|'get_ip_by_id'
op|'('
name|'self'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns default IP address of the given node.\n        """'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'self'
op|'.'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|'['
string|"'node_id'"
op|']'
op|'=='
name|'id'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'item'
op|'['
string|"'ip_addr'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|free_node
dedent|''
dedent|''
dedent|''
name|'def'
name|'free_node'
op|'('
name|'self'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets/frees status of the given node as 0 (IDLE).\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"free_node...."'
op|')'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'self'
op|'.'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|'['
string|"'node_id'"
op|']'
op|'=='
name|'str'
op|'('
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'['
string|"'status'"
op|']'
op|'='
number|'0'
comment|'# make status IDLE'
newline|'\n'
nl|'\n'
DECL|member|power_mgr
dedent|''
dedent|''
dedent|''
name|'def'
name|'power_mgr'
op|'('
name|'self'
op|','
name|'node_id'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Changes power state of the given node.\n\n        According to the mode (1-ON, 2-OFF, 3-REBOOT), power state can be\n        changed. /tftpboot/pdu_mgr script handles power management of\n        PDU (Power Distribution Unit).\n        """'
newline|'\n'
name|'if'
name|'node_id'
op|'<'
number|'5'
op|':'
newline|'\n'
indent|'            '
name|'pdu_num'
op|'='
number|'1'
newline|'\n'
name|'pdu_outlet_num'
op|'='
name|'node_id'
op|'+'
number|'5'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'pdu_num'
op|'='
number|'2'
newline|'\n'
name|'pdu_outlet_num'
op|'='
name|'node_id'
newline|'\n'
dedent|''
name|'path1'
op|'='
string|'"10.0.100."'
op|'+'
name|'str'
op|'('
name|'pdu_num'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'/tftpboot/pdu_mgr'"
op|','
name|'path1'
op|','
name|'str'
op|'('
name|'pdu_outlet_num'
op|')'
op|','
nl|'\n'
name|'str'
op|'('
name|'mode'
op|')'
op|','
string|"'>>'"
op|','
string|"'pdu_output'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|deactivate_node
dedent|''
name|'def'
name|'deactivate_node'
op|'('
name|'self'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Deactivates the given node by turnning it off.\n\n        /tftpboot/fs_x directory is a NFS of node#x\n        and /tftpboot/root_x file is an file system image of node#x.\n        """'
newline|'\n'
name|'node_ip'
op|'='
name|'self'
op|'.'
name|'get_ip_by_id'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"deactivate_node is called for "'
nl|'\n'
string|'"node_id = %(id)s node_ip = %(ip)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'str'
op|'('
name|'node_id'
op|')'
op|','
string|"'ip'"
op|':'
name|'node_ip'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'self'
op|'.'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|'['
string|"'node_id'"
op|']'
op|'=='
name|'node_id'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"status of node is set to 0"'
op|')'
op|')'
newline|'\n'
name|'item'
op|'['
string|"'status'"
op|']'
op|'='
number|'0'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'power_mgr'
op|'('
name|'node_id'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sleep_mgr'
op|'('
number|'5'
op|')'
newline|'\n'
name|'path'
op|'='
string|'"/tftpboot/fs_"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'pathx'
op|'='
string|'"/tftpboot/root_"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'/usr/sbin/rpc.mountd'"
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
string|"'sudo'"
op|','
string|"'umount'"
op|','
string|"'-f'"
op|','
name|'pathx'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'rm'"
op|','
string|"'-f'"
op|','
name|'pathx'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"rootfs is already removed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|network_set
dedent|''
dedent|''
name|'def'
name|'network_set'
op|'('
name|'self'
op|','
name|'node_ip'
op|','
name|'mac_address'
op|','
name|'ip_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets network configuration based on the given ip and mac address.\n\n        User can access the bare-metal node using ssh.\n        """'
newline|'\n'
name|'cmd'
op|'='
op|'('
name|'FLAGS'
op|'.'
name|'tile_monitor'
op|'+'
nl|'\n'
string|'" --resume --net "'
op|'+'
name|'node_ip'
op|'+'
string|'" --run - "'
op|'+'
nl|'\n'
string|'"ifconfig xgbe0 hw ether "'
op|'+'
name|'mac_address'
op|'+'
nl|'\n'
string|'" - --wait --run - ifconfig xgbe0 "'
op|'+'
name|'ip_address'
op|'+'
nl|'\n'
string|'" - --wait --quit"'
op|')'
newline|'\n'
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
comment|'#utils.execute(cmd, shell=True)'
nl|'\n'
name|'self'
op|'.'
name|'sleep_mgr'
op|'('
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|iptables_set
dedent|''
name|'def'
name|'iptables_set'
op|'('
name|'self'
op|','
name|'node_ip'
op|','
name|'user_data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets security setting (iptables:port) if needed.\n\n        iptables -A INPUT -p tcp ! -s $IP --dport $PORT -j DROP\n        /tftpboot/iptables_rule script sets iptables rule on the given node.\n        """'
newline|'\n'
name|'if'
name|'user_data'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'open_ip'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'user_data'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'/tftpboot/iptables_rule'"
op|','
name|'node_ip'
op|','
name|'open_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_activated
dedent|''
dedent|''
name|'def'
name|'check_activated'
op|'('
name|'self'
op|','
name|'node_id'
op|','
name|'node_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Checks whether the given node is activated or not.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Before ping to the bare-metal node"'
op|')'
op|')'
newline|'\n'
name|'tile_output'
op|'='
string|'"/tftpboot/tile_output_"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'grep_cmd'
op|'='
op|'('
string|'"ping -c1 "'
op|'+'
name|'node_ip'
op|'+'
string|'" | grep Unreachable > "'
op|'+'
nl|'\n'
name|'tile_output'
op|')'
newline|'\n'
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'grep_cmd'
op|','
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sleep_mgr'
op|'('
number|'5'
op|')'
newline|'\n'
nl|'\n'
name|'file'
op|'='
name|'open'
op|'('
name|'tile_output'
op|','
string|'"r"'
op|')'
newline|'\n'
name|'out_msg'
op|'='
name|'file'
op|'.'
name|'readline'
op|'('
op|')'
op|'.'
name|'find'
op|'('
string|'"Unreachable"'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'rm'"
op|','
name|'tile_output'
op|')'
newline|'\n'
name|'if'
name|'out_msg'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
op|'('
string|'"TILERA_BOARD_#"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
op|'+'
string|'" "'
op|'+'
name|'node_ip'
op|'+'
nl|'\n'
string|'" is ready"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
op|'('
string|'"TILERA_BOARD_#"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
op|'+'
string|'" "'
op|'+'
nl|'\n'
name|'node_ip'
op|'+'
string|'" is not ready, out_msg="'
op|'+'
name|'out_msg'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'power_mgr'
op|'('
name|'node_id'
op|','
number|'2'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|vmlinux_set
dedent|''
dedent|''
name|'def'
name|'vmlinux_set'
op|'('
name|'self'
op|','
name|'node_id'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets kernel into default path (/tftpboot) if needed.\n\n        From basepath to /tftpboot, kernel is set based on the given mode\n        such as 0-NoSet, 1-SetVmlinux, or 9-RemoveVmlinux.\n        """'
newline|'\n'
name|'cmd'
op|'='
string|'"Noting to do for tilera nodes: vmlinux is in CF"'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|sleep_mgr
dedent|''
name|'def'
name|'sleep_mgr'
op|'('
name|'self'
op|','
name|'time_in_seconds'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sleeps until the node is activated.\n        """'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'time_in_seconds'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ssh_set
dedent|''
name|'def'
name|'ssh_set'
op|'('
name|'self'
op|','
name|'node_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets and Runs sshd in the node.\n        """'
newline|'\n'
name|'cmd'
op|'='
op|'('
name|'FLAGS'
op|'.'
name|'tile_monitor'
op|'+'
nl|'\n'
string|'" --resume --net "'
op|'+'
name|'node_ip'
op|'+'
string|'" --run - "'
op|'+'
nl|'\n'
string|'"/usr/sbin/sshd - --wait --quit"'
op|')'
newline|'\n'
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sleep_mgr'
op|'('
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|activate_node
dedent|''
name|'def'
name|'activate_node'
op|'('
name|'self'
op|','
name|'node_id'
op|','
name|'node_ip'
op|','
name|'name'
op|','
name|'mac_address'
op|','
nl|'\n'
name|'ip_address'
op|','
name|'user_data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Activates the given node using ID, IP, and MAC address.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"activate_node"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'power_mgr'
op|'('
name|'node_id'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'power_mgr'
op|'('
name|'node_id'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sleep_mgr'
op|'('
number|'100'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'check_activated'
op|'('
name|'node_id'
op|','
name|'node_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_set'
op|'('
name|'node_ip'
op|','
name|'mac_address'
op|','
name|'ip_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ssh_set'
op|'('
name|'node_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables_set'
op|'('
name|'node_ip'
op|','
name|'user_data'
op|')'
newline|'\n'
name|'return'
name|'power_state'
op|'.'
name|'RUNNING'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'deactivate_node'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Node is unknown error state."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'console_log'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Gets console output of the given node.\n        """'
newline|'\n'
name|'node_ip'
op|'='
name|'self'
op|'.'
name|'get_ip_by_id'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'log_path'
op|'='
string|'"/tftpboot/log_"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'kmsg_cmd'
op|'='
op|'('
name|'FLAGS'
op|'.'
name|'tile_monitor'
op|'+'
nl|'\n'
string|'" --resume --net "'
op|'+'
name|'node_ip'
op|'+'
nl|'\n'
string|'" -- dmesg > "'
op|'+'
name|'log_path'
op|')'
newline|'\n'
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'kmsg_cmd'
op|','
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sleep_mgr'
op|'('
number|'5'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cp'"
op|','
name|'log_path'
op|','
name|'console_log'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_image
dedent|''
name|'def'
name|'get_image'
op|'('
name|'self'
op|','
name|'bp'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Gets the bare-metal file system image into the instance path.\n\n        Noting to do for tilera nodes: actual image is used.\n        """'
newline|'\n'
name|'path_fs'
op|'='
string|'"/tftpboot/tilera_fs"'
newline|'\n'
name|'path_root'
op|'='
name|'bp'
op|'+'
string|'"/root"'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cp'"
op|','
name|'path_fs'
op|','
name|'path_root'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_image
dedent|''
name|'def'
name|'set_image'
op|'('
name|'self'
op|','
name|'bpath'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets the PXE bare-metal file system from the instance path.\n\n        This should be done after ssh key is injected.\n        /tftpboot/fs_x directory is a NFS of node#x.\n        /tftpboot/root_x file is an file system image of node#x.\n        """'
newline|'\n'
name|'path1'
op|'='
name|'bpath'
op|'+'
string|'"/root"'
newline|'\n'
name|'pathx'
op|'='
string|'"/tftpboot/root_"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'path2'
op|'='
string|'"/tftpboot/fs_"'
op|'+'
name|'str'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'mv'"
op|','
name|'path1'
op|','
name|'pathx'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'mount'"
op|','
string|"'-o'"
op|','
string|"'loop'"
op|','
name|'pathx'
op|','
name|'path2'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
