begin_unit
comment|'# Copyright 2012 Cloudbase Solutions Srl'
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
string|'"""\nConstants used in ops classes\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'os_win'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'units'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'arch'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
nl|'\n'
DECL|variable|HYPERV_POWER_STATE
name|'HYPERV_POWER_STATE'
op|'='
op|'{'
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_DISABLED'
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_SHUTTING_DOWN'
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
op|':'
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_PAUSED'
op|':'
name|'power_state'
op|'.'
name|'PAUSED'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_SUSPENDED'
op|':'
name|'power_state'
op|'.'
name|'SUSPENDED'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|WMI_WIN32_PROCESSOR_ARCHITECTURE
name|'WMI_WIN32_PROCESSOR_ARCHITECTURE'
op|'='
op|'{'
nl|'\n'
name|'constants'
op|'.'
name|'ARCH_I686'
op|':'
name|'arch'
op|'.'
name|'I686'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'ARCH_MIPS'
op|':'
name|'arch'
op|'.'
name|'MIPS'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'ARCH_ALPHA'
op|':'
name|'arch'
op|'.'
name|'ALPHA'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'ARCH_PPC'
op|':'
name|'arch'
op|'.'
name|'PPC'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'ARCH_ARMV7'
op|':'
name|'arch'
op|'.'
name|'ARMV7'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'ARCH_IA64'
op|':'
name|'arch'
op|'.'
name|'IA64'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'ARCH_X86_64'
op|':'
name|'arch'
op|'.'
name|'X86_64'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CTRL_TYPE_IDE
name|'CTRL_TYPE_IDE'
op|'='
string|'"IDE"'
newline|'\n'
DECL|variable|CTRL_TYPE_SCSI
name|'CTRL_TYPE_SCSI'
op|'='
string|'"SCSI"'
newline|'\n'
nl|'\n'
DECL|variable|DISK
name|'DISK'
op|'='
string|'"VHD"'
newline|'\n'
DECL|variable|DISK_FORMAT
name|'DISK_FORMAT'
op|'='
name|'DISK'
newline|'\n'
DECL|variable|DVD
name|'DVD'
op|'='
string|'"DVD"'
newline|'\n'
DECL|variable|DVD_FORMAT
name|'DVD_FORMAT'
op|'='
string|'"ISO"'
newline|'\n'
nl|'\n'
DECL|variable|DISK_FORMAT_MAP
name|'DISK_FORMAT_MAP'
op|'='
op|'{'
nl|'\n'
name|'DISK_FORMAT'
op|'.'
name|'lower'
op|'('
op|')'
op|':'
name|'DISK'
op|','
nl|'\n'
name|'DVD_FORMAT'
op|'.'
name|'lower'
op|'('
op|')'
op|':'
name|'DVD'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|DISK_FORMAT_VHD
name|'DISK_FORMAT_VHD'
op|'='
string|'"VHD"'
newline|'\n'
DECL|variable|DISK_FORMAT_VHDX
name|'DISK_FORMAT_VHDX'
op|'='
string|'"VHDX"'
newline|'\n'
nl|'\n'
DECL|variable|HOST_POWER_ACTION_SHUTDOWN
name|'HOST_POWER_ACTION_SHUTDOWN'
op|'='
string|'"shutdown"'
newline|'\n'
DECL|variable|HOST_POWER_ACTION_REBOOT
name|'HOST_POWER_ACTION_REBOOT'
op|'='
string|'"reboot"'
newline|'\n'
DECL|variable|HOST_POWER_ACTION_STARTUP
name|'HOST_POWER_ACTION_STARTUP'
op|'='
string|'"startup"'
newline|'\n'
nl|'\n'
DECL|variable|IMAGE_PROP_VM_GEN_1
name|'IMAGE_PROP_VM_GEN_1'
op|'='
string|'"hyperv-gen1"'
newline|'\n'
DECL|variable|IMAGE_PROP_VM_GEN_2
name|'IMAGE_PROP_VM_GEN_2'
op|'='
string|'"hyperv-gen2"'
newline|'\n'
nl|'\n'
DECL|variable|VM_GEN_1
name|'VM_GEN_1'
op|'='
number|'1'
newline|'\n'
DECL|variable|VM_GEN_2
name|'VM_GEN_2'
op|'='
number|'2'
newline|'\n'
nl|'\n'
DECL|variable|SERIAL_CONSOLE_BUFFER_SIZE
name|'SERIAL_CONSOLE_BUFFER_SIZE'
op|'='
number|'4'
op|'*'
name|'units'
op|'.'
name|'Ki'
newline|'\n'
endmarker|''
end_unit
