begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM'
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
name|'import'
name|'extensions'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'services'"
op|')'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServicesIndexTemplate
name|'class'
name|'ServicesIndexTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'services'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'service'"
op|','
name|'selector'
op|'='
string|"'services'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'binary'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'zone'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'status'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'state'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'update_at'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServicesUpdateTemplate
dedent|''
dedent|''
name|'class'
name|'ServicesUpdateTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'service'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'disabled'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceController
dedent|''
dedent|''
name|'class'
name|'ServiceController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ServicesIndexTemplate'
op|')'
newline|'\n'
DECL|member|index
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
string|'"""\n        Return a list of all running services. Filter by host & service name.\n        """'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'host'
op|'='
string|"''"
newline|'\n'
name|'if'
string|"'host'"
name|'in'
name|'req'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'req'
op|'.'
name|'GET'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
name|'service'
op|'='
string|"''"
newline|'\n'
name|'if'
string|"'service'"
name|'in'
name|'req'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'req'
op|'.'
name|'GET'
op|'['
string|"'service'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'services'
name|'if'
name|'s'
op|'['
string|"'host'"
op|']'
op|'=='
name|'host'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'service'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'services'
name|'if'
name|'s'
op|'['
string|"'binary'"
op|']'
op|'=='
name|'service'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'svcs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'svc'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'delta'
op|'='
name|'now'
op|'-'
op|'('
name|'svc'
op|'['
string|"'updated_at'"
op|']'
name|'or'
name|'svc'
op|'['
string|"'created_at'"
op|']'
op|')'
newline|'\n'
name|'alive'
op|'='
name|'abs'
op|'('
name|'utils'
op|'.'
name|'total_seconds'
op|'('
name|'delta'
op|')'
op|')'
op|'<='
name|'CONF'
op|'.'
name|'service_down_time'
newline|'\n'
name|'art'
op|'='
op|'('
name|'alive'
name|'and'
string|'"up"'
op|')'
name|'or'
string|'"down"'
newline|'\n'
name|'active'
op|'='
string|"'enabled'"
newline|'\n'
name|'if'
name|'svc'
op|'['
string|"'disabled'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'active'
op|'='
string|"'disabled'"
newline|'\n'
dedent|''
name|'svcs'
op|'.'
name|'append'
op|'('
op|'{'
string|'"binary"'
op|':'
name|'svc'
op|'['
string|"'binary'"
op|']'
op|','
string|"'host'"
op|':'
name|'svc'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'zone'"
op|':'
name|'svc'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'active'
op|','
string|"'state'"
op|':'
name|'art'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'svc'
op|'['
string|"'updated_at'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'services'"
op|':'
name|'svcs'
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
name|'ServicesUpdateTemplate'
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
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Enable/Disable scheduling for a service"""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'id'
op|'=='
string|'"enable"'
op|':'
newline|'\n'
indent|'            '
name|'disabled'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'elif'
name|'id'
op|'=='
string|'"disable"'
op|':'
newline|'\n'
indent|'            '
name|'disabled'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
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
string|'"Unknown action"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'body'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'service'
op|'='
name|'body'
op|'['
string|"'service'"
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
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'svc'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'service'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'svc'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
string|"'Unknown service'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'db'
op|'.'
name|'service_update'
op|'('
name|'context'
op|','
name|'svc'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'disabled'"
op|':'
name|'disabled'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ServiceNotFound'
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
string|'"service not found"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'service'"
op|':'
name|'service'
op|','
string|"'disabled'"
op|':'
name|'disabled'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Services
dedent|''
dedent|''
name|'class'
name|'Services'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Services support"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Services"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-services"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/services/api/v2"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-10-28T00:00:00-00:00"'
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
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-services'"
op|','
nl|'\n'
name|'ServiceController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'resource'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
