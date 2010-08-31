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
string|'"""\nVolume manager manages creating, attaching, detaching, and\ndestroying persistent storage volumes, ala EBS.\n"""'
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
name|'manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'volume_driver'"
op|','
string|"'nova.volume.driver.AOEDriver'"
op|','
nl|'\n'
string|"'Driver to use for volume creation'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'num_shelves'"
op|','
nl|'\n'
number|'100'
op|','
nl|'\n'
string|"'Number of vblade shelves'"
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
string|"'Number of vblade blades per shelf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AOEManager
name|'class'
name|'AOEManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages Ata-Over_Ethernet volumes"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'volume_driver'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'volume_driver'
op|':'
newline|'\n'
comment|'# NOTE(vish): support the legacy fake storage flag'
nl|'\n'
indent|'            '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'                '
name|'volume_driver'
op|'='
string|"'nova.volume.driver.FakeAOEDriver'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'volume_driver'
op|'='
name|'FLAGS'
op|'.'
name|'volume_driver'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'volume_driver'
op|')'
newline|'\n'
name|'super'
op|'('
name|'AOEManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ensure_blades
dedent|''
name|'def'
name|'_ensure_blades'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that blades have been created in datastore"""'
newline|'\n'
name|'total_blades'
op|'='
name|'FLAGS'
op|'.'
name|'num_shelves'
op|'*'
name|'FLAGS'
op|'.'
name|'blades_per_shelf'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'db'
op|'.'
name|'export_device_count'
op|'('
name|'context'
op|')'
op|'>='
name|'total_blades'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'for'
name|'shelf_id'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'num_shelves'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'blade_id'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'blades_per_shelf'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'dev'
op|'='
op|'{'
string|"'shelf_id'"
op|':'
name|'shelf_id'
op|','
string|"'blade_id'"
op|':'
name|'blade_id'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'export_device_create'
op|'('
name|'context'
op|','
name|'dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|create_volume
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and exports the volume"""'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|'"volume %s: creating"'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
op|'{'
string|"'node_name'"
op|':'
name|'FLAGS'
op|'.'
name|'node_name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'size'
op|'='
name|'volume_ref'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: creating lv of size %sG"'
op|','
name|'volume_id'
op|','
name|'size'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_volume'
op|'('
name|'volume_id'
op|','
name|'size'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: allocating shelf & blade"'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_blades'
op|'('
name|'context'
op|')'
newline|'\n'
name|'rval'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|'='
name|'rval'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: exporting shelf %s & blade %s"'
op|','
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
name|'driver'
op|'.'
name|'create_export'
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
name|'self'
op|'.'
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
string|'"volume %s: re-exporting all values"'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_exports'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"volume %s: created successfully"'
op|','
name|'volume_id'
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
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes and unexports volume"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Deleting volume with id of: %s"'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
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
name|'self'
op|'.'
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
name|'driver'
op|'.'
name|'remove_export'
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
name|'driver'
op|'.'
name|'delete_volumevolume_id'
newline|'\n'
name|'self'
op|'.'
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
dedent|''
dedent|''
endmarker|''
end_unit
