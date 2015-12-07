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
string|'"""\nManagement class for live migration VM operations.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'os_win'
name|'import'
name|'utilsfactory'
newline|'\n'
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
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'migrate_data'
name|'as'
name|'migrate_data_obj'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LiveMigrationOps
name|'class'
name|'LiveMigrationOps'
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
name|'_livemigrutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_livemigrationutils'
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
name|'_imagecache'
op|'='
name|'imagecache'
op|'.'
name|'ImageCache'
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
nl|'\n'
DECL|member|live_migration
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
name|'post_method'
op|','
nl|'\n'
name|'recover_method'
op|','
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'migrate_data'
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
string|'"live_migration called"'
op|','
name|'instance'
op|'='
name|'instance_ref'
op|')'
newline|'\n'
name|'instance_name'
op|'='
name|'instance_ref'
op|'['
string|'"name"'
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'copy_vm_console_logs'
op|'('
name|'instance_name'
op|','
name|'dest'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'copy_vm_dvd_disks'
op|'('
name|'instance_name'
op|','
name|'dest'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_livemigrutils'
op|'.'
name|'live_migrate_vm'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'dest'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Calling live migration recover_method "'
nl|'\n'
string|'"for instance: %s"'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'recover_method'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
name|'block_migration'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Calling live migration post_method for instance: %s"'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'post_method'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
name|'block_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pre_live_migration
dedent|''
name|'def'
name|'pre_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"pre_live_migration called"'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_livemigrutils'
op|'.'
name|'check_live_migration_config'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_cow_images'
op|':'
newline|'\n'
indent|'            '
name|'boot_from_volume'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'ebs_root_in_block_devices'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'boot_from_volume'
name|'and'
name|'instance'
op|'.'
name|'image_ref'
op|':'
newline|'\n'
indent|'                '
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
dedent|''
dedent|''
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'initialize_volumes_connection'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'disk_path_mapping'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'get_disk_path_mapping'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'disk_path_mapping'
op|':'
newline|'\n'
comment|'# We create a planned VM, ensuring that volumes will remain'
nl|'\n'
comment|'# attached after the VM is migrated.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_livemigrutils'
op|'.'
name|'create_planned_vm'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'host'
op|','
nl|'\n'
name|'disk_path_mapping'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_live_migration
dedent|''
dedent|''
name|'def'
name|'post_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'disconnect_volumes'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
nl|'\n'
name|'create_dir'
op|'='
name|'False'
op|','
nl|'\n'
name|'remove_dir'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_live_migration_at_destination
dedent|''
name|'def'
name|'post_live_migration_at_destination'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'network_info'
op|','
name|'block_migration'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"post_live_migration_at_destination called"'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'log_vm_serial_output'
op|'('
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_destination
dedent|''
name|'def'
name|'check_can_live_migrate_destination'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'src_compute_info'
op|','
name|'dst_compute_info'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"check_can_live_migrate_destination called"'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'return'
name|'migrate_data_obj'
op|'.'
name|'HyperVLiveMigrateData'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_destination_cleanup
dedent|''
name|'def'
name|'check_can_live_migrate_destination_cleanup'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"check_can_live_migrate_destination_cleanup called"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_source
dedent|''
name|'def'
name|'check_can_live_migrate_source'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"check_can_live_migrate_source called"'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'return'
name|'dest_check_data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
