begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'mock'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
DECL|variable|UUID
name|'UUID'
op|'='
string|"'70f6db34-de8d-4fbd-aafb-4065bdfa6114'"
newline|'\n'
DECL|variable|last_add_fixed_ip
name|'last_add_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
DECL|variable|last_remove_fixed_ip
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_add_fixed_ip
name|'def'
name|'compute_api_add_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'last_add_fixed_ip'
newline|'\n'
nl|'\n'
name|'last_add_fixed_ip'
op|'='
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_remove_fixed_ip
dedent|''
name|'def'
name|'compute_api_remove_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'last_remove_fixed_ip'
newline|'\n'
nl|'\n'
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_get
dedent|''
name|'def'
name|'compute_api_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'want_objects'
op|'='
name|'False'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'uuid'
op|'='
name|'instance_id'
newline|'\n'
name|'instance'
op|'.'
name|'id'
op|'='
number|'1'
newline|'\n'
name|'instance'
op|'.'
name|'vm_state'
op|'='
string|"'fake'"
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
string|"'fake'"
newline|'\n'
name|'instance'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'instance'
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
name|'FixedIpTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
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
string|'"add_fixed_ip"'
op|','
nl|'\n'
name|'compute_api_add_fixed_ip'
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
string|'"remove_fixed_ip"'
op|','
nl|'\n'
name|'compute_api_remove_fixed_ip'
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
string|"'get'"
op|','
name|'compute_api_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'self'
op|'.'
name|'_get_app'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_app
dedent|''
name|'def'
name|'_get_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
string|"'os-multinic'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_url
dedent|''
name|'def'
name|'_get_url'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'/v2/fake'"
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip
dedent|''
name|'def'
name|'test_add_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_add_fixed_ip'
newline|'\n'
name|'last_add_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addFixedIp'
op|'='
name|'dict'
op|'('
name|'networkId'
op|'='
string|"'test_net'"
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_add_fixed_ip'
op|','
op|'('
name|'UUID'
op|','
string|"'test_net'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_add_fixed_ip_bad_request
dedent|''
name|'def'
name|'_test_add_fixed_ip_bad_request'
op|'('
name|'self'
op|','
name|'body'
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
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'resp'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip_empty_network_id
dedent|''
name|'def'
name|'test_add_fixed_ip_empty_network_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'addFixedIp'"
op|':'
op|'{'
string|"'network_id'"
op|':'
string|"''"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_add_fixed_ip_bad_request'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip_network_id_bigger_than_36
dedent|''
name|'def'
name|'test_add_fixed_ip_network_id_bigger_than_36'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'addFixedIp'"
op|':'
op|'{'
string|"'network_id'"
op|':'
string|"'a'"
op|'*'
number|'37'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_add_fixed_ip_bad_request'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip_no_network
dedent|''
name|'def'
name|'test_add_fixed_ip_no_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_add_fixed_ip'
newline|'\n'
name|'last_add_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addFixedIp'
op|'='
name|'dict'
op|'('
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_add_fixed_ip'
op|','
op|'('
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'add_fixed_ip'"
op|')'
newline|'\n'
DECL|member|test_add_fixed_ip_no_more_ips_available
name|'def'
name|'test_add_fixed_ip_no_more_ips_available'
op|'('
name|'self'
op|','
name|'mock_add_fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_add_fixed_ip'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'NoMoreFixedIps'
op|'('
name|'net'
op|'='
string|"'netid'"
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addFixedIp'
op|'='
name|'dict'
op|'('
name|'networkId'
op|'='
string|"'test_net'"
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip
dedent|''
name|'def'
name|'test_remove_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_remove_fixed_ip'
newline|'\n'
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeFixedIp'
op|'='
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.10.1'"
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_remove_fixed_ip'
op|','
op|'('
name|'UUID'
op|','
string|"'10.10.10.1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_no_address
dedent|''
name|'def'
name|'test_remove_fixed_ip_no_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_remove_fixed_ip'
newline|'\n'
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeFixedIp'
op|'='
name|'dict'
op|'('
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_remove_fixed_ip'
op|','
op|'('
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_invalid_address
dedent|''
name|'def'
name|'test_remove_fixed_ip_invalid_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'remove_fixed_ip'"
op|':'
op|'{'
string|"'address'"
op|':'
string|"''"
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'resp'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'remove_fixed_ip'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FixedIpNotFoundForSpecificInstance'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'UUID'
op|','
name|'ip'
op|'='
string|"'10.10.10.1'"
op|')'
op|')'
newline|'\n'
DECL|member|test_remove_fixed_ip_not_found
name|'def'
name|'test_remove_fixed_ip_not_found'
op|'('
name|'self'
op|','
name|'_remove_fixed_ip'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'remove_fixed_ip'"
op|':'
op|'{'
string|"'address'"
op|':'
string|"'10.10.10.1'"
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_url'
op|'('
op|')'
op|'+'
string|"'/servers/%s/action'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'resp'
op|'.'
name|'status_int'
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
name|'FixedIpTestV2'
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
name|'flags'
op|'('
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Multinic'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_app
dedent|''
name|'def'
name|'_get_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_invalid_address
dedent|''
name|'def'
name|'test_remove_fixed_ip_invalid_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(cyeoh): This test is disabled for the V2 API because it is'
nl|'\n'
comment|'# has poorer input validation.'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
