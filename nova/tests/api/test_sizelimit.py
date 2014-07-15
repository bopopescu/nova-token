begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
name|'StringIO'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'sizelimit'
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
DECL|variable|MAX_REQUEST_BODY_SIZE
name|'MAX_REQUEST_BODY_SIZE'
op|'='
name|'CONF'
op|'.'
name|'osapi_max_request_body_size'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLimitingReader
name|'class'
name|'TestLimitingReader'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_limiting_reader
indent|'    '
name|'def'
name|'test_limiting_reader'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'BYTES'
op|'='
number|'1024'
newline|'\n'
name|'bytes_read'
op|'='
number|'0'
newline|'\n'
name|'data'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|'"*"'
op|'*'
name|'BYTES'
op|')'
newline|'\n'
name|'for'
name|'chunk'
name|'in'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'sizelimit'
op|'.'
name|'LimitingReader'
op|'('
name|'data'
op|','
name|'BYTES'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bytes_read'
op|'+='
name|'len'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bytes_read'
op|','
name|'BYTES'
op|')'
newline|'\n'
nl|'\n'
name|'bytes_read'
op|'='
number|'0'
newline|'\n'
name|'data'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|'"*"'
op|'*'
name|'BYTES'
op|')'
newline|'\n'
name|'reader'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'sizelimit'
op|'.'
name|'LimitingReader'
op|'('
name|'data'
op|','
name|'BYTES'
op|')'
newline|'\n'
name|'byte'
op|'='
name|'reader'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
name|'while'
name|'len'
op|'('
name|'byte'
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'bytes_read'
op|'+='
number|'1'
newline|'\n'
name|'byte'
op|'='
name|'reader'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bytes_read'
op|','
name|'BYTES'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_limiting_reader_fails
dedent|''
name|'def'
name|'test_limiting_reader_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'BYTES'
op|'='
number|'1024'
newline|'\n'
nl|'\n'
DECL|function|_consume_all_iter
name|'def'
name|'_consume_all_iter'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bytes_read'
op|'='
number|'0'
newline|'\n'
name|'data'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|'"*"'
op|'*'
name|'BYTES'
op|')'
newline|'\n'
name|'for'
name|'chunk'
name|'in'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'sizelimit'
op|'.'
name|'LimitingReader'
op|'('
name|'data'
op|','
name|'BYTES'
op|'-'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'bytes_read'
op|'+='
name|'len'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|','
nl|'\n'
name|'_consume_all_iter'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_consume_all_read
name|'def'
name|'_consume_all_read'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bytes_read'
op|'='
number|'0'
newline|'\n'
name|'data'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|'"*"'
op|'*'
name|'BYTES'
op|')'
newline|'\n'
name|'reader'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'sizelimit'
op|'.'
name|'LimitingReader'
op|'('
name|'data'
op|','
name|'BYTES'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'byte'
op|'='
name|'reader'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
name|'while'
name|'len'
op|'('
name|'byte'
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'bytes_read'
op|'+='
number|'1'
newline|'\n'
name|'byte'
op|'='
name|'reader'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|','
nl|'\n'
name|'_consume_all_read'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestRequestBodySizeLimiter
dedent|''
dedent|''
name|'class'
name|'TestRequestBodySizeLimiter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'TestRequestBodySizeLimiter'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
op|')'
newline|'\n'
DECL|function|fake_app
name|'def'
name|'fake_app'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'middleware'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'sizelimit'
op|'.'
name|'RequestBodySizeLimiter'
op|'('
name|'fake_app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'method'
op|'='
string|"'POST'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_length_acceptable
dedent|''
name|'def'
name|'test_content_length_acceptable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'Content-Length'"
op|']'
op|'='
name|'MAX_REQUEST_BODY_SIZE'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'body'
op|'='
string|'"0"'
op|'*'
name|'MAX_REQUEST_BODY_SIZE'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_length_too_large
dedent|''
name|'def'
name|'test_content_length_too_large'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'Content-Length'"
op|']'
op|'='
name|'MAX_REQUEST_BODY_SIZE'
op|'+'
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'body'
op|'='
string|'"0"'
op|'*'
op|'('
name|'MAX_REQUEST_BODY_SIZE'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'413'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_request_too_large_no_content_length
dedent|''
name|'def'
name|'test_request_too_large_no_content_length'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'body'
op|'='
string|'"0"'
op|'*'
op|'('
name|'MAX_REQUEST_BODY_SIZE'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'Content-Length'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'413'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
