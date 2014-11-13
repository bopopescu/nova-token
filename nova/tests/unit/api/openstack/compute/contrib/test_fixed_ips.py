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
name|'as'
name|'fixed_ips_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'fixed_ips'
name|'as'
name|'fixed_ips_v21'
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
name|'i18n'
name|'import'
name|'_'
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
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_network'
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
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'test_network'
op|'.'
name|'fake_network'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
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
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'test_network'
op|'.'
name|'fake_network'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'10.0.0.2'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'virtual_interface_id'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'3'"
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
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'test_network'
op|'.'
name|'fake_network'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'True'
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
op|','
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'address'
op|'=='
string|"'inv.ali.d.ip'"
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid fixed IP Address %s in request"'
op|')'
op|'%'
name|'address'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'FixedIpInvalid'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
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
name|'and'
name|'not'
name|'fixed_ip'
op|'['
string|"'deleted'"
op|']'
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
DECL|class|FixedIpTestV21
dedent|''
name|'class'
name|'FixedIpTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|fixed_ips
indent|'    '
name|'fixed_ips'
op|'='
name|'fixed_ips_v21'
newline|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'/v2/fake/os-fixed-ips'"
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'FixedIpTestV21'
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
name|'self'
op|'.'
name|'fixed_ips'
op|'.'
name|'FixedIPController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assert_equal
dedent|''
name|'def'
name|'_assert_equal'
op|'('
name|'self'
op|','
name|'ret'
op|','
name|'exp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ret'
op|'.'
name|'wsgi_code'
op|','
name|'exp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_reserve_action
dedent|''
name|'def'
name|'_get_reserve_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'reserve'
newline|'\n'
nl|'\n'
DECL|member|_get_unreserve_action
dedent|''
name|'def'
name|'_get_unreserve_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'unreserve'
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
string|"'%s/192.168.1.1'"
op|'%'
name|'self'
op|'.'
name|'url'
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
DECL|member|test_fixed_ips_get_bad_ip_fail
dedent|''
name|'def'
name|'test_fixed_ips_get_bad_ip_fail'
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
string|"'%s/10.0.0.1'"
op|'%'
name|'self'
op|'.'
name|'url'
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
DECL|member|test_fixed_ips_get_invalid_ip_address
dedent|''
name|'def'
name|'test_fixed_ips_get_invalid_ip_address'
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
string|"'%s/inv.ali.d.ip'"
op|'%'
name|'self'
op|'.'
name|'url'
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
name|'HTTPBadRequest'
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
string|"'inv.ali.d.ip'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ips_get_deleted_ip_fail
dedent|''
name|'def'
name|'test_fixed_ips_get_deleted_ip_fail'
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
string|"'%s/10.0.0.2'"
op|'%'
name|'self'
op|'.'
name|'url'
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
string|"'10.0.0.2'"
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
string|"'%s/192.168.1.1/action'"
op|'%'
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_reserve_action'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
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
name|'_assert_equal'
op|'('
name|'result'
name|'or'
name|'action'
op|','
number|'202'
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
string|"'%s/10.0.0.1/action'"
op|'%'
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_reserve_action'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
DECL|member|test_fixed_ip_reserve_invalid_ip_address
dedent|''
name|'def'
name|'test_fixed_ip_reserve_invalid_ip_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'%s/inv.ali.d.ip/action'"
op|'%'
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_reserve_action'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'action'
op|','
name|'req'
op|','
string|"'inv.ali.d.ip'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ip_reserve_deleted_ip
dedent|''
name|'def'
name|'test_fixed_ip_reserve_deleted_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'reserve'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_reserve_action'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'%s/10.0.0.2/action'"
op|'%'
name|'self'
op|'.'
name|'url'
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
name|'action'
op|','
name|'req'
op|','
nl|'\n'
string|"'10.0.0.2'"
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
string|"'%s/192.168.1.1/action'"
op|'%'
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_unreserve_action'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
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
name|'_assert_equal'
op|'('
name|'result'
name|'or'
name|'action'
op|','
number|'202'
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
string|"'%s/10.0.0.1/action'"
op|'%'
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_unreserve_action'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
DECL|member|test_fixed_ip_unreserve_invalid_ip_address
dedent|''
name|'def'
name|'test_fixed_ip_unreserve_invalid_ip_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'%s/inv.ali.d.ip/action'"
op|'%'
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_unreserve_action'
op|'('
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'action'
op|','
name|'req'
op|','
string|"'inv.ali.d.ip'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_ip_unreserve_deleted_ip
dedent|''
name|'def'
name|'test_fixed_ip_unreserve_deleted_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'%s/10.0.0.2/action'"
op|'%'
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_get_unreserve_action'
op|'('
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
name|'action'
op|','
name|'req'
op|','
nl|'\n'
string|"'10.0.0.2'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIpTestV2
dedent|''
dedent|''
name|'class'
name|'FixedIpTestV2'
op|'('
name|'FixedIpTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|fixed_ips
indent|'    '
name|'fixed_ips'
op|'='
name|'fixed_ips_v2'
newline|'\n'
nl|'\n'
DECL|member|_assert_equal
name|'def'
name|'_assert_equal'
op|'('
name|'self'
op|','
name|'ret'
op|','
name|'exp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ret'
op|'.'
name|'status'
op|','
string|"'202 Accepted'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_reserve_action
dedent|''
name|'def'
name|'_get_reserve_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
newline|'\n'
nl|'\n'
DECL|member|_get_unreserve_action
dedent|''
name|'def'
name|'_get_unreserve_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
