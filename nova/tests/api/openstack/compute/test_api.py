begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
name|'as'
name|'openstack_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APITest
name|'class'
name|'APITest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_wsgi_app
indent|'    '
name|'def'
name|'_wsgi_app'
op|'('
name|'self'
op|','
name|'inner_app'
op|')'
op|':'
newline|'\n'
comment|'# simpler version of the app than fakes.wsgi_app'
nl|'\n'
indent|'        '
name|'return'
name|'openstack_api'
op|'.'
name|'FaultWrapper'
op|'('
name|'inner_app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_malformed_json
dedent|''
name|'def'
name|'test_malformed_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
string|"'{'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_malformed_xml
dedent|''
name|'def'
name|'test_malformed_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
string|"'<hi im not xml>'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/xml"'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vendor_content_type_json
dedent|''
name|'def'
name|'test_vendor_content_type_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctype'
op|'='
string|"'application/vnd.openstack.compute+json'"
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
name|'ctype'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
name|'ctype'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vendor_content_type_xml
dedent|''
name|'def'
name|'test_vendor_content_type_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctype'
op|'='
string|"'application/vnd.openstack.compute+xml'"
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
name|'ctype'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
name|'ctype'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'etree'
op|'.'
name|'XML'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exceptions_are_converted_to_faults_webob_exc
dedent|''
name|'def'
name|'test_exceptions_are_converted_to_faults_webob_exc'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|raise_webob_exc
name|'def'
name|'raise_webob_exc'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
string|"'Raised a webob.exc'"
op|')'
newline|'\n'
nl|'\n'
comment|'#api.application = raise_webob_exc'
nl|'\n'
dedent|''
name|'api'
op|'='
name|'self'
op|'.'
name|'_wsgi_app'
op|'('
name|'raise_webob_exc'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exceptions_are_converted_to_faults_api_fault
dedent|''
name|'def'
name|'test_exceptions_are_converted_to_faults_api_fault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|raise_api_fault
name|'def'
name|'raise_api_fault'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
string|"'Raised a webob.exc'"
op|')'
newline|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
comment|'#api.application = raise_api_fault'
nl|'\n'
dedent|''
name|'api'
op|'='
name|'self'
op|'.'
name|'_wsgi_app'
op|'('
name|'raise_api_fault'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'itemNotFound'"
name|'in'
name|'resp'
op|'.'
name|'body'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exceptions_are_converted_to_faults_exception
dedent|''
name|'def'
name|'test_exceptions_are_converted_to_faults_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|fail
name|'def'
name|'fail'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Threw an exception"'
op|')'
newline|'\n'
nl|'\n'
comment|'#api.application = fail'
nl|'\n'
dedent|''
name|'api'
op|'='
name|'self'
op|'.'
name|'_wsgi_app'
op|'('
name|'fail'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'\'{"computeFault\''
name|'in'
name|'resp'
op|'.'
name|'body'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'500'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exceptions_are_converted_to_faults_exception_xml
dedent|''
name|'def'
name|'test_exceptions_are_converted_to_faults_exception_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|fail
name|'def'
name|'fail'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Threw an exception"'
op|')'
newline|'\n'
nl|'\n'
comment|'#api.application = fail'
nl|'\n'
dedent|''
name|'api'
op|'='
name|'self'
op|'.'
name|'_wsgi_app'
op|'('
name|'fail'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'<computeFault'"
name|'in'
name|'resp'
op|'.'
name|'body'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'500'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_test_exception_safety_reflected_in_faults
dedent|''
name|'def'
name|'_do_test_exception_safety_reflected_in_faults'
op|'('
name|'self'
op|','
name|'expose'
op|')'
op|':'
newline|'\n'
DECL|class|ExceptionWithSafety
indent|'        '
name|'class'
name|'ExceptionWithSafety'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|safe
indent|'            '
name|'safe'
op|'='
name|'expose'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|fail
name|'def'
name|'fail'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ExceptionWithSafety'
op|'('
string|"'some explanation'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'api'
op|'='
name|'self'
op|'.'
name|'_wsgi_app'
op|'('
name|'fail'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'\'{"computeFault\''
name|'in'
name|'resp'
op|'.'
name|'body'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'('
string|"'ExceptionWithSafety: some explanation'"
name|'if'
name|'expose'
name|'else'
nl|'\n'
string|"'The server has either erred or is incapable '"
nl|'\n'
string|"'of performing the requested operation.'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'expected'
name|'in'
name|'resp'
op|'.'
name|'body'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'500'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_safe_exceptions_are_described_in_faults
dedent|''
name|'def'
name|'test_safe_exceptions_are_described_in_faults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_exception_safety_reflected_in_faults'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unsafe_exceptions_are_not_described_in_faults
dedent|''
name|'def'
name|'test_unsafe_exceptions_are_not_described_in_faults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_exception_safety_reflected_in_faults'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_test_exception_mapping
dedent|''
name|'def'
name|'_do_test_exception_mapping'
op|'('
name|'self'
op|','
name|'exception_type'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|fail
name|'def'
name|'fail'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception_type'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'api'
op|'='
name|'self'
op|'.'
name|'_wsgi_app'
op|'('
name|'fail'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'msg'
name|'in'
name|'resp'
op|'.'
name|'body'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
name|'exception_type'
op|'.'
name|'code'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'hasattr'
op|'('
name|'exception_type'
op|','
string|"'headers'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'exception_type'
op|'.'
name|'headers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'key'
name|'in'
name|'resp'
op|'.'
name|'headers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'resp'
op|'.'
name|'headers'
op|'['
name|'key'
op|']'
op|','
name|'str'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quota_error_mapping
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_quota_error_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_exception_mapping'
op|'('
name|'exception'
op|'.'
name|'QuotaError'
op|','
string|"'too many used'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_nova_notfound_exception_mapping
dedent|''
name|'def'
name|'test_non_nova_notfound_exception_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|ExceptionWithCode
indent|'        '
name|'class'
name|'ExceptionWithCode'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|variable|code
indent|'            '
name|'code'
op|'='
number|'404'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_do_test_exception_mapping'
op|'('
name|'ExceptionWithCode'
op|','
nl|'\n'
string|"'NotFound'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_nova_exception_mapping
dedent|''
name|'def'
name|'test_non_nova_exception_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|ExceptionWithCode
indent|'        '
name|'class'
name|'ExceptionWithCode'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|variable|code
indent|'            '
name|'code'
op|'='
number|'417'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_do_test_exception_mapping'
op|'('
name|'ExceptionWithCode'
op|','
nl|'\n'
string|"'Expectation failed'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exception_with_none_code_throws_500
dedent|''
name|'def'
name|'test_exception_with_none_code_throws_500'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|ExceptionWithNoneCode
indent|'        '
name|'class'
name|'ExceptionWithNoneCode'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|variable|code
indent|'            '
name|'code'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'msg'
op|'='
string|"'Internal Server Error'"
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|fail
name|'def'
name|'fail'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ExceptionWithNoneCode'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'api'
op|'='
name|'self'
op|'.'
name|'_wsgi_app'
op|'('
name|'fail'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'500'
op|','
name|'resp'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_request_id_in_response
dedent|''
name|'def'
name|'test_request_id_in_response'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'context'
op|'='
name|'nova'
op|'.'
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'bob'"
op|','
number|'1'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'request_id'
op|'='
string|"'test-req-id'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'context'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'headers'
op|'['
string|"'x-compute-request-id'"
op|']'
op|','
string|"'test-req-id'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
