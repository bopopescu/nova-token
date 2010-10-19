begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2010 OpenStack LLC.'
nl|'\n'
comment|'#    Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'#    Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'#    All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2009 Facebook'
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
string|'"""\nImplementation of an S3-like storage server based on local files.\n\nUseful to test features that will eventually run on S3, or if you want to\nrun something locally that was once running on S3.\n\nWe don\'t support all the features of S3, but it does work with the\nstandard S3 client for the most basic semantics. To use the standard\nS3 client with this module::\n\n    c = S3.AWSAuthConnection("", "", server="localhost", port=8888,\n                             is_secure=False)\n    c.create_bucket("mybucket")\n    c.put("mybucket", "mykey", "a value")\n    print c.get("mybucket", "mykey").body\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
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
name|'urllib'
newline|'\n'
nl|'\n'
name|'from'
name|'tornado'
name|'import'
name|'escape'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'internet'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'error'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'resource'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'server'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'static'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'auth'
name|'import'
name|'manager'
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
DECL|function|render_xml
name|'def'
name|'render_xml'
op|'('
name|'request'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Writes value as XML string to request"""'
newline|'\n'
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
name|'request'
op|'.'
name|'setHeader'
op|'('
string|'"Content-Type"'
op|','
string|'"application/xml; charset=UTF-8"'
op|')'
newline|'\n'
nl|'\n'
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
name|'request'
op|'.'
name|'write'
op|'('
string|'\'<?xml version="1.0" encoding="UTF-8"?>\\n\''
op|')'
newline|'\n'
name|'request'
op|'.'
name|'write'
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
name|'request'
op|'.'
name|'write'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'write'
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
name|'request'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|finish
dedent|''
name|'def'
name|'finish'
op|'('
name|'request'
op|','
name|'content'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Finalizer method for request"""'
newline|'\n'
name|'if'
name|'content'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'.'
name|'write'
op|'('
name|'content'
op|')'
newline|'\n'
dedent|''
name|'request'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_render_parts
dedent|''
name|'def'
name|'_render_parts'
op|'('
name|'value'
op|','
name|'write_cb'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper method to render different Python objects to XML"""'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'write_cb'
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
indent|'        '
name|'write_cb'
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
indent|'        '
name|'write_cb'
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
indent|'        '
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
indent|'            '
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
indent|'                '
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
indent|'                '
name|'write_cb'
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
name|'_render_parts'
op|'('
name|'subsubvalue'
op|','
name|'write_cb'
op|')'
newline|'\n'
name|'write_cb'
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
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"Unknown S3 value type %r"'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_argument
dedent|''
dedent|''
name|'def'
name|'get_argument'
op|'('
name|'request'
op|','
name|'key'
op|','
name|'default_value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the request\'s value at key, or default_value\n    if not found\n    """'
newline|'\n'
name|'if'
name|'key'
name|'in'
name|'request'
op|'.'
name|'args'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'request'
op|'.'
name|'args'
op|'['
name|'key'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'default_value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_context
dedent|''
name|'def'
name|'get_context'
op|'('
name|'request'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the supplied request\'s context object"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|"# Authorization Header format: 'AWS <access>:<secret>'"
nl|'\n'
indent|'        '
name|'authorization_header'
op|'='
name|'request'
op|'.'
name|'getHeader'
op|'('
string|"'Authorization'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'authorization_header'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
dedent|''
name|'auth_header_value'
op|'='
name|'authorization_header'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'access'
op|','
name|'_ignored'
op|','
name|'secret'
op|'='
name|'auth_header_value'
op|'.'
name|'rpartition'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'am'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|'='
name|'am'
op|'.'
name|'authenticate'
op|'('
name|'access'
op|','
nl|'\n'
name|'secret'
op|','
nl|'\n'
op|'{'
op|'}'
op|','
nl|'\n'
name|'request'
op|'.'
name|'method'
op|','
nl|'\n'
name|'request'
op|'.'
name|'getRequestHostname'
op|'('
op|')'
op|','
nl|'\n'
name|'request'
op|'.'
name|'uri'
op|','
nl|'\n'
name|'headers'
op|'='
name|'request'
op|'.'
name|'getAllHeaders'
op|'('
op|')'
op|','
nl|'\n'
name|'check_type'
op|'='
string|"'s3'"
op|')'
newline|'\n'
name|'return'
name|'context'
op|'.'
name|'RequestContext'
op|'('
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
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Authentication Failure: %s"'
op|','
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|ErrorHandlingResource
dedent|''
dedent|''
name|'class'
name|'ErrorHandlingResource'
op|'('
name|'resource'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps exceptions to 404 / 401 codes.  Won\'t work for\n    exceptions thrown after NOT_DONE_YET is returned.\n    """'
newline|'\n'
comment|'# TODO(unassigned) (calling-all-twisted-experts): This needs to be'
nl|'\n'
comment|'#                   plugged in to the right place in twisted...'
nl|'\n'
comment|"#                   This doesn't look like it's the right place"
nl|'\n'
comment|'#                   (consider exceptions in getChild; or after'
nl|'\n'
comment|'#                   NOT_DONE_YET is returned'
nl|'\n'
DECL|member|render
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Renders the response as XML"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'resource'
op|'.'
name|'Resource'
op|'.'
name|'render'
op|'('
name|'self'
op|','
name|'request'
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
name|'request'
op|'.'
name|'setResponseCode'
op|'('
number|'404'
op|')'
newline|'\n'
name|'return'
string|"''"
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'request'
op|'.'
name|'setResponseCode'
op|'('
number|'403'
op|')'
newline|'\n'
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|S3
dedent|''
dedent|''
dedent|''
name|'class'
name|'S3'
op|'('
name|'ErrorHandlingResource'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ErrorHandlingResource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getChild
dedent|''
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'request'
op|')'
op|':'
comment|'# pylint: disable-msg=C0103'
newline|'\n'
indent|'        '
string|'"""Returns either the image or bucket resource"""'
newline|'\n'
name|'request'
op|'.'
name|'context'
op|'='
name|'get_context'
op|'('
name|'request'
op|')'
newline|'\n'
name|'if'
name|'name'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'_images'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'ImagesResource'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'BucketResource'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|render_GET
dedent|''
dedent|''
name|'def'
name|'render_GET'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
comment|'# pylint: disable-msg=R0201'
newline|'\n'
indent|'        '
string|'"""Renders the GET request for a list of buckets as XML"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'List of buckets requested'"
op|')'
newline|'\n'
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
name|'request'
op|'.'
name|'context'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'render_xml'
op|'('
name|'request'
op|','
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
name|'return'
name|'server'
op|'.'
name|'NOT_DONE_YET'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BucketResource
dedent|''
dedent|''
name|'class'
name|'BucketResource'
op|'('
name|'ErrorHandlingResource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A web resource containing an S3-like bucket"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
nl|'\n'
DECL|member|getChild
dedent|''
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the bucket resource itself, or the object resource\n        the bucket contains if a name is supplied\n        """'
newline|'\n'
name|'if'
name|'name'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'ObjectResource'
op|'('
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|render_GET
dedent|''
dedent|''
name|'def'
name|'render_GET'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Returns the keys for the bucket resource"'
string|'""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"List keys for bucket %s"'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'self'
op|'.'
name|'name'
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
name|'return'
name|'error'
op|'.'
name|'NoResource'
op|'('
name|'message'
op|'='
string|'"No such bucket"'
op|')'
op|'.'
name|'render'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'prefix'
op|'='
name|'get_argument'
op|'('
name|'request'
op|','
string|'"prefix"'
op|','
string|'u""'
op|')'
newline|'\n'
name|'marker'
op|'='
name|'get_argument'
op|'('
name|'request'
op|','
string|'"marker"'
op|','
string|'u""'
op|')'
newline|'\n'
name|'max_keys'
op|'='
name|'int'
op|'('
name|'get_argument'
op|'('
name|'request'
op|','
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
name|'get_argument'
op|'('
name|'request'
op|','
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
nl|'\n'
name|'marker'
op|'='
name|'marker'
op|','
nl|'\n'
name|'max_keys'
op|'='
name|'max_keys'
op|','
nl|'\n'
name|'terse'
op|'='
name|'terse'
op|')'
newline|'\n'
name|'render_xml'
op|'('
name|'request'
op|','
op|'{'
string|'"ListBucketResult"'
op|':'
name|'results'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'server'
op|'.'
name|'NOT_DONE_YET'
newline|'\n'
nl|'\n'
DECL|member|render_PUT
dedent|''
name|'def'
name|'render_PUT'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Creates the bucket resource"'
string|'""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Creating bucket %s"'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"calling bucket.Bucket.create(%r, %r)"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'name'
op|','
nl|'\n'
name|'request'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'bucket'
op|'.'
name|'Bucket'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'request'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
name|'return'
name|'server'
op|'.'
name|'NOT_DONE_YET'
newline|'\n'
nl|'\n'
DECL|member|render_DELETE
dedent|''
name|'def'
name|'render_DELETE'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the bucket resource"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Deleting bucket %s"'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'bucket_object'
op|'='
name|'bucket'
op|'.'
name|'Bucket'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
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
name|'request'
op|'.'
name|'setResponseCode'
op|'('
number|'204'
op|')'
newline|'\n'
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ObjectResource
dedent|''
dedent|''
name|'class'
name|'ObjectResource'
op|'('
name|'ErrorHandlingResource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The resource returned from a bucket"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'bucket'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'bucket'
op|'='
name|'bucket'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
nl|'\n'
DECL|member|render_GET
dedent|''
name|'def'
name|'render_GET'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the object\n\n        Raises NotAuthorized if user in request context is not\n        authorized to delete the object.\n        """'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Getting object: %s / %s"'
op|','
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'obj'
op|'='
name|'self'
op|'.'
name|'bucket'
op|'['
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
op|']'
newline|'\n'
name|'request'
op|'.'
name|'setHeader'
op|'('
string|'"Content-Type"'
op|','
string|'"application/unknown"'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'setHeader'
op|'('
string|'"Last-Modified"'
op|','
nl|'\n'
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
name|'request'
op|'.'
name|'setHeader'
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
name|'return'
name|'static'
op|'.'
name|'File'
op|'('
name|'obj'
op|'.'
name|'path'
op|')'
op|'.'
name|'render_GET'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|render_PUT
dedent|''
name|'def'
name|'render_PUT'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Modifies/inserts the object and returns a result code\n\n        Raises NotAuthorized if user in request context is not\n        authorized to delete the object.\n        """'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Putting object: %s / %s"'
op|','
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
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
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'content'
op|'.'
name|'seek'
op|'('
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'bucket'
op|'['
name|'key'
op|']'
op|'='
name|'request'
op|'.'
name|'content'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'request'
op|'.'
name|'setHeader'
op|'('
string|'"Etag"'
op|','
string|'\'"\''
op|'+'
name|'self'
op|'.'
name|'bucket'
op|'['
name|'key'
op|']'
op|'.'
name|'md5'
op|'+'
string|'\'"\''
op|')'
newline|'\n'
name|'finish'
op|'('
name|'request'
op|')'
newline|'\n'
name|'return'
name|'server'
op|'.'
name|'NOT_DONE_YET'
newline|'\n'
nl|'\n'
DECL|member|render_DELETE
dedent|''
name|'def'
name|'render_DELETE'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the object and returns a result code\n\n        Raises NotAuthorized if user in request context is not\n        authorized to delete the object.\n        """'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Deleting object: %s / %s"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'del'
name|'self'
op|'.'
name|'bucket'
op|'['
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
op|']'
newline|'\n'
name|'request'
op|'.'
name|'setResponseCode'
op|'('
number|'204'
op|')'
newline|'\n'
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageResource
dedent|''
dedent|''
name|'class'
name|'ImageResource'
op|'('
name|'ErrorHandlingResource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A web resource representing a single image"""'
newline|'\n'
DECL|variable|isLeaf
name|'isLeaf'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'img'
op|'='
name|'image'
op|'.'
name|'Image'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|render_GET
dedent|''
name|'def'
name|'render_GET'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the image file"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'img'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|','
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'static'
op|'.'
name|'File'
op|'('
name|'self'
op|'.'
name|'img'
op|'.'
name|'image_path'
op|','
nl|'\n'
name|'defaultType'
op|'='
string|"'application/octet-stream'"
nl|'\n'
op|')'
op|'.'
name|'render_GET'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|class|ImagesResource
dedent|''
dedent|''
name|'class'
name|'ImagesResource'
op|'('
name|'resource'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A web resource representing a list of images"""'
newline|'\n'
DECL|member|getChild
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'_request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns itself or an ImageResource if no name given"""'
newline|'\n'
name|'if'
name|'name'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'ImageResource'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|render_GET
dedent|''
dedent|''
name|'def'
name|'render_GET'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
comment|'# pylint: disable-msg=R0201'
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
name|'request'
op|'.'
name|'context'
op|','
name|'readonly'
op|'='
name|'True'
op|')'
op|']'
newline|'\n'
nl|'\n'
comment|'# Bug #617776:'
nl|'\n'
comment|"# We used to have 'type' in the image metadata, but this field"
nl|'\n'
comment|"# should be called 'imageType', as per the EC2 specification."
nl|'\n'
comment|'# For compat with old metadata files we copy type to imageType if'
nl|'\n'
comment|'# imageType is not present.'
nl|'\n'
comment|'# For compat with euca2ools (and any other clients using the'
nl|'\n'
comment|'# incorrect name) we copy imageType to type.'
nl|'\n'
comment|'# imageType is primary if we end up with both in the metadata file'
nl|'\n'
comment|'# (which should never happen).'
nl|'\n'
DECL|function|decorate
name|'def'
name|'decorate'
op|'('
name|'m'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'imageType'"
name|'not'
name|'in'
name|'m'
name|'and'
string|"'type'"
name|'in'
name|'m'
op|':'
newline|'\n'
indent|'                '
name|'m'
op|'['
string|"u'imageType'"
op|']'
op|'='
name|'m'
op|'['
string|"'type'"
op|']'
newline|'\n'
dedent|''
name|'elif'
string|"'imageType'"
name|'in'
name|'m'
op|':'
newline|'\n'
indent|'                '
name|'m'
op|'['
string|"u'type'"
op|']'
op|'='
name|'m'
op|'['
string|"'imageType'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'displayName'"
name|'not'
name|'in'
name|'m'
op|':'
newline|'\n'
indent|'                '
name|'m'
op|'['
string|"u'displayName'"
op|']'
op|'='
string|"u''"
newline|'\n'
dedent|''
name|'return'
name|'m'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'.'
name|'write'
op|'('
name|'json'
op|'.'
name|'dumps'
op|'('
op|'['
name|'decorate'
op|'('
name|'i'
op|'.'
name|'metadata'
op|')'
name|'for'
name|'i'
name|'in'
name|'images'
op|']'
op|')'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
name|'return'
name|'server'
op|'.'
name|'NOT_DONE_YET'
newline|'\n'
nl|'\n'
DECL|member|render_PUT
dedent|''
name|'def'
name|'render_PUT'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
comment|'# pylint: disable-msg=R0201'
newline|'\n'
indent|'        '
string|'""" create a new registered image """'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'get_argument'
op|'('
name|'request'
op|','
string|"'image_id'"
op|','
string|"u''"
op|')'
newline|'\n'
name|'image_location'
op|'='
name|'get_argument'
op|'('
name|'request'
op|','
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
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
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
nl|'\n'
name|'if'
name|'not'
name|'bucket_object'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
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
name|'register_aws_image'
op|','
nl|'\n'
name|'args'
op|'='
op|'('
name|'image_id'
op|','
name|'image_location'
op|','
name|'request'
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
name|'return'
string|"''"
newline|'\n'
nl|'\n'
DECL|member|render_POST
dedent|''
name|'def'
name|'render_POST'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
comment|'# pylint: disable-msg=R0201'
newline|'\n'
indent|'        '
string|'"""Update image attributes: public/private"""'
newline|'\n'
nl|'\n'
comment|'# image_id required for all requests'
nl|'\n'
name|'image_id'
op|'='
name|'get_argument'
op|'('
name|'request'
op|','
string|"'image_id'"
op|','
string|"u''"
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
name|'if'
name|'not'
name|'image_object'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"not authorized for render_POST in images"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'operation'
op|'='
name|'get_argument'
op|'('
name|'request'
op|','
string|"'operation'"
op|','
string|"u''"
op|')'
newline|'\n'
name|'if'
name|'operation'
op|':'
newline|'\n'
comment|'# operation implies publicity toggle'
nl|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"handling publicity toggle"'
op|')'
newline|'\n'
name|'image_object'
op|'.'
name|'set_public'
op|'('
name|'operation'
op|'=='
string|"'add'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# other attributes imply update'
nl|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"update user fields"'
op|')'
newline|'\n'
name|'clean_args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'arg'
name|'in'
name|'request'
op|'.'
name|'args'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'clean_args'
op|'['
name|'arg'
op|']'
op|'='
name|'request'
op|'.'
name|'args'
op|'['
name|'arg'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'image_object'
op|'.'
name|'update_user_editable_fields'
op|'('
name|'clean_args'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"''"
newline|'\n'
nl|'\n'
DECL|member|render_DELETE
dedent|''
name|'def'
name|'render_DELETE'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
comment|'# pylint: disable-msg=R0201'
newline|'\n'
indent|'        '
string|'"""Delete a registered image"""'
newline|'\n'
name|'image_id'
op|'='
name|'get_argument'
op|'('
name|'request'
op|','
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
name|'image_object'
op|'.'
name|'is_authorized'
op|'('
name|'request'
op|'.'
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
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
name|'request'
op|'.'
name|'setResponseCode'
op|'('
number|'204'
op|')'
newline|'\n'
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_site
dedent|''
dedent|''
name|'def'
name|'get_site'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Support for WSGI-like interfaces"""'
newline|'\n'
name|'root'
op|'='
name|'S3'
op|'('
op|')'
newline|'\n'
name|'site'
op|'='
name|'server'
op|'.'
name|'Site'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'site'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_application
dedent|''
name|'def'
name|'get_application'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Support WSGI-like interfaces"""'
newline|'\n'
name|'factory'
op|'='
name|'get_site'
op|'('
op|')'
newline|'\n'
name|'application'
op|'='
name|'service'
op|'.'
name|'Application'
op|'('
string|'"objectstore"'
op|')'
newline|'\n'
comment|'# Disabled because of lack of proper introspection in Twisted'
nl|'\n'
comment|'# or possibly different versions of twisted?'
nl|'\n'
comment|'# pylint: disable-msg=E1101'
nl|'\n'
name|'objectStoreService'
op|'='
name|'internet'
op|'.'
name|'TCPServer'
op|'('
name|'FLAGS'
op|'.'
name|'s3_port'
op|','
name|'factory'
op|')'
newline|'\n'
name|'objectStoreService'
op|'.'
name|'setServiceParent'
op|'('
name|'application'
op|')'
newline|'\n'
name|'return'
name|'application'
newline|'\n'
dedent|''
endmarker|''
end_unit
