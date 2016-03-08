begin_unit
comment|'# Copyright (c) The Johns Hopkins University/Applied Physics Laboratory'
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
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'castellan'
op|'.'
name|'common'
op|'.'
name|'exception'
name|'import'
name|'KeyManagerError'
newline|'\n'
name|'import'
name|'cryptography'
op|'.'
name|'exceptions'
name|'as'
name|'crypto_exceptions'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'backends'
name|'import'
name|'default_backend'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'primitives'
op|'.'
name|'asymmetric'
name|'import'
name|'dsa'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'primitives'
op|'.'
name|'asymmetric'
name|'import'
name|'ec'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'primitives'
op|'.'
name|'asymmetric'
name|'import'
name|'padding'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'primitives'
op|'.'
name|'asymmetric'
name|'import'
name|'rsa'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
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
name|'signature_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|TEST_RSA_PRIVATE_KEY
name|'TEST_RSA_PRIVATE_KEY'
op|'='
name|'rsa'
op|'.'
name|'generate_private_key'
op|'('
name|'public_exponent'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|key_size
name|'key_size'
op|'='
number|'1024'
op|','
nl|'\n'
DECL|variable|backend
name|'backend'
op|'='
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# secp521r1 is assumed to be available on all supported platforms'
nl|'\n'
DECL|variable|TEST_ECC_PRIVATE_KEY
name|'TEST_ECC_PRIVATE_KEY'
op|'='
name|'ec'
op|'.'
name|'generate_private_key'
op|'('
name|'ec'
op|'.'
name|'SECP521R1'
op|'('
op|')'
op|','
nl|'\n'
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|TEST_DSA_PRIVATE_KEY
name|'TEST_DSA_PRIVATE_KEY'
op|'='
name|'dsa'
op|'.'
name|'generate_private_key'
op|'('
name|'key_size'
op|'='
number|'3072'
op|','
nl|'\n'
DECL|variable|backend
name|'backend'
op|'='
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeKeyManager
name|'class'
name|'FakeKeyManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'certs'
op|'='
op|'{'
string|"'invalid_format_cert'"
op|':'
nl|'\n'
name|'FakeCastellanCertificate'
op|'('
string|"'A'"
op|'*'
number|'256'
op|','
string|"'BLAH'"
op|')'
op|','
nl|'\n'
string|"'valid_format_cert'"
op|':'
nl|'\n'
name|'FakeCastellanCertificate'
op|'('
string|"'A'"
op|'*'
number|'256'
op|','
string|"'X.509'"
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cert_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cert'
op|'='
name|'self'
op|'.'
name|'certs'
op|'.'
name|'get'
op|'('
name|'cert_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'cert'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'KeyManagerError'
op|'('
string|'"No matching certificate found."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cert'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCastellanCertificate
dedent|''
dedent|''
name|'class'
name|'FakeCastellanCertificate'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'cert_format'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
name|'data'
newline|'\n'
name|'self'
op|'.'
name|'cert_format'
op|'='
name|'cert_format'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|format
name|'def'
name|'format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'cert_format'
newline|'\n'
nl|'\n'
DECL|member|get_encoded
dedent|''
name|'def'
name|'get_encoded'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'data'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCryptoCertificate
dedent|''
dedent|''
name|'class'
name|'FakeCryptoCertificate'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'pub_key'
op|'='
name|'TEST_RSA_PRIVATE_KEY'
op|'.'
name|'public_key'
op|'('
op|')'
op|','
nl|'\n'
name|'not_valid_before'
op|'='
op|'('
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
nl|'\n'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
number|'1'
op|')'
op|')'
op|','
nl|'\n'
name|'not_valid_after'
op|'='
op|'('
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'+'
nl|'\n'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
number|'2'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pub_key'
op|'='
name|'pub_key'
newline|'\n'
name|'self'
op|'.'
name|'cert_not_valid_before'
op|'='
name|'not_valid_before'
newline|'\n'
name|'self'
op|'.'
name|'cert_not_valid_after'
op|'='
name|'not_valid_after'
newline|'\n'
nl|'\n'
DECL|member|public_key
dedent|''
name|'def'
name|'public_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'pub_key'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|not_valid_before
name|'def'
name|'not_valid_before'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'cert_not_valid_before'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|not_valid_after
name|'def'
name|'not_valid_after'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'cert_not_valid_after'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BadPublicKey
dedent|''
dedent|''
name|'class'
name|'BadPublicKey'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|verifier
indent|'    '
name|'def'
name|'verifier'
op|'('
name|'self'
op|','
name|'signature'
op|','
name|'padding'
op|','
name|'hash_method'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSignatureUtils
dedent|''
dedent|''
name|'class'
name|'TestSignatureUtils'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test methods of signature_utils"""'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_public_key'"
op|')'
newline|'\n'
DECL|member|test_verify_signature_PSS
name|'def'
name|'test_verify_signature_PSS'
op|'('
name|'self'
op|','
name|'mock_get_pub_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
string|"b'224626ae19824466f2a7f39ab7b80f7f'"
newline|'\n'
name|'mock_get_pub_key'
op|'.'
name|'return_value'
op|'='
name|'TEST_RSA_PRIVATE_KEY'
op|'.'
name|'public_key'
op|'('
op|')'
newline|'\n'
name|'for'
name|'hash_name'
op|','
name|'hash_alg'
name|'in'
name|'signature_utils'
op|'.'
name|'HASH_METHODS'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'signer'
op|'='
name|'TEST_RSA_PRIVATE_KEY'
op|'.'
name|'signer'
op|'('
nl|'\n'
name|'padding'
op|'.'
name|'PSS'
op|'('
nl|'\n'
name|'mgf'
op|'='
name|'padding'
op|'.'
name|'MGF1'
op|'('
name|'hash_alg'
op|')'
op|','
nl|'\n'
name|'salt_length'
op|'='
name|'padding'
op|'.'
name|'PSS'
op|'.'
name|'MAX_LENGTH'
nl|'\n'
op|')'
op|','
nl|'\n'
name|'hash_alg'
nl|'\n'
op|')'
newline|'\n'
name|'signer'
op|'.'
name|'update'
op|'('
name|'data'
op|')'
newline|'\n'
name|'signature'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'signer'
op|'.'
name|'finalize'
op|'('
op|')'
op|')'
newline|'\n'
name|'img_sig_cert_uuid'
op|'='
string|"'fea14bc2-d75f-4ba5-bccc-b5c924ad0693'"
newline|'\n'
name|'verifier'
op|'='
name|'signature_utils'
op|'.'
name|'get_verifier'
op|'('
name|'None'
op|','
name|'img_sig_cert_uuid'
op|','
nl|'\n'
name|'hash_name'
op|','
name|'signature'
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'RSA_PSS'
op|')'
newline|'\n'
name|'verifier'
op|'.'
name|'update'
op|'('
name|'data'
op|')'
newline|'\n'
name|'verifier'
op|'.'
name|'verify'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_public_key'"
op|')'
newline|'\n'
DECL|member|test_verify_signature_ECC
name|'def'
name|'test_verify_signature_ECC'
op|'('
name|'self'
op|','
name|'mock_get_pub_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
string|"b'224626ae19824466f2a7f39ab7b80f7f'"
newline|'\n'
comment|'# test every ECC curve'
nl|'\n'
name|'for'
name|'curve'
name|'in'
name|'signature_utils'
op|'.'
name|'ECC_CURVES'
op|':'
newline|'\n'
indent|'            '
name|'key_type_name'
op|'='
string|"'ECC_'"
op|'+'
name|'curve'
op|'.'
name|'name'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|'.'
name|'lookup'
op|'('
name|'key_type_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|':'
newline|'\n'
indent|'                '
name|'import'
name|'warnings'
newline|'\n'
name|'warnings'
op|'.'
name|'warn'
op|'('
string|'"ECC curve \'%s\' not supported"'
op|'%'
name|'curve'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Create a private key to use'
nl|'\n'
dedent|''
name|'private_key'
op|'='
name|'ec'
op|'.'
name|'generate_private_key'
op|'('
name|'curve'
op|','
nl|'\n'
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
name|'mock_get_pub_key'
op|'.'
name|'return_value'
op|'='
name|'private_key'
op|'.'
name|'public_key'
op|'('
op|')'
newline|'\n'
name|'for'
name|'hash_name'
op|','
name|'hash_alg'
name|'in'
name|'signature_utils'
op|'.'
name|'HASH_METHODS'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'signer'
op|'='
name|'private_key'
op|'.'
name|'signer'
op|'('
nl|'\n'
name|'ec'
op|'.'
name|'ECDSA'
op|'('
name|'hash_alg'
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'signer'
op|'.'
name|'update'
op|'('
name|'data'
op|')'
newline|'\n'
name|'signature'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'signer'
op|'.'
name|'finalize'
op|'('
op|')'
op|')'
newline|'\n'
name|'img_sig_cert_uuid'
op|'='
string|"'fea14bc2-d75f-4ba5-bccc-b5c924ad0693'"
newline|'\n'
name|'verifier'
op|'='
name|'signature_utils'
op|'.'
name|'get_verifier'
op|'('
name|'None'
op|','
nl|'\n'
name|'img_sig_cert_uuid'
op|','
nl|'\n'
name|'hash_name'
op|','
name|'signature'
op|','
nl|'\n'
name|'key_type_name'
op|')'
newline|'\n'
name|'verifier'
op|'.'
name|'update'
op|'('
name|'data'
op|')'
newline|'\n'
name|'verifier'
op|'.'
name|'verify'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_public_key'"
op|')'
newline|'\n'
DECL|member|test_verify_signature_DSA
name|'def'
name|'test_verify_signature_DSA'
op|'('
name|'self'
op|','
name|'mock_get_pub_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
string|"b'224626ae19824466f2a7f39ab7b80f7f'"
newline|'\n'
name|'mock_get_pub_key'
op|'.'
name|'return_value'
op|'='
name|'TEST_DSA_PRIVATE_KEY'
op|'.'
name|'public_key'
op|'('
op|')'
newline|'\n'
name|'for'
name|'hash_name'
op|','
name|'hash_alg'
name|'in'
name|'signature_utils'
op|'.'
name|'HASH_METHODS'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'signer'
op|'='
name|'TEST_DSA_PRIVATE_KEY'
op|'.'
name|'signer'
op|'('
nl|'\n'
name|'hash_alg'
nl|'\n'
op|')'
newline|'\n'
name|'signer'
op|'.'
name|'update'
op|'('
name|'data'
op|')'
newline|'\n'
name|'signature'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'signer'
op|'.'
name|'finalize'
op|'('
op|')'
op|')'
newline|'\n'
name|'img_sig_cert_uuid'
op|'='
string|"'fea14bc2-d75f-4ba5-bccc-b5c924ad0693'"
newline|'\n'
name|'verifier'
op|'='
name|'signature_utils'
op|'.'
name|'get_verifier'
op|'('
name|'None'
op|','
name|'img_sig_cert_uuid'
op|','
nl|'\n'
name|'hash_name'
op|','
name|'signature'
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'DSA'
op|')'
newline|'\n'
name|'verifier'
op|'.'
name|'update'
op|'('
name|'data'
op|')'
newline|'\n'
name|'verifier'
op|'.'
name|'verify'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_public_key'"
op|')'
newline|'\n'
DECL|member|test_verify_signature_bad_signature
name|'def'
name|'test_verify_signature_bad_signature'
op|'('
name|'self'
op|','
name|'mock_get_pub_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
string|"b'224626ae19824466f2a7f39ab7b80f7f'"
newline|'\n'
name|'mock_get_pub_key'
op|'.'
name|'return_value'
op|'='
name|'TEST_RSA_PRIVATE_KEY'
op|'.'
name|'public_key'
op|'('
op|')'
newline|'\n'
name|'img_sig_cert_uuid'
op|'='
string|"'fea14bc2-d75f-4ba5-bccc-b5c924ad0693'"
newline|'\n'
name|'verifier'
op|'='
name|'signature_utils'
op|'.'
name|'get_verifier'
op|'('
name|'None'
op|','
name|'img_sig_cert_uuid'
op|','
nl|'\n'
string|"'SHA-256'"
op|','
string|"'BLAH'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'RSA_PSS'
op|')'
newline|'\n'
name|'verifier'
op|'.'
name|'update'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'crypto_exceptions'
op|'.'
name|'InvalidSignature'
op|','
nl|'\n'
name|'verifier'
op|'.'
name|'verify'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_verifier_invalid_image_props
dedent|''
name|'def'
name|'test_get_verifier_invalid_image_props'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Required image properties for signature'"
nl|'\n'
string|"' verification do not exist. Cannot verify'"
nl|'\n'
string|"' signature. Missing property: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_verifier'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
string|"'SHA-256'"
op|','
string|"'BLAH'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'RSA_PSS'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_public_key'"
op|')'
newline|'\n'
DECL|member|test_verify_signature_bad_sig_key_type
name|'def'
name|'test_verify_signature_bad_sig_key_type'
op|'('
name|'self'
op|','
name|'mock_get_pub_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_pub_key'
op|'.'
name|'return_value'
op|'='
name|'TEST_RSA_PRIVATE_KEY'
op|'.'
name|'public_key'
op|'('
op|')'
newline|'\n'
name|'img_sig_cert_uuid'
op|'='
string|"'fea14bc2-d75f-4ba5-bccc-b5c924ad0693'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Invalid signature key type: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_verifier'
op|','
nl|'\n'
name|'None'
op|','
name|'img_sig_cert_uuid'
op|','
string|"'SHA-256'"
op|','
nl|'\n'
string|"'BLAH'"
op|','
string|"'BLAH'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_public_key'"
op|')'
newline|'\n'
DECL|member|test_get_verifier_none
name|'def'
name|'test_get_verifier_none'
op|'('
name|'self'
op|','
name|'mock_get_pub_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_pub_key'
op|'.'
name|'return_value'
op|'='
name|'BadPublicKey'
op|'('
op|')'
newline|'\n'
name|'img_sig_cert_uuid'
op|'='
string|"'fea14bc2-d75f-4ba5-bccc-b5c924ad0693'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Error occurred while creating'"
nl|'\n'
string|"' the verifier'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_verifier'
op|','
nl|'\n'
name|'None'
op|','
name|'img_sig_cert_uuid'
op|','
string|"'SHA-256'"
op|','
nl|'\n'
string|"'BLAH'"
op|','
name|'signature_utils'
op|'.'
name|'RSA_PSS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_signature
dedent|''
name|'def'
name|'test_get_signature'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'signature'
op|'='
string|"b'A'"
op|'*'
number|'256'
newline|'\n'
name|'data'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'signature'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'signature'
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_signature'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_signature_fail
dedent|''
name|'def'
name|'test_get_signature_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'The signature data was not properly'"
nl|'\n'
string|"' encoded using base64'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_signature'
op|','
string|"'///'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_hash_method
dedent|''
name|'def'
name|'test_get_hash_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hash_dict'
op|'='
name|'signature_utils'
op|'.'
name|'HASH_METHODS'
newline|'\n'
name|'for'
name|'hash_name'
name|'in'
name|'hash_dict'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'hash_class'
op|'='
name|'signature_utils'
op|'.'
name|'get_hash_method'
op|'('
name|'hash_name'
op|')'
op|'.'
name|'__class__'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'hash_dict'
op|'['
name|'hash_name'
op|']'
op|','
name|'hash_class'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_hash_method_fail
dedent|''
dedent|''
name|'def'
name|'test_get_hash_method_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Invalid signature hash method: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_hash_method'
op|','
string|"'SHA-2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_signature_key_type_lookup
dedent|''
name|'def'
name|'test_signature_key_type_lookup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'sig_format'
name|'in'
op|'['
name|'signature_utils'
op|'.'
name|'RSA_PSS'
op|','
name|'signature_utils'
op|'.'
name|'DSA'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'sig_key_type'
op|'='
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|'.'
name|'lookup'
op|'('
name|'sig_format'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'sig_key_type'
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sig_format'
op|','
name|'sig_key_type'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_signature_key_type_lookup_fail
dedent|''
dedent|''
name|'def'
name|'test_signature_key_type_lookup_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Invalid signature key type: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|'.'
name|'lookup'
op|','
nl|'\n'
string|"'RSB-PSS'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_certificate'"
op|')'
newline|'\n'
DECL|member|test_get_public_key_rsa
name|'def'
name|'test_get_public_key_rsa'
op|'('
name|'self'
op|','
name|'mock_get_cert'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_cert'
op|'='
name|'FakeCryptoCertificate'
op|'('
op|')'
newline|'\n'
name|'mock_get_cert'
op|'.'
name|'return_value'
op|'='
name|'fake_cert'
newline|'\n'
name|'sig_key_type'
op|'='
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|'.'
name|'lookup'
op|'('
nl|'\n'
name|'signature_utils'
op|'.'
name|'RSA_PSS'
nl|'\n'
op|')'
newline|'\n'
name|'result_pub_key'
op|'='
name|'signature_utils'
op|'.'
name|'get_public_key'
op|'('
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'sig_key_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_cert'
op|'.'
name|'public_key'
op|'('
op|')'
op|','
name|'result_pub_key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_certificate'"
op|')'
newline|'\n'
DECL|member|test_get_public_key_ecc
name|'def'
name|'test_get_public_key_ecc'
op|'('
name|'self'
op|','
name|'mock_get_cert'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_cert'
op|'='
name|'FakeCryptoCertificate'
op|'('
name|'TEST_ECC_PRIVATE_KEY'
op|'.'
name|'public_key'
op|'('
op|')'
op|')'
newline|'\n'
name|'mock_get_cert'
op|'.'
name|'return_value'
op|'='
name|'fake_cert'
newline|'\n'
name|'sig_key_type'
op|'='
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|'.'
name|'lookup'
op|'('
string|"'ECC_SECP521R1'"
op|')'
newline|'\n'
name|'result_pub_key'
op|'='
name|'signature_utils'
op|'.'
name|'get_public_key'
op|'('
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'sig_key_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_cert'
op|'.'
name|'public_key'
op|'('
op|')'
op|','
name|'result_pub_key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_certificate'"
op|')'
newline|'\n'
DECL|member|test_get_public_key_dsa
name|'def'
name|'test_get_public_key_dsa'
op|'('
name|'self'
op|','
name|'mock_get_cert'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_cert'
op|'='
name|'FakeCryptoCertificate'
op|'('
name|'TEST_DSA_PRIVATE_KEY'
op|'.'
name|'public_key'
op|'('
op|')'
op|')'
newline|'\n'
name|'mock_get_cert'
op|'.'
name|'return_value'
op|'='
name|'fake_cert'
newline|'\n'
name|'sig_key_type'
op|'='
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|'.'
name|'lookup'
op|'('
nl|'\n'
name|'signature_utils'
op|'.'
name|'DSA'
nl|'\n'
op|')'
newline|'\n'
name|'result_pub_key'
op|'='
name|'signature_utils'
op|'.'
name|'get_public_key'
op|'('
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'sig_key_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_cert'
op|'.'
name|'public_key'
op|'('
op|')'
op|','
name|'result_pub_key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.signature_utils.get_certificate'"
op|')'
newline|'\n'
DECL|member|test_get_public_key_invalid_key
name|'def'
name|'test_get_public_key_invalid_key'
op|'('
name|'self'
op|','
name|'mock_get_certificate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_pub_key'
op|'='
string|"'A'"
op|'*'
number|'256'
newline|'\n'
name|'mock_get_certificate'
op|'.'
name|'return_value'
op|'='
name|'FakeCryptoCertificate'
op|'('
name|'bad_pub_key'
op|')'
newline|'\n'
name|'sig_key_type'
op|'='
name|'signature_utils'
op|'.'
name|'SignatureKeyType'
op|'.'
name|'lookup'
op|'('
nl|'\n'
name|'signature_utils'
op|'.'
name|'RSA_PSS'
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Invalid public key type for '"
nl|'\n'
string|"'signature key type: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_public_key'
op|','
name|'None'
op|','
nl|'\n'
name|'None'
op|','
name|'sig_key_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'cryptography.x509.load_der_x509_certificate'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'castellan.key_manager.API'"
op|','
name|'return_value'
op|'='
name|'FakeKeyManager'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_get_certificate
name|'def'
name|'test_get_certificate'
op|'('
name|'self'
op|','
name|'mock_key_manager_API'
op|','
name|'mock_load_cert'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cert_uuid'
op|'='
string|"'valid_format_cert'"
newline|'\n'
name|'x509_cert'
op|'='
name|'FakeCryptoCertificate'
op|'('
op|')'
newline|'\n'
name|'mock_load_cert'
op|'.'
name|'return_value'
op|'='
name|'x509_cert'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'x509_cert'
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_certificate'
op|'('
name|'None'
op|','
name|'cert_uuid'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'cryptography.x509.load_der_x509_certificate'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'castellan.key_manager.API'"
op|','
name|'return_value'
op|'='
name|'FakeKeyManager'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_get_expired_certificate
name|'def'
name|'test_get_expired_certificate'
op|'('
name|'self'
op|','
name|'mock_key_manager_API'
op|','
nl|'\n'
name|'mock_load_cert'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cert_uuid'
op|'='
string|"'valid_format_cert'"
newline|'\n'
name|'x509_cert'
op|'='
name|'FakeCryptoCertificate'
op|'('
nl|'\n'
name|'not_valid_after'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
nl|'\n'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
number|'1'
op|')'
op|')'
newline|'\n'
name|'mock_load_cert'
op|'.'
name|'return_value'
op|'='
name|'x509_cert'
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Certificate is not valid after: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_certificate'
op|','
name|'None'
op|','
nl|'\n'
name|'cert_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'cryptography.x509.load_der_x509_certificate'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'castellan.key_manager.API'"
op|','
name|'return_value'
op|'='
name|'FakeKeyManager'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_get_not_yet_valid_certificate
name|'def'
name|'test_get_not_yet_valid_certificate'
op|'('
name|'self'
op|','
name|'mock_key_manager_API'
op|','
nl|'\n'
name|'mock_load_cert'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cert_uuid'
op|'='
string|"'valid_format_cert'"
newline|'\n'
name|'x509_cert'
op|'='
name|'FakeCryptoCertificate'
op|'('
nl|'\n'
name|'not_valid_before'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'+'
nl|'\n'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
number|'1'
op|')'
op|')'
newline|'\n'
name|'mock_load_cert'
op|'.'
name|'return_value'
op|'='
name|'x509_cert'
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Certificate is not valid before: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_certificate'
op|','
name|'None'
op|','
nl|'\n'
name|'cert_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'castellan.key_manager.API'"
op|','
name|'return_value'
op|'='
name|'FakeKeyManager'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_get_certificate_key_manager_fail
name|'def'
name|'test_get_certificate_key_manager_fail'
op|'('
name|'self'
op|','
name|'mock_key_manager_API'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_cert_uuid'
op|'='
string|"'fea14bc2-d75f-4ba5-bccc-b5c924ad0695'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Unable to retrieve certificate with ID: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_certificate'
op|','
name|'None'
op|','
nl|'\n'
name|'bad_cert_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'castellan.key_manager.API'"
op|','
name|'return_value'
op|'='
name|'FakeKeyManager'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_get_certificate_invalid_format
name|'def'
name|'test_get_certificate_invalid_format'
op|'('
name|'self'
op|','
name|'mock_API'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cert_uuid'
op|'='
string|"'invalid_format_cert'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaisesRegex'
op|'('
name|'exception'
op|'.'
name|'SignatureVerificationError'
op|','
nl|'\n'
string|"'Invalid certificate format: .*'"
op|','
nl|'\n'
name|'signature_utils'
op|'.'
name|'get_certificate'
op|','
name|'None'
op|','
nl|'\n'
name|'cert_uuid'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
