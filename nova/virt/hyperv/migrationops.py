begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
string|'"""\nManagement class for migration / resize operations.\n"""'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
name|'hostutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'imagecache'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'pathutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vhdutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'volumeops'
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
DECL|class|MigrationOps
name|'class'
name|'MigrationOps'
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
name|'_hostutils'
op|'='
name|'hostutils'
op|'.'
name|'HostUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'vmutils'
op|'.'
name|'VMUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'='
name|'vhdutils'
op|'.'
name|'VHDUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'='
name|'pathutils'
op|'.'
name|'PathUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'vmops'
op|'.'
name|'VMOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'='
name|'imagecache'
op|'.'
name|'ImageCache'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_migrate_disk_files
dedent|''
name|'def'
name|'_migrate_disk_files'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'disk_files'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'same_host'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'dest'
name|'in'
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'get_local_ips'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'same_host'
op|'='
name|'True'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Migration target is the source host"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Migration target host: %s"'
op|')'
op|'%'
name|'dest'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'revert_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_migr_revert_dir'
op|'('
nl|'\n'
name|'instance_name'
op|','
name|'remove_dir'
op|'='
name|'True'
op|')'
newline|'\n'
name|'dest_path'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'same_host'
op|':'
newline|'\n'
comment|'# Since source and target are the same, we copy the files to'
nl|'\n'
comment|'# a temporary location before moving them into place'
nl|'\n'
indent|'                '
name|'dest_path'
op|'='
string|"'%s_tmp'"
op|'%'
name|'instance_path'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'dest_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rmtree'
op|'('
name|'dest_path'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'makedirs'
op|'('
name|'dest_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'dest_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'('
nl|'\n'
name|'instance_name'
op|','
name|'dest'
op|','
name|'remove_dir'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'disk_file'
name|'in'
name|'disk_files'
op|':'
newline|'\n'
comment|'# Skip the config drive as the instance is already configured'
nl|'\n'
indent|'                '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'disk_file'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|'!='
string|"'configdrive.vhd'"
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'\'Copying disk "%(disk_file)s" to \''
nl|'\n'
string|'\'"%(dest_path)s"\''
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'copy'
op|'('
name|'disk_file'
op|','
name|'dest_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rename'
op|'('
name|'instance_path'
op|','
name|'revert_path'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'same_host'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rename'
op|'('
name|'dest_path'
op|','
name|'instance_path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_cleanup_failed_disk_migration'
op|'('
name|'instance_path'
op|','
name|'revert_path'
op|','
nl|'\n'
name|'dest_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_cleanup_failed_disk_migration
dedent|''
dedent|''
dedent|''
name|'def'
name|'_cleanup_failed_disk_migration'
op|'('
name|'self'
op|','
name|'instance_path'
op|','
nl|'\n'
name|'revert_path'
op|','
name|'dest_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'dest_path'
name|'and'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'dest_path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rmtree'
op|'('
name|'dest_path'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'revert_path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rename'
op|'('
name|'revert_path'
op|','
name|'instance_path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|'# Log and ignore this exception'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Cannot cleanup migration files"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_disk_and_power_off
dedent|''
dedent|''
name|'def'
name|'migrate_disk_and_power_off'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'instance_type'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"migrate_disk_and_power_off called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|'"name"'
op|']'
newline|'\n'
nl|'\n'
op|'('
name|'disk_files'
op|','
nl|'\n'
name|'volume_drives'
op|')'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_storage_paths'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'disk_files'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_migrate_disk_files'
op|'('
name|'instance_name'
op|','
name|'disk_files'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|','
name|'destroy_disks'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# disk_info is not used'
nl|'\n'
name|'return'
string|'""'
newline|'\n'
nl|'\n'
DECL|member|confirm_migration
dedent|''
name|'def'
name|'confirm_migration'
op|'('
name|'self'
op|','
name|'migration'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"confirm_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_migr_revert_dir'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'remove_dir'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_revert_migration_files
dedent|''
name|'def'
name|'_revert_migration_files'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'('
nl|'\n'
name|'instance_name'
op|','
name|'create_dir'
op|'='
name|'False'
op|','
name|'remove_dir'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'revert_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_migr_revert_dir'
op|'('
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rename'
op|'('
name|'revert_path'
op|','
name|'instance_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_revert_migration
dedent|''
name|'def'
name|'finish_revert_migration'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"finish_revert_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_revert_migration_files'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'ebs_root_in_block_devices'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_path'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_vhd_path'
op|'('
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'create_instance'
op|'('
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'root_vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'power_on'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_merge_base_vhd
dedent|''
name|'def'
name|'_merge_base_vhd'
op|'('
name|'self'
op|','
name|'diff_vhd_path'
op|','
name|'base_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_vhd_copy_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'diff_vhd_path'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'base_vhd_path'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Copying base disk %(base_vhd_path)s to '"
nl|'\n'
string|"'%(base_vhd_copy_path)s'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'copyfile'
op|'('
name|'base_vhd_path'
op|','
name|'base_vhd_copy_path'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reconnecting copied base VHD "'
nl|'\n'
string|'"%(base_vhd_copy_path)s and diff "'
nl|'\n'
string|'"VHD %(diff_vhd_path)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'reconnect_parent_vhd'
op|'('
name|'diff_vhd_path'
op|','
nl|'\n'
name|'base_vhd_copy_path'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Merging base disk %(base_vhd_copy_path)s and "'
nl|'\n'
string|'"diff disk %(diff_vhd_path)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'merge_vhd'
op|'('
name|'diff_vhd_path'
op|','
name|'base_vhd_copy_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Replace the differential VHD with the merged one'
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'rename'
op|'('
name|'base_vhd_copy_path'
op|','
name|'diff_vhd_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'base_vhd_copy_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'remove'
op|'('
name|'base_vhd_copy_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_resize_vhd
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_resize_vhd'
op|'('
name|'self'
op|','
name|'vhd_path'
op|','
name|'new_size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Getting info for disk: %s"'
op|')'
op|','
name|'vhd_path'
op|')'
newline|'\n'
name|'base_disk_path'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_parent_path'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
name|'if'
name|'base_disk_path'
op|':'
newline|'\n'
comment|'# A differential VHD cannot be resized'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_merge_base_vhd'
op|'('
name|'vhd_path'
op|','
name|'base_disk_path'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Resizing disk \\"%(vhd_path)s\\" to new max "'
nl|'\n'
string|'"size %(new_size)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'resize_vhd'
op|'('
name|'vhd_path'
op|','
name|'new_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_base_disk
dedent|''
name|'def'
name|'_check_base_disk'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'diff_vhd_path'
op|','
nl|'\n'
name|'src_base_disk_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_vhd_path'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'get_cached_image'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# If the location of the base host differs between source'
nl|'\n'
comment|'# and target hosts we need to reconnect the base disk'
nl|'\n'
name|'if'
name|'src_base_disk_path'
op|'.'
name|'lower'
op|'('
op|')'
op|'!='
name|'base_vhd_path'
op|'.'
name|'lower'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reconnecting copied base VHD "'
nl|'\n'
string|'"%(base_vhd_path)s and diff "'
nl|'\n'
string|'"VHD %(diff_vhd_path)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'reconnect_parent_vhd'
op|'('
name|'diff_vhd_path'
op|','
nl|'\n'
name|'base_vhd_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_migration
dedent|''
dedent|''
name|'def'
name|'finish_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration'
op|','
name|'instance'
op|','
name|'disk_info'
op|','
nl|'\n'
name|'network_info'
op|','
name|'image_meta'
op|','
name|'resize_instance'
op|'='
name|'False'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"finish_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'ebs_root_in_block_devices'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_path'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_vhd_path'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'root_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'"Cannot find boot VHD "'
nl|'\n'
string|'"file: %s"'
op|')'
op|'%'
name|'root_vhd_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vhd_info'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_info'
op|'('
name|'root_vhd_path'
op|')'
newline|'\n'
name|'src_base_disk_path'
op|'='
name|'vhd_info'
op|'.'
name|'get'
op|'('
string|'"ParentPath"'
op|')'
newline|'\n'
name|'if'
name|'src_base_disk_path'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_check_base_disk'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'root_vhd_path'
op|','
nl|'\n'
name|'src_base_disk_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'resize_instance'
op|':'
newline|'\n'
indent|'                '
name|'curr_size'
op|'='
name|'vhd_info'
op|'['
string|"'MaxInternalSize'"
op|']'
newline|'\n'
name|'new_size'
op|'='
name|'instance'
op|'['
string|"'root_gb'"
op|']'
op|'*'
number|'1024'
op|'**'
number|'3'
newline|'\n'
name|'if'
name|'new_size'
op|'<'
name|'curr_size'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'"Cannot resize a VHD to a "'
nl|'\n'
string|'"smaller size"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'new_size'
op|'>'
name|'curr_size'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_resize_vhd'
op|'('
name|'root_vhd_path'
op|','
name|'new_size'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'create_instance'
op|'('
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'root_vhd_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'power_on'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
