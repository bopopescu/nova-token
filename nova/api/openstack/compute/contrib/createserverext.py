begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
comment|'#    under the License'
nl|'\n'
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
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'views'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'createserverext'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'views'
op|'.'
name|'servers'
op|'.'
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds security group output when viewing server details."""'
newline|'\n'
nl|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detailed view of a single instance."""'
newline|'\n'
name|'server'
op|'='
name|'super'
op|'('
name|'ViewBuilder'
op|','
name|'self'
op|')'
op|'.'
name|'show'
op|'('
name|'request'
op|','
name|'instance'
op|')'
newline|'\n'
name|'context'
op|'='
name|'request'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'['
string|'"server"'
op|']'
op|'['
string|'"security_groups"'
op|']'
op|'='
name|'self'
op|'.'
name|'_get_groups'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|_get_groups
dedent|''
name|'def'
name|'_get_groups'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list of security groups for this instance."""'
newline|'\n'
name|'groups'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'security_groups'"
op|')'
newline|'\n'
name|'if'
name|'groups'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|'{'
string|'"name"'
op|':'
name|'group'
op|'['
string|'"name"'
op|']'
op|'}'
name|'for'
name|'group'
name|'in'
name|'groups'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
dedent|''
dedent|''
name|'class'
name|'Controller'
op|'('
name|'servers'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|variable|_view_builder_class
indent|'    '
name|'_view_builder_class'
op|'='
name|'ViewBuilder'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Createserverext
dedent|''
name|'class'
name|'Createserverext'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extended support to the Create Server v1.1 API"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Createserverext"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-create-server-ext"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"createserverext/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-07-19T00:00:00+00:00"'
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
op|']'
newline|'\n'
name|'controller'
op|'='
name|'Controller'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-create-server-ext'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
