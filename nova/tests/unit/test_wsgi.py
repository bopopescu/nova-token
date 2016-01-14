begin_unit
comment|'# Copyright 2011 United States Government as represented by the'
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
string|'"""Unit tests for `nova.wsgi`."""'
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
name|'tempfile'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'requests'
newline|'\n'
name|'import'
name|'testtools'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'wsgi'
newline|'\n'
nl|'\n'
DECL|variable|SSL_CERT_DIR
name|'SSL_CERT_DIR'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
op|','
nl|'\n'
string|"'ssl_cert'"
op|')'
op|')'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLoaderNothingExists
name|'class'
name|'TestLoaderNothingExists'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Loader tests where os.path.exists always returns False."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestLoaderNothingExists'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'os.path.exists'"
op|','
name|'lambda'
name|'_'
op|':'
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_relpath_config_not_found
dedent|''
name|'def'
name|'test_relpath_config_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'api_paste_config'
op|'='
string|"'api-paste.ini'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'ConfigNotFound'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Loader'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_asbpath_config_not_found
dedent|''
name|'def'
name|'test_asbpath_config_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'api_paste_config'
op|'='
string|"'/etc/nova/api-paste.ini'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'ConfigNotFound'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Loader'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLoaderNormalFilesystem
dedent|''
dedent|''
name|'class'
name|'TestLoaderNormalFilesystem'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Loader tests with normal filesystem (unmodified os.path module)."""'
newline|'\n'
nl|'\n'
name|'_paste_config'
op|'='
string|'"""\n[app:test_app]\nuse = egg:Paste#static\ndocument_root = /tmp\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestLoaderNormalFilesystem'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
name|'mode'
op|'='
string|'"w+t"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'_paste_config'
op|'.'
name|'lstrip'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loader'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Loader'
op|'('
name|'self'
op|'.'
name|'config'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_found
dedent|''
name|'def'
name|'test_config_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'config'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'loader'
op|'.'
name|'config_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_app_not_found
dedent|''
name|'def'
name|'test_app_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'PasteAppNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'loader'
op|'.'
name|'load_app'
op|','
nl|'\n'
string|'"nonexistent app"'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_app_found
dedent|''
name|'def'
name|'test_app_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url_parser'
op|'='
name|'self'
op|'.'
name|'loader'
op|'.'
name|'load_app'
op|'('
string|'"test_app"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/tmp"'
op|','
name|'url_parser'
op|'.'
name|'directory'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'config'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'TestLoaderNormalFilesystem'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestWSGIServer
dedent|''
dedent|''
name|'class'
name|'TestWSGIServer'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI server tests."""'
newline|'\n'
nl|'\n'
DECL|member|test_no_app
name|'def'
name|'test_no_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_app"'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"test_app"'
op|','
name|'server'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_custom_max_header_line
dedent|''
name|'def'
name|'test_custom_max_header_line'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'max_header_line'
op|'='
number|'4096'
op|')'
comment|'# Default value is 16384.'
newline|'\n'
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_custom_max_header_line"'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'max_header_line'
op|','
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'MAX_HEADER_LINE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_random_port
dedent|''
name|'def'
name|'test_start_random_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_random_port"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'server'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'testtools'
op|'.'
name|'skipIf'
op|'('
name|'not'
name|'utils'
op|'.'
name|'is_ipv6_supported'
op|'('
op|')'
op|','
string|'"no ipv6 support"'
op|')'
newline|'\n'
DECL|member|test_start_random_port_with_ipv6
name|'def'
name|'test_start_random_port_with_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_random_port"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"::1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"::1"'
op|','
name|'server'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'server'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'testtools'
op|'.'
name|'skipIf'
op|'('
name|'not'
name|'utils'
op|'.'
name|'is_linux'
op|'('
op|')'
op|','
string|"'SO_REUSEADDR behaves differently '"
nl|'\n'
string|"'on OSX and BSD, see bugs '"
nl|'\n'
string|"'1436895 and 1467145'"
op|')'
newline|'\n'
DECL|member|test_socket_options_for_simple_server
name|'def'
name|'test_socket_options_for_simple_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# test normal socket options has set properly'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'tcp_keepidle'
op|'='
number|'500'
op|')'
newline|'\n'
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_socket_options"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'sock'
op|'='
name|'server'
op|'.'
name|'_socket'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'sock'
op|'.'
name|'getsockopt'
op|'('
name|'socket'
op|'.'
name|'SOL_SOCKET'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'SO_REUSEADDR'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'sock'
op|'.'
name|'getsockopt'
op|'('
name|'socket'
op|'.'
name|'SOL_SOCKET'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'SO_KEEPALIVE'
op|')'
op|')'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'socket'
op|','
string|"'TCP_KEEPIDLE'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'tcp_keepidle'
op|','
nl|'\n'
name|'sock'
op|'.'
name|'getsockopt'
op|'('
name|'socket'
op|'.'
name|'IPPROTO_TCP'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'TCP_KEEPIDLE'
op|')'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_pool_waitall
dedent|''
name|'def'
name|'test_server_pool_waitall'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# test pools waitall method gets called while stopping server'
nl|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_server"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'server'
op|'.'
name|'_pool'
op|','
nl|'\n'
string|"'waitall'"
op|')'
name|'as'
name|'mock_waitall'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'mock_waitall'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_uri_length_limit
dedent|''
dedent|''
name|'def'
name|'test_uri_length_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_uri_length_limit"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'max_url_len'
op|'='
number|'16384'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'uri'
op|'='
string|'"http://127.0.0.1:%d/%s"'
op|'%'
op|'('
name|'server'
op|'.'
name|'port'
op|','
number|'10000'
op|'*'
string|"'x'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'requests'
op|'.'
name|'get'
op|'('
name|'uri'
op|','
name|'proxies'
op|'='
op|'{'
string|'"http"'
op|':'
string|'""'
op|'}'
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'resp'
op|'.'
name|'status_code'
op|','
nl|'\n'
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'REQUEST_URI_TOO_LARGE'
op|')'
newline|'\n'
nl|'\n'
name|'uri'
op|'='
string|'"http://127.0.0.1:%d/%s"'
op|'%'
op|'('
name|'server'
op|'.'
name|'port'
op|','
number|'20000'
op|'*'
string|"'x'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'requests'
op|'.'
name|'get'
op|'('
name|'uri'
op|','
name|'proxies'
op|'='
op|'{'
string|'"http"'
op|':'
string|'""'
op|'}'
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_code'
op|','
nl|'\n'
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'REQUEST_URI_TOO_LARGE'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_pool_size_to_default
dedent|''
name|'def'
name|'test_reset_pool_size_to_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_resize"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'max_url_len'
op|'='
number|'16384'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Stopping the server, which in turn sets pool size to 0'
nl|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'server'
op|'.'
name|'_pool'
op|'.'
name|'size'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|'# Resetting pool size to default'
nl|'\n'
name|'server'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'server'
op|'.'
name|'_pool'
op|'.'
name|'size'
op|','
name|'CONF'
op|'.'
name|'wsgi_default_pool_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_client_socket_timeout
dedent|''
name|'def'
name|'test_client_socket_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'client_socket_timeout'
op|'='
number|'5'
op|')'
newline|'\n'
nl|'\n'
comment|'# mocking eventlet spawn method to check it is called with'
nl|'\n'
comment|"# configured 'client_socket_timeout' value."
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventlet'
op|','
nl|'\n'
string|"'spawn'"
op|')'
name|'as'
name|'mock_spawn'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_app"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'_'
op|','
name|'kwargs'
op|'='
name|'mock_spawn'
op|'.'
name|'call_args'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'client_socket_timeout'
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'socket_timeout'"
op|']'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wsgi_keep_alive
dedent|''
dedent|''
name|'def'
name|'test_wsgi_keep_alive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'wsgi_keep_alive'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# mocking eventlet spawn method to check it is called with'
nl|'\n'
comment|"# configured 'wsgi_keep_alive' value."
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventlet'
op|','
nl|'\n'
string|"'spawn'"
op|')'
name|'as'
name|'mock_spawn'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_app"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'_'
op|','
name|'kwargs'
op|'='
name|'mock_spawn'
op|'.'
name|'call_args'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'wsgi_keep_alive'
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'keepalive'"
op|']'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestWSGIServerWithSSL
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestWSGIServerWithSSL'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI server with SSL tests."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestWSGIServerWithSSL'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enabled_ssl_apis'
op|'='
op|'['
string|"'fake_ssl'"
op|']'
op|','
nl|'\n'
name|'ssl_cert_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'SSL_CERT_DIR'
op|','
string|"'certificate.crt'"
op|')'
op|','
nl|'\n'
name|'ssl_key_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'SSL_CERT_DIR'
op|','
string|"'privatekey.key'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ssl_server
dedent|''
name|'def'
name|'test_ssl_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|test_app
indent|'        '
name|'def'
name|'test_app'
op|'('
name|'env'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'start_response'
op|'('
string|"'200 OK'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
op|'['
string|"'PONG'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'fake_ssl_server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"fake_ssl"'
op|','
name|'test_app'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|','
nl|'\n'
name|'use_ssl'
op|'='
name|'True'
op|')'
newline|'\n'
name|'fake_ssl_server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'fake_ssl_server'
op|'.'
name|'port'
op|')'
newline|'\n'
nl|'\n'
name|'cli'
op|'='
name|'eventlet'
op|'.'
name|'connect'
op|'('
op|'('
string|'"localhost"'
op|','
name|'fake_ssl_server'
op|'.'
name|'port'
op|')'
op|')'
newline|'\n'
name|'cli'
op|'='
name|'eventlet'
op|'.'
name|'wrap_ssl'
op|'('
name|'cli'
op|','
nl|'\n'
name|'ca_certs'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'SSL_CERT_DIR'
op|','
string|"'ca.crt'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'cli'
op|'.'
name|'write'
op|'('
string|"'POST / HTTP/1.1\\r\\nHost: localhost\\r\\n'"
nl|'\n'
string|"'Connection: close\\r\\nContent-length:4\\r\\n\\r\\nPING'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'cli'
op|'.'
name|'read'
op|'('
number|'8192'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'['
op|'-'
number|'4'
op|':'
op|']'
op|','
string|'"PONG"'
op|')'
newline|'\n'
nl|'\n'
name|'fake_ssl_server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'fake_ssl_server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_two_servers
dedent|''
name|'def'
name|'test_two_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|test_app
indent|'        '
name|'def'
name|'test_app'
op|'('
name|'env'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'start_response'
op|'('
string|"'200 OK'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
op|'['
string|"'PONG'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'fake_ssl_server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"fake_ssl"'
op|','
name|'test_app'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|','
name|'use_ssl'
op|'='
name|'True'
op|')'
newline|'\n'
name|'fake_ssl_server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'fake_ssl_server'
op|'.'
name|'port'
op|')'
newline|'\n'
nl|'\n'
name|'fake_server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"fake"'
op|','
name|'test_app'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'fake_server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'fake_server'
op|'.'
name|'port'
op|')'
newline|'\n'
nl|'\n'
name|'cli'
op|'='
name|'eventlet'
op|'.'
name|'connect'
op|'('
op|'('
string|'"localhost"'
op|','
name|'fake_ssl_server'
op|'.'
name|'port'
op|')'
op|')'
newline|'\n'
name|'cli'
op|'='
name|'eventlet'
op|'.'
name|'wrap_ssl'
op|'('
name|'cli'
op|','
nl|'\n'
name|'ca_certs'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'SSL_CERT_DIR'
op|','
string|"'ca.crt'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'cli'
op|'.'
name|'write'
op|'('
string|"'POST / HTTP/1.1\\r\\nHost: localhost\\r\\n'"
nl|'\n'
string|"'Connection: close\\r\\nContent-length:4\\r\\n\\r\\nPING'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'cli'
op|'.'
name|'read'
op|'('
number|'8192'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'['
op|'-'
number|'4'
op|':'
op|']'
op|','
string|'"PONG"'
op|')'
newline|'\n'
nl|'\n'
name|'cli'
op|'='
name|'eventlet'
op|'.'
name|'connect'
op|'('
op|'('
string|'"localhost"'
op|','
name|'fake_server'
op|'.'
name|'port'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'cli'
op|'.'
name|'sendall'
op|'('
string|"'POST / HTTP/1.1\\r\\nHost: localhost\\r\\n'"
nl|'\n'
string|"'Connection: close\\r\\nContent-length:4\\r\\n\\r\\nPING'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'cli'
op|'.'
name|'recv'
op|'('
number|'8192'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'['
op|'-'
number|'4'
op|':'
op|']'
op|','
string|'"PONG"'
op|')'
newline|'\n'
nl|'\n'
name|'fake_ssl_server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'fake_ssl_server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'testtools'
op|'.'
name|'skipIf'
op|'('
name|'not'
name|'utils'
op|'.'
name|'is_linux'
op|'('
op|')'
op|','
string|"'SO_REUSEADDR behaves differently '"
nl|'\n'
string|"'on OSX and BSD, see bugs '"
nl|'\n'
string|"'1436895 and 1467145'"
op|')'
newline|'\n'
DECL|member|test_socket_options_for_ssl_server
name|'def'
name|'test_socket_options_for_ssl_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# test normal socket options has set properly'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'tcp_keepidle'
op|'='
number|'500'
op|')'
newline|'\n'
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_socket_options"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|','
nl|'\n'
name|'use_ssl'
op|'='
name|'True'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'sock'
op|'='
name|'server'
op|'.'
name|'_socket'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'sock'
op|'.'
name|'getsockopt'
op|'('
name|'socket'
op|'.'
name|'SOL_SOCKET'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'SO_REUSEADDR'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'sock'
op|'.'
name|'getsockopt'
op|'('
name|'socket'
op|'.'
name|'SOL_SOCKET'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'SO_KEEPALIVE'
op|')'
op|')'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'socket'
op|','
string|"'TCP_KEEPIDLE'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'tcp_keepidle'
op|','
nl|'\n'
name|'sock'
op|'.'
name|'getsockopt'
op|'('
name|'socket'
op|'.'
name|'IPPROTO_TCP'
op|','
nl|'\n'
name|'socket'
op|'.'
name|'TCP_KEEPIDLE'
op|')'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'testtools'
op|'.'
name|'skipIf'
op|'('
name|'not'
name|'utils'
op|'.'
name|'is_ipv6_supported'
op|'('
op|')'
op|','
string|'"no ipv6 support"'
op|')'
newline|'\n'
DECL|member|test_app_using_ipv6_and_ssl
name|'def'
name|'test_app_using_ipv6_and_ssl'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'greetings'
op|'='
string|"'Hello, World!!!'"
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|hello_world
name|'def'
name|'hello_world'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'greetings'
newline|'\n'
nl|'\n'
dedent|''
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"fake_ssl"'
op|','
nl|'\n'
name|'hello_world'
op|','
nl|'\n'
name|'host'
op|'='
string|'"::1"'
op|','
nl|'\n'
name|'port'
op|'='
number|'0'
op|','
nl|'\n'
name|'use_ssl'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'requests'
op|'.'
name|'get'
op|'('
string|"'https://[::1]:%d/'"
op|'%'
name|'server'
op|'.'
name|'port'
op|','
nl|'\n'
name|'verify'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'SSL_CERT_DIR'
op|','
string|"'ca.crt'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'greetings'
op|','
name|'response'
op|'.'
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
