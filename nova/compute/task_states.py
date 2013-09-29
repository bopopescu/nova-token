begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""Possible task states for instances.\n\nCompute instance task states represent what is happening to the instance at the\ncurrent moment. These tasks can be generic, such as \'spawning\', or specific,\nsuch as \'block_device_mapping\'. These task states allow for a better view into\nwhat an instance is doing and should be displayed to users/administrators as\nnecessary.\n\n"""'
newline|'\n'
nl|'\n'
comment|'# possible task states during create()'
nl|'\n'
DECL|variable|SCHEDULING
name|'SCHEDULING'
op|'='
string|"'scheduling'"
newline|'\n'
DECL|variable|BLOCK_DEVICE_MAPPING
name|'BLOCK_DEVICE_MAPPING'
op|'='
string|"'block_device_mapping'"
newline|'\n'
DECL|variable|NETWORKING
name|'NETWORKING'
op|'='
string|"'networking'"
newline|'\n'
DECL|variable|SPAWNING
name|'SPAWNING'
op|'='
string|"'spawning'"
newline|'\n'
nl|'\n'
comment|'# possible task states during snapshot()'
nl|'\n'
DECL|variable|IMAGE_SNAPSHOT
name|'IMAGE_SNAPSHOT'
op|'='
string|"'image_snapshot'"
newline|'\n'
DECL|variable|IMAGE_PENDING_UPLOAD
name|'IMAGE_PENDING_UPLOAD'
op|'='
string|"'image_pending_upload'"
newline|'\n'
DECL|variable|IMAGE_UPLOADING
name|'IMAGE_UPLOADING'
op|'='
string|"'image_uploading'"
newline|'\n'
nl|'\n'
comment|'# possible task states during backup()'
nl|'\n'
DECL|variable|IMAGE_BACKUP
name|'IMAGE_BACKUP'
op|'='
string|"'image_backup'"
newline|'\n'
nl|'\n'
comment|'# possible task states during live_snapshot()'
nl|'\n'
DECL|variable|IMAGE_LIVE_SNAPSHOT
name|'IMAGE_LIVE_SNAPSHOT'
op|'='
string|"'image_live_snapshot'"
newline|'\n'
nl|'\n'
comment|'# possible task states during set_admin_password()'
nl|'\n'
DECL|variable|UPDATING_PASSWORD
name|'UPDATING_PASSWORD'
op|'='
string|"'updating_password'"
newline|'\n'
nl|'\n'
comment|'# possible task states during resize()'
nl|'\n'
DECL|variable|RESIZE_PREP
name|'RESIZE_PREP'
op|'='
string|"'resize_prep'"
newline|'\n'
DECL|variable|RESIZE_MIGRATING
name|'RESIZE_MIGRATING'
op|'='
string|"'resize_migrating'"
newline|'\n'
DECL|variable|RESIZE_MIGRATED
name|'RESIZE_MIGRATED'
op|'='
string|"'resize_migrated'"
newline|'\n'
DECL|variable|RESIZE_FINISH
name|'RESIZE_FINISH'
op|'='
string|"'resize_finish'"
newline|'\n'
nl|'\n'
comment|'# possible task states during revert_resize()'
nl|'\n'
DECL|variable|RESIZE_REVERTING
name|'RESIZE_REVERTING'
op|'='
string|"'resize_reverting'"
newline|'\n'
nl|'\n'
comment|'# possible task states during confirm_resize()'
nl|'\n'
DECL|variable|RESIZE_CONFIRMING
name|'RESIZE_CONFIRMING'
op|'='
string|"'resize_confirming'"
newline|'\n'
nl|'\n'
comment|'# possible task states during reboot()'
nl|'\n'
DECL|variable|REBOOTING
name|'REBOOTING'
op|'='
string|"'rebooting'"
newline|'\n'
DECL|variable|REBOOTING_HARD
name|'REBOOTING_HARD'
op|'='
string|"'rebooting_hard'"
newline|'\n'
nl|'\n'
comment|'# possible task states during pause()'
nl|'\n'
DECL|variable|PAUSING
name|'PAUSING'
op|'='
string|"'pausing'"
newline|'\n'
nl|'\n'
comment|'# possible task states during unpause()'
nl|'\n'
DECL|variable|UNPAUSING
name|'UNPAUSING'
op|'='
string|"'unpausing'"
newline|'\n'
nl|'\n'
comment|'# possible task states during suspend()'
nl|'\n'
DECL|variable|SUSPENDING
name|'SUSPENDING'
op|'='
string|"'suspending'"
newline|'\n'
nl|'\n'
comment|'# possible task states during resume()'
nl|'\n'
DECL|variable|RESUMING
name|'RESUMING'
op|'='
string|"'resuming'"
newline|'\n'
nl|'\n'
comment|'# possible task states during power_off()'
nl|'\n'
DECL|variable|POWERING_OFF
name|'POWERING_OFF'
op|'='
string|"'powering-off'"
newline|'\n'
nl|'\n'
comment|'# possible task states during power_on()'
nl|'\n'
DECL|variable|POWERING_ON
name|'POWERING_ON'
op|'='
string|"'powering-on'"
newline|'\n'
nl|'\n'
comment|'# possible task states during rescue()'
nl|'\n'
DECL|variable|RESCUING
name|'RESCUING'
op|'='
string|"'rescuing'"
newline|'\n'
nl|'\n'
comment|'# possible task states during unrescue()'
nl|'\n'
DECL|variable|UNRESCUING
name|'UNRESCUING'
op|'='
string|"'unrescuing'"
newline|'\n'
nl|'\n'
comment|'# possible task states during rebuild()'
nl|'\n'
DECL|variable|REBUILDING
name|'REBUILDING'
op|'='
string|"'rebuilding'"
newline|'\n'
DECL|variable|REBUILD_BLOCK_DEVICE_MAPPING
name|'REBUILD_BLOCK_DEVICE_MAPPING'
op|'='
string|'"rebuild_block_device_mapping"'
newline|'\n'
DECL|variable|REBUILD_SPAWNING
name|'REBUILD_SPAWNING'
op|'='
string|"'rebuild_spawning'"
newline|'\n'
nl|'\n'
comment|'# possible task states during live_migrate()'
nl|'\n'
DECL|variable|MIGRATING
name|'MIGRATING'
op|'='
string|'"migrating"'
newline|'\n'
nl|'\n'
comment|'# possible task states during delete()'
nl|'\n'
DECL|variable|DELETING
name|'DELETING'
op|'='
string|"'deleting'"
newline|'\n'
nl|'\n'
comment|'# possible task states during soft_delete()'
nl|'\n'
DECL|variable|SOFT_DELETING
name|'SOFT_DELETING'
op|'='
string|"'soft-deleting'"
newline|'\n'
nl|'\n'
comment|'# possible task states during restore()'
nl|'\n'
DECL|variable|RESTORING
name|'RESTORING'
op|'='
string|"'restoring'"
newline|'\n'
nl|'\n'
comment|'# possible task states during shelve()'
nl|'\n'
DECL|variable|SHELVING
name|'SHELVING'
op|'='
string|"'shelving'"
newline|'\n'
DECL|variable|SHELVING_IMAGE_PENDING_UPLOAD
name|'SHELVING_IMAGE_PENDING_UPLOAD'
op|'='
string|"'shelving_image_pending_upload'"
newline|'\n'
DECL|variable|SHELVING_IMAGE_UPLOADING
name|'SHELVING_IMAGE_UPLOADING'
op|'='
string|"'shelving_image_uploading'"
newline|'\n'
nl|'\n'
comment|'# possible task states during shelve_offload()'
nl|'\n'
DECL|variable|SHELVING_OFFLOADING
name|'SHELVING_OFFLOADING'
op|'='
string|"'shelving_offloading'"
newline|'\n'
nl|'\n'
comment|'# possible task states during unshelve()'
nl|'\n'
DECL|variable|UNSHELVING
name|'UNSHELVING'
op|'='
string|"'unshelving'"
newline|'\n'
endmarker|''
end_unit
