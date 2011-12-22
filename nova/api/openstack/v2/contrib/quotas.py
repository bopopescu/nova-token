begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
nl|'\n'
nl|'\n'
DECL|variable|quota_resources
name|'quota_resources'
op|'='
op|'['
string|"'metadata_items'"
op|','
string|"'injected_file_content_bytes'"
op|','
nl|'\n'
string|"'volumes'"
op|','
string|"'gigabytes'"
op|','
string|"'ram'"
op|','
string|"'floating_ips'"
op|','
string|"'instances'"
op|','
nl|'\n'
string|"'injected_files'"
op|','
string|"'cores'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaSetsController
name|'class'
name|'QuotaSetsController'
op|'('
name|'object'
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
name|'project_id'
op|','
name|'quota_set'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert the quota object to a result dict"""'
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
name|'project_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'resource'
name|'in'
name|'quota_resources'
op|':'
newline|'\n'
indent|'            '
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
name|'return'
name|'dict'
op|'('
name|'quota_set'
op|'='
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'api'
op|'.'
name|'authorize_project_context'
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
name|'quota'
op|'.'
name|'get_project_quotas'
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
DECL|member|update
dedent|''
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'project_id'
op|'='
name|'id'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'body'
op|'['
string|"'quota_set'"
op|']'
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
name|'quota_resources'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'int'
op|'('
name|'body'
op|'['
string|"'quota_set'"
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'db'
op|'.'
name|'quota_update'
op|'('
name|'context'
op|','
name|'project_id'
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
name|'ProjectQuotaNotFound'
op|':'
newline|'\n'
indent|'                    '
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'context'
op|','
name|'project_id'
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
op|'{'
string|"'quota_set'"
op|':'
name|'quota'
op|'.'
name|'get_project_quotas'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|defaults
dedent|''
name|'def'
name|'defaults'
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
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
name|'quota'
op|'.'
name|'_get_default_quotas'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaTemplate
dedent|''
dedent|''
name|'class'
name|'QuotaTemplate'
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
string|"'quota_set'"
op|','
name|'selector'
op|'='
string|"'quota_set'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'resource'
name|'in'
name|'quota_resources'
op|':'
newline|'\n'
indent|'            '
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
name|'resource'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'text'
op|'='
name|'resource'
newline|'\n'
nl|'\n'
dedent|''
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
DECL|class|QuotaSerializer
dedent|''
dedent|''
name|'class'
name|'QuotaSerializer'
op|'('
name|'xmlutil'
op|'.'
name|'XMLTemplateSerializer'
op|')'
op|':'
newline|'\n'
DECL|member|default
indent|'    '
name|'def'
name|'default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'QuotaTemplate'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Quotas
dedent|''
dedent|''
name|'class'
name|'Quotas'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Quotas management support"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Quotas"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-quota-sets"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/quotas-sets/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-08-08T00:00:00+00:00"'
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
nl|'\n'
name|'body_serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'QuotaSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
name|'body_serializers'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-quota-sets'"
op|','
nl|'\n'
name|'QuotaSetsController'
op|'('
op|')'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|"'defaults'"
op|':'
string|"'GET'"
op|'}'
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
