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
name|'netaddr'
newline|'\n'
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
name|'floating_ips_bulk'
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
name|'cfg'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPBulk
name|'class'
name|'FloatingIPBulk'
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
name|'FloatingIPBulk'
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
name|'floating_ips_bulk'
op|'.'
name|'FloatingIPBulkController'
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
name|'FloatingIPBulk'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_floating_ips
dedent|''
name|'def'
name|'_setup_floating_ips'
op|'('
name|'self'
op|','
name|'ip_range'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'floating_ips_bulk_create'"
op|':'
op|'{'
string|"'ip_range'"
op|':'
name|'ip_range'
op|'}'
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
string|"'/v2/fake/os-floating-ips-bulk'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|'"floating_ips_bulk_create"'
op|':'
op|'{'
nl|'\n'
string|"'ip_range'"
op|':'
name|'ip_range'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'CONF'
op|'.'
name|'default_floating_pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'CONF'
op|'.'
name|'public_interface'
op|'}'
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
nl|'\n'
DECL|member|test_create_ips
dedent|''
name|'def'
name|'test_create_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'192.168.1.0/24'"
newline|'\n'
name|'self'
op|'.'
name|'_setup_floating_ips'
op|'('
name|'ip_range'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_ips_pool
dedent|''
name|'def'
name|'test_create_ips_pool'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'10.0.1.0/20'"
newline|'\n'
name|'pool'
op|'='
string|"'a new pool'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'floating_ips_bulk_create'"
op|':'
nl|'\n'
op|'{'
string|"'ip_range'"
op|':'
name|'ip_range'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
op|'}'
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
string|"'/v2/fake/os-floating-ips-bulk'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|'"floating_ips_bulk_create"'
op|':'
op|'{'
nl|'\n'
string|"'ip_range'"
op|':'
name|'ip_range'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'CONF'
op|'.'
name|'public_interface'
op|'}'
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
nl|'\n'
DECL|member|test_list_ips
dedent|''
name|'def'
name|'test_list_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'192.168.1.1/28'"
newline|'\n'
name|'self'
op|'.'
name|'_setup_floating_ips'
op|'('
name|'ip_range'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-floating-ips-bulk'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'ip_info'
op|'='
op|'['
op|'{'
string|"'address'"
op|':'
name|'str'
op|'('
name|'ip_addr'
op|')'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'CONF'
op|'.'
name|'default_floating_pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'CONF'
op|'.'
name|'public_interface'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'None'
op|'}'
nl|'\n'
name|'for'
name|'ip_addr'
name|'in'
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'ip_range'
op|')'
op|'.'
name|'iter_hosts'
op|'('
op|')'
op|']'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'floating_ip_info'"
op|':'
name|'ip_info'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_ips
dedent|''
name|'def'
name|'test_delete_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'192.168.1.0/20'"
newline|'\n'
name|'self'
op|'.'
name|'_setup_floating_ips'
op|'('
name|'ip_range'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'ip_range'"
op|':'
name|'ip_range'
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
string|"'/v2/fake/os-fixed-ips/delete'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
string|'"delete"'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|'"floating_ips_bulk_delete"'
op|':'
name|'ip_range'
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
nl|'\n'
comment|'# Check that the IPs are actually deleted'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-floating-ips-bulk'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'floating_ip_info'"
op|':'
op|'['
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
nl|'\n'
DECL|member|test_create_duplicate_fail
dedent|''
name|'def'
name|'test_create_duplicate_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'192.168.1.0/20'"
newline|'\n'
name|'self'
op|'.'
name|'_setup_floating_ips'
op|'('
name|'ip_range'
op|')'
newline|'\n'
nl|'\n'
name|'ip_range'
op|'='
string|"'192.168.1.0/28'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'floating_ips_bulk_create'"
op|':'
op|'{'
string|"'ip_range'"
op|':'
name|'ip_range'
op|'}'
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
string|"'/v2/fake/os-floating-ips-bulk'"
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
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_bad_cidr_fail
dedent|''
name|'def'
name|'test_create_bad_cidr_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# netaddr can't handle /32 or 31 cidrs"
nl|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'192.168.1.1/32'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'floating_ips_bulk_create'"
op|':'
op|'{'
string|"'ip_range'"
op|':'
name|'ip_range'
op|'}'
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
string|"'/v2/fake/os-floating-ips-bulk'"
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
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_invalid_cidr_fail
dedent|''
name|'def'
name|'test_create_invalid_cidr_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'not a cidr'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'floating_ips_bulk_create'"
op|':'
op|'{'
string|"'ip_range'"
op|':'
name|'ip_range'
op|'}'
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
string|"'/v2/fake/os-floating-ips-bulk'"
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
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
