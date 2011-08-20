begin_unit
comment|'# Copyright (C) 2011 Midokura KK'
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
name|'json'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
op|'.'
name|'virtual_interfaces'
name|'import'
name|'ServerVirtualInterfaceController'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_get
name|'def'
name|'compute_api_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'virtual_interfaces'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000000'"
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'00-00-00-00-00-00'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
string|"'11111111-1111-1111-1111-11111111111111111'"
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'11-11-11-11-11-11'"
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerVirtualInterfaceTest
dedent|''
name|'class'
name|'ServerVirtualInterfaceTest'
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
name|'ServerVirtualInterfaceTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'ServerVirtualInterfaceController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'compute_api_get'
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
name|'ServerVirtualInterfaceTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_virtual_interfaces_list
dedent|''
name|'def'
name|'test_get_virtual_interfaces_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/servers/1/os-virtual-interfaces'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'virtual_interfaces'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000000'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'00-00-00-00-00-00'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'11111111-1111-1111-1111-11111111111111111'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'11-11-11-11-11-11'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
