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
name|'import'
name|'wsgi'
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
name|'__name__'
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
comment|'# NOTE(johannes): We leave the explanation empty here on'
nl|'\n'
comment|'# purpose. It could possibly have sensitive information'
nl|'\n'
comment|'# that should not be returned back to the user. See'
nl|'\n'
comment|'# bugs 868360 and 874472'
nl|'\n'
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
DECL|variable|ExtensionManager
name|'ExtensionManager'
op|'='
name|'None'
comment|'# override in subclasses'
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
name|'if'
name|'self'
op|'.'
name|'ExtensionManager'
op|':'
newline|'\n'
indent|'                '
name|'ext_mgr'
op|'='
name|'self'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Must specify an ExtensionManager class"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'mapper'
op|'='
name|'ProjectMapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resources'
op|'='
op|'{'
op|'}'
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
name|'self'
op|'.'
name|'_setup_extensions'
op|'('
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
nl|'\n'
name|'wsgi_resource'
op|'='
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'resource'
op|'.'
name|'controller'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resources'
op|'['
name|'resource'
op|'.'
name|'collection'
op|']'
op|'='
name|'wsgi_resource'
newline|'\n'
name|'kargs'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'controller'
op|'='
name|'wsgi_resource'
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
name|'if'
name|'resource'
op|'.'
name|'custom_routes_fn'
op|':'
newline|'\n'
indent|'                '
name|'resource'
op|'.'
name|'custom_routes_fn'
op|'('
name|'mapper'
op|','
name|'wsgi_resource'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_extensions
dedent|''
dedent|''
dedent|''
name|'def'
name|'_setup_extensions'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'extension'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_controller_extensions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ext_name'
op|'='
name|'extension'
op|'.'
name|'extension'
op|'.'
name|'name'
newline|'\n'
name|'collection'
op|'='
name|'extension'
op|'.'
name|'collection'
newline|'\n'
name|'controller'
op|'='
name|'extension'
op|'.'
name|'controller'
newline|'\n'
nl|'\n'
name|'if'
name|'collection'
name|'not'
name|'in'
name|'self'
op|'.'
name|'resources'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Extension %(ext_name)s: Cannot extend '"
nl|'\n'
string|"'resource %(collection)s: No such resource'"
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extension %(ext_name)s extending resource: '"
nl|'\n'
string|"'%(collection)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'resource'
op|'='
name|'self'
op|'.'
name|'resources'
op|'['
name|'collection'
op|']'
newline|'\n'
name|'resource'
op|'.'
name|'register_actions'
op|'('
name|'controller'
op|')'
newline|'\n'
name|'resource'
op|'.'
name|'register_extensions'
op|'('
name|'controller'
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
name|'raise'
name|'NotImplementedError'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
