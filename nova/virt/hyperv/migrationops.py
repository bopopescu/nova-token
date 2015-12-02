begin_unit
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'units'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'configdrive'
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
name|'utilsfactory'
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
name|'utilsfactory'
op|'.'
name|'get_hostutils'
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
comment|'# TODO(mikal): it would be nice if this method took a full instance,'
nl|'\n'
comment|'# because it could then be passed to the log messages below.'
nl|'\n'
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
string|'"Migration target is the source host"'
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
string|'"Migration target host: %s"'
op|','
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
op|','
name|'create_dir'
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
string|'\'Copying disk "%(disk_file)s" to \''
nl|'\n'
string|'\'"%(dest_path)s"\''
op|','
nl|'\n'
op|'{'
string|"'disk_file'"
op|':'
name|'disk_file'
op|','
string|"'dest_path'"
op|':'
name|'dest_path'
op|'}'
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
name|'move_folder_files'
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
name|'move_folder_files'
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
name|'_LE'
op|'('
string|'"Cannot cleanup migration files"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_target_flavor
dedent|''
dedent|''
name|'def'
name|'_check_target_flavor'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'new_root_gb'
op|'='
name|'flavor'
op|'.'
name|'root_gb'
newline|'\n'
name|'curr_root_gb'
op|'='
name|'instance'
op|'.'
name|'root_gb'
newline|'\n'
nl|'\n'
name|'if'
name|'new_root_gb'
op|'<'
name|'curr_root_gb'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceFaultRollback'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'CannotResizeDisk'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Cannot resize the root disk to a smaller size. "'
nl|'\n'
string|'"Current size: %(curr_root_gb)s GB. Requested "'
nl|'\n'
string|'"size: %(new_root_gb)s GB."'
op|')'
op|'%'
op|'{'
nl|'\n'
string|"'curr_root_gb'"
op|':'
name|'curr_root_gb'
op|','
nl|'\n'
string|"'new_root_gb'"
op|':'
name|'new_root_gb'
op|'}'
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
name|'flavor'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
name|'timeout'
op|'='
number|'0'
op|','
nl|'\n'
name|'retry_interval'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"migrate_disk_and_power_off called"'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_check_target_flavor'
op|'('
name|'instance'
op|','
name|'flavor'
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
op|','
name|'timeout'
op|','
name|'retry_interval'
op|')'
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
name|'instance'
op|'.'
name|'name'
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
name|'instance'
op|'.'
name|'name'
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
string|'"confirm_migration called"'
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
op|'.'
name|'name'
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
DECL|member|_check_and_attach_config_drive
dedent|''
name|'def'
name|'_check_and_attach_config_drive'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vm_gen'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'configdrive'
op|'.'
name|'required_by'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'configdrive_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_configdrive_path'
op|'('
nl|'\n'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'configdrive_path'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'attach_config_drive'
op|'('
name|'instance'
op|','
name|'configdrive_path'
op|','
nl|'\n'
name|'vm_gen'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'ConfigDriveNotFound'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_revert_migration
dedent|''
dedent|''
dedent|''
name|'def'
name|'finish_revert_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
name|'power_on'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"finish_revert_migration called"'
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
op|'.'
name|'name'
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
name|'lookup_root_vhd_path'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'eph_vhd_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_ephemeral_vhd_path'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'image_meta'
op|'='
name|'objects'
op|'.'
name|'ImageMeta'
op|'.'
name|'from_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'vm_gen'
op|'='
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_image_vm_generation'
op|'('
nl|'\n'
name|'instance'
op|'.'
name|'uuid'
op|','
name|'root_vhd_path'
op|','
name|'image_meta'
op|')'
newline|'\n'
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
op|','
name|'eph_vhd_path'
op|','
name|'vm_gen'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_check_and_attach_config_drive'
op|'('
name|'instance'
op|','
name|'vm_gen'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'power_on'
op|':'
newline|'\n'
indent|'            '
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
string|"'Copying base disk %(base_vhd_path)s to '"
nl|'\n'
string|"'%(base_vhd_copy_path)s'"
op|','
nl|'\n'
op|'{'
string|"'base_vhd_path'"
op|':'
name|'base_vhd_path'
op|','
nl|'\n'
string|"'base_vhd_copy_path'"
op|':'
name|'base_vhd_copy_path'
op|'}'
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
string|'"Reconnecting copied base VHD "'
nl|'\n'
string|'"%(base_vhd_copy_path)s and diff "'
nl|'\n'
string|'"VHD %(diff_vhd_path)s"'
op|','
nl|'\n'
op|'{'
string|"'base_vhd_copy_path'"
op|':'
name|'base_vhd_copy_path'
op|','
nl|'\n'
string|"'diff_vhd_path'"
op|':'
name|'diff_vhd_path'
op|'}'
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
string|'"Merging base disk %(base_vhd_copy_path)s and "'
nl|'\n'
string|'"diff disk %(diff_vhd_path)s"'
op|','
nl|'\n'
op|'{'
string|"'base_vhd_copy_path'"
op|':'
name|'base_vhd_copy_path'
op|','
nl|'\n'
string|"'diff_vhd_path'"
op|':'
name|'diff_vhd_path'
op|'}'
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
DECL|member|_check_resize_vhd
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_check_resize_vhd'
op|'('
name|'self'
op|','
name|'vhd_path'
op|','
name|'vhd_info'
op|','
name|'new_size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'curr_size'
op|'='
name|'vhd_info'
op|'['
string|"'MaxInternalSize'"
op|']'
newline|'\n'
name|'if'
name|'new_size'
op|'<'
name|'curr_size'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'CannotResizeDisk'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Cannot resize the root disk to a smaller size. "'
nl|'\n'
string|'"Current size: %(curr_root_gb)s GB. Requested "'
nl|'\n'
string|'"size: %(new_root_gb)s GB."'
op|')'
op|'%'
op|'{'
nl|'\n'
string|"'curr_root_gb'"
op|':'
name|'curr_size'
op|','
nl|'\n'
string|"'new_root_gb'"
op|':'
name|'new_size'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'new_size'
op|'>'
name|'curr_size'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_resize_vhd'
op|'('
name|'vhd_path'
op|','
name|'new_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_resize_vhd
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
name|'if'
name|'vhd_path'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|'"vhd"'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Getting parent disk info for disk: %s"'
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
comment|'# A differential VHD cannot be resized. This limitation'
nl|'\n'
comment|'# does not apply to the VHDX format.'
nl|'\n'
indent|'                '
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
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Resizing disk \\"%(vhd_path)s\\" to new max "'
nl|'\n'
string|'"size %(new_size)s"'
op|','
nl|'\n'
op|'{'
string|"'vhd_path'"
op|':'
name|'vhd_path'
op|','
string|"'new_size'"
op|':'
name|'new_size'
op|'}'
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
string|'"Reconnecting copied base VHD "'
nl|'\n'
string|'"%(base_vhd_path)s and diff "'
nl|'\n'
string|'"VHD %(diff_vhd_path)s"'
op|','
nl|'\n'
op|'{'
string|"'base_vhd_path'"
op|':'
name|'base_vhd_path'
op|','
nl|'\n'
string|"'diff_vhd_path'"
op|':'
name|'diff_vhd_path'
op|'}'
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
op|','
name|'power_on'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"finish_migration called"'
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
op|'.'
name|'name'
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
name|'lookup_root_vhd_path'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'root_vhd_path'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'DiskNotFound'
op|'('
name|'location'
op|'='
name|'root_vhd_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'root_vhd_info'
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
name|'root_vhd_info'
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
name|'new_size'
op|'='
name|'instance'
op|'.'
name|'root_gb'
op|'*'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
name|'self'
op|'.'
name|'_check_resize_vhd'
op|'('
name|'root_vhd_path'
op|','
name|'root_vhd_info'
op|','
name|'new_size'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'eph_vhd_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_ephemeral_vhd_path'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'resize_instance'
op|':'
newline|'\n'
indent|'            '
name|'new_size'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'ephemeral_gb'"
op|','
number|'0'
op|')'
op|'*'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
name|'if'
name|'not'
name|'eph_vhd_path'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'new_size'
op|':'
newline|'\n'
indent|'                    '
name|'eph_vhd_path'
op|'='
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'create_ephemeral_vhd'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'eph_vhd_info'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_info'
op|'('
name|'eph_vhd_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_resize_vhd'
op|'('
name|'eph_vhd_path'
op|','
name|'eph_vhd_info'
op|','
name|'new_size'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'vm_gen'
op|'='
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_image_vm_generation'
op|'('
nl|'\n'
name|'instance'
op|'.'
name|'uuid'
op|','
name|'root_vhd_path'
op|','
name|'image_meta'
op|')'
newline|'\n'
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
op|','
name|'eph_vhd_path'
op|','
name|'vm_gen'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_check_and_attach_config_drive'
op|'('
name|'instance'
op|','
name|'vm_gen'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'power_on'
op|':'
newline|'\n'
indent|'            '
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
dedent|''
endmarker|''
end_unit
