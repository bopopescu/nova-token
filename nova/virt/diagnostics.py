begin_unit
comment|'# Copyright (c) 2014 VMware, Inc.'
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
nl|'\n'
DECL|class|CpuDiagnostics
name|'class'
name|'CpuDiagnostics'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'time'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new CpuDiagnostics object\n\n        :param time: CPU Time in nano seconds (Integer)\n        """'
newline|'\n'
name|'self'
op|'.'
name|'time'
op|'='
name|'time'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NicDiagnostics
dedent|''
dedent|''
name|'class'
name|'NicDiagnostics'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'mac_address'
op|'='
string|"'00:00:00:00:00:00'"
op|','
nl|'\n'
name|'rx_octets'
op|'='
number|'0'
op|','
name|'rx_errors'
op|'='
number|'0'
op|','
name|'rx_drop'
op|'='
number|'0'
op|','
name|'rx_packets'
op|'='
number|'0'
op|','
nl|'\n'
name|'tx_octets'
op|'='
number|'0'
op|','
name|'tx_errors'
op|'='
number|'0'
op|','
name|'tx_drop'
op|'='
number|'0'
op|','
name|'tx_packets'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new NicDiagnostics object\n\n        :param mac_address: Mac address of the interface (String)\n        :param rx_octets: Received octets (Integer)\n        :param rx_errors: Received errors (Integer)\n        :param rx_drop: Received packets dropped (Integer)\n        :param rx_packets: Received packets (Integer)\n        :param tx_octets: Transmitted Octets (Integer)\n        :param tx_errors: Transmit errors (Integer)\n        :param tx_drop: Transmit dropped packets (Integer)\n        :param tx_packets: Transmit packets (Integer)\n        """'
newline|'\n'
name|'self'
op|'.'
name|'mac_address'
op|'='
name|'mac_address'
newline|'\n'
name|'self'
op|'.'
name|'rx_octets'
op|'='
name|'rx_octets'
newline|'\n'
name|'self'
op|'.'
name|'rx_errors'
op|'='
name|'rx_errors'
newline|'\n'
name|'self'
op|'.'
name|'rx_drop'
op|'='
name|'rx_drop'
newline|'\n'
name|'self'
op|'.'
name|'rx_packets'
op|'='
name|'rx_packets'
newline|'\n'
name|'self'
op|'.'
name|'tx_octets'
op|'='
name|'tx_octets'
newline|'\n'
name|'self'
op|'.'
name|'tx_errors'
op|'='
name|'tx_errors'
newline|'\n'
name|'self'
op|'.'
name|'tx_drop'
op|'='
name|'tx_drop'
newline|'\n'
name|'self'
op|'.'
name|'tx_packets'
op|'='
name|'tx_packets'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DiskDiagnostics
dedent|''
dedent|''
name|'class'
name|'DiskDiagnostics'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'id'
op|'='
string|"''"
op|','
name|'read_bytes'
op|'='
number|'0'
op|','
name|'read_requests'
op|'='
number|'0'
op|','
nl|'\n'
name|'write_bytes'
op|'='
number|'0'
op|','
name|'write_requests'
op|'='
number|'0'
op|','
name|'errors_count'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new DiskDiagnostics object\n\n        :param id: Disk ID (String)\n        :param read_bytes: Disk reads in bytes(Integer)\n        :param read_requests: Read requests (Integer)\n        :param write_bytes: Disk writes in bytes (Integer)\n        :param write_requests: Write requests (Integer)\n        :param errors_count: Disk errors (Integer)\n        """'
newline|'\n'
name|'self'
op|'.'
name|'id'
op|'='
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'read_bytes'
op|'='
name|'read_bytes'
newline|'\n'
name|'self'
op|'.'
name|'read_requests'
op|'='
name|'read_requests'
newline|'\n'
name|'self'
op|'.'
name|'write_bytes'
op|'='
name|'write_bytes'
newline|'\n'
name|'self'
op|'.'
name|'write_requests'
op|'='
name|'write_requests'
newline|'\n'
name|'self'
op|'.'
name|'errors_count'
op|'='
name|'errors_count'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MemoryDiagnostics
dedent|''
dedent|''
name|'class'
name|'MemoryDiagnostics'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'maximum'
op|'='
number|'0'
op|','
name|'used'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new MemoryDiagnostics object\n\n        :param maximum: Amount of memory provisioned for the VM in MB (Integer)\n        :param used: Amount of memory used by the VM in MB (Integer)\n        """'
newline|'\n'
name|'self'
op|'.'
name|'maximum'
op|'='
name|'maximum'
newline|'\n'
name|'self'
op|'.'
name|'used'
op|'='
name|'used'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Diagnostics
dedent|''
dedent|''
name|'class'
name|'Diagnostics'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|version
indent|'    '
name|'version'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'state'
op|'='
name|'None'
op|','
name|'driver'
op|'='
name|'None'
op|','
name|'hypervisor_os'
op|'='
name|'None'
op|','
nl|'\n'
name|'uptime'
op|'='
number|'0'
op|','
name|'cpu_details'
op|'='
name|'None'
op|','
name|'nic_details'
op|'='
name|'None'
op|','
nl|'\n'
name|'disk_details'
op|'='
name|'None'
op|','
name|'config_drive'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new diagnostics object\n\n        :param state: The current state of the VM. Example values are:\n                      \'pending\', \'running\', \'paused\', \'shutdown\', \'crashed\',\n                      \'suspended\' and \'building\' (String)\n        :param driver: A string denoting the driver on which the VM is running.\n                       Examples may be: \'libvirt\', \'xenapi\', \'hyperv\' and\n                       \'vmwareapi\' (String)\n        :param hypervisor_os: A string denoting the hypervisor OS (String)\n        :param uptime: The amount of time in seconds that the VM has been\n                       running (Integer)\n        :param cpu_details: And array of CpuDiagnostics or None.\n        :param nic_details: And array of NicDiagnostics or None.\n        :param disk_details: And array of DiskDiagnostics or None.\n        :param config_drive: Indicates if the config drive is supported on the\n                             instance (Boolean)\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'state'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'hypervisor_os'
op|'='
name|'hypervisor_os'
newline|'\n'
name|'self'
op|'.'
name|'uptime'
op|'='
name|'uptime'
newline|'\n'
name|'self'
op|'.'
name|'config_drive'
op|'='
name|'config_drive'
newline|'\n'
name|'if'
name|'cpu_details'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cpu_details'
op|'='
name|'cpu_details'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cpu_details'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
name|'nic_details'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nic_details'
op|'='
name|'nic_details'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nic_details'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
name|'disk_details'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'disk_details'
op|'='
name|'disk_details'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'disk_details'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'memory_details'
op|'='
name|'MemoryDiagnostics'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
