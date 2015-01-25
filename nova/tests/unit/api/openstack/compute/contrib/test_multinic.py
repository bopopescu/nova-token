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
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'multinic'
name|'as'
name|'multinic_v2'
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
name|'multinic'
name|'as'
name|'multinic_v21'
newline|'\n'
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
DECL|variable|controller_class
indent|'    '
name|'controller_class'
op|'='
name|'multinic_v21'
newline|'\n'
DECL|variable|validation_error
name|'validation_error'
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
name|'controller'
op|'='
name|'self'
op|'.'
name|'controller_class'
op|'.'
name|'MultinicController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_req'
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
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_add_fixed_ip'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
comment|'# NOTE: on v2.1, http status code is set as wsgi_code of API'
nl|'\n'
comment|'# method instead of status_int in a response object.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'multinic_v21'
op|'.'
name|'MultinicController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_add_fixed_ip'
op|'.'
name|'wsgi_code'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'resp'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_add_fixed_ip'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
nl|'\n'
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
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
name|'self'
op|'.'
name|'_test_add_fixed_ip_bad_request'
op|'('
name|'body'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_add_fixed_ip'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
nl|'\n'
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
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
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_remove_fixed_ip'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
comment|'# NOTE: on v2.1, http status code is set as wsgi_code of API'
nl|'\n'
comment|'# method instead of status_int in a response object.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'multinic_v21'
op|'.'
name|'MultinicController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_remove_fixed_ip'
op|'.'
name|'wsgi_code'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'resp'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_remove_fixed_ip'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
nl|'\n'
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
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
string|"'removeFixedIp'"
op|':'
op|'{'
string|"'address'"
op|':'
string|"''"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_remove_fixed_ip'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
nl|'\n'
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
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
string|"'removeFixedIp'"
op|':'
op|'{'
string|"'address'"
op|':'
string|"'10.10.10.1'"
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
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_remove_fixed_ip'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
nl|'\n'
name|'UUID'
op|','
name|'body'
op|'='
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
DECL|variable|controller_class
indent|'    '
name|'controller_class'
op|'='
name|'multinic_v2'
newline|'\n'
DECL|variable|validation_error
name|'validation_error'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_invalid_address
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
nl|'\n'
nl|'\n'
DECL|class|MultinicPolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'MultinicPolicyEnforcementV21'
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
name|'MultinicPolicyEnforcementV21'
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
name|'multinic_v21'
op|'.'
name|'MultinicController'
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
DECL|member|test_add_fixed_ip_policy_failed
dedent|''
name|'def'
name|'test_add_fixed_ip_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"compute_extension:v3:os-multinic"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
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
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_add_fixed_ip'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'addFixedIp'"
op|':'
op|'{'
string|"'networkId'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|'}'
op|'}'
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
DECL|member|test_remove_fixed_ip_policy_failed
dedent|''
name|'def'
name|'test_remove_fixed_ip_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"compute_extension:v3:os-multinic"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
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
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_remove_fixed_ip'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'removeFixedIp'"
op|':'
op|'{'
string|"'address'"
op|':'
string|'"10.0.0.1"'
op|'}'
op|'}'
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
dedent|''
dedent|''
endmarker|''
end_unit
