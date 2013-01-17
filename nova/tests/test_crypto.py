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
name|'exception'
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
nl|'\n'
nl|'\n'
DECL|class|CertExceptionTests
dedent|''
dedent|''
name|'class'
name|'CertExceptionTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_fetch_ca_file_not_found
indent|'    '
name|'def'
name|'test_fetch_ca_file_not_found'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_project_ca'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CryptoCAFileNotFound'
op|','
name|'crypto'
op|'.'
name|'fetch_ca'
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fetch_crl_file_not_found
dedent|''
dedent|''
name|'def'
name|'test_fetch_crl_file_not_found'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_project_ca'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CryptoCRLFileNotFound'
op|','
nl|'\n'
name|'crypto'
op|'.'
name|'fetch_crl'
op|','
name|'project_id'
op|'='
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EncryptionTests
dedent|''
dedent|''
dedent|''
name|'class'
name|'EncryptionTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|pubkey
indent|'    '
name|'pubkey'
op|'='
op|'('
string|'"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDArtgrfBu/g2o28o+H2ng/crv"'
nl|'\n'
string|'"zgES91i/NNPPFTOutXelrJ9QiPTPTm+B8yspLsXifmbsmXztNOlBQgQXs6usxb4"'
nl|'\n'
string|'"fnJKNUZ84Vkp5esbqK/L7eyRqwPvqo7btKBMoAMVX/kUyojMpxb7Ssh6M6Y8cpi"'
nl|'\n'
string|'"goi+MSDPD7+5yRJ9z4mH9h7MCY6Ejv8KTcNYmVHvRhsFUcVhWcIISlNWUGiG7rf"'
nl|'\n'
string|'"oki060F5myQN3AXcL8gHG5/Qb1RVkQFUKZ5geQ39/wSyYA1Q65QTba/5G2QNbl2"'
nl|'\n'
string|'"0eAIBTyKZhN6g88ak+yARa6BLLDkrlP7L4WctHQMLsuXHohQsUO9AcOlVMARgrg"'
nl|'\n'
string|'"uF test@test"'
op|')'
newline|'\n'
name|'prikey'
op|'='
string|'"""-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAwK7YK3wbv4NqNvKPh9p4P3K784BEvdYvzTTzxUzrrV3payfU\nIj0z05vgfMrKS7F4n5m7Jl87TTpQUIEF7OrrMW+H5ySjVGfOFZKeXrG6ivy+3ska\nsD76qO27SgTKADFV/5FMqIzKcW+0rIejOmPHKYoKIvjEgzw+/uckSfc+Jh/YezAm\nOhI7/Ck3DWJlR70YbBVHFYVnCCEpTVlBohu636JItOtBeZskDdwF3C/IBxuf0G9U\nVZEBVCmeYHkN/f8EsmANUOuUE22v+RtkDW5dtHgCAU8imYTeoPPGpPsgEWugSyw5\nK5T+y+FnLR0DC7Llx6IULFDvQHDpVTAEYK4LhQIDAQABAoIBAF9ibrrgHnBpItx+\nqVUMbriiGK8LUXxUmqdQTljeolDZi6KzPc2RVKWtpazBSvG7skX3+XCediHd+0JP\nDNri1HlNiA6B0aUIGjoNsf6YpwsE4YwyK9cR5k5YGX4j7se3pKX2jOdngxQyw1Mh\ndkmCeWZz4l67nbSFz32qeQlwrsB56THJjgHB7elDoGCXTX/9VJyjFlCbfxVCsIng\ninrNgT0uMSYMNpAjTNOjguJt/DtXpwzei5eVpsERe0TRRVH23ycS0fuq/ancYwI/\nMDr9KSB8r+OVGeVGj3popCxECxYLBxhqS1dAQyJjhQXKwajJdHFzidjXO09hLBBz\nFiutpYUCgYEA6OFikTrPlCMGMJjSj+R9woDAOPfvCDbVZWfNo8iupiECvei88W28\nRYFnvUQRjSC0pHe//mfUSmiEaE+SjkNCdnNR+vsq9q+htfrADm84jl1mfeWatg/g\nzuGz2hAcZnux3kQMI7ufOwZNNpM2bf5B4yKamvG8tZRRxSkkAL1NV48CgYEA08/Z\nTy9g9XPKoLnUWStDh1zwG+c0q14l2giegxzaUAG5DOgOXbXcw0VQ++uOWD5ARELG\ng9wZcbBsXxJrRpUqx+GAlv2Y1bkgiPQS1JIyhsWEUtwfAC/G+uZhCX53aI3Pbsjh\nQmkPCSp5DuOuW2PybMaw+wVe+CaI/gwAWMYDAasCgYEA4Fzkvc7PVoU33XIeywr0\nLoQkrb4QyPUrOvt7H6SkvuFm5thn0KJMlRpLfAksb69m2l2U1+HooZd4mZawN+eN\nDNmlzgxWJDypq83dYwq8jkxmBj1DhMxfZnIE+L403nelseIVYAfPLOqxUTcbZXVk\nvRQFp+nmSXqQHUe5rAy1ivkCgYEAqLu7cclchCxqDv/6mc5NTVhMLu5QlvO5U6fq\nHqitgW7d69oxF5X499YQXZ+ZFdMBf19ypTiBTIAu1M3nh6LtIa4SsjXzus5vjKpj\nFdQhTBus/hU83Pkymk1MoDOPDEtsI+UDDdSDldmv9pyKGWPVi7H86vusXCLWnwsQ\ne6fCXWECgYEAqgpGvva5kJ1ISgNwnJbwiNw0sOT9BMOsdNZBElf0kJIIy6FMPvap\n6S1ziw+XWfdQ83VIUOCL5DrwmcYzLIogS0agmnx/monfDx0Nl9+OZRxy6+AI9vkK\n86A1+DXdo+IgX3grFK1l1gPhAZPRWJZ+anrEkyR4iLq6ZoPZ3BQn97U=\n-----END RSA PRIVATE KEY-----"""'
newline|'\n'
DECL|variable|text
name|'text'
op|'='
string|'"Some text! %$*"'
newline|'\n'
nl|'\n'
DECL|function|_ssh_decrypt_text
name|'def'
name|'_ssh_decrypt_text'
op|'('
name|'self'
op|','
name|'ssh_private_key'
op|','
name|'text'
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
name|'sshkey'
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
string|"'ssh.key'"
op|')'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'sshkey'
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
name|'ssh_private_key'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
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
name|'sshkey'
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
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'DecryptionFailure'
op|'('
name|'reason'
op|'='
name|'exc'
op|'.'
name|'stderr'
op|')'
newline|'\n'
nl|'\n'
DECL|function|test_ssh_encrypt_decrypt_text
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_ssh_encrypt_decrypt_text'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'enc'
op|'='
name|'crypto'
op|'.'
name|'ssh_encrypt_text'
op|'('
name|'self'
op|'.'
name|'pubkey'
op|','
name|'self'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'enc'
op|','
name|'self'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_ssh_decrypt_text'
op|'('
name|'self'
op|'.'
name|'prikey'
op|','
name|'enc'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'self'
op|'.'
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|function|test_ssh_encrypt_failure
dedent|''
name|'def'
name|'test_ssh_encrypt_failure'
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
name|'exception'
op|'.'
name|'EncryptionFailure'
op|','
nl|'\n'
name|'crypto'
op|'.'
name|'ssh_encrypt_text'
op|','
string|"''"
op|','
name|'self'
op|'.'
name|'text'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
