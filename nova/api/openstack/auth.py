begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
comment|'#    under the License.import datetime'
nl|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'auth'
newline|'\n'
name|'from'
name|'nova'
name|'import'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
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
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AuthMiddleware
name|'class'
name|'AuthMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Authorize the openstack API request or return an HTTP Forbidden."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'db_driver'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'db_driver'
op|':'
newline|'\n'
indent|'            '
name|'db_driver'
op|'='
name|'FLAGS'
op|'.'
name|'db_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'db_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth'
op|'='
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'AuthMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
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
name|'if'
name|'not'
name|'self'
op|'.'
name|'has_authentication'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'authenticate'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'user'
op|'='
name|'self'
op|'.'
name|'get_user_by_authentication'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'project'
op|'='
name|'self'
op|'.'
name|'auth'
op|'.'
name|'get_project'
op|'('
name|'FLAGS'
op|'.'
name|'default_project'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user'
op|','
name|'project'
op|','
nl|'\n'
name|'version'
op|'='
name|'req'
op|'.'
name|'script_name'
op|'.'
name|'replace'
op|'('
string|"'/v'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
DECL|member|has_authentication
dedent|''
name|'def'
name|'has_authentication'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'X-Auth-Token'"
name|'in'
name|'req'
op|'.'
name|'headers'
newline|'\n'
nl|'\n'
DECL|member|get_user_by_authentication
dedent|''
name|'def'
name|'get_user_by_authentication'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'authorize_token'
op|'('
name|'req'
op|'.'
name|'headers'
op|'['
string|'"X-Auth-Token"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|authenticate
dedent|''
name|'def'
name|'authenticate'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
comment|"# Unless the request is explicitly made against /<version>/ don't"
nl|'\n'
comment|'# honor it'
nl|'\n'
indent|'        '
name|'path_info'
op|'='
name|'req'
op|'.'
name|'path_info'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'path_info'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'username'
op|'='
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
newline|'\n'
name|'key'
op|'='
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'token'
op|','
name|'user'
op|'='
name|'self'
op|'.'
name|'_authorize_user'
op|'('
name|'username'
op|','
name|'key'
op|','
name|'req'
op|')'
newline|'\n'
name|'if'
name|'user'
name|'and'
name|'token'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
name|'token'
op|'.'
name|'token_hash'
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-Server-Management-Url'"
op|']'
op|'='
name|'token'
op|'.'
name|'server_management_url'
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-Storage-Url'"
op|']'
op|'='
name|'token'
op|'.'
name|'storage_url'
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-CDN-Management-Url'"
op|']'
op|'='
name|'token'
op|'.'
name|'cdn_management_url'
newline|'\n'
name|'res'
op|'.'
name|'content_type'
op|'='
string|"'text/plain'"
newline|'\n'
name|'res'
op|'.'
name|'status'
op|'='
string|"'204'"
newline|'\n'
name|'return'
name|'res'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|authorize_token
dedent|''
dedent|''
name|'def'
name|'authorize_token'
op|'('
name|'self'
op|','
name|'token_hash'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" retrieves user information from the datastore given a token\n\n        If the token has expired, returns None\n        If the token is not found, returns None\n        Otherwise returns dict(id=(the authorized user\'s id))\n\n        This method will also remove the token if the timestamp is older than\n        2 days ago.\n        """'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'token'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'auth_token_get'
op|'('
name|'ctxt'
op|','
name|'token_hash'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'token'
op|':'
newline|'\n'
indent|'            '
name|'delta'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
op|'('
op|')'
op|'-'
name|'token'
op|'.'
name|'created_at'
newline|'\n'
name|'if'
name|'delta'
op|'.'
name|'days'
op|'>='
number|'2'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'auth_token_destroy'
op|'('
name|'ctxt'
op|','
name|'token'
op|'.'
name|'token_hash'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'auth'
op|'.'
name|'get_user'
op|'('
name|'token'
op|'.'
name|'user_id'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_authorize_user
dedent|''
name|'def'
name|'_authorize_user'
op|'('
name|'self'
op|','
name|'username'
op|','
name|'key'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generates a new token and assigns it to a user.\n\n        username - string\n        key - string API key\n        req - wsgi.Request object\n        """'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'auth'
op|'.'
name|'get_user_from_access_key'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'user'
name|'and'
name|'user'
op|'.'
name|'name'
op|'=='
name|'username'
op|':'
newline|'\n'
indent|'            '
name|'token_hash'
op|'='
name|'hashlib'
op|'.'
name|'sha1'
op|'('
string|"'%s%s%f'"
op|'%'
op|'('
name|'username'
op|','
name|'key'
op|','
nl|'\n'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
name|'token_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'token_dict'
op|'['
string|"'token_hash'"
op|']'
op|'='
name|'token_hash'
newline|'\n'
name|'token_dict'
op|'['
string|"'cdn_management_url'"
op|']'
op|'='
string|"''"
newline|'\n'
comment|'# Same as auth url, e.g. http://foo.org:8774/baz/v1.0'
nl|'\n'
name|'token_dict'
op|'['
string|"'server_management_url'"
op|']'
op|'='
name|'req'
op|'.'
name|'url'
newline|'\n'
name|'token_dict'
op|'['
string|"'storage_url'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'token_dict'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'token'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'auth_token_create'
op|'('
name|'ctxt'
op|','
name|'token_dict'
op|')'
newline|'\n'
name|'return'
name|'token'
op|','
name|'user'
newline|'\n'
dedent|''
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
