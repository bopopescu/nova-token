begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
string|'"""\nRequest Body limiting middleware.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#default request size is 112k'
nl|'\n'
DECL|variable|max_request_body_size_opt
name|'max_request_body_size_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'osapi_max_request_body_size'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'114688'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The maximum body size '"
nl|'\n'
string|"'per each osapi request(bytes)'"
op|')'
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
name|'register_opt'
op|'('
name|'max_request_body_size_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitingReader
name|'class'
name|'LimitingReader'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Reader to limit the size of an incoming request."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'limit'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        :param data: Underlying data object\n        :param limit: maximum number of bytes the reader should allow\n        """'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
name|'data'
newline|'\n'
name|'self'
op|'.'
name|'limit'
op|'='
name|'limit'
newline|'\n'
name|'self'
op|'.'
name|'bytes_read'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'chunk'
name|'in'
name|'self'
op|'.'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'bytes_read'
op|'+='
name|'len'
op|'('
name|'chunk'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'bytes_read'
op|'>'
name|'self'
op|'.'
name|'limit'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Request is too large."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'chunk'
newline|'\n'
nl|'\n'
DECL|member|read
dedent|''
dedent|''
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'i'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'data'
op|'.'
name|'read'
op|'('
name|'i'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'bytes_read'
op|'+='
name|'len'
op|'('
name|'result'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'bytes_read'
op|'>'
name|'self'
op|'.'
name|'limit'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Request is too large."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestBodySizeLimiter
dedent|''
dedent|''
name|'class'
name|'RequestBodySizeLimiter'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Limit the size of incoming requests."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'super'
op|'('
name|'RequestBodySizeLimiter'
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
name|'if'
name|'req'
op|'.'
name|'content_length'
op|'>'
name|'CONF'
op|'.'
name|'osapi_max_request_body_size'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Request is too large."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'req'
op|'.'
name|'content_length'
name|'is'
name|'None'
name|'and'
name|'req'
op|'.'
name|'is_body_readable'
op|':'
newline|'\n'
indent|'            '
name|'limiter'
op|'='
name|'LimitingReader'
op|'('
name|'req'
op|'.'
name|'body_file'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'osapi_max_request_body_size'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'body_file'
op|'='
name|'limiter'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
