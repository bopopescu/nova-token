begin_unit
comment|'#    Copyright (c) 2011 Justin Santa Barbara'
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
name|'urllib'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'requests'
newline|'\n'
name|'import'
name|'six'
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
nl|'\n'
DECL|class|APIResponse
name|'class'
name|'APIResponse'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decoded API Response\n\n    This provides a decoded version of the Requests response which\n    include a json decoded body, far more convenient for testing that\n    returned structures are correct, or using parts of returned\n    structures in tests.\n\n\n    This class is a simple wrapper around dictionaries for API\n    responses in tests. It includes extra attributes so that they can\n    be inspected in addition to the attributes.\n\n    All json responses from Nova APIs are dictionary compatible, or\n    blank, so other possible base classes are not needed.\n\n    """'
newline|'\n'
DECL|variable|status
name|'status'
op|'='
number|'200'
newline|'\n'
string|'"""The HTTP status code as an int"""'
newline|'\n'
DECL|variable|content
name|'content'
op|'='
string|'""'
newline|'\n'
string|'"""The Raw HTTP response body as a string"""'
newline|'\n'
DECL|variable|body
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
string|'"""The decoded json body as a dictionary"""'
newline|'\n'
DECL|variable|headers
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
string|'"""Response headers as a dictionary"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'response'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Construct an API response from a Requests response\n\n        :param response: a ``requests`` library response\n        """'
newline|'\n'
name|'super'
op|'('
name|'APIResponse'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'status'
op|'='
name|'response'
op|'.'
name|'status_code'
newline|'\n'
name|'self'
op|'.'
name|'content'
op|'='
name|'response'
op|'.'
name|'content'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'content'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'self'
op|'.'
name|'content'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'headers'
op|'='
name|'response'
op|'.'
name|'headers'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# because __str__ falls back to __repr__ we can still use repr'
nl|'\n'
comment|'# on self but add in the other attributes.'
nl|'\n'
indent|'        '
name|'return'
string|'"<Response body:%r, status_code:%s>"'
op|'%'
op|'('
name|'self'
op|'.'
name|'body'
op|','
name|'self'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OpenStackApiException
dedent|''
dedent|''
name|'class'
name|'OpenStackApiException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|','
name|'response'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'response'
op|'='
name|'response'
newline|'\n'
name|'if'
name|'not'
name|'message'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
string|"'Unspecified error'"
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'response'
op|':'
newline|'\n'
indent|'            '
name|'_status'
op|'='
name|'response'
op|'.'
name|'status_code'
newline|'\n'
name|'_body'
op|'='
name|'response'
op|'.'
name|'content'
newline|'\n'
nl|'\n'
name|'message'
op|'='
op|'('
string|"'%(message)s\\nStatus Code: %(_status)s\\n'"
nl|'\n'
string|"'Body: %(_body)s'"
op|'%'
nl|'\n'
op|'{'
string|"'message'"
op|':'
name|'message'
op|','
string|"'_status'"
op|':'
name|'_status'
op|','
nl|'\n'
string|"'_body'"
op|':'
name|'_body'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'OpenStackApiException'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OpenStackApiAuthenticationException
dedent|''
dedent|''
name|'class'
name|'OpenStackApiAuthenticationException'
op|'('
name|'OpenStackApiException'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'response'
op|'='
name|'None'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'message'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
string|'"Authentication error"'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'OpenStackApiAuthenticationException'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|','
nl|'\n'
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OpenStackApiAuthorizationException
dedent|''
dedent|''
name|'class'
name|'OpenStackApiAuthorizationException'
op|'('
name|'OpenStackApiException'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'response'
op|'='
name|'None'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'message'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
string|'"Authorization error"'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'OpenStackApiAuthorizationException'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|','
nl|'\n'
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OpenStackApiNotFoundException
dedent|''
dedent|''
name|'class'
name|'OpenStackApiNotFoundException'
op|'('
name|'OpenStackApiException'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'response'
op|'='
name|'None'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'message'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
string|'"Item not found"'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'OpenStackApiNotFoundException'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestOpenStackClient
dedent|''
dedent|''
name|'class'
name|'TestOpenStackClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simple OpenStack API Client.\n\n    This is a really basic OpenStack API client that is under our control,\n    so we can make changes / insert hooks for testing\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'auth_user'
op|','
name|'auth_key'
op|','
name|'auth_uri'
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'openstack'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestOpenStackClient'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth_result'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'auth_user'
op|'='
name|'auth_user'
newline|'\n'
name|'self'
op|'.'
name|'auth_key'
op|'='
name|'auth_key'
newline|'\n'
name|'self'
op|'.'
name|'auth_uri'
op|'='
name|'auth_uri'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
nl|'\n'
DECL|member|request
dedent|''
name|'def'
name|'request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'method'
op|'='
string|"'GET'"
op|','
name|'body'
op|'='
name|'None'
op|','
name|'headers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
newline|'\n'
name|'_headers'
op|'.'
name|'update'
op|'('
name|'headers'
name|'or'
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'requests'
op|'.'
name|'request'
op|'('
name|'method'
op|','
name|'url'
op|','
name|'data'
op|'='
name|'body'
op|','
name|'headers'
op|'='
name|'_headers'
op|')'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|_authenticate
dedent|''
name|'def'
name|'_authenticate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'auth_result'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'auth_result'
newline|'\n'
nl|'\n'
dedent|''
name|'auth_uri'
op|'='
name|'self'
op|'.'
name|'auth_uri'
newline|'\n'
name|'headers'
op|'='
op|'{'
string|"'X-Auth-User'"
op|':'
name|'self'
op|'.'
name|'auth_user'
op|','
nl|'\n'
string|"'X-Auth-Key'"
op|':'
name|'self'
op|'.'
name|'auth_key'
op|','
nl|'\n'
string|"'X-Auth-Project-Id'"
op|':'
name|'self'
op|'.'
name|'project_id'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'('
name|'auth_uri'
op|','
nl|'\n'
name|'headers'
op|'='
name|'headers'
op|')'
newline|'\n'
nl|'\n'
name|'http_status'
op|'='
name|'response'
op|'.'
name|'status_code'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(auth_uri)s => code %(http_status)s"'
op|','
nl|'\n'
op|'{'
string|"'auth_uri'"
op|':'
name|'auth_uri'
op|','
string|"'http_status'"
op|':'
name|'http_status'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'http_status'
op|'=='
number|'401'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'OpenStackApiAuthenticationException'
op|'('
name|'response'
op|'='
name|'response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'auth_result'
op|'='
name|'response'
op|'.'
name|'headers'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'auth_result'
newline|'\n'
nl|'\n'
DECL|member|api_request
dedent|''
name|'def'
name|'api_request'
op|'('
name|'self'
op|','
name|'relative_uri'
op|','
name|'check_response_status'
op|'='
name|'None'
op|','
nl|'\n'
name|'strip_version'
op|'='
name|'False'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'auth_result'
op|'='
name|'self'
op|'.'
name|'_authenticate'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(justinsb): httplib 'helpfully' converts headers to lower case"
nl|'\n'
name|'base_uri'
op|'='
name|'auth_result'
op|'['
string|"'x-server-management-url'"
op|']'
newline|'\n'
name|'if'
name|'strip_version'
op|':'
newline|'\n'
comment|'# NOTE(vish): cut out version number and tenant_id'
nl|'\n'
indent|'            '
name|'base_uri'
op|'='
string|"'/'"
op|'.'
name|'join'
op|'('
name|'base_uri'
op|'.'
name|'split'
op|'('
string|"'/'"
op|','
number|'3'
op|')'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'full_uri'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
name|'base_uri'
op|','
name|'relative_uri'
op|')'
newline|'\n'
nl|'\n'
name|'headers'
op|'='
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'headers'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
name|'auth_result'
op|'['
string|"'x-auth-token'"
op|']'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'('
name|'full_uri'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'http_status'
op|'='
name|'response'
op|'.'
name|'status_code'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(relative_uri)s => code %(http_status)s"'
op|','
nl|'\n'
op|'{'
string|"'relative_uri'"
op|':'
name|'relative_uri'
op|','
string|"'http_status'"
op|':'
name|'http_status'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'check_response_status'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'http_status'
name|'not'
name|'in'
name|'check_response_status'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'http_status'
op|'=='
number|'404'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'OpenStackApiNotFoundException'
op|'('
name|'response'
op|'='
name|'response'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'http_status'
op|'=='
number|'401'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'OpenStackApiAuthorizationException'
op|'('
name|'response'
op|'='
name|'response'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'OpenStackApiException'
op|'('
nl|'\n'
name|'message'
op|'='
string|'"Unexpected status code"'
op|','
nl|'\n'
name|'response'
op|'='
name|'response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|_decode_json
dedent|''
name|'def'
name|'_decode_json'
op|'('
name|'self'
op|','
name|'response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'APIResponse'
op|'('
name|'status'
op|'='
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'if'
name|'response'
op|'.'
name|'content'
op|':'
newline|'\n'
indent|'            '
name|'resp'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
DECL|member|api_get
dedent|''
name|'def'
name|'api_get'
op|'('
name|'self'
op|','
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'check_response_status'"
op|','
op|'['
number|'200'
op|']'
op|')'
newline|'\n'
name|'return'
name|'APIResponse'
op|'('
name|'self'
op|'.'
name|'api_request'
op|'('
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|api_post
dedent|''
name|'def'
name|'api_post'
op|'('
name|'self'
op|','
name|'relative_uri'
op|','
name|'body'
op|','
name|'api_version'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'['
string|"'method'"
op|']'
op|'='
string|"'POST'"
newline|'\n'
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'='
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'headers'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'kwargs'
op|'['
string|"'body'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'api_version'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'['
string|"'X-OpenStack-Nova-API-Version'"
op|']'
op|'='
name|'api_version'
newline|'\n'
nl|'\n'
dedent|''
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'check_response_status'"
op|','
op|'['
number|'200'
op|','
number|'202'
op|']'
op|')'
newline|'\n'
name|'return'
name|'APIResponse'
op|'('
name|'self'
op|'.'
name|'api_request'
op|'('
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|api_put
dedent|''
name|'def'
name|'api_put'
op|'('
name|'self'
op|','
name|'relative_uri'
op|','
name|'body'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'['
string|"'method'"
op|']'
op|'='
string|"'PUT'"
newline|'\n'
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'='
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'headers'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'kwargs'
op|'['
string|"'body'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'check_response_status'"
op|','
op|'['
number|'200'
op|','
number|'202'
op|','
number|'204'
op|']'
op|')'
newline|'\n'
name|'return'
name|'APIResponse'
op|'('
name|'self'
op|'.'
name|'api_request'
op|'('
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|api_delete
dedent|''
name|'def'
name|'api_delete'
op|'('
name|'self'
op|','
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'['
string|"'method'"
op|']'
op|'='
string|"'DELETE'"
newline|'\n'
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'check_response_status'"
op|','
op|'['
number|'200'
op|','
number|'202'
op|','
number|'204'
op|']'
op|')'
newline|'\n'
name|'return'
name|'APIResponse'
op|'('
name|'self'
op|'.'
name|'api_request'
op|'('
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'#####################################'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Convenience methods'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The following are a set of convenience methods to get well known'
nl|'\n'
comment|'# resources, they can be helpful in setting up resources in'
nl|'\n'
comment|'# tests. All of these convenience methods throw exceptions if they'
nl|'\n'
comment|'# get a non 20x status code, so will appropriately abort tests if'
nl|'\n'
comment|'# they fail.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# They all return the most relevant part of their response body as'
nl|'\n'
comment|'# decoded data structure.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#####################################'
nl|'\n'
nl|'\n'
DECL|member|get_server
dedent|''
name|'def'
name|'get_server'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/servers/%s'"
op|'%'
name|'server_id'
op|')'
op|'.'
name|'body'
op|'['
string|"'server'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_servers
dedent|''
name|'def'
name|'get_servers'
op|'('
name|'self'
op|','
name|'detail'
op|'='
name|'True'
op|','
name|'search_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rel_url'
op|'='
string|"'/servers/detail'"
name|'if'
name|'detail'
name|'else'
string|"'/servers'"
newline|'\n'
nl|'\n'
name|'if'
name|'search_opts'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'qparams'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'opt'
op|','
name|'val'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'search_opts'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'qparams'
op|'['
name|'opt'
op|']'
op|'='
name|'val'
newline|'\n'
dedent|''
name|'if'
name|'qparams'
op|':'
newline|'\n'
indent|'                '
name|'query_string'
op|'='
string|'"?%s"'
op|'%'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'qparams'
op|')'
newline|'\n'
name|'rel_url'
op|'+='
name|'query_string'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
name|'rel_url'
op|')'
op|'.'
name|'body'
op|'['
string|"'servers'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|post_server
dedent|''
name|'def'
name|'post_server'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/servers'"
op|','
name|'server'
op|')'
op|'.'
name|'body'
newline|'\n'
name|'if'
string|"'reservation_id'"
name|'in'
name|'response'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'response'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'response'
op|'['
string|"'server'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|put_server
dedent|''
dedent|''
name|'def'
name|'put_server'
op|'('
name|'self'
op|','
name|'server_id'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_put'
op|'('
string|"'/servers/%s'"
op|'%'
name|'server_id'
op|','
name|'server'
op|')'
op|'.'
name|'body'
newline|'\n'
nl|'\n'
DECL|member|post_server_action
dedent|''
name|'def'
name|'post_server_action'
op|'('
name|'self'
op|','
name|'server_id'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/servers/%s/action'"
op|'%'
name|'server_id'
op|','
name|'data'
op|')'
op|'.'
name|'body'
newline|'\n'
nl|'\n'
DECL|member|delete_server
dedent|''
name|'def'
name|'delete_server'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_delete'
op|'('
string|"'/servers/%s'"
op|'%'
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_image
dedent|''
name|'def'
name|'get_image'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/images/%s'"
op|'%'
name|'image_id'
op|')'
op|'.'
name|'body'
op|'['
string|"'image'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_images
dedent|''
name|'def'
name|'get_images'
op|'('
name|'self'
op|','
name|'detail'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rel_url'
op|'='
string|"'/images/detail'"
name|'if'
name|'detail'
name|'else'
string|"'/images'"
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
name|'rel_url'
op|')'
op|'.'
name|'body'
op|'['
string|"'images'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|post_image
dedent|''
name|'def'
name|'post_image'
op|'('
name|'self'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/images'"
op|','
name|'image'
op|')'
op|'.'
name|'body'
op|'['
string|"'image'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|delete_image
dedent|''
name|'def'
name|'delete_image'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_delete'
op|'('
string|"'/images/%s'"
op|'%'
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_flavor
dedent|''
name|'def'
name|'get_flavor'
op|'('
name|'self'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/flavors/%s'"
op|'%'
name|'flavor_id'
op|')'
op|'.'
name|'body'
op|'['
string|"'flavor'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_flavors
dedent|''
name|'def'
name|'get_flavors'
op|'('
name|'self'
op|','
name|'detail'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rel_url'
op|'='
string|"'/flavors/detail'"
name|'if'
name|'detail'
name|'else'
string|"'/flavors'"
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
name|'rel_url'
op|')'
op|'.'
name|'body'
op|'['
string|"'flavors'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|post_flavor
dedent|''
name|'def'
name|'post_flavor'
op|'('
name|'self'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/flavors'"
op|','
name|'flavor'
op|')'
op|'.'
name|'body'
op|'['
string|"'flavor'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|delete_flavor
dedent|''
name|'def'
name|'delete_flavor'
op|'('
name|'self'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_delete'
op|'('
string|"'/flavors/%s'"
op|'%'
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_extra_spec
dedent|''
name|'def'
name|'post_extra_spec'
op|'('
name|'self'
op|','
name|'flavor_id'
op|','
name|'spec'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/flavors/%s/os-extra_specs'"
op|'%'
nl|'\n'
name|'flavor_id'
op|','
name|'spec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_volume
dedent|''
name|'def'
name|'get_volume'
op|'('
name|'self'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/volumes/%s'"
op|'%'
name|'volume_id'
op|')'
op|'.'
name|'body'
op|'['
string|"'volume'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_volumes
dedent|''
name|'def'
name|'get_volumes'
op|'('
name|'self'
op|','
name|'detail'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rel_url'
op|'='
string|"'/volumes/detail'"
name|'if'
name|'detail'
name|'else'
string|"'/volumes'"
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
name|'rel_url'
op|')'
op|'.'
name|'body'
op|'['
string|"'volumes'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|post_volume
dedent|''
name|'def'
name|'post_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/volumes'"
op|','
name|'volume'
op|')'
op|'.'
name|'body'
op|'['
string|"'volume'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_delete'
op|'('
string|"'/volumes/%s'"
op|'%'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_server_volume
dedent|''
name|'def'
name|'get_server_volume'
op|'('
name|'self'
op|','
name|'server_id'
op|','
name|'attachment_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/servers/%s/os-volume_attachments/%s'"
op|'%'
nl|'\n'
op|'('
name|'server_id'
op|','
name|'attachment_id'
op|')'
nl|'\n'
op|')'
op|'.'
name|'body'
op|'['
string|"'volumeAttachment'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_server_volumes
dedent|''
name|'def'
name|'get_server_volumes'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/servers/%s/os-volume_attachments'"
op|'%'
nl|'\n'
op|'('
name|'server_id'
op|')'
op|')'
op|'.'
name|'body'
op|'['
string|"'volumeAttachments'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|post_server_volume
dedent|''
name|'def'
name|'post_server_volume'
op|'('
name|'self'
op|','
name|'server_id'
op|','
name|'volume_attachment'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/servers/%s/os-volume_attachments'"
op|'%'
nl|'\n'
op|'('
name|'server_id'
op|')'
op|','
name|'volume_attachment'
nl|'\n'
op|')'
op|'.'
name|'body'
op|'['
string|"'volumeAttachment'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|delete_server_volume
dedent|''
name|'def'
name|'delete_server_volume'
op|'('
name|'self'
op|','
name|'server_id'
op|','
name|'attachment_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_delete'
op|'('
string|"'/servers/%s/os-volume_attachments/%s'"
op|'%'
nl|'\n'
op|'('
name|'server_id'
op|','
name|'attachment_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_server_metadata
dedent|''
name|'def'
name|'post_server_metadata'
op|'('
name|'self'
op|','
name|'server_id'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'post_body'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'post_body'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'update'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/servers/%s/metadata'"
op|'%'
name|'server_id'
op|','
nl|'\n'
name|'post_body'
op|')'
op|'.'
name|'body'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_server_groups
dedent|''
name|'def'
name|'get_server_groups'
op|'('
name|'self'
op|','
name|'all_projects'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'all_projects'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
nl|'\n'
string|"'/os-server-groups?all_projects'"
op|')'
op|'.'
name|'body'
op|'['
string|"'server_groups'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/os-server-groups'"
op|')'
op|'.'
name|'body'
op|'['
string|"'server_groups'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_server_group
dedent|''
dedent|''
name|'def'
name|'get_server_group'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/os-server-groups/%s'"
op|'%'
nl|'\n'
name|'group_id'
op|')'
op|'.'
name|'body'
op|'['
string|"'server_group'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|post_server_groups
dedent|''
name|'def'
name|'post_server_groups'
op|'('
name|'self'
op|','
name|'group'
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/os-server-groups'"
op|','
op|'{'
string|'"server_group"'
op|':'
name|'group'
op|'}'
op|','
nl|'\n'
name|'api_version'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'body'
op|'['
string|"'server_group'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|delete_server_group
dedent|''
name|'def'
name|'delete_server_group'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'api_delete'
op|'('
string|"'/os-server-groups/%s'"
op|'%'
name|'group_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_actions
dedent|''
name|'def'
name|'get_instance_actions'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
string|"'/servers/%s/os-instance-actions'"
op|'%'
nl|'\n'
op|'('
name|'server_id'
op|')'
op|')'
op|'.'
name|'body'
op|'['
string|"'instanceActions'"
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
