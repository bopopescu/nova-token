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
string|'"""\nWSGI middleware for OpenStack API controllers.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'accounts'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'consoles'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'image_metadata'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'ips'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'limits'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'server_metadata'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'users'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'versions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'zones'
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
name|'wsgi'
name|'as'
name|'base_wsgi'
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
string|"'nova.api.openstack.v2'"
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
name|'DEFINE_bool'
op|'('
string|"'allow_admin_api'"
op|','
nl|'\n'
name|'False'
op|','
nl|'\n'
string|"'When True, this API service will accept admin operations.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'allow_instance_snapshots'"
op|','
nl|'\n'
name|'True'
op|','
nl|'\n'
string|"'When True, this API service will permit instance snapshot operations.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FaultWrapper
name|'class'
name|'FaultWrapper'
op|'('
name|'base_wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Calls down the middleware stack, making exceptions into faults."""'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Caught error: %s"'
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
op|')'
newline|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIMapper
dedent|''
dedent|''
dedent|''
name|'class'
name|'APIMapper'
op|'('
name|'routes'
op|'.'
name|'Mapper'
op|')'
op|':'
newline|'\n'
DECL|member|routematch
indent|'    '
name|'def'
name|'routematch'
op|'('
name|'self'
op|','
name|'url'
op|'='
name|'None'
op|','
name|'environ'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'url'
name|'is'
string|'""'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'_match'
op|'('
string|'""'
op|','
name|'environ'
op|')'
newline|'\n'
name|'return'
name|'result'
op|'['
number|'0'
op|']'
op|','
name|'result'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'routes'
op|'.'
name|'Mapper'
op|'.'
name|'routematch'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'environ'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectMapper
dedent|''
dedent|''
name|'class'
name|'ProjectMapper'
op|'('
name|'APIMapper'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|resource
indent|'    '
name|'def'
name|'resource'
op|'('
name|'self'
op|','
name|'member_name'
op|','
name|'collection_name'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
op|'('
string|"'parent_resource'"
name|'in'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'path_prefix'"
op|']'
op|'='
string|"'{project_id}/'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'parent_resource'
op|'='
name|'kwargs'
op|'['
string|"'parent_resource'"
op|']'
newline|'\n'
name|'p_collection'
op|'='
name|'parent_resource'
op|'['
string|"'collection_name'"
op|']'
newline|'\n'
name|'p_member'
op|'='
name|'parent_resource'
op|'['
string|"'member_name'"
op|']'
newline|'\n'
name|'kwargs'
op|'['
string|"'path_prefix'"
op|']'
op|'='
string|"'{project_id}/%s/:%s_id'"
op|'%'
op|'('
name|'p_collection'
op|','
nl|'\n'
name|'p_member'
op|')'
newline|'\n'
dedent|''
name|'routes'
op|'.'
name|'Mapper'
op|'.'
name|'resource'
op|'('
name|'self'
op|','
name|'member_name'
op|','
nl|'\n'
name|'collection_name'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIRouter
dedent|''
dedent|''
name|'class'
name|'APIRouter'
op|'('
name|'base_wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Routes requests on the OpenStack API to the appropriate controller\n    and method.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_config'
op|','
op|'**'
name|'local_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simple paste factory, :class:`nova.wsgi.Router` doesn\'t have one"""'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ext_mgr'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'ext_mgr'
op|'='
name|'extensions'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'server_members'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'mapper'
op|'='
name|'ProjectMapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_routes'
op|'('
name|'mapper'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_ext_routes'
op|'('
name|'mapper'
op|','
name|'ext_mgr'
op|')'
newline|'\n'
name|'super'
op|'('
name|'APIRouter'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'mapper'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_ext_routes
dedent|''
name|'def'
name|'_setup_ext_routes'
op|'('
name|'self'
op|','
name|'mapper'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
nl|'\n'
op|'{'
string|"'application/xml'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'resource'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_resources'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extended resource: %s'"
op|')'
op|','
nl|'\n'
name|'resource'
op|'.'
name|'collection'
op|')'
newline|'\n'
name|'if'
name|'resource'
op|'.'
name|'serializer'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'resource'
op|'.'
name|'serializer'
op|'='
name|'serializer'
newline|'\n'
nl|'\n'
dedent|''
name|'kargs'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'controller'
op|'='
name|'wsgi'
op|'.'
name|'Resource'
op|'('
nl|'\n'
name|'resource'
op|'.'
name|'controller'
op|','
name|'resource'
op|'.'
name|'deserializer'
op|','
nl|'\n'
name|'resource'
op|'.'
name|'serializer'
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
name|'resource'
op|'.'
name|'collection_actions'
op|','
nl|'\n'
name|'member'
op|'='
name|'resource'
op|'.'
name|'member_actions'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'resource'
op|'.'
name|'parent'
op|':'
newline|'\n'
indent|'                '
name|'kargs'
op|'['
string|"'parent_resource'"
op|']'
op|'='
name|'resource'
op|'.'
name|'parent'
newline|'\n'
nl|'\n'
dedent|''
name|'mapper'
op|'.'
name|'resource'
op|'('
name|'resource'
op|'.'
name|'collection'
op|','
name|'resource'
op|'.'
name|'collection'
op|','
op|'**'
name|'kargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_routes
dedent|''
dedent|''
name|'def'
name|'_setup_routes'
op|'('
name|'self'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_members'
op|'='
name|'self'
op|'.'
name|'server_members'
newline|'\n'
name|'server_members'
op|'['
string|"'action'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Including admin operations in API."'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'server_members'
op|'['
string|"'diagnostics'"
op|']'
op|'='
string|"'GET'"
newline|'\n'
name|'server_members'
op|'['
string|"'actions'"
op|']'
op|'='
string|"'GET'"
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"user"'
op|','
string|'"users"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'users'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"account"'
op|','
string|'"accounts"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'accounts'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"zone"'
op|','
string|'"zones"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'zones'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'info'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'select'"
op|':'
string|"'POST'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"versions"'
op|','
string|'"/"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'versions'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'action'
op|'='
string|"'show'"
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'redirect'
op|'('
string|'""'
op|','
string|'"/"'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"console"'
op|','
string|'"consoles"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'consoles'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'parent_resource'
op|'='
name|'dict'
op|'('
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
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"server"'
op|','
string|'"servers"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'servers'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|','
nl|'\n'
name|'member'
op|'='
name|'self'
op|'.'
name|'server_members'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"ip"'
op|','
string|'"ips"'
op|','
name|'controller'
op|'='
name|'ips'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'parent_resource'
op|'='
name|'dict'
op|'('
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
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"image"'
op|','
string|'"images"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'images'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"limit"'
op|','
string|'"limits"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'limits'
op|'.'
name|'create_resource'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"flavor"'
op|','
string|'"flavors"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'flavors'
op|'.'
name|'create_resource'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'image_metadata_controller'
op|'='
name|'image_metadata'
op|'.'
name|'create_resource'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"image_meta"'
op|','
string|'"metadata"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'image_metadata_controller'
op|','
nl|'\n'
name|'parent_resource'
op|'='
name|'dict'
op|'('
name|'member_name'
op|'='
string|"'image'"
op|','
nl|'\n'
name|'collection_name'
op|'='
string|"'images'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"metadata"'
op|','
string|'"/{project_id}/images/{image_id}/metadata"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'image_metadata_controller'
op|','
nl|'\n'
name|'action'
op|'='
string|"'update_all'"
op|','
nl|'\n'
name|'conditions'
op|'='
op|'{'
string|'"method"'
op|':'
op|'['
string|"'PUT'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'server_metadata_controller'
op|'='
name|'server_metadata'
op|'.'
name|'create_resource'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"server_meta"'
op|','
string|'"metadata"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'server_metadata_controller'
op|','
nl|'\n'
name|'parent_resource'
op|'='
name|'dict'
op|'('
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
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"metadata"'
op|','
nl|'\n'
string|'"/{project_id}/servers/{server_id}/metadata"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'server_metadata_controller'
op|','
nl|'\n'
name|'action'
op|'='
string|"'update_all'"
op|','
nl|'\n'
name|'conditions'
op|'='
op|'{'
string|'"method"'
op|':'
op|'['
string|"'PUT'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
