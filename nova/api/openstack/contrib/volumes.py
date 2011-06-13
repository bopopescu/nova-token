begin_unit
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""The volumes extension."""'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
name|'volume'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
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
string|'"nova.api.volumes"'
op|')'
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
nl|'\n'
nl|'\n'
DECL|function|_translate_volume_detail_view
name|'def'
name|'_translate_volume_detail_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for volumes details view."""'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'_translate_volume_summary_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
newline|'\n'
nl|'\n'
comment|'# No additional data / lookups at the moment'
nl|'\n'
nl|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_volume_summary_view
dedent|''
name|'def'
name|'_translate_volume_summary_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for volumes summary view."""'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'d'
op|'['
string|"'id'"
op|']'
op|'='
name|'vol'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'status'"
op|']'
op|'='
name|'vol'
op|'['
string|"'status'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'size'"
op|']'
op|'='
name|'vol'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'availabilityZone'"
op|']'
op|'='
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'createdAt'"
op|']'
op|'='
name|'vol'
op|'['
string|"'created_at'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'=='
string|"'attached'"
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'attachments'"
op|']'
op|'='
op|'['
name|'_translate_attachment_detail_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'attachments'"
op|']'
op|'='
op|'['
op|'{'
op|'}'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'d'
op|'['
string|"'displayName'"
op|']'
op|'='
name|'vol'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'displayDescription'"
op|']'
op|'='
name|'vol'
op|'['
string|"'display_description'"
op|']'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeController
dedent|''
name|'class'
name|'VolumeController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Volumes API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"volume"'
op|':'
op|'['
nl|'\n'
string|'"id"'
op|','
nl|'\n'
string|'"status"'
op|','
nl|'\n'
string|'"size"'
op|','
nl|'\n'
string|'"availabilityZone"'
op|','
nl|'\n'
string|'"createdAt"'
op|','
nl|'\n'
string|'"displayName"'
op|','
nl|'\n'
string|'"displayDescription"'
op|','
nl|'\n'
op|']'
op|'}'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'volume_api'
op|'='
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VolumeController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given volume."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'volume'"
op|':'
name|'_translate_volume_detail_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a volume."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Delete volume with id: %s"'
op|')'
op|','
name|'id'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'volume_id'
op|'='
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a summary list of volumes."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_translate_volume_summary_view'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a detailed list of volumes."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_translate_volume_detail_view'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_items
dedent|''
name|'def'
name|'_items'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'entity_maker'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of volumes, transformed through entity_maker."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'limited_list'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'volumes'
op|','
name|'req'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
name|'entity_maker'
op|'('
name|'context'
op|','
name|'vol'
op|')'
name|'for'
name|'vol'
name|'in'
name|'limited_list'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'volumes'"
op|':'
name|'res'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new volume."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vol'
op|'='
name|'body'
op|'['
string|"'volume'"
op|']'
newline|'\n'
name|'size'
op|'='
name|'vol'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Create volume of %s GB"'
op|')'
op|','
name|'size'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'new_volume'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
name|'size'
op|','
name|'None'
op|','
nl|'\n'
name|'vol'
op|'.'
name|'get'
op|'('
string|"'display_name'"
op|')'
op|','
nl|'\n'
name|'vol'
op|'.'
name|'get'
op|'('
string|"'display_description'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Work around problem that instance is lazy-loaded...'
nl|'\n'
name|'new_volume'
op|'['
string|"'instance'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'retval'
op|'='
name|'_translate_volume_detail_view'
op|'('
name|'context'
op|','
name|'new_volume'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'volume'"
op|':'
name|'retval'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_attachment_detail_view
dedent|''
dedent|''
name|'def'
name|'_translate_attachment_detail_view'
op|'('
name|'_context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for attachment details view."""'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'_translate_attachment_summary_view'
op|'('
name|'_context'
op|','
name|'vol'
op|')'
newline|'\n'
nl|'\n'
comment|'# No additional data / lookups at the moment'
nl|'\n'
nl|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_attachment_summary_view
dedent|''
name|'def'
name|'_translate_attachment_summary_view'
op|'('
name|'_context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for attachment summary view."""'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'volume_id'
op|'='
name|'vol'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(justinsb): We use the volume id as the id of the attachment object'
nl|'\n'
name|'d'
op|'['
string|"'id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
nl|'\n'
name|'d'
op|'['
string|"'volumeId'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'if'
name|'vol'
op|'.'
name|'get'
op|'('
string|"'instance_id'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'serverId'"
op|']'
op|'='
name|'vol'
op|'['
string|"'instance_id'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'vol'
op|'.'
name|'get'
op|'('
string|"'mountpoint'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'device'"
op|']'
op|'='
name|'vol'
op|'['
string|"'mountpoint'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeAttachmentController
dedent|''
name|'class'
name|'VolumeAttachmentController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The volume attachment API controller for the Openstack API.\n\n    A child resource of the server.  Note that we use the volume id\n    as the ID of the attachment (though this is not guaranteed externally)\n\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|"'attributes'"
op|':'
op|'{'
nl|'\n'
string|"'volumeAttachment'"
op|':'
op|'['
string|"'id'"
op|','
nl|'\n'
string|"'serverId'"
op|','
nl|'\n'
string|"'volumeId'"
op|','
nl|'\n'
string|"'device'"
op|']'
op|'}'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'='
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VolumeAttachmentController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of volume attachments for a given instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'server_id'
op|','
nl|'\n'
name|'entity_maker'
op|'='
name|'_translate_attachment_summary_view'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given volume attachment."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'volume_id'
op|'='
name|'id'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"volume_id not found"'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'str'
op|'('
name|'vol'
op|'['
string|"'instance_id'"
op|']'
op|')'
op|'!='
name|'server_id'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"instance_id != server_id"'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'volumeAttachment'"
op|':'
name|'_translate_attachment_detail_view'
op|'('
name|'context'
op|','
nl|'\n'
name|'vol'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach a volume to an instance."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_id'
op|'='
name|'server_id'
newline|'\n'
name|'volume_id'
op|'='
name|'body'
op|'['
string|"'volumeAttachment'"
op|']'
op|'['
string|"'volumeId'"
op|']'
newline|'\n'
name|'device'
op|'='
name|'body'
op|'['
string|"'volumeAttachment'"
op|']'
op|'['
string|"'device'"
op|']'
newline|'\n'
nl|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Attach volume %(volume_id)s to instance %(server_id)s"'
nl|'\n'
string|'" at %(device)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'attach_volume'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|','
nl|'\n'
name|'device'
op|'='
name|'device'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# The attach is async'
nl|'\n'
dedent|''
name|'attachment'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'attachment'
op|'['
string|"'id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'attachment'
op|'['
string|"'volumeId'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
nl|'\n'
comment|'# NOTE(justinsb): And now, we have a problem...'
nl|'\n'
comment|"# The attach is async, so there's a window in which we don't see"
nl|'\n'
comment|'# the attachment (until the attachment completes).  We could also'
nl|'\n'
comment|'# get problems with concurrent requests.  I think we need an'
nl|'\n'
comment|"# attachment state, and to write to the DB here, but that's a bigger"
nl|'\n'
comment|'# change.'
nl|'\n'
comment|"# For now, we'll probably have to rely on libraries being smart"
nl|'\n'
nl|'\n'
comment|'# TODO(justinsb): How do I return "accepted" here?'
nl|'\n'
name|'return'
op|'{'
string|"'volumeAttachment'"
op|':'
name|'attachment'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update a volume attachment.  We don\'t currently support this."""'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach a volume from an instance."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'volume_id'
op|'='
name|'id'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Detach volume %s"'
op|')'
op|','
name|'volume_id'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'str'
op|'('
name|'vol'
op|'['
string|"'instance_id'"
op|']'
op|')'
op|'!='
name|'server_id'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"instance_id != server_id"'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'detach_volume'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_items
dedent|''
name|'def'
name|'_items'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'entity_maker'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of attachments, transformed through entity_maker."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'volumes'
op|'='
name|'instance'
op|'['
string|"'volumes'"
op|']'
newline|'\n'
name|'limited_list'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'volumes'
op|','
name|'req'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
name|'entity_maker'
op|'('
name|'context'
op|','
name|'vol'
op|')'
name|'for'
name|'vol'
name|'in'
name|'limited_list'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'volumeAttachments'"
op|':'
name|'res'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Volumes
dedent|''
dedent|''
name|'class'
name|'Volumes'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
DECL|member|get_name
indent|'    '
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Volumes"'
newline|'\n'
nl|'\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"OS-VOLUMES"'
newline|'\n'
nl|'\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Volumes support"'
newline|'\n'
nl|'\n'
DECL|member|get_namespace
dedent|''
name|'def'
name|'get_namespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"http://docs.openstack.org/ext/volumes/api/v1.1"'
newline|'\n'
nl|'\n'
DECL|member|get_updated
dedent|''
name|'def'
name|'get_updated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"2011-03-25T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(justinsb): No way to provide singular name ('volume')"
nl|'\n'
comment|'# Does this matter?'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'volumes'"
op|','
nl|'\n'
name|'VolumeController'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'volume_attachments'"
op|','
nl|'\n'
name|'VolumeAttachmentController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'member_name'
op|'='
string|"'server'"
op|','
nl|'\n'
name|'collection_name'
op|'='
string|"'servers'"
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
