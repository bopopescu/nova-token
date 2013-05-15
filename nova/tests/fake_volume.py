begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""Implementation of a fake volume API."""'
newline|'\n'
nl|'\n'
name|'import'
name|'uuid'
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
name|'import'
name|'exception'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'cinder_cross_az_attach'"
op|','
nl|'\n'
string|"'nova.volume.cinder'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_volume
name|'class'
name|'fake_volume'
op|'('
op|')'
op|':'
newline|'\n'
DECL|variable|user_uuid
indent|'    '
name|'user_uuid'
op|'='
string|"'4a3cd440-b9c2-11e1-afa6-0800200c9a66'"
newline|'\n'
DECL|variable|instance_uuid
name|'instance_uuid'
op|'='
string|"'4a3cd441-b9c2-11e1-afa6-0800200c9a66'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'size'
op|','
name|'name'
op|','
nl|'\n'
name|'description'
op|','
name|'volume_id'
op|','
name|'snapshot'
op|','
nl|'\n'
name|'volume_type'
op|','
name|'metadata'
op|','
nl|'\n'
name|'availability_zone'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot_id'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'snapshot'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'snapshot_id'
op|'='
name|'snapshot'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'volume_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'vol'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'WTF'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'volume_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user_uuid'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake-project-id'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'snapshot_id'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'size'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'availability_zone'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'attach_time'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'attach_status'"
op|':'
string|"'detached'"
op|','
nl|'\n'
string|"'scheduled_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'launched_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'terminated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'provider_location'"
op|':'
string|"'fake-location'"
op|','
nl|'\n'
string|"'provider_auth'"
op|':'
string|"'fake-auth'"
op|','
nl|'\n'
string|"'volume_type_id'"
op|':'
number|'99'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'vol'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'vol'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'vol'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_snapshot
dedent|''
dedent|''
name|'class'
name|'fake_snapshot'
op|'('
op|')'
op|':'
newline|'\n'
DECL|variable|user_uuid
indent|'    '
name|'user_uuid'
op|'='
string|"'4a3cd440-b9c2-11e1-afa6-0800200c9a66'"
newline|'\n'
DECL|variable|instance_uuid
name|'instance_uuid'
op|'='
string|"'4a3cd441-b9c2-11e1-afa6-0800200c9a66'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'volume_id'
op|','
name|'size'
op|','
name|'name'
op|','
name|'desc'
op|','
name|'id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'id'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'snap'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'WTF'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'str'
op|'('
name|'id'
op|')'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume_id'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'creating'"
op|','
nl|'\n'
string|"'progress'"
op|':'
string|"'0%'"
op|','
nl|'\n'
string|"'volume_size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'desc'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user_uuid'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake-project-id'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'snap'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'snap'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'snap'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
dedent|''
dedent|''
name|'class'
name|'API'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|volume_list
indent|'    '
name|'volume_list'
op|'='
op|'['
op|']'
newline|'\n'
DECL|variable|snapshot_list
name|'snapshot_list'
op|'='
op|'['
op|']'
newline|'\n'
DECL|variable|_instance
name|'_instance'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|class|Singleton
name|'class'
name|'Singleton'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'API'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'API'
op|'.'
name|'_instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'API'
op|'.'
name|'_instance'
op|'='
name|'API'
op|'.'
name|'Singleton'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_EventHandler_instance'
op|'='
name|'API'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'size'
op|','
name|'name'
op|','
name|'description'
op|','
name|'snapshot'
op|'='
name|'None'
op|','
nl|'\n'
name|'volume_type'
op|'='
name|'None'
op|','
name|'metadata'
op|'='
name|'None'
op|','
name|'availability_zone'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'v'
op|'='
name|'fake_volume'
op|'('
name|'size'
op|','
name|'name'
op|','
nl|'\n'
name|'description'
op|','
name|'None'
op|','
nl|'\n'
name|'snapshot'
op|','
name|'volume_type'
op|','
nl|'\n'
name|'metadata'
op|','
name|'availability_zone'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_list'
op|'.'
name|'append'
op|'('
name|'v'
op|'.'
name|'vol'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'creating volume %s'"
op|','
name|'v'
op|'.'
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'v'
op|'.'
name|'vol'
newline|'\n'
nl|'\n'
DECL|member|create_with_kwargs
dedent|''
name|'def'
name|'create_with_kwargs'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'volume_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'v'
op|'='
name|'fake_volume'
op|'('
name|'kwargs'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'description'"
op|']'
op|','
nl|'\n'
name|'str'
op|'('
name|'volume_id'
op|')'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
name|'if'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'status'"
op|','
name|'None'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'.'
name|'vol'
op|'['
string|"'status'"
op|']'
op|'='
name|'kwargs'
op|'['
string|"'status'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'kwargs'
op|'['
string|"'host'"
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'.'
name|'vol'
op|'['
string|"'host'"
op|']'
op|'='
name|'kwargs'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'kwargs'
op|'['
string|"'attach_status'"
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'.'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'='
name|'kwargs'
op|'['
string|"'attach_status'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'snapshot_id'"
op|','
name|'None'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'.'
name|'vol'
op|'['
string|"'snapshot_id'"
op|']'
op|'='
name|'kwargs'
op|'['
string|"'snapshot_id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'volume_list'
op|'.'
name|'append'
op|'('
name|'v'
op|'.'
name|'vol'
op|')'
newline|'\n'
name|'return'
name|'v'
op|'.'
name|'vol'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
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
name|'if'
name|'volume_id'
op|'=='
number|'87654321'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'volume_id'
op|','
nl|'\n'
string|"'attach_time'"
op|':'
string|"'13:56:24'"
op|','
nl|'\n'
string|"'attach_status'"
op|':'
string|"'attached'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'in-use'"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'v'
name|'in'
name|'self'
op|'.'
name|'volume_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'v'
op|'['
string|"'id'"
op|']'
op|'=='
name|'str'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'v'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'volume_list'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
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
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'deleting volume %s'"
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_list'
op|'='
op|'['
name|'v'
name|'for'
name|'v'
name|'in'
name|'self'
op|'.'
name|'volume_list'
nl|'\n'
name|'if'
name|'v'
op|'['
string|"'id'"
op|']'
op|'!='
name|'volume_id'
op|']'
newline|'\n'
nl|'\n'
DECL|member|check_attach
dedent|''
name|'def'
name|'check_attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'instance'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'!='
string|"'available'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"status must be available"'
op|')'
newline|'\n'
name|'msg'
op|'='
string|'"%s"'
op|'%'
name|'volume'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'=='
string|"'attached'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"already attached"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'instance'
name|'and'
name|'not'
name|'CONF'
op|'.'
name|'cinder_cross_az_attach'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance'
op|'['
string|"'availability_zone'"
op|']'
op|'!='
name|'volume'
op|'['
string|"'availability_zone'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance and volume not in same availability_zone"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_detach
dedent|''
dedent|''
dedent|''
name|'def'
name|'check_detach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'=='
string|'"available"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"already detached"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach
dedent|''
dedent|''
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_uuid'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'attaching volume %s'"
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'in-use'"
newline|'\n'
name|'volume'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'mountpoint'
newline|'\n'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'attached'"
newline|'\n'
name|'volume'
op|'['
string|"'instance_uuid'"
op|']'
op|'='
name|'instance_uuid'
newline|'\n'
name|'volume'
op|'['
string|"'attach_time'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_set_snapshot_id
dedent|''
name|'def'
name|'fake_set_snapshot_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'['
string|"'snapshot_id'"
op|']'
op|'='
name|'snapshot_id'
newline|'\n'
nl|'\n'
DECL|member|reset_fake_api
dedent|''
name|'def'
name|'reset_fake_api'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'volume_list'
op|'['
op|':'
op|']'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'snapshot_list'
op|'['
op|':'
op|']'
newline|'\n'
nl|'\n'
DECL|member|detach
dedent|''
name|'def'
name|'detach'
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
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'detaching volume %s'"
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'available'"
newline|'\n'
name|'volume'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'detached'"
newline|'\n'
name|'volume'
op|'['
string|"'instance_uuid'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|initialize_connection
dedent|''
name|'def'
name|'initialize_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|','
string|"'data'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|terminate_connection
dedent|''
name|'def'
name|'terminate_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_snapshot
dedent|''
name|'def'
name|'get_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'snap'
name|'in'
name|'self'
op|'.'
name|'snapshot_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'snap'
op|'['
string|"'id'"
op|']'
op|'=='
name|'str'
op|'('
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'snap'
newline|'\n'
nl|'\n'
DECL|member|get_all_snapshots
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_all_snapshots'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'snapshot_list'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot
dedent|''
name|'def'
name|'create_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'name'
op|','
name|'description'
op|','
name|'id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'snapshot'
op|'='
name|'fake_snapshot'
op|'('
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
name|'volume'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'name'
op|','
name|'description'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'snapshot_list'
op|'.'
name|'append'
op|'('
name|'snapshot'
op|'.'
name|'snap'
op|')'
newline|'\n'
name|'return'
name|'snapshot'
op|'.'
name|'snap'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot_with_kwargs
dedent|''
name|'def'
name|'create_snapshot_with_kwargs'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot'
op|'='
name|'fake_snapshot'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'volume_id'"
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'volume_size'"
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'description'"
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'snap_id'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'status'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'status'"
op|','
name|'None'
op|')'
newline|'\n'
name|'snapshot'
op|'.'
name|'snap'
op|'['
string|"'status'"
op|']'
op|'='
name|'status'
newline|'\n'
name|'self'
op|'.'
name|'snapshot_list'
op|'.'
name|'append'
op|'('
name|'snapshot'
op|'.'
name|'snap'
op|')'
newline|'\n'
name|'return'
name|'snapshot'
op|'.'
name|'snap'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot_force
dedent|''
name|'def'
name|'create_snapshot_force'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'name'
op|','
name|'description'
op|','
name|'id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'snapshot'
op|'='
name|'fake_snapshot'
op|'('
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
name|'volume'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'name'
op|','
name|'description'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'snapshot_list'
op|'.'
name|'append'
op|'('
name|'snapshot'
op|'.'
name|'snap'
op|')'
newline|'\n'
name|'return'
name|'snapshot'
op|'.'
name|'snap'
newline|'\n'
nl|'\n'
DECL|member|delete_snapshot
dedent|''
name|'def'
name|'delete_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'snapshot_list'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'self'
op|'.'
name|'snapshot_list'
nl|'\n'
name|'if'
name|'s'
op|'['
string|"'id'"
op|']'
op|'!='
name|'snapshot_id'
op|']'
newline|'\n'
nl|'\n'
DECL|member|reserve_volume
dedent|''
name|'def'
name|'reserve_volume'
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
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'reserving volume %s'"
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'attaching'"
newline|'\n'
nl|'\n'
DECL|member|unreserve_volume
dedent|''
name|'def'
name|'unreserve_volume'
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
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'unreserving volume %s'"
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'available'"
newline|'\n'
nl|'\n'
DECL|member|begin_detaching
dedent|''
name|'def'
name|'begin_detaching'
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
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'beging detaching volume %s'"
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'detaching'"
newline|'\n'
nl|'\n'
DECL|member|roll_detaching
dedent|''
name|'def'
name|'roll_detaching'
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
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'roll detaching volume %s'"
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'in-use'"
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
