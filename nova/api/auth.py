begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
string|'"""\nCommon Auth Middleware.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'middleware'
name|'import'
name|'request_id'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
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
name|'import'
name|'context'
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
op|'.'
name|'i18n'
name|'import'
name|'_LW'
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
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|auth_opts
name|'auth_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'api_rate_limit'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
op|'('
string|"'Whether to use per-user rate limiting for the api. '"
nl|'\n'
string|"'This option is only used by v2 api. Rate limiting '"
nl|'\n'
string|"'is removed from v3 api.'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'auth_strategy'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'keystone'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The strategy to use for auth: noauth or keystone.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_forwarded_for'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Treat X-Forwarded-For as the canonical remote address. '"
nl|'\n'
string|"'Only enable this if you have a sanitizing proxy.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'auth_opts'
op|')'
newline|'\n'
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
DECL|function|_load_pipeline
name|'def'
name|'_load_pipeline'
op|'('
name|'loader'
op|','
name|'pipeline'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'filters'
op|'='
op|'['
name|'loader'
op|'.'
name|'get_filter'
op|'('
name|'n'
op|')'
name|'for'
name|'n'
name|'in'
name|'pipeline'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|']'
newline|'\n'
name|'app'
op|'='
name|'loader'
op|'.'
name|'get_app'
op|'('
name|'pipeline'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'filters'
op|'.'
name|'reverse'
op|'('
op|')'
newline|'\n'
name|'for'
name|'filter'
name|'in'
name|'filters'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'filter'
op|'('
name|'app'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'app'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pipeline_factory
dedent|''
name|'def'
name|'pipeline_factory'
op|'('
name|'loader'
op|','
name|'global_conf'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A paste pipeline replica that keys off of auth_strategy."""'
newline|'\n'
name|'pipeline'
op|'='
name|'local_conf'
op|'['
name|'CONF'
op|'.'
name|'auth_strategy'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'api_rate_limit'
op|':'
newline|'\n'
indent|'        '
name|'limit_name'
op|'='
name|'CONF'
op|'.'
name|'auth_strategy'
op|'+'
string|"'_nolimit'"
newline|'\n'
name|'pipeline'
op|'='
name|'local_conf'
op|'.'
name|'get'
op|'('
name|'limit_name'
op|','
name|'pipeline'
op|')'
newline|'\n'
dedent|''
name|'pipeline'
op|'='
name|'pipeline'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
comment|'# NOTE (Alex Xu): This is just for configuration file compatibility.'
nl|'\n'
comment|"# If the configuration file still contains 'ratelimit_v3', just ignore it."
nl|'\n'
comment|'# We will remove this code at next release (J)'
nl|'\n'
name|'if'
string|"'ratelimit_v3'"
name|'in'
name|'pipeline'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|"'ratelimit_v3 is removed from v3 api.'"
op|')'
op|')'
newline|'\n'
name|'pipeline'
op|'.'
name|'remove'
op|'('
string|"'ratelimit_v3'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_load_pipeline'
op|'('
name|'loader'
op|','
name|'pipeline'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pipeline_factory_v21
dedent|''
name|'def'
name|'pipeline_factory_v21'
op|'('
name|'loader'
op|','
name|'global_conf'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A paste pipeline replica that keys off of auth_strategy."""'
newline|'\n'
name|'return'
name|'_load_pipeline'
op|'('
name|'loader'
op|','
name|'local_conf'
op|'['
name|'CONF'
op|'.'
name|'auth_strategy'
op|']'
op|'.'
name|'split'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(oomichi): This pipeline_factory_v3 is for passing check-grenade-dsvm.'
nl|'\n'
DECL|variable|pipeline_factory_v3
dedent|''
name|'pipeline_factory_v3'
op|'='
name|'pipeline_factory_v21'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InjectContext
name|'class'
name|'InjectContext'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add a \'nova.context\' to WSGI environ."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
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
name|'context'
op|'='
name|'context'
newline|'\n'
name|'super'
op|'('
name|'InjectContext'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaKeystoneContext
dedent|''
dedent|''
name|'class'
name|'NovaKeystoneContext'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make a request context from keystone headers."""'
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
name|'user_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_USER'"
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_USER_ID'"
op|','
name|'user_id'
op|')'
newline|'\n'
name|'if'
name|'user_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Neither X_USER_ID nor X_USER found in request"'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'roles'
op|'='
name|'self'
op|'.'
name|'_get_roles'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'X_TENANT_ID'"
name|'in'
name|'req'
op|'.'
name|'headers'
op|':'
newline|'\n'
comment|'# This is the new header since Keystone went to ID/Name'
nl|'\n'
indent|'            '
name|'project_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X_TENANT_ID'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# This is for legacy compatibility'
nl|'\n'
indent|'            '
name|'project_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X_TENANT'"
op|']'
newline|'\n'
dedent|''
name|'project_name'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_TENANT_NAME'"
op|')'
newline|'\n'
name|'user_name'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_USER_NAME'"
op|')'
newline|'\n'
nl|'\n'
name|'req_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
name|'request_id'
op|'.'
name|'ENV_REQUEST_ID'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the auth token'
nl|'\n'
name|'auth_token'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_AUTH_TOKEN'"
op|','
nl|'\n'
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_STORAGE_TOKEN'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Build a context, including the auth_token...'
nl|'\n'
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_forwarded_for'
op|':'
newline|'\n'
indent|'            '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|','
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'service_catalog'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_SERVICE_CATALOG'"
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'catalog_header'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_SERVICE_CATALOG'"
op|')'
newline|'\n'
name|'service_catalog'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'catalog_header'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Invalid service catalog json.'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(jamielennox): This is a full auth plugin set by auth_token'
nl|'\n'
comment|'# middleware in newer versions.'
nl|'\n'
dedent|''
dedent|''
name|'user_auth_plugin'
op|'='
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'keystone.token_auth'"
op|')'
newline|'\n'
nl|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'user_name'
op|'='
name|'user_name'
op|','
nl|'\n'
name|'project_name'
op|'='
name|'project_name'
op|','
nl|'\n'
name|'roles'
op|'='
name|'roles'
op|','
nl|'\n'
name|'auth_token'
op|'='
name|'auth_token'
op|','
nl|'\n'
name|'remote_address'
op|'='
name|'remote_address'
op|','
nl|'\n'
name|'service_catalog'
op|'='
name|'service_catalog'
op|','
nl|'\n'
name|'request_id'
op|'='
name|'req_id'
op|','
nl|'\n'
name|'user_auth_plugin'
op|'='
name|'user_auth_plugin'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'ctx'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
DECL|member|_get_roles
dedent|''
name|'def'
name|'_get_roles'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the list of roles."""'
newline|'\n'
nl|'\n'
name|'if'
string|"'X_ROLES'"
name|'in'
name|'req'
op|'.'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'roles'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_ROLES'"
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Fallback to deprecated role header:'
nl|'\n'
indent|'            '
name|'roles'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X_ROLE'"
op|','
string|"''"
op|')'
newline|'\n'
name|'if'
name|'roles'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"Sourcing roles from deprecated X-Role HTTP "'
nl|'\n'
string|'"header"'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'['
name|'r'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'r'
name|'in'
name|'roles'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
