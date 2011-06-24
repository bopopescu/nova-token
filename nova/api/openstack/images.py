begin_unit
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
name|'import'
name|'webob'
op|'.'
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
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'faults'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
name|'import'
name|'images'
name|'as'
name|'images_view'
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
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.images'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|SUPPORTED_FILTERS
name|'SUPPORTED_FILTERS'
op|'='
op|'['
string|"'name'"
op|','
string|"'status'"
op|']'
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
string|'"""Base controller for retrieving/displaying images."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'image_service'
op|'='
name|'None'
op|','
name|'compute_service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize new `ImageController`.\n\n        :param compute_service: `nova.compute.api:API`\n        :param image_service: `nova.image.service:BaseImageService`\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_compute_service'
op|'='
name|'compute_service'
name|'or'
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_image_service'
op|'='
name|'image_service'
name|'or'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'get_default_image_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_filters
dedent|''
name|'def'
name|'_get_filters'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a dictionary of query param filters from the request\n\n        :param req: the Request object coming from the wsgi layer\n        :retval a dict of key/value filters\n        """'
newline|'\n'
name|'filters'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'param'
name|'in'
name|'req'
op|'.'
name|'str_params'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'param'
name|'in'
name|'SUPPORTED_FILTERS'
name|'or'
name|'param'
op|'.'
name|'startswith'
op|'('
string|"'property-'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'filters'
op|'['
name|'param'
op|']'
op|'='
name|'req'
op|'.'
name|'str_params'
op|'.'
name|'get'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'filters'
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
string|'"""Return detailed information about a specific image.\n\n        :param req: `wsgi.Request` object\n        :param id: Image identifier\n        """'
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
name|'image'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
name|'exception'
op|'.'
name|'InvalidImageRef'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Image not found."'
op|')'
newline|'\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'explanation'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'image'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete an image, if allowed.\n\n        :param req: `wsgi.Request` object\n        :param id: Image identifier (integer)\n        """'
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
name|'_image_service'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNoContent'
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
string|'"""Snapshot or backup a server instance and save the image.\n\n        Images now have an `image_type` associated with them, which can be\n        \'snapshot\' or the backup type, like \'daily\' or \'weekly\'.\n\n        If the image_type is backup-like, then the rotation factor can be\n        included and that will cause the oldest backups that exceed the\n        rotation factor to be deleted.\n\n        :param req: `wsgi.Request` object\n        """'
newline|'\n'
DECL|function|get_param
name|'def'
name|'get_param'
op|'('
name|'param'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'body'
op|'['
string|'"image"'
op|']'
op|'['
name|'param'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
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
name|'content_type'
op|'='
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'body'
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
name|'image_type'
op|'='
name|'body'
op|'['
string|'"image"'
op|']'
op|'.'
name|'get'
op|'('
string|'"image_type"'
op|','
string|'"snapshot"'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server_id'
op|'='
name|'self'
op|'.'
name|'_server_id_from_req_data'
op|'('
name|'body'
op|')'
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
name|'image_name'
op|'='
name|'get_param'
op|'('
string|'"name"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'image_type'
op|'=='
string|'"snapshot"'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'_compute_service'
op|'.'
name|'snapshot'
op|'('
nl|'\n'
name|'context'
op|','
name|'server_id'
op|','
name|'image_name'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'image_type'
op|'=='
string|'"backup"'
op|':'
newline|'\n'
comment|'# NOTE(sirp): Unlike snapshot, backup is not a customer facing'
nl|'\n'
comment|"# API call; rather, it's used by the internal backup scheduler"
nl|'\n'
indent|'            '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|':'
newline|'\n'
indent|'                '
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
name|'backup_type'
op|'='
name|'get_param'
op|'('
string|'"backup_type"'
op|')'
newline|'\n'
name|'rotation'
op|'='
name|'int'
op|'('
name|'get_param'
op|'('
string|'"rotation"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_compute_service'
op|'.'
name|'backup'
op|'('
nl|'\n'
name|'context'
op|','
name|'server_id'
op|','
name|'image_name'
op|','
nl|'\n'
name|'backup_type'
op|','
name|'rotation'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Invalid image_type \'%s\' passed"'
op|')'
op|'%'
name|'image_type'
op|')'
newline|'\n'
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
name|'return'
name|'dict'
op|'('
name|'image'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_builder
dedent|''
name|'def'
name|'get_builder'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Indicates that you must use a Controller subclass."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_server_id_from_req_data
dedent|''
name|'def'
name|'_server_id_from_req_data'
op|'('
name|'self'
op|','
name|'data'
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
nl|'\n'
DECL|class|ControllerV10
dedent|''
dedent|''
name|'class'
name|'ControllerV10'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Version 1.0 specific controller logic."""'
newline|'\n'
nl|'\n'
DECL|member|get_builder
name|'def'
name|'get_builder'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Property to get the ViewBuilder class we need to use."""'
newline|'\n'
name|'base_url'
op|'='
name|'request'
op|'.'
name|'application_url'
newline|'\n'
name|'return'
name|'images_view'
op|'.'
name|'ViewBuilderV10'
op|'('
name|'base_url'
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
string|'"""Return an index listing of images available to the request.\n\n        :param req: `wsgi.Request` object\n\n        """'
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
name|'filters'
op|'='
name|'self'
op|'.'
name|'_get_filters'
op|'('
name|'req'
op|')'
newline|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'index'
op|'('
name|'context'
op|','
name|'filters'
op|')'
newline|'\n'
name|'images'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'images'
op|','
name|'req'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'False'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
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
string|'"""Return a detailed index listing of images available to the request.\n\n        :param req: `wsgi.Request` object.\n\n        """'
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
name|'filters'
op|'='
name|'self'
op|'.'
name|'_get_filters'
op|'('
name|'req'
op|')'
newline|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'detail'
op|'('
name|'context'
op|','
name|'filters'
op|')'
newline|'\n'
name|'images'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'images'
op|','
name|'req'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_server_id_from_req_data
dedent|''
name|'def'
name|'_server_id_from_req_data'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'data'
op|'['
string|"'image'"
op|']'
op|'['
string|"'serverId'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerV11
dedent|''
dedent|''
name|'class'
name|'ControllerV11'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Version 1.1 specific controller logic."""'
newline|'\n'
nl|'\n'
DECL|member|get_builder
name|'def'
name|'get_builder'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Property to get the ViewBuilder class we need to use."""'
newline|'\n'
name|'base_url'
op|'='
name|'request'
op|'.'
name|'application_url'
newline|'\n'
name|'return'
name|'images_view'
op|'.'
name|'ViewBuilderV11'
op|'('
name|'base_url'
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
string|'"""Return an index listing of images available to the request.\n\n        :param req: `wsgi.Request` object\n\n        """'
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
name|'filters'
op|'='
name|'self'
op|'.'
name|'_get_filters'
op|'('
name|'req'
op|')'
newline|'\n'
op|'('
name|'marker'
op|','
name|'limit'
op|')'
op|'='
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
newline|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'index'
op|'('
nl|'\n'
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|','
name|'marker'
op|'='
name|'marker'
op|','
name|'limit'
op|'='
name|'limit'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'False'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
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
string|'"""Return a detailed index listing of images available to the request.\n\n        :param req: `wsgi.Request` object.\n\n        """'
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
name|'filters'
op|'='
name|'self'
op|'.'
name|'_get_filters'
op|'('
name|'req'
op|')'
newline|'\n'
op|'('
name|'marker'
op|','
name|'limit'
op|')'
op|'='
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
newline|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'detail'
op|'('
nl|'\n'
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|','
name|'marker'
op|'='
name|'marker'
op|','
name|'limit'
op|'='
name|'limit'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_server_id_from_req_data
dedent|''
name|'def'
name|'_server_id_from_req_data'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'data'
op|'['
string|"'image'"
op|']'
op|'['
string|"'serverRef'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
name|'version'
op|'='
string|"'1.0'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'controller'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'ControllerV10'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'ControllerV11'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'xmlns'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'wsgi'
op|'.'
name|'XMLNS_V10'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"image"'
op|':'
op|'['
string|'"id"'
op|','
string|'"name"'
op|','
string|'"updated"'
op|','
string|'"created"'
op|','
string|'"status"'
op|','
nl|'\n'
string|'"serverId"'
op|','
string|'"progress"'
op|','
string|'"serverRef"'
op|']'
op|','
nl|'\n'
string|'"link"'
op|':'
op|'['
string|'"rel"'
op|','
string|'"type"'
op|','
string|'"href"'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'xmlns'
op|'='
name|'xmlns'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'controller'
op|','
name|'serializers'
op|'='
name|'serializers'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
