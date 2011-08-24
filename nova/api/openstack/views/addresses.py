begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
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
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.views.addresses'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Models a server addresses response as a python dictionary."""'
newline|'\n'
nl|'\n'
DECL|member|build
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV10
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV10'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|build
indent|'    '
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'private_ips'
op|'='
name|'self'
op|'.'
name|'build_private_parts'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'public_ips'
op|'='
name|'self'
op|'.'
name|'build_public_parts'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'public'
op|'='
name|'public_ips'
op|','
name|'private'
op|'='
name|'private_ips'
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_public_parts
dedent|''
name|'def'
name|'build_public_parts'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
string|"'fixed_ips/floating_ips/address'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_private_parts
dedent|''
name|'def'
name|'build_private_parts'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
string|"'fixed_ips/address'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV11
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV11'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|build
indent|'    '
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'interfaces'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'networks'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'interface'
name|'in'
name|'interfaces'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'network_label'
op|'='
name|'self'
op|'.'
name|'_extract_network_label'
op|'('
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'network_label'
name|'not'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'                '
name|'networks'
op|'['
name|'network_label'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ip_addresses'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_extract_ipv4_addresses'
op|'('
name|'interface'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                '
name|'ipv6_address'
op|'='
name|'self'
op|'.'
name|'_extract_ipv6_address'
op|'('
name|'interface'
op|')'
newline|'\n'
name|'if'
name|'ipv6_address'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'ip_addresses'
op|'.'
name|'append'
op|'('
name|'ipv6_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'networks'
op|'['
name|'network_label'
op|']'
op|'.'
name|'extend'
op|'('
name|'ip_addresses'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'networks'
newline|'\n'
nl|'\n'
DECL|member|build_network
dedent|''
name|'def'
name|'build_network'
op|'('
name|'self'
op|','
name|'interfaces'
op|','
name|'requested_network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'interface'
name|'in'
name|'interfaces'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'network_label'
op|'='
name|'self'
op|'.'
name|'_extract_network_label'
op|'('
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'network_label'
op|'=='
name|'requested_network'
op|':'
newline|'\n'
indent|'                '
name|'ips'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_extract_ipv4_addresses'
op|'('
name|'interface'
op|')'
op|')'
newline|'\n'
name|'ipv6'
op|'='
name|'self'
op|'.'
name|'_extract_ipv6_address'
op|'('
name|'interface'
op|')'
newline|'\n'
name|'if'
name|'ipv6'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'ips'
op|'.'
name|'append'
op|'('
name|'ipv6'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
name|'network_label'
op|':'
name|'ips'
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_extract_network_label
dedent|''
name|'def'
name|'_extract_network_label'
op|'('
name|'self'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'interface'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|_extract_ipv4_addresses
dedent|''
dedent|''
name|'def'
name|'_extract_ipv4_addresses'
op|'('
name|'self'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'fixed_ip'
name|'in'
name|'interface'
op|'['
string|"'fixed_ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'_build_ip_entity'
op|'('
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'fixed_ip'
op|'.'
name|'get'
op|'('
string|"'floating_ips'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'self'
op|'.'
name|'_build_ip_entity'
op|'('
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extract_ipv6_address
dedent|''
dedent|''
dedent|''
name|'def'
name|'_extract_ipv6_address'
op|'('
name|'self'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ipv6'
op|'='
name|'interface'
op|'.'
name|'get'
op|'('
string|"'fixed_ipv6'"
op|')'
newline|'\n'
name|'if'
name|'fixed_ipv6'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_build_ip_entity'
op|'('
name|'fixed_ipv6'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_ip_entity
dedent|''
dedent|''
name|'def'
name|'_build_ip_entity'
op|'('
name|'self'
op|','
name|'address'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'addr'"
op|':'
name|'address'
op|','
string|"'version'"
op|':'
name|'version'
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
