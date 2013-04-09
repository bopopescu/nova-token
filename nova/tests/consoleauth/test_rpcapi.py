begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
string|'"""\nUnit Tests for nova.consoleauth.rpcapi\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'consoleauth'
name|'import'
name|'rpcapi'
name|'as'
name|'consoleauth_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAuthRpcAPITestCase
name|'class'
name|'ConsoleAuthRpcAPITestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_test_consoleauth_api
indent|'    '
name|'def'
name|'_test_consoleauth_api'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'do_cast'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'_do_cast'"
op|','
name|'False'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
name|'rpcapi'
op|'='
name|'consoleauth_rpcapi'
op|'.'
name|'ConsoleAuthAPI'
op|'('
op|')'
newline|'\n'
name|'expected_retval'
op|'='
string|"'foo'"
newline|'\n'
name|'expected_version'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'rpcapi'
op|'.'
name|'BASE_RPC_API_VERSION'
op|')'
newline|'\n'
name|'expected_msg'
op|'='
name|'rpcapi'
op|'.'
name|'make_msg'
op|'('
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'expected_msg'
op|'['
string|"'version'"
op|']'
op|'='
name|'expected_version'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'call_ctxt'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'call_topic'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'call_msg'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'call_timeout'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|_fake_call
name|'def'
name|'_fake_call'
op|'('
name|'_ctxt'
op|','
name|'_topic'
op|','
name|'_msg'
op|','
name|'_timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'call_ctxt'
op|'='
name|'_ctxt'
newline|'\n'
name|'self'
op|'.'
name|'call_topic'
op|'='
name|'_topic'
newline|'\n'
name|'self'
op|'.'
name|'call_msg'
op|'='
name|'_msg'
newline|'\n'
name|'self'
op|'.'
name|'call_timeout'
op|'='
name|'_timeout'
newline|'\n'
name|'return'
name|'expected_retval'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'do_cast'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'_fake_call'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'call'"
op|','
name|'_fake_call'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'retval'
op|'='
name|'getattr'
op|'('
name|'rpcapi'
op|','
name|'method'
op|')'
op|'('
name|'ctxt'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'do_cast'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'retval'
op|','
name|'expected_retval'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'call_ctxt'
op|','
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'call_topic'
op|','
name|'CONF'
op|'.'
name|'consoleauth_topic'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'call_msg'
op|','
name|'expected_msg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'call_timeout'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_console
dedent|''
name|'def'
name|'test_authorize_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_consoleauth_api'
op|'('
string|"'authorize_console'"
op|','
name|'token'
op|'='
string|"'token'"
op|','
nl|'\n'
name|'console_type'
op|'='
string|"'ctype'"
op|','
name|'host'
op|'='
string|"'h'"
op|','
name|'port'
op|'='
string|"'p'"
op|','
nl|'\n'
name|'internal_access_path'
op|'='
string|"'iap'"
op|','
name|'instance_uuid'
op|'='
string|'"instance"'
op|','
nl|'\n'
name|'version'
op|'='
string|'"1.2"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_token
dedent|''
name|'def'
name|'test_check_token'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_consoleauth_api'
op|'('
string|"'check_token'"
op|','
name|'token'
op|'='
string|"'t'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_tokens_for_instnace
dedent|''
name|'def'
name|'test_delete_tokens_for_instnace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_consoleauth_api'
op|'('
string|"'delete_tokens_for_instance'"
op|','
nl|'\n'
name|'_do_cast'
op|'='
name|'True'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|'"instance"'
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
