begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nTests for Crypto module.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|X509Test
name|'class'
name|'X509Test'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_can_generate_x509
indent|'    '
name|'def'
name|'test_can_generate_x509'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tmpdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ca_path'
op|'='
name|'tmpdir'
op|')'
newline|'\n'
name|'crypto'
op|'.'
name|'ensure_ca_filesystem'
op|'('
op|')'
newline|'\n'
name|'_key'
op|','
name|'cert_str'
op|'='
name|'crypto'
op|'.'
name|'generate_x509_cert'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
name|'project_cert'
op|'='
name|'crypto'
op|'.'
name|'fetch_ca'
op|'('
name|'project_id'
op|'='
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
name|'signed_cert_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|'"signed"'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'signed_cert_file'
op|','
string|"'w'"
op|')'
name|'as'
name|'keyfile'
op|':'
newline|'\n'
indent|'                '
name|'keyfile'
op|'.'
name|'write'
op|'('
name|'cert_str'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'project_cert_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|'"project"'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'project_cert_file'
op|','
string|"'w'"
op|')'
name|'as'
name|'keyfile'
op|':'
newline|'\n'
indent|'                '
name|'keyfile'
op|'.'
name|'write'
op|'('
name|'project_cert'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'enc'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'verify'"
op|','
string|"'-CAfile'"
op|','
nl|'\n'
name|'project_cert_file'
op|','
string|"'-verbose'"
op|','
name|'signed_cert_file'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'err'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_encrypt_decrypt_x509
dedent|''
dedent|''
name|'def'
name|'test_encrypt_decrypt_x509'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tmpdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ca_path'
op|'='
name|'tmpdir'
op|')'
newline|'\n'
name|'project_id'
op|'='
string|'"fake"'
newline|'\n'
name|'crypto'
op|'.'
name|'ensure_ca_filesystem'
op|'('
op|')'
newline|'\n'
name|'cert'
op|'='
name|'crypto'
op|'.'
name|'fetch_ca'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'public_key'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|'"public.pem"'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'public_key'
op|','
string|"'w'"
op|')'
name|'as'
name|'keyfile'
op|':'
newline|'\n'
indent|'                '
name|'keyfile'
op|'.'
name|'write'
op|'('
name|'cert'
op|')'
newline|'\n'
dedent|''
name|'text'
op|'='
string|'"some @#!%^* test text"'
newline|'\n'
name|'enc'
op|','
name|'_err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
nl|'\n'
string|"'rsautl'"
op|','
nl|'\n'
string|"'-certin'"
op|','
nl|'\n'
string|"'-encrypt'"
op|','
nl|'\n'
string|"'-inkey'"
op|','
string|"'%s'"
op|'%'
name|'public_key'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'text'
op|')'
newline|'\n'
name|'dec'
op|'='
name|'crypto'
op|'.'
name|'decrypt_text'
op|'('
name|'project_id'
op|','
name|'enc'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'text'
op|','
name|'dec'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RevokeCertsTest
dedent|''
dedent|''
dedent|''
name|'class'
name|'RevokeCertsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_revoke_certs_by_user_and_project
indent|'    '
name|'def'
name|'test_revoke_certs_by_user_and_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'user_id'
op|'='
string|"'test_user'"
newline|'\n'
name|'project_id'
op|'='
number|'2'
newline|'\n'
name|'file_name'
op|'='
string|"'test_file'"
newline|'\n'
nl|'\n'
DECL|function|mock_certificate_get_all_by_user_and_project
name|'def'
name|'mock_certificate_get_all_by_user_and_project'
op|'('
name|'context'
op|','
nl|'\n'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'return'
op|'['
op|'{'
string|'"user_id"'
op|':'
name|'user_id'
op|','
string|'"project_id"'
op|':'
name|'project_id'
op|','
nl|'\n'
string|'"file_name"'
op|':'
name|'file_name'
op|'}'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'certificate_get_all_by_user_and_project'"
op|','
nl|'\n'
name|'mock_certificate_get_all_by_user_and_project'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'crypto'
op|','
string|"'revoke_cert'"
op|')'
newline|'\n'
name|'crypto'
op|'.'
name|'revoke_cert'
op|'('
name|'project_id'
op|','
name|'file_name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'crypto'
op|'.'
name|'revoke_certs_by_user_and_project'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_revoke_certs_by_user
dedent|''
name|'def'
name|'test_revoke_certs_by_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'user_id'
op|'='
string|"'test_user'"
newline|'\n'
name|'project_id'
op|'='
number|'2'
newline|'\n'
name|'file_name'
op|'='
string|"'test_file'"
newline|'\n'
nl|'\n'
DECL|function|mock_certificate_get_all_by_user
name|'def'
name|'mock_certificate_get_all_by_user'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'return'
op|'['
op|'{'
string|'"user_id"'
op|':'
name|'user_id'
op|','
string|'"project_id"'
op|':'
name|'project_id'
op|','
nl|'\n'
string|'"file_name"'
op|':'
name|'file_name'
op|'}'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'certificate_get_all_by_user'"
op|','
nl|'\n'
name|'mock_certificate_get_all_by_user'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'crypto'
op|','
string|"'revoke_cert'"
op|')'
newline|'\n'
name|'crypto'
op|'.'
name|'revoke_cert'
op|'('
name|'project_id'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'crypto'
op|'.'
name|'revoke_certs_by_user'
op|'('
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_revoke_certs_by_project
dedent|''
name|'def'
name|'test_revoke_certs_by_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'user_id'
op|'='
string|"'test_user'"
newline|'\n'
name|'project_id'
op|'='
number|'2'
newline|'\n'
name|'file_name'
op|'='
string|"'test_file'"
newline|'\n'
nl|'\n'
DECL|function|mock_certificate_get_all_by_project
name|'def'
name|'mock_certificate_get_all_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'return'
op|'['
op|'{'
string|'"user_id"'
op|':'
name|'user_id'
op|','
string|'"project_id"'
op|':'
name|'project_id'
op|','
nl|'\n'
string|'"file_name"'
op|':'
name|'file_name'
op|'}'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'certificate_get_all_by_project'"
op|','
nl|'\n'
name|'mock_certificate_get_all_by_project'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'crypto'
op|','
string|"'revoke_cert'"
op|')'
newline|'\n'
name|'crypto'
op|'.'
name|'revoke_cert'
op|'('
name|'project_id'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'crypto'
op|'.'
name|'revoke_certs_by_project'
op|'('
name|'project_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
