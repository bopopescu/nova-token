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
string|'"""\nManagement class for VM snapshot operations.\n"""'
newline|'\n'
name|'import'
name|'os'
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
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
name|'hyperv'
name|'import'
name|'utilsfactory'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
DECL|class|SnapshotOps
name|'class'
name|'SnapshotOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_pathutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_pathutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vhdutils'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_save_glance_image
dedent|''
name|'def'
name|'_save_glance_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'image_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'glance_image_service'
op|','
nl|'\n'
name|'image_id'
op|')'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'image_metadata'
op|'='
op|'{'
string|'"is_public"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|'"vhd"'
op|','
nl|'\n'
string|'"container_format"'
op|':'
string|'"bare"'
op|','
nl|'\n'
string|'"properties"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'open'
op|'('
name|'image_vhd_path'
op|','
string|"'rb'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'glance_image_service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image_metadata'
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_id'
op|','
name|'update_task_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create snapshot from a running VM instance."""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|'"name"'
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating snapshot for instance %s"'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'snapshot_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'take_vm_snapshot'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'update_task_state'
op|'('
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_PENDING_UPLOAD'
op|')'
newline|'\n'
nl|'\n'
name|'export_dir'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'src_vhd_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_root_vhd_path'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Getting info for VHD %s"'
op|','
name|'src_vhd_path'
op|')'
newline|'\n'
name|'src_base_disk_path'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_parent_path'
op|'('
nl|'\n'
name|'src_vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'export_dir'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_export_dir'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'dest_vhd_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'export_dir'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
nl|'\n'
name|'src_vhd_path'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Copying VHD %(src_vhd_path)s to %(dest_vhd_path)s'"
op|','
nl|'\n'
op|'{'
string|"'src_vhd_path'"
op|':'
name|'src_vhd_path'
op|','
nl|'\n'
string|"'dest_vhd_path'"
op|':'
name|'dest_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'copyfile'
op|'('
name|'src_vhd_path'
op|','
name|'dest_vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'image_vhd_path'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'not'
name|'src_base_disk_path'
op|':'
newline|'\n'
indent|'                '
name|'image_vhd_path'
op|'='
name|'dest_vhd_path'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'basename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'src_base_disk_path'
op|')'
newline|'\n'
name|'dest_base_disk_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'export_dir'
op|','
name|'basename'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Copying base disk %(src_vhd_path)s to '"
nl|'\n'
string|"'%(dest_base_disk_path)s'"
op|','
nl|'\n'
op|'{'
string|"'src_vhd_path'"
op|':'
name|'src_vhd_path'
op|','
nl|'\n'
string|"'dest_base_disk_path'"
op|':'
name|'dest_base_disk_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'copyfile'
op|'('
name|'src_base_disk_path'
op|','
nl|'\n'
name|'dest_base_disk_path'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Reconnecting copied base VHD "'
nl|'\n'
string|'"%(dest_base_disk_path)s and diff "'
nl|'\n'
string|'"VHD %(dest_vhd_path)s"'
op|','
nl|'\n'
op|'{'
string|"'dest_base_disk_path'"
op|':'
name|'dest_base_disk_path'
op|','
nl|'\n'
string|"'dest_vhd_path'"
op|':'
name|'dest_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'reconnect_parent_vhd'
op|'('
name|'dest_vhd_path'
op|','
nl|'\n'
name|'dest_base_disk_path'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Merging base disk %(dest_base_disk_path)s and "'
nl|'\n'
string|'"diff disk %(dest_vhd_path)s"'
op|','
nl|'\n'
op|'{'
string|"'dest_base_disk_path'"
op|':'
name|'dest_base_disk_path'
op|','
nl|'\n'
string|"'dest_vhd_path'"
op|':'
name|'dest_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'merge_vhd'
op|'('
name|'dest_vhd_path'
op|','
name|'dest_base_disk_path'
op|')'
newline|'\n'
name|'image_vhd_path'
op|'='
name|'dest_base_disk_path'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Updating Glance image %(image_id)s with content from "'
nl|'\n'
string|'"merged disk %(image_vhd_path)s"'
op|','
nl|'\n'
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
string|"'image_vhd_path'"
op|':'
name|'image_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'update_task_state'
op|'('
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_UPLOADING'
op|','
nl|'\n'
name|'expected_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_PENDING_UPLOAD'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_save_glance_image'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image_vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Snapshot image %(image_id)s updated for VM "'
nl|'\n'
string|'"%(instance_name)s"'
op|','
nl|'\n'
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Removing snapshot %s"'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'remove_vm_snapshot'
op|'('
name|'snapshot_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Failed to remove snapshot for VM %s'"
op|')'
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'export_dir'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Removing directory: %s'"
op|','
name|'export_dir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rmtree'
op|'('
name|'export_dir'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
