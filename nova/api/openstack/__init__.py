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
name|'json'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'traceback'
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
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'ratelimiting'
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
name|'sharedipgroups'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'os_api_auth'"
op|','
nl|'\n'
string|"'nova.api.openstack.auth.AuthMiddleware'"
op|','
nl|'\n'
string|"'The auth mechanism to use for the OpenStack API implemenation'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'os_api_ratelimiting'"
op|','
nl|'\n'
string|"'nova.api.openstack.ratelimiting.RateLimitingMiddleware'"
op|','
nl|'\n'
string|"'Default ratelimiting implementation for the Openstack API'"
op|')'
newline|'\n'
nl|'\n'
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
DECL|class|API
name|'class'
name|'API'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI entry point for all OpenStack API requests."""'
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
name|'auth_middleware'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'FLAGS'
op|'.'
name|'os_api_auth'
op|')'
newline|'\n'
name|'ratelimiting_middleware'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'FLAGS'
op|'.'
name|'os_api_ratelimiting'
op|')'
newline|'\n'
name|'app'
op|'='
name|'auth_middleware'
op|'('
name|'ratelimiting_middleware'
op|'('
name|'APIRouter'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'API'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'app'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
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
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Caught error: %s"'
op|')'
op|'%'
name|'str'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'traceback'
op|'.'
name|'format_exc'
op|'('
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
name|'str'
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
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'server_members'
op|'='
op|'{'
string|"'action'"
op|':'
string|"'POST'"
op|'}'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Including admin operations in API."'
op|')'
newline|'\n'
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
nl|'\n'
dedent|''
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"server"'
op|','
string|'"servers"'
op|','
name|'controller'
op|'='
name|'servers'
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
op|','
nl|'\n'
name|'member'
op|'='
name|'server_members'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"backup_schedule"'
op|','
string|'"backup_schedules"'
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
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"sharedipgroup"'
op|','
string|'"sharedipgroups"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'sharedipgroups'
op|'.'
name|'Controller'
op|'('
op|')'
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
dedent|''
dedent|''
endmarker|''
end_unit
