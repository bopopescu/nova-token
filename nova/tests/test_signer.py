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
string|'"""Tests for Signer."""'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'signer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ClassWithStrRepr
name|'class'
name|'ClassWithStrRepr'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__repr__
indent|'    '
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'A string representation'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SignerTestCase
dedent|''
dedent|''
name|'class'
name|'SignerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'SignerTestCase'
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
name|'signer'
op|'='
name|'signer'
op|'.'
name|'Signer'
op|'('
string|"'uV3F3YluFJax1cknvbcGwgjvx4QpvB+leU8dUj2o'"
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
name|'super'
op|'('
name|'SignerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# S3 Authorization Signing input & output examples taken from here:'
nl|'\n'
comment|'# http://docs.amazonwebservices.com/AmazonS3/latest/dev/'
nl|'\n'
DECL|member|test_s3_authorization_get
dedent|''
name|'def'
name|'test_s3_authorization_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'xXjDGYUmKxnwqr5KXNPGldn5LbA='"
op|','
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'.'
name|'s3_authorization'
op|'('
nl|'\n'
op|'{'
string|"'Date'"
op|':'
string|"'Tue, 27 Mar 2007 19:36:42 +0000'"
op|'}'
op|','
nl|'\n'
string|"'GET'"
op|','
nl|'\n'
string|"'/johnsmith/photos/puppy.jpg'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_s3_authorization_put
dedent|''
name|'def'
name|'test_s3_authorization_put'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'hcicpDDvL9SsO6AkvxqmIWkmOuQ='"
op|','
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'.'
name|'s3_authorization'
op|'('
nl|'\n'
op|'{'
string|"'Date'"
op|':'
string|"'Tue, 27 Mar 2007 21:15:45 +0000'"
op|','
nl|'\n'
string|"'Content-Length'"
op|':'
string|"'94328'"
op|','
nl|'\n'
string|"'Content-Type'"
op|':'
string|"'image/jpeg'"
op|'}'
op|','
nl|'\n'
string|"'PUT'"
op|','
nl|'\n'
string|"'/johnsmith/photos/puppy.jpg'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_using_version_2
dedent|''
name|'def'
name|'test_generate_using_version_2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'clXalhbLZXxEuI32OoX+OeXsN6Mr2q4jzGyIDAr4RZg='"
op|','
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'.'
name|'generate'
op|'('
nl|'\n'
op|'{'
string|"'SignatureMethod'"
op|':'
string|"'HmacSHA256'"
op|','
nl|'\n'
string|"'SignatureVersion'"
op|':'
string|"'2'"
op|'}'
op|','
nl|'\n'
string|"'GET'"
op|','
string|"'server'"
op|','
string|"'/foo'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_force_HmacSHA1
dedent|''
name|'def'
name|'test_generate_force_HmacSHA1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Stub out haslib.sha256'
nl|'\n'
indent|'        '
name|'import'
name|'hashlib'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'hashlib'
op|','
string|"'sha256'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create Signer again now that hashlib.sha256 is None'
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'='
name|'signer'
op|'.'
name|'Signer'
op|'('
nl|'\n'
string|"'uV3F3YluFJax1cknvbcGwgjvx4QpvB+leU8dUj2o'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'uJTByiDIcgB65STrS5i2egQgd+U='"
op|','
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'.'
name|'generate'
op|'('
op|'{'
string|"'SignatureVersion'"
op|':'
string|"'2'"
op|'}'
op|','
nl|'\n'
string|"'GET'"
op|','
string|"'server'"
op|','
string|"'/foo'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_with_unicode_param
dedent|''
name|'def'
name|'test_generate_with_unicode_param'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'clXalhbLZXxEuI32OoX+OeXsN6Mr2q4jzGyIDAr4RZg='"
op|','
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'.'
name|'generate'
op|'('
op|'{'
string|"'SignatureVersion'"
op|':'
string|"u'2'"
op|'}'
op|','
nl|'\n'
string|"'GET'"
op|','
string|"'server'"
op|','
string|"'/foo'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_with_non_string_or_unicode_param
dedent|''
name|'def'
name|'test_generate_with_non_string_or_unicode_param'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'99IAgCkhTR2aMTgRobnzKGuNxVFSdb7vlQRvnj3Urqk='"
op|','
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'.'
name|'generate'
op|'('
nl|'\n'
op|'{'
string|"'AnotherParam'"
op|':'
name|'ClassWithStrRepr'
op|'('
op|')'
op|','
nl|'\n'
string|"'SignatureVersion'"
op|':'
string|"'2'"
op|'}'
op|','
nl|'\n'
string|"'GET'"
op|','
string|"'server'"
op|','
string|"'/foo'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_unknown_version
dedent|''
name|'def'
name|'test_generate_unknown_version'
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
name|'Error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'signer'
op|'.'
name|'generate'
op|','
nl|'\n'
op|'{'
string|"'SignatureMethod'"
op|':'
string|"'HmacSHA256'"
op|','
string|"'SignatureVersion'"
op|':'
string|"'9'"
op|'}'
op|','
nl|'\n'
string|"'GET'"
op|','
string|"'server'"
op|','
string|"'/foo'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
