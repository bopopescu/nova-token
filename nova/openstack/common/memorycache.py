begin_unit
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
string|'"""Super simple fake memcache client."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
DECL|variable|memcache_opts
name|'memcache_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'memcached_servers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Memcached servers or None for in process cache.'"
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
name|'memcache_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_client
name|'def'
name|'get_client'
op|'('
name|'memcached_servers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'client_cls'
op|'='
name|'Client'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'memcached_servers'
op|':'
newline|'\n'
indent|'        '
name|'memcached_servers'
op|'='
name|'CONF'
op|'.'
name|'memcached_servers'
newline|'\n'
dedent|''
name|'if'
name|'memcached_servers'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'import'
name|'memcache'
newline|'\n'
name|'client_cls'
op|'='
name|'memcache'
op|'.'
name|'Client'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'client_cls'
op|'('
name|'memcached_servers'
op|','
name|'debug'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Client
dedent|''
name|'class'
name|'Client'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Replicates a tiny subset of memcached client interface."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
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
string|'"""Ignores the passed in args."""'
newline|'\n'
name|'self'
op|'.'
name|'cache'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieves the value for a key or None.\n\n        This expunges expired keys during each get.\n        """'
newline|'\n'
nl|'\n'
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'list'
op|'('
name|'self'
op|'.'
name|'cache'
op|')'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'timeout'
op|','
name|'_value'
op|')'
op|'='
name|'self'
op|'.'
name|'cache'
op|'['
name|'k'
op|']'
newline|'\n'
name|'if'
name|'timeout'
name|'and'
name|'now'
op|'>='
name|'timeout'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'self'
op|'.'
name|'cache'
op|'['
name|'k'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'cache'
op|'.'
name|'get'
op|'('
name|'key'
op|','
op|'('
number|'0'
op|','
name|'None'
op|')'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
DECL|member|set
dedent|''
name|'def'
name|'set'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|','
name|'time'
op|'='
number|'0'
op|','
name|'min_compress_len'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the value for a key."""'
newline|'\n'
name|'timeout'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'time'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'timeout'
op|'='
name|'timeutils'
op|'.'
name|'utcnow_ts'
op|'('
op|')'
op|'+'
name|'time'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cache'
op|'['
name|'key'
op|']'
op|'='
op|'('
name|'timeout'
op|','
name|'value'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|add
dedent|''
name|'def'
name|'add'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|','
name|'time'
op|'='
number|'0'
op|','
name|'min_compress_len'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the value for a key if it doesn\'t exist."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'set'
op|'('
name|'key'
op|','
name|'value'
op|','
name|'time'
op|','
name|'min_compress_len'
op|')'
newline|'\n'
nl|'\n'
DECL|member|incr
dedent|''
name|'def'
name|'incr'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'delta'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Increments the value for a key."""'
newline|'\n'
name|'value'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'new_value'
op|'='
name|'int'
op|'('
name|'value'
op|')'
op|'+'
name|'delta'
newline|'\n'
name|'self'
op|'.'
name|'cache'
op|'['
name|'key'
op|']'
op|'='
op|'('
name|'self'
op|'.'
name|'cache'
op|'['
name|'key'
op|']'
op|'['
number|'0'
op|']'
op|','
name|'str'
op|'('
name|'new_value'
op|')'
op|')'
newline|'\n'
name|'return'
name|'new_value'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'time'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the value associated with a key."""'
newline|'\n'
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'cache'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'.'
name|'cache'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
