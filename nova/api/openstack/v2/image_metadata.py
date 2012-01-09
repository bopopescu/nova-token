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
name|'image'
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
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The image metadata API controller for the Openstack API"""'
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
name|'image_service'
op|'='
name|'image'
op|'.'
name|'get_default_image_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_image
dedent|''
name|'def'
name|'_get_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
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
name|'msg'
op|'='
name|'_'
op|'('
string|'"Image not found."'
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
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of metadata for a given instance"""'
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
name|'metadata'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|'['
string|"'properties'"
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|')'
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
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'image_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'metadata'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|'['
string|"'properties'"
op|']'
newline|'\n'
name|'if'
name|'id'
name|'in'
name|'metadata'
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
name|'metadata'
op|'['
name|'id'
op|']'
op|'}'
op|'}'
newline|'\n'
dedent|''
name|'else'
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
name|'image_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'if'
string|"'metadata'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'body'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'image'
op|'['
string|"'properties'"
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'common'
op|'.'
name|'check_img_metadata_quota_limit'
op|'('
name|'context'
op|','
name|'image'
op|'['
string|"'properties'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'metadata'
op|'='
name|'image'
op|'['
string|"'properties'"
op|']'
op|')'
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
name|'image_id'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'meta'
op|'='
name|'body'
op|'['
string|"'meta'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Incorrect request body format'"
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
name|'not'
name|'id'
name|'in'
name|'meta'
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
dedent|''
name|'if'
name|'len'
op|'('
name|'meta'
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
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'image'
op|'['
string|"'properties'"
op|']'
op|'['
name|'id'
op|']'
op|'='
name|'meta'
op|'['
name|'id'
op|']'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_quota_limit'
op|'('
name|'context'
op|','
name|'image'
op|'['
string|"'properties'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'meta'
op|'='
name|'meta'
op|')'
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
name|'image_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_quota_limit'
op|'('
name|'context'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'image'
op|'['
string|"'properties'"
op|']'
op|'='
name|'metadata'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
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
name|'image_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'id'
name|'in'
name|'image'
op|'['
string|"'properties'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid metadata key"'
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
dedent|''
name|'image'
op|'['
string|"'properties'"
op|']'
op|'.'
name|'pop'
op|'('
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'None'
op|')'
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
