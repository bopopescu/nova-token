begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack, LLC'
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
name|'import'
name|'flags'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
name|'use_forwarded_for_opt'
op|'='
DECL|variable|use_forwarded_for_opt
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
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'add_option'
op|'('
name|'use_forwarded_for_opt'
op|')'
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
string|'"""Make a request context from keystone headers"""'
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
name|'user_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X_USER'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"X_USER not found in request"'
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
comment|'# get the roles'
nl|'\n'
dedent|''
name|'roles'
op|'='
op|'['
name|'r'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'r'
name|'in'
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
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|']'
newline|'\n'
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
nl|'\n'
comment|'# Get the auth token'
nl|'\n'
dedent|''
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
name|'getattr'
op|'('
name|'req'
op|','
string|"'remote_address'"
op|','
string|"'127.0.0.1'"
op|')'
newline|'\n'
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
newline|'\n'
name|'if'
name|'FLAGS'
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
dedent|''
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
name|'strategy'
op|'='
string|"'keystone'"
op|','
nl|'\n'
name|'remote_address'
op|'='
name|'remote_address'
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
dedent|''
dedent|''
endmarker|''
end_unit
