begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 Openstack, LLC.'
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
string|'"""Eventlet WSGI Services to proxy VNC for XCP protocol."""'
newline|'\n'
nl|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'green'
newline|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'greenio'
newline|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'wsgi'
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
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.xvpvncproxy'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|xvp_proxy_opts
name|'xvp_proxy_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'xvpvncproxy_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'6081'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Port that the XCP VNC proxy should bind to'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'xvpvncproxy_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'0.0.0.0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Address that the XCP VNC proxy should bind to'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'add_options'
op|'('
name|'xvp_proxy_opts'
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'consoleauth_topic'"
op|','
string|"'nova.consoleauth'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XCPVNCProxy
name|'class'
name|'XCPVNCProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class to use the xvp auth protocol to proxy instance vnc consoles."""'
newline|'\n'
nl|'\n'
DECL|member|one_way_proxy
name|'def'
name|'one_way_proxy'
op|'('
name|'self'
op|','
name|'source'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Proxy tcp connection from source to dest."""'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'source'
op|'.'
name|'recv'
op|'('
number|'32384'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# If recv fails, send a write shutdown the other direction'
nl|'\n'
dedent|''
name|'if'
name|'d'
name|'is'
name|'None'
name|'or'
name|'len'
op|'('
name|'d'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'dest'
op|'.'
name|'shutdown'
op|'('
name|'socket'
op|'.'
name|'SHUT_WR'
op|')'
newline|'\n'
name|'break'
newline|'\n'
comment|'# If send fails, terminate proxy in both directions'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# sendall raises an exception on write error, unlike send'
nl|'\n'
indent|'                '
name|'dest'
op|'.'
name|'sendall'
op|'('
name|'d'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'source'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'dest'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
DECL|member|handshake
dedent|''
dedent|''
dedent|''
name|'def'
name|'handshake'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'connect_info'
op|','
name|'sockets'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Execute hypervisor-specific vnc auth handshaking (if needed)."""'
newline|'\n'
name|'host'
op|'='
name|'connect_info'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'port'
op|'='
name|'int'
op|'('
name|'connect_info'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'='
name|'eventlet'
op|'.'
name|'connect'
op|'('
op|'('
name|'host'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Handshake as necessary'
nl|'\n'
name|'if'
name|'connect_info'
op|'.'
name|'get'
op|'('
string|"'internal_access_path'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'.'
name|'sendall'
op|'('
string|'"CONNECT %s HTTP/1.1\\r\\n\\r\\n"'
op|'%'
nl|'\n'
name|'connect_info'
op|'['
string|"'internal_access_path'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
string|'""'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'b'
op|'='
name|'server'
op|'.'
name|'recv'
op|'('
number|'1'
op|')'
newline|'\n'
name|'if'
name|'b'
op|':'
newline|'\n'
indent|'                    '
name|'data'
op|'+='
name|'b'
newline|'\n'
name|'if'
name|'data'
op|'.'
name|'find'
op|'('
string|'"\\r\\n\\r\\n"'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'not'
name|'data'
op|'.'
name|'split'
op|'('
string|'"\\r\\n"'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'find'
op|'('
string|'"200"'
op|')'
op|':'
newline|'\n'
indent|'                            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Error in handshake: %s"'
op|')'
op|','
name|'data'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'b'
name|'or'
name|'len'
op|'('
name|'data'
op|')'
op|'>'
number|'4096'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Error in handshake: %s"'
op|')'
op|','
name|'data'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'client'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'eventlet.input'"
op|']'
op|'.'
name|'get_socket'
op|'('
op|')'
newline|'\n'
name|'client'
op|'.'
name|'sendall'
op|'('
string|'"HTTP/1.1 200 OK\\r\\n\\r\\n"'
op|')'
newline|'\n'
name|'socketsserver'
op|'='
name|'None'
newline|'\n'
name|'sockets'
op|'['
string|"'client'"
op|']'
op|'='
name|'client'
newline|'\n'
name|'sockets'
op|'['
string|"'server'"
op|']'
op|'='
name|'server'
newline|'\n'
nl|'\n'
DECL|member|proxy_connection
dedent|''
name|'def'
name|'proxy_connection'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'connect_info'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Spawn bi-directional vnc proxy."""'
newline|'\n'
name|'sockets'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'t0'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'handshake'
op|','
name|'req'
op|','
name|'connect_info'
op|','
name|'sockets'
op|')'
newline|'\n'
name|'t0'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'sockets'
op|'.'
name|'get'
op|'('
string|"'client'"
op|')'
name|'or'
name|'not'
name|'sockets'
op|'.'
name|'get'
op|'('
string|"'server'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Invalid request: %s"'
op|')'
op|','
name|'req'
op|')'
newline|'\n'
name|'start_response'
op|'('
string|"'400 Invalid Request'"
op|','
nl|'\n'
op|'['
op|'('
string|"'content-type'"
op|','
string|"'text/html'"
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
string|'"Invalid Request"'
newline|'\n'
nl|'\n'
dedent|''
name|'client'
op|'='
name|'sockets'
op|'['
string|"'client'"
op|']'
newline|'\n'
name|'server'
op|'='
name|'sockets'
op|'['
string|"'server'"
op|']'
newline|'\n'
nl|'\n'
name|'t1'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'one_way_proxy'
op|','
name|'client'
op|','
name|'server'
op|')'
newline|'\n'
name|'t2'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'one_way_proxy'
op|','
name|'server'
op|','
name|'client'
op|')'
newline|'\n'
name|'t1'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'t2'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure our sockets are closed'
nl|'\n'
name|'server'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'client'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'('
name|'environ'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Request: %s"'
op|')'
op|','
name|'req'
op|')'
newline|'\n'
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
name|'if'
name|'not'
name|'token'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Request made with missing token: %s"'
op|')'
op|','
name|'req'
op|')'
newline|'\n'
name|'start_response'
op|'('
string|"'400 Invalid Request'"
op|','
nl|'\n'
op|'['
op|'('
string|"'content-type'"
op|','
string|"'text/html'"
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
string|'"Invalid Request"'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'connect_info'
op|'='
name|'rpc'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'FLAGS'
op|'.'
name|'consoleauth_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'check_token'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'token'"
op|':'
name|'token'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'connect_info'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Request made with invalid token: %s"'
op|')'
op|','
name|'req'
op|')'
newline|'\n'
name|'start_response'
op|'('
string|"'401 Not Authorized'"
op|','
nl|'\n'
op|'['
op|'('
string|"'content-type'"
op|','
string|"'text/html'"
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
string|'"Not Authorized"'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'proxy_connection'
op|'('
name|'req'
op|','
name|'connect_info'
op|','
name|'start_response'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Unexpected error: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SafeHttpProtocol
dedent|''
dedent|''
dedent|''
name|'class'
name|'SafeHttpProtocol'
op|'('
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'HttpProtocol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""HttpProtocol wrapper to suppress IOErrors.\n\n       The proxy code above always shuts down client connections, so we catch\n       the IOError that raises when the SocketServer tries to flush the\n       connection.\n    """'
newline|'\n'
DECL|member|finish
name|'def'
name|'finish'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'eventlet'
op|'.'
name|'green'
op|'.'
name|'BaseHTTPServer'
op|'.'
name|'BaseHTTPRequestHandler'
op|'.'
name|'finish'
op|'('
name|'self'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'eventlet'
op|'.'
name|'greenio'
op|'.'
name|'shutdown_safe'
op|'('
name|'self'
op|'.'
name|'connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_wsgi_server
dedent|''
dedent|''
name|'def'
name|'get_wsgi_server'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Starting nova-xvpvncproxy node (version %s)"'
op|')'
op|','
nl|'\n'
name|'version'
op|'.'
name|'version_string_with_vcs'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"XCP VNC Proxy"'
op|','
nl|'\n'
name|'XCPVNCProxy'
op|'('
op|')'
op|','
nl|'\n'
name|'protocol'
op|'='
name|'SafeHttpProtocol'
op|','
nl|'\n'
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'xvpvncproxy_host'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'xvpvncproxy_port'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
