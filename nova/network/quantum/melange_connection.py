begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|melange_opts
name|'melange_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'melange_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'HOST for connecting to melange'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'melange_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'9898'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PORT for connecting to melange'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'melange_opts'
op|')'
newline|'\n'
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
DECL|variable|json_content_type
name|'json_content_type'
op|'='
op|'{'
string|"'Content-type'"
op|':'
string|'"application/json"'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# FIXME(danwent): talk to the Melange folks about creating a'
nl|'\n'
comment|'# client lib that we can import as a library, instead of'
nl|'\n'
comment|'# have to have all of the client code in here.'
nl|'\n'
DECL|class|MelangeConnection
name|'class'
name|'MelangeConnection'
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
op|','
name|'host'
op|'='
name|'None'
op|','
name|'port'
op|'='
name|'None'
op|','
name|'use_ssl'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'melange_host'
newline|'\n'
dedent|''
name|'if'
name|'port'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'port'
op|'='
name|'int'
op|'('
name|'FLAGS'
op|'.'
name|'melange_port'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'port'
newline|'\n'
name|'self'
op|'.'
name|'use_ssl'
op|'='
name|'use_ssl'
newline|'\n'
name|'self'
op|'.'
name|'version'
op|'='
string|'"v0.1"'
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
name|'params'
op|'='
name|'None'
op|','
name|'headers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"GET"'
op|','
name|'path'
op|','
name|'params'
op|'='
name|'params'
op|','
name|'headers'
op|'='
name|'headers'
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
name|'body'
op|'='
name|'None'
op|','
name|'headers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"POST"'
op|','
name|'path'
op|','
name|'body'
op|'='
name|'body'
op|','
name|'headers'
op|'='
name|'headers'
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
name|'path'
op|','
name|'headers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"DELETE"'
op|','
name|'path'
op|','
name|'headers'
op|'='
name|'headers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_connection
dedent|''
name|'def'
name|'_get_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'use_ssl'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'port'
op|')'
newline|'\n'
nl|'\n'
DECL|member|do_request
dedent|''
dedent|''
name|'def'
name|'do_request'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'path'
op|','
name|'body'
op|'='
name|'None'
op|','
name|'headers'
op|'='
name|'None'
op|','
name|'params'
op|'='
name|'None'
op|','
nl|'\n'
name|'content_type'
op|'='
string|'".json"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'headers'
op|'='
name|'headers'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'params'
op|'='
name|'params'
name|'or'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|'"/%s/%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'version'
op|','
name|'path'
op|','
name|'content_type'
op|')'
newline|'\n'
name|'if'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'url'
op|'+='
string|'"?%s"'
op|'%'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'connection'
op|'='
name|'self'
op|'.'
name|'_get_connection'
op|'('
op|')'
newline|'\n'
name|'connection'
op|'.'
name|'request'
op|'('
name|'method'
op|','
name|'url'
op|','
name|'body'
op|','
name|'headers'
op|')'
newline|'\n'
name|'response'
op|'='
name|'connection'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\n'
name|'response_str'
op|'='
name|'response'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'if'
name|'response'
op|'.'
name|'status'
op|'<'
number|'400'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'response_str'
newline|'\n'
dedent|''
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Server returned error: %s"'
op|'%'
name|'response_str'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'socket'
op|'.'
name|'error'
op|','
name|'IOError'
op|')'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Unable to connect to "'
nl|'\n'
string|'"server. Got error: %s"'
op|'%'
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_ip
dedent|''
dedent|''
name|'def'
name|'allocate_ip'
op|'('
name|'self'
op|','
name|'network_id'
op|','
name|'network_tenant_id'
op|','
name|'vif_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
name|'mac_address'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"allocate IP on network |%(network_id)s| "'
nl|'\n'
string|'"belonging to |%(network_tenant_id)s| "'
nl|'\n'
string|'"to this vif |%(vif_id)s| with mac |%(mac_address)s| "'
nl|'\n'
string|'"belonging to |%(project_id)s| "'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
op|'('
name|'network_tenant_id'
nl|'\n'
name|'if'
name|'network_tenant_id'
name|'else'
string|'""'
op|')'
newline|'\n'
name|'request_body'
op|'='
op|'('
name|'json'
op|'.'
name|'dumps'
op|'('
name|'dict'
op|'('
name|'network'
op|'='
name|'dict'
op|'('
name|'mac_address'
op|'='
name|'mac_address'
op|','
nl|'\n'
name|'tenant_id'
op|'='
name|'project_id'
op|')'
op|')'
op|')'
nl|'\n'
name|'if'
name|'mac_address'
name|'else'
name|'None'
op|')'
newline|'\n'
name|'url'
op|'='
op|'('
string|'"ipam%(tenant_scope)s/networks/%(network_id)s/"'
nl|'\n'
string|'"interfaces/%(vif_id)s/ip_allocations"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'post'
op|'('
name|'url'
op|','
name|'body'
op|'='
name|'request_body'
op|','
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|')'
op|'['
string|"'ip_addresses'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|create_block
dedent|''
name|'def'
name|'create_block'
op|'('
name|'self'
op|','
name|'network_id'
op|','
name|'cidr'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
name|'gateway'
op|'='
name|'None'
op|','
name|'dns1'
op|'='
name|'None'
op|','
name|'dns2'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
name|'project_id'
name|'if'
name|'project_id'
name|'else'
string|'""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|'"ipam%(tenant_scope)s/ip_blocks"'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'req_params'
op|'='
name|'dict'
op|'('
name|'ip_block'
op|'='
name|'dict'
op|'('
name|'cidr'
op|'='
name|'cidr'
op|','
name|'network_id'
op|'='
name|'network_id'
op|','
nl|'\n'
name|'type'
op|'='
string|"'private'"
op|','
name|'gateway'
op|'='
name|'gateway'
op|','
nl|'\n'
name|'dns1'
op|'='
name|'dns1'
op|','
name|'dns2'
op|'='
name|'dns2'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'post'
op|'('
name|'url'
op|','
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'req_params'
op|')'
op|','
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_block
dedent|''
name|'def'
name|'delete_block'
op|'('
name|'self'
op|','
name|'block_id'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
name|'project_id'
name|'if'
name|'project_id'
name|'else'
string|'""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|'"ipam%(tenant_scope)s/ip_blocks/%(block_id)s"'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'delete'
op|'('
name|'url'
op|','
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_blocks
dedent|''
name|'def'
name|'get_blocks'
op|'('
name|'self'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
name|'project_id'
name|'if'
name|'project_id'
name|'else'
string|'""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|'"ipam%(tenant_scope)s/ip_blocks"'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'url'
op|','
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_routes
dedent|''
name|'def'
name|'get_routes'
op|'('
name|'self'
op|','
name|'block_id'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
name|'project_id'
name|'if'
name|'project_id'
name|'else'
string|'""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
op|'('
string|'"ipam%(tenant_scope)s/ip_blocks/%(block_id)s/ip_routes"'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'url'
op|','
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|')'
op|'['
string|"'ip_routes'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_allocated_ips
dedent|''
name|'def'
name|'get_allocated_ips'
op|'('
name|'self'
op|','
name|'network_id'
op|','
name|'vif_id'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
name|'project_id'
name|'if'
name|'project_id'
name|'else'
string|'""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
op|'('
string|'"ipam%(tenant_scope)s/networks/%(network_id)s/"'
nl|'\n'
string|'"interfaces/%(vif_id)s/ip_allocations"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'url'
op|','
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|')'
op|'['
string|"'ip_addresses'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_allocated_ips_for_network
dedent|''
name|'def'
name|'get_allocated_ips_for_network'
op|'('
name|'self'
op|','
name|'network_id'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
name|'project_id'
name|'if'
name|'project_id'
name|'else'
string|'""'
newline|'\n'
name|'url'
op|'='
op|'('
string|'"ipam%(tenant_scope)s/allocated_ip_addresses"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# TODO(bgh): This request fails if you add the ".json" to the end so'
nl|'\n'
comment|'# it has to call do_request itself.  Melange bug?'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'do_request'
op|'('
string|'"GET"'
op|','
name|'url'
op|','
name|'content_type'
op|'='
string|'""'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|')'
op|'['
string|"'ip_addresses'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|deallocate_ips
dedent|''
name|'def'
name|'deallocate_ips'
op|'('
name|'self'
op|','
name|'network_id'
op|','
name|'vif_id'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tenant_scope'
op|'='
string|'"/tenants/%s"'
op|'%'
name|'project_id'
name|'if'
name|'project_id'
name|'else'
string|'""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
op|'('
string|'"ipam%(tenant_scope)s/networks/%(network_id)s/"'
nl|'\n'
string|'"interfaces/%(vif_id)s/ip_allocations"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'delete'
op|'('
name|'url'
op|','
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_vif
dedent|''
name|'def'
name|'create_vif'
op|'('
name|'self'
op|','
name|'vif_id'
op|','
name|'instance_id'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"ipam/interfaces"'
newline|'\n'
nl|'\n'
name|'request_body'
op|'='
name|'dict'
op|'('
name|'interface'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'vif_id'
op|','
name|'tenant_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'device_id'
op|'='
name|'instance_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'post'
op|'('
name|'url'
op|','
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'request_body'
op|')'
op|','
nl|'\n'
name|'headers'
op|'='
name|'json_content_type'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|')'
op|'['
string|"'interface'"
op|']'
op|'['
string|"'mac_address'"
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
