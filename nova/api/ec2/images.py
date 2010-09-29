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
string|'"""\nProxy AMI-related calls from the cloud controller, to the running\nobjectstore service.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'import'
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
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
DECL|function|modify
name|'def'
name|'modify'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'operation'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'POST'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'qs'
op|'('
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
string|"'operation'"
op|':'
name|'operation'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|function|update
dedent|''
name|'def'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'attributes'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""update an image\'s attributes / info.json"""'
newline|'\n'
name|'attributes'
op|'.'
name|'update'
op|'('
op|'{'
string|'"image_id"'
op|':'
name|'image_id'
op|'}'
op|')'
newline|'\n'
name|'conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'POST'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'qs'
op|'('
name|'attributes'
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|function|register
dedent|''
name|'def'
name|'register'
op|'('
name|'context'
op|','
name|'image_location'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" rpc call to register a new image based from a manifest """'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'ami'"
op|')'
newline|'\n'
name|'conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'PUT'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'qs'
op|'('
op|'{'
string|"'image_location'"
op|':'
name|'image_location'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'image_id'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'image_id'
newline|'\n'
nl|'\n'
DECL|function|list
dedent|''
name|'def'
name|'list'
op|'('
name|'context'
op|','
name|'filter_list'
op|'='
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" return a list of all images that a user can see\n\n    optionally filtered by a list of image_id """'
newline|'\n'
nl|'\n'
comment|'# FIXME: send along the list of only_images to check for'
nl|'\n'
name|'response'
op|'='
name|'conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'GET'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'filter_list'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'i'
name|'for'
name|'i'
name|'in'
name|'result'
name|'if'
name|'i'
op|'['
string|"'imageId'"
op|']'
name|'in'
name|'filter_list'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|function|get
dedent|''
name|'def'
name|'get'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""return a image object if the context has permissions"""'
newline|'\n'
name|'result'
op|'='
name|'list'
op|'('
name|'context'
op|','
op|'['
name|'image_id'
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|"'Image %s could not be found'"
op|'%'
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'image'
op|'='
name|'result'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'image'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|deregister
dedent|''
name|'def'
name|'deregister'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" unregister an image """'
newline|'\n'
name|'conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'DELETE'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'qs'
op|'('
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|conn
dedent|''
name|'def'
name|'conn'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'access'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_access_key'
op|'('
name|'context'
op|'.'
name|'user'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'secret'
op|'='
name|'str'
op|'('
name|'context'
op|'.'
name|'user'
op|'.'
name|'secret'
op|')'
newline|'\n'
name|'calling'
op|'='
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'OrdinaryCallingFormat'
op|'('
op|')'
newline|'\n'
name|'return'
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'S3Connection'
op|'('
name|'aws_access_key_id'
op|'='
name|'access'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'secret'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'False'
op|','
nl|'\n'
name|'calling_format'
op|'='
name|'calling'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'s3_port'
op|','
nl|'\n'
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'s3_host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|qs
dedent|''
name|'def'
name|'qs'
op|'('
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pairs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'params'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pairs'
op|'.'
name|'append'
op|'('
name|'key'
op|'+'
string|"'='"
op|'+'
name|'urllib'
op|'.'
name|'quote'
op|'('
name|'params'
op|'['
name|'key'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'&'"
op|'.'
name|'join'
op|'('
name|'pairs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
