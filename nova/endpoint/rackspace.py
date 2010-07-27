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
string|'"""\nRackspace API\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'multiprocessing'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'import'
name|'tornado'
op|'.'
name|'web'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'datastore'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'storage'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'cloud_topic'"
op|','
string|"'cloud'"
op|','
string|"'the topic clouds listen on'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Unauthorized
name|'class'
name|'Unauthorized'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|NotFound
dedent|''
name|'class'
name|'NotFound'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Api
dedent|''
name|'class'
name|'Api'
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
string|'"""build endpoints here"""'
newline|'\n'
name|'self'
op|'.'
name|'controllers'
op|'='
op|'{'
nl|'\n'
string|'"v1.0"'
op|':'
name|'RackspaceAuthenticationApi'
op|'('
op|')'
op|','
nl|'\n'
string|'"servers"'
op|':'
name|'RackspaceCloudServerApi'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|handler
dedent|''
name|'def'
name|'handler'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'responder'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        This is the entrypoint from wsgi.  Read PEP 333 and wsgi.org for\n        more intormation.  The key points are responder is a callback that\n        needs to run before you return, and takes two arguments, response\n        code string ("200 OK") and headers (["X-How-Cool-Am-I: Ultra-Suede"])\n        and the return value is the body of the response.\n        """'
newline|'\n'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'build_context'
op|'('
name|'environ'
op|')'
newline|'\n'
name|'controller'
op|','
name|'path'
op|'='
name|'wsgi'
op|'.'
name|'Util'
op|'.'
name|'route'
op|'('
nl|'\n'
name|'environ'
op|'['
string|"'PATH_INFO'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controllers'
nl|'\n'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Route %s to %s"'
op|','
name|'str'
op|'('
name|'path'
op|')'
op|','
name|'str'
op|'('
name|'controller'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'controller'
op|':'
newline|'\n'
indent|'            '
name|'responder'
op|'('
string|'"404 Not Found"'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'return'
string|'""'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'='
name|'controller'
op|'.'
name|'process'
op|'('
name|'path'
op|','
name|'environ'
op|')'
newline|'\n'
name|'if'
name|'type'
op|'('
name|'rv'
op|')'
name|'is'
name|'tuple'
op|':'
newline|'\n'
indent|'                '
name|'responder'
op|'('
name|'rv'
op|'['
number|'0'
op|']'
op|','
name|'rv'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'rv'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'responder'
op|'('
string|'"200 OK"'
op|','
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rv'
newline|'\n'
dedent|''
name|'except'
name|'Unauthorized'
op|':'
newline|'\n'
indent|'            '
name|'responder'
op|'('
string|'"401 Unauthorized"'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'return'
string|'""'
newline|'\n'
dedent|''
name|'except'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'responder'
op|'('
string|'"404 Not Found"'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'return'
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|build_context
dedent|''
dedent|''
name|'def'
name|'build_context'
op|'('
name|'self'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'env'
op|'.'
name|'has_key'
op|'('
string|'"HTTP_X_AUTH_TOKEN"'
op|')'
op|':'
newline|'\n'
comment|'# TODO(todd): once we make an actual unique token, this will change'
nl|'\n'
indent|'            '
name|'rv'
op|'['
string|"'user'"
op|']'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'get_user_from_access_key'
op|'('
nl|'\n'
name|'env'
op|'['
string|"'HTTP_X_AUTH_TOKEN'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'rv'
op|'['
string|"'user'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'rv'
op|'['
string|"'project'"
op|']'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
nl|'\n'
name|'rv'
op|'['
string|"'user'"
op|']'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RackspaceApiEndpoint
dedent|''
dedent|''
name|'class'
name|'RackspaceApiEndpoint'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|process
indent|'    '
name|'def'
name|'process'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Main entrypoint for all controllers (what gets run by the wsgi handler).\n        Check authentication based on key, raise Unauthorized if invalid.\n\n        Select the most appropriate action based on request type GET, POST, etc,\n        then pass it through to the implementing controller.  Defalut to GET if\n        the implementing child doesn\'t respond to a particular type.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'check_authentication'
op|'('
name|'env'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Unauthorized'
op|'('
string|'"Unable to authenticate"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'method'
op|'='
name|'env'
op|'['
string|"'REQUEST_METHOD'"
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'callback'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'callback'
op|':'
newline|'\n'
indent|'            '
name|'callback'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|'"get"'
op|')'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"%s processing %s with %s"'
op|','
name|'self'
op|','
name|'method'
op|','
name|'callback'
op|')'
newline|'\n'
name|'return'
name|'callback'
op|'('
name|'path'
op|','
name|'env'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        The default GET will look at the path and call an appropriate\n        action within this controller based on the the structure of the path.\n\n        Given the following path lengths (with the first part stripped of by\n        router, as it is the controller name):\n            = 0  -> index\n            = 1  -> first component (/servers/details -> details)\n            >= 2 -> second path component (/servers/ID/ips/* -> ips)\n\n        This should return\n            A String if 200 OK and no additional headers\n            (CODE, HEADERS, BODY) for custom response code and headers\n        """'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'path'
op|')'
op|'=='
number|'0'
name|'and'
name|'hasattr'
op|'('
name|'self'
op|','
string|'"index"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"%s running index"'
op|','
name|'self'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'index'
op|'('
name|'env'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'path'
op|')'
op|'>='
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'='
name|'path'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'='
name|'path'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"%s running action %s"'
op|','
name|'self'
op|','
name|'action'
op|')'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'self'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'action'
op|')'
newline|'\n'
name|'return'
name|'method'
op|'('
name|'path'
op|','
name|'env'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotFound'
op|'('
string|'"Missing method %s"'
op|'%'
name|'path'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_authentication
dedent|''
dedent|''
name|'def'
name|'check_authentication'
op|'('
name|'self'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'env'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RackspaceAuthenticationApi
dedent|''
dedent|''
name|'class'
name|'RackspaceAuthenticationApi'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# TODO(todd): make a actual session with a unique token'
nl|'\n'
comment|'# just pass the auth key back through for now'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'_path'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
string|"'204 No Content'"
newline|'\n'
name|'headers'
op|'='
op|'['
nl|'\n'
op|'('
string|"'X-Server-Management-Url'"
op|','
string|"'http://%s'"
op|'%'
name|'env'
op|'['
string|"'HTTP_HOST'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'X-Storage-Url'"
op|','
string|"'http://%s'"
op|'%'
name|'env'
op|'['
string|"'HTTP_HOST'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'X-CDN-Managment-Url'"
op|','
string|"'http://%s'"
op|'%'
name|'env'
op|'['
string|"'HTTP_HOST'"
op|']'
op|')'
op|','
nl|'\n'
op|'('
string|"'X-Auth-Token'"
op|','
name|'env'
op|'['
string|"'HTTP_X_AUTH_KEY'"
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'body'
op|'='
string|'""'
newline|'\n'
name|'return'
op|'('
name|'response'
op|','
name|'headers'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RackspaceCloudServerApi
dedent|''
dedent|''
name|'class'
name|'RackspaceCloudServerApi'
op|'('
name|'RackspaceApiEndpoint'
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
name|'instdir'
op|'='
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'network'
op|'.'
name|'PublicNetworkController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|post
dedent|''
name|'def'
name|'post'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'path'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'             '
name|'return'
name|'self'
op|'.'
name|'launch_server'
op|'('
name|'env'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'path_parts'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'delete_server'
op|'('
name|'path_parts'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|'"202 Accepted"'
op|','
op|'['
op|']'
op|','
string|'""'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|'"404 Not Found"'
op|','
op|'['
op|']'
op|','
nl|'\n'
string|'"Did not find image, or it was not in a running state"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|index
dedent|''
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'detail'
op|'('
name|'env'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'args'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
op|'{'
string|'"servers"'
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
name|'for'
name|'inst'
name|'in'
name|'self'
op|'.'
name|'instdir'
op|'.'
name|'all'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'['
string|'"servers"'
op|']'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'instance_details'
op|'('
name|'inst'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
comment|'##'
nl|'\n'
comment|'##'
nl|'\n'
nl|'\n'
DECL|member|launch_server
dedent|''
name|'def'
name|'launch_server'
op|'('
name|'self'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'env'
op|'['
string|"'wsgi.input'"
op|']'
op|'.'
name|'read'
op|'('
name|'int'
op|'('
name|'env'
op|'['
string|"'CONTENT_LENGTH'"
op|']'
op|')'
op|')'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'self'
op|'.'
name|'build_server_instance'
op|'('
name|'data'
op|','
name|'env'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'schedule_launch_of_instance'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|'"server"'
op|':'
name|'self'
op|'.'
name|'instance_details'
op|'('
name|'inst'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_details
dedent|''
name|'def'
name|'instance_details'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"instance_id"'
op|','
name|'None'
op|')'
op|','
nl|'\n'
string|'"imageId"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"image_id"'
op|','
name|'None'
op|')'
op|','
nl|'\n'
string|'"flavorId"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"instacne_type"'
op|','
name|'None'
op|')'
op|','
nl|'\n'
string|'"hostId"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"node_name"'
op|','
name|'None'
op|')'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"state"'
op|','
string|'"pending"'
op|')'
op|','
nl|'\n'
string|'"addresses"'
op|':'
op|'{'
nl|'\n'
string|'"public"'
op|':'
op|'['
name|'self'
op|'.'
name|'network'
op|'.'
name|'get_public_ip_for_instance'
op|'('
nl|'\n'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"instance_id"'
op|','
name|'None'
op|')'
nl|'\n'
op|')'
op|']'
op|','
nl|'\n'
string|'"private"'
op|':'
op|'['
name|'inst'
op|'.'
name|'get'
op|'('
string|'"private_dns_name"'
op|','
name|'None'
op|')'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
nl|'\n'
comment|'# implemented only by Rackspace, not AWS'
nl|'\n'
string|'"name"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|'"name"'
op|','
string|'"Not-Specified"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# not supported'
nl|'\n'
string|'"progress"'
op|':'
string|'"Not-Supported"'
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
nl|'\n'
string|'"Server Label"'
op|':'
string|'"Not-Supported"'
op|','
nl|'\n'
string|'"Image Version"'
op|':'
string|'"Not-Supported"'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|build_server_instance
dedent|''
name|'def'
name|'build_server_instance'
op|'('
name|'self'
op|','
name|'env'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'reservation'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
newline|'\n'
name|'ltime'
op|'='
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'self'
op|'.'
name|'instdir'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'name'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'imageId'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'flavorId'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'context'
op|'['
string|"'user'"
op|']'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'context'
op|'['
string|"'project'"
op|']'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
name|'reservation'
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
name|'ltime'
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'address'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
name|'mac'
op|'='
name|'inst'
op|'['
string|"'mac_address'"
op|']'
nl|'\n'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'private_dns_name'"
op|']'
op|'='
name|'str'
op|'('
name|'address'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'bridge_name'"
op|']'
op|'='
name|'network'
op|'.'
name|'BridgedNetwork'
op|'.'
name|'get_network_for_project'
op|'('
nl|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'default'"
comment|'# security group'
nl|'\n'
op|')'
op|'['
string|"'bridge_name'"
op|']'
newline|'\n'
comment|'# key_data, key_name, ami_launch_index'
nl|'\n'
comment|'# TODO(todd): key data or root password'
nl|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
DECL|member|schedule_launch_of_instance
dedent|''
name|'def'
name|'schedule_launch_of_instance'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'cast'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"method"'
op|':'
string|'"run_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'inst'
op|'.'
name|'instance_id'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_server
dedent|''
name|'def'
name|'delete_server'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'owner_hostname'
op|'='
name|'self'
op|'.'
name|'host_for_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
comment|"# it isn't launched?"
nl|'\n'
name|'if'
name|'not'
name|'owner_hostname'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'rpc_transport'
op|'='
string|'"%s:%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'owner_hostname'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'rpc_transport'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"reboot_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance_id'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|host_for_instance
dedent|''
name|'def'
name|'host_for_instance'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'model'
op|'.'
name|'Instance'
op|'.'
name|'lookup'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'instance'
op|'['
string|'"node_name"'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
