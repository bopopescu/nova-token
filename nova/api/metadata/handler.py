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
string|'"""Metadata request handler."""'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'hmac'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
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
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'neutronv2'
name|'import'
name|'api'
name|'as'
name|'neutronapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'memorycache'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
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
DECL|variable|metadata_proxy_opts
name|'metadata_proxy_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'service_metadata_proxy'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set flag to indicate Neutron will proxy metadata requests and '"
nl|'\n'
string|"'resolve instance ids.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'metadata_proxy_shared_secret'"
op|','
nl|'\n'
name|'default'
op|'='
string|"''"
op|','
name|'secret'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Shared secret to validate proxies Neutron metadata requests'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|metadata_opts
name|'metadata_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'metadata_cache_expiration'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'15'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Time in seconds to cache metadata; 0 to disable '"
nl|'\n'
string|"'metadata caching entirely (not recommended). Increasing'"
nl|'\n'
string|"'this should improve response times of the metadata API '"
nl|'\n'
string|"'when under heavy load. Higher values may increase memory'"
nl|'\n'
string|"'usage and result in longer times for host metadata '"
nl|'\n'
string|"'changes to take effect.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'metadata_proxy_opts'
op|','
string|"'neutron'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'metadata_opts'
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
nl|'\n'
DECL|class|MetadataRequestHandler
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
name|'memorycache'
op|'.'
name|'get_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_metadata_by_remote_address
dedent|''
name|'def'
name|'get_metadata_by_remote_address'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Using cached metadata for %s"'
op|','
name|'address'
op|')'
newline|'\n'
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
name|'if'
name|'CONF'
op|'.'
name|'metadata_cache_expiration'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
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
name|'CONF'
op|'.'
name|'metadata_cache_expiration'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|get_metadata_by_instance_id
dedent|''
name|'def'
name|'get_metadata_by_instance_id'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cache_key'
op|'='
string|"'metadata-%s'"
op|'%'
name|'instance_id'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Using cached metadata for instance %s"'
op|','
name|'instance_id'
op|')'
newline|'\n'
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
name|'get_metadata_by_instance_id'
op|'('
name|'instance_id'
op|','
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
name|'if'
name|'CONF'
op|'.'
name|'metadata_cache_expiration'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
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
name|'CONF'
op|'.'
name|'metadata_cache_expiration'
op|')'
newline|'\n'
nl|'\n'
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
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'req'
op|'.'
name|'path_info'
op|')'
op|'=='
string|'"/"'
op|':'
newline|'\n'
indent|'            '
name|'resp'
op|'='
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
newline|'\n'
name|'req'
op|'.'
name|'response'
op|'.'
name|'body'
op|'='
name|'resp'
newline|'\n'
name|'req'
op|'.'
name|'response'
op|'.'
name|'content_type'
op|'='
name|'base'
op|'.'
name|'MIME_TYPE_TEXT_PLAIN'
newline|'\n'
name|'return'
name|'req'
op|'.'
name|'response'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'neutron'
op|'.'
name|'service_metadata_proxy'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Metadata-Provider'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'_handle_instance_id_request_from_lb'
op|'('
name|'req'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'_handle_instance_id_request'
op|'('
name|'req'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Instance-ID'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
nl|'\n'
name|'_LW'
op|'('
string|'"X-Instance-ID present in request headers. The "'
nl|'\n'
string|'"\'service_metadata_proxy\' option must be "'
nl|'\n'
string|'"enabled to process this header."'
op|')'
op|')'
newline|'\n'
dedent|''
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'_handle_remote_ip_request'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'meta_data'
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
name|'if'
name|'callable'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'data'
op|'('
name|'req'
op|','
name|'meta_data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'resp'
op|'='
name|'base'
op|'.'
name|'ec2_md_print'
op|'('
name|'data'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'resp'
op|','
name|'six'
op|'.'
name|'text_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'.'
name|'response'
op|'.'
name|'text'
op|'='
name|'resp'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'.'
name|'response'
op|'.'
name|'body'
op|'='
name|'resp'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'.'
name|'response'
op|'.'
name|'content_type'
op|'='
name|'meta_data'
op|'.'
name|'get_mimetype'
op|'('
op|')'
newline|'\n'
name|'return'
name|'req'
op|'.'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|_handle_remote_ip_request
dedent|''
name|'def'
name|'_handle_remote_ip_request'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'get_metadata_by_remote_address'
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
name|'_LE'
op|'('
string|"'Failed to get metadata for IP: %s'"
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
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'_LE'
op|'('
string|"'Failed to get metadata for IP: %s'"
op|')'
op|','
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'meta_data'
newline|'\n'
nl|'\n'
DECL|member|_handle_instance_id_request
dedent|''
name|'def'
name|'_handle_instance_id_request'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Instance-ID'"
op|')'
newline|'\n'
name|'tenant_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Tenant-ID'"
op|')'
newline|'\n'
name|'signature'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Instance-ID-Signature'"
op|')'
newline|'\n'
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Ensure that only one header was passed'
nl|'\n'
nl|'\n'
name|'if'
name|'instance_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'X-Instance-ID header is missing from request.'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'signature'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'X-Instance-ID-Signature header is missing from request.'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'tenant_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'X-Tenant-ID header is missing from request.'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'isinstance'
op|'('
name|'instance_id'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Multiple X-Instance-ID headers found within request.'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'isinstance'
op|'('
name|'tenant_id'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Multiple X-Tenant-ID headers found within request.'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'msg'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_validate_shared_secret'
op|'('
name|'instance_id'
op|','
name|'signature'
op|','
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_meta_by_instance_id'
op|'('
name|'instance_id'
op|','
name|'tenant_id'
op|','
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_id_from_lb
dedent|''
name|'def'
name|'_get_instance_id_from_lb'
op|'('
name|'self'
op|','
name|'provider_id'
op|','
name|'instance_address'
op|')'
op|':'
newline|'\n'
comment|'# We use admin context, admin=True to lookup the'
nl|'\n'
comment|'# inter-Edge network port'
nl|'\n'
indent|'        '
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'neutron'
op|'='
name|'neutronapi'
op|'.'
name|'get_client'
op|'('
name|'context'
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Tenant, instance ids are found in the following method:'
nl|'\n'
comment|'#  X-Metadata-Provider contains id of the metadata provider, and since'
nl|'\n'
comment|'#  overlapping networks cannot be connected to the same metadata'
nl|'\n'
comment|"#  provider, the combo of tenant's instance IP and the metadata"
nl|'\n'
comment|'#  provider has to be unique.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#  The networks which are connected to the metadata provider are'
nl|'\n'
comment|'#  retrieved in the 1st call to neutron.list_subnets()'
nl|'\n'
comment|'#  In the 2nd call we read the ports which belong to any of the'
nl|'\n'
comment|'#  networks retrieved above, and have the X-Forwarded-For IP address.'
nl|'\n'
comment|'#  This combination has to be unique as explained above, and we can'
nl|'\n'
comment|'#  read the instance_id, tenant_id from that port entry.'
nl|'\n'
nl|'\n'
comment|'# Retrieve networks which are connected to metadata provider'
nl|'\n'
name|'md_subnets'
op|'='
name|'neutron'
op|'.'
name|'list_subnets'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'advanced_service_providers'
op|'='
op|'['
name|'provider_id'
op|']'
op|','
nl|'\n'
name|'fields'
op|'='
op|'['
string|"'network_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'md_networks'
op|'='
op|'['
name|'subnet'
op|'['
string|"'network_id'"
op|']'
nl|'\n'
name|'for'
name|'subnet'
name|'in'
name|'md_subnets'
op|'['
string|"'subnets'"
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|"# Retrieve the instance data from the instance's port"
nl|'\n'
indent|'            '
name|'instance_data'
op|'='
name|'neutron'
op|'.'
name|'list_ports'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'fixed_ips'
op|'='
string|"'ip_address='"
op|'+'
name|'instance_address'
op|','
nl|'\n'
name|'network_id'
op|'='
name|'md_networks'
op|','
nl|'\n'
name|'fields'
op|'='
op|'['
string|"'device_id'"
op|','
string|"'tenant_id'"
op|']'
op|')'
op|'['
string|"'ports'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'Failed to get instance id for metadata '"
nl|'\n'
string|"'request, provider %(provider)s '"
nl|'\n'
string|"'networks %(networks)s '"
nl|'\n'
string|"'requester %(requester)s. Error: %(error)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'provider'"
op|':'
name|'provider_id'
op|','
nl|'\n'
string|"'networks'"
op|':'
name|'md_networks'
op|','
nl|'\n'
string|"'requester'"
op|':'
name|'instance_address'
op|','
nl|'\n'
string|"'error'"
op|':'
name|'e'
op|'}'
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
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_id'
op|'='
name|'instance_data'
op|'['
string|"'device_id'"
op|']'
newline|'\n'
name|'tenant_id'
op|'='
name|'instance_data'
op|'['
string|"'tenant_id'"
op|']'
newline|'\n'
nl|'\n'
comment|"# instance_data is unicode-encoded, while memorycache doesn't like"
nl|'\n'
comment|'# that. Therefore we convert to str'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instance_id'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'instance_id'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance_id'
op|','
name|'tenant_id'
newline|'\n'
nl|'\n'
DECL|member|_handle_instance_id_request_from_lb
dedent|''
name|'def'
name|'_handle_instance_id_request_from_lb'
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
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|')'
newline|'\n'
name|'if'
name|'remote_address'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'X-Forwarded-For is missing from request.'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'provider_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Metadata-Provider'"
op|')'
newline|'\n'
name|'if'
name|'provider_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'X-Metadata-Provider is missing from request.'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'instance_address'
op|'='
name|'remote_address'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# If authentication token is set, authenticate'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'neutron'
op|'.'
name|'metadata_proxy_shared_secret'
op|':'
newline|'\n'
indent|'            '
name|'signature'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Metadata-Provider-Signature'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_validate_shared_secret'
op|'('
name|'provider_id'
op|','
name|'signature'
op|','
nl|'\n'
name|'instance_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_id'
op|','
name|'tenant_id'
op|'='
name|'self'
op|'.'
name|'_get_instance_id_from_lb'
op|'('
nl|'\n'
name|'provider_id'
op|','
name|'instance_address'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_meta_by_instance_id'
op|'('
name|'instance_id'
op|','
name|'tenant_id'
op|','
nl|'\n'
name|'instance_address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_shared_secret
dedent|''
name|'def'
name|'_validate_shared_secret'
op|'('
name|'self'
op|','
name|'requestor_id'
op|','
name|'signature'
op|','
nl|'\n'
name|'requestor_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_signature'
op|'='
name|'hmac'
op|'.'
name|'new'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'neutron'
op|'.'
name|'metadata_proxy_shared_secret'
op|','
nl|'\n'
name|'requestor_id'
op|','
name|'hashlib'
op|'.'
name|'sha256'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'utils'
op|'.'
name|'constant_time_compare'
op|'('
name|'expected_signature'
op|','
name|'signature'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'requestor_id'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'X-Instance-ID-Signature: %(signature)s does '"
nl|'\n'
string|"'not match the expected value: '"
nl|'\n'
string|"'%(expected_signature)s for id: '"
nl|'\n'
string|"'%(requestor_id)s. Request From: '"
nl|'\n'
string|"'%(requestor_address)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'signature'"
op|':'
name|'signature'
op|','
nl|'\n'
string|"'expected_signature'"
op|':'
name|'expected_signature'
op|','
nl|'\n'
string|"'requestor_id'"
op|':'
name|'requestor_id'
op|','
nl|'\n'
string|"'requestor_address'"
op|':'
name|'requestor_address'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|"'Invalid proxy request signature.'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_meta_by_instance_id
dedent|''
dedent|''
name|'def'
name|'_get_meta_by_instance_id'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'tenant_id'
op|','
name|'remote_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'get_metadata_by_instance_id'
op|'('
name|'instance_id'
op|','
nl|'\n'
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
name|'_LE'
op|'('
string|"'Failed to get metadata for instance id: %s'"
op|')'
op|','
nl|'\n'
name|'instance_id'
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
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'_LE'
op|'('
string|"'Failed to get metadata for instance id: %s'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'meta_data'
op|'.'
name|'instance'
op|'.'
name|'project_id'
op|'!='
name|'tenant_id'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Tenant_id %(tenant_id)s does not match tenant_id "'
nl|'\n'
string|'"of instance %(instance_id)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'tenant_id'"
op|':'
name|'tenant_id'
op|','
string|"'instance_id'"
op|':'
name|'instance_id'
op|'}'
op|')'
newline|'\n'
comment|'# causes a 404 to be raised'
nl|'\n'
name|'meta_data'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'meta_data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
