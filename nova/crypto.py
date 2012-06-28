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
string|'"""Wrappers around standard crypto data elements.\n\nIncludes root and intermediate CAs, SSH key_pairs and x509 certificates.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'absolute_import'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
nl|'\n'
name|'import'
name|'Crypto'
op|'.'
name|'Cipher'
op|'.'
name|'AES'
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
name|'db'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|crypto_opts
name|'crypto_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ca_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cacert.pem'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Filename of root CA'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'key_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'private'"
op|','
string|"'cakey.pem'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Filename of private key'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'crl_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'crl.pem'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Filename of root Certificate Revocation List'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'keys_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$state_path/keys'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Where we keep our keys'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ca_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$state_path/CA'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Where we keep our root CA'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_project_ca'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Should we use a CA for each project?'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'user_cert_subject'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'/C=US/ST=California/O=OpenStack/'"
nl|'\n'
string|"'OU=NovaDev/CN=%.16s-%.16s-%s'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Subject for certificate for users, %s for '"
nl|'\n'
string|"'project, user, timestamp'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'project_cert_subject'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'/C=US/ST=California/O=OpenStack/'"
nl|'\n'
string|"'OU=NovaDev/CN=project-ca-%.16s-%s'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Subject for certificate for projects, %s for '"
nl|'\n'
string|"'project, timestamp'"
op|')'
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
name|'register_opts'
op|'('
name|'crypto_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ca_folder
name|'def'
name|'ca_folder'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'use_project_ca'
name|'and'
name|'project_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'ca_path'
op|','
string|"'projects'"
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'FLAGS'
op|'.'
name|'ca_path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ca_path
dedent|''
name|'def'
name|'ca_path'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
name|'FLAGS'
op|'.'
name|'ca_file'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|key_path
dedent|''
name|'def'
name|'key_path'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
name|'FLAGS'
op|'.'
name|'key_file'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|crl_path
dedent|''
name|'def'
name|'crl_path'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
name|'FLAGS'
op|'.'
name|'crl_file'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_ca
dedent|''
name|'def'
name|'fetch_ca'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'use_project_ca'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'ca_path'
op|'('
name|'project_id'
op|')'
op|','
string|"'r'"
op|')'
name|'as'
name|'cafile'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cafile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_ca_filesystem
dedent|''
dedent|''
name|'def'
name|'ensure_ca_filesystem'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure the CA filesystem exists."""'
newline|'\n'
name|'ca_dir'
op|'='
name|'ca_folder'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_path'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'genrootca_sh_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
nl|'\n'
string|"'CA'"
op|','
nl|'\n'
string|"'genrootca.sh'"
op|')'
newline|'\n'
nl|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_dir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'ca_dir'
op|')'
newline|'\n'
dedent|''
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_dir'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|'"sh"'
op|','
name|'genrootca_sh_path'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_generate_fingerprint
dedent|''
dedent|''
name|'def'
name|'_generate_fingerprint'
op|'('
name|'public_key_file'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ssh-keygen'"
op|','
string|"'-q'"
op|','
string|"'-l'"
op|','
string|"'-f'"
op|','
name|'public_key_file'
op|')'
newline|'\n'
name|'fingerprint'
op|'='
name|'out'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'return'
name|'fingerprint'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_fingerprint
dedent|''
name|'def'
name|'generate_fingerprint'
op|'('
name|'public_key'
op|')'
op|':'
newline|'\n'
indent|'    '
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
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pubfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp.pub'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'pubfile'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'f'
op|'.'
name|'write'
op|'('
name|'public_key'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_generate_fingerprint'
op|'('
name|'pubfile'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidKeypair'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_key_pair
dedent|''
dedent|''
dedent|''
name|'def'
name|'generate_key_pair'
op|'('
name|'bits'
op|'='
number|'1024'
op|')'
op|':'
newline|'\n'
comment|'# what is the magic 65537?'
nl|'\n'
nl|'\n'
indent|'    '
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
indent|'        '
name|'keyfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ssh-keygen'"
op|','
string|"'-q'"
op|','
string|"'-b'"
op|','
name|'bits'
op|','
string|"'-N'"
op|','
string|"''"
op|','
nl|'\n'
string|"'-t'"
op|','
string|"'rsa'"
op|','
string|"'-f'"
op|','
name|'keyfile'
op|')'
newline|'\n'
name|'fingerprint'
op|'='
name|'_generate_fingerprint'
op|'('
string|"'%s.pub'"
op|'%'
op|'('
name|'keyfile'
op|')'
op|')'
newline|'\n'
name|'private_key'
op|'='
name|'open'
op|'('
name|'keyfile'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'public_key'
op|'='
name|'open'
op|'('
name|'keyfile'
op|'+'
string|"'.pub'"
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'private_key'
op|','
name|'public_key'
op|','
name|'fingerprint'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_crl
dedent|''
name|'def'
name|'fetch_crl'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get crl file for project."""'
newline|'\n'
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'use_project_ca'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'crl_path'
op|'('
name|'project_id'
op|')'
op|','
string|"'r'"
op|')'
name|'as'
name|'crlfile'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'crlfile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|decrypt_text
dedent|''
dedent|''
name|'def'
name|'decrypt_text'
op|'('
name|'project_id'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'private_key'
op|'='
name|'key_path'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'private_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ProjectNotFound'
op|'('
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'dec'
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
string|"'-decrypt'"
op|','
nl|'\n'
string|"'-inkey'"
op|','
string|"'%s'"
op|'%'
name|'private_key'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'text'
op|')'
newline|'\n'
name|'return'
name|'dec'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DecryptionFailure'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_cert
dedent|''
dedent|''
name|'def'
name|'revoke_cert'
op|'('
name|'project_id'
op|','
name|'file_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke a cert by file name."""'
newline|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
comment|'# NOTE(vish): potential race condition here'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'ca'"
op|','
string|"'-config'"
op|','
string|"'./openssl.cnf'"
op|','
string|"'-revoke'"
op|','
nl|'\n'
name|'file_name'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'ca'"
op|','
string|"'-gencrl'"
op|','
string|"'-config'"
op|','
string|"'./openssl.cnf'"
op|','
nl|'\n'
string|"'-out'"
op|','
name|'FLAGS'
op|'.'
name|'crl_file'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_certs_by_user
dedent|''
name|'def'
name|'revoke_certs_by_user'
op|'('
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke all user certs."""'
newline|'\n'
name|'admin'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'cert'
name|'in'
name|'db'
op|'.'
name|'certificate_get_all_by_user'
op|'('
name|'admin'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'revoke_cert'
op|'('
name|'cert'
op|'['
string|"'project_id'"
op|']'
op|','
name|'cert'
op|'['
string|"'file_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_certs_by_project
dedent|''
dedent|''
name|'def'
name|'revoke_certs_by_project'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke all project certs."""'
newline|'\n'
comment|'# NOTE(vish): This is somewhat useless because we can just shut down'
nl|'\n'
comment|'#             the vpn.'
nl|'\n'
name|'admin'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'cert'
name|'in'
name|'db'
op|'.'
name|'certificate_get_all_by_project'
op|'('
name|'admin'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'revoke_cert'
op|'('
name|'cert'
op|'['
string|"'project_id'"
op|']'
op|','
name|'cert'
op|'['
string|"'file_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_certs_by_user_and_project
dedent|''
dedent|''
name|'def'
name|'revoke_certs_by_user_and_project'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke certs for user in project."""'
newline|'\n'
name|'admin'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'cert'
name|'in'
name|'db'
op|'.'
name|'certificate_get_all_by_user_and_project'
op|'('
name|'admin'
op|','
nl|'\n'
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'revoke_cert'
op|'('
name|'cert'
op|'['
string|"'project_id'"
op|']'
op|','
name|'cert'
op|'['
string|"'file_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_project_cert_subject
dedent|''
dedent|''
name|'def'
name|'_project_cert_subject'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper to generate user cert subject."""'
newline|'\n'
name|'return'
name|'FLAGS'
op|'.'
name|'project_cert_subject'
op|'%'
op|'('
name|'project_id'
op|','
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_user_cert_subject
dedent|''
name|'def'
name|'_user_cert_subject'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper to generate user cert subject."""'
newline|'\n'
name|'return'
name|'FLAGS'
op|'.'
name|'user_cert_subject'
op|'%'
op|'('
name|'project_id'
op|','
name|'user_id'
op|','
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_x509_cert
dedent|''
name|'def'
name|'generate_x509_cert'
op|'('
name|'user_id'
op|','
name|'project_id'
op|','
name|'bits'
op|'='
number|'1024'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate and sign a cert for user in project."""'
newline|'\n'
name|'subject'
op|'='
name|'_user_cert_subject'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
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
indent|'        '
name|'keyfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp.key'"
op|')'
op|')'
newline|'\n'
name|'csrfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp.csr'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'genrsa'"
op|','
string|"'-out'"
op|','
name|'keyfile'
op|','
name|'str'
op|'('
name|'bits'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'req'"
op|','
string|"'-new'"
op|','
string|"'-key'"
op|','
name|'keyfile'
op|','
string|"'-out'"
op|','
nl|'\n'
name|'csrfile'
op|','
string|"'-batch'"
op|','
string|"'-subj'"
op|','
name|'subject'
op|')'
newline|'\n'
name|'private_key'
op|'='
name|'open'
op|'('
name|'keyfile'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'csr'
op|'='
name|'open'
op|'('
name|'csrfile'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'('
name|'serial'
op|','
name|'signed_csr'
op|')'
op|'='
name|'sign_csr'
op|'('
name|'csr'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'fname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
string|"'newcerts/%s.pem'"
op|'%'
name|'serial'
op|')'
newline|'\n'
name|'cert'
op|'='
op|'{'
string|"'user_id'"
op|':'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'project_id'
op|','
nl|'\n'
string|"'file_name'"
op|':'
name|'fname'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'certificate_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'cert'
op|')'
newline|'\n'
name|'return'
op|'('
name|'private_key'
op|','
name|'signed_csr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_ensure_project_folder
dedent|''
name|'def'
name|'_ensure_project_folder'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_path'
op|'('
name|'project_id'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'geninter_sh_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
nl|'\n'
string|"'CA'"
op|','
nl|'\n'
string|"'geninter.sh'"
op|')'
newline|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_folder'
op|'('
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sh'"
op|','
name|'geninter_sh_path'
op|','
name|'project_id'
op|','
nl|'\n'
name|'_project_cert_subject'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_vpn_files
dedent|''
dedent|''
name|'def'
name|'generate_vpn_files'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'project_folder'
op|'='
name|'ca_folder'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'key_fn'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'project_folder'
op|','
string|"'server.key'"
op|')'
newline|'\n'
name|'crt_fn'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'project_folder'
op|','
string|"'server.crt'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'crt_fn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
comment|'# NOTE(vish): The 2048 is to maintain compatibility with the old script.'
nl|'\n'
comment|'#             We are using "project-vpn" as the user_id for the cert'
nl|'\n'
comment|'#             even though that user may not really exist. Ultimately'
nl|'\n'
comment|'#             this will be changed to be launched by a real user.  At'
nl|'\n'
comment|'#             that point we will can delete this helper method.'
nl|'\n'
dedent|''
name|'key'
op|','
name|'csr'
op|'='
name|'generate_x509_cert'
op|'('
string|"'project-vpn'"
op|','
name|'project_id'
op|','
number|'2048'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'key_fn'
op|','
string|"'w'"
op|')'
name|'as'
name|'keyfile'
op|':'
newline|'\n'
indent|'        '
name|'keyfile'
op|'.'
name|'write'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'crt_fn'
op|','
string|"'w'"
op|')'
name|'as'
name|'crtfile'
op|':'
newline|'\n'
indent|'        '
name|'crtfile'
op|'.'
name|'write'
op|'('
name|'csr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|sign_csr
dedent|''
dedent|''
name|'def'
name|'sign_csr'
op|'('
name|'csr_text'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'use_project_ca'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'project_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'ca_folder'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'_ensure_project_folder'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'project_folder'
op|'='
name|'ca_folder'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_sign_csr
dedent|''
name|'def'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'ca_folder'
op|')'
op|':'
newline|'\n'
indent|'    '
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
indent|'        '
name|'inbound'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'inbound.csr'"
op|')'
newline|'\n'
name|'outbound'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'outbound.csr'"
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'open'
op|'('
name|'inbound'
op|','
string|"'w'"
op|')'
name|'as'
name|'csrfile'
op|':'
newline|'\n'
indent|'            '
name|'csrfile'
op|'.'
name|'write'
op|'('
name|'csr_text'
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
string|"'Flags path: %s'"
op|')'
op|','
name|'ca_folder'
op|')'
newline|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Change working dir to CA'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_folder'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'ca_folder'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_folder'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'ca'"
op|','
string|"'-batch'"
op|','
string|"'-out'"
op|','
name|'outbound'
op|','
string|"'-config'"
op|','
nl|'\n'
string|"'./openssl.cnf'"
op|','
string|"'-infiles'"
op|','
name|'inbound'
op|')'
newline|'\n'
name|'out'
op|','
name|'_err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'x509'"
op|','
string|"'-in'"
op|','
name|'outbound'
op|','
nl|'\n'
string|"'-serial'"
op|','
string|"'-noout'"
op|')'
newline|'\n'
name|'serial'
op|'='
name|'string'
op|'.'
name|'strip'
op|'('
name|'out'
op|'.'
name|'rpartition'
op|'('
string|"'='"
op|')'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'open'
op|'('
name|'outbound'
op|','
string|"'r'"
op|')'
name|'as'
name|'crtfile'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'serial'
op|','
name|'crtfile'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_cipher
dedent|''
dedent|''
dedent|''
name|'def'
name|'_build_cipher'
op|'('
name|'key'
op|','
name|'iv'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make a 128bit AES CBC encode/decode Cipher object.\n       Padding is handled internally."""'
newline|'\n'
name|'return'
name|'Crypto'
op|'.'
name|'Cipher'
op|'.'
name|'AES'
op|'.'
name|'new'
op|'('
name|'key'
op|','
name|'IV'
op|'='
name|'iv'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|encryptor
dedent|''
name|'def'
name|'encryptor'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simple symmetric key encryption."""'
newline|'\n'
name|'key'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'key'
op|')'
newline|'\n'
name|'iv'
op|'='
string|"'\\0'"
op|'*'
number|'16'
newline|'\n'
nl|'\n'
DECL|function|encrypt
name|'def'
name|'encrypt'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cipher'
op|'='
name|'_build_cipher'
op|'('
name|'key'
op|','
name|'iv'
op|')'
newline|'\n'
comment|'# Must pad string to multiple of 16 chars'
nl|'\n'
name|'padding'
op|'='
op|'('
number|'16'
op|'-'
name|'len'
op|'('
name|'data'
op|')'
op|'%'
number|'16'
op|')'
op|'*'
string|'" "'
newline|'\n'
name|'v'
op|'='
name|'cipher'
op|'.'
name|'encrypt'
op|'('
name|'data'
op|'+'
name|'padding'
op|')'
newline|'\n'
name|'del'
name|'cipher'
newline|'\n'
name|'v'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'v'
op|')'
newline|'\n'
name|'return'
name|'v'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'encrypt'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|decryptor
dedent|''
name|'def'
name|'decryptor'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simple symmetric key decryption."""'
newline|'\n'
name|'key'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'key'
op|')'
newline|'\n'
name|'iv'
op|'='
string|"'\\0'"
op|'*'
number|'16'
newline|'\n'
nl|'\n'
DECL|function|decrypt
name|'def'
name|'decrypt'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'data'
op|')'
newline|'\n'
name|'cipher'
op|'='
name|'_build_cipher'
op|'('
name|'key'
op|','
name|'iv'
op|')'
newline|'\n'
name|'v'
op|'='
name|'cipher'
op|'.'
name|'decrypt'
op|'('
name|'data'
op|')'
op|'.'
name|'rstrip'
op|'('
op|')'
newline|'\n'
name|'del'
name|'cipher'
newline|'\n'
name|'return'
name|'v'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'decrypt'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission is hereby granted, free of charge, to any person obtaining a'
nl|'\n'
comment|'# copy of this software and associated documentation files (the'
nl|'\n'
comment|'# "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'# without limitation the rights to use, copy, modify, merge, publish, dis-'
nl|'\n'
comment|'# tribute, sublicense, and/or sell copies of the Software, and to permit'
nl|'\n'
comment|'# persons to whom the Software is furnished to do so, subject to the fol-'
nl|'\n'
comment|'# lowing conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The above copyright notice and this permission notice shall be included'
nl|'\n'
comment|'# in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS'
nl|'\n'
comment|'# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-'
nl|'\n'
comment|'# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT'
nl|'\n'
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,'
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
comment|'# http://code.google.com/p/boto'
nl|'\n'
nl|'\n'
DECL|function|compute_md5
dedent|''
name|'def'
name|'compute_md5'
op|'('
name|'fp'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Compute an md5 hash.\n\n    :type fp: file\n    :param fp: File pointer to the file to MD5 hash.  The file pointer will be\n               reset to the beginning of the file before the method returns.\n\n    :rtype: tuple\n    :returns: the hex digest version of the MD5 hash\n\n    """'
newline|'\n'
name|'m'
op|'='
name|'hashlib'
op|'.'
name|'md5'
op|'('
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
name|'s'
op|'='
name|'fp'
op|'.'
name|'read'
op|'('
number|'8192'
op|')'
newline|'\n'
name|'while'
name|'s'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'.'
name|'update'
op|'('
name|'s'
op|')'
newline|'\n'
name|'s'
op|'='
name|'fp'
op|'.'
name|'read'
op|'('
number|'8192'
op|')'
newline|'\n'
dedent|''
name|'hex_md5'
op|'='
name|'m'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
comment|'# size = fp.tell()'
nl|'\n'
name|'fp'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
name|'return'
name|'hex_md5'
newline|'\n'
dedent|''
endmarker|''
end_unit
