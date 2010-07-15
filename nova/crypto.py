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
comment|'# Copyright 2010 Anso Labs, LLC'
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
string|'"""\nWrappers around standard crypto, including root and intermediate CAs,\nSSH keypairs and x509 certificates.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'import'
name|'M2Crypto'
newline|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ca_file'"
op|','
string|"'cacert.pem'"
op|','
string|"'Filename of root CA'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'keys_path'"
op|','
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'../keys'"
op|')'
op|','
string|"'Where we keep our keys'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ca_path'"
op|','
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'../CA'"
op|')'
op|','
string|"'Where we keep our root CA'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
string|"'use_intermediate_ca'"
op|','
name|'False'
op|','
string|"'Should we use intermediate CAs for each project?'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|ca_path
name|'def'
name|'ca_path'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'project_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s/INTER/%s/cacert.pem"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'ca_path'
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"%s/cacert.pem"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'ca_path'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fetch_ca
dedent|''
name|'def'
name|'fetch_ca'
op|'('
name|'project_id'
op|'='
name|'None'
op|','
name|'chain'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'use_intermediate_ca'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'buffer'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'project_id'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'ca_path'
op|'('
name|'project_id'
op|')'
op|','
string|'"r"'
op|')'
name|'as'
name|'cafile'
op|':'
newline|'\n'
indent|'            '
name|'buffer'
op|'+='
name|'cafile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'chain'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'buffer'
newline|'\n'
dedent|''
dedent|''
name|'with'
name|'open'
op|'('
name|'ca_path'
op|'('
name|'None'
op|')'
op|','
string|'"r"'
op|')'
name|'as'
name|'cafile'
op|':'
newline|'\n'
indent|'        '
name|'buffer'
op|'+='
name|'cafile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'buffer'
newline|'\n'
nl|'\n'
DECL|function|generate_key_pair
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
name|'tmpdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
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
string|'\'ssh-keygen -q -b %d -N "" -f %s\''
op|'%'
op|'('
name|'bits'
op|','
name|'keyfile'
op|')'
op|')'
newline|'\n'
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
string|"'ssh-keygen -q -l -f %s.pub'"
op|'%'
op|'('
name|'keyfile'
op|')'
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
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'tmpdir'
op|')'
newline|'\n'
comment|'# code below returns public key in pem format'
nl|'\n'
comment|'# key = M2Crypto.RSA.gen_key(bits, 65537, callback=lambda: None)'
nl|'\n'
comment|'# private_key = key.as_pem(cipher=None)'
nl|'\n'
comment|'# bio = M2Crypto.BIO.MemoryBuffer()'
nl|'\n'
comment|'# key.save_pub_key_bio(bio)'
nl|'\n'
comment|'# public_key = bio.read()'
nl|'\n'
comment|"# public_key, err = execute('ssh-keygen -y -f /dev/stdin', private_key)"
nl|'\n'
nl|'\n'
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
DECL|function|ssl_pub_to_ssh_pub
dedent|''
name|'def'
name|'ssl_pub_to_ssh_pub'
op|'('
name|'ssl_public_key'
op|','
name|'name'
op|'='
string|"'root'"
op|','
name|'suffix'
op|'='
string|"'nova'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""requires lsh-utils"""'
newline|'\n'
name|'convert'
op|'='
string|'"sed -e\'1d\' -e\'$d\' |  pkcs1-conv --public-key-info --base-64 |"'
op|'+'
string|'" sexp-conv |  sed -e\'1s/(rsa-pkcs1/(rsa-pkcs1-sha1/\' |  sexp-conv -s"'
op|'+'
string|'" transport | lsh-export-key --openssh"'
newline|'\n'
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
name|'convert'
op|','
name|'ssl_public_key'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Failed to generate key: %s"'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'%s %s@%s\\n'"
op|'%'
op|'('
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
op|','
name|'name'
op|','
name|'suffix'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_x509_cert
dedent|''
name|'def'
name|'generate_x509_cert'
op|'('
name|'subject'
op|'='
string|'"/C=US/ST=California/L=The Mission/O=CloudFed/OU=NOVA/CN=foo"'
op|','
name|'bits'
op|'='
number|'1024'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'tmpdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"openssl genrsa -out %s %s"'
op|'%'
op|'('
name|'keyfile'
op|','
name|'bits'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Generating private key: %s"'
op|','
string|'"openssl genrsa -out %s %s"'
op|'%'
op|'('
name|'keyfile'
op|','
name|'bits'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Generating CSR: %s"'
op|','
string|'"openssl req -new -key %s -out %s -batch -subj %s"'
op|'%'
op|'('
name|'keyfile'
op|','
name|'csrfile'
op|','
name|'subject'
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
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'tmpdir'
op|')'
newline|'\n'
name|'return'
op|'('
name|'private_key'
op|','
name|'csr'
op|')'
newline|'\n'
nl|'\n'
DECL|function|sign_csr
dedent|''
name|'def'
name|'sign_csr'
op|'('
name|'csr_text'
op|','
name|'intermediate'
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
name|'use_intermediate_ca'
op|':'
newline|'\n'
indent|'        '
name|'intermediate'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'intermediate'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'FLAGS'
op|'.'
name|'ca_path'
op|')'
newline|'\n'
dedent|''
name|'user_ca'
op|'='
string|'"%s/INTER/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'ca_path'
op|','
name|'intermediate'
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
name|'user_ca'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'FLAGS'
op|'.'
name|'ca_path'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Generating intermediate CA: %s"'
op|','
string|'"sh geninter.sh %s"'
op|'%'
op|'('
name|'intermediate'
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
dedent|''
name|'return'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'user_ca'
op|')'
newline|'\n'
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
name|'tmpfolder'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'csrfile'
op|'='
name|'open'
op|'('
string|'"%s/inbound.csr"'
op|'%'
op|'('
name|'tmpfolder'
op|')'
op|','
string|'"w"'
op|')'
newline|'\n'
name|'csrfile'
op|'.'
name|'write'
op|'('
name|'csr_text'
op|')'
newline|'\n'
name|'csrfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Flags path: %s"'
op|'%'
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
comment|'# Change working dir to CA'
nl|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_folder'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'runthis'
op|'('
string|'"Signing cert: %s"'
op|','
string|'"openssl ca -batch -out %s/outbound.crt -config ./openssl.cnf -infiles %s/inbound.csr"'
op|'%'
op|'('
name|'tmpfolder'
op|','
name|'tmpfolder'
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
name|'with'
name|'open'
op|'('
string|'"%s/outbound.crt"'
op|'%'
op|'('
name|'tmpfolder'
op|')'
op|','
string|'"r"'
op|')'
name|'as'
name|'crtfile'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'crtfile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkreq
dedent|''
dedent|''
name|'def'
name|'mkreq'
op|'('
name|'bits'
op|','
name|'subject'
op|'='
string|'"foo"'
op|','
name|'ca'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pk'
op|'='
name|'M2Crypto'
op|'.'
name|'EVP'
op|'.'
name|'PKey'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'Request'
op|'('
op|')'
newline|'\n'
name|'rsa'
op|'='
name|'M2Crypto'
op|'.'
name|'RSA'
op|'.'
name|'gen_key'
op|'('
name|'bits'
op|','
number|'65537'
op|','
name|'callback'
op|'='
name|'lambda'
op|':'
name|'None'
op|')'
newline|'\n'
name|'pk'
op|'.'
name|'assign_rsa'
op|'('
name|'rsa'
op|')'
newline|'\n'
name|'rsa'
op|'='
name|'None'
comment|'# should not be freed here'
newline|'\n'
name|'req'
op|'.'
name|'set_pubkey'
op|'('
name|'pk'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'set_subject'
op|'('
name|'subject'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'sign'
op|'('
name|'pk'
op|','
string|"'sha512'"
op|')'
newline|'\n'
name|'assert'
name|'req'
op|'.'
name|'verify'
op|'('
name|'pk'
op|')'
newline|'\n'
name|'pk2'
op|'='
name|'req'
op|'.'
name|'get_pubkey'
op|'('
op|')'
newline|'\n'
name|'assert'
name|'req'
op|'.'
name|'verify'
op|'('
name|'pk2'
op|')'
newline|'\n'
name|'return'
name|'req'
op|','
name|'pk'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkcacert
dedent|''
name|'def'
name|'mkcacert'
op|'('
name|'subject'
op|'='
string|"'nova'"
op|','
name|'years'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'req'
op|','
name|'pk'
op|'='
name|'mkreq'
op|'('
number|'2048'
op|','
name|'subject'
op|','
name|'ca'
op|'='
number|'1'
op|')'
newline|'\n'
name|'pkey'
op|'='
name|'req'
op|'.'
name|'get_pubkey'
op|'('
op|')'
newline|'\n'
name|'sub'
op|'='
name|'req'
op|'.'
name|'get_subject'
op|'('
op|')'
newline|'\n'
name|'cert'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'X509'
op|'('
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_serial_number'
op|'('
number|'1'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_version'
op|'('
number|'2'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_subject'
op|'('
name|'sub'
op|')'
comment|'# FIXME subject is not set in mkreq yet'
newline|'\n'
name|'t'
op|'='
name|'long'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
op|'+'
name|'time'
op|'.'
name|'timezone'
newline|'\n'
name|'now'
op|'='
name|'M2Crypto'
op|'.'
name|'ASN1'
op|'.'
name|'ASN1_UTCTIME'
op|'('
op|')'
newline|'\n'
name|'now'
op|'.'
name|'set_time'
op|'('
name|'t'
op|')'
newline|'\n'
name|'nowPlusYear'
op|'='
name|'M2Crypto'
op|'.'
name|'ASN1'
op|'.'
name|'ASN1_UTCTIME'
op|'('
op|')'
newline|'\n'
name|'nowPlusYear'
op|'.'
name|'set_time'
op|'('
name|'t'
op|'+'
op|'('
name|'years'
op|'*'
number|'60'
op|'*'
number|'60'
op|'*'
number|'24'
op|'*'
number|'365'
op|')'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_not_before'
op|'('
name|'now'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_not_after'
op|'('
name|'nowPlusYear'
op|')'
newline|'\n'
name|'issuer'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'X509_Name'
op|'('
op|')'
newline|'\n'
name|'issuer'
op|'.'
name|'C'
op|'='
string|'"US"'
newline|'\n'
name|'issuer'
op|'.'
name|'CN'
op|'='
name|'subject'
newline|'\n'
name|'cert'
op|'.'
name|'set_issuer'
op|'('
name|'issuer'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_pubkey'
op|'('
name|'pkey'
op|')'
newline|'\n'
name|'ext'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'new_extension'
op|'('
string|"'basicConstraints'"
op|','
string|"'CA:TRUE'"
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'add_ext'
op|'('
name|'ext'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'sign'
op|'('
name|'pk'
op|','
string|"'sha512'"
op|')'
newline|'\n'
nl|'\n'
comment|"# print 'cert', dir(cert)"
nl|'\n'
name|'print'
name|'cert'
op|'.'
name|'as_pem'
op|'('
op|')'
newline|'\n'
name|'print'
name|'pk'
op|'.'
name|'get_rsa'
op|'('
op|')'
op|'.'
name|'as_pem'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'cert'
op|','
name|'pk'
op|','
name|'pkey'
newline|'\n'
nl|'\n'
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
string|'"""\n    @type fp: file\n    @param fp: File pointer to the file to MD5 hash.  The file pointer will be\n               reset to the beginning of the file before the method returns.\n\n    @rtype: tuple\n    @return: the hex digest version of the MD5 hash\n    """'
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
