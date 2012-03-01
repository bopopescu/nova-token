begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'common'
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
nl|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" The server metadata API controller for the Openstack API """'
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
name|'super'
op|'('
name|'Controller'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_metadata
dedent|''
name|'def'
name|'_get_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server'
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
name|'meta'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instance_metadata'
op|'('
name|'context'
op|','
name|'server'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Server does not exist'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'meta_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'meta'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'meta_dict'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'return'
name|'meta_dict'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetadataTemplate'
op|')'
newline|'\n'
DECL|member|index
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
string|'""" Returns the list of metadata for a given instance """'
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
name|'return'
op|'{'
string|"'metadata'"
op|':'
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetadataTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetadataDeserializer'
op|')'
newline|'\n'
DECL|member|create
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'body'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Malformed request body"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'new_metadata'
op|'='
name|'self'
op|'.'
name|'_update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'metadata'"
op|':'
name|'new_metadata'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetaItemTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetaItemDeserializer'
op|')'
newline|'\n'
DECL|member|update
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'meta_item'
op|'='
name|'body'
op|'['
string|"'meta'"
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
name|'expl'
op|'='
name|'_'
op|'('
string|"'Malformed request body'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'id'
name|'not'
name|'in'
name|'meta_item'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Request body and URI mismatch'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'meta_item'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Request body contains too many items'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'_update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'meta_item'
op|','
nl|'\n'
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'meta'"
op|':'
name|'meta_item'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetadataTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetadataDeserializer'
op|')'
newline|'\n'
DECL|member|update_all
name|'def'
name|'update_all'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'body'
op|'['
string|"'metadata'"
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
name|'expl'
op|'='
name|'_'
op|'('
string|"'Malformed request body'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'new_metadata'
op|'='
name|'self'
op|'.'
name|'_update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'metadata'"
op|':'
name|'new_metadata'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_update_instance_metadata
dedent|''
name|'def'
name|'_update_instance_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_id'
op|','
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server'
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
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Server does not exist'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Malformed request body"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'QuotaError'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_handle_quota_error'
op|'('
name|'error'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'common'
op|'.'
name|'MetaItemTemplate'
op|')'
newline|'\n'
DECL|member|show
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
string|'""" Return a single metadata item """'
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
name|'data'
op|'='
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'meta'"
op|':'
op|'{'
name|'id'
op|':'
name|'data'
op|'['
name|'id'
op|']'
op|'}'
op|'}'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Metadata item was not found"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'204'
op|')'
newline|'\n'
DECL|member|delete
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
string|'""" Deletes an existing metadata """'
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
name|'metadata'
op|'='
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Metadata item was not found"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server'
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
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'delete_instance_metadata'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Server does not exist'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_handle_quota_error
dedent|''
dedent|''
name|'def'
name|'_handle_quota_error'
op|'('
name|'self'
op|','
name|'error'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reraise quota errors as api-specific http exceptions."""'
newline|'\n'
name|'if'
name|'error'
op|'.'
name|'kwargs'
op|'['
string|"'code'"
op|']'
op|'=='
string|'"MetadataLimitExceeded"'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
name|'explanation'
op|'='
name|'error'
op|'.'
name|'message'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'error'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
