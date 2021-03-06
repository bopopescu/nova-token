begin_unit
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
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
name|'network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'floating_ip_pools'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ip_view
name|'def'
name|'_translate_floating_ip_view'
op|'('
name|'pool_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'pool_name'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ip_pools_view
dedent|''
name|'def'
name|'_translate_floating_ip_pools_view'
op|'('
name|'pools'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'floating_ip_pools'"
op|':'
op|'['
name|'_translate_floating_ip_view'
op|'('
name|'pool_name'
op|')'
nl|'\n'
name|'for'
name|'pool_name'
name|'in'
name|'pools'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPPoolsController
dedent|''
name|'class'
name|'FloatingIPPoolsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Floating IP Pool API controller for the OpenStack API."""'
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
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIPPoolsController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
string|'"""Return a list of pools."""'
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
name|'pools'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip_pools'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'_translate_floating_ip_pools_view'
op|'('
name|'pools'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Floating_ip_pools
dedent|''
dedent|''
name|'class'
name|'Floating_ip_pools'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Floating IPs support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FloatingIpPools"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-floating-ip-pools"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"floating_ip_pools/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-01-04T00:00:00Z"'
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
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-floating-ip-pools'"
op|','
nl|'\n'
name|'FloatingIPPoolsController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
