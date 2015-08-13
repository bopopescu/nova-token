begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'import'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
op|'.'
name|'parse'
name|'as'
name|'urlparse'
newline|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'schemas'
name|'import'
name|'quota_sets'
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
name|'import'
name|'validation'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-quota-sets"'
newline|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaSetsController
name|'class'
name|'QuotaSetsController'
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
name|'project_id'
op|','
name|'quota_set'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert the quota object to a result dict."""'
newline|'\n'
name|'if'
name|'project_id'
op|':'
newline|'\n'
indent|'            '
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
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
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
name|'in'
name|'quota_set'
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
dedent|''
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
DECL|member|_validate_quota_limit
dedent|''
name|'def'
name|'_validate_quota_limit'
op|'('
name|'self'
op|','
name|'resource'
op|','
name|'limit'
op|','
name|'minimum'
op|','
name|'maximum'
op|')'
op|':'
newline|'\n'
comment|'# NOTE: -1 is a flag value for unlimited'
nl|'\n'
indent|'        '
name|'if'
name|'limit'
op|'<'
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Quota limit %(limit)s for %(resource)s "'
nl|'\n'
string|'"must be -1 or greater."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'resource'"
op|':'
name|'resource'
op|'}'
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
DECL|function|conv_inf
dedent|''
name|'def'
name|'conv_inf'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'float'
op|'('
string|'"inf"'
op|')'
name|'if'
name|'value'
op|'=='
op|'-'
number|'1'
name|'else'
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'conv_inf'
op|'('
name|'limit'
op|')'
op|'<'
name|'conv_inf'
op|'('
name|'minimum'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Quota limit %(limit)s for %(resource)s must "'
nl|'\n'
string|'"be greater than or equal to already used and "'
nl|'\n'
string|'"reserved %(minimum)s."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'minimum'"
op|':'
name|'minimum'
op|'}'
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
dedent|''
name|'if'
name|'conv_inf'
op|'('
name|'limit'
op|')'
op|'>'
name|'conv_inf'
op|'('
name|'maximum'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Quota limit %(limit)s for %(resource)s must be "'
nl|'\n'
string|'"less than or equal to %(maximum)s."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'maximum'"
op|':'
name|'maximum'
op|'}'
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
DECL|member|_get_quotas
dedent|''
dedent|''
name|'def'
name|'_get_quotas'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|','
name|'user_id'
op|'='
name|'None'
op|','
name|'usages'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'user_id'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_user_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'user_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'usages'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_project_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'usages'
op|'='
name|'usages'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'usages'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'values'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
name|'k'
op|':'
name|'v'
op|'['
string|"'limit'"
op|']'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'values'
op|'.'
name|'items'
op|'('
op|')'
op|'}'
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
op|')'
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
op|','
name|'action'
op|'='
string|"'show'"
op|','
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'QUERY_STRING'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'user_id'
op|'='
name|'user_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
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
op|','
name|'action'
op|'='
string|"'detail'"
op|','
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'400'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'quota_sets'
op|'.'
name|'update'
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
op|','
name|'action'
op|'='
string|"'update'"
op|','
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'id'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'QUERY_STRING'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'quota_set'
op|'='
name|'body'
op|'['
string|"'quota_set'"
op|']'
newline|'\n'
name|'force_update'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'quota_set'
op|'.'
name|'get'
op|'('
string|"'force'"
op|','
nl|'\n'
string|"'False'"
op|')'
op|')'
newline|'\n'
name|'settable_quotas'
op|'='
name|'QUOTAS'
op|'.'
name|'get_settable_quotas'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(dims): Pass #1 - In this loop for quota_set.items(), we validate'
nl|'\n'
comment|'# min/max values and bail out if any of the items in the set is bad.'
nl|'\n'
name|'valid_quotas'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'body'
op|'['
string|"'quota_set'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'=='
string|"'force'"
name|'or'
op|'('
name|'not'
name|'value'
name|'and'
name|'value'
op|'!='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
comment|'# validate whether already used and reserved exceeds the new'
nl|'\n'
comment|'# quota, this check will be ignored if admin want to force'
nl|'\n'
comment|'# update'
nl|'\n'
dedent|''
name|'value'
op|'='
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'force_update'
op|':'
newline|'\n'
indent|'                '
name|'minimum'
op|'='
name|'settable_quotas'
op|'['
name|'key'
op|']'
op|'['
string|"'minimum'"
op|']'
newline|'\n'
name|'maximum'
op|'='
name|'settable_quotas'
op|'['
name|'key'
op|']'
op|'['
string|"'maximum'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_validate_quota_limit'
op|'('
name|'key'
op|','
name|'value'
op|','
name|'minimum'
op|','
name|'maximum'
op|')'
newline|'\n'
dedent|''
name|'valid_quotas'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
comment|'# NOTE(dims): Pass #2 - At this point we know that all the'
nl|'\n'
comment|'# values are correct and we can iterate and update them all in one'
nl|'\n'
comment|'# shot without having to worry about rolling back etc as we have done'
nl|'\n'
comment|'# the validation up front in the loop above.'
nl|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'valid_quotas'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'objects'
op|'.'
name|'Quotas'
op|'.'
name|'create_limit'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'key'
op|','
name|'value'
op|','
name|'user_id'
op|'='
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'QuotaExists'
op|':'
newline|'\n'
indent|'                '
name|'objects'
op|'.'
name|'Quotas'
op|'.'
name|'update_limit'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'key'
op|','
name|'value'
op|','
name|'user_id'
op|'='
name|'user_id'
op|')'
newline|'\n'
comment|"# Note(gmann): Removed 'id' from update's response to make it same"
nl|'\n'
comment|'# as V2. If needed it can be added with microversion.'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|defaults
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
op|','
name|'action'
op|'='
string|"'defaults'"
op|','
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_defaults'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(oomichi): Here should be 204(No Content) instead of 202 by v2.1'
nl|'\n'
comment|'# +microversions because the resource quota-set has been deleted completely'
nl|'\n'
comment|'# when returning a response.'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
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
op|','
name|'action'
op|'='
string|"'delete'"
op|','
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'QUERY_STRING'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'user_id'
op|':'
newline|'\n'
indent|'            '
name|'QUOTAS'
op|'.'
name|'destroy_all_by_project_and_user'
op|'('
name|'context'
op|','
nl|'\n'
name|'id'
op|','
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'QUOTAS'
op|'.'
name|'destroy_all_by_project'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaSets
dedent|''
dedent|''
dedent|''
name|'class'
name|'QuotaSets'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Quotas management support."""'
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
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'QuotaSetsController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|"'defaults'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'detail'"
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
