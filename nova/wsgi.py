begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""Utility methods for working with WSGI servers."""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'print_function'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'wsgi'
newline|'\n'
name|'import'
name|'greenlet'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'paste'
name|'import'
name|'deploy'
newline|'\n'
name|'import'
name|'routes'
op|'.'
name|'middleware'
newline|'\n'
name|'import'
name|'ssl'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
comment|'# Raise the default from 8192 to accommodate large tokens'
nl|'\n'
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'MAX_HEADER_LINE'
op|'='
number|'16384'
newline|'\n'
nl|'\n'
DECL|variable|wsgi_opts
name|'wsgi_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'api_paste_config'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"api-paste.ini"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'File name for the paste.deploy config for nova-api'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'wsgi_log_format'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'\'%(client_ip)s "%(request_line)s" status: %(status_code)s\''
nl|'\n'
string|"' len: %(body_length)s time: %(wall_seconds).7f'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A python format string that is used as the template to '"
nl|'\n'
string|"'generate log lines. The following values can be formatted '"
nl|'\n'
string|"'into it: client_ip, date_time, request_line, status_code, '"
nl|'\n'
string|"'body_length, wall_seconds.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ssl_ca_file'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"CA certificate file to use to verify "'
nl|'\n'
string|'"connecting clients"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ssl_cert_file'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"SSL certificate of API server"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ssl_key_file'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"SSL private key of API server"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'tcp_keepidle'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Sets the value of TCP_KEEPIDLE in seconds for each "'
nl|'\n'
string|'"server socket. Not supported on OS X."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'wsgi_default_pool_size'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Size of the pool of greenthreads used by wsgi"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
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
name|'wsgi_opts'
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
DECL|class|Server
name|'class'
name|'Server'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server class to manage a WSGI server, serving a WSGI application."""'
newline|'\n'
nl|'\n'
DECL|variable|default_pool_size
name|'default_pool_size'
op|'='
name|'CONF'
op|'.'
name|'wsgi_default_pool_size'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'app'
op|','
name|'host'
op|'='
string|"'0.0.0.0'"
op|','
name|'port'
op|'='
number|'0'
op|','
name|'pool_size'
op|'='
name|'None'
op|','
nl|'\n'
name|'protocol'
op|'='
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'HttpProtocol'
op|','
name|'backlog'
op|'='
number|'128'
op|','
nl|'\n'
name|'use_ssl'
op|'='
name|'False'
op|','
name|'max_url_len'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize, but do not start, a WSGI server.\n\n        :param name: Pretty name for logging.\n        :param app: The WSGI application to serve.\n        :param host: IP address to serve the application.\n        :param port: Port number to server the application.\n        :param pool_size: Maximum number of eventlets to spawn concurrently.\n        :param backlog: Maximum number of queued connections.\n        :param max_url_len: Maximum length of permitted URLs.\n        :returns: None\n        :raises: nova.exception.InvalidInput\n        """'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'app'
newline|'\n'
name|'self'
op|'.'
name|'_server'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_protocol'
op|'='
name|'protocol'
newline|'\n'
name|'self'
op|'.'
name|'_pool'
op|'='
name|'eventlet'
op|'.'
name|'GreenPool'
op|'('
name|'pool_size'
name|'or'
name|'self'
op|'.'
name|'default_pool_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_logger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.%s.wsgi.server"'
op|'%'
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wsgi_logger'
op|'='
name|'logging'
op|'.'
name|'WritableLogger'
op|'('
name|'self'
op|'.'
name|'_logger'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_use_ssl'
op|'='
name|'use_ssl'
newline|'\n'
name|'self'
op|'.'
name|'_max_url_len'
op|'='
name|'max_url_len'
newline|'\n'
nl|'\n'
name|'if'
name|'backlog'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
nl|'\n'
name|'reason'
op|'='
string|"'The backlog must be more than 1'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bind_addr'
op|'='
op|'('
name|'host'
op|','
name|'port'
op|')'
newline|'\n'
comment|"# TODO(dims): eventlet's green dns/socket module does not actually"
nl|'\n'
comment|'# support IPv6 in getaddrinfo(). We need to get around this in the'
nl|'\n'
comment|'# future or monitor upstream for a fix'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'='
name|'socket'
op|'.'
name|'getaddrinfo'
op|'('
name|'bind_addr'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'bind_addr'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'AF_UNSPEC'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'SOCK_STREAM'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'family'
op|'='
name|'info'
op|'['
number|'0'
op|']'
newline|'\n'
name|'bind_addr'
op|'='
name|'info'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'family'
op|'='
name|'socket'
op|'.'
name|'AF_INET'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_socket'
op|'='
name|'eventlet'
op|'.'
name|'listen'
op|'('
name|'bind_addr'
op|','
name|'family'
op|','
name|'backlog'
op|'='
name|'backlog'
op|')'
newline|'\n'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|')'
op|'='
name|'self'
op|'.'
name|'_socket'
op|'.'
name|'getsockname'
op|'('
op|')'
op|'['
number|'0'
op|':'
number|'2'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"%(name)s listening on %(host)s:%(port)s"'
op|')'
op|'%'
name|'self'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start serving a WSGI application.\n\n        :returns: None\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_use_ssl'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'ca_file'
op|'='
name|'CONF'
op|'.'
name|'ssl_ca_file'
newline|'\n'
name|'cert_file'
op|'='
name|'CONF'
op|'.'
name|'ssl_cert_file'
newline|'\n'
name|'key_file'
op|'='
name|'CONF'
op|'.'
name|'ssl_key_file'
newline|'\n'
nl|'\n'
name|'if'
name|'cert_file'
name|'and'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'cert_file'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unable to find cert_file : %s"'
op|')'
op|'%'
name|'cert_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ca_file'
name|'and'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_file'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unable to find ca_file : %s"'
op|')'
op|'%'
name|'ca_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'key_file'
name|'and'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'key_file'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unable to find key_file : %s"'
op|')'
op|'%'
name|'key_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_use_ssl'
name|'and'
op|'('
name|'not'
name|'cert_file'
name|'or'
name|'not'
name|'key_file'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"When running server in SSL mode, you must "'
nl|'\n'
string|'"specify both a cert_file and key_file "'
nl|'\n'
string|'"option value in your configuration file"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'ssl_kwargs'
op|'='
op|'{'
nl|'\n'
string|"'server_side'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'certfile'"
op|':'
name|'cert_file'
op|','
nl|'\n'
string|"'keyfile'"
op|':'
name|'key_file'
op|','
nl|'\n'
string|"'cert_reqs'"
op|':'
name|'ssl'
op|'.'
name|'CERT_NONE'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'ssl_ca_file'
op|':'
newline|'\n'
indent|'                    '
name|'ssl_kwargs'
op|'['
string|"'ca_certs'"
op|']'
op|'='
name|'ca_file'
newline|'\n'
name|'ssl_kwargs'
op|'['
string|"'cert_reqs'"
op|']'
op|'='
name|'ssl'
op|'.'
name|'CERT_REQUIRED'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_socket'
op|'='
name|'eventlet'
op|'.'
name|'wrap_ssl'
op|'('
name|'self'
op|'.'
name|'_socket'
op|','
nl|'\n'
op|'**'
name|'ssl_kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_socket'
op|'.'
name|'setsockopt'
op|'('
name|'socket'
op|'.'
name|'SOL_SOCKET'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'SO_REUSEADDR'
op|','
number|'1'
op|')'
newline|'\n'
comment|'# sockets can hang around forever without keepalive'
nl|'\n'
name|'self'
op|'.'
name|'_socket'
op|'.'
name|'setsockopt'
op|'('
name|'socket'
op|'.'
name|'SOL_SOCKET'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'SO_KEEPALIVE'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|"# This option isn't available in the OS X version of eventlet"
nl|'\n'
name|'if'
name|'hasattr'
op|'('
name|'socket'
op|','
string|"'TCP_KEEPIDLE'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_socket'
op|'.'
name|'setsockopt'
op|'('
name|'socket'
op|'.'
name|'IPPROTO_TCP'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'TCP_KEEPIDLE'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'tcp_keepidle'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Failed to start %(name)s on %(host)s"'
nl|'\n'
string|'":%(port)s with SSL support"'
op|')'
op|'%'
name|'self'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'wsgi_kwargs'
op|'='
op|'{'
nl|'\n'
string|"'func'"
op|':'
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'server'
op|','
nl|'\n'
string|"'sock'"
op|':'
name|'self'
op|'.'
name|'_socket'
op|','
nl|'\n'
string|"'site'"
op|':'
name|'self'
op|'.'
name|'app'
op|','
nl|'\n'
string|"'protocol'"
op|':'
name|'self'
op|'.'
name|'_protocol'
op|','
nl|'\n'
string|"'custom_pool'"
op|':'
name|'self'
op|'.'
name|'_pool'
op|','
nl|'\n'
string|"'log'"
op|':'
name|'self'
op|'.'
name|'_wsgi_logger'
op|','
nl|'\n'
string|"'log_format'"
op|':'
name|'CONF'
op|'.'
name|'wsgi_log_format'
op|','
nl|'\n'
string|"'debug'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_max_url_len'
op|':'
newline|'\n'
indent|'            '
name|'wsgi_kwargs'
op|'['
string|"'url_length_limit'"
op|']'
op|'='
name|'self'
op|'.'
name|'_max_url_len'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_server'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
op|'**'
name|'wsgi_kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop this server.\n\n        This is not a very nice action, as currently the method by which a\n        server is stopped is by killing its eventlet.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Stopping WSGI server."'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_server'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
comment|'# Resize pool to stop new requests from being processed'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_pool'
op|'.'
name|'resize'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_server'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Block, until the server has stopped.\n\n        Waits on the server\'s eventlet to finish, then returns.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_server'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"WSGI server has stopped."'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Request
dedent|''
dedent|''
dedent|''
name|'class'
name|'Request'
op|'('
name|'webob'
op|'.'
name|'Request'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Application
dedent|''
name|'class'
name|'Application'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base WSGI application wrapper. Subclasses need to implement __call__."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_config'
op|','
op|'**'
name|'local_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Used for paste app factories in paste.deploy config files.\n\n        Any local configuration (that is, values under the [app:APPNAME]\n        section of the paste config) will be passed into the `__init__` method\n        as kwargs.\n\n        A hypothetical configuration would look like:\n\n            [app:wadl]\n            latest_version = 1.3\n            paste.app_factory = nova.api.fancy_api:Wadl.factory\n\n        which would result in a call to the `Wadl` class as\n\n            import nova.api.fancy_api\n            fancy_api.Wadl(latest_version=\'1.3\')\n\n        You could of course re-implement the `factory` method in subclasses,\n        but using the kwarg passing it shouldn\'t be necessary.\n\n        """'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|'**'
name|'local_config'
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
string|'r"""Subclasses will probably want to implement __call__ like this:\n\n        @webob.dec.wsgify(RequestClass=Request)\n        def __call__(self, req):\n          # Any of the following objects work as responses:\n\n          # Option 1: simple string\n          res = \'message\\n\'\n\n          # Option 2: a nicely formatted HTTP exception page\n          res = exc.HTTPForbidden(detail=\'Nice try\')\n\n          # Option 3: a webob Response object (in case you need to play with\n          # headers, or you want to be treated like an iterable, or or or)\n          res = Response();\n          res.app_iter = open(\'somefile\')\n\n          # Option 4: any wsgi app to be run next\n          res = self.application\n\n          # Option 5: you can get a Response object for a wsgi app, too, to\n          # play with headers etc\n          res = req.get_response(self.application)\n\n          # You can then just return your response...\n          return res\n          # ... or set req.response and return None.\n          req.response = res\n\n        See the end of http://pythonpaste.org/webob/modules/dec.html\n        for more info.\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|"'You must implement __call__'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Middleware
dedent|''
dedent|''
name|'class'
name|'Middleware'
op|'('
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base WSGI middleware.\n\n    These classes require an application to be\n    initialized that will be called next.  By default the middleware will\n    simply call its wrapped app, or you can override __call__ to customize its\n    behavior.\n\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_config'
op|','
op|'**'
name|'local_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Used for paste app factories in paste.deploy config files.\n\n        Any local configuration (that is, values under the [filter:APPNAME]\n        section of the paste config) will be passed into the `__init__` method\n        as kwargs.\n\n        A hypothetical configuration would look like:\n\n            [filter:analytics]\n            redis_host = 127.0.0.1\n            paste.filter_factory = nova.api.analytics:Analytics.factory\n\n        which would result in a call to the `Analytics` class as\n\n            import nova.api.analytics\n            analytics.Analytics(app_from_paste, redis_host=\'127.0.0.1\')\n\n        You could of course re-implement the `factory` method in subclasses,\n        but using the kwarg passing it shouldn\'t be necessary.\n\n        """'
newline|'\n'
DECL|function|_factory
name|'def'
name|'_factory'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'('
name|'app'
op|','
op|'**'
name|'local_config'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_factory'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
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
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
nl|'\n'
DECL|member|process_request
dedent|''
name|'def'
name|'process_request'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called on each request.\n\n        If this returns None, the next application down the stack will be\n        executed. If it returns a response then that response will be returned\n        and execution will stop here.\n\n        """'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|process_response
dedent|''
name|'def'
name|'process_response'
op|'('
name|'self'
op|','
name|'response'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Do whatever you\'d like to the response."""'
newline|'\n'
name|'return'
name|'response'
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
name|'response'
op|'='
name|'self'
op|'.'
name|'process_request'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'response'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'response'
newline|'\n'
dedent|''
name|'response'
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
name|'return'
name|'self'
op|'.'
name|'process_response'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Debug
dedent|''
dedent|''
name|'class'
name|'Debug'
op|'('
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper class for debugging a WSGI application.\n\n    Can be inserted into any WSGI application chain to get information\n    about the request and response.\n\n    """'
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
name|'print'
op|'('
op|'('
string|"'*'"
op|'*'
number|'40'
op|')'
op|'+'
string|"' REQUEST ENVIRON'"
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'req'
op|'.'
name|'environ'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'print'
op|'('
name|'key'
op|','
string|"'='"
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'print'
op|'('
op|')'
newline|'\n'
name|'resp'
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
nl|'\n'
name|'print'
op|'('
op|'('
string|"'*'"
op|'*'
number|'40'
op|')'
op|'+'
string|"' RESPONSE HEADERS'"
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'resp'
op|'.'
name|'headers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'print'
op|'('
name|'key'
op|','
string|"'='"
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'print'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'resp'
op|'.'
name|'app_iter'
op|'='
name|'self'
op|'.'
name|'print_generator'
op|'('
name|'resp'
op|'.'
name|'app_iter'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|print_generator
name|'def'
name|'print_generator'
op|'('
name|'app_iter'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Iterator that prints the contents of a wrapper string."""'
newline|'\n'
name|'print'
op|'('
op|'('
string|"'*'"
op|'*'
number|'40'
op|')'
op|'+'
string|"' BODY'"
op|')'
newline|'\n'
name|'for'
name|'part'
name|'in'
name|'app_iter'
op|':'
newline|'\n'
indent|'            '
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
name|'part'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'part'
newline|'\n'
dedent|''
name|'print'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI middleware that maps incoming requests to WSGI apps."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a router for the given routes.Mapper.\n\n        Each route in `mapper` must specify a \'controller\', which is a\n        WSGI app to call.  You\'ll probably want to specify an \'action\' as\n        well and have your controller be an object that can route\n        the request to the action-specific method.\n\n        Examples:\n          mapper = routes.Mapper()\n          sc = ServerController()\n\n          # Explicit mapping of one route to a controller+action\n          mapper.connect(None, \'/svrlist\', controller=sc, action=\'list\')\n\n          # Actions are all implicitly defined\n          mapper.resource(\'server\', \'servers\', controller=sc)\n\n          # Pointing to an arbitrary WSGI app.  You can specify the\n          # {path_info:.*} parameter so the target app can be handed just that\n          # section of the URL.\n          mapper.connect(None, \'/v1.0/{path_info:.*}\', controller=BlogApp())\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'='
name|'mapper'
newline|'\n'
name|'self'
op|'.'
name|'_router'
op|'='
name|'routes'
op|'.'
name|'middleware'
op|'.'
name|'RoutesMiddleware'
op|'('
name|'self'
op|'.'
name|'_dispatch'
op|','
nl|'\n'
name|'self'
op|'.'
name|'map'
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
string|'"""Route the incoming request to a controller based on self.map.\n\n        If no match, return a 404.\n\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_router'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'Request'
op|')'
newline|'\n'
DECL|member|_dispatch
name|'def'
name|'_dispatch'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Dispatch the request to the appropriate controller.\n\n        Called by self._router after matching the incoming request to a route\n        and putting the information into req.environ.  Either returns 404\n        or the routed WSGI app\'s response.\n\n        """'
newline|'\n'
name|'match'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'match'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'app'
op|'='
name|'match'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'return'
name|'app'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Loader
dedent|''
dedent|''
name|'class'
name|'Loader'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used to load WSGI applications from paste configurations."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'config_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize the loader, and attempt to find the config.\n\n        :param config_path: Full or relative path to the paste config.\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'config_path'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'config_path'
op|'='
name|'config_path'
name|'or'
name|'CONF'
op|'.'
name|'api_paste_config'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isabs'
op|'('
name|'config_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'config_path'
op|'='
name|'CONF'
op|'.'
name|'find_file'
op|'('
name|'config_path'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'config_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'config_path'
op|'='
name|'config_path'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'config_path'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ConfigNotFound'
op|'('
name|'path'
op|'='
name|'config_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|load_app
dedent|''
dedent|''
name|'def'
name|'load_app'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the paste URLMap wrapped WSGI application.\n\n        :param name: Name of the application to load.\n        :returns: Paste URLMap object wrapping the requested application.\n        :raises: `nova.exception.PasteAppNotFound`\n\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Loading app %(name)s from %(path)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'path'"
op|':'
name|'self'
op|'.'
name|'config_path'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'deploy'
op|'.'
name|'loadapp'
op|'('
string|'"config:%s"'
op|'%'
name|'self'
op|'.'
name|'config_path'
op|','
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'LookupError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'err'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PasteAppNotFound'
op|'('
name|'name'
op|'='
name|'name'
op|','
name|'path'
op|'='
name|'self'
op|'.'
name|'config_path'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
