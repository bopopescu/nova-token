begin_unit
comment|'# Copyright 2012 IBM Corp.'
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
name|'netaddr'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
string|"'default_floating_pool'"
op|','
string|"'nova.network.floating_ips'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'public_interface'"
op|','
string|"'nova.network.linux_net'"
op|')'
newline|'\n'
nl|'\n'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'floating_ips_bulk'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPBulkController
name|'class'
name|'FloatingIPBulkController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of all floating ips."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_floating_ip_info'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of all floating ips for a given host."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_floating_ip_info'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_floating_ip_info
dedent|''
name|'def'
name|'_get_floating_ip_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip_info'
op|'='
op|'{'
string|'"floating_ip_info"'
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'floating_ips'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'floating_ips'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoFloatingIpsDefined'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'floating_ip_info'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'floating_ip'
name|'in'
name|'floating_ips'
op|':'
newline|'\n'
indent|'            '
name|'instance_uuid'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'floating_ip'
op|'['
string|"'fixed_ip_id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'fixed_ip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get'
op|'('
name|'context'
op|','
name|'floating_ip'
op|'['
string|"'fixed_ip_id'"
op|']'
op|')'
newline|'\n'
name|'instance_uuid'
op|'='
name|'fixed_ip'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'{'
string|"'address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'floating_ip'
op|'['
string|"'pool'"
op|']'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'floating_ip'
op|'['
string|"'interface'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'floating_ip'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
name|'floating_ip_info'
op|'['
string|"'floating_ip_info'"
op|']'
op|'.'
name|'append'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'floating_ip_info'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Bulk create floating ips."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'floating_ips_bulk_create'"
name|'not'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
dedent|''
name|'params'
op|'='
name|'body'
op|'['
string|"'floating_ips_bulk_create'"
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'ip_range'"
name|'not'
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
dedent|''
name|'ip_range'
op|'='
name|'params'
op|'['
string|"'ip_range'"
op|']'
newline|'\n'
nl|'\n'
name|'pool'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'pool'"
op|','
name|'CONF'
op|'.'
name|'default_floating_pool'
op|')'
newline|'\n'
name|'interface'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'interface'"
op|','
name|'CONF'
op|'.'
name|'public_interface'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ips'
op|'='
op|'('
op|'{'
string|"'address'"
op|':'
name|'str'
op|'('
name|'address'
op|')'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'interface'
op|'}'
nl|'\n'
name|'for'
name|'address'
name|'in'
name|'self'
op|'.'
name|'_address_to_hosts'
op|'('
name|'ip_range'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'exc'
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
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'floating_ip_bulk_create'
op|'('
name|'context'
op|','
name|'ips'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpExists'
name|'as'
name|'exc'
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
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|'"floating_ips_bulk_create"'
op|':'
op|'{'
string|'"ip_range"'
op|':'
name|'ip_range'
op|','
nl|'\n'
string|'"pool"'
op|':'
name|'pool'
op|','
nl|'\n'
string|'"interface"'
op|':'
name|'interface'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Bulk delete floating IPs."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'id'
op|'!='
string|'"delete"'
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
string|'"Unknown action"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ip_range'
op|'='
name|'body'
op|'['
string|"'ip_range'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ips'
op|'='
op|'('
op|'{'
string|"'address'"
op|':'
name|'str'
op|'('
name|'address'
op|')'
op|'}'
nl|'\n'
name|'for'
name|'address'
name|'in'
name|'self'
op|'.'
name|'_address_to_hosts'
op|'('
name|'ip_range'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'exc'
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
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'floating_ip_bulk_destroy'
op|'('
name|'context'
op|','
name|'ips'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|'"floating_ips_bulk_delete"'
op|':'
name|'ip_range'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_address_to_hosts
dedent|''
name|'def'
name|'_address_to_hosts'
op|'('
name|'self'
op|','
name|'addresses'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Iterate over hosts within an address range.\n\n        If an explicit range specifier is missing, the parameter is\n        interpreted as a specific individual address.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'addresses'
op|')'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'addresses'
op|')'
newline|'\n'
name|'if'
name|'net'
op|'.'
name|'size'
op|'<'
number|'4'
op|':'
newline|'\n'
indent|'                '
name|'reason'
op|'='
name|'_'
op|'('
string|'"/%s should be specified as single address(es) "'
nl|'\n'
string|'"not in cidr format"'
op|')'
op|'%'
name|'net'
op|'.'
name|'prefixlen'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'net'
op|'.'
name|'iter_hosts'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'netaddr'
op|'.'
name|'AddrFormatError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'str'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Floating_ips_bulk
dedent|''
dedent|''
dedent|''
name|'class'
name|'Floating_ips_bulk'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Bulk handling of Floating IPs."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FloatingIpsBulk"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-floating-ips-bulk"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"floating_ips_bulk/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-10-29T13:25:27-06:00"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-floating-ips-bulk'"
op|','
nl|'\n'
name|'FloatingIPBulkController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'resource'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
