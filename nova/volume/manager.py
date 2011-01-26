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
string|'"""\nVolume manager manages creating, attaching, detaching, and persistent storage.\n\nPersistant storage volumes keep their state independent of instances.  You can\nattach to an instance, terminate the instance, spawn a new instance (even\none from a different image) and re-attach the volume with the same data\nintact.\n\n**Related Flags**\n\n:volume_topic:  What :mod:`rpc` topic to listen to (default: `volume`).\n:volume_manager:  The module name of a class derived from\n                  :class:`manager.Manager` (default:\n                  :class:`nova.volume.manager.AOEManager`).\n:storage_availability_zone:  Defaults to `nova`.\n:volume_driver:  Used by :class:`AOEManager`.  Defaults to\n                 :class:`nova.volume.driver.AOEDriver`.\n:num_shelves:  Number of shelves for AoE (default: 100).\n:num_blades:  Number of vblades per shelf to allocate AoE storage from\n              (default: 16).\n:volume_group:  Name of the group that will contain exported volumes (default:\n                `nova-volumes`)\n:aoe_eth_dev:  Device name the volumes will be exported on (default: `eth0`).\n:num_shell_tries:  Number of times to attempt to run AoE commands (default: 3)\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'log'
name|'as'
name|'logging'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.volume.manager'"
op|')'
newline|'\n'
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
name|'DEFINE_string'
op|'('
string|"'volume_driver'"
op|','
string|"'nova.volume.driver.ISCSIDriver'"
op|','
nl|'\n'
string|"'Driver to use for volume creation'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
string|"'use_local_volumes'"
op|','
name|'True'
op|','
nl|'\n'
string|"'if True, will not discover local volumes'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeManager
name|'class'
name|'VolumeManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages attachable block storage devices."""'
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
string|'"""Load the driver from the one specified in args, or from flags."""'
newline|'\n'
name|'if'
name|'not'
name|'volume_driver'
op|':'
newline|'\n'
indent|'            '
name|'volume_driver'
op|'='
name|'FLAGS'
op|'.'
name|'volume_driver'
newline|'\n'
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
name|'VolumeManager'
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
comment|'# NOTE(vish): Implementation specific db handling is done'
nl|'\n'
comment|'#             by the driver.'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'db'
op|'='
name|'self'
op|'.'
name|'db'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Do any initialization that needs to be run if this is a\n           standalone service."""'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'check_for_setup_error'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_all_by_host'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Re-exporting %s volumes"'
op|')'
op|','
name|'len'
op|'('
name|'volumes'
op|')'
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
name|'in'
op|'['
string|"'available'"
op|','
string|"'in-use'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_export'
op|'('
name|'ctxt'
op|','
name|'volume'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"volume %s: skipping export"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume
dedent|''
dedent|''
dedent|''
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
string|'"""Creates and exports the volume."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
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
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"volume %s: creating"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
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
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
comment|"# NOTE(vish): so we don't have to get volume from db again"
nl|'\n'
comment|'#             before passing it to the driver.'
nl|'\n'
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|'='
name|'self'
op|'.'
name|'host'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vol_name'
op|'='
name|'volume_ref'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vol_size'
op|'='
name|'volume_ref'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %(vol_name)s: creating lv of"'
nl|'\n'
string|'" size %(vol_size)sG"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_volume'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: creating export"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_export'
op|'('
name|'context'
op|','
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'status'"
op|':'
string|"'error'"
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'launched_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: created successfully"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'volume_id'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
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
string|'"""Deletes and unexports volume."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
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
name|'_'
op|'('
string|'"Volume is still attached"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|'!='
name|'self'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Volume is not local to this node"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
string|'"volume %s: removing export"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'remove_export'
op|'('
name|'context'
op|','
name|'volume_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: deleting"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'delete_volume'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'error_deleting'"
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
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
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: deleted successfully"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|setup_compute_volume
dedent|''
name|'def'
name|'setup_compute_volume'
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
string|'"""Setup remote volume on compute host.\n\n        Returns path to device."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
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
string|"'host'"
op|']'
op|'=='
name|'self'
op|'.'
name|'host'
name|'and'
name|'FLAGS'
op|'.'
name|'use_local_volumes'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'local_path'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'discover_volume'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'path'
newline|'\n'
nl|'\n'
DECL|member|remove_compute_volume
dedent|''
name|'def'
name|'remove_compute_volume'
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
string|'"""Remove remote volume on compute host."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
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
string|"'host'"
op|']'
op|'=='
name|'self'
op|'.'
name|'host'
name|'and'
name|'FLAGS'
op|'.'
name|'use_local_volumes'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'undiscover_volume'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
