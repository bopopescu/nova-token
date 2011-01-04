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
string|'"""\nManagement class for VM-related functions (spawn, reboot, etc).\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
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
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'network_utils'
name|'import'
name|'NetworkHelper'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vm_utils'
name|'import'
name|'VMHelper'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vm_utils'
name|'import'
name|'ImageType'
newline|'\n'
nl|'\n'
DECL|variable|XenAPI
name|'XenAPI'
op|'='
name|'None'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.xenapi.vmops"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMOps
name|'class'
name|'VMOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Management class for VM-related tasks\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'XenAPI'
op|'='
name|'session'
op|'.'
name|'get_imported_xenapi'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'VMHelper'
op|'.'
name|'XenAPI'
op|'='
name|'self'
op|'.'
name|'XenAPI'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List VM instances"""'
newline|'\n'
name|'vms'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'vm'
name|'in'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'rec'
op|'['
string|'"is_a_template"'
op|']'
name|'and'
name|'not'
name|'rec'
op|'['
string|'"is_control_domain"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'vms'
op|'.'
name|'append'
op|'('
name|'rec'
op|'['
string|'"name_label"'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'vms'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'not'
name|'None'
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
string|"'Attempted to create'"
nl|'\n'
string|"' non-unique name %s'"
op|')'
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bridge'
op|'='
name|'db'
op|'.'
name|'network_get_by_instance'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'NetworkHelper'
op|'.'
name|'find_network_with_bridge'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'bridge'
op|')'
newline|'\n'
nl|'\n'
name|'user'
op|'='
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'instance'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'project'
op|'='
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'instance'
op|'.'
name|'project_id'
op|')'
newline|'\n'
comment|'#if kernel is not present we must download a raw disk'
nl|'\n'
name|'if'
name|'instance'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'disk_image_type'
op|'='
name|'ImageType'
op|'.'
name|'DISK'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'disk_image_type'
op|'='
name|'ImageType'
op|'.'
name|'DISK_RAW'
newline|'\n'
dedent|''
name|'vdi_uuid'
op|'='
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'image_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'disk_image_type'
op|')'
newline|'\n'
name|'vdi_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VDI.get_by_uuid'"
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
comment|'#Have a look at the VDI and see if it has a PV kernel'
nl|'\n'
name|'pv_kernel'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'pv_kernel'
op|'='
name|'VMHelper'
op|'.'
name|'lookup_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
dedent|''
name|'kernel'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'kernel'
op|'='
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'kernel_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'ImageType'
op|'.'
name|'KERNEL_RAMDISK'
op|')'
newline|'\n'
dedent|''
name|'ramdisk'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'ramdisk_id'
op|':'
newline|'\n'
indent|'            '
name|'ramdisk'
op|'='
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'ramdisk_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'ImageType'
op|'.'
name|'KERNEL_RAMDISK'
op|')'
newline|'\n'
dedent|''
name|'vm_ref'
op|'='
name|'VMHelper'
op|'.'
name|'create_vm'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'instance'
op|','
name|'kernel'
op|','
name|'ramdisk'
op|','
name|'pv_kernel'
op|')'
newline|'\n'
name|'VMHelper'
op|'.'
name|'create_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
number|'0'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'network_ref'
op|':'
newline|'\n'
indent|'            '
name|'VMHelper'
op|'.'
name|'create_vif'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'network_ref'
op|','
name|'instance'
op|'.'
name|'mac_address'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Starting VM %s...'"
op|')'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VM.start'"
op|','
name|'vm_ref'
op|','
name|'False'
op|','
name|'False'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Spawning VM %s created %s.'"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(armando): Do we really need to do this in virt?'
nl|'\n'
name|'timer'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_wait_for_boot
name|'def'
name|'_wait_for_boot'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'state'
op|'='
name|'self'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'['
string|"'state'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
name|'state'
op|')'
newline|'\n'
name|'if'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Instance %s: booted'"
op|')'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'instance %s: failed to boot'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_boot'
newline|'\n'
name|'return'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Create snapshot from a running VM instance\n\n        :param instance: instance to be snapshotted\n        :param name: name/label to be given to the snapshot\n\n        Steps involved in a XenServer snapshot:\n\n        1. XAPI-Snapshot: Snapshotting the instance using XenAPI. This\n            creates: Snapshot (Template) VM, Snapshot VBD, Snapshot VDI,\n            Snapshot VHD\n\n        2. Wait-for-coalesce: The Snapshot VDI and Instance VDI both point to\n            a \'base-copy\' VDI.  The base_copy is immutable and may be chained\n            with other base_copies.  If chained, the base_copies\n            coalesce together, so, we must wait for this coalescing to occur to\n            get a stable representation of the data on disk.\n\n        3. Push-to-glance: Once coalesced, we call a plugin on the XenServer\n            that will bundle the VHDs together and then push the bundle into\n            Glance.\n        """'
newline|'\n'
nl|'\n'
comment|'#TODO(sirp): Add quiesce and VSS locking support when Windows support'
nl|'\n'
comment|'# is added'
nl|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Starting snapshot for VM %s"'
op|')'
op|','
name|'instance'
op|')'
newline|'\n'
name|'vm_ref'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'label'
op|'='
string|'"%s-snapshot"'
op|'%'
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'template_vm_ref'
op|','
name|'template_vdi_uuids'
op|'='
name|'VMHelper'
op|'.'
name|'create_snapshot'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
name|'vm_ref'
op|','
name|'label'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
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
name|'error'
op|'('
name|'_'
op|'('
string|'"Unable to Snapshot %s: %s"'
op|')'
op|','
name|'vm_ref'
op|','
name|'exc'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# call plugin to ship snapshot off to glance'
nl|'\n'
indent|'            '
name|'VMHelper'
op|'.'
name|'upload_image'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
name|'template_vdi_uuids'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_destroy'
op|'('
name|'instance'
op|','
name|'template_vm_ref'
op|','
name|'shutdown'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Finished snapshot and upload for VM %s"'
op|')'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot VM instance"""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'instance not'"
nl|'\n'
string|"' found %s'"
op|')'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.clean_reboot'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_destroy'
op|'('
name|'instance'
op|','
name|'vm'
op|','
name|'shutdown'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_destroy
dedent|''
name|'def'
name|'_destroy'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vm'
op|','
name|'shutdown'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Destroy VM instance """'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|"# Don't complain, just return.  This lets us clean up instances"
nl|'\n'
comment|'# that have already disappeared from the underlying platform.'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
comment|'# Get the VDIs related to the VM'
nl|'\n'
dedent|''
name|'vdis'
op|'='
name|'VMHelper'
op|'.'
name|'lookup_vm_vdis'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'shutdown'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.hard_shutdown'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
comment|'# Disk clean-up'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'vdis'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'vdi'
name|'in'
name|'vdis'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VDI.destroy'"
op|','
name|'vdi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
comment|'# VM Destroy'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.destroy'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_wait_with_callback
dedent|''
dedent|''
name|'def'
name|'_wait_with_callback'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'task'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance_id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'callback'
op|'('
name|'ret'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pause VM instance"""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Instance not'"
nl|'\n'
string|"' found %s'"
op|')'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.pause'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unpause VM instance"""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Instance not'"
nl|'\n'
string|"' found %s'"
op|')'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.unpause'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""suspend the specified instance"""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"suspend: instance not present %s"'
op|')'
op|'%'
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.suspend'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'task'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|resume
dedent|''
name|'def'
name|'resume'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""resume the specified instance"""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"resume: instance not present %s"'
op|')'
op|'%'
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.resume'"
op|','
name|'vm'
op|','
name|'False'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'task'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Instance not'"
nl|'\n'
string|"' found %s'"
op|')'
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'return'
name|'VMHelper'
op|'.'
name|'compile_info'
op|'('
name|'rec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM diagnostics"""'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|'"Instance not found %s"'
op|')'
op|'%'
nl|'\n'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'return'
name|'VMHelper'
op|'.'
name|'compile_diagnostics'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'rec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return snapshot of console"""'
newline|'\n'
comment|'# TODO: implement this to fix pylint!'
nl|'\n'
name|'return'
string|"'FAKE CONSOLE OUTPUT of instance'"
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
