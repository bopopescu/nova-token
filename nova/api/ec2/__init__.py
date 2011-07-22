begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nStarting point for routing EC2 requests.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
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
name|'log'
name|'as'
name|'logging'
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
name|'ec2'
name|'import'
name|'apirequest'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.api"'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
string|"'use_forwarded_for'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Treat X-Forwarded-For as the canonical remote address. '"
nl|'\n'
string|"'Only enable this if you have a sanitizing proxy.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'lockout_attempts'"
op|','
number|'5'
op|','
nl|'\n'
string|"'Number of failed auths before lockout.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'lockout_minutes'"
op|','
number|'15'
op|','
nl|'\n'
string|"'Number of minutes to lockout if triggered.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'lockout_window'"
op|','
number|'15'
op|','
nl|'\n'
string|"'Number of minutes for lockout window.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestLogging
name|'class'
name|'RequestLogging'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Access-Log akin logging for all EC2 API requests."""'
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
name|'start'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log_request_completion'
op|'('
name|'rv'
op|','
name|'req'
op|','
name|'start'
op|')'
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
DECL|member|log_request_completion
dedent|''
name|'def'
name|'log_request_completion'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'request'
op|','
name|'start'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'apireq'
op|'='
name|'request'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'ec2.request'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'apireq'
op|':'
newline|'\n'
indent|'            '
name|'controller'
op|'='
name|'apireq'
op|'.'
name|'controller'
newline|'\n'
name|'action'
op|'='
name|'apireq'
op|'.'
name|'action'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'controller'
op|'='
name|'None'
newline|'\n'
name|'action'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'ctxt'
op|'='
name|'request'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'nova.context'"
op|','
name|'None'
op|')'
newline|'\n'
name|'delta'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'start'
newline|'\n'
name|'seconds'
op|'='
name|'delta'
op|'.'
name|'seconds'
newline|'\n'
name|'microseconds'
op|'='
name|'delta'
op|'.'
name|'microseconds'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
nl|'\n'
string|'"%s.%ss %s %s %s %s:%s %s [%s] %s %s"'
op|','
nl|'\n'
name|'seconds'
op|','
nl|'\n'
name|'microseconds'
op|','
nl|'\n'
name|'request'
op|'.'
name|'remote_addr'
op|','
nl|'\n'
name|'request'
op|'.'
name|'method'
op|','
nl|'\n'
string|'"%s%s"'
op|'%'
op|'('
name|'request'
op|'.'
name|'script_name'
op|','
name|'request'
op|'.'
name|'path_info'
op|')'
op|','
nl|'\n'
name|'controller'
op|','
nl|'\n'
name|'action'
op|','
nl|'\n'
name|'response'
op|'.'
name|'status_int'
op|','
nl|'\n'
name|'request'
op|'.'
name|'user_agent'
op|','
nl|'\n'
name|'request'
op|'.'
name|'content_type'
op|','
nl|'\n'
name|'response'
op|'.'
name|'content_type'
op|','
nl|'\n'
name|'context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Lockout
dedent|''
dedent|''
name|'class'
name|'Lockout'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Lockout for x minutes on y failed auths in a z minute period.\n\n    x = lockout_timeout flag\n    y = lockout_window flag\n    z = lockout_attempts flag\n\n    Uses memcached if lockout_memcached_servers flag is set, otherwise it\n    uses a very simple in-proccess cache. Due to the simplicity of\n    the implementation, the timeout window is started with the first\n    failed request, so it will block if there are x failed logins within\n    that period.\n\n    There is a possible race condition where simultaneous requests could\n    sneak in before the lockout hits, but this is extremely rare and would\n    only result in a couple of extra failed attempts."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""middleware can use fake for testing."""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'memcached_servers'
op|':'
newline|'\n'
indent|'            '
name|'import'
name|'memcache'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'from'
name|'nova'
name|'import'
name|'fakememcache'
name|'as'
name|'memcache'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mc'
op|'='
name|'memcache'
op|'.'
name|'Client'
op|'('
name|'FLAGS'
op|'.'
name|'memcached_servers'
op|','
nl|'\n'
name|'debug'
op|'='
number|'0'
op|')'
newline|'\n'
name|'super'
op|'('
name|'Lockout'
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
name|'access_key'
op|'='
name|'str'
op|'('
name|'req'
op|'.'
name|'params'
op|'['
string|"'AWSAccessKeyId'"
op|']'
op|')'
newline|'\n'
name|'failures_key'
op|'='
string|'"authfailures-%s"'
op|'%'
name|'access_key'
newline|'\n'
name|'failures'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'mc'
op|'.'
name|'get'
op|'('
name|'failures_key'
op|')'
name|'or'
number|'0'
op|')'
newline|'\n'
name|'if'
name|'failures'
op|'>='
name|'FLAGS'
op|'.'
name|'lockout_attempts'
op|':'
newline|'\n'
indent|'            '
name|'detail'
op|'='
name|'_'
op|'('
string|'"Too many failed authentications."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'detail'
op|'='
name|'detail'
op|')'
newline|'\n'
dedent|''
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
name|'if'
name|'res'
op|'.'
name|'status_int'
op|'=='
number|'403'
op|':'
newline|'\n'
indent|'            '
name|'failures'
op|'='
name|'self'
op|'.'
name|'mc'
op|'.'
name|'incr'
op|'('
name|'failures_key'
op|')'
newline|'\n'
name|'if'
name|'failures'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# NOTE(vish): To use incr, failures has to be a string.'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'failures_key'
op|','
string|"'1'"
op|','
name|'time'
op|'='
name|'FLAGS'
op|'.'
name|'lockout_window'
op|'*'
number|'60'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'failures'
op|'>='
name|'FLAGS'
op|'.'
name|'lockout_attempts'
op|':'
newline|'\n'
indent|'                '
name|'lock_mins'
op|'='
name|'FLAGS'
op|'.'
name|'lockout_minutes'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'Access key %(access_key)s has had %(failures)d'"
nl|'\n'
string|"' failed authentications and will be locked out'"
nl|'\n'
string|"' for %(lock_mins)d minutes.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'failures_key'
op|','
name|'str'
op|'('
name|'failures'
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'FLAGS'
op|'.'
name|'lockout_minutes'
op|'*'
number|'60'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Authenticate
dedent|''
dedent|''
name|'class'
name|'Authenticate'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Authenticate an EC2 request and add \'nova.context\' to WSGI environ."""'
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
comment|'# Read request signature and access id.'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'signature'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'Signature'"
op|']'
newline|'\n'
name|'access'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'AWSAccessKeyId'"
op|']'
newline|'\n'
dedent|''
name|'except'
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
op|')'
newline|'\n'
nl|'\n'
comment|'# Make a copy of args for authentication and signature verification.'
nl|'\n'
dedent|''
name|'auth_params'
op|'='
name|'dict'
op|'('
name|'req'
op|'.'
name|'params'
op|')'
newline|'\n'
comment|'# Not part of authentication args'
nl|'\n'
name|'auth_params'
op|'.'
name|'pop'
op|'('
string|"'Signature'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Authenticate the request.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'user'
op|','
name|'project'
op|')'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'authenticate'
op|'('
nl|'\n'
name|'access'
op|','
nl|'\n'
name|'signature'
op|','
nl|'\n'
name|'auth_params'
op|','
nl|'\n'
name|'req'
op|'.'
name|'method'
op|','
nl|'\n'
name|'req'
op|'.'
name|'host'
op|','
nl|'\n'
name|'req'
op|'.'
name|'path'
op|')'
newline|'\n'
comment|'# Be explicit for what exceptions are 403, the rest bubble as 500'
nl|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
name|'exception'
op|'.'
name|'NotAuthorized'
op|')'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Authentication Failure: %s"'
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
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
comment|'# Authenticated!'
nl|'\n'
dedent|''
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
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|'='
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'user'
op|'.'
name|'is_admin'
op|'('
op|')'
op|','
nl|'\n'
name|'remote_address'
op|'='
name|'remote_address'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'ctxt'
newline|'\n'
name|'uname'
op|'='
name|'user'
op|'.'
name|'name'
newline|'\n'
name|'pname'
op|'='
name|'project'
op|'.'
name|'name'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'Authenticated Request For %(uname)s:%(pname)s)'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Requestify
dedent|''
dedent|''
name|'class'
name|'Requestify'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
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
name|'app'
op|','
name|'controller'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Requestify'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'controller'
op|')'
op|'('
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
name|'non_args'
op|'='
op|'['
string|"'Action'"
op|','
string|"'Signature'"
op|','
string|"'AWSAccessKeyId'"
op|','
string|"'SignatureMethod'"
op|','
nl|'\n'
string|"'SignatureVersion'"
op|','
string|"'Version'"
op|','
string|"'Timestamp'"
op|']'
newline|'\n'
name|'args'
op|'='
name|'dict'
op|'('
name|'req'
op|'.'
name|'params'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Raise KeyError if omitted'
nl|'\n'
indent|'            '
name|'action'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'Action'"
op|']'
newline|'\n'
comment|'# Fix bug lp:720157 for older (version 1) clients'
nl|'\n'
name|'version'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'SignatureVersion'"
op|']'
newline|'\n'
name|'if'
name|'int'
op|'('
name|'version'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'non_args'
op|'.'
name|'remove'
op|'('
string|"'SignatureMethod'"
op|')'
newline|'\n'
name|'if'
string|"'SignatureMethod'"
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'.'
name|'pop'
op|'('
string|"'SignatureMethod'"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'non_arg'
name|'in'
name|'non_args'
op|':'
newline|'\n'
comment|'# Remove, but raise KeyError if omitted'
nl|'\n'
indent|'                '
name|'args'
op|'.'
name|'pop'
op|'('
name|'non_arg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
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
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'action: %s'"
op|')'
op|','
name|'action'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'args'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'arg: %(key)s\\t\\tval: %(value)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Success!'
nl|'\n'
dedent|''
name|'api_request'
op|'='
name|'apirequest'
op|'.'
name|'APIRequest'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
name|'action'
op|','
nl|'\n'
name|'req'
op|'.'
name|'params'
op|'['
string|"'Version'"
op|']'
op|','
name|'args'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.request'"
op|']'
op|'='
name|'api_request'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action_args'"
op|']'
op|'='
name|'args'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Authorizer
dedent|''
dedent|''
name|'class'
name|'Authorizer'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Authorize an EC2 API request.\n\n    Return a 401 if ec2.controller and ec2.action in WSGI environ may not be\n    executed in nova.context.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Authorizer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'action_roles'
op|'='
op|'{'
nl|'\n'
string|"'CloudController'"
op|':'
op|'{'
nl|'\n'
string|"'DescribeAvailabilityZones'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeRegions'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeSnapshots'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeKeyPairs'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'CreateKeyPair'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DeleteKeyPair'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeSecurityGroups'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'ImportPublicKey'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'AuthorizeSecurityGroupIngress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'RevokeSecurityGroupIngress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'CreateSecurityGroup'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'DeleteSecurityGroup'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'GetConsoleOutput'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeVolumes'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'CreateVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'AttachVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DetachVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeInstances'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeAddresses'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'AllocateAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'ReleaseAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'AssociateAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'DisassociateAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'RunInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'TerminateInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'RebootInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'UpdateInstance'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'StartInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'StopInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DeleteVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeImages'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DeregisterImage'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'RegisterImage'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeImageAttribute'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'ModifyImageAttribute'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'UpdateImage'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'CreateImage'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'AdminController'"
op|':'
op|'{'
nl|'\n'
comment|"# All actions have the same permission: ['none'] (the default)"
nl|'\n'
comment|'# superusers will be allowed to run them'
nl|'\n'
comment|'# all others will get HTTPUnauthorized.'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'controller'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.request'"
op|']'
op|'.'
name|'controller'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'action'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.request'"
op|']'
op|'.'
name|'action'
newline|'\n'
name|'allowed_roles'
op|'='
name|'self'
op|'.'
name|'action_roles'
op|'['
name|'controller'
op|']'
op|'.'
name|'get'
op|'('
name|'action'
op|','
op|'['
string|"'none'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_matches_any_role'
op|'('
name|'context'
op|','
name|'allowed_roles'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Unauthorized request for controller=%(controller)s '"
nl|'\n'
string|"'and action=%(action)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_matches_any_role
dedent|''
dedent|''
name|'def'
name|'_matches_any_role'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'roles'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if any role in roles is allowed in context."""'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
string|"'all'"
name|'in'
name|'roles'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
string|"'none'"
name|'in'
name|'roles'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'any'
op|'('
name|'role'
name|'in'
name|'context'
op|'.'
name|'roles'
name|'for'
name|'role'
name|'in'
name|'roles'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Executor
dedent|''
dedent|''
name|'class'
name|'Executor'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Execute an EC2 API request.\n\n    Executes \'ec2.action\' upon \'ec2.controller\', passing \'nova.context\' and\n    \'ec2.action_args\' (all variables in WSGI environ.)  Returns an XML\n    response, or a 400 upon failure.\n    """'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'api_request'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.request'"
op|']'
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'api_request'
op|'.'
name|'invoke'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'InstanceNotFound raised: %s'"
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'context'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'ex'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'VolumeNotFound'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'VolumeNotFound raised: %s'"
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_vol_id'
op|'('
name|'ex'
op|'.'
name|'volume_id'
op|')'
newline|'\n'
name|'message'
op|'='
name|'_'
op|'('
string|"'Volume %s not found'"
op|')'
op|'%'
name|'ec2_id'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'context'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'SnapshotNotFound'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'SnapshotNotFound raised: %s'"
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_snap_id'
op|'('
name|'ex'
op|'.'
name|'snapshot_id'
op|')'
newline|'\n'
name|'message'
op|'='
name|'_'
op|'('
string|"'Snapshot %s not found'"
op|')'
op|'%'
name|'ec2_id'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'context'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'message'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'NotFound raised: %s'"
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'context'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ApiError'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'ApiError raised: %s'"
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'if'
name|'ex'
op|'.'
name|'code'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'context'
op|','
name|'ex'
op|'.'
name|'code'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
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
name|'_error'
op|'('
name|'req'
op|','
name|'context'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
nl|'\n'
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'KeyPairExists'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'KeyPairExists raised: %s'"
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'context'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'='
op|'{'
string|"'environment'"
op|':'
name|'req'
op|'.'
name|'environ'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Unexpected error raised: %s'"
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|','
nl|'\n'
name|'extra'
op|'='
name|'extra'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
nl|'\n'
name|'context'
op|','
nl|'\n'
string|"'UnknownError'"
op|','
nl|'\n'
name|'_'
op|'('
string|"'An unknown error has occurred. '"
nl|'\n'
string|"'Please try your request again.'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'resp'
op|'.'
name|'status'
op|'='
number|'200'
newline|'\n'
name|'resp'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'text/xml'"
newline|'\n'
name|'resp'
op|'.'
name|'body'
op|'='
name|'str'
op|'('
name|'result'
op|')'
newline|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
DECL|member|_error
dedent|''
dedent|''
name|'def'
name|'_error'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'context'
op|','
name|'code'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"%s: %s"'
op|','
name|'code'
op|','
name|'message'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'resp'
op|'.'
name|'status'
op|'='
number|'400'
newline|'\n'
name|'resp'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'text/xml'"
newline|'\n'
name|'resp'
op|'.'
name|'body'
op|'='
name|'str'
op|'('
string|'\'<?xml version="1.0"?>\\n\''
nl|'\n'
string|"'<Response><Errors><Error><Code>%s</Code>'"
nl|'\n'
string|"'<Message>%s</Message></Error></Errors>'"
nl|'\n'
string|"'<RequestID>%s</RequestID></Response>'"
op|'%'
nl|'\n'
op|'('
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'code'
op|')'
op|','
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'message'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'context'
op|'.'
name|'request_id'
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Versions
dedent|''
dedent|''
name|'class'
name|'Versions'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
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
string|'"""Respond to a request for all EC2 versions."""'
newline|'\n'
comment|'# available api versions'
nl|'\n'
name|'versions'
op|'='
op|'['
nl|'\n'
string|"'1.0'"
op|','
nl|'\n'
string|"'2007-01-19'"
op|','
nl|'\n'
string|"'2007-03-01'"
op|','
nl|'\n'
string|"'2007-08-29'"
op|','
nl|'\n'
string|"'2007-10-10'"
op|','
nl|'\n'
string|"'2007-12-15'"
op|','
nl|'\n'
string|"'2008-02-01'"
op|','
nl|'\n'
string|"'2008-09-01'"
op|','
nl|'\n'
string|"'2009-04-04'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
string|"'%s\\n'"
op|'%'
name|'v'
name|'for'
name|'v'
name|'in'
name|'versions'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
