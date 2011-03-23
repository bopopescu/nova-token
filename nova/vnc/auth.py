begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# pylint: disable-msg=C0103'
nl|'\n'
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
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""Auth Components for VNC Console"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'Request'
newline|'\n'
nl|'\n'
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
name|'rpc'
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
name|'import'
name|'vnc'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.vnc-proxy'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaAuthMiddleware
name|'class'
name|'NovaAuthMiddleware'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implementation of Middleware to Handle Nova Auth"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'app'
op|'='
name|'app'
newline|'\n'
name|'self'
op|'.'
name|'register_listeners'
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
name|'token'
op|'='
name|'req'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
string|"'token'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'token'
op|':'
newline|'\n'
indent|'            '
name|'referrer'
op|'='
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'HTTP_REFERER'"
op|')'
newline|'\n'
name|'auth_params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'referrer'
op|')'
op|'.'
name|'query'
op|')'
newline|'\n'
name|'if'
string|"'token'"
name|'in'
name|'auth_params'
op|':'
newline|'\n'
indent|'                '
name|'token'
op|'='
name|'auth_params'
op|'['
string|"'token'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'token'
name|'in'
name|'self'
op|'.'
name|'tokens'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Unauthorized Access: (%s)"'
op|')'
op|','
name|'req'
op|'.'
name|'environ'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'detail'
op|'='
string|"'Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'req'
op|'.'
name|'path'
op|'=='
name|'vnc'
op|'.'
name|'proxy'
op|'.'
name|'WS_ENDPOINT'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'.'
name|'environ'
op|'['
string|"'vnc_host'"
op|']'
op|'='
name|'self'
op|'.'
name|'tokens'
op|'['
name|'token'
op|']'
op|'['
string|"'args'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'vnc_port'"
op|']'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'tokens'
op|'['
name|'token'
op|']'
op|'['
string|"'args'"
op|']'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|register_listeners
dedent|''
name|'def'
name|'register_listeners'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'middleware'
op|'='
name|'self'
newline|'\n'
name|'middleware'
op|'.'
name|'tokens'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|Callback
name|'class'
name|'Callback'
op|':'
newline|'\n'
DECL|member|__call__
indent|'            '
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'data'
op|'['
string|"'method'"
op|']'
op|'=='
string|"'authorize_vnc_console'"
op|':'
newline|'\n'
indent|'                    '
name|'token'
op|'='
name|'data'
op|'['
string|"'args'"
op|']'
op|'['
string|"'token'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Received Token: %s)"'
op|')'
op|','
name|'token'
op|')'
newline|'\n'
name|'middleware'
op|'.'
name|'tokens'
op|'['
name|'token'
op|']'
op|'='
op|'{'
string|"'args'"
op|':'
name|'data'
op|'['
string|"'args'"
op|']'
op|','
string|"'last_activity_at'"
op|':'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|delete_expired_tokens
dedent|''
dedent|''
dedent|''
name|'def'
name|'delete_expired_tokens'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'now'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'to_delete'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'middleware'
op|'.'
name|'tokens'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'now'
op|'-'
name|'v'
op|'['
string|"'last_activity_at'"
op|']'
op|'>'
name|'FLAGS'
op|'.'
name|'vnc_token_ttl'
op|':'
newline|'\n'
indent|'                    '
name|'to_delete'
op|'.'
name|'append'
op|'('
name|'k'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'k'
name|'in'
name|'to_delete'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Deleting Token: %s)"'
op|')'
op|','
name|'k'
op|')'
newline|'\n'
name|'del'
name|'middleware'
op|'.'
name|'tokens'
op|'['
name|'k'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
name|'consumer'
op|'='
name|'rpc'
op|'.'
name|'TopicConsumer'
op|'('
nl|'\n'
name|'connection'
op|'='
name|'conn'
op|','
nl|'\n'
name|'topic'
op|'='
name|'FLAGS'
op|'.'
name|'vnc_console_proxy_topic'
op|')'
newline|'\n'
name|'consumer'
op|'.'
name|'register_callback'
op|'('
name|'Callback'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'consumer'
op|'.'
name|'fetch'
op|','
name|'auto_ack'
op|'='
name|'True'
op|','
nl|'\n'
name|'enable_callbacks'
op|'='
name|'True'
op|')'
op|'.'
name|'start'
op|'('
number|'0.1'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'delete_expired_tokens'
op|')'
op|'.'
name|'start'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoggingMiddleware
dedent|''
dedent|''
name|'class'
name|'LoggingMiddleware'
op|'('
name|'object'
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
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'app'
op|'='
name|'app'
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
nl|'\n'
indent|'        '
name|'if'
name|'req'
op|'.'
name|'path'
op|'=='
name|'vnc'
op|'.'
name|'proxy'
op|'.'
name|'WS_ENDPOINT'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Received Websocket Request: %s"'
op|')'
op|','
name|'req'
op|'.'
name|'url'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Received Request: %s"'
op|')'
op|','
name|'req'
op|'.'
name|'url'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
