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
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.api.openstack.v2.test_urlmap'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UrlmapTest
name|'class'
name|'UrlmapTest'
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
name|'UrlmapTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_path_version_v1_1
dedent|''
name|'def'
name|'test_path_version_v1_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test URL path specifying v1.1 returns v2 content."""'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'v2.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_version_v1_1
dedent|''
name|'def'
name|'test_content_type_version_v1_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test Content-Type specifying v1.1 returns v2 content."""'
newline|'\n'
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
name|'content_type'
op|'='
string|'"application/json;version=1.1"'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'v2.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accept_version_v1_1
dedent|''
name|'def'
name|'test_accept_version_v1_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test Accept header specifying v1.1 returns v2 content."""'
newline|'\n'
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
name|'accept'
op|'='
string|'"application/json;version=1.1"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'v2.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_path_version_v2
dedent|''
name|'def'
name|'test_path_version_v2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test URL path specifying v2 returns v2 content."""'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'v2.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_version_v2
dedent|''
name|'def'
name|'test_content_type_version_v2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test Content-Type specifying v2 returns v2 content."""'
newline|'\n'
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
name|'content_type'
op|'='
string|'"application/json;version=2"'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'v2.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accept_version_v2
dedent|''
name|'def'
name|'test_accept_version_v2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test Accept header specifying v2 returns v2 content."""'
newline|'\n'
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
name|'accept'
op|'='
string|'"application/json;version=2"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'v2.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_path_content_type
dedent|''
name|'def'
name|'test_path_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test URL path specifying JSON returns JSON content."""'
newline|'\n'
name|'url'
op|'='
string|"'/v2/fake/images/cedef40a-ed67-4d10-800e-17455edce175.json'"
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
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/xml"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'image'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accept_content_type
dedent|''
name|'def'
name|'test_accept_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test Accept header specifying JSON returns JSON content."""'
newline|'\n'
name|'url'
op|'='
string|"'/v2/fake/images/cedef40a-ed67-4d10-800e-17455edce175'"
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
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/xml;q=0.8, application/json"'
newline|'\n'
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
string|'"application/json"'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'image'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
