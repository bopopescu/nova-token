begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# Copyright [2010] [Anso Labs, LLC]'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""\nNova Storage manages creating, attaching, detaching, and\ndestroying persistent storage volumes, ala EBS.\nCurrently uses Ata-over-Ethernet.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'from'
name|'tornado'
name|'import'
name|'ioloop'
newline|'\n'
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
name|'rpc'
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
name|'DEFINE_string'
op|'('
string|"'storage_name'"
op|','
nl|'\n'
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
string|"'name of this node'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'shelf_id'"
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
op|','
nl|'\n'
string|"'AoE shelf_id for this node'"
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
string|"'availability zone of this node'"
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
comment|'# TODO(joshua) Index of volumes by project'
nl|'\n'
nl|'\n'
DECL|function|get_volume
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
name|'if'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sismember'
op|'('
string|"'volumes'"
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'volume_class'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
op|')'
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
DECL|class|BlockStore
dedent|''
name|'class'
name|'BlockStore'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    There is one BlockStore running on each volume node.\n    However, each BlockStore can report on the state of\n    *all* volumes in the cluster.\n    """'
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
name|'BlockStore'
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
DECL|member|report_state
dedent|''
name|'def'
name|'report_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'#TODO: aggregate the state of the system'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
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
number|'100'
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
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sadd'
op|'('
string|"'volumes'"
op|','
name|'vol'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sadd'
op|'('
string|"'volumes:%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'storage_name'
op|')'
op|','
name|'vol'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_restart_exports'
op|'('
op|')'
newline|'\n'
name|'return'
name|'vol'
op|'['
string|"'volume_id'"
op|']'
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
DECL|member|delete_volume
dedent|''
dedent|''
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
string|"'status'"
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
name|'storage_name'
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
name|'vol'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'srem'
op|'('
string|"'volumes'"
op|','
name|'vol'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'srem'
op|'('
string|"'volumes:%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'storage_name'
op|')'
op|','
name|'vol'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_restart_exports
dedent|''
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
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Setting exports to auto: %s"'
op|','
string|'"sudo vblade-persist auto all"'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Starting all exports: %s"'
op|','
string|'"sudo vblade-persist start all"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_init_volume_group
dedent|''
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
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"PVCreate returned: %s"'
op|','
string|'"sudo pvcreate %s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'storage_dev'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"VGCreate returned: %s"'
op|','
string|'"sudo vgcreate %s %s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
name|'FLAGS'
op|'.'
name|'storage_dev'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeBlockStore
dedent|''
dedent|''
name|'class'
name|'FakeBlockStore'
op|'('
name|'BlockStore'
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
name|'super'
op|'('
name|'FakeBlockStore'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_init_volume_group
dedent|''
name|'def'
name|'_init_volume_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_restart_exports
dedent|''
name|'def'
name|'_restart_exports'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Volume
dedent|''
dedent|''
name|'class'
name|'Volume'
op|'('
name|'datastore'
op|'.'
name|'RedisModel'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|object_type
indent|'    '
name|'object_type'
op|'='
string|"'volume'"
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'object_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
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
op|'='
name|'volume_id'
op|')'
newline|'\n'
comment|"#TODO(vish): do we really need to store the volume id as .object_id .volume_id and ['volume_id']?"
nl|'\n'
name|'vol'
op|'['
string|"'volume_id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'vol'
op|'['
string|"'node_name'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'storage_name'
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
string|"'attachTime'"
op|']'
op|'='
string|"'none'"
newline|'\n'
name|'vol'
op|'['
string|'"create_time"'
op|']'
op|'='
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
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
string|"'attachStatus'"
op|']'
op|'='
string|'"detached"'
comment|'# attaching | attached | detaching | detached'
newline|'\n'
name|'vol'
op|'['
string|"'deleteOnTermination'"
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
name|'vol'
op|'.'
name|'create_lv'
op|'('
op|')'
newline|'\n'
name|'vol'
op|'.'
name|'setup_export'
op|'('
op|')'
newline|'\n'
comment|'# TODO(joshua) - We need to trigger a fanout message for aoe-discover on all the nodes'
nl|'\n'
comment|'# TODO(joshua'
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
name|'return'
name|'vol'
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
string|"'attachStatus'"
op|']'
op|'='
string|'"attaching"'
newline|'\n'
name|'self'
op|'['
string|"'attachTime'"
op|']'
op|'='
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'['
string|"'deleteOnTermination'"
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
string|"'attachStatus'"
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
string|"'attachStatus'"
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
string|"'attachStatus'"
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
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_remove_export'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_delete_lv'
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
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_lv
dedent|''
name|'def'
name|'create_lv'
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
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Creating LV: %s"'
op|','
string|'"sudo lvcreate -L %s -n %s %s"'
op|'%'
op|'('
name|'sizestr'
op|','
name|'self'
op|'['
string|"'volume_id'"
op|']'
op|','
name|'FLAGS'
op|'.'
name|'volume_group'
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
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Removing LV: %s"'
op|','
string|'"sudo lvremove -f %s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
name|'self'
op|'.'
name|'volume_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_export
dedent|''
name|'def'
name|'setup_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|'='
name|'get_next_aoe_numbers'
op|'('
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
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Creating AOE export: %s"'
op|','
nl|'\n'
string|'"sudo vblade-persist setup %s %s %s /dev/%s/%s"'
op|'%'
nl|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|','
name|'FLAGS'
op|'.'
name|'aoe_eth_dev'
op|','
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
name|'self'
op|'.'
name|'volume_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_remove_export
dedent|''
name|'def'
name|'_remove_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Stopped AOE export: %s"'
op|','
string|'"sudo vblade-persist stop %s %s"'
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
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Destroyed AOE export: %s"'
op|','
string|'"sudo vblade-persist destroy %s %s"'
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
DECL|member|create_lv
indent|'    '
name|'def'
name|'create_lv'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|setup_export
dedent|''
name|'def'
name|'setup_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(???): This may not be good enough?'
nl|'\n'
indent|'        '
name|'blade_id'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
name|'random'
op|'.'
name|'choice'
op|'('
string|"'0123456789'"
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'3'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'['
string|"'shelf_id'"
op|']'
op|'='
name|'FLAGS'
op|'.'
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
op|'['
string|"'aoe_device'"
op|']'
op|'='
string|'"e%s.%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'shelf_id'
op|','
name|'blade_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_remove_export
dedent|''
name|'def'
name|'_remove_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
nl|'\n'
DECL|function|get_next_aoe_numbers
dedent|''
dedent|''
name|'def'
name|'get_next_aoe_numbers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'aoes'
op|'='
name|'glob'
op|'.'
name|'glob'
op|'('
string|'"/var/lib/vblade-persist/vblades/e*"'
op|')'
newline|'\n'
name|'aoes'
op|'.'
name|'extend'
op|'('
op|'['
string|"'e0.0'"
op|']'
op|')'
newline|'\n'
name|'blade_id'
op|'='
name|'int'
op|'('
name|'max'
op|'('
op|'['
name|'int'
op|'('
name|'a'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
number|'1'
op|']'
op|')'
name|'for'
name|'a'
name|'in'
name|'aoes'
op|']'
op|')'
op|')'
op|'+'
number|'1'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Next blade_id is %s"'
op|'%'
op|'('
name|'blade_id'
op|')'
op|')'
newline|'\n'
name|'shelf_id'
op|'='
name|'FLAGS'
op|'.'
name|'shelf_id'
newline|'\n'
name|'return'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
