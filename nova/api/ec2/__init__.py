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
nl|'\n'
string|'"""\nStarting point for routing EC2 requests\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'routes'
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
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'admin'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
DECL|variable|_log
name|'_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"api"'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Routing for all EC2 API requests."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'Authenticate'
op|'('
name|'Router'
op|'('
op|')'
op|')'
newline|'\n'
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
string|'"""Authenticates an EC2 request."""'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
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
comment|'#TODO(gundlach): where do arguments come from?'
nl|'\n'
indent|'        '
name|'args'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'arguments'
newline|'\n'
nl|'\n'
comment|'# Read request signature.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'signature'
op|'='
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Signature'"
op|')'
op|'['
number|'0'
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
op|'{'
op|'}'
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
name|'auth_params'
op|'['
name|'key'
op|']'
op|'='
name|'value'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Get requested action and remove authentication args for final request.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'='
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Action'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'access'
op|'='
name|'args'
op|'.'
name|'pop'
op|'('
string|"'AWSAccessKeyId'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'SignatureMethod'"
op|')'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'SignatureVersion'"
op|')'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Version'"
op|')'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Timestamp'"
op|')'
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
comment|'# Authenticate the request.'
nl|'\n'
dedent|''
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
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Error'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Authentication Failure: %s"'
op|'%'
name|'ex'
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
dedent|''
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'action: %s'"
op|'%'
name|'action'
op|')'
newline|'\n'
nl|'\n'
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
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'arg: %s\\t\\tval: %s'"
op|'%'
op|'('
name|'key'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Authenticated!'
nl|'\n'
dedent|''
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action'"
op|']'
op|'='
name|'action'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.context'"
op|']'
op|'='
name|'APIRequestContext'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Finds controller for a request, executes environ[\'ec2.action\'] upon it, and\n    returns an XML response.  If the action fails, returns a 400.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'map'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'.'
name|'connect'
op|'('
string|'"/{controller_name}/"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controllers'
op|'='
name|'dict'
op|'('
name|'Cloud'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
op|','
nl|'\n'
name|'Admin'
op|'='
name|'admin'
op|'.'
name|'AdminController'
op|'('
op|')'
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
comment|'# Obtain the appropriate controller for this request.'
nl|'\n'
indent|'        '
name|'match'
op|'='
name|'self'
op|'.'
name|'map'
op|'.'
name|'match'
op|'('
name|'req'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'match'
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
op|')'
newline|'\n'
dedent|''
name|'controller_name'
op|'='
name|'match'
op|'['
string|"'controller_name'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'controller'
op|'='
name|'self'
op|'.'
name|'controllers'
op|'['
name|'controller_name'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error'
op|'('
string|"'unhandled'"
op|','
string|"'no controller named %s'"
op|'%'
name|'controller_name'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'api_request'
op|'='
name|'APIRequest'
op|'('
name|'controller'
op|','
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action'"
op|']'
op|')'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'api_request'
op|'.'
name|'send'
op|'('
name|'context'
op|','
op|'**'
name|'args'
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
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|'+'
string|'"."'
op|'+'
name|'ex'
op|'.'
name|'code'
op|','
name|'ex'
op|'.'
name|'message'
op|')'
newline|'\n'
comment|'# TODO(vish): do something more useful with unknown exceptions'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error'
op|'('
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'str'
op|'('
name|'ex'
op|')'
op|')'
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
name|'code'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'.'
name|'status'
op|'='
number|'400'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'text/xml'"
newline|'\n'
name|'req'
op|'.'
name|'response'
op|'='
op|'('
string|'\'<?xml version="1.0"?>\\n\''
nl|'\n'
string|"'<Response><Errors><Error><Code>%s</Code>'"
nl|'\n'
string|"'<Message>%s</Message></Error></Errors>'"
nl|'\n'
string|"'<RequestID>?</RequestID></Response>'"
op|')'
op|'%'
op|'('
name|'code'
op|','
name|'message'
op|')'
op|')'
newline|'\n'
newline|'\n'
end_unit
