begin_unit
comment|'# Copyright 2013 Red Hat, Inc.'
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
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
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
name|'wsgi'
newline|'\n'
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
op|'.'
name|'i18n'
name|'import'
name|'_LI'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'os-assisted-volume-snapshots'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AssistedVolumeSnapshotsController
name|'class'
name|'AssistedVolumeSnapshotsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
name|'super'
op|'('
name|'AssistedVolumeSnapshotsController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
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
string|'"""Creates a new snapshot."""'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'create'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'snapshot'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'snapshot'
op|'='
name|'body'
op|'['
string|"'snapshot'"
op|']'
newline|'\n'
name|'create_info'
op|'='
name|'snapshot'
op|'['
string|"'create_info'"
op|']'
newline|'\n'
name|'volume_id'
op|'='
name|'snapshot'
op|'['
string|"'volume_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Create assisted snapshot from volume %s"'
op|')'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'volume_snapshot_create'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'create_info'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a snapshot."""'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'delete'"
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Delete snapshot with id: %s"'
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
name|'delete_metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'delete_metadata'
op|'.'
name|'update'
op|'('
name|'req'
op|'.'
name|'GET'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'delete_info'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'delete_metadata'
op|'['
string|"'delete_info'"
op|']'
op|')'
newline|'\n'
name|'volume_id'
op|'='
name|'delete_info'
op|'['
string|"'volume_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'ValueError'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'volume_snapshot_delete'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'id'
op|','
name|'delete_info'
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
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'204'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Assisted_volume_snapshots
dedent|''
dedent|''
name|'class'
name|'Assisted_volume_snapshots'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Assisted volume snapshots."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"AssistedVolumeSnapshots"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-assisted-volume-snapshots"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"assisted-volume-snapshots/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2013-08-29T00:00:00Z"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-assisted-volume-snapshots'"
op|','
nl|'\n'
name|'AssistedVolumeSnapshotsController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'resource'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit