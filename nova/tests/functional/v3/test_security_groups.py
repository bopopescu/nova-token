begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'security_group'
name|'import'
name|'neutron_driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'v3'
name|'import'
name|'test_servers'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get
name|'def'
name|'fake_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'nova_group'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'nova_group'
op|'['
string|"'id'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'nova_group'
op|'['
string|"'description'"
op|']'
op|'='
string|"'default'"
newline|'\n'
name|'nova_group'
op|'['
string|"'name'"
op|']'
op|'='
string|"'default'"
newline|'\n'
name|'nova_group'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'openstack'"
newline|'\n'
name|'nova_group'
op|'['
string|"'rules'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
name|'nova_group'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instances_security_groups_bindings
dedent|''
name|'def'
name|'fake_get_instances_security_groups_bindings'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'servers'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'s'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
name|'s'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
op|']'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'test'"
op|'}'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_add_to_instance
dedent|''
name|'def'
name|'fake_add_to_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'security_group_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_remove_from_instance
dedent|''
name|'def'
name|'fake_remove_from_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'security_group_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_list
dedent|''
name|'def'
name|'fake_list'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'names'
op|'='
name|'None'
op|','
name|'ids'
op|'='
name|'None'
op|','
name|'project'
op|'='
name|'None'
op|','
nl|'\n'
name|'search_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'fake_get'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instance_security_groups
dedent|''
name|'def'
name|'fake_get_instance_security_groups'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'fake_get'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_create_security_group
dedent|''
name|'def'
name|'fake_create_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'fake_get'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupsJsonTest
dedent|''
name|'class'
name|'SecurityGroupsJsonTest'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|"'os-security-groups'"
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-access-ips"'
op|']'
newline|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'v2'"
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'SecurityGroupsJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.security_groups.'"
nl|'\n'
string|"'Security_groups'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.keypairs.Keypairs'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.extended_ips.Extended_ips'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.extended_ips_mac.'"
nl|'\n'
string|"'Extended_ips_mac'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'security_group_api'
op|'='
op|'('
string|"'neutron'"
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'SecurityGroupsJsonTest'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|','
string|"'get'"
op|','
name|'fake_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
string|"'get_instances_security_groups_bindings'"
op|','
nl|'\n'
name|'fake_get_instances_security_groups_bindings'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
string|"'add_to_instance'"
op|','
nl|'\n'
name|'fake_add_to_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
string|"'remove_from_instance'"
op|','
nl|'\n'
name|'fake_remove_from_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
string|"'list'"
op|','
nl|'\n'
name|'fake_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
string|"'get_instance_security_groups'"
op|','
nl|'\n'
name|'fake_get_instance_security_groups'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
string|"'create_security_group'"
op|','
nl|'\n'
name|'fake_create_security_group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create
dedent|''
name|'def'
name|'test_server_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_post_server'
op|'('
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_get
dedent|''
name|'def'
name|'test_server_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"'80fe::'"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_detail
dedent|''
name|'def'
name|'test_server_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_post_server'
op|'('
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/detail'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"'80fe::'"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-detail-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_create_subs
dedent|''
name|'def'
name|'_get_create_subs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'group_name'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|'"description"'
op|':'
string|'"default"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_create_security_group
dedent|''
name|'def'
name|'_create_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_create_subs'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-security-groups'"
op|','
nl|'\n'
string|"'security-group-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_group
dedent|''
name|'def'
name|'_add_group'
op|'('
name|'self'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'group_name'"
op|':'
string|"'test'"
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'security-group-add-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_group_create
dedent|''
name|'def'
name|'test_security_group_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_create_security_group'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_create_subs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'security-groups-create-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_groups_list
dedent|''
name|'def'
name|'test_security_groups_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of security groups get list request.'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-security-groups'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'security-groups-list-get-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_groups_get
dedent|''
name|'def'
name|'test_security_groups_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of security groups get request.'
nl|'\n'
indent|'        '
name|'security_group_id'
op|'='
string|"'11111111-1111-1111-1111-111111111111'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-security-groups/%s'"
op|'%'
name|'security_group_id'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'security-groups-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_groups_list_server
dedent|''
name|'def'
name|'test_security_groups_list_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of security groups for a specific server.'
nl|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/os-security-groups'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-security-groups-list-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_groups_add
dedent|''
name|'def'
name|'test_security_groups_add'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_security_group'
op|'('
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_add_group'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_groups_remove
dedent|''
name|'def'
name|'test_security_groups_remove'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_security_group'
op|'('
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_group'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'group_name'"
op|':'
string|"'test'"
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'security-group-remove-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content'
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
