begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'json'
newline|'\n'
nl|'\n'
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
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFaults
name|'class'
name|'TestFaults'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests covering `nova.api.openstack.faults:Fault` class."""'
newline|'\n'
nl|'\n'
DECL|member|_prepare_xml
name|'def'
name|'_prepare_xml'
op|'('
name|'self'
op|','
name|'xml_string'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove characters from string which hinder XML equality testing."""'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"\\n"'
op|','
string|'""'
op|')'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"\\t"'
op|','
string|'""'
op|')'
newline|'\n'
name|'return'
name|'xml_string'
newline|'\n'
nl|'\n'
DECL|member|test_400_fault_xml
dedent|''
name|'def'
name|'test_400_fault_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test fault serialized to XML via file-extension and/or header."""'
newline|'\n'
name|'requests'
op|'='
op|'['
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/xml"'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'fault'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|"'scram'"
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
string|'"""\n                <badRequest code="400">\n                    <message>scram</message>\n                </badRequest>\n            """'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_400_fault_json
dedent|''
dedent|''
name|'def'
name|'test_400_fault_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test fault serialized to JSON via file-extension and/or header."""'
newline|'\n'
name|'requests'
op|'='
op|'['
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.json'"
op|')'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/json"'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'fault'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|"'scram'"
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"badRequest"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"scram"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'400'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'actual'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_413_fault_xml
dedent|''
dedent|''
name|'def'
name|'test_413_fault_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'requests'
op|'='
op|'['
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/xml"'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
newline|'\n'
name|'fault'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'('
name|'explanation'
op|'='
string|"'sorry'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
number|'4'
op|'}'
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
string|'"""\n                <overLimit code="413">\n                    <message>sorry</message>\n                    <retryAfter>4</retryAfter>\n                </overLimit>\n            """'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'headers'
op|'['
string|"'Retry-After'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_413_fault_json
dedent|''
dedent|''
name|'def'
name|'test_413_fault_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test fault serialized to JSON via file-extension and/or header."""'
newline|'\n'
name|'requests'
op|'='
op|'['
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.json'"
op|')'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/json"'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
newline|'\n'
name|'fault'
op|'='
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'('
name|'explanation'
op|'='
string|"'sorry'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
number|'4'
op|'}'
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"overLimit"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"sorry"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'413'
op|','
nl|'\n'
string|'"retryAfter"'
op|':'
number|'4'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'actual'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_raise
dedent|''
dedent|''
name|'def'
name|'test_raise'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the ability to raise exceptions in WSGI-ified methods."""'
newline|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|raiser
name|'def'
name|'raiser'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
string|"'whut?'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'raiser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'content_type'
op|','
string|'"application/xml"'
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'whut?'"
name|'in'
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
