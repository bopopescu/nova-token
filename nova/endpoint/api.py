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
string|'"""\nTornado REST API Request Handlers for Nova functions\nMost calls are proxied into the responsible controller.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'multiprocessing'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'import'
name|'tornado'
op|'.'
name|'web'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'cloud'
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
name|'DEFINE_integer'
op|'('
string|"'cc_port'"
op|','
number|'8773'
op|','
string|"'cloud controller port'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIRequestContext
name|'class'
name|'APIRequestContext'
op|'('
name|'object'
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
name|'handler'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'handler'
op|'='
name|'handler'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'user'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'project'
newline|'\n'
name|'self'
op|'.'
name|'request_id'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
nl|'\n'
op|'['
name|'random'
op|'.'
name|'choice'
op|'('
string|"'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-'"
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'20'
op|')'
op|']'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RootRequestHandler
dedent|''
dedent|''
name|'class'
name|'RootRequestHandler'
op|'('
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'RequestHandler'
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
comment|'# available api versions'
nl|'\n'
indent|'        '
name|'versions'
op|'='
op|'['
nl|'\n'
string|"'1.0'"
op|','
nl|'\n'
string|"'2007-01-19'"
op|','
nl|'\n'
string|"'2007-03-01'"
op|','
nl|'\n'
string|"'2007-08-29'"
op|','
nl|'\n'
string|"'2007-10-10'"
op|','
nl|'\n'
string|"'2007-12-15'"
op|','
nl|'\n'
string|"'2008-02-01'"
op|','
nl|'\n'
string|"'2008-09-01'"
op|','
nl|'\n'
string|"'2009-04-04'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'for'
name|'version'
name|'in'
name|'versions'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'write'
op|'('
string|"'%s\\n'"
op|'%'
name|'version'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataRequestHandler
dedent|''
dedent|''
name|'class'
name|'MetadataRequestHandler'
op|'('
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'RequestHandler'
op|')'
op|':'
newline|'\n'
DECL|member|print_data
indent|'    '
name|'def'
name|'print_data'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'output'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'key'
op|'=='
string|"'_name'"
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'output'
op|'+='
name|'key'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
string|"'_name'"
name|'in'
name|'data'
op|'['
name|'key'
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'output'
op|'+='
string|"'='"
op|'+'
name|'str'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|'['
string|"'_name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'output'
op|'+='
string|"'/'"
newline|'\n'
dedent|''
dedent|''
name|'output'
op|'+='
string|"'\\n'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'write'
op|'('
name|'output'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|')'
comment|'# cut off last \\n'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'write'
op|'('
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'write'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookup
dedent|''
dedent|''
name|'def'
name|'lookup'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'data'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'data'
op|'['
name|'item'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'data'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cc'
op|'='
name|'self'
op|'.'
name|'application'
op|'.'
name|'controllers'
op|'['
string|"'Cloud'"
op|']'
newline|'\n'
name|'meta_data'
op|'='
name|'cc'
op|'.'
name|'get_metadata'
op|'('
name|'self'
op|'.'
name|'request'
op|'.'
name|'remote_ip'
op|')'
newline|'\n'
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'error'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'remote_ip'
op|')'
newline|'\n'
name|'raise'
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'404'
op|')'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'self'
op|'.'
name|'lookup'
op|'('
name|'path'
op|','
name|'meta_data'
op|')'
newline|'\n'
name|'if'
name|'data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'404'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'print_data'
op|'('
name|'data'
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
DECL|class|APIServerApplication
dedent|''
dedent|''
name|'class'
name|'APIServerApplication'
op|'('
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'Application'
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
name|'controllers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tornado'
op|'.'
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
string|"r'/'"
op|','
name|'RootRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/cloudpipe/(.*)'"
op|','
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'api'
op|'.'
name|'CloudPipeRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/cloudpipe'"
op|','
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'api'
op|'.'
name|'CloudPipeRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/services/([A-Za-z0-9]+)/'"
op|','
name|'APIRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/latest/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2009-04-04/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2008-09-01/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2008-02-01/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-12-15/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-10-10/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-08-29/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-03-01/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-01-19/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/1.0/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|']'
op|','
name|'pool'
op|'='
name|'multiprocessing'
op|'.'
name|'Pool'
op|'('
number|'4'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controllers'
op|'='
name|'controllers'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
