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
string|'"""\nWSGI middleware for OpenStack Volume API.\n"""'
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
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'volume'
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
name|'volume'
name|'import'
name|'snapshots'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'volume'
name|'import'
name|'types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'volume'
name|'import'
name|'volumes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'volume'
name|'import'
name|'versions'
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
string|"'nova.api.openstack.volume'"
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
nl|'\n'
DECL|class|APIRouter
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
name|'mapper'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
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
string|'"volume"'
op|','
string|'"volumes"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'volumes'
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
string|'"type"'
op|','
string|'"types"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'types'
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
string|'"snapshot"'
op|','
string|'"snapshots"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'snapshots'
op|'.'
name|'create_resource'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
