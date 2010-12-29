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
string|'"""Metadata request handler."""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
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
nl|'\n'
nl|'\n'
DECL|class|MetadataRequestHandler
name|'class'
name|'MetadataRequestHandler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Serve metadata from the EC2 API."""'
newline|'\n'
nl|'\n'
DECL|member|print_data
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
comment|'# Cut off last \\n'
nl|'\n'
dedent|''
name|'return'
name|'output'
op|'['
op|':'
op|'-'
number|'1'
op|']'
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
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'data'
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
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cc'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_forwarded_for'
op|':'
newline|'\n'
indent|'            '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|','
name|'remote_address'
op|')'
newline|'\n'
dedent|''
name|'meta_data'
op|'='
name|'cc'
op|'.'
name|'get_metadata'
op|'('
name|'remote_address'
op|')'
newline|'\n'
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|')'
op|'%'
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'self'
op|'.'
name|'lookup'
op|'('
name|'req'
op|'.'
name|'path_info'
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
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'print_data'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
