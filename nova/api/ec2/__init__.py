begin_unit
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
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
DECL|variable|_DEPRECATED_MIDDLEWARE
name|'_DEPRECATED_MIDDLEWARE'
op|'='
op|'('
nl|'\n'
string|"'%s has been deprecated and removed from Nova in Mitaka. '"
nl|'\n'
string|"'You will need to remove lines referencing it in your paste.ini before '"
nl|'\n'
string|"'upgrade to Newton or your cloud will break.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_DEPRECATION_MESSAGE
name|'_DEPRECATION_MESSAGE'
op|'='
op|'('
string|"'The in tree EC2 API has been removed in Mitaka. '"
nl|'\n'
string|"'Please remove entries from api-paste.ini'"
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(sdague): this whole file is safe to remove in Newton. We just'
nl|'\n'
comment|'# needed a release cycle for it.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DeprecatedMiddleware
name|'class'
name|'DeprecatedMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'DeprecatedMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
name|'_DEPRECATED_MIDDLEWARE'
op|'%'
name|'type'
op|'('
name|'self'
op|')'
op|'.'
name|'__name__'
op|')'
op|')'
comment|'# noqa'
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
comment|'# deprecated middleware needs to be a no op, not an exception'
nl|'\n'
indent|'        '
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FaultWrapper
dedent|''
dedent|''
name|'class'
name|'FaultWrapper'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Lockout
dedent|''
name|'class'
name|'Lockout'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EC2KeystoneAuth
dedent|''
name|'class'
name|'EC2KeystoneAuth'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoAuth
dedent|''
name|'class'
name|'NoAuth'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Requestify
dedent|''
name|'class'
name|'Requestify'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Authorizer
dedent|''
name|'class'
name|'Authorizer'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestLogging
dedent|''
name|'class'
name|'RequestLogging'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Validator
dedent|''
name|'class'
name|'Validator'
op|'('
name|'DeprecatedMiddleware'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Executor
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
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'_DEPRECATION_MESSAGE'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
