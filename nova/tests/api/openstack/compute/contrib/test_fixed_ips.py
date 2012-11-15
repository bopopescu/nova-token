begin_unit
comment|'# Copyright 2012 IBM'
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
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'fixed_ips'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'import'
name|'jsonutils'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_fixed_ips
name|'fake_fixed_ips'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.1.1'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'virtual_interface_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'allocated'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'leased'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'reserved'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.1.2'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'virtual_interface_id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'allocated'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'leased'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'reserved'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_by_address
name|'def'
name|'fake_fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'fixed_ip'
name|'in'
name|'fake_fixed_ips'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fixed_ip'
newline|'\n'
dedent|''
dedent|''
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
nl|'\n'
DECL|function|fake_fixed_ip_get_by_address_detailed
dedent|''
name|'def'
name|'fake_fixed_ip_get_by_address_detailed'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|'"192.168.1.0/24"'
op|'}'
newline|'\n'
name|'for'
name|'fixed_ip'
name|'in'
name|'fake_fixed_ips'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'fixed_ip'
op|','
name|'FakeModel'
op|'('
name|'network'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
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
nl|'\n'
DECL|function|fake_fixed_ip_update
dedent|''
name|'def'
name|'fake_fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fixed_ip'
op|'='
name|'fake_fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'if'
name|'fixed_ip'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
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
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'['
name|'key'
op|']'
op|'='
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeModel
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out for model."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'values'
op|'='
name|'values'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'<FakeModel: %s>'"
op|'%'
name|'self'
op|'.'
name|'values'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_network_get_all
dedent|''
dedent|''
name|'def'
name|'fake_network_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|'"192.168.1.0/24"'
op|'}'
newline|'\n'
name|'return'
op|'['
name|'FakeModel'
op|'('
name|'network'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIpTest
dedent|''
name|'class'
name|'FixedIpTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FixedIpTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"fixed_ip_get_by_address"'
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"fixed_ip_get_by_address_detailed"'
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_address_detailed'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"fixed_ip_update"'
op|','
name|'fake_fixed_ip_update'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'fixed_ips'
op|'.'
name|'FixedIPController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FixedIpTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ips_get
dedent|''
name|'def'
name|'test_fixed_ips_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-fixed-ips/192.168.1.1'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'192.168.1.1'"
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'fixed_ip'"
op|':'
op|'{'
string|"'cidr'"
op|':'
string|"'192.168.1.0/24'"
op|','
nl|'\n'
string|"'hostname'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.1.1'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ips_get_fail
dedent|''
name|'def'
name|'test_fixed_ips_get_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-fixed-ips/10.0.0.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
nl|'\n'
string|"'10.0.0.1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ip_reserve
dedent|''
name|'def'
name|'test_fixed_ip_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_fixed_ips'
op|'['
number|'0'
op|']'
op|'['
string|"'reserved'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'ip_addr'
op|'='
string|"'192.168.1.1'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'reserve'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-fixed-ips/192.168.1.1/action'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
op|'('
name|'req'
op|','
string|'"192.168.1.1"'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'202 Accepted'"
op|','
name|'result'
op|'.'
name|'status'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_fixed_ips'
op|'['
number|'0'
op|']'
op|'['
string|"'reserved'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ip_reserve_bad_ip
dedent|''
name|'def'
name|'test_fixed_ip_reserve_bad_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_addr'
op|'='
string|"'10.0.0.1'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'reserve'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-fixed-ips/10.0.0.1/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
op|','
name|'req'
op|','
nl|'\n'
string|"'10.0.0.1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ip_unreserve
dedent|''
name|'def'
name|'test_fixed_ip_unreserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_fixed_ips'
op|'['
number|'0'
op|']'
op|'['
string|"'reserved'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'ip_addr'
op|'='
string|"'192.168.1.1'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'unreserve'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-fixed-ips/192.168.1.1/action'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
op|'('
name|'req'
op|','
string|'"192.168.1.1"'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'202 Accepted'"
op|','
name|'result'
op|'.'
name|'status'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_fixed_ips'
op|'['
number|'0'
op|']'
op|'['
string|"'reserved'"
op|']'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ip_unreserve_bad_ip
dedent|''
name|'def'
name|'test_fixed_ip_unreserve_bad_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_addr'
op|'='
string|"'10.0.0.1'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'unreserve'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-fixed-ips/10.0.0.1/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
op|','
name|'req'
op|','
nl|'\n'
string|"'10.0.0.1'"
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
