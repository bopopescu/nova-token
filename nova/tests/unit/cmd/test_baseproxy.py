begin_unit
comment|'# Copyright 2015 IBM Corp.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_reports'
name|'import'
name|'guru_meditation_report'
name|'as'
name|'gmr'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cmd'
name|'import'
name|'baseproxy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'console'
name|'import'
name|'websocketproxy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'config'
op|','
string|"'parse_args'"
op|','
name|'new'
op|'='
name|'lambda'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|':'
name|'None'
op|')'
newline|'\n'
DECL|class|BaseProxyTestCase
name|'class'
name|'BaseProxyTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.path.exists'"
op|','
name|'return_value'
op|'='
name|'False'
op|')'
newline|'\n'
comment|'# NOTE(mriedem): sys.exit raises TestingException so we can actually exit'
nl|'\n'
comment|'# the test normally.'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'sys.exit'"
op|','
name|'side_effect'
op|'='
name|'test'
op|'.'
name|'TestingException'
op|')'
newline|'\n'
DECL|member|test_proxy_ssl_without_cert
name|'def'
name|'test_proxy_ssl_without_cert'
op|'('
name|'self'
op|','
name|'mock_exit'
op|','
name|'mock_exists'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ssl_only'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
name|'baseproxy'
op|'.'
name|'proxy'
op|','
nl|'\n'
string|"'0.0.0.0'"
op|','
string|"'6080'"
op|')'
newline|'\n'
name|'mock_exit'
op|'.'
name|'assert_called_once_with'
op|'('
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.path.exists'"
op|','
name|'return_value'
op|'='
name|'False'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'sys.exit'"
op|','
name|'side_effect'
op|'='
name|'test'
op|'.'
name|'TestingException'
op|')'
newline|'\n'
DECL|member|test_proxy_web_dir_does_not_exist
name|'def'
name|'test_proxy_web_dir_does_not_exist'
op|'('
name|'self'
op|','
name|'mock_exit'
op|','
name|'mock_exists'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'web'
op|'='
string|"'/my/fake/webserver/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
name|'baseproxy'
op|'.'
name|'proxy'
op|','
nl|'\n'
string|"'0.0.0.0'"
op|','
string|"'6080'"
op|')'
newline|'\n'
name|'mock_exit'
op|'.'
name|'assert_called_once_with'
op|'('
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.path.exists'"
op|','
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'logging'
op|','
string|"'setup'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'gmr'
op|'.'
name|'TextGuruMeditation'
op|','
string|"'setup_autorun'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.console.websocketproxy.NovaWebSocketProxy.__init__'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'None'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.console.websocketproxy.NovaWebSocketProxy.start_server'"
op|')'
newline|'\n'
DECL|member|test_proxy
name|'def'
name|'test_proxy'
op|'('
name|'self'
op|','
name|'mock_start'
op|','
name|'mock_init'
op|','
name|'mock_gmr'
op|','
name|'mock_log'
op|','
nl|'\n'
name|'mock_exists'
op|')'
op|':'
newline|'\n'
comment|'# Force verbose=False so something else testing nova.cmd.baseproxy'
nl|'\n'
comment|"# doesn't impact the call to mocked NovaWebSocketProxy.__init__."
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'False'
op|')'
newline|'\n'
name|'baseproxy'
op|'.'
name|'proxy'
op|'('
string|"'0.0.0.0'"
op|','
string|"'6080'"
op|')'
newline|'\n'
name|'mock_log'
op|'.'
name|'assert_called_once_with'
op|'('
name|'baseproxy'
op|'.'
name|'CONF'
op|','
string|"'nova'"
op|')'
newline|'\n'
name|'mock_gmr'
op|'.'
name|'mock_assert_called_once_with'
op|'('
name|'version'
op|')'
newline|'\n'
name|'mock_init'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'listen_host'
op|'='
string|"'0.0.0.0'"
op|','
name|'listen_port'
op|'='
string|"'6080'"
op|','
name|'source_is_ipv6'
op|'='
name|'False'
op|','
nl|'\n'
name|'verbose'
op|'='
name|'False'
op|','
name|'cert'
op|'='
string|"'self.pem'"
op|','
name|'key'
op|'='
name|'None'
op|','
name|'ssl_only'
op|'='
name|'False'
op|','
nl|'\n'
name|'daemon'
op|'='
name|'False'
op|','
name|'record'
op|'='
name|'False'
op|','
name|'traffic'
op|'='
name|'False'
op|','
nl|'\n'
name|'web'
op|'='
string|"'/usr/share/spice-html5'"
op|','
name|'file_only'
op|'='
name|'True'
op|','
nl|'\n'
name|'RequestHandlerClass'
op|'='
name|'websocketproxy'
op|'.'
name|'NovaProxyRequestHandler'
op|')'
newline|'\n'
name|'mock_start'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
