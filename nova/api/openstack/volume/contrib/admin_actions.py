begin_unit
comment|'#   Copyright 2012 OpenStack, LLC.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
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
name|'db'
newline|'\n'
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
name|'import'
name|'volume'
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
nl|'\n'
DECL|class|AdminController
name|'class'
name|'AdminController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstract base class for AdminControllers."""'
newline|'\n'
nl|'\n'
DECL|variable|collection
name|'collection'
op|'='
name|'None'
comment|'# api collection to extend'
newline|'\n'
nl|'\n'
comment|'# FIXME(clayg): this will be hard to keep up-to-date'
nl|'\n'
comment|'# Concrete classes can expand or over-ride'
nl|'\n'
DECL|variable|valid_status
name|'valid_status'
op|'='
name|'set'
op|'('
op|'['
nl|'\n'
string|"'creating'"
op|','
nl|'\n'
string|"'available'"
op|','
nl|'\n'
string|"'deleting'"
op|','
nl|'\n'
string|"'error'"
op|','
nl|'\n'
string|"'error_deleting'"
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'super'
op|'('
name|'AdminController'
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
comment|'# singular name of the resource'
nl|'\n'
name|'self'
op|'.'
name|'resource_name'
op|'='
name|'self'
op|'.'
name|'collection'
op|'.'
name|'rstrip'
op|'('
string|"'s'"
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
nl|'\n'
DECL|member|_update
dedent|''
name|'def'
name|'_update'
op|'('
name|'self'
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
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_status
dedent|''
name|'def'
name|'_validate_status'
op|'('
name|'self'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'status'
name|'not'
name|'in'
name|'self'
op|'.'
name|'valid_status'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
string|'"Must specify a valid status"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|authorize
dedent|''
dedent|''
name|'def'
name|'authorize'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'action_name'
op|')'
op|':'
newline|'\n'
comment|'# e.g. "snapshot_admin_actions:reset_status"'
nl|'\n'
indent|'        '
name|'action'
op|'='
string|"'%s_admin_actions:%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'resource_name'
op|','
name|'action_name'
op|')'
newline|'\n'
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'volume'"
op|','
name|'action'
op|')'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'os-reset_status'"
op|')'
newline|'\n'
DECL|member|_reset_status
name|'def'
name|'_reset_status'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reset status on the resource."""'
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
name|'self'
op|'.'
name|'authorize'
op|'('
name|'context'
op|','
string|"'reset_status'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'new_status'
op|'='
name|'body'
op|'['
string|"'os-reset_status'"
op|']'
op|'['
string|"'status'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
string|'"Must specify \'status\'"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_validate_status'
op|'('
name|'new_status'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Updating status of %(resource)s \'%(id)s\' to \'%(status)s\'"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
op|'{'
string|"'resource'"
op|':'
name|'self'
op|'.'
name|'resource_name'
op|','
string|"'id'"
op|':'
name|'id'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'new_status'
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_update'
op|'('
name|'context'
op|','
name|'id'
op|','
op|'{'
string|"'status'"
op|':'
name|'new_status'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'e'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeAdminController
dedent|''
dedent|''
name|'class'
name|'VolumeAdminController'
op|'('
name|'AdminController'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AdminController for Volumes."""'
newline|'\n'
nl|'\n'
DECL|variable|collection
name|'collection'
op|'='
string|"'volumes'"
newline|'\n'
DECL|variable|valid_status
name|'valid_status'
op|'='
name|'AdminController'
op|'.'
name|'valid_status'
op|'.'
name|'union'
op|'('
nl|'\n'
name|'set'
op|'('
op|'['
string|"'attaching'"
op|','
string|"'in-use'"
op|','
string|"'detaching'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_update
name|'def'
name|'_update'
op|'('
name|'self'
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
name|'db'
op|'.'
name|'volume_update'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'os-force_delete'"
op|')'
newline|'\n'
DECL|member|_force_delete
name|'def'
name|'_force_delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a resource, bypassing the check that it must be available."""'
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
name|'self'
op|'.'
name|'authorize'
op|'('
name|'context'
op|','
string|"'force_delete'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume'
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
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'volume'
op|','
name|'force'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SnapshotAdminController
dedent|''
dedent|''
name|'class'
name|'SnapshotAdminController'
op|'('
name|'AdminController'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AdminController for Snapshots."""'
newline|'\n'
nl|'\n'
DECL|variable|collection
name|'collection'
op|'='
string|"'snapshots'"
newline|'\n'
nl|'\n'
DECL|member|_update
name|'def'
name|'_update'
op|'('
name|'self'
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
name|'db'
op|'.'
name|'snapshot_update'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Admin_actions
dedent|''
dedent|''
name|'class'
name|'Admin_actions'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Enable admin actions."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"AdminActions"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-admin-actions"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/volume/ext/admin-actions/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-08-25T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'class_'
name|'in'
op|'('
name|'VolumeAdminController'
op|','
name|'SnapshotAdminController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'controller'
op|'='
name|'class_'
op|'('
op|')'
newline|'\n'
name|'extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
name|'class_'
op|'.'
name|'collection'
op|','
name|'controller'
op|')'
newline|'\n'
name|'exts'
op|'.'
name|'append'
op|'('
name|'extension'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exts'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
