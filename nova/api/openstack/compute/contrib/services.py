begin_unit
comment|'# Copyright 2012 IBM Corp.'
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
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'servicegroup'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|class|ServiceController
name|'class'
name|'ServiceController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host_api'
op|'='
name|'compute'
op|'.'
name|'HostAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'ext_mgr'
newline|'\n'
nl|'\n'
DECL|member|_get_services
dedent|''
name|'def'
name|'_get_services'
op|'('
name|'self'
op|','
name|'req'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'services'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_all'
op|'('
nl|'\n'
name|'context'
op|','
name|'set_zones'
op|'='
name|'True'
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
name|'binary'
op|'='
string|"''"
newline|'\n'
name|'if'
string|"'binary'"
name|'in'
name|'req'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'            '
name|'binary'
op|'='
name|'req'
op|'.'
name|'GET'
op|'['
string|"'binary'"
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
name|'binary'
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
name|'binary'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'services'
newline|'\n'
nl|'\n'
DECL|member|_get_service_detail
dedent|''
name|'def'
name|'_get_service_detail'
op|'('
name|'self'
op|','
name|'svc'
op|','
name|'detailed'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'alive'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'svc'
op|')'
newline|'\n'
name|'state'
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
indent|'            '
name|'active'
op|'='
string|"'disabled'"
newline|'\n'
dedent|''
name|'service_detail'
op|'='
op|'{'
string|"'binary'"
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
name|'state'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'svc'
op|'['
string|"'updated_at'"
op|']'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-extended-services-delete'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'service_detail'
op|'['
string|"'id'"
op|']'
op|'='
name|'svc'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'            '
name|'service_detail'
op|'['
string|"'disabled_reason'"
op|']'
op|'='
name|'svc'
op|'['
string|"'disabled_reason'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'service_detail'
newline|'\n'
nl|'\n'
DECL|member|_get_services_list
dedent|''
name|'def'
name|'_get_services_list'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'detailed'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'services'
op|'='
name|'self'
op|'.'
name|'_get_services'
op|'('
name|'req'
op|')'
newline|'\n'
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
name|'svcs'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_get_service_detail'
op|'('
name|'svc'
op|','
name|'detailed'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'svcs'
newline|'\n'
nl|'\n'
DECL|member|_is_valid_as_reason
dedent|''
name|'def'
name|'_is_valid_as_reason'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'reason'
op|'.'
name|'strip'
op|'('
op|')'
op|','
string|"'Disabled reason'"
op|','
nl|'\n'
name|'min_length'
op|'='
number|'1'
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the specified service."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-extended-services-delete'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPMethodNotAllowed'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_delete'
op|'('
name|'context'
op|','
name|'id'
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
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Service %s not found."'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
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
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
string|'"""Return a list of all running services."""'
newline|'\n'
name|'detailed'
op|'='
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-extended-services'"
op|')'
newline|'\n'
name|'services'
op|'='
name|'self'
op|'.'
name|'_get_services_list'
op|'('
name|'req'
op|','
name|'detailed'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'services'"
op|':'
name|'services'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
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
string|'"""Enable/Disable scheduling for a service."""'
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
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
name|'ext_loaded'
op|'='
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-extended-services'"
op|')'
newline|'\n'
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
name|'status'
op|'='
string|'"enabled"'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'id'
op|'=='
string|'"disable"'
name|'or'
nl|'\n'
op|'('
name|'id'
op|'=='
string|'"disable-log-reason"'
name|'and'
name|'ext_loaded'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'disabled'
op|'='
name|'True'
newline|'\n'
name|'status'
op|'='
string|'"disabled"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unknown action"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'binary'
op|'='
name|'body'
op|'['
string|"'binary'"
op|']'
newline|'\n'
name|'ret_value'
op|'='
op|'{'
nl|'\n'
string|"'service'"
op|':'
op|'{'
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'status'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'status_detail'
op|'='
op|'{'
nl|'\n'
string|"'disabled'"
op|':'
name|'disabled'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'id'
op|'=='
string|'"disable-log-reason"'
op|':'
newline|'\n'
indent|'                '
name|'reason'
op|'='
name|'body'
op|'['
string|"'disabled_reason'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_is_valid_as_reason'
op|'('
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|"'The string containing the reason for disabling '"
nl|'\n'
string|"'the service contains invalid characters or is '"
nl|'\n'
string|"'too long.'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'status_detail'
op|'['
string|"'disabled_reason'"
op|']'
op|'='
name|'reason'
newline|'\n'
name|'ret_value'
op|'['
string|"'service'"
op|']'
op|'['
string|"'disabled_reason'"
op|']'
op|'='
name|'reason'
newline|'\n'
dedent|''
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
name|'msg'
op|'='
name|'_'
op|'('
string|"'Invalid attribute in the request'"
op|')'
newline|'\n'
name|'if'
string|"'host'"
name|'in'
name|'body'
name|'and'
string|"'binary'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Missing disabled reason field'"
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_update'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|','
name|'status_detail'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'HostBinaryNotFound'
name|'as'
name|'e'
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
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'ret_value'
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
string|'"""Services support."""'
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
string|'"2012-10-28T00:00:00Z"'
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
name|'self'
op|'.'
name|'ext_mgr'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
