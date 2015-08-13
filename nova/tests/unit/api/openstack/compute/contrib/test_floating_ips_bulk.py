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
name|'mock'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
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
name|'import'
name|'floating_ips_bulk'
name|'as'
name|'fipbulk_v21'
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
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'floating_ips_bulk'
name|'as'
name|'fipbulk_v2'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
DECL|class|FloatingIPBulkV21
name|'class'
name|'FloatingIPBulkV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|floating_ips_bulk
indent|'    '
name|'floating_ips_bulk'
op|'='
name|'fipbulk_v21'
newline|'\n'
DECL|variable|bad_request
name|'bad_request'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'FloatingIPBulkV21'
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
name|'self'
op|'.'
name|'floating_ips_bulk'
op|'.'
name|'FloatingIPBulkController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
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
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
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
string|"'192.168.1.0/28'"
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
string|"'10.0.1.0/29'"
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
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
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
name|'self'
op|'.'
name|'_test_list_ips'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_list_ips
dedent|''
name|'def'
name|'_test_list_ips'
op|'('
name|'self'
op|','
name|'req'
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
op|','
nl|'\n'
string|"'fixed_ip'"
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
DECL|member|test_list_ips_associated
dedent|''
name|'def'
name|'test_list_ips_associated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_ips_associated'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.FloatingIPList.get_all'"
op|')'
newline|'\n'
DECL|member|_test_list_ips_associated
name|'def'
name|'_test_list_ips_associated'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_uuid'
op|'='
string|'"fake-uuid"'
newline|'\n'
name|'fixed_address'
op|'='
string|'"10.0.0.1"'
newline|'\n'
name|'floating_address'
op|'='
string|'"192.168.0.1"'
newline|'\n'
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'('
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'address'
op|'='
name|'fixed_address'
op|')'
newline|'\n'
name|'floating_ip'
op|'='
name|'objects'
op|'.'
name|'FloatingIP'
op|'('
name|'address'
op|'='
name|'floating_address'
op|','
nl|'\n'
name|'fixed_ip'
op|'='
name|'fixed_ip'
op|','
nl|'\n'
name|'pool'
op|'='
name|'CONF'
op|'.'
name|'default_floating_pool'
op|','
nl|'\n'
name|'interface'
op|'='
name|'CONF'
op|'.'
name|'public_interface'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|')'
newline|'\n'
name|'floating_list'
op|'='
name|'objects'
op|'.'
name|'FloatingIPList'
op|'('
name|'objects'
op|'='
op|'['
name|'floating_ip'
op|']'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'floating_list'
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
name|'floating_address'
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
name|'instance_uuid'
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
name|'fixed_address'
op|'}'
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
DECL|member|test_list_ip_by_host
dedent|''
name|'def'
name|'test_list_ip_by_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_ip_by_host'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_list_ip_by_host
dedent|''
name|'def'
name|'_test_list_ip_by_host'
op|'('
name|'self'
op|','
name|'req'
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
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
string|"'host'"
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
name|'self'
op|'.'
name|'_test_delete_ips'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_delete_ips
dedent|''
name|'def'
name|'_test_delete_ips'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'192.168.1.0/29'"
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
op|'='
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
string|"'192.168.1.0/30'"
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
string|"'192.168.1.0/29'"
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
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
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'bad_request'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPBulkV2
dedent|''
dedent|''
name|'class'
name|'FloatingIPBulkV2'
op|'('
name|'FloatingIPBulkV21'
op|')'
op|':'
newline|'\n'
DECL|variable|floating_ips_bulk
indent|'    '
name|'floating_ips_bulk'
op|'='
name|'fipbulk_v2'
newline|'\n'
DECL|variable|bad_request
name|'bad_request'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
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
name|'FloatingIPBulkV2'
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
name|'non_admin_req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'admin_req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_ips_with_non_admin
dedent|''
name|'def'
name|'test_list_ips_with_non_admin'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AdminRequired'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'self'
op|'.'
name|'non_admin_req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_ip_with_non_admin
dedent|''
name|'def'
name|'test_list_ip_with_non_admin'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AdminRequired'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'non_admin_req'
op|','
string|'"host"'
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
name|'self'
op|'.'
name|'_test_delete_ips'
op|'('
name|'self'
op|'.'
name|'admin_req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_ip_by_host
dedent|''
name|'def'
name|'test_list_ip_by_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_ip_by_host'
op|'('
name|'self'
op|'.'
name|'admin_req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_ips_associated
dedent|''
name|'def'
name|'test_list_ips_associated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_list_ips_associated'
op|'('
name|'self'
op|'.'
name|'admin_req'
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
name|'self'
op|'.'
name|'_test_list_ips'
op|'('
name|'self'
op|'.'
name|'admin_req'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPBulkPolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'FloatingIPBulkPolicyEnforcementV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'FloatingIPBulkPolicyEnforcementV21'
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
name|'fipbulk_v21'
op|'.'
name|'FloatingIPBulkController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_common_policy_check
dedent|''
name|'def'
name|'_common_policy_check'
op|'('
name|'self'
op|','
name|'func'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwarg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-floating-ips-bulk"'
newline|'\n'
name|'rule'
op|'='
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rule'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'func'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwarg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_policy_failed
dedent|''
name|'def'
name|'test_index_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_ip_policy_failed
dedent|''
name|'def'
name|'test_show_ip_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'self'
op|'.'
name|'req'
op|','
string|'"host"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_policy_failed
dedent|''
name|'def'
name|'test_create_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_policy_failed
dedent|''
name|'def'
name|'test_update_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip_range'
op|'='
string|"'192.168.1.0/29'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'ip_range'"
op|':'
name|'ip_range'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
string|'"delete"'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
