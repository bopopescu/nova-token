begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nHelper methods for operations related to the management of VM records and\ntheir attributes like VDIs, VIFs, as well as their lookup functions.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'pickle'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
name|'import'
name|'AuthManager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
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
name|'virt'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'HelperBase'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'volume_utils'
name|'import'
name|'StorageError'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|XENAPI_POWER_STATE
name|'XENAPI_POWER_STATE'
op|'='
op|'{'
nl|'\n'
string|"'Halted'"
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
string|"'Running'"
op|':'
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
string|"'Paused'"
op|':'
name|'power_state'
op|'.'
name|'PAUSED'
op|','
nl|'\n'
string|"'Suspended'"
op|':'
name|'power_state'
op|'.'
name|'SUSPENDED'
op|','
nl|'\n'
string|"'Crashed'"
op|':'
name|'power_state'
op|'.'
name|'CRASHED'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageType
name|'class'
name|'ImageType'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Enumeration class for distinguishing different image types\n            0 - kernel/ramdisk image (goes on dom0\'s filesystem)\n            1 - disk image (local SR, partitioned by objectstore plugin)\n            2 - raw disk image (local SR, NOT partitioned by plugin)\n        """'
newline|'\n'
nl|'\n'
DECL|variable|KERNEL_RAMDISK
name|'KERNEL_RAMDISK'
op|'='
number|'0'
newline|'\n'
DECL|variable|DISK
name|'DISK'
op|'='
number|'1'
newline|'\n'
DECL|variable|DISK_RAW
name|'DISK_RAW'
op|'='
number|'2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMHelper
dedent|''
name|'class'
name|'VMHelper'
op|'('
name|'HelperBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The class that wraps the helper methods together.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_vm
name|'def'
name|'create_vm'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'kernel'
op|','
name|'ramdisk'
op|','
name|'pv_kernel'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VM record.  Returns a Deferred that gives the new\n        VM reference.\n        the pv_kernel flag indicates whether the guest is HVM or PV\n        """'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'instance'
op|'.'
name|'instance_type'
op|']'
newline|'\n'
name|'mem'
op|'='
name|'str'
op|'('
name|'long'
op|'('
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
newline|'\n'
name|'vcpus'
op|'='
name|'str'
op|'('
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'rec'
op|'='
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'instance'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'name_description'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'is_a_template'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_static_min'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'memory_static_max'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'memory_dynamic_min'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'memory_dynamic_max'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'VCPUs_at_startup'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'VCPUs_max'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'VCPUs_params'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'actions_after_shutdown'"
op|':'
string|"'destroy'"
op|','
nl|'\n'
string|"'actions_after_reboot'"
op|':'
string|"'restart'"
op|','
nl|'\n'
string|"'actions_after_crash'"
op|':'
string|"'destroy'"
op|','
nl|'\n'
string|"'PV_bootloader'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_kernel'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_ramdisk'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_args'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_bootloader_args'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_legacy_args'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'HVM_boot_policy'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'HVM_boot_params'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'platform'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'PCI_bus'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'recommendations'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'affinity'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'user_version'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
comment|'#Complete VM configuration record according to the image type'
nl|'\n'
comment|'#non-raw/raw with PV kernel/raw in HVM mode'
nl|'\n'
name|'if'
name|'instance'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'rec'
op|'['
string|"'PV_bootloader'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'rec'
op|'['
string|"'PV_kernel'"
op|']'
op|'='
name|'kernel'
newline|'\n'
name|'rec'
op|'['
string|"'PV_ramdisk'"
op|']'
op|'='
name|'ramdisk'
newline|'\n'
name|'rec'
op|'['
string|"'PV_args'"
op|']'
op|'='
string|"'root=/dev/xvda1'"
newline|'\n'
name|'rec'
op|'['
string|"'PV_bootloader_args'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'rec'
op|'['
string|"'PV_legacy_args'"
op|']'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'pv_kernel'
op|':'
newline|'\n'
indent|'                '
name|'rec'
op|'['
string|"'PV_args'"
op|']'
op|'='
string|"'noninteractive'"
newline|'\n'
name|'rec'
op|'['
string|"'PV_bootloader'"
op|']'
op|'='
string|"'pygrub'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'rec'
op|'['
string|"'HVM_boot_policy'"
op|']'
op|'='
string|"'BIOS order'"
newline|'\n'
name|'rec'
op|'['
string|"'HVM_boot_params'"
op|']'
op|'='
op|'{'
string|"'order'"
op|':'
string|"'dc'"
op|'}'
newline|'\n'
name|'rec'
op|'['
string|"'platform'"
op|']'
op|'='
op|'{'
string|"'acpi'"
op|':'
string|"'true'"
op|','
string|"'apic'"
op|':'
string|"'true'"
op|','
nl|'\n'
string|"'pae'"
op|':'
string|"'true'"
op|','
string|"'viridian'"
op|':'
string|"'true'"
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VM %s...'"
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'vm_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VM.create'"
op|','
name|'rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created VM %s as %s.'"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'return'
name|'vm_ref'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_vbd
name|'def'
name|'create_vbd'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
name|'userdevice'
op|','
name|'bootable'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VBD record.  Returns a Deferred that gives the new\n        VBD reference."""'
newline|'\n'
name|'vbd_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VDI'"
op|']'
op|'='
name|'vdi_ref'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'userdevice'"
op|']'
op|'='
name|'str'
op|'('
name|'userdevice'
op|')'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'bootable'"
op|']'
op|'='
name|'bootable'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'mode'"
op|']'
op|'='
string|"'RW'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'type'"
op|']'
op|'='
string|"'disk'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'unpluggable'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'empty'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_supported_algorithms'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating VBD for VM %s, VDI %s ... '"
op|')'
op|','
nl|'\n'
name|'vm_ref'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'vbd_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VBD.create'"
op|','
name|'vbd_rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created VBD %s for VM %s, VDI %s.'"
op|')'
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'vdi_ref'
op|')'
newline|'\n'
name|'return'
name|'vbd_ref'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_vbd_by_number
name|'def'
name|'find_vbd_by_number'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm_ref'
op|','
name|'number'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the VBD reference from the device number"""'
newline|'\n'
name|'vbds'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_VBDs'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'if'
name|'vbds'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'vbd'
name|'in'
name|'vbds'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'vbd_rec'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VBD'
op|'.'
name|'get_record'
op|'('
name|'vbd'
op|')'
newline|'\n'
name|'if'
name|'vbd_rec'
op|'['
string|"'userdevice'"
op|']'
op|'=='
name|'str'
op|'('
name|'number'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'return'
name|'vbd'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'raise'
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'VBD not found in instance %s'"
op|')'
op|'%'
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|unplug_vbd
name|'def'
name|'unplug_vbd'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vbd_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unplug VBD from VM"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vbd_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VBD.unplug'"
op|','
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'if'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'!='
string|"'DEVICE_ALREADY_DETACHED'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to unplug VBD %s'"
op|')'
op|'%'
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|destroy_vbd
name|'def'
name|'destroy_vbd'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vbd_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy VBD from host database"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VBD.destroy'"
op|','
name|'vbd_ref'
op|')'
newline|'\n'
comment|'#FIXME(armando): find a solution to missing instance_id'
nl|'\n'
comment|'#with Josh Kearney'
nl|'\n'
name|'session'
op|'.'
name|'wait_for_task'
op|'('
number|'0'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to destroy VBD %s'"
op|')'
op|'%'
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_vif
name|'def'
name|'create_vif'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm_ref'
op|','
name|'network_ref'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VIF record.  Returns a Deferred that gives the new\n        VIF reference."""'
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
string|"'0'"
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
name|'mac_address'
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
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating VIF for VM %s, network %s.'"
op|')'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'network_ref'
op|')'
newline|'\n'
name|'vif_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VIF.create'"
op|','
name|'vif_rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created VIF %s for VM %s, network %s.'"
op|')'
op|','
name|'vif_ref'
op|','
nl|'\n'
name|'vm_ref'
op|','
name|'network_ref'
op|')'
newline|'\n'
name|'return'
name|'vif_ref'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_snapshot
name|'def'
name|'create_snapshot'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'instance_id'
op|','
name|'vm_ref'
op|','
name|'label'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Creates Snapshot (Template) VM, Snapshot VBD, Snapshot VDI,\n        Snapshot VHD\n        """'
newline|'\n'
comment|'#TODO(sirp): Add quiesce and VSS locking support when Windows support'
nl|'\n'
comment|'# is added'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Snapshotting VM %s with label \'%s\'..."'
op|')'
op|','
nl|'\n'
name|'vm_ref'
op|','
name|'label'
op|')'
newline|'\n'
nl|'\n'
name|'vm_vdi_ref'
op|','
name|'vm_vdi_rec'
op|'='
name|'get_vdi_for_vm_safely'
op|'('
name|'session'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'vm_vdi_uuid'
op|'='
name|'vm_vdi_rec'
op|'['
string|'"uuid"'
op|']'
newline|'\n'
name|'sr_ref'
op|'='
name|'vm_vdi_rec'
op|'['
string|'"SR"'
op|']'
newline|'\n'
nl|'\n'
name|'original_parent_uuid'
op|'='
name|'get_vhd_parent_uuid'
op|'('
name|'session'
op|','
name|'vm_vdi_ref'
op|')'
newline|'\n'
nl|'\n'
name|'task'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.snapshot'"
op|','
name|'vm_ref'
op|','
name|'label'
op|')'
newline|'\n'
name|'template_vm_ref'
op|'='
name|'session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance_id'
op|','
name|'task'
op|')'
newline|'\n'
name|'template_vdi_rec'
op|'='
name|'get_vdi_for_vm_safely'
op|'('
name|'session'
op|','
name|'template_vm_ref'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'template_vdi_uuid'
op|'='
name|'template_vdi_rec'
op|'['
string|'"uuid"'
op|']'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created snapshot %s from VM %s.'"
op|')'
op|','
name|'template_vm_ref'
op|','
nl|'\n'
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'parent_uuid'
op|'='
name|'wait_for_vhd_coalesce'
op|'('
nl|'\n'
name|'session'
op|','
name|'instance_id'
op|','
name|'sr_ref'
op|','
name|'vm_vdi_ref'
op|','
name|'original_parent_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(sirp): we need to assert only one parent, not parents two deep'
nl|'\n'
name|'return'
name|'template_vm_ref'
op|','
op|'['
name|'template_vdi_uuid'
op|','
name|'parent_uuid'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|upload_image
name|'def'
name|'upload_image'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'instance_id'
op|','
name|'vdi_uuids'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Requests that the Glance plugin bundle the specified VDIs and\n        push them into Glance using the specified human-friendly name.\n        """'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Asking xapi to upload %s as ID %s"'
op|')'
op|','
nl|'\n'
name|'vdi_uuids'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
op|'{'
string|"'vdi_uuids'"
op|':'
name|'vdi_uuids'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'glance_host'"
op|':'
name|'FLAGS'
op|'.'
name|'glance_host'
op|','
nl|'\n'
string|"'glance_port'"
op|':'
name|'FLAGS'
op|'.'
name|'glance_port'
op|'}'
newline|'\n'
nl|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'params'"
op|':'
name|'pickle'
op|'.'
name|'dumps'
op|'('
name|'params'
op|')'
op|'}'
newline|'\n'
name|'task'
op|'='
name|'session'
op|'.'
name|'async_call_plugin'
op|'('
string|"'glance'"
op|','
string|"'put_vdis'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance_id'
op|','
name|'task'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|fetch_image
name|'def'
name|'fetch_image'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'instance_id'
op|','
name|'image'
op|','
name|'user'
op|','
name|'project'
op|','
name|'type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        type is interpreted as an ImageType instance\n        """'
newline|'\n'
name|'url'
op|'='
name|'images'
op|'.'
name|'image_url'
op|'('
name|'image'
op|')'
newline|'\n'
name|'access'
op|'='
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_access_key'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Asking xapi to fetch %s as %s"'
op|','
name|'url'
op|','
name|'access'
op|')'
newline|'\n'
name|'fn'
op|'='
op|'('
name|'type'
op|'!='
name|'ImageType'
op|'.'
name|'KERNEL_RAMDISK'
op|')'
name|'and'
string|"'get_vdi'"
name|'or'
string|"'get_kernel'"
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'args'
op|'['
string|"'src_url'"
op|']'
op|'='
name|'url'
newline|'\n'
name|'args'
op|'['
string|"'username'"
op|']'
op|'='
name|'access'
newline|'\n'
name|'args'
op|'['
string|"'password'"
op|']'
op|'='
name|'user'
op|'.'
name|'secret'
newline|'\n'
name|'args'
op|'['
string|"'add_partition'"
op|']'
op|'='
string|"'false'"
newline|'\n'
name|'args'
op|'['
string|"'raw'"
op|']'
op|'='
string|"'false'"
newline|'\n'
name|'if'
name|'type'
op|'!='
name|'ImageType'
op|'.'
name|'KERNEL_RAMDISK'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'add_partition'"
op|']'
op|'='
string|"'true'"
newline|'\n'
name|'if'
name|'type'
op|'=='
name|'ImageType'
op|'.'
name|'DISK_RAW'
op|':'
newline|'\n'
indent|'                '
name|'args'
op|'['
string|"'raw'"
op|']'
op|'='
string|"'true'"
newline|'\n'
dedent|''
dedent|''
name|'task'
op|'='
name|'session'
op|'.'
name|'async_call_plugin'
op|'('
string|"'objectstore'"
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance_id'
op|','
name|'task'
op|')'
newline|'\n'
name|'return'
name|'uuid'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup_image
name|'def'
name|'lookup_image'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vdi_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Looking up vdi %s for PV kernel"'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'fn'
op|'='
string|'"is_vdi_pv"'
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'args'
op|'['
string|"'vdi-ref'"
op|']'
op|'='
name|'vdi_ref'
newline|'\n'
comment|'#TODO: Call proper function in plugin'
nl|'\n'
name|'task'
op|'='
name|'session'
op|'.'
name|'async_call_plugin'
op|'('
string|"'objectstore'"
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
name|'pv_str'
op|'='
name|'session'
op|'.'
name|'wait_for_task'
op|'('
name|'task'
op|')'
newline|'\n'
name|'if'
name|'pv_str'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'true'"
op|':'
newline|'\n'
indent|'            '
name|'pv'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'pv_str'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'false'"
op|':'
newline|'\n'
indent|'            '
name|'pv'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"PV Kernel in VDI:%d"'
op|','
name|'pv'
op|')'
newline|'\n'
name|'return'
name|'pv'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup
name|'def'
name|'lookup'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'i'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Look the instance i up, and returns it if available"""'
newline|'\n'
name|'vms'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_by_name_label'
op|'('
name|'i'
op|')'
newline|'\n'
name|'n'
op|'='
name|'len'
op|'('
name|'vms'
op|')'
newline|'\n'
name|'if'
name|'n'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'n'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Duplicate'
op|'('
name|'_'
op|'('
string|"'duplicate name found: %s'"
op|')'
op|'%'
name|'i'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup_vm_vdis
name|'def'
name|'lookup_vm_vdis'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Look for the VDIs that are attached to the VM"""'
newline|'\n'
comment|'# Firstly we get the VBDs, then the VDIs.'
nl|'\n'
comment|'# TODO(Armando): do we leave the read-only devices?'
nl|'\n'
name|'vbds'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_VBDs'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'vdis'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'vbds'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'vbd'
name|'in'
name|'vbds'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'vdi'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VBD'
op|'.'
name|'get_VDI'
op|'('
name|'vbd'
op|')'
newline|'\n'
comment|'# Test valid VDI'
nl|'\n'
name|'record'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'vdi'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'VDI %s is still available'"
op|')'
op|','
nl|'\n'
name|'record'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'vdis'
op|'.'
name|'append'
op|'('
name|'vdi'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'len'
op|'('
name|'vdis'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'vdis'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|compile_info
name|'def'
name|'compile_info'
op|'('
name|'cls'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fill record with VM status information"""'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"(VM_UTILS) xenserver vm state -> |%s|"'
op|')'
op|','
nl|'\n'
name|'record'
op|'['
string|"'power_state'"
op|']'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"(VM_UTILS) xenapi power_state -> |%s|"'
op|')'
op|','
nl|'\n'
name|'XENAPI_POWER_STATE'
op|'['
name|'record'
op|'['
string|"'power_state'"
op|']'
op|']'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'XENAPI_POWER_STATE'
op|'['
name|'record'
op|'['
string|"'power_state'"
op|']'
op|']'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'long'
op|'('
name|'record'
op|'['
string|"'memory_static_max'"
op|']'
op|')'
op|'>>'
number|'10'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'long'
op|'('
name|'record'
op|'['
string|"'memory_dynamic_max'"
op|']'
op|')'
op|'>>'
number|'10'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'record'
op|'['
string|"'VCPUs_max'"
op|']'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|compile_diagnostics
name|'def'
name|'compile_diagnostics'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Compile VM diagnostics data"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'session'
op|'.'
name|'get_xenapi_host'
op|'('
op|')'
newline|'\n'
name|'host_ip'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'host'
op|'.'
name|'get_record'
op|'('
name|'host'
op|')'
op|'['
string|'"address"'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'KeyError'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|'"Unable to retrieve diagnostics"'
op|':'
name|'e'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'diags'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'xml'
op|'='
name|'get_rrd'
op|'('
name|'host_ip'
op|','
name|'record'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
name|'if'
name|'xml'
op|':'
newline|'\n'
indent|'                '
name|'rrd'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'node'
name|'in'
name|'enumerate'
op|'('
name|'rrd'
op|'.'
name|'firstChild'
op|'.'
name|'childNodes'
op|')'
op|':'
newline|'\n'
comment|"# We don't want all of the extra garbage"
nl|'\n'
indent|'                    '
name|'if'
name|'i'
op|'>='
number|'3'
name|'and'
name|'i'
op|'<='
number|'11'
op|':'
newline|'\n'
indent|'                        '
name|'ref'
op|'='
name|'node'
op|'.'
name|'childNodes'
newline|'\n'
comment|'# Name and Value'
nl|'\n'
name|'diags'
op|'['
name|'ref'
op|'['
number|'0'
op|']'
op|'.'
name|'firstChild'
op|'.'
name|'data'
op|']'
op|'='
name|'ref'
op|'['
number|'6'
op|']'
op|'.'
name|'firstChild'
op|'.'
name|'data'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'diags'
newline|'\n'
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|'"Unable to retrieve diagnostics"'
op|':'
name|'e'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_rrd
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_rrd'
op|'('
name|'host'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the VM RRD XML as a string"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'urllib'
op|'.'
name|'urlopen'
op|'('
string|'"http://%s:%s@%s/vm_rrd?uuid=%s"'
op|'%'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'uuid'
op|')'
op|')'
newline|'\n'
name|'return'
name|'xml'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#TODO(sirp): This code comes from XS5.6 pluginlib.py, we should refactor to'
nl|'\n'
comment|'# use that implmenetation'
nl|'\n'
DECL|function|get_vhd_parent
dedent|''
dedent|''
name|'def'
name|'get_vhd_parent'
op|'('
name|'session'
op|','
name|'vdi_rec'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Returns the VHD parent of the given VDI record, as a (ref, rec) pair.\n    Returns None if we\'re at the root of the tree.\n    """'
newline|'\n'
name|'if'
string|"'vhd-parent'"
name|'in'
name|'vdi_rec'
op|'['
string|"'sm_config'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'parent_uuid'
op|'='
name|'vdi_rec'
op|'['
string|"'sm_config'"
op|']'
op|'['
string|"'vhd-parent'"
op|']'
newline|'\n'
comment|'#NOTE(sirp): changed xenapi -> get_xenapi()'
nl|'\n'
name|'parent_ref'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_by_uuid'
op|'('
name|'parent_uuid'
op|')'
newline|'\n'
name|'parent_rec'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'parent_ref'
op|')'
newline|'\n'
comment|'#NOTE(sirp): changed log -> logging'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"VHD %s has parent %s"'
op|')'
op|','
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|','
name|'parent_ref'
op|')'
newline|'\n'
name|'return'
name|'parent_ref'
op|','
name|'parent_rec'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vhd_parent_uuid
dedent|''
dedent|''
name|'def'
name|'get_vhd_parent_uuid'
op|'('
name|'session'
op|','
name|'vdi_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'get_vhd_parent'
op|'('
name|'session'
op|','
name|'vdi_rec'
op|')'
newline|'\n'
name|'if'
name|'ret'
op|':'
newline|'\n'
indent|'        '
name|'parent_ref'
op|','
name|'parent_rec'
op|'='
name|'ret'
newline|'\n'
name|'return'
name|'parent_rec'
op|'['
string|'"uuid"'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|scan_sr
dedent|''
dedent|''
name|'def'
name|'scan_sr'
op|'('
name|'session'
op|','
name|'instance_id'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Re-scanning SR %s"'
op|')'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'task'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.SR.scan'"
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance_id'
op|','
name|'task'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wait_for_vhd_coalesce
dedent|''
name|'def'
name|'wait_for_vhd_coalesce'
op|'('
name|'session'
op|','
name|'instance_id'
op|','
name|'sr_ref'
op|','
name|'vdi_ref'
op|','
nl|'\n'
name|'original_parent_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Spin until the parent VHD is coalesced into its parent VHD\n\n    Before coalesce:\n        * original_parent_vhd\n            * parent_vhd\n                snapshot\n\n    Atter coalesce:\n        * parent_vhd\n            snapshot\n    """'
newline|'\n'
name|'max_attempts'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_vhd_coalesce_max_attempts'
newline|'\n'
name|'attempts'
op|'='
op|'{'
string|"'counter'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_poll_vhds
name|'def'
name|'_poll_vhds'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attempts'
op|'['
string|"'counter'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'if'
name|'attempts'
op|'['
string|"'counter'"
op|']'
op|'>'
name|'max_attempts'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"VHD coalesce attempts exceeded (%d > %d), giving up..."'
op|')'
nl|'\n'
op|'%'
op|'('
name|'attempts'
op|'['
string|"'counter'"
op|']'
op|','
name|'max_attempts'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'scan_sr'
op|'('
name|'session'
op|','
name|'instance_id'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'parent_uuid'
op|'='
name|'get_vhd_parent_uuid'
op|'('
name|'session'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'if'
name|'original_parent_uuid'
name|'and'
op|'('
name|'parent_uuid'
op|'!='
name|'original_parent_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Parent %s doesn\'t match original parent %s, "'
nl|'\n'
string|'"waiting for coalesce..."'
op|')'
op|','
nl|'\n'
name|'parent_uuid'
op|','
name|'original_parent_uuid'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Breakout of the loop (normally) and return the parent_uuid'
nl|'\n'
indent|'            '
name|'raise'
name|'utils'
op|'.'
name|'LoopingCallDone'
op|'('
name|'parent_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'loop'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'_poll_vhds'
op|')'
newline|'\n'
name|'loop'
op|'.'
name|'start'
op|'('
name|'FLAGS'
op|'.'
name|'xenapi_vhd_coalesce_poll_interval'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'parent_uuid'
op|'='
name|'loop'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'return'
name|'parent_uuid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vdi_for_vm_safely
dedent|''
name|'def'
name|'get_vdi_for_vm_safely'
op|'('
name|'session'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vdi_refs'
op|'='
name|'VMHelper'
op|'.'
name|'lookup_vm_vdis'
op|'('
name|'session'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'if'
name|'vdi_refs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"No VDIs found for VM %s"'
op|')'
op|'%'
name|'vm_ref'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'num_vdis'
op|'='
name|'len'
op|'('
name|'vdi_refs'
op|')'
newline|'\n'
name|'if'
name|'num_vdis'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Unexpected number of VDIs (%s) found for "'
nl|'\n'
string|'"VM %s"'
op|')'
op|'%'
op|'('
name|'num_vdis'
op|','
name|'vm_ref'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'vdi_ref'
op|'='
name|'vdi_refs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
name|'return'
name|'vdi_ref'
op|','
name|'vdi_rec'
newline|'\n'
dedent|''
endmarker|''
end_unit
