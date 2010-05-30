begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'#'
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
string|'"""\nImplementation of an S3-like storage server based on local files.\n\nUseful to test features that will eventually run on S3, or if you want to\nrun something locally that was once running on S3.\n\nWe don\'t support all the features of S3, but it does work with the\nstandard S3 client for the most basic semantics. To use the standard\nS3 client with this module::\n\n    c = S3.AWSAuthConnection("", "", server="localhost", port=8888,\n                             is_secure=False)\n    c.create_bucket("mybucket")\n    c.put("mybucket", "mykey", "a value")\n    print c.get("mybucket", "mykey").body\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'urllib'
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
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'from'
name|'tornado'
name|'import'
name|'escape'
op|','
name|'web'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'bucket'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'image'
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
nl|'\n'
nl|'\n'
DECL|function|catch_nova_exceptions
name|'def'
name|'catch_nova_exceptions'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
comment|'# FIXME: find a way to wrap all handlers in the web.Application.__init__ ?'
nl|'\n'
DECL|function|wrapper
indent|'    '
name|'def'
name|'wrapper'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'target'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'404'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Application
dedent|''
name|'class'
name|'Application'
op|'('
name|'web'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implementation of an S3-like storage server based on local files."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'user_manager'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'web'
op|'.'
name|'Application'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'['
nl|'\n'
op|'('
string|'r"/"'
op|','
name|'RootHandler'
op|')'
op|','
nl|'\n'
op|'('
string|'r"/_images/"'
op|','
name|'ImageHandler'
op|')'
op|','
nl|'\n'
op|'('
string|'r"/([^/]+)/(.+)"'
op|','
name|'ObjectHandler'
op|')'
op|','
nl|'\n'
op|'('
string|'r"/([^/]+)/"'
op|','
name|'BucketHandler'
op|')'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'buckets_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'FLAGS'
op|'.'
name|'buckets_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'images_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'buckets_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"buckets_path does not exist"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'images_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"images_path does not exist"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'user_manager'
op|'='
name|'user_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseRequestHandler
dedent|''
dedent|''
name|'class'
name|'BaseRequestHandler'
op|'('
name|'web'
op|'.'
name|'RequestHandler'
op|')'
op|':'
newline|'\n'
DECL|variable|SUPPORTED_METHODS
indent|'    '
name|'SUPPORTED_METHODS'
op|'='
op|'('
string|'"PUT"'
op|','
string|'"GET"'
op|','
string|'"DELETE"'
op|','
string|'"HEAD"'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|context
name|'def'
name|'context'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'self'
op|','
string|"'_context'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|"# Authorization Header format: 'AWS <access>:<secret>'"
nl|'\n'
indent|'                '
name|'access'
op|','
name|'sep'
op|','
name|'secret'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'Authorization'"
op|']'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'rpartition'
op|'('
string|"':'"
op|')'
newline|'\n'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|'='
name|'self'
op|'.'
name|'application'
op|'.'
name|'user_manager'
op|'.'
name|'authenticate'
op|'('
name|'access'
op|','
name|'secret'
op|','
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'request'
op|'.'
name|'method'
op|','
name|'self'
op|'.'
name|'request'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'request'
op|'.'
name|'path'
op|','
name|'False'
op|')'
newline|'\n'
comment|'# FIXME: check signature here!'
nl|'\n'
name|'self'
op|'.'
name|'_context'
op|'='
name|'api'
op|'.'
name|'APIRequestContext'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Error'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Authentication Failure: %s"'
op|'%'
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_context'
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
name|'escape'
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
name|'escape'
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
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'escape'
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
name|'escape'
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
name|'escape'
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
DECL|member|head
dedent|''
dedent|''
name|'def'
name|'head'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'buckets'
op|'='
op|'['
name|'b'
name|'for'
name|'b'
name|'in'
name|'bucket'
op|'.'
name|'Bucket'
op|'.'
name|'all'
op|'('
op|')'
name|'if'
name|'b'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|']'
newline|'\n'
nl|'\n'
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
op|'['
name|'b'
op|'.'
name|'metadata'
name|'for'
name|'b'
name|'in'
name|'buckets'
op|']'
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
indent|'    '
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|get
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"List keys for bucket %s"'
op|'%'
op|'('
name|'bucket_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
number|'1000'
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
nl|'\n'
name|'results'
op|'='
name|'bucket_object'
op|'.'
name|'list_keys'
op|'('
name|'prefix'
op|'='
name|'prefix'
op|','
name|'marker'
op|'='
name|'marker'
op|','
name|'max_keys'
op|'='
name|'max_keys'
op|','
name|'terse'
op|'='
name|'terse'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'render_xml'
op|'('
op|'{'
string|'"ListBucketResult"'
op|':'
name|'results'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|put
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Creating bucket %s"'
op|'%'
op|'('
name|'bucket_name'
op|')'
op|')'
newline|'\n'
name|'bucket'
op|'.'
name|'Bucket'
op|'.'
name|'create'
op|'('
name|'bucket_name'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|delete
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Deleting bucket %s"'
op|'%'
op|'('
name|'bucket_name'
op|')'
op|')'
newline|'\n'
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bucket_object'
op|'.'
name|'delete'
op|'('
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
indent|'    '
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'bucket_name'
op|','
name|'object_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Getting object: %s / %s"'
op|'%'
op|'('
name|'bucket_name'
op|','
name|'object_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'obj'
op|'='
name|'bucket_object'
op|'['
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'object_name'
op|')'
op|']'
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
name|'obj'
op|'.'
name|'mtime'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|'"Etag"'
op|','
string|'\'"\''
op|'+'
name|'obj'
op|'.'
name|'md5'
op|'+'
string|'\'"\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
name|'obj'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|put
name|'def'
name|'put'
op|'('
name|'self'
op|','
name|'bucket_name'
op|','
name|'object_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Putting object: %s / %s"'
op|'%'
op|'('
name|'bucket_name'
op|','
name|'object_name'
op|')'
op|')'
newline|'\n'
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'key'
op|'='
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'object_name'
op|')'
newline|'\n'
name|'bucket_object'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'body'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|'"Etag"'
op|','
string|'\'"\''
op|'+'
name|'bucket_object'
op|'['
name|'key'
op|']'
op|'.'
name|'md5'
op|'+'
string|'\'"\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'bucket_name'
op|','
name|'object_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Deleting object: %s / %s"'
op|'%'
op|'('
name|'bucket_name'
op|','
name|'object_name'
op|')'
op|')'
newline|'\n'
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'del'
name|'bucket_object'
op|'['
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'object_name'
op|')'
op|']'
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
DECL|class|ImageHandler
dedent|''
dedent|''
name|'class'
name|'ImageHandler'
op|'('
name|'BaseRequestHandler'
op|')'
op|':'
newline|'\n'
DECL|variable|SUPPORTED_METHODS
indent|'    '
name|'SUPPORTED_METHODS'
op|'='
op|'('
string|'"POST"'
op|','
string|'"PUT"'
op|','
string|'"GET"'
op|','
string|'"DELETE"'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" returns a json listing of all images\n            that a user has permissions to see """'
newline|'\n'
nl|'\n'
name|'images'
op|'='
op|'['
name|'i'
name|'for'
name|'i'
name|'in'
name|'image'
op|'.'
name|'Image'
op|'.'
name|'all'
op|'('
op|')'
name|'if'
name|'i'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
name|'json'
op|'.'
name|'dumps'
op|'('
op|'['
name|'i'
op|'.'
name|'metadata'
name|'for'
name|'i'
name|'in'
name|'images'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|put
name|'def'
name|'put'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" create a new registered image """'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|"'image_id'"
op|','
string|"u''"
op|')'
newline|'\n'
name|'image_location'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|"'image_location'"
op|','
string|"u''"
op|')'
newline|'\n'
nl|'\n'
name|'image_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'image_path'
op|'.'
name|'startswith'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|')'
name|'or'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'image_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'image_location'
op|'.'
name|'split'
op|'('
string|'"/"'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'manifest'
op|'='
name|'image_location'
op|'['
name|'len'
op|'('
name|'image_location'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
number|'0'
op|']'
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'p'
op|'='
name|'multiprocessing'
op|'.'
name|'Process'
op|'('
name|'target'
op|'='
name|'image'
op|'.'
name|'Image'
op|'.'
name|'create'
op|','
name|'args'
op|'='
nl|'\n'
op|'('
name|'image_id'
op|','
name|'image_location'
op|','
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|post
name|'def'
name|'post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" update image attributes: public/private """'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|"'image_id'"
op|','
string|"u''"
op|')'
newline|'\n'
name|'operation'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|"'operation'"
op|','
string|"u''"
op|')'
newline|'\n'
nl|'\n'
name|'image_object'
op|'='
name|'image'
op|'.'
name|'Image'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_object'
op|'.'
name|'set_public'
op|'('
name|'operation'
op|'=='
string|"'add'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'catch_nova_exceptions'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" delete a registered image """'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|'"image_id"'
op|','
string|'u""'
op|')'
newline|'\n'
name|'image_object'
op|'='
name|'image'
op|'.'
name|'Image'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image'
op|'.'
name|'is_authorized'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_object'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'set_status'
op|'('
number|'204'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
