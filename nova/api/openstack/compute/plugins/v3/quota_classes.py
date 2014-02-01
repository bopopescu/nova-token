begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'import'
name|'nova'
op|'.'
name|'context'
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
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
DECL|variable|FILTERED_QUOTAS
name|'FILTERED_QUOTAS'
op|'='
op|'['
string|"'injected_files'"
op|','
string|"'injected_file_content_bytes'"
op|','
nl|'\n'
string|"'injected_file_path_bytes'"
op|']'
newline|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-quota-class-sets"'
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
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaClassSetsController
name|'class'
name|'QuotaClassSetsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_format_quota_set
indent|'    '
name|'def'
name|'_format_quota_set'
op|'('
name|'self'
op|','
name|'quota_class'
op|','
name|'quota_set'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert the quota object to a result dict."""'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'str'
op|'('
name|'quota_class'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'resource'
name|'in'
name|'QUOTAS'
op|'.'
name|'resources'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'resource'
name|'not'
name|'in'
name|'FILTERED_QUOTAS'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'['
name|'resource'
op|']'
op|'='
name|'quota_set'
op|'['
name|'resource'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'dict'
op|'('
name|'quota_class_set'
op|'='
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'403'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'nova'
op|'.'
name|'context'
op|'.'
name|'authorize_quota_class_context'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
nl|'\n'
name|'QUOTAS'
op|'.'
name|'get_class_quotas'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|')'
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
name|'quota_class'
op|'='
name|'id'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'quota_class_set'"
op|')'
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
string|'"The request body invalid"'
op|')'
newline|'\n'
dedent|''
name|'quota_class_set'
op|'='
name|'body'
op|'['
string|"'quota_class_set'"
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'quota_class_set'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'QUOTAS'
name|'and'
name|'key'
name|'not'
name|'in'
name|'FILTERED_QUOTAS'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'value'
op|'='
name|'utils'
op|'.'
name|'validate_integer'
op|'('
nl|'\n'
name|'body'
op|'['
string|"'quota_class_set'"
op|']'
op|'['
name|'key'
op|']'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'db'
op|'.'
name|'quota_class_update'
op|'('
name|'context'
op|','
name|'quota_class'
op|','
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'QuotaClassNotFound'
op|':'
newline|'\n'
indent|'                    '
name|'db'
op|'.'
name|'quota_class_create'
op|'('
name|'context'
op|','
name|'quota_class'
op|','
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AdminRequired'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
nl|'\n'
name|'quota_class'
op|','
nl|'\n'
name|'QUOTAS'
op|'.'
name|'get_class_quotas'
op|'('
name|'context'
op|','
name|'quota_class'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaClasses
dedent|''
dedent|''
name|'class'
name|'QuotaClasses'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Quota classes management support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"QuotaClasses"'
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
name|'QuotaClassSetsController'
op|'('
op|')'
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
dedent|''
dedent|''
endmarker|''
end_unit
