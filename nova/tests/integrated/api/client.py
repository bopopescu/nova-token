begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'json'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
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
string|"'nova.tests.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OpenStackApiException
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
name|'status'
newline|'\n'
name|'_body'
op|'='
name|'response'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'message'
op|'='
name|'_'
op|'('
string|"'%(message)s\\nStatus Code: %(_status)s\\n'"
nl|'\n'
string|"'Body: %(_body)s'"
op|')'
op|'%'
name|'locals'
op|'('
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
name|'_'
op|'('
string|'"Authentication error"'
op|')'
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
name|'_'
op|'('
string|'"Item not found"'
op|')'
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
string|'""" A really basic OpenStack API client that is under our control,\n    so we can make changes / insert hooks for testing"""'
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
name|'if'
name|'headers'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'parsed_url'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'url'
op|')'
newline|'\n'
name|'port'
op|'='
name|'parsed_url'
op|'.'
name|'port'
newline|'\n'
name|'hostname'
op|'='
name|'parsed_url'
op|'.'
name|'hostname'
newline|'\n'
name|'scheme'
op|'='
name|'parsed_url'
op|'.'
name|'scheme'
newline|'\n'
nl|'\n'
name|'if'
name|'scheme'
op|'=='
string|"'http'"
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'hostname'
op|','
nl|'\n'
name|'port'
op|'='
name|'port'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'scheme'
op|'=='
string|"'https'"
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'('
name|'hostname'
op|','
nl|'\n'
name|'port'
op|'='
name|'port'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'OpenStackApiException'
op|'('
string|'"Unknown scheme: %s"'
op|'%'
name|'url'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'relative_url'
op|'='
name|'parsed_url'
op|'.'
name|'path'
newline|'\n'
name|'if'
name|'parsed_url'
op|'.'
name|'query'
op|':'
newline|'\n'
indent|'            '
name|'relative_url'
op|'='
name|'relative_url'
op|'+'
name|'parsed_url'
op|'.'
name|'query'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Doing %(method)s on %(relative_url)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Body: %s"'
op|')'
op|'%'
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'conn'
op|'.'
name|'request'
op|'('
name|'method'
op|','
name|'relative_url'
op|','
name|'body'
op|','
name|'headers'
op|')'
newline|'\n'
name|'response'
op|'='
name|'conn'
op|'.'
name|'getresponse'
op|'('
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
name|'status'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(auth_uri)s => code %(http_status)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
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
name|'auth_headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'response'
op|'.'
name|'getheaders'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'auth_headers'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'auth_result'
op|'='
name|'auth_headers'
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
comment|"#NOTE(justinsb): httplib 'helpfully' converts headers to lower case"
nl|'\n'
name|'base_uri'
op|'='
name|'auth_result'
op|'['
string|"'x-server-management-url'"
op|']'
newline|'\n'
name|'full_uri'
op|'='
name|'base_uri'
op|'+'
name|'relative_uri'
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
name|'status'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(relative_uri)s => code %(http_status)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'check_response_status'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'http_status'
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
name|'_'
op|'('
string|'"Unexpected status code"'
op|')'
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
name|'body'
op|'='
name|'response'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Decoding JSON: %s"'
op|')'
op|'%'
op|'('
name|'body'
op|')'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
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
name|'response'
op|'='
name|'self'
op|'.'
name|'api_request'
op|'('
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_decode_json'
op|'('
name|'response'
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
name|'json'
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
op|']'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'api_request'
op|'('
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_decode_json'
op|'('
name|'response'
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
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'api_request'
op|'('
name|'relative_uri'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
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
name|'return'
name|'self'
op|'.'
name|'api_get'
op|'('
name|'rel_url'
op|')'
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
name|'return'
name|'self'
op|'.'
name|'api_post'
op|'('
string|"'/servers'"
op|','
name|'server'
op|')'
op|'['
string|"'server'"
op|']'
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
dedent|''
dedent|''
endmarker|''
end_unit
