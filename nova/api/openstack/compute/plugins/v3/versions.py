begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
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
name|'compute'
op|'.'
name|'views'
name|'import'
name|'versions'
name|'as'
name|'views_versions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"versions"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsController
name|'class'
name|'VersionsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
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
name|'id'
op|'='
string|"'v3.0'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'builder'
op|'='
name|'views_versions'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'versions'
op|'.'
name|'VERSIONS'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'builder'
op|'.'
name|'build_version'
op|'('
name|'versions'
op|'.'
name|'VERSIONS'
op|'['
name|'id'
op|']'
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
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API Version information."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Versions"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
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
name|'resources'
op|'='
op|'['
nl|'\n'
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
name|'VersionsController'
op|'('
op|')'
op|','
nl|'\n'
name|'custom_routes_fn'
op|'='
name|'self'
op|'.'
name|'version_map'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|version_map
dedent|''
name|'def'
name|'version_map'
op|'('
name|'self'
op|','
name|'mapper'
op|','
name|'wsgi_resource'
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
name|'wsgi_resource'
op|','
nl|'\n'
name|'action'
op|'='
string|"'show'"
op|','
name|'conditions'
op|'='
op|'{'
string|'"method"'
op|':'
op|'['
string|"'GET'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'redirect'
op|'('
string|'""'
op|','
string|'"/"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
