begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'exception'
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
name|'network'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_network_cache_model'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RouteTests
name|'class'
name|'RouteTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_create_route_with_attrs
indent|'    '
name|'def'
name|'test_create_route_with_attrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'route'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
newline|'\n'
name|'ip'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'192.168.1.1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'route'
op|'['
string|"'cidr'"
op|']'
op|','
string|"'0.0.0.0/24'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'route'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
op|','
string|"'192.168.1.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'route'
op|'['
string|"'interface'"
op|']'
op|','
string|"'eth0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_routes_equal
dedent|''
name|'def'
name|'test_routes_equal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'route1'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
newline|'\n'
name|'route2'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'route1'
op|','
name|'route2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_routes_not_equal
dedent|''
name|'def'
name|'test_routes_not_equal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'route1'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
newline|'\n'
name|'route2'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'1.1.1.1/24'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'route1'
op|','
name|'route2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydrate
dedent|''
name|'def'
name|'test_hydrate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'route'
op|'='
name|'model'
op|'.'
name|'Route'
op|'.'
name|'hydrate'
op|'('
nl|'\n'
op|'{'
string|"'gateway'"
op|':'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'192.168.1.1'"
op|')'
op|')'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'route'
op|'['
string|"'cidr'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'route'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
op|','
string|"'192.168.1.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'route'
op|'['
string|"'interface'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIPTests
dedent|''
dedent|''
name|'class'
name|'FixedIPTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_createnew_fixed_ip_with_attrs
indent|'    '
name|'def'
name|'test_createnew_fixed_ip_with_attrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'192.168.1.100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|','
string|"'192.168.1.100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'type'"
op|']'
op|','
string|"'fixed'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'version'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_fixed_ipv6
dedent|''
name|'def'
name|'test_create_fixed_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'::1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|','
string|"'::1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'type'"
op|']'
op|','
string|"'fixed'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'version'"
op|']'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_fixed_bad_ip_fails
dedent|''
name|'def'
name|'test_create_fixed_bad_ip_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidIpAddressError'
op|','
nl|'\n'
name|'model'
op|'.'
name|'FixedIP'
op|','
nl|'\n'
name|'address'
op|'='
string|"'picklespicklespickles'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_equate_two_fixed_ips
dedent|''
name|'def'
name|'test_equate_two_fixed_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'::1'"
op|')'
newline|'\n'
name|'fixed_ip2'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'::1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|','
name|'fixed_ip2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_equate_two_dissimilar_fixed_ips_fails
dedent|''
name|'def'
name|'test_equate_two_dissimilar_fixed_ips_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'::1'"
op|')'
newline|'\n'
name|'fixed_ip2'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'::2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'fixed_ip'
op|','
name|'fixed_ip2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydrate
dedent|''
name|'def'
name|'test_hydrate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'.'
name|'hydrate'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'type'"
op|']'
op|','
string|"'fixed'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'version'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_floating_ip
dedent|''
name|'def'
name|'test_add_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'192.168.1.100'"
op|')'
newline|'\n'
name|'fixed_ip'
op|'.'
name|'add_floating_ip'
op|'('
string|"'192.168.1.101'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|','
op|'['
string|"'192.168.1.101'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_floating_ip_repeatedly_only_one_instance
dedent|''
name|'def'
name|'test_add_floating_ip_repeatedly_only_one_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
string|"'192.168.1.100'"
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'.'
name|'add_floating_ip'
op|'('
string|"'192.168.1.101'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|','
op|'['
string|"'192.168.1.101'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SubnetTests
dedent|''
dedent|''
name|'class'
name|'SubnetTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_create_subnet_with_attrs
indent|'    '
name|'def'
name|'test_create_subnet_with_attrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'route1'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|','
string|"'10.10.0.0/24'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'1.2.3.4'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'2.3.4.5'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
op|','
string|"'10.10.0.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.2'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.3'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|','
op|'['
name|'route1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'version'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_route
dedent|''
name|'def'
name|'test_add_route'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
newline|'\n'
name|'route1'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
newline|'\n'
name|'route2'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|'{'
string|"'cidr'"
op|':'
string|"'1.1.1.1/24'"
op|'}'
op|')'
newline|'\n'
name|'subnet'
op|'.'
name|'add_route'
op|'('
name|'route2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|','
op|'['
name|'route1'
op|','
name|'route2'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_route_a_lot
dedent|''
name|'def'
name|'test_add_route_a_lot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
newline|'\n'
name|'route1'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
newline|'\n'
name|'route2'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|'{'
string|"'cidr'"
op|':'
string|"'1.1.1.1/24'"
op|'}'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'subnet'
op|'.'
name|'add_route'
op|'('
name|'route2'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|','
op|'['
name|'route1'
op|','
name|'route2'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_dns
dedent|''
name|'def'
name|'test_add_dns'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
newline|'\n'
name|'dns'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'9.9.9.9'"
op|')'
op|')'
newline|'\n'
name|'subnet'
op|'.'
name|'add_dns'
op|'('
name|'dns'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'1.2.3.4'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'2.3.4.5'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'9.9.9.9'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_dns_a_lot
dedent|''
name|'def'
name|'test_add_dns_a_lot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'subnet'
op|'.'
name|'add_dns'
op|'('
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'9.9.9.9'"
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'1.2.3.4'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'2.3.4.5'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'9.9.9.9'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_ip
dedent|''
name|'def'
name|'test_add_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
newline|'\n'
name|'subnet'
op|'.'
name|'add_ip'
op|'('
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'192.168.1.102'"
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.2'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.3'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'192.168.1.102'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_ip_a_lot
dedent|''
name|'def'
name|'test_add_ip_a_lot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'subnet'
op|'.'
name|'add_ip'
op|'('
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'192.168.1.102'"
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.2'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.3'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'192.168.1.102'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydrate
dedent|''
name|'def'
name|'test_hydrate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet_dict'
op|'='
op|'{'
nl|'\n'
string|"'cidr'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'dns'"
op|':'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'1.1.1.1'"
op|')'
op|')'
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'2.2.2.2'"
op|')'
op|')'
op|']'
op|','
nl|'\n'
string|"'routes'"
op|':'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
op|']'
op|','
nl|'\n'
string|"'version'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'3.3.3.3'"
op|')'
op|')'
op|'}'
newline|'\n'
name|'subnet'
op|'='
name|'model'
op|'.'
name|'Subnet'
op|'.'
name|'hydrate'
op|'('
name|'subnet_dict'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|','
string|"'255.255.255.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|','
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'1.1.1.1'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
op|','
string|"'3.3.3.3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|','
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'2.2.2.2'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|','
op|'['
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_route'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'subnet'
op|'['
string|"'version'"
op|']'
op|','
number|'4'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkTests
dedent|''
dedent|''
name|'class'
name|'NetworkTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_create_network
indent|'    '
name|'def'
name|'test_create_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_network'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'br0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'label'"
op|']'
op|','
string|"'public'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'subnets'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'255.255.255.255'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_subnet
dedent|''
name|'def'
name|'test_add_subnet'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_network'
op|'('
op|')'
newline|'\n'
name|'network'
op|'.'
name|'add_subnet'
op|'('
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'0.0.0.0'"
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'subnets'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'255.255.255.255'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'0.0.0.0'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_subnet_a_lot
dedent|''
name|'def'
name|'test_add_subnet_a_lot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_network'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'.'
name|'add_subnet'
op|'('
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'0.0.0.0'"
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'subnets'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'255.255.255.255'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'0.0.0.0'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydrate
dedent|''
name|'def'
name|'test_hydrate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'new_network'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'bridge'
op|'='
string|"'br0'"
op|','
nl|'\n'
name|'label'
op|'='
string|"'public'"
op|','
nl|'\n'
name|'subnets'
op|'='
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'255.255.255.255'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
name|'network'
op|'='
name|'model'
op|'.'
name|'Network'
op|'.'
name|'hydrate'
op|'('
name|'fake_network_cache_model'
op|'.'
name|'new_network'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'br0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'label'"
op|']'
op|','
string|"'public'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network'
op|'['
string|"'subnets'"
op|']'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_subnet'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'cidr'
op|'='
string|"'255.255.255.255'"
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VIFTests
dedent|''
dedent|''
name|'class'
name|'VIFTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_create_vif
indent|'    '
name|'def'
name|'test_create_vif'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
string|"'aa:aa:aa:aa:aa:aa'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vif'
op|'['
string|"'network'"
op|']'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_network'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vif_get_fixed_ips
dedent|''
name|'def'
name|'test_vif_get_fixed_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
newline|'\n'
name|'fixed_ips'
op|'='
name|'vif'
op|'.'
name|'fixed_ips'
op|'('
op|')'
newline|'\n'
name|'ips'
op|'='
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.2'"
op|')'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.0.3'"
op|')'
op|')'
op|']'
op|'*'
number|'2'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixed_ips'
op|','
name|'ips'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vif_get_floating_ips
dedent|''
name|'def'
name|'test_vif_get_floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'add_floating_ip'
op|'('
string|"'192.168.1.1'"
op|')'
newline|'\n'
name|'floating_ips'
op|'='
name|'vif'
op|'.'
name|'floating_ips'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'floating_ips'
op|','
op|'['
string|"'192.168.1.1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vif_get_labeled_ips
dedent|''
name|'def'
name|'test_vif_get_labeled_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
newline|'\n'
name|'labeled_ips'
op|'='
name|'vif'
op|'.'
name|'labeled_ips'
op|'('
op|')'
newline|'\n'
name|'ip_dict'
op|'='
op|'{'
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'10.10.0.2'"
op|'}'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'10.10.0.3'"
op|'}'
op|')'
op|']'
op|'*'
number|'2'
op|','
nl|'\n'
string|"'network_label'"
op|':'
string|"'public'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'labeled_ips'
op|','
name|'ip_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydrate
dedent|''
name|'def'
name|'test_hydrate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'new_vif'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'address'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'network'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_network'
op|'('
op|')'
op|')'
newline|'\n'
name|'vif'
op|'='
name|'model'
op|'.'
name|'VIF'
op|'.'
name|'hydrate'
op|'('
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
string|"'aa:aa:aa:aa:aa:aa'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vif'
op|'['
string|"'network'"
op|']'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_network'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkInfoTests
dedent|''
dedent|''
name|'class'
name|'NetworkInfoTests'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_create_model
indent|'    '
name|'def'
name|'test_create_model'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ninfo'
op|'='
name|'model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'bb:bb:bb:bb:bb:bb'"
op|'}'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ninfo'
op|'.'
name|'fixed_ips'
op|'('
op|')'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
op|'{'
string|"'address'"
op|':'
string|"'10.10.0.2'"
op|'}'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'10.10.0.3'"
op|'}'
op|')'
op|']'
op|'*'
number|'4'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_floating_ips
dedent|''
name|'def'
name|'test_get_floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'add_floating_ip'
op|'('
string|"'192.168.1.1'"
op|')'
newline|'\n'
name|'ninfo'
op|'='
name|'model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
name|'vif'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'bb:bb:bb:bb:bb:bb'"
op|'}'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ninfo'
op|'.'
name|'floating_ips'
op|'('
op|')'
op|','
op|'['
string|"'192.168.1.1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydrate
dedent|''
name|'def'
name|'test_hydrate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ninfo'
op|'='
name|'model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'bb:bb:bb:bb:bb:bb'"
op|'}'
op|')'
op|']'
op|')'
newline|'\n'
name|'deserialized'
op|'='
name|'model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'ninfo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ninfo'
op|'.'
name|'fixed_ips'
op|'('
op|')'
op|','
nl|'\n'
op|'['
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
op|'{'
string|"'address'"
op|':'
string|"'10.10.0.2'"
op|'}'
op|')'
op|','
nl|'\n'
name|'fake_network_cache_model'
op|'.'
name|'new_ip'
op|'('
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'10.10.0.3'"
op|'}'
op|')'
op|']'
op|'*'
number|'4'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
