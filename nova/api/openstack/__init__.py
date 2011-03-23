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
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'accounts'
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
name|'import'
name|'backup_schedules'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'consoles'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'limits'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'shared_ip_groups'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'users'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'zones'
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
string|"'nova.api.openstack'"
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
nl|'\n'
nl|'\n'
DECL|class|FaultWrapper
name|'class'
name|'FaultWrapper'
op|'('
name|'wsgi'
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
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIRouter
dedent|''
dedent|''
dedent|''
name|'class'
name|'APIRouter'
op|'('
name|'wsgi'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'server_members'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
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
DECL|member|_setup_routes
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
string|"'pause'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'server_members'
op|'['
string|"'unpause'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
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
name|'server_members'
op|'['
string|"'suspend'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'server_members'
op|'['
string|"'resume'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'server_members'
op|'['
string|"'rescue'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'server_members'
op|'['
string|"'unrescue'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'server_members'
op|'['
string|"'reset_network'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'server_members'
op|'['
string|"'inject_network_info'"
op|']'
op|'='
string|"'POST'"
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
name|'controller'
op|'='
name|'zones'
op|'.'
name|'Controller'
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
string|"'info'"
op|':'
string|"'GET'"
op|'}'
op|')'
op|','
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
name|'controller'
op|'='
name|'users'
op|'.'
name|'Controller'
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
name|'Controller'
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
dedent|''
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"backup_schedule"'
op|','
string|'"backup_schedule"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'backup_schedules'
op|'.'
name|'Controller'
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
string|'"console"'
op|','
string|'"consoles"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'consoles'
op|'.'
name|'Controller'
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
name|'controller'
op|'='
name|'images'
op|'.'
name|'Controller'
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
string|'"flavor"'
op|','
string|'"flavors"'
op|','
name|'controller'
op|'='
name|'flavors'
op|'.'
name|'Controller'
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
string|'"shared_ip_group"'
op|','
string|'"shared_ip_groups"'
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
name|'controller'
op|'='
name|'shared_ip_groups'
op|'.'
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'_limits'
op|'='
name|'limits'
op|'.'
name|'LimitsController'
op|'('
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"limit"'
op|','
string|'"limits"'
op|','
name|'controller'
op|'='
name|'_limits'
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
DECL|class|APIRouterV10
dedent|''
dedent|''
name|'class'
name|'APIRouterV10'
op|'('
name|'APIRouter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Define routes specific to OpenStack API V1.0."""'
newline|'\n'
nl|'\n'
DECL|member|_setup_routes
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
name|'super'
op|'('
name|'APIRouterV10'
op|','
name|'self'
op|')'
op|'.'
name|'_setup_routes'
op|'('
name|'mapper'
op|')'
newline|'\n'
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
name|'ControllerV10'
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
nl|'\n'
DECL|class|APIRouterV11
dedent|''
dedent|''
name|'class'
name|'APIRouterV11'
op|'('
name|'APIRouter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Define routes specific to OpenStack API V1.1."""'
newline|'\n'
nl|'\n'
DECL|member|_setup_routes
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
name|'super'
op|'('
name|'APIRouterV11'
op|','
name|'self'
op|')'
op|'.'
name|'_setup_routes'
op|'('
name|'mapper'
op|')'
newline|'\n'
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
name|'ControllerV11'
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
nl|'\n'
DECL|class|Versions
dedent|''
dedent|''
name|'class'
name|'Versions'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
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
string|'"""Respond to a request for all OpenStack API versions."""'
newline|'\n'
name|'response'
op|'='
op|'{'
nl|'\n'
string|'"versions"'
op|':'
op|'['
nl|'\n'
name|'dict'
op|'('
name|'status'
op|'='
string|'"DEPRECATED"'
op|','
name|'id'
op|'='
string|'"v1.0"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'status'
op|'='
string|'"CURRENT"'
op|','
name|'id'
op|'='
string|'"v1.1"'
op|')'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"application/xml"'
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
name|'dict'
op|'('
name|'version'
op|'='
op|'['
string|'"status"'
op|','
string|'"id"'
op|']'
op|')'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'content_type'
op|'='
name|'req'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Serializer'
op|'('
name|'metadata'
op|')'
op|'.'
name|'serialize'
op|'('
name|'response'
op|','
name|'content_type'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
