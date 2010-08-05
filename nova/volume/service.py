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
name|'import'
name|'os'
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
name|'datastore'
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
name|'utils'
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
name|'DEFINE_integer'
op|'('
string|"'first_shelf_id'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'last_octet'
op|'('
name|'utils'
op|'.'
name|'get_my_ip'
op|'('
op|')'
op|')'
op|'*'
number|'10'
op|','
nl|'\n'
string|"'AoE starting shelf_id for this service'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'last_shelf_id'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'last_octet'
op|'('
name|'utils'
op|'.'
name|'get_my_ip'
op|'('
op|')'
op|')'
op|'*'
number|'10'
op|'+'
number|'9'
op|','
nl|'\n'
string|"'AoE starting shelf_id for this service'"
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
DECL|class|NoMoreBlades
name|'class'
name|'NoMoreBlades'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|get_volume
dedent|''
name|'def'
name|'get_volume'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Returns a redis-backed volume object """'
newline|'\n'
name|'volume_class'
op|'='
name|'Volume'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'        '
name|'volume_class'
op|'='
name|'FakeVolume'
newline|'\n'
dedent|''
name|'vol'
op|'='
name|'volume_class'
op|'.'
name|'lookup'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'vol'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'vol'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Volume does not exist"'
op|')'
newline|'\n'
nl|'\n'
DECL|class|VolumeService
dedent|''
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
name|'volume_class'
op|'='
name|'Volume'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume_class'
op|'='
name|'FakeVolume'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_init_volume_group'
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
name|'size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Creates an exported volume (fake or real),\n        restarts exports to make it available.\n        Volume at this point has size, owner, and zone.\n        """'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Creating volume of size: %s"'
op|'%'
op|'('
name|'size'
op|')'
op|')'
newline|'\n'
name|'vol'
op|'='
name|'yield'
name|'self'
op|'.'
name|'volume_class'
op|'.'
name|'create'
op|'('
name|'size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"restarting exports"'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_restart_exports'
op|'('
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'vol'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|by_node
dedent|''
name|'def'
name|'by_node'
op|'('
name|'self'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" returns a list of volumes for a node """'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'smembers'
op|'('
string|"'volumes:%s'"
op|'%'
op|'('
name|'node_id'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'volume_class'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|all
name|'def'
name|'all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" returns a list of all volumes """'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'smembers'
op|'('
string|"'volumes'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'volume_class'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'vol'
op|'='
name|'get_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'vol'
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
name|'vol'
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
name|'yield'
name|'vol'
op|'.'
name|'destroy'
op|'('
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
DECL|member|_restart_exports
name|'def'
name|'_restart_exports'
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
name|'return'
newline|'\n'
dedent|''
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo vblade-persist auto all"'
op|')'
newline|'\n'
comment|'# NOTE(vish): this command sometimes sends output to stderr for warnings'
nl|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo vblade-persist start all"'
op|','
name|'error_ok'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_init_volume_group
name|'def'
name|'_init_volume_group'
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
name|'return'
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
nl|'\n'
DECL|class|Volume
dedent|''
dedent|''
name|'class'
name|'Volume'
op|'('
name|'datastore'
op|'.'
name|'BasicModel'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'volume_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'volume_id'
op|'='
name|'volume_id'
newline|'\n'
name|'super'
op|'('
name|'Volume'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|identifier
name|'def'
name|'identifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'volume_id'
newline|'\n'
nl|'\n'
DECL|member|default_state
dedent|''
name|'def'
name|'default_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|'"volume_id"'
op|':'
name|'self'
op|'.'
name|'volume_id'
op|','
nl|'\n'
string|'"node_name"'
op|':'
string|'"unassigned"'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'cls'
op|','
name|'size'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'vol'"
op|')'
newline|'\n'
name|'vol'
op|'='
name|'cls'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'vol'
op|'['
string|"'node_name'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'vol'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'user_id'
newline|'\n'
name|'vol'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
name|'vol'
op|'['
string|'"instance_id"'
op|']'
op|'='
string|"'none'"
newline|'\n'
name|'vol'
op|'['
string|'"mountpoint"'
op|']'
op|'='
string|"'none'"
newline|'\n'
name|'vol'
op|'['
string|"'attach_time'"
op|']'
op|'='
string|"'none'"
newline|'\n'
name|'vol'
op|'['
string|"'status'"
op|']'
op|'='
string|'"creating"'
comment|'# creating | available | in-use'
newline|'\n'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
comment|'# attaching | attached | detaching | detached'
newline|'\n'
name|'vol'
op|'['
string|"'delete_on_termination'"
op|']'
op|'='
string|"'False'"
newline|'\n'
name|'vol'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'vol'
op|'.'
name|'_create_lv'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'vol'
op|'.'
name|'_setup_export'
op|'('
op|')'
newline|'\n'
comment|'# TODO(joshua) - We need to trigger a fanout message for aoe-discover on all the nodes'
nl|'\n'
name|'vol'
op|'['
string|"'status'"
op|']'
op|'='
string|'"available"'
newline|'\n'
name|'vol'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'vol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_attach
dedent|''
name|'def'
name|'start_attach'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" """'
newline|'\n'
name|'self'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance_id'
newline|'\n'
name|'self'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'mountpoint'
newline|'\n'
name|'self'
op|'['
string|"'status'"
op|']'
op|'='
string|'"in-use"'
newline|'\n'
name|'self'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"attaching"'
newline|'\n'
name|'self'
op|'['
string|"'attach_time'"
op|']'
op|'='
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
newline|'\n'
name|'self'
op|'['
string|"'delete_on_termination'"
op|']'
op|'='
string|"'False'"
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_attach
dedent|''
name|'def'
name|'finish_attach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" """'
newline|'\n'
name|'self'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"attached"'
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_detach
dedent|''
name|'def'
name|'start_detach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" """'
newline|'\n'
name|'self'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detaching"'
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_detach
dedent|''
name|'def'
name|'finish_detach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'['
string|"'status'"
op|']'
op|'='
string|'"available"'
newline|'\n'
name|'self'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'is_new'
op|'='
name|'self'
op|'.'
name|'is_new_record'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'Volume'
op|','
name|'self'
op|')'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'if'
name|'is_new'
op|':'
newline|'\n'
indent|'            '
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'__devices_key'
newline|'\n'
comment|'# TODO(vish): these should be added by admin commands'
nl|'\n'
name|'more'
op|'='
name|'redis'
op|'.'
name|'scard'
op|'('
name|'self'
op|'.'
name|'_redis_association_name'
op|'('
string|'"node"'
op|','
nl|'\n'
name|'self'
op|'['
string|"'node_name'"
op|']'
op|')'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'redis'
op|'.'
name|'exists'
op|'('
name|'key'
op|')'
name|'and'
name|'not'
name|'more'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'shelf_id'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'first_shelf_id'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'last_shelf_id'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'blade_id'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'blades_per_shelf'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'redis'
op|'.'
name|'sadd'
op|'('
name|'key'
op|','
string|'"%s.%s"'
op|'%'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'associate_with'
op|'('
string|'"node"'
op|','
name|'self'
op|'['
string|"'node_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'self'
op|'.'
name|'_remove_export'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_delete_lv'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'unassociate_with'
op|'('
string|'"node"'
op|','
name|'self'
op|'['
string|"'node_name'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'get'
op|'('
string|"'shelf_id'"
op|','
name|'None'
op|')'
name|'and'
name|'self'
op|'.'
name|'get'
op|'('
string|"'blade_id'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'__devices_key'
newline|'\n'
name|'redis'
op|'.'
name|'sadd'
op|'('
name|'key'
op|','
string|'"%s.%s"'
op|'%'
op|'('
name|'self'
op|'['
string|"'shelf_id'"
op|']'
op|','
name|'self'
op|'['
string|"'blade_id'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'Volume'
op|','
name|'self'
op|')'
op|'.'
name|'destroy'
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
DECL|member|_create_lv
name|'def'
name|'_create_lv'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'str'
op|'('
name|'self'
op|'['
string|"'size'"
op|']'
op|')'
op|'=='
string|"'0'"
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
name|'self'
op|'['
string|"'size'"
op|']'
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
name|'self'
op|'['
string|"'volume_id'"
op|']'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_group'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_delete_lv
name|'def'
name|'_delete_lv'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'self'
op|'['
string|"'volume_id'"
op|']'
op|')'
op|','
name|'error_ok'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|__devices_key
name|'def'
name|'__devices_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'volume_devices:%s'"
op|'%'
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_setup_export
name|'def'
name|'_setup_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'__devices_key'
newline|'\n'
name|'device'
op|'='
name|'redis'
op|'.'
name|'spop'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NoMoreBlades'
op|'('
op|')'
newline|'\n'
dedent|''
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|'='
name|'device'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'self'
op|'['
string|"'aoe_device'"
op|']'
op|'='
string|'"e%s.%s"'
op|'%'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
newline|'\n'
name|'self'
op|'['
string|"'shelf_id'"
op|']'
op|'='
name|'shelf_id'
newline|'\n'
name|'self'
op|'['
string|"'blade_id'"
op|']'
op|'='
name|'blade_id'
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_exec_setup_export'
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
DECL|member|_exec_setup_export
name|'def'
name|'_exec_setup_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'self'
op|'['
string|"'shelf_id'"
op|']'
op|','
nl|'\n'
name|'self'
op|'['
string|"'blade_id'"
op|']'
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
name|'self'
op|'['
string|"'volume_id'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_remove_export
name|'def'
name|'_remove_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'get'
op|'('
string|"'shelf_id'"
op|','
name|'None'
op|')'
name|'or'
name|'not'
name|'self'
op|'.'
name|'get'
op|'('
string|"'blade_id'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'False'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'self'
op|'.'
name|'_exec_remove_export'
op|'('
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
DECL|member|_exec_remove_export
name|'def'
name|'_exec_remove_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo vblade-persist stop %s %s"'
op|'%'
op|'('
name|'self'
op|'['
string|"'shelf_id'"
op|']'
op|','
nl|'\n'
name|'self'
op|'['
string|"'blade_id'"
op|']'
op|')'
op|','
name|'error_ok'
op|'='
number|'1'
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
name|'self'
op|'['
string|"'shelf_id'"
op|']'
op|','
nl|'\n'
name|'self'
op|'['
string|"'blade_id'"
op|']'
op|')'
op|','
name|'error_ok'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeVolume
dedent|''
dedent|''
name|'class'
name|'FakeVolume'
op|'('
name|'Volume'
op|')'
op|':'
newline|'\n'
DECL|member|_create_lv
indent|'    '
name|'def'
name|'_create_lv'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_exec_setup_export
dedent|''
name|'def'
name|'_exec_setup_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'aoe_export_dir'
op|','
name|'self'
op|'['
string|"'aoe_device'"
op|']'
op|')'
newline|'\n'
name|'f'
op|'='
name|'file'
op|'('
name|'fname'
op|','
string|'"w"'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_exec_remove_export
dedent|''
name|'def'
name|'_exec_remove_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'aoe_export_dir'
op|','
name|'self'
op|'['
string|"'aoe_device'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_lv
dedent|''
name|'def'
name|'_delete_lv'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
