begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nNova Storage manages creating, attaching, detaching, and\ndestroying persistent storage volumes, ala EBS.\nCurrently uses Ata-over-Ethernet.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
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
name|'process'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'validate'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'storage_dev'"
op|','
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'Physical device to use for volumes'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'volume_group'"
op|','
string|"'nova-volumes'"
op|','
nl|'\n'
string|"'Name for the VG that will contain exported volumes'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'aoe_eth_dev'"
op|','
string|"'eth0'"
op|','
nl|'\n'
string|"'Which device to export the volumes on'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'aoe_export_dir'"
op|','
nl|'\n'
string|"'/var/lib/vblade-persist/vblades'"
op|','
nl|'\n'
string|"'AoE directory where exports are created'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'blades_per_shelf'"
op|','
nl|'\n'
number|'16'
op|','
nl|'\n'
string|"'Number of AoE blades per shelf'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'storage_availability_zone'"
op|','
nl|'\n'
string|"'nova'"
op|','
nl|'\n'
string|"'availability zone of this service'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
string|"'fake_storage'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Should we make real storage volumes to attach?'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeService
name|'class'
name|'VolumeService'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    There is one VolumeNode running on each host.\n    However, each VolumeNode can report on the state of\n    *all* volumes in the cluster.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VolumeService'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_exec_init_volumes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
op|'@'
name|'validate'
op|'.'
name|'rangetest'
op|'('
name|'size'
op|'='
op|'('
number|'0'
op|','
number|'1000'
op|')'
op|')'
newline|'\n'
DECL|member|create_volume
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'volume_id'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Creates an exported volume (fake or real),\n        restarts exports to make it available.\n        Volume at this point has size, owner, and zone.\n        """'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|'"volume %s: creating"'
op|'%'
op|'('
name|'volume_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'volume_ref'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# db.volume_update(context, volume_id, {'node_name': FLAGS.node_name})"
nl|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: creating lv of size %sG"'
op|'%'
op|'('
name|'volume_id'
op|','
name|'size'
op|')'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_exec_create_volume'
op|'('
name|'volume_id'
op|','
name|'volume_ref'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: allocating shelf & blade"'
op|'%'
op|'('
name|'volume_id'
op|')'
op|')'
newline|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|'='
name|'db'
op|'.'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: exporting shelf %s & blade %s"'
op|'%'
op|'('
name|'volume_id'
op|','
nl|'\n'
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'yield'
name|'self'
op|'.'
name|'_exec_create_export'
op|'('
name|'volume_id'
op|','
name|'shelf_id'
op|','
name|'blade_id'
op|')'
newline|'\n'
comment|'# TODO(joshua): We need to trigger a fanout message'
nl|'\n'
comment|'#               for aoe-discover on all the nodes'
nl|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: re-exporting all values"'
op|'%'
op|'('
name|'volume_id'
op|')'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_exec_ensure_exports'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: created successfully"'
op|'%'
op|'('
name|'volume_id'
op|')'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|delete_volume
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume_id'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Deleting volume with id of: %s"'
op|'%'
op|'('
name|'volume_id'
op|')'
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'volume_ref'
op|'['
string|"'attach_status'"
op|']'
op|'=='
string|'"attached"'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Volume is still attached"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'volume_ref'
op|'['
string|"'node_name'"
op|']'
op|'!='
name|'FLAGS'
op|'.'
name|'node_name'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Volume is not local to this node"'
op|')'
newline|'\n'
dedent|''
name|'shelf_id'
op|','
name|'blade_id'
op|'='
name|'db'
op|'.'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_exec_remove_export'
op|'('
name|'volume_id'
op|','
name|'shelf_id'
op|','
name|'blade_id'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_exec_delete_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_exec_create_volume
name|'def'
name|'_exec_create_volume'
op|'('
name|'self'
op|','
name|'volume_id'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'int'
op|'('
name|'size'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'sizestr'
op|'='
string|"'100M'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'sizestr'
op|'='
string|"'%sG'"
op|'%'
name|'size'
newline|'\n'
dedent|''
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo lvcreate -L %s -n %s %s"'
op|'%'
op|'('
name|'sizestr'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_group'
op|')'
op|','
nl|'\n'
name|'terminate_on_stderr'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_exec_delete_volume
name|'def'
name|'_exec_delete_volume'
op|'('
name|'self'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo lvremove -f %s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
nl|'\n'
name|'volume_id'
op|')'
op|','
nl|'\n'
name|'terminate_on_stderr'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_exec_create_export
name|'def'
name|'_exec_create_export'
op|'('
name|'self'
op|','
name|'volume_id'
op|','
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo vblade-persist setup %s %s %s /dev/%s/%s"'
op|'%'
nl|'\n'
op|'('
name|'shelf_id'
op|','
nl|'\n'
name|'blade_id'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'aoe_eth_dev'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
nl|'\n'
name|'volume_id'
op|')'
op|','
nl|'\n'
name|'terminate_on_stderr'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_exec_remove_export
name|'def'
name|'_exec_remove_export'
op|'('
name|'self'
op|','
name|'_volume_id'
op|','
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo vblade-persist stop %s %s"'
op|'%'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|','
nl|'\n'
name|'terminate_on_stderr'
op|'='
name|'False'
op|')'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo vblade-persist destroy %s %s"'
op|'%'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|','
nl|'\n'
name|'terminate_on_stderr'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_exec_ensure_exports
name|'def'
name|'_exec_ensure_exports'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'None'
op|')'
newline|'\n'
comment|'# NOTE(vish): these commands sometimes sends output to stderr for warnings'
nl|'\n'
dedent|''
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo vblade-persist auto all"'
op|','
nl|'\n'
name|'terminate_on_stderr'
op|'='
name|'False'
op|')'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo vblade-persist start all"'
op|','
nl|'\n'
name|'terminate_on_stderr'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_exec_init_volumes
name|'def'
name|'_exec_init_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo pvcreate %s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'storage_dev'
op|')'
op|')'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo vgcreate %s %s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'storage_dev'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
