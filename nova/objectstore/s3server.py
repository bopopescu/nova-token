begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2009 Facebook'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
string|'"""Implementation of an S3-like storage server based on local files.\n\nUseful to test features that will eventually run on S3, or if you want to\nrun something locally that was once running on S3.\n\nWe don\'t support all the features of S3, but it does work with the\nstandard S3 client for the most basic semantics. To use the standard\nS3 client with this module::\n\n    c = S3.AWSAuthConnection("", "", server="localhost", port=8888,\n                             is_secure=False)\n    c.create_bucket("mybucket")\n    c.put("mybucket", "mykey", "a value")\n    print c.get("mybucket", "mykey").body\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'bisect'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'urllib'
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
name|'routes'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|s3_opts
name|'s3_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'buckets_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'buckets'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'path to s3 buckets'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'s3_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"0.0.0.0"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address for S3 API to listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'s3_listen_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3333'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'port for s3 api to listen'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'s3_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_wsgi_server
name|'def'
name|'get_wsgi_server'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"S3 Objectstore"'
op|','
nl|'\n'
name|'S3Application'
op|'('
name|'CONF'
op|'.'
name|'buckets_path'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
name|'CONF'
op|'.'
name|'s3_listen_port'
op|','
nl|'\n'
name|'host'
op|'='
name|'CONF'
op|'.'
name|'s3_listen'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|S3Application
dedent|''
name|'class'
name|'S3Application'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implementation of an S3-like storage server based on local files.\n\n    If bucket depth is given, we break files up into multiple directories\n    to prevent hitting file system limits for number of files in each\n    directories. 1 means one level of directories, 2 means 2, etc.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'root_directory'
op|','
name|'bucket_depth'
op|'='
number|'0'
op|','
name|'mapper'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'mapper'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mapper'
op|'.'
name|'connect'
op|'('
string|"'/'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
name|'RootHandler'
op|'('
name|'self'
op|')'
op|'('
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|"'/{bucket}/{object_name}'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
name|'ObjectHandler'
op|'('
name|'self'
op|')'
op|'('
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|"'/{bucket_name}/'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
name|'BucketHandler'
op|'('
name|'self'
op|')'
op|'('
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'directory'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'root_directory'
op|')'
newline|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'self'
op|'.'
name|'directory'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'bucket_depth'
op|'='
name|'bucket_depth'
newline|'\n'
name|'super'
op|'('
name|'S3Application'
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
nl|'\n'
DECL|class|BaseRequestHandler
dedent|''
dedent|''
name|'class'
name|'BaseRequestHandler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class emulating Tornado\'s web framework pattern in WSGI.\n\n    This is a direct port of Tornado\'s implementation, so some key decisions\n    about how the code interacts have already been chosen.\n\n    The two most common ways of designing web frameworks can be\n    classified as async object-oriented and sync functional.\n\n    Tornado\'s is on the OO side because a response is built up in and using\n    the shared state of an object and one of the object\'s methods will\n    eventually trigger the "finishing" of the response asynchronously.\n\n    Most WSGI stuff is in the functional side, we pass a request object to\n    every call down a chain and the eventual return value will be a response.\n\n    Part of the function of the routing code in S3Application as well as the\n    code in BaseRequestHandler\'s __call__ method is to merge those two styles\n    together enough that the Tornado code can work without extensive\n    modifications.\n\n    To do that it needs to give the Tornado-style code clean objects that it\n    can modify the state of for each request that is processed, so we use a\n    very simple factory lambda to create new state for each request, that\'s\n    the stuff in the router, and when we let the Tornado code modify that\n    object to handle the request, then we return the response it generated.\n    This wouldn\'t work the same if Tornado was being more async\'y and doing\n    other callbacks throughout the process, but since Tornado is being\n    relatively simple here we can be satisfied that the response will be\n    complete by the end of the get/post method.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
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
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'method'
op|'='
name|'request'
op|'.'
name|'method'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'f'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'self'
op|'.'
name|'invalid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'='
name|'request'
newline|'\n'
name|'self'
op|'.'
name|'response'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'params'
op|'='
name|'request'
op|'.'
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'del'
name|'params'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'f'
op|'('
op|'**'
name|'params'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|get_argument
dedent|''
name|'def'
name|'get_argument'
op|'('
name|'self'
op|','
name|'arg'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'request'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
name|'arg'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_header
dedent|''
name|'def'
name|'set_header'
op|'('
name|'self'
op|','
name|'header'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'response'
op|'.'
name|'headers'
op|'['
name|'header'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|set_status
dedent|''
name|'def'
name|'set_status'
op|'('
name|'self'
op|','
name|'status_code'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'response'
op|'.'
name|'status'
op|'='
name|'status_code'
newline|'\n'
nl|'\n'
DECL|member|finish
dedent|''
name|'def'
name|'finish'
op|'('
name|'self'
op|','
name|'body'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'response'
op|'.'
name|'body'
op|'='
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|invalid
dedent|''
name|'def'
name|'invalid'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|render_xml
dedent|''
name|'def'
name|'render_xml'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'assert'
name|'isinstance'
op|'('
name|'value'
op|','
name|'dict'
op|')'
name|'and'
name|'len'
op|'('
name|'value'
op|')'
op|'=='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|'"Content-Type"'
op|','
string|'"application/xml; charset=UTF-8"'
op|')'
newline|'\n'
name|'name'
op|'='
name|'value'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'parts'
op|'='
op|'['
op|']'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
string|"'<'"
op|'+'
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'name'
op|')'
op|'+'
nl|'\n'
string|'\' xmlns="http://doc.s3.amazonaws.com/2006-03-01">\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_render_parts'
op|'('
name|'value'
op|'.'
name|'values'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|','
name|'parts'
op|')'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
string|"'</'"
op|'+'
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'name'
op|')'
op|'+'
string|"'>'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
string|'\'<?xml version="1.0" encoding="UTF-8"?>\\n\''
op|'+'
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
name|'parts'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_render_parts
dedent|''
name|'def'
name|'_render_parts'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'parts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'parts'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
name|'utils'
op|'.'
name|'xhtml_escape'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'value'
op|','
name|'int'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'value'
op|','
name|'long'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
name|'str'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'value'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
name|'value'
op|'.'
name|'strftime'
op|'('
string|'"%Y-%m-%dT%H:%M:%S.000Z"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'value'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'name'
op|','
name|'subvalue'
name|'in'
name|'value'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'subvalue'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'subvalue'
op|'='
op|'['
name|'subvalue'
op|']'
newline|'\n'
dedent|''
name|'for'
name|'subsubvalue'
name|'in'
name|'subvalue'
op|':'
newline|'\n'
indent|'                    '
name|'parts'
op|'.'
name|'append'
op|'('
string|"'<'"
op|'+'
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'name'
op|')'
op|'+'
string|"'>'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_render_parts'
op|'('
name|'subsubvalue'
op|','
name|'parts'
op|')'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
string|"'</'"
op|'+'
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'name'
op|')'
op|'+'
string|"'>'"
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Unknown S3 value type %r"'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_object_path
dedent|''
dedent|''
name|'def'
name|'_object_path'
op|'('
name|'self'
op|','
name|'bucket'
op|','
name|'object_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'application'
op|'.'
name|'bucket_depth'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|','
name|'bucket'
op|','
name|'object_name'
op|')'
op|')'
newline|'\n'
dedent|''
name|'hash'
op|'='
name|'hashlib'
op|'.'
name|'md5'
op|'('
name|'object_name'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|','
name|'bucket'
op|')'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'bucket_depth'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
name|'hash'
op|'['
op|':'
number|'2'
op|'*'
op|'('
name|'i'
op|'+'
number|'1'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
name|'object_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RootHandler
dedent|''
dedent|''
name|'class'
name|'RootHandler'
op|'('
name|'BaseRequestHandler'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'    '
name|'def'
name|'get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'names'
op|'='
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|')'
newline|'\n'
name|'buckets'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'names'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|','
name|'name'
op|')'
newline|'\n'
name|'info'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'path'
op|')'
newline|'\n'
name|'buckets'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|'"Name"'
op|':'
name|'name'
op|','
nl|'\n'
string|'"CreationDate"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcfromtimestamp'
op|'('
nl|'\n'
name|'info'
op|'.'
name|'st_ctime'
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'render_xml'
op|'('
op|'{'
string|'"ListAllMyBucketsResult"'
op|':'
op|'{'
nl|'\n'
string|'"Buckets"'
op|':'
op|'{'
string|'"Bucket"'
op|':'
name|'buckets'
op|'}'
op|','
nl|'\n'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BucketHandler
dedent|''
dedent|''
name|'class'
name|'BucketHandler'
op|'('
name|'BaseRequestHandler'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'    '
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'bucket_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|'"prefix"'
op|','
string|'u""'
op|')'
newline|'\n'
name|'marker'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|'"marker"'
op|','
string|'u""'
op|')'
newline|'\n'
name|'max_keys'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'get_argument'
op|'('
string|'"max-keys"'
op|','
number|'50000'
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|','
nl|'\n'
name|'bucket_name'
op|')'
op|')'
newline|'\n'
name|'terse'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'get_argument'
op|'('
string|'"terse"'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|')'
name|'or'
nl|'\n'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'path'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'404'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'object_names'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'root'
op|','
name|'dirs'
op|','
name|'files'
name|'in'
name|'os'
op|'.'
name|'walk'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'file_name'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'                '
name|'object_names'
op|'.'
name|'append'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'file_name'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'skip'
op|'='
name|'len'
op|'('
name|'path'
op|')'
op|'+'
number|'1'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'bucket_depth'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'skip'
op|'+='
number|'2'
op|'*'
op|'('
name|'i'
op|'+'
number|'1'
op|')'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'object_names'
op|'='
op|'['
name|'n'
op|'['
name|'skip'
op|':'
op|']'
name|'for'
name|'n'
name|'in'
name|'object_names'
op|']'
newline|'\n'
name|'object_names'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'contents'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'start_pos'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'marker'
op|':'
newline|'\n'
indent|'            '
name|'start_pos'
op|'='
name|'bisect'
op|'.'
name|'bisect_right'
op|'('
name|'object_names'
op|','
name|'marker'
op|','
name|'start_pos'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'prefix'
op|':'
newline|'\n'
indent|'            '
name|'start_pos'
op|'='
name|'bisect'
op|'.'
name|'bisect_left'
op|'('
name|'object_names'
op|','
name|'prefix'
op|','
name|'start_pos'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'truncated'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'object_name'
name|'in'
name|'object_names'
op|'['
name|'start_pos'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'object_name'
op|'.'
name|'startswith'
op|'('
name|'prefix'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'contents'
op|')'
op|'>='
name|'max_keys'
op|':'
newline|'\n'
indent|'                '
name|'truncated'
op|'='
name|'True'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'object_path'
op|'='
name|'self'
op|'.'
name|'_object_path'
op|'('
name|'bucket_name'
op|','
name|'object_name'
op|')'
newline|'\n'
name|'c'
op|'='
op|'{'
string|'"Key"'
op|':'
name|'object_name'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'terse'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'object_path'
op|')'
newline|'\n'
name|'c'
op|'.'
name|'update'
op|'('
op|'{'
nl|'\n'
string|'"LastModified"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcfromtimestamp'
op|'('
nl|'\n'
name|'info'
op|'.'
name|'st_mtime'
op|')'
op|','
nl|'\n'
string|'"Size"'
op|':'
name|'info'
op|'.'
name|'st_size'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'contents'
op|'.'
name|'append'
op|'('
name|'c'
op|')'
newline|'\n'
name|'marker'
op|'='
name|'object_name'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'render_xml'
op|'('
op|'{'
string|'"ListBucketResult"'
op|':'
op|'{'
nl|'\n'
string|'"Name"'
op|':'
name|'bucket_name'
op|','
nl|'\n'
string|'"Prefix"'
op|':'
name|'prefix'
op|','
nl|'\n'
string|'"Marker"'
op|':'
name|'marker'
op|','
nl|'\n'
string|'"MaxKeys"'
op|':'
name|'max_keys'
op|','
nl|'\n'
string|'"IsTruncated"'
op|':'
name|'truncated'
op|','
nl|'\n'
string|'"Contents"'
op|':'
name|'contents'
op|','
nl|'\n'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|put
dedent|''
name|'def'
name|'put'
op|'('
name|'self'
op|','
name|'bucket_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|','
name|'bucket_name'
op|')'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|')'
name|'or'
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'403'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'bucket_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|','
name|'bucket_name'
op|')'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|')'
name|'or'
nl|'\n'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'path'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'404'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'os'
op|'.'
name|'listdir'
op|'('
name|'path'
op|')'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'403'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'os'
op|'.'
name|'rmdir'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_status'
op|'('
number|'204'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ObjectHandler
dedent|''
dedent|''
name|'class'
name|'ObjectHandler'
op|'('
name|'BaseRequestHandler'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'    '
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'bucket'
op|','
name|'object_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'object_name'
op|'='
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'object_name'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_object_path'
op|'('
name|'bucket'
op|','
name|'object_name'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|')'
name|'or'
nl|'\n'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'path'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'404'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'info'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|'"Content-Type"'
op|','
string|'"application/unknown"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|'"Last-Modified"'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcfromtimestamp'
op|'('
nl|'\n'
name|'info'
op|'.'
name|'st_mtime'
op|')'
op|')'
newline|'\n'
name|'object_file'
op|'='
name|'open'
op|'('
name|'path'
op|','
string|'"r"'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'finish'
op|'('
name|'object_file'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'object_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|put
dedent|''
dedent|''
name|'def'
name|'put'
op|'('
name|'self'
op|','
name|'bucket'
op|','
name|'object_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'object_name'
op|'='
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'object_name'
op|')'
newline|'\n'
name|'bucket_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|','
name|'bucket'
op|')'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'bucket_dir'
op|'.'
name|'startswith'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|')'
name|'or'
nl|'\n'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'bucket_dir'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'404'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'path'
op|'='
name|'self'
op|'.'
name|'_object_path'
op|'('
name|'bucket'
op|','
name|'object_name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'bucket_dir'
op|')'
name|'or'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'403'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'directory'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'path'
op|')'
newline|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'directory'
op|')'
newline|'\n'
name|'object_file'
op|'='
name|'open'
op|'('
name|'path'
op|','
string|'"w"'
op|')'
newline|'\n'
name|'object_file'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'request'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'object_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|"'ETag'"
op|','
nl|'\n'
string|'\'"%s"\''
op|'%'
name|'hashlib'
op|'.'
name|'md5'
op|'('
name|'self'
op|'.'
name|'request'
op|'.'
name|'body'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'bucket'
op|','
name|'object_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'object_name'
op|'='
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'object_name'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_object_path'
op|'('
name|'bucket'
op|','
name|'object_name'
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'self'
op|'.'
name|'application'
op|'.'
name|'directory'
op|')'
name|'or'
nl|'\n'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'path'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_status'
op|'('
number|'404'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_status'
op|'('
number|'204'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
