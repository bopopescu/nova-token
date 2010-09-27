begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nTest WSGI basics and provide some helper functions for other WSGI tests.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Test
name|'class'
name|'Test'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_debug
indent|'    '
name|'def'
name|'test_debug'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|Application
indent|'        '
name|'class'
name|'Application'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Dummy application to test debug."""'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'start_response'
op|'('
string|'"200"'
op|','
op|'['
op|'('
string|'"X-Test"'
op|','
string|'"checking"'
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
op|'['
string|"'Test result'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'application'
op|'='
name|'wsgi'
op|'.'
name|'Debug'
op|'('
name|'Application'
op|'('
op|')'
op|')'
newline|'\n'
name|'result'
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
name|'application'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"Test result"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_router
dedent|''
name|'def'
name|'test_router'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|Application
indent|'        '
name|'class'
name|'Application'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Test application to call from router."""'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'start_response'
op|'('
string|'"200"'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'return'
op|'['
string|"'Router result'"
op|']'
newline|'\n'
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Test router."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/test"'
op|','
name|'controller'
op|'='
name|'Application'
op|'('
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'Router'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'mapper'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'result'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/test'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'Router'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"Router result"'
op|')'
newline|'\n'
name|'result'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/bad'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'Router'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"Router result"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_controller
dedent|''
name|'def'
name|'test_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|Controller
indent|'        '
name|'class'
name|'Controller'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Test controller to call from router."""'
newline|'\n'
DECL|variable|test
name|'test'
op|'='
name|'self'
newline|'\n'
nl|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
comment|'# pylint: disable-msg=W0622,C0103'
newline|'\n'
indent|'                '
string|'"""Default action called for requests with an ID."""'
newline|'\n'
name|'self'
op|'.'
name|'test'
op|'.'
name|'assertEqual'
op|'('
name|'req'
op|'.'
name|'path_info'
op|','
string|"'/tests/123'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test'
op|'.'
name|'assertEqual'
op|'('
name|'id'
op|','
string|"'123'"
op|')'
newline|'\n'
name|'return'
name|'id'
newline|'\n'
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Test router."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"test"'
op|','
string|'"tests"'
op|','
name|'controller'
op|'='
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'Router'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'mapper'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'result'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'Router'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"123"'
op|')'
newline|'\n'
name|'result'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/test/123'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'Router'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"123"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SerializerTest
dedent|''
dedent|''
name|'class'
name|'SerializerTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|match
indent|'    '
name|'def'
name|'match'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'accept'
op|','
name|'expect'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'input_dict'
op|'='
name|'dict'
op|'('
name|'servers'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
op|'('
number|'2'
op|','
number|'3'
op|')'
op|')'
op|')'
newline|'\n'
name|'expected_xml'
op|'='
string|"'<servers><a>(2,3)</a></servers>'"
newline|'\n'
name|'expected_json'
op|'='
string|'\'{"servers":{"a":[2,3]}}\''
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
name|'headers'
op|'='
name|'dict'
op|'('
name|'Accept'
op|'='
name|'accept'
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'wsgi'
op|'.'
name|'Serializer'
op|'('
name|'req'
op|'.'
name|'environ'
op|')'
op|'.'
name|'to_content_type'
op|'('
name|'input_dict'
op|')'
newline|'\n'
name|'result'
op|'='
name|'result'
op|'.'
name|'replace'
op|'('
string|"'\\n'"
op|','
string|"''"
op|')'
op|'.'
name|'replace'
op|'('
string|"' '"
op|','
string|"''"
op|')'
newline|'\n'
name|'if'
name|'expect'
op|'=='
string|"'xml'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected_xml'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'expect'
op|'=='
string|"'json'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected_json'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
string|'"Bad expect value"'
newline|'\n'
nl|'\n'
DECL|member|test_basic
dedent|''
dedent|''
name|'def'
name|'test_basic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4.json'"
op|','
name|'None'
op|','
name|'expect'
op|'='
string|"'json'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4'"
op|','
string|"'application/json'"
op|','
name|'expect'
op|'='
string|"'json'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4'"
op|','
string|"'application/xml'"
op|','
name|'expect'
op|'='
string|"'xml'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4.xml'"
op|','
name|'None'
op|','
name|'expect'
op|'='
string|"'xml'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_defaults_to_json
dedent|''
name|'def'
name|'test_defaults_to_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4'"
op|','
name|'None'
op|','
name|'expect'
op|'='
string|"'json'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4'"
op|','
string|"'text/html'"
op|','
name|'expect'
op|'='
string|"'json'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_suffix_takes_precedence_over_accept_header
dedent|''
name|'def'
name|'test_suffix_takes_precedence_over_accept_header'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4.xml'"
op|','
string|"'application/json'"
op|','
name|'expect'
op|'='
string|"'xml'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'match'
op|'('
string|"'/servers/4.xml.'"
op|','
string|"'application/json'"
op|','
name|'expect'
op|'='
string|"'json'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
