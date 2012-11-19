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
name|'import'
name|'os'
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
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_forwarded_for'"
op|','
string|"'nova.api.auth'"
op|')'
newline|'\n'
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
name|'if'
name|'CONF'
op|'.'
name|'memcached_servers'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'memcache'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'nova'
op|'.'
name|'common'
name|'import'
name|'memorycache'
name|'as'
name|'memcache'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataRequestHandler
dedent|''
name|'class'
name|'MetadataRequestHandler'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Serve metadata."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'_cache'
op|'='
name|'memcache'
op|'.'
name|'Client'
op|'('
name|'CONF'
op|'.'
name|'memcached_servers'
op|','
name|'debug'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_metadata
dedent|''
name|'def'
name|'get_metadata'
op|'('
name|'self'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FixedIpNotFoundForAddress'
op|'('
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cache_key'
op|'='
string|"'metadata-%s'"
op|'%'
name|'address'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_cache'
op|'.'
name|'get'
op|'('
name|'cache_key'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'base'
op|'.'
name|'get_metadata_by_address'
op|'('
name|'address'
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
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_cache'
op|'.'
name|'set'
op|'('
name|'cache_key'
op|','
name|'data'
op|','
number|'15'
op|')'
newline|'\n'
nl|'\n'
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
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
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
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
newline|'\n'
name|'if'
name|'CONF'
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
nl|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
string|'"/"'
op|'+'
name|'req'
op|'.'
name|'path_info'
op|')'
op|'=='
string|'"/"'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'base'
op|'.'
name|'ec2_md_print'
op|'('
name|'base'
op|'.'
name|'VERSIONS'
op|'+'
op|'['
string|'"latest"'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'get_metadata'
op|'('
name|'remote_address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|')'
op|','
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'An unknown error has occurred. '"
nl|'\n'
string|"'Please try your request again.'"
op|')'
newline|'\n'
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
name|'return'
name|'exc'
newline|'\n'
dedent|''
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|')'
op|','
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
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'meta_data'
op|'.'
name|'lookup'
op|'('
name|'req'
op|'.'
name|'path_info'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'base'
op|'.'
name|'InvalidMetadataPath'
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
nl|'\n'
dedent|''
name|'return'
name|'base'
op|'.'
name|'ec2_md_print'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
